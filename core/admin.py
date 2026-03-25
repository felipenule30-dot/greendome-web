from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from .models import Member, SiteConfig, Personaje, MundoCard, Actividad, TimelineItem


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


# ── Members ───────────────────────────────────────────────────────
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display    = ('nombre', 'email', 'origen', 'fecha_registro')
    list_filter     = ('origen', 'fecha_registro')
    search_fields   = ('nombre', 'email')
    readonly_fields = ('fecha_registro',)
    ordering        = ('-fecha_registro',)
