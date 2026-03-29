from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from django.forms import Textarea, TextInput
from .models import Member, SiteConfig, Personaje, MundoCard, Actividad, TimelineItem, BlogPost, BlogImage, FAQItem, ClubPhoto


# ── SiteConfig (singleton) ────────────────────────────────────────
@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    """
    Singleton: la lista redirige directamente al formulario de edición.
    Así no hay que buscar "dónde hacer clic".
    """
    fieldsets = (
        ('🖼️  Logos', {
            'fields': ('logo', 'logo_nav'),
            'description': (
                '<strong>Logo Hero</strong>: el logo GRANDE del centro de la pantalla (hero + footer). '
                'Usa el PNG con cúpula + "GREEN DOME". '
                '<br><strong>Logo Nav</strong>: el logo PEQUEÑO de la esquina superior izquierda. '
                'Puede ser solo el icono/arco sin texto. '
                'Si no subes Logo Nav se usará el mismo que el Hero reducido.'
            ),
        }),
        ('🏠  Hero', {
            'fields': ('hero_bg', 'eyebrow', 'tagline', 'cta_texto'),
            'description': (
                '<strong>Fondo del Hero</strong>: imagen o GIF de fondo. '
                'Recomendado JPG/PNG de al menos 1920x1080px. '
                'Si no subes nada se mantiene el fondo oscuro por defecto.'
            ),
        }),
        ('ℹ️  Quiénes somos', {
            'fields': ('about_title', 'about_texto_1', 'about_texto_2'),
        }),
        ('📊  Estadísticas (4 cifras)', {
            'fields': (
                ('stat_1_num', 'stat_1_label'),
                ('stat_2_num', 'stat_2_label'),
                ('stat_3_num', 'stat_3_label'),
                ('stat_4_num', 'stat_4_label'),
            ),
        }),
        ('📬  Contacto y redes', {
            'fields': ('email', 'instagram', 'whatsapp', 'whatsapp_msg', 'contacto_desc'),
        }),
        ('🗺️  Google Maps', {
            'fields': ('maps_embed_url', 'maps_directions_url', 'maps_review_url'),
            'description': (
                '<strong>maps_embed_url</strong>: Ve a Google Maps → busca tu local → Compartir → '
                '"Insertar un mapa" → copia la URL del <code>src=""</code>.<br>'
                '<strong>maps_directions_url</strong>: La URL de tu ficha en Google Maps (para el botón "Cómo llegar").<br>'
                '<strong>maps_review_url</strong>: En Google Maps → tu ficha → "Obtener enlace para compartir reseñas".'
            ),
        }),
        ('🤖  SEO Automático (solo lectura)', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords', 'seo_updated_at'),
            'classes': ('collapse',),
            'description': (
                '⚙️ Estos campos se actualizan automáticamente cada día con el comando '
                '<code>python manage.py optimize_seo</code>. '
                'Puedes editarlos manualmente pero serán sobreescritos en la próxima ejecución automática.'
            ),
        }),
    )

    readonly_fields = ('seo_updated_at',)

    # Redirige la vista de lista directamente al objeto pk=1
    def changelist_view(self, request, extra_context=None):
        obj = SiteConfig.load()
        return HttpResponseRedirect(
            reverse('admin:core_siteconfig_change', args=[obj.pk])
        )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# ── Personajes ────────────────────────────────────────────────────
@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display       = ('orden', 'nombre', 'rol', 'tag_badge', 'activo')
    list_display_links = ('nombre',)
    list_editable      = ('orden', 'activo')
    list_filter        = ('activo',)
    search_fields      = ('nombre', 'rol')
    save_on_top        = True
    fieldsets = (
        ('Informacion del personaje', {
            'fields': ('nombre', 'rol', 'bio', 'orden', 'activo'),
        }),
        ('Imagen', {
            'fields': ('imagen', 'img_filename', 'bg_css'),
            'description': (
                'Opcion 1: sube un PNG directamente en "Imagen". '
                'Opcion 2: escribe el nombre del archivo que ya esta en static/img/ '
                '(ej: mascot-main.png) en "Img filename".'
            ),
        }),
        ('Tag de color', {
            'fields': ('tag', 'tag_color', 'tag_txt'),
        }),
    )

    @admin.display(description='Tag')
    def tag_badge(self, obj):
        return format_html(
            '<span style="background:{};color:{};padding:3px 12px;'
            'border-radius:99px;font-size:11px;font-weight:bold">{}</span>',
            obj.tag_color, obj.tag_txt, obj.tag
        )


