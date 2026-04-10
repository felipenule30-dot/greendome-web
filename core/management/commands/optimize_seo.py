"""
management command: optimize_seo
Rota y actualiza automáticamente las keywords y meta descriptions
en SiteConfig cada día para maximizar cobertura SEO.

Uso manual:
    python manage.py optimize_seo

Programar diariamente (Windows):
    schtasks /create /tn "GreenDome SEO" /tr
    "C:\\...\\venv\\Scripts\\python manage.py optimize_seo"
    /sc daily /st 03:00
"""

import random
import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone


# ─────────────────────────────────────────────────────────────
# BANCO DE KEYWORDS — todas las variantes posibles para Sevilla
# ─────────────────────────────────────────────────────────────

KEYWORD_SETS = [
    # Set 1 — Foco: asociación / club
    (
        "green dome, asociación cannábica sevilla, club cannábico sevilla, "
        "club social cannabis sevilla, asociaciones cannábicas sevilla, "
        "cannabis nervión, asociación cannabis nervión, club privado cannabis sevilla, "
        "asociaciones nervión sevilla, green dome svq"
    ),
    # Set 2 — Foco: búsquedas informales
    (
        "weed sevilla, marihuana sevilla, hierba sevilla, cannabis sevilla, "
        "club cannabis sevilla, green dome sevilla, asociacion canabica sevilla, "
        "canabis sevilla, social club sevilla, club cannábico nervión"
    ),
    # Set 3 — Foco: consumo responsable / cultura
    (
        "consumo responsable cannabis sevilla, cultura cannabis sevilla, "
        "club cannabis privado sevilla, asociación privada cannabis sevilla, "
        "cannabis social club sevilla, comunidad cannabis nervión, "
        "club cannábico sin ánimo de lucro sevilla, cannabis andalucía cultura, "
        "cannabis legal modelo asociativo, asociación cannábica nervión sevilla"
    ),
    # Set 4 — Foco: localización barrio
    (
        "club cannabis nervión sevilla, asociación nervión sevilla, "
        "cannabis barrio nervión, weed nervión, marihuana nervión sevilla, "
        "hierba nervión sevilla, club privado nervión, asociaciones cannábicas andalucía, "
        "cannabis andalucía, club cannábico andalucía"
    ),
    # Set 5 — Foco: long-tail / intención búsqueda
    (
        "cómo unirse a club cannábico sevilla, cómo hacerse socio club cannabis sevilla, "
        "asociación cannábica sin ánimo de lucro sevilla, club social cannabis nervión, "
        "green dome club sevilla, greendome svq instagram, lacupulaverdesv, "
        "cúpula verde sevilla, la cúpula verde sevilla, cannabis club sevilla españa"
    ),
    # Set 6 — Foco: cultura + comunidad
    (
        "cultura cannabis sevilla, comunidad cannabis sevilla, historia cannabis españa, "
        "club cultural cannabis sevilla, asociación cultural cannabis sevilla, "
        "consumo responsable cannabis, weed culture sevilla, cannabis lifestyle sevilla, "
        "green dome asociación, club cannábico sevilla centro"
    ),
    # Set 7 — Foco: inglés (turismo)
    (
        "cannabis club seville spain, weed club seville, marijuana seville, "
        "social cannabis club seville, green dome seville, weed sevilla spain, "
        "cannabis association seville, private cannabis club seville, "
        "where to find weed seville, cannabis nervión seville"
    ),
    # Set 8 — Foco: búsquedas informales sin errores
    (
        "hierba sevilla, weed sevilla, marihuana sevilla, "
        "club privado cannabis sevilla, asociacion cannabis sevilla, "
        "cannabis nervion sevilla, green dome sevilla instagram, "
        "greendome sevilla, la cupula verde sevilla, greendome svq"
    ),
]

TITLE_VARIANTS = [
    "Green Dome — Club Cannábico · Asociación Cannabis Sevilla · Nervión",
    "Green Dome Sevilla · Club Cannábico Sin Ánimo de Lucro · Nervión",
    "Green Dome · Asociación Cannábica Sevilla — Club Social Cannabis Nervión",
    "Club Cannábico Green Dome · Sevilla, Nervión · Desde 2025",
    "Green Dome SVQ · Asociación Cannábica Sin Ánimo de Lucro · Sevilla",
    "Green Dome — Asociación Cannabis Sevilla · Club Privado Nervión",
    "Asociación Cannábica Green Dome · Club Social Cannabis · Sevilla",
]

DESCRIPTION_VARIANTS = [
    (
        "Green Dome: club cannábico sin ánimo de lucro en Sevilla (Nervión). "
        "Asociación de cannabis con foco en cultura, historia y consumo responsable. "
        "Únete a la comunidad desde noviembre 2025."
    ),
    (
        "Green Dome es la asociación cannábica de referencia en Sevilla, barrio de Nervión. "
        "Club social de cannabis sin ánimo de lucro. Cultura, comunidad y consumo responsable."
    ),
    (
        "Asociación cannábica Green Dome en Sevilla. Club privado de cannabis en Nervión. "
        "Historia, cultura cannábica y comunidad. Sin ánimo de lucro desde 2025."
    ),
    (
        "Green Dome — club cannábico y asociación sin ánimo de lucro en Sevilla, Nervión. "
        "Somos una comunidad que promueve la cultura cannabis y el consumo responsable en Andalucía."
    ),
    (
        "Busca un club cannábico en Sevilla? Green Dome es tu asociación: "
        "privado, sin ánimo de lucro, en el barrio de Nervión. "
        "Cultura, historia y comunidad cannabis desde noviembre 2025."
    ),
]


class Command(BaseCommand):
    help = "Optimiza y rota las keywords SEO de Green Dome diariamente"

    def handle(self, *args, **options):
        from core.models import SiteConfig

        cfg = SiteConfig.load()

        # Usa el día del año para rotar de forma determinista
        day_of_year = datetime.date.today().timetuple().tm_yday

        keywords   = KEYWORD_SETS[day_of_year % len(KEYWORD_SETS)]
        title      = TITLE_VARIANTS[day_of_year % len(TITLE_VARIANTS)]
        desc       = DESCRIPTION_VARIANTS[day_of_year % len(DESCRIPTION_VARIANTS)]

        # Guardamos en SiteConfig para que la vista los use
        # La FAQPage es estática en home.html (no se rota — evita inconsistencias en rastreo)
        cfg.seo_keywords    = keywords
        cfg.seo_title       = title
        cfg.seo_description = desc
        cfg.seo_updated_at  = timezone.now()
        cfg.save()

        self.stdout.write(self.style.SUCCESS(
            f"[OK] SEO actualizado [{datetime.date.today()}]\n"
            f"   Title: {title[:60]}...\n"
            f"   Keywords: {keywords[:80]}..."
        ))
