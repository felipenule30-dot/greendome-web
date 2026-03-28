from django.urls import path
from . import views

urlpatterns = [
    # ── Home ─────────────────────────────────────────────────────
    path('', views.home, name='home'),

    # ── Secciones con slug propio (SEO) ──────────────────────────
    path('cannabis-club-sevilla/', views.seccion_sobre_nosotros, name='seccion_sobre_nosotros'),
    path('que-hacemos/',           views.seccion_que_hacemos,    name='seccion_que_hacemos'),
    path('nuestro-mundo/',         views.seccion_nuestro_mundo,  name='seccion_nuestro_mundo'),
    path('contacto/',              views.seccion_contacto,       name='seccion_contacto'),

    # ── FAQ ──────────────────────────────────────────────────────
    path('faq/',                   views.faq,                    name='faq'),

    # ── Blog ─────────────────────────────────────────────────────
    path('blog/',                  views.blog_list,              name='blog_list'),
    path('blog/<slug:slug>/',      views.blog_detail,            name='blog_detail'),

    # ── Age gate ─────────────────────────────────────────────────
    path('age-gate/',              views.age_gate,               name='age_gate'),
    path('age-gate/confirm/',      views.age_gate_confirm,       name='age_gate_confirm'),
    path('acceso-denegado/',       views.access_denied,          name='access_denied'),

    # ── API ───────────────────────────────────────────────────────
    path('api/register/',          views.register_member,        name='register_member'),
]
