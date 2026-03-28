"""
Corrige las tildes de los textos de SiteConfig en la base de datos.
Ejecutar en el servidor:
    cd /root/greendome-web && source venv/bin/activate
    python3 fix_siteconfig_tildes.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greendome.settings')
django.setup()

from core.models import SiteConfig

cfg = SiteConfig.load()

cfg.about_title   = 'Una cúpula verde en el corazón de Sevilla'
cfg.about_texto_1 = (
    'Green Dome nació de la convicción de que el conocimiento y la cultura transforman. '
    'Somos una asociación cannábica sin ánimo de lucro comprometida con la información '
    'veraz, el consumo responsable y la construcción de comunidad en Sevilla.'
)
cfg.about_texto_2 = (
    'Creemos en el poder del diálogo abierto, la educación y el arte como herramientas '
    'de cambio social. Aquí no vendemos nada: compartimos historia, ideas y humanidad.'
)
cfg.tagline        = 'Cultura, comunidad y conocimiento.\nSin ánimo de lucro. Sin fronteras.'
cfg.eyebrow        = 'Sevilla · Noviembre 2025'
cfg.stat_1_label   = 'Fundación'
cfg.stat_2_label   = 'Sin ánimo de lucro'
cfg.stat_3_label   = 'Sevilla, España'
cfg.whatsapp_msg   = 'Hola Green Dome, quiero información sobre membresía'
cfg.contacto_desc  = (
    'Green Dome es un club privado. Para información sobre membresía '
    'contáctanos directamente.'
)
cfg.cta_texto      = 'Descúbrenos'

cfg.save()
print('✓ SiteConfig: textos corregidos con tildes correctas.')
print(f'  about_title:   {cfg.about_title}')
print(f'  tagline:       {cfg.tagline[:40]}...')
