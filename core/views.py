import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Member, SiteConfig, Personaje, MundoCard, Actividad, TimelineItem, BlogPost, BlogImage, FAQItem, ClubPhoto


def age_gate(request):
    """Pantalla de verificación de edad — acceso directo a /age-gate/."""
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
        'config':      SiteConfig.load(),
        'personajes':  Personaje.objects.filter(activo=True),
        'cards':       MundoCard.objects.filter(activo=True),
        'actividades': Actividad.objects.filter(activo=True),
        'timeline':    TimelineItem.objects.all(),
    }
    return render(request, 'core/home.html', ctx)


# ── Secciones con slug propio ─────────────────────────────────────

def seccion_sobre_nosotros(request):
    """Página /cannabis-club-sevilla/ — sección Quiénes Somos."""
    ctx = {
        'config':      SiteConfig.load(),
        'actividades': Actividad.objects.filter(activo=True),
        'timeline':    TimelineItem.objects.all(),
    }
    return render(request, 'core/seccion_sobre_nosotros.html', ctx)


def seccion_que_hacemos(request):
    """Página /que-hacemos/ — sección Qué Hacemos."""
    ctx = {
        'config':      SiteConfig.load(),
        'actividades': Actividad.objects.filter(activo=True),
    }
    return render(request, 'core/seccion_que_hacemos.html', ctx)


def seccion_nuestro_mundo(request):
    """Página /nuestro-mundo/ — sección Nuestro Mundo."""
    ctx = {
        'config': SiteConfig.load(),
        'cards':  MundoCard.objects.filter(activo=True),
    }
    return render(request, 'core/seccion_nuestro_mundo.html', ctx)


def seccion_contacto(request):
    """Página /contacto/ — sección Contacto."""
    ctx = {'config': SiteConfig.load()}
    return render(request, 'core/seccion_contacto.html', ctx)


# ── FAQ ───────────────────────────────────────────────────────────

def faq(request):
    """Página /faq/ — preguntas frecuentes completas."""
    ctx = {
        'config': SiteConfig.load(),
        'faqs':   FAQItem.objects.filter(activo=True),
    }
    return render(request, 'core/faq.html', ctx)


# ── Blog ──────────────────────────────────────────────────────────

def blog_list(request):
    """Página /blog/ — listado de artículos."""
    ctx = {
        'config': SiteConfig.load(),
        'posts':  BlogPost.objects.filter(publicado=True),
    }
    return render(request, 'core/blog_list.html', ctx)


def blog_detail(request, slug):
    """Página /blog/<slug>/ — artículo individual."""
    post     = get_object_or_404(BlogPost, slug=slug, publicado=True)
    recientes = BlogPost.objects.filter(publicado=True).exclude(pk=post.pk)[:3]
    imagenes  = post.imagenes.all()
    ctx = {
        'config':   SiteConfig.load(),
        'post':     post,
        'recientes': recientes,
        'imagenes': imagenes,
    }
    return render(request, 'core/blog_detail.html', ctx)


# ── Cannabis Club Seville (English page) ──────────────────────────

def seccion_seville(request):
    """Página /cannabis-club-seville/ — versión en inglés."""
    ctx = {
        'config': SiteConfig.load(),
        'posts':  BlogPost.objects.filter(publicado=True, idioma='en')[:5],
    }
    return render(request, 'core/seccion_seville.html', ctx)


# ── The Club — galería de fotos ────────────────────────────────────

def the_club(request):
    """Página /the-club/ — galería de fotos del interior."""
    ctx = {
        'config': SiteConfig.load(),
        'fotos':  ClubPhoto.objects.filter(activo=True),
    }
    return render(request, 'core/the_club.html', ctx)


# ── Registro miembros ─────────────────────────────────────────────

@require_POST
def register_member(request):
    """Guarda un nuevo miembro desde el modal de registro."""
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        data = request.POST

    nombre = (data.get('nombre') or '').strip()
    email  = (data.get('email')  or '').strip().lower()

    if not nombre or not email:
        return JsonResponse({'ok': False, 'error': 'Nombre y email son requeridos.'}, status=400)

    _, created = Member.objects.get_or_create(
        email=email,
        defaults={'nombre': nombre, 'origen': 'age_gate'},
    )

    request.session['member_registered'] = True
    return JsonResponse({'ok': True, 'created': created})
