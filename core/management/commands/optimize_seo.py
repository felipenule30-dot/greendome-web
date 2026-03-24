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
        "green dome, asociacion cannabica sevilla, club cannabico sevilla, "
        "club social cannabis sevilla, asociaciones cannabicas sevilla, "
        "cannabis nervion, asociacion cannabis nervion, club privado cannabis sevilla, "
        "asociaciones nervion sevilla, green dome svq"
    ),
    # Set 2 — Foco: búsquedas informales
    (
        "weed sevilla, marihuana sevilla, hierba sevilla, cannabis sevilla, "
        "club cannabis sevilla, green dome sevilla, asociacion canabica sevilla, "
        "canabis sevilla, social club sevilla, club cannabico nervion"
    ),
    # Set 3 — Foco: comparativas / tipo de negocio
    (
        "tienda cannabis sevilla, dispensario cannabis sevilla, "
        "donde comprar cannabis sevilla, cbd sevilla, club cbd sevilla, "
        "asociacion cbd sevilla, cannabis legal sevilla, cannabis recreativo sevilla, "
        "consumo responsable sevilla, cultura cannabis andalucia"
    ),
    # Set 4 — Foco: localización barrio
    (
        "club cannabis nervion sevilla, asociacion nervion sevilla, "
        "cannabis barrio nervion, weed nervion, marihuana nervion sevilla, "
        "hierba nervion sevilla, club privado nervion, asociaciones cannabicas andalucia, "
        "cannabis andalucia, club canabico andalucia"
    ),
    # Set 5 — Foco: long-tail / intención búsqueda
    (
        "como unirse a club cannabico sevilla, como hacerse socio club cannabis sevilla, "
        "asociacion cannabica sin animo lucro sevilla, club social cannabis nervion, "
        "green dome club sevilla, greendome svq instagram, lacupulaverdesv, "
        "cupula verde sevilla, la cupula verde sevilla, cannabis club sevilla espana"
    ),
    # Set 6 — Foco: cultura + comunidad
    (
        "cultura cannabis sevilla, comunidad cannabis sevilla, historia cannabis espana, "
        "club cultural cannabis sevilla, asociacion cultural cannabis sevilla, "
        "consumo responsable cannabis, weed culture sevilla, cannabis lifestyle sevilla, "
        "green dome asociacion, club canabico sevilla centro"
    ),
    # Set 7 — Foco: inglés (turismo)
    (
        "cannabis club seville spain, weed club seville, marijuana seville, "
        "social cannabis club seville, green dome seville, weed sevilla spain, "
        "cannabis association seville, private cannabis club seville, "
        "where to find weed seville, cannabis nervion seville"
    ),
    # Set 8 — Foco: variantes ortográficas (errores comunes)
    (
        "asociacion canabica sevilla, club canabico sevilla, canabis nervion, "
        "hierba sevilla, weed store sevilla, marihuana nervion, "
        "asociacion marihuana sevilla, club marihuana sevilla, "
        "green dome sevilla instagram, greendome sevilla"
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

FAQ_SETS = [
    [
        {
            "q": "¿Qué es Green Dome?",
            "a": (
                "Green Dome es una asociación cannábica sin ánimo de lucro en Sevilla (Nervión). "
                "Es un club social privado donde la cultura, el conocimiento y el consumo "
                "responsable son los pilares. Abierto desde noviembre de 2025."
            ),
        },
        {
            "q": "¿Dónde está el club cannábico Green Dome en Sevilla?",
            "a": (
                "Green Dome se encuentra en el barrio de Nervión, Sevilla. "
                "Al ser un club privado la dirección exacta se facilita a socios. "
                "Contáctanos por email lacupulaverdesv@gmail.com o Instagram @greendome_svq."
            ),
        },
        {
            "q": "¿Cómo me hago socio de un club cannábico en Sevilla?",
            "a": (
                "Para unirte a Green Dome, el club cannábico de Sevilla Nervión, "
                "contacta por el formulario web, email lacupulaverdesv@gmail.com "
                "o Instagram @greendome_svq. Acceso exclusivo para mayores de 18 años."
            ),
        },
    ],
    [
        {
            "q": "¿Es legal un club cannábico en España?",
            "a": (
                "Las asociaciones cannábicas en España operan bajo el modelo asociativo "
                "sin ánimo de lucro en un marco legal de consumo privado entre socios adultos. "
                "Green Dome es una asociación legalmente constituida en Sevilla."
            ),
        },
        {
            "q": "¿Qué diferencia hay entre una tienda de cannabis y un club cannábico?",
            "a": (
                "Un club cannábico como Green Dome no es una tienda: es una asociación privada "
                "sin ánimo de lucro donde los socios comparten cultura, conocimiento "
                "y consumo responsable. No vendemos nada al público general."
            ),
        },
        {
            "q": "¿Dónde encontrar cannabis en Sevilla?",
            "a": (
                "Green Dome es una asociación cannábica privada en el barrio de Nervión, Sevilla. "
                "No somos una tienda pública — somos una comunidad. "
                "Contacta con nosotros para más información sobre cómo ser socio."
            ),
        },
    ],
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
        faq_set    = FAQ_SETS[day_of_year % len(FAQ_SETS)]

        # Guardamos en SiteConfig para que la vista los use
        cfg.seo_keywords    = keywords
        cfg.seo_title       = title
        cfg.seo_description = desc
        cfg.seo_faq_json    = self._build_faq_json(faq_set)
        cfg.seo_updated_at  = timezone.now()
        cfg.save()

        self.stdout.write(self.style.SUCCESS(
            f"[OK] SEO actualizado [{datetime.date.today()}]\n"
            f"   Title: {title[:60]}...\n"
            f"   Keywords: {keywords[:80]}..."
        ))

    @staticmethod
    def _build_faq_json(faq_set):
        import json
        items = [
            {
                "@type": "Question",
                "name": f["q"],
                "acceptedAnswer": {"@type": "Answer", "text": f["a"]},
            }
            for f in faq_set
        ]
        return json.dumps({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": items,
        }, ensure_ascii=False)
