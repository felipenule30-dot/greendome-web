"""
management command: generate_blog_images

Genera imágenes de portada 1200×630px para los artículos del blog
que no tienen imagen asignada. Usa Pillow para crear una imagen
con fondo degradado oscuro, acento verde #7ed957 y el título del artículo.

Uso:
    python manage.py generate_blog_images           # genera solo los que faltan
    python manage.py generate_blog_images --force   # regenera todos
"""

import os
import textwrap
from io import BytesIO

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand


WIDTH, HEIGHT = 1200, 630
GREEN = (126, 217, 87)
BG_TOP = (13, 10, 20)       # #0d0a14
BG_BOT = (26, 13, 46)       # #1a0d2e
ACCENT = (126, 217, 87)     # #7ed957


def _make_image(titulo: str) -> bytes:
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new("RGB", (WIDTH, HEIGHT), BG_TOP)
    draw = ImageDraw.Draw(img)

    # Degradado vertical manual
    for y in range(HEIGHT):
        t = y / HEIGHT
        r = int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * t)
        g = int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * t)
        b = int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * t)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

    # Borde verde izquierdo (8px)
    draw.rectangle([(0, 0), (8, HEIGHT)], fill=ACCENT)

    # Línea decorativa verde inferior
    draw.rectangle([(0, HEIGHT - 6), (WIDTH, HEIGHT)], fill=ACCENT)

    # Logo texto "Green Dome" arriba
    try:
        font_label = ImageFont.truetype("arial.ttf", 28)
        font_title = ImageFont.truetype("arial.ttf", 56)
        font_sub   = ImageFont.truetype("arial.ttf", 26)
    except OSError:
        font_label = ImageFont.load_default()
        font_title = font_label
        font_sub   = font_label

    # Label "Green Dome · Blog"
    draw.text((60, 60), "Green Dome  ·  Blog", font=font_label, fill=ACCENT)

    # Línea separadora corta
    draw.rectangle([(60, 110), (200, 114)], fill=ACCENT)

    # Título del artículo (wrap automático)
    wrapped = textwrap.fill(titulo, width=30)
    draw.text((60, 140), wrapped, font=font_title, fill=(255, 255, 255))

    # Subline "greendome.net"
    draw.text((60, HEIGHT - 70), "greendome.net  ·  Sevilla, Nervión", font=font_sub, fill=(136, 136, 136))

    buf = BytesIO()
    img.save(buf, format="JPEG", quality=90, optimize=True)
    return buf.getvalue()


class Command(BaseCommand):
    help = "Genera imágenes de portada para artículos del blog sin imagen"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Regenera la imagen aunque el artículo ya tenga una",
        )

    def handle(self, *args, **options):
        from core.models import BlogPost

        posts = BlogPost.objects.filter(publicado=True)
        if not options["force"]:
            posts = posts.filter(imagen="")

        if not posts.exists():
            self.stdout.write(self.style.WARNING("No hay artículos sin imagen. Usa --force para regenerar."))
            return

        generadas = 0
        for post in posts:
            self.stdout.write(f"  Generando imagen para: {post.titulo[:60]}...")
            try:
                jpg_bytes = _make_image(post.titulo)
                filename = f"blog/cover_{post.slug[:60]}.jpg"
                post.imagen.save(filename, ContentFile(jpg_bytes), save=True)
                generadas += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  ERROR en '{post.slug}': {e}"))

        self.stdout.write(self.style.SUCCESS(f"\n[OK] {generadas} imagen(es) generada(s)."))
        self.stdout.write("Recuerda ejecutar 'python manage.py collectstatic' si usas whitenoise.")
