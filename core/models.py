from django.db import models


# ── Contenido editable del sitio ─────────────────────────────────


class SiteConfig(models.Model):
    """Singleton: configuración general y textos de la web."""
    # ── Logos ─────────────────────────────────────────────────────
    logo            = models.ImageField(
        upload_to='branding/', blank=True, null=True,
        verbose_name='Logo Hero (centro)',
        help_text='Logo GRANDE del centro del hero y footer. PNG recomendado (con texto "GREEN DOME" incluido). Transparente o con fondo.'
    )
    logo_nav        = models.ImageField(
        upload_to='branding/', blank=True, null=True,
        verbose_name='Logo Nav (esquina superior)',
        help_text='Logo PEQUEÑO de la esquina superior izquierda. Puede ser solo el icono/arco sin texto. PNG con fondo transparente.'
    )
    # ── Hero ──────────────────────────────────────────────────────
    hero_bg         = models.ImageField(
        upload_to='branding/', blank=True, null=True,
        verbose_name='Fondo del Hero',
        help_text='Imagen o GIF de fondo del hero. Si no subes nada se usa el fondo oscuro por defecto. Recomendado: JPG/PNG ancho (1920x1080 mínimo).'
    )
    tagline         = models.CharField(max_length=250, default='Cultura, comunidad y conocimiento.')
    eyebrow         = models.CharField(max_length=100, default='Sevilla · Noviembre 2025', help_text='Texto pequeño sobre el título del hero')
    cta_texto       = models.CharField(max_length=60,  default='Descúbrenos', help_text='Botón del hero')
    # ── Quiénes somos ─────────────────────────────────────────────
    about_title     = models.CharField(max_length=150, default='Una cúpula verde en el corazón de Sevilla')
    about_texto_1   = models.TextField(default='Green Dome nació de la convicción de que el conocimiento y la cultura transforman.')
    about_texto_2   = models.TextField(default='Creemos en el poder del diálogo abierto, la educación y el arte como herramientas de cambio social.')
    stat_1_num      = models.CharField(max_length=20, default='2025')
    stat_1_label    = models.CharField(max_length=50, default='Fundación')
    stat_2_num      = models.CharField(max_length=20, default='100%')
    stat_2_label    = models.CharField(max_length=50, default='Sin ánimo de lucro')
    stat_3_num      = models.CharField(max_length=20, default='SVQ')
    stat_3_label    = models.CharField(max_length=50, default='Sevilla, España')
    stat_4_num      = models.CharField(max_length=20, default='∞')
    stat_4_label    = models.CharField(max_length=50, default='Comunidad')
    # ── Contacto y redes ──────────────────────────────────────────
    email           = models.EmailField(default='lacupulaverdesv@gmail.com')
    instagram       = models.CharField(max_length=60, default='greendome_svq')
    whatsapp        = models.CharField(max_length=20, default='+34600000000', help_text='Formato: +34XXXXXXXXX')
    whatsapp_msg    = models.CharField(max_length=200, default='Hola Green Dome, quiero información sobre membresía')
    contacto_desc   = models.TextField(default='Green Dome es un club privado. Para información sobre membresía contáctanos directamente.')
    # ── Google Maps ───────────────────────────────────────────────
    maps_embed_url  = models.URLField(
        max_length=1000, blank=True,
        default='https://maps.google.com/maps?q=37.3806919,-5.9812485&t=&z=17&ie=UTF8&iwloc=&output=embed',
        help_text=(
            'URL del iframe embed. Cómo obtenerla: '
            'Google Maps → busca "Asociación Cannábica Green Dome Sevilla" → '
            'Compartir → "Insertar un mapa" → copia SOLO la URL del src=""'
        )
    )
    maps_directions_url = models.URLField(
        max_length=1000, blank=True,
        default='https://www.google.com/maps/place/Asociaci%C3%B3n+Cann%C3%A1bica+Green+Dome/@37.3806919,-5.9812485,17z',
        help_text='URL de Google Maps para "Cómo llegar". Abre la ficha de Green Dome en Google Maps y copia la URL del navegador.'
    )
    maps_review_url = models.URLField(
        max_length=1000, blank=True, default='',
        help_text='URL para dejar reseña en Google. En Google Maps → tu ficha → "Obtener enlace para compartir reseñas" → pega aquí.'
    )
    # ── SEO dinámico (actualizado por optimize_seo) ───────────────
    seo_title       = models.CharField(max_length=200, blank=True, default='',
        help_text='Sobreescribe el title tag. Se actualiza automáticamente cada día con optimize_seo.')
    seo_description = models.TextField(blank=True, default='',
        help_text='Sobreescribe la meta description. Actualizado automáticamente.')
    seo_keywords    = models.TextField(blank=True, default='',
        help_text='Keywords para meta keywords. Actualizado automáticamente.')
    seo_faq_json    = models.TextField(blank=True, default='',
        help_text='JSON-LD FAQPage generado por optimize_seo. No edites manualmente.')
    seo_updated_at  = models.DateTimeField(null=True, blank=True,
        help_text='Última actualización SEO automática.')

    class Meta:
        verbose_name = 'Configuración del sitio'
        verbose_name_plural = 'Configuración del sitio'

    def __str__(self):
        return 'Configuración general'

    def save(self, *args, **kwargs):
        self.pk = 1  # singleton
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Personaje(models.Model):
    """Personajes de la sección scroll horizontal."""
    nombre      = models.CharField(max_length=100)
    rol         = models.CharField(max_length=150)
    bio         = models.TextField()
    tag         = models.CharField(max_length=30, help_text='Etiqueta de color (ej: Mascota, Fundador…)')
    tag_color   = models.CharField(max_length=7,  default='#7ed957', help_text='Color hex del tag')
    tag_txt     = models.CharField(max_length=7,  default='#0d0a14', help_text='Color hex del texto del tag')
    imagen      = models.ImageField(upload_to='personajes/', blank=True, null=True, help_text='PNG con fondo transparente o de color')
    img_filename= models.CharField(max_length=100, blank=True, help_text='Nombre de archivo en static/img/ (ej: mascot-main.png). Se usa si no hay imagen subida.')
    bg_css      = models.CharField(max_length=200, default='radial-gradient(circle at 60% 30%, #5b3080, #2d1a45)', help_text='CSS background de la tarjeta de imagen')
    orden       = models.PositiveSmallIntegerField(default=0)
    activo      = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Personaje'
        verbose_name_plural = 'Personajes'
        ordering = ['orden']

    def __str__(self):
        return self.nombre


