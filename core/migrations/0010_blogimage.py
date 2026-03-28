from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_blog_post_prohibicion_cannabis'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(
                    upload_to='blog/',
                    verbose_name='Imagen',
                    help_text='Sube la imagen. Una vez guardada, copia su URL y p\xe9gala en el contenido del art\xedculo.',
                )),
                ('descripcion', models.CharField(
                    blank=True, max_length=200,
                    verbose_name='Descripci\xf3n / Alt text',
                    help_text='Descripci\xf3n de la imagen para accesibilidad y SEO.',
                )),
                ('orden', models.PositiveSmallIntegerField(default=0)),
                ('post', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='imagenes',
                    to='core.blogpost',
                    verbose_name='Art\xedculo',
                )),
            ],
            options={
                'verbose_name': 'Imagen del art\xedculo',
                'verbose_name_plural': 'Im\xe1genes del art\xedculo',
                'ordering': ['orden'],
            },
        ),
    ]
