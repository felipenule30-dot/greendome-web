import re
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Member, SiteConfig, Personaje, MundoCard, Actividad, TimelineItem

_BOT_RE = re.compile(
    r'(googlebot|bingbot|slurp|duckduckbot|baiduspider|yandexbot|facebot|twitterbot|linkedinbot|applebot)',
    re.IGNORECASE,
)

def _is_bot(request):
    ua = request.META.get('HTTP_USER_AGENT', '')
    return bool(_BOT_RE.search(ua))


def age_gate(request):
    """Pantalla de verificación de edad (+18)."""
    if request.session.get('age_verified') or _is_bot(request):
        return redirect('home')
    return render(request, 'core/age_gate.html')


def age_gate_confirm(request):
    """Procesa la confirmación de edad."""
    if request.method == 'POST':
        confirmed = request.POST.get('confirmed') == 'yes'
        if confirmed:
            request.session['age_verified'] = True
            return JsonResponse({'ok': True})
        return JsonResponse({'ok': False, 'redirect': '/acceso-denegado/'})
    return redirect('age_gate')


def access_denied(request):
    return render(request, 'core/access_denied.html', status=403)


def home(request):
    """Página principal — age gate gestionado por JavaScript en el cliente."""
    ctx = {
        'config':     SiteConfig.load(),
        'personajes': Personaje.objects.filter(activo=True),
        'cards':      MundoCard.objects.filter(activo=True),
        'actividades':Actividad.objects.filter(activo=True),
        'timeline':   TimelineItem.objects.all(),
    }
    return render(request, 'core/home.html', ctx)


@require_POST
def register_member(request):
    """Guarda un nuevo miembro desde el modal de registro."""
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        data = request.POST

    nombre = (data.get('nombre') or '').strip()
    email = (data.get('email') or '').strip().lower()

    if not nombre or not email:
        return JsonResponse({'ok': False, 'error': 'Nombre y email son requeridos.'}, status=400)

    _, created = Member.objects.get_or_create(
        email=email,
        defaults={'nombre': nombre, 'origen': 'age_gate'},
    )

    request.session['member_registered'] = True
    return JsonResponse({'ok': True, 'created': created})
