from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

from core.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}


def google_verification(request):
    return HttpResponse(
        'google-site-verification: google5bc53e07450d12e0.html',
        content_type='text/html'
    )


def robots_txt(request):
    lines = [
        'User-agent: *',
        'Disallow: /admin/',
        'Disallow: /api/',
        f'Sitemap: https://{settings.META_SITE_DOMAIN}/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines) + '\n', content_type='text/plain')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt),
    path('google5bc53e07450d12e0.html', google_verification),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
