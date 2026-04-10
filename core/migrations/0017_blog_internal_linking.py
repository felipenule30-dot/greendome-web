"""
Data migration: añade internal linking contextual entre los 4 artículos del blog.

Objetivo SEO: los internal links distribuyen PageRank entre artículos,
aumentan el tiempo en sitio y ayudan a Google a entender la estructura temática.

Links añadidos:
  Artículo 1 (cómo hacerse socio)  → Historia clubs + Autocultivo
  Artículo 2 (CBD vs THC)          → Cómo hacerse socio
  Artículo 3 (historia clubs)      → Cómo hacerse socio + Autocultivo
  Artículo 4 (autocultivo)         → Historia clubs + Cómo hacerse socio
"""
from django.db import migrations

BASE_URL = "https://greendome.net/blog"

LINK_BLOCK = """
<div style="background:rgba(126,217,87,.04);border:1px solid rgba(126,217,87,.15);border-radius:16px;padding:1.5rem 1.8rem;margin:3rem 0;">
  <p style="color:#7ed957;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:1rem;">Artículos relacionados</p>
  <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.6rem;">
    {items}
  </ul>
</div>
"""

LINK_ITEM = (
    '<li>'
    '<a href="{url}" style="color:#aaa;text-decoration:none;font-size:.95rem;'
    'display:flex;align-items:center;gap:.5rem;transition:color .2s;" '
    'onmouseover="this.style.color=\'#7ed957\'" onmouseout="this.style.color=\'#aaa\'">'
    '<span style="color:#7ed957;font-size:.8rem;">→</span> {titulo}'
    '</a>'
    '</li>'
)

ARTICLES = {
    "como-hacerse-socio-cannabis-club-espana-guia": [
        ("/historia-clubes-cannabicos-espana-modelo-asociativo/",
         "Historia de los clubes cannábicos en España: del underground a la legalidad"),
        ("/autocultivo-cannabis-espana-que-dice-la-ley/",
         "Autocultivo de cannabis en España: qué dice la ley y qué dice la realidad"),
    ],
    "cbd-vs-thc-diferencias-efectos-usos-guia": [
        ("/como-hacerse-socio-cannabis-club-espana-guia/",
         "Cómo hacerse socio de un cannabis club en España: guía paso a paso"),
        ("/historia-clubes-cannabicos-espana-modelo-asociativo/",
         "Historia de los clubes cannábicos en España: del underground a la legalidad"),
    ],
    "historia-clubes-cannabicos-espana-modelo-asociativo": [
        ("/como-hacerse-socio-cannabis-club-espana-guia/",
         "Cómo hacerse socio de un cannabis club en España: guía paso a paso"),
        ("/autocultivo-cannabis-espana-que-dice-la-ley/",
         "Autocultivo de cannabis en España: qué dice la ley y qué dice la realidad"),
    ],
    "autocultivo-cannabis-espana-que-dice-la-ley": [
        ("/historia-clubes-cannabicos-espana-modelo-asociativo/",
         "Historia de los clubes cannábicos en España: del underground a la legalidad"),
        ("/como-hacerse-socio-cannabis-club-espana-guia/",
         "Cómo hacerse socio de un cannabis club en España: guía paso a paso"),
    ],
}


def build_link_block(links):
    items = "\n    ".join(
        LINK_ITEM.format(url=f"{BASE_URL}{slug}", titulo=titulo)
        for slug, titulo in links
    )
    return LINK_BLOCK.format(items=items)


def add_internal_links(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    marker = 'Artículos relacionados'

    for slug, links in ARTICLES.items():
        try:
            post = BlogPost.objects.get(slug=slug)
            if marker not in post.contenido:
                block = build_link_block(links)
                # Insertamos antes del <hr> final si existe, si no al final
                if '<hr>' in post.contenido:
                    post.contenido = post.contenido.replace('<hr>', block + '\n<hr>', 1)
                else:
                    post.contenido += block
                post.save()
        except BlogPost.DoesNotExist:
            pass


def remove_internal_links(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    marker_start = '\n<div style="background:rgba(126,217,87,.04);border:1px solid rgba(126,217,87,.15)'
    for slug in ARTICLES:
        try:
            post = BlogPost.objects.get(slug=slug)
            if 'Artículos relacionados' in post.contenido:
                start = post.contenido.find(marker_start)
                if start != -1:
                    end = post.contenido.find('</div>', start)
                    if end != -1:
                        post.contenido = post.contenido[:start] + post.contenido[end + 6:]
                        post.save()
        except BlogPost.DoesNotExist:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_merge_20260410_1240'),
    ]

    operations = [
        migrations.RunPython(add_internal_links, remove_internal_links),
    ]
