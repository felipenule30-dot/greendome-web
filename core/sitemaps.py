from datetime import datetime, timezone
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost

# Fecha de la última actualización significativa del sitio
_SITE_UPDATED = datetime(2026, 3, 29, tzinfo=timezone.utc)


class StaticViewSitemap(Sitemap):
    """Páginas estáticas + secciones con slug propio."""
    protocol = 'https'

    # (name, priority, changefreq)
    PAGES = [
        ('home',                   1.0, 'weekly'),
        ('faq',                    0.9, 'monthly'),
        ('blog_list',              0.9, 'daily'),
        ('seccion_sobre_nosotros', 0.8, 'monthly'),
        ('seccion_que_hacemos',    0.8, 'monthly'),
        ('seccion_nuestro_mundo',  0.8, 'monthly'),
        ('seccion_contacto',       0.8, 'monthly'),
        ('seccion_seville',        0.9, 'weekly'),
        ('the_club',               0.8, 'weekly'),
    ]

    def items(self):
        return self.PAGES

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]

    def changefreq(self, item):
        return item[2]

    def lastmod(self, item):
        return _SITE_UPDATED


class BlogSitemap(Sitemap):
    """Artículos del blog publicados."""
    protocol   = 'https'
    changefreq = 'monthly'
    priority   = 0.7

    def items(self):
        return BlogPost.objects.filter(publicado=True)

    def lastmod(self, obj):
        return obj.actualizado

    def location(self, obj):
        return obj.get_absolute_url()