# ── MundoCard ─────────────────────────────────────────────────────
@admin.register(MundoCard)
class MundoCardAdmin(admin.ModelAdmin):
    list_display       = ('orden', 'icono', 'titulo', 'color_class', 'activo')
    list_display_links = ('titulo',)
    list_editable      = ('orden', 'activo')
    list_filter        = ('activo', 'color_class')
    search_fields      = ('titulo',)
    save_on_top        = True
    fieldsets = (
        ('Contenido', {
            'fields': ('titulo', 'descripcion', 'orden', 'activo'),
        }),
        ('Visual', {
            'fields': ('icono', 'imagen', 'color_class'),
            'description': (
                'Sube un GIF o imagen en "Imagen" para mostrarla en la card. '
                'Si no subes imagen se usará el emoji.'
            ),
        }),
    )


# ── Actividades ───────────────────────────────────────────────────
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display       = ('orden', 'titulo', 'activo')
    list_display_links = ('titulo',)
    list_editable      = ('orden', 'activo')
    search_fields      = ('titulo',)
    save_on_top        = True


# ── Timeline ──────────────────────────────────────────────────────
@admin.register(TimelineItem)
class TimelineItemAdmin(admin.ModelAdmin):
    list_display       = ('orden', 'año', 'desc_corta', 'destacado')
    list_display_links = ('año',)
    list_editable      = ('orden', 'destacado')
    search_fields      = ('año', 'descripcion')
    save_on_top        = True

    @admin.display(description='Descripcion')
    def desc_corta(self, obj):
        return obj.descripcion[:80] + ('...' if len(obj.descripcion) > 80 else '')


