"""
Data migration: añade un párrafo de «respuesta rápida» al inicio del contenido
de los 4 artículos SEO existentes.

Objetivo GEO (Generative Engine Optimization): los modelos de IA generativa
(ChatGPT, Perplexity, Gemini) extraen el primer párrafo de la página para
generar snippets. Con una respuesta directa al inicio, el artículo es mucho
más probable de aparecer citado en respuestas de IA.
"""
from django.db import migrations


RESPUESTA_RAPIDA_HTML = """<div style="background:rgba(126,217,87,.06);border-left:4px solid #7ed957;padding:1.2rem 1.5rem;border-radius:0 12px 12px 0;margin-bottom:2.5rem;">
  <p style="color:#7ed957;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.6rem;">Respuesta rápida</p>
  <p style="color:#fff;font-size:1rem;line-height:1.7;margin:0;">{texto}</p>
</div>

"""

RESPUESTAS = {
    "como-hacerse-socio-cannabis-club-espana-guia": (
        "Para hacerse socio de un cannabis social club en España necesitas: "
        "<strong>ser mayor de 18 años</strong>, ser referido por un socio existente, "
        "firmar el reglamento interno y abonar la cuota de membresía. "
        "El proceso se completa en 1–2 visitas y permite el acceso inmediato al club."
    ),
    "cbd-vs-thc-diferencias-efectos-usos-guia": (
        "El <strong>THC</strong> es el cannabinoide psicoactivo del cannabis (produce euforia); "
        "el <strong>CBD</strong> no es psicoactivo y tiene propiedades ansiolíticas y antiinflamatorias. "
        "La diferencia clave: el THC actúa sobre receptores CB1 en el cerebro; "
        "el CBD actúa sobre múltiples receptores. "
        "Usados juntos producen el llamado «efecto séquito», potenciando sus beneficios."
    ),
    "historia-clubes-cannabicos-espana-modelo-asociativo": (
        "Los clubes cannábicos en España surgieron en el País Vasco en 1991 con la ARSECA "
        "y se consolidaron jurídicamente a través de sentencias del Tribunal Supremo "
        "(STS 484/2015). Hoy operan bajo un <strong>modelo de consumo compartido privado "
        "sin ánimo de lucro</strong>: legal en su práctica pero sin regulación explícita."
    ),
    "autocultivo-cannabis-espana-que-dice-la-ley": (
        "El autocultivo de cannabis en España <strong>no es delito penal</strong> si se realiza "
        "en espacio privado, para consumo personal y sin ánimo de lucro (Código Penal, art. 368). "
        "No existe un número legal de plantas fijado por ley, pero los tribunales suelen "
        "considerar 1–3 plantas como consumo propio. "
        "El cultivo visible desde la vía pública sí puede ser sanción administrativa "
        "(Ley Mordaza, art. 36.18)."
    ),
}


def add_respuesta_rapida(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    for slug, texto in RESPUESTAS.items():
        try:
            post = BlogPost.objects.get(slug=slug)
            bloque = RESPUESTA_RAPIDA_HTML.format(texto=texto)
            if 'Respuesta rápida' not in post.contenido:
                post.contenido = bloque + post.contenido
                post.save()
        except BlogPost.DoesNotExist:
            pass


def remove_respuesta_rapida(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    marker_start = '<div style="background:rgba(126,217,87,.06);border-left:4px solid #7ed957'
    marker_end = '</div>\n\n'
    for slug in RESPUESTAS:
        try:
            post = BlogPost.objects.get(slug=slug)
            if post.contenido.startswith(marker_start):
                end_idx = post.contenido.find(marker_end)
                if end_idx != -1:
                    post.contenido = post.contenido[end_idx + len(marker_end):]
                    post.save()
        except BlogPost.DoesNotExist:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_blog_cuatro_articulos_seo'),
    ]

    operations = [
        migrations.RunPython(add_respuesta_rapida, remove_respuesta_rapida),
    ]
