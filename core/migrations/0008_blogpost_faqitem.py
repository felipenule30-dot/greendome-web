from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_siteconfig_hero_bg'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=300, verbose_name='Pregunta')),
                ('respuesta', models.TextField(verbose_name='Respuesta')),
                ('orden', models.PositiveSmallIntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Pregunta frecuente',
                'verbose_name_plural': 'FAQ \u2014 Preguntas frecuentes',
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='T\xedtulo')),
                ('slug', models.SlugField(max_length=220, unique=True, help_text='URL amigable (auto-generado si se deja vac\xedo). Ej: cannabis-club-sevilla-guia')),
                ('resumen', models.TextField(verbose_name='Resumen / Intro', help_text='1-2 frases que aparecen en la lista del blog y en la meta description.')),
                ('contenido', models.TextField(verbose_name='Contenido', help_text='HTML o texto plano. Puedes usar etiquetas <h2>, <p>, <ul>, etc.')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Imagen de portada', help_text='Recomendado: 1200x630px JPG (proporci\xf3n OG).')),
                ('autor', models.CharField(default='Green Dome', max_length=100, verbose_name='Autor')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado', help_text='Solo los art\xedculos publicados son visibles en la web.')),
                ('fecha_pub', models.DateTimeField(verbose_name='Fecha de publicaci\xf3n', help_text='Fecha que se muestra en el art\xedculo y en el sitemap.')),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Art\xedculo del blog',
                'verbose_name_plural': 'Blog \u2014 Art\xedculos',
                'ordering': ['-fecha_pub'],
            },
        ),
    ]