# ── Blog ──────────────────────────────────────────────────────────
class BlogImageInline(admin.TabularInline):
    model       = BlogImage
    extra       = 2
    fields      = ('imagen', 'descripcion', 'orden', 'url_copiada')
    readonly_fields = ('url_copiada',)
    ordering    = ('orden',)

    @admin.display(description='URL para pegar en el contenido')
    def url_copiada(self, obj):
        if obj.pk and obj.imagen:
            url = obj.imagen.url
            return format_html(
                '<code style="font-size:11px;color:#7ed957;word-break:break-all;">{}</code>'
                '<br><small style="color:#888;">Copia esta URL y pégala en el contenido como:<br>'
                '<code style="font-size:10px;">'
                '&lt;img src=&quot;{}&quot; alt=&quot;{}&quot; '
                'style=&quot;width:100%;border-radius:12px;margin:1.5rem 0;&quot;&gt;'
                '</code></small>',
                url, url, obj.descripcion or 'descripción'
            )
        return '(Guarda primero para ver la URL)'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display        = ('titulo_corto', 'idioma', 'autor', 'publicado', 'fecha_pub', 'preview_link')
    list_display_links  = ('titulo_corto',)
    list_editable       = ('publicado', 'idioma')
    list_filter         = ('publicado', 'idioma', 'fecha_pub', 'autor')
    search_fields       = ('titulo', 'resumen', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy      = 'fecha_pub'
    save_on_top         = True
    inlines             = [BlogImageInline]

    fieldsets = (
        ('📝  Contenido principal', {
            'fields': ('titulo', 'slug', 'resumen'),
            'description': (
                '<strong>Título</strong>: el slug se genera automáticamente a partir del título. '
                '<br><strong>Resumen</strong>: 1-3 frases. Aparece en la lista del blog y en la '
                'meta description de Google (idealmente entre 120-160 caracteres).'
            ),
        }),
        ('🖼️  Imagen de portada', {
            'fields': ('imagen',),
            'description': (
                'Sube la imagen de portada del artículo. '
                'Recomendado: <strong>1200 × 630 px</strong> en JPG (proporción Open Graph). '
                'Se mostrará en la cabecera del artículo y como imagen en redes sociales.'
            ),
        }),
        ('✍️  Cuerpo del artículo (HTML)', {
            'fields': ('contenido',),
            'description': (
                'Escribe el artículo en HTML. Etiquetas útiles:<br>'
                '<code>&lt;h2&gt;Título de sección&lt;/h2&gt;</code> — subtítulos<br>'
                '<code>&lt;h3&gt;Subtítulo menor&lt;/h3&gt;</code><br>'
                '<code>&lt;p&gt;Párrafo normal&lt;/p&gt;</code><br>'
                '<code>&lt;strong&gt;negrita&lt;/strong&gt;</code> — texto en negrita verde<br>'
                '<code>&lt;em&gt;cursiva&lt;/em&gt;</code><br>'
                '<code>&lt;ul&gt;&lt;li&gt;item&lt;/li&gt;&lt;/ul&gt;</code> — lista<br>'
                '<code>&lt;blockquote&gt;cita o fuente&lt;/blockquote&gt;</code> — cita destacada<br>'
                '<code>&lt;img src="URL" alt="desc" style="width:100%;border-radius:12px;margin:1.5rem 0;"&gt;</code>'
                ' — imagen inline (sube la imagen a /admin/core/blogpost/ y usa su URL, '
                'o usa una URL externa)<br>'
                '<code>&lt;hr&gt;</code> — separador<br>'
                '<code>&lt;ol&gt;&lt;li&gt;item&lt;/li&gt;&lt;/ol&gt;</code> — lista numerada'
            ),
        }),
        ('⚙️  Publicación y metadatos', {
            'fields': ('autor', 'idioma', 'publicado', 'fecha_pub'),
            'description': (
                'Marca <strong>Publicado</strong> para que el artículo sea visible en la web. '
                'La <strong>fecha de publicación</strong> aparece en el artículo y en el sitemap. '
                'Puedes programar artículos con fecha futura (no aparecerán hasta esa fecha).'
            ),
        }),
    )

    # Textarea grande para el contenido HTML
    formfield_overrides = {
        __import__('django.db.models', fromlist=['TextField']).TextField: {
            'widget': Textarea(attrs={
                'rows': 40,
                'cols': 120,
                'style': (
                    'font-family: "Courier New", monospace; '
                    'font-size: 13px; '
                    'background: #1a1a2e; '
                    'color: #e0e0e0; '
                    'border: 1px solid #444; '
                    'border-radius: 8px; '
                    'padding: 12px; '
                    'line-height: 1.6; '
                    'width: 100%;'
                ),
            })
        },
    }

    # Imagen preview en la lista
    @admin.display(description='Vista previa')
    def preview_link(self, obj):
        if obj.pk and obj.slug:
            return format_html(
                '<a href="/blog/{}/" target="_blank" '
                'style="color:#7ed957;font-size:11px;">🔗 Ver en web</a>',
                obj.slug
            )
        return '—'

    @admin.display(description='Título')
    def titulo_corto(self, obj):
        t = obj.titulo
        return t[:60] + '…' if len(t) > 60 else t

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('creado_en', 'actualizado')
        return ()


# ── FAQ ───────────────────────────────────────────────────────────
@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display       = ('orden', 'pregunta', 'activo')
    list_display_links = ('pregunta',)
    list_editable      = ('orden', 'activo')
    search_fields      = ('pregunta', 'respuesta')
    save_on_top        = True


# ── The Club — Galería de fotos ───────────────────────────────────
@admin.register(ClubPhoto)
class ClubPhotoAdmin(admin.ModelAdmin):
    list_display       = ('orden', 'titulo_o_nombre', 'activo', 'preview')
    list_display_links = ('titulo_o_nombre',)
    list_editable      = ('orden', 'activo')
    save_on_top        = True

    fieldsets = (
        ('📸  Foto', {
            'fields': ('imagen', 'titulo', 'descripcion'),
            'description': (
                'Sube la foto. Una vez guardada verás la previsualización. '
                'El <strong>Título</strong> aparece como pie de foto. '
                'La <strong>Descripción</strong> es el texto alternativo (importante para SEO y accesibilidad).'
            ),
        }),
        ('⚙️  Configuración', {
            'fields': ('orden', 'activo'),
        }),
    )

    @admin.display(description='Foto')
    def titulo_o_nombre(self, obj):
        return obj.titulo or f'Foto #{obj.orden}'

    @admin.display(description='Vista previa')
    def preview(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:6px;object-fit:cover;" />',
                obj.imagen.url
            )
        return '—'


# ── Members ───────────────────────────────────────────────────────
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display    = ('nombre', 'email', 'origen', 'fecha_registro')
    list_filter     = ('origen', 'fecha_registro')
    search_fields   = ('nombre', 'email')
    readonly_fields = ('fecha_registro',)
    ordering        = ('-fecha_registro',)
