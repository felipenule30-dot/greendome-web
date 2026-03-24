"""
Puebla la BD con el contenido inicial de Green Dome.
Ejecutar: venv/Scripts/python seed_data.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greendome.settings')
django.setup()

from core.models import SiteConfig, Personaje, MundoCard, Actividad, TimelineItem

# ── SiteConfig ──────────────────────────────────────────────────
cfg = SiteConfig.load()
cfg.tagline       = 'Cultura, comunidad y conocimiento.\nSin ánimo de lucro. Sin fronteras.'
cfg.eyebrow       = 'Sevilla · Noviembre 2025'
cfg.cta_texto     = 'Descúbrenos'
cfg.about_title   = 'Una cúpula verde en el corazón de Sevilla'
cfg.about_texto_1 = ('Green Dome nació de la convicción de que el conocimiento y la cultura transforman. '
                     'Somos una asociación cannábica sin ánimo de lucro comprometida con la información '
                     'veraz, el consumo responsable y la construcción de comunidad en Sevilla.')
cfg.about_texto_2 = ('Creemos en el poder del diálogo abierto, la educación y el arte como herramientas '
                     'de cambio social. Aquí no vendemos nada: compartimos historia, ideas y humanidad.')
cfg.stat_1_num    = '2025';  cfg.stat_1_label = 'Fundación'
cfg.stat_2_num    = '100%';  cfg.stat_2_label = 'Sin ánimo de lucro'
cfg.stat_3_num    = 'SVQ';   cfg.stat_3_label = 'Sevilla, España'
cfg.stat_4_num    = '∞';     cfg.stat_4_label = 'Comunidad'
cfg.email         = 'lacupulaverdesv@gmail.com'
cfg.instagram     = 'greendome_svq'
cfg.whatsapp      = '+34600000000'
cfg.whatsapp_msg  = 'Hola Green Dome, quiero información sobre membresía'
cfg.contacto_desc = ('Green Dome es un club privado. Para información sobre membresía '
                     'contáctanos directamente.')
cfg.save()
print('✓ SiteConfig guardado')

# ── Personajes ──────────────────────────────────────────────────
Personaje.objects.all().delete()
personajes = [
    dict(nombre='El Dome', rol='La cara de Green Dome', orden=1,
         tag='Mascota', tag_color='#7ed957', tag_txt='#0d0a14',
         img_filename='mascot-main.png',
         bg_css='radial-gradient(circle at 60% 30%, #5b3080, #2d1a45)',
         bio='Peludo, tranquilo y con esa mirada que lo dice todo sin decir nada. '
             'El Dome es el espíritu del club: va a su ritmo, no le importa el ruido, y siempre está ahí.'),
    dict(nombre='El Fundador', rol='Visionario · Sevilla, 2025', orden=2,
         tag='Fundador', tag_color='#c9a84c', tag_txt='#0d0a14',
         img_filename='char-fundador.png',
         bg_css='radial-gradient(circle at 40% 30%, #1a4a0e, #0d0a14)',
         bio='Manos en los bolsillos, cabeza clara. Soñó con un espacio propio en Sevilla '
             'donde la cultura tuviera un hogar. Y lo construyó desde cero, sin prisa y sin pausa.'),
    dict(nombre='El Sabio', rol='Historia · Memoria viva', orden=3,
         tag='Veterano', tag_color='#5db845', tag_txt='#0d0a14',
         img_filename='char-sabio.png',
         bg_css='radial-gradient(circle at 50% 20%, #3d2565, #1a0d2e)',
         bio='Lleva el bastón pero no necesita apoyo. Lo ha visto todo, lo recuerda todo. '
             'Un dedo levantado suyo vale más que una conferencia entera. Escúchale.'),
    dict(nombre='El Social', rol='Alma del club · Siempre presente', orden=4,
         tag='Comunidad', tag_color='#e05c5c', tag_txt='#ffffff',
         img_filename='char-social.png',
         bg_css='radial-gradient(circle at 50% 30%, #0d3b2e, #061a14)',
         bio='Camiseta de Green Dome, ojos bien abiertos y siempre con una sonrisa. '
             'Es el primero en llegar y el último en irse. El club late porque él late.'),
    dict(nombre='El Zen', rol='Calma · Introspección', orden=5,
         tag='Filosofía', tag_color='#7b68ee', tag_txt='#ffffff',
         img_filename='char-zen.png',
         bg_css='radial-gradient(circle at 50% 30%, #2d1a45, #0d0a14)',
         bio='Ojos entrecerrados, respiración lenta. Para él el club es un espacio de reflexión. '
             'Habla poco, piensa mucho y cuando abre la boca merece la pena escuchar.'),
    dict(nombre='El Artesano', rol='Precisión · Ritual', orden=6,
         tag='Oficio', tag_color='#c9a84c', tag_txt='#0d0a14',
         img_filename='char-artesano.png',
         bg_css='radial-gradient(circle at 50% 20%, #0d3b2e, #061a14)',
         bio='Cada movimiento tiene su por qué. Metódico, cuidadoso, experto. '
             'Para él todo es un ritual que merece atención y respeto. El arte está en los detalles.'),
]
for d in personajes:
    Personaje.objects.create(**d)
print(f'✓ {len(personajes)} Personajes creados')

# ── MundoCards ──────────────────────────────────────────────────
MundoCard.objects.all().delete()
cards = [
    dict(icono='📜', titulo='Historia del Cannabis', orden=1, color_class='color-1',
         descripcion='Miles de años de historia humana entrelazada con esta planta. Desde las civilizaciones antiguas hasta el siglo XXI, exploramos el recorrido cultural y científico del cannabis.'),
    dict(icono='🏛️', titulo='Clubes en España', orden=2, color_class='color-2',
         descripcion='El modelo asociativo español es único en el mundo. Conoce la historia legal, los hitos y la evolución del movimiento de asociaciones cannábicas en nuestro país.'),
    dict(icono='🌱', titulo='Consumo Responsable', orden=3, color_class='color-3',
         descripcion='La información salva vidas. Promovemos el consumo consciente, la reducción de riesgos y el autocuidado como pilares de una comunidad sana.'),
    dict(icono='🎨', titulo='Arte y Cultura', orden=4, color_class='color-4',
         descripcion='Música, pintura, literatura, cine. El cannabis ha inspirado décadas de creación. Celebramos el arte como expresión libre de nuestra comunidad.'),
    dict(icono='🤝', titulo='Comunidad', orden=5, color_class='color-5',
         descripcion='Green Dome son sus personas. Eventos, charlas, talleres y encuentros que forjan lazos reales en un espacio seguro y respetuoso en Sevilla.'),
]
for d in cards:
    MundoCard.objects.create(**d)
print(f'✓ {len(cards)} MundoCards creadas')

# ── Actividades ─────────────────────────────────────────────────
Actividad.objects.all().delete()
actividades = [
    dict(orden=1, titulo='Charlas y talleres educativos',
         descripcion='Sesiones abiertas sobre historia, ciencia, legislación y consumo responsable del cannabis.'),
    dict(orden=2, titulo='Eventos culturales',
         descripcion='Música en vivo, exposiciones de arte, proyecciones de cine y encuentros literarios en Sevilla.'),
    dict(orden=3, titulo='Información y reducción de riesgos',
         descripcion='Materiales informativos, guías de consumo consciente y atención personalizada a los socios.'),
    dict(orden=4, titulo='Defensa del modelo asociativo',
         descripcion='Participación activa en el debate social y legal sobre el modelo cannábico en España.'),
    dict(orden=5, titulo='Construcción de comunidad',
         descripcion='Espacio seguro, inclusivo y respetuoso donde las personas se conectan con un propósito común.'),
]
for d in actividades:
    Actividad.objects.create(**d)
print(f'✓ {len(actividades)} Actividades creadas')

# ── Timeline ────────────────────────────────────────────────────
TimelineItem.objects.all().delete()
timeline = [
    dict(orden=1, año='2700 a.C.', destacado=False,
         descripcion='Primer uso medicinal documentado en China por el Emperador Shennong.'),
    dict(orden=2, año='1961', destacado=False,
         descripcion='Convención única sobre estupefacientes de la ONU. El cannabis queda bajo control internacional.'),
    dict(orden=3, año='1991', destacado=False,
         descripcion='California aprueba el uso medicinal. Primer estado en el mundo.'),
    dict(orden=4, año='2001', destacado=False,
         descripcion='El Tribunal Supremo español consolida el modelo asociativo como espacio legal.'),
    dict(orden=5, año='2013', destacado=False,
         descripcion='Uruguay se convierte en el primer país del mundo en legalizar el cannabis.'),
    dict(orden=6, año='Nov 2025', destacado=True,
         descripcion='Nace Green Dome en Sevilla. Una cúpula verde para la comunidad sevillana.'),
    dict(orden=7, año='Hoy', destacado=False,
         descripcion='Creciendo. Construyendo comunidad, cultura y conocimiento desde el corazón de Andalucía.'),
]
for d in timeline:
    TimelineItem.objects.create(**d)
print(f'✓ {len(timeline)} Hitos del timeline creados')

print('\n✅ Datos iniciales cargados correctamente.')
print('   Entra en /admin para editar todo el contenido.')