class MundoCard(models.Model):
    """Cards de la sección Nuestro Mundo."""
    COLOR_CHOICES = [(f'color-{i}', f'Color {i}') for i in range(1, 7)]
    icono       = models.CharField(max_length=10, default='🌿')
    titulo      = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen      = models.ImageField(
        upload_to='mundo/', blank=True, null=True,
        help_text='GIF o imagen para la card. Si subes imagen se muestra en lugar del emoji.'
    )
    color_class = models.CharField(max_length=10, choices=COLOR_CHOICES, default='color-1')
    orden       = models.PositiveSmallIntegerField(default=0)
    activo      = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Card "Nuestro Mundo"'
        verbose_name_plural = 'Cards "Nuestro Mundo"'
        ordering = ['orden']

    def __str__(self):
        return self.titulo


class Actividad(models.Model):
    """Lista de actividades en la sección Qué Hacemos."""
    titulo      = models.CharField(max_length=150)
    descripcion = models.TextField()
    orden       = models.PositiveSmallIntegerField(default=0)
    activo      = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['orden']

    def __str__(self):
        return self.titulo


class TimelineItem(models.Model):
    """Hitos del timeline histórico."""
    año         = models.CharField(max_length=20, verbose_name='Año / Fecha')
    descripcion = models.TextField()
    destacado   = models.BooleanField(default=False, help_text='Marcar si es el hito de Green Dome')
    orden       = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Hito del timeline'
        verbose_name_plural = 'Timeline histórico'
        ordering = ['orden']

    def __str__(self):
        return f'{self.año} — {self.descripcion[:50]}'


# ── Blog ─────────────────────────────────────────────────────────


class BlogPost(models.Model):
    """Artículos del blog de Green Dome."""
    titulo      = models.CharField(max_length=200, verbose_name='Título')
    slug        = models.SlugField(max_length=220, unique=True,
                    help_text='URL amigable (auto-generado si se deja vacío). Ej: cannabis-club-sevilla-guia')
    resumen     = models.TextField(verbose_name='Resumen / Intro',
                    help_text='1-2 frases que aparecen en la lista del blog y en la meta description.')
    contenido   = models.TextField(verbose_name='Contenido',
                    help_text='HTML o texto plano. Puedes usar etiquetas <h2>, <p>, <ul>, etc.')
    imagen      = models.ImageField(upload_to='blog/', blank=True, null=True,
                    verbose_name='Imagen de portada',
                    help_text='Recomendado: 1200x630px JPG (proporción OG).')
    autor       = models.CharField(max_length=100, default='Green Dome', verbose_name='Autor')
    publicado   = models.BooleanField(default=False,
                    verbose_name='Publicado',
                    help_text='Solo los artículos publicados son visibles en la web.')
    fecha_pub   = models.DateTimeField(verbose_name='Fecha de publicación',
                    help_text='Fecha que se muestra en el artículo y en el sitemap.')
    creado_en   = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Artículo del blog'
        verbose_name_plural = 'Blog — Artículos'
        ordering = ['-fecha_pub']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog_detail', kwargs={'slug': self.slug})


# ── FAQ ──────────────────────────────────────────────────────────


class FAQItem(models.Model):
    """Preguntas frecuentes para la página /faq/."""
    pregunta    = models.CharField(max_length=300, verbose_name='Pregunta')
    respuesta   = models.TextField(verbose_name='Respuesta')
    orden       = models.PositiveSmallIntegerField(default=0)
    activo      = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Pregunta frecuente'
        verbose_name_plural = 'FAQ — Preguntas frecuentes'
        ordering = ['orden']

    def __str__(self):
        return self.pregunta


# ── Registro de miembros ─────────────────────────────────────────


class Member(models.Model):
    ORIGEN_CHOICES = [
        ('age_gate', 'Age Gate'),
        ('newsletter', 'Newsletter'),
    ]

    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    origen = models.CharField(max_length=20, choices=ORIGEN_CHOICES, default='age_gate')

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f'{self.nombre} <{self.email}>'
