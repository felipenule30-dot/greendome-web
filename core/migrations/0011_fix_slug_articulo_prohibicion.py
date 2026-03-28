"""
Corrige el slug del artículo de la prohibición del cannabis:
elimina el carácter acentuado 'ó' que Django's <slug:slug> no acepta (solo ASCII).
"""
from django.db import migrations

SLUG_VIEJO = "como-eeuu-criminalizó-el-cannabis-para-perseguir-a-las-minorias"
SLUG_NUEVO = "como-eeuu-criminalizo-el-cannabis-para-perseguir-a-las-minorias"


def fix_slug(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    BlogPost.objects.filter(slug=SLUG_VIEJO).update(slug=SLUG_NUEVO)


def revert_slug(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    BlogPost.objects.filter(slug=SLUG_NUEVO).update(slug=SLUG_VIEJO)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_blogimage'),
    ]

    operations = [
        migrations.RunPython(fix_slug, revert_slug),
    ]
