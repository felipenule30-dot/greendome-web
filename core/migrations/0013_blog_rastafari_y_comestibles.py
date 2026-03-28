"""
Data migration: dos artículos nuevos del blog de Green Dome.
1. La cultura rastafari y el cannabis en Jamaica
2. Fun fact: por qué los comestibles pegan diferente a fumar
"""
from django.db import migrations
from django.utils import timezone
from datetime import datetime


# ─────────────────────────────────────────────────────────────────
# ARTÍCULO 1 — Rastafari
# ─────────────────────────────────────────────────────────────────

TITULO_1 = "Ganja y Jah: la historia del cannabis en la cultura rastafari de Jamaica"
SLUG_1   = "ganja-jah-cannabis-cultura-rastafari-jamaica"
RESUMEN_1 = (
    "Para el movimiento rastafari, el cannabis no es una droga recreativa: "
    "es un sacramento, una puerta espiritual y un acto de resistencia política. "
    "Descubre cómo una planta se convirtió en el centro de una de las culturas "
    "más influyentes del siglo XX."
)
CONTENIDO_1 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
<em>«Fumar hierba revela que eres un hombre. No te hace hacer tonterías como el alcohol.»</em><br>
<strong style="color:#7ed957;">— Bob Marley</strong>, entrevista en <em>High Times</em>, 1976.
</p>

<h2>Jamaica antes del reggae: el origen del movimiento</h2>

<p>El rastafari nació en Jamaica en la década de 1930, en el contexto de la pobreza extrema,
el colonialismo británico y la búsqueda de identidad de la diáspora africana.
Su chispa fue la coronación, en 1930, de <strong>Ras Tafari Makonnen</strong> como
<strong>Haile Selassie I</strong>, emperador de Etiopía — el único país africano
que había resistido la colonización europea.</p>

<p>Figuras como <strong>Leonard Howell</strong>, considerado el primer predicador rastafari,
y el movimiento pan-africanista de <strong>Marcus Garvey</strong>
(«mirad hacia África, donde un rey negro será coronado») dieron forma a una teología
que veía en Selassie la reencarnación de Cristo y en África la tierra prometida —
<em>Zion</em> — frente al sistema opresor occidental al que llamaron <em>Babylon</em>.</p>

<blockquote>
<strong>Fuentes:</strong> Barry Chevannes, <em>Rastafari: Roots and Ideology</em>,
Syracuse University Press, 1994; Ennis B. Edmonds,
<em>Rastafari: From Outcasts to Culture Bearers</em>, Oxford University Press, 2003.
</blockquote>

<h2>La ganja como sacramento: «la hierba de la sabiduría»</h2>

<p>El cannabis — llamado <em>ganja</em> en Jamaica, término de origen sánscrito
traído por trabajadores indios en el siglo XIX — ocupa en el rastafari
un lugar equivalente al vino en el catolicismo o al peyote en rituales nativos americanos.
No es recreativo: es <strong>un sacramento que conecta con Jah</strong>
(nombre rastafari de Dios, abreviación de Yahveh).</p>

<p>La base bíblica que citan los rastas incluye pasajes como
<em>Génesis 1:29</em> («He aquí que os doy toda planta que da semilla»),
<em>Salmo 104:14</em> («Hace crecer la hierba para el ganado, y las plantas
para el servicio del hombre») y <em>Apocalipsis 22:2</em>
(«las hojas del árbol eran para la sanidad de las naciones»).</p>

<p>El consumo se realiza en sesiones llamadas <strong><em>reasonings</em></strong>:
círculos comunitarios donde se comparte la ganja en una pipa llamada
<em>chalice</em> o <em>chillum</em>, se canta, se debate filosofía,
política y espiritualidad. El objetivo no es la euforia sino la
<em>meditación profunda</em> y la conexión colectiva.</p>

<blockquote>
<strong>Fuentes:</strong> Leonard Barrett, <em>The Rastafarians</em>,
Beacon Press, 1977; Michael Barnett (ed.),
<em>Rastafari in the New Millennium</em>, Syracuse University Press, 2012.
</blockquote>

<h2>Bob Marley y la exportación global de la cultura rastafari</h2>

<p>Sería imposible hablar de rastafari sin <strong>Bob Marley</strong> (1945-1981).
A través del reggae — música que fusionaba ritmos africanos, ska jamaicano y
letras de resistencia — Marley llevó la filosofía rastafari a cada rincón del planeta.
Álbumes como <em>Catch a Fire</em> (1973), <em>Natty Dread</em> (1974) o
<em>Exodus</em> (1977) convirtieron la ganja, los dreadlocks y los colores
rojo-amarillo-verde (los de la bandera etíope) en iconos globales.</p>

<p>Marley era abiertamente practicante: fumaba ganja como parte de su devoción diaria
y fue arrestado en 1968 en Jamaica por posesión. Su respuesta fue seguir predicando
que la criminalización del cannabis era una herramienta de <em>Babylon</em>
para suprimir a los pobres y a los negros — algo que, como vimos en nuestro artículo
sobre la prohibición en EE.UU., no iba muy desencaminado.</p>

<blockquote>
<strong>Fuentes:</strong> Timothy White, <em>Catch a Fire: The Life of Bob Marley</em>,
Henry Holt, 1983; Roger Steffens, <em>So Much Things to Say: The Oral History of Bob Marley</em>,
W.W. Norton, 2017.
</blockquote>

<h2>Jamaica hoy: entre la fe y la ley</h2>

<p>Durante décadas, el cannabis fue ilegal en Jamaica — la patria espiritual de la
cultura que lo sacralizó. En 2015, Jamaica <strong>despenalizó la posesión
de hasta 2 onzas</strong> (56 gramos) y creó un marco legal para uso médico,
científico y sacramental rastafari. Los miembros registrados de comunidades
rastafari pueden cultivar y consumir sin restricciones legales.</p>

<p>El turismo cannábico creció exponencialmente desde entonces.
Sin embargo, muchos rastas veteranos ven con ambivalencia la comercialización:
para ellos, la ganja nunca fue un producto de mercado sino un don espiritual
que <em>Babylon</em> está intentando apropiarse ahora que resulta lucrativo.</p>

<blockquote>
<strong>Fuentes:</strong> Dangerous Drugs (Amendment) Act, Jamaica, 2015;
Terri-Karelle Reid, «Rastafari and the Legalization of Cannabis in Jamaica»,
<em>Caribbean Quarterly</em>, vol. 62, 2016.
</blockquote>

<hr>

<p style="color:#888;font-size:.9rem;">
<strong>Bibliografía:</strong> Chevannes (1994) · Edmonds (2003) · Barrett (1977) ·
Barnett (2012) · White (1983) · Steffens (2017) · Reid (2016) ·
Dangerous Drugs (Amendment) Act, Jamaica (2015).
</p>
"""


# ─────────────────────────────────────────────────────────────────
# ARTÍCULO 2 — Comestibles vs Fumar
# ─────────────────────────────────────────────────────────────────

TITULO_2 = "¿Por qué los comestibles te destrozan más que fumar? La ciencia detrás del viaje"
SLUG_2   = "por-que-comestibles-pegan-diferente-fumar-cannabis-ciencia"
RESUMEN_2 = (
    "Comes un brownie, pasa una hora y no sientes nada, decides comer otro… "
    "y entonces te arrepientes. No es magia negra: es química pura. "
    "Tu hígado convierte el THC en una molécula diferente — y mucho más potente."
)
CONTENIDO_2 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
<em>«El clásico error del comestible: comes uno, no sientes nada en 45 minutos,
comes otro. Una hora después estás en el techo.»</em><br>
<strong style="color:#7ed957;">— Experiencia universal, relatada en todos los idiomas.</strong>
</p>

<h2>La clave está en el hígado: THC vs 11-hidroxi-THC</h2>

<p>Cuando fumas o vaporizas cannabis, el <strong>THC</strong> (tetrahidrocannabinol)
pasa directamente de tus pulmones al torrente sanguíneo y llega al cerebro
<strong>en segundos</strong>. El efecto empieza casi de inmediato y alcanza
su pico en 10-30 minutos.</p>

<p>Cuando comes un comestible, el THC sigue un camino completamente diferente:
estómago → intestino delgado → hígado. Ahí ocurre la magia química.
El hígado metaboliza el THC mediante la enzima <strong>CYP2C9</strong>
y lo convierte en <strong>11-hidroxi-THC</strong> — una molécula diferente,
más pequeña, que <strong>cruza la barrera hematoencefálica más fácilmente</strong>
que el THC original y produce efectos notablemente más intensos y duraderos.</p>

<p>Este proceso se llama <strong>«metabolismo de primer paso»</strong>
(<em>first-pass metabolism</em>) y es la razón de todo.</p>

<blockquote>
<strong>Fuentes:</strong> Huestis, M.A., «Human Cannabinoid Pharmacokinetics»,
<em>Chemistry & Biodiversity</em>, vol. 4, n.º 8, 2007, pp. 1770-1804;
Sharma, P. et al., «Chemistry, Metabolism and Toxicology of Cannabis»,
<em>Iranian Journal of Psychiatry</em>, vol. 7, n.º 4, 2012.
</blockquote>

<h2>Por qué tardan tanto en hacer efecto</h2>

<p>El proceso digestivo no es rápido. Después de comer un comestible:</p>

<ul>
  <li><strong>0-30 min</strong>: el comestible se digiere en el estómago.</li>
  <li><strong>30-90 min</strong>: el THC se absorbe en el intestino delgado
  y llega al hígado (la velocidad depende de si has comido, tu metabolismo,
  el contenido graso del comestible — el THC es liposoluble, se absorbe mejor
  con grasas).</li>
  <li><strong>90-120 min</strong>: el 11-hidroxi-THC alcanza el cerebro
  y empieza el efecto.</li>
  <li><strong>2-4 horas</strong>: pico máximo del efecto.</li>
  <li><strong>4-8 horas</strong>: descenso gradual (frente a 1-3 horas
  fumando).</li>
</ul>

<blockquote>
<strong>Fuentes:</strong> MacCallum, C.A. y Russo, E.B.,
«Practical Considerations in Medical Cannabis Administration and Dosing»,
<em>European Journal of Internal Medicine</em>, vol. 49, 2019, pp. 12-19.
</blockquote>

<h2>Fun facts que quizá no sabías</h2>

<ul>
  <li>🍫 <strong>El chocolate potencia el efecto.</strong> Contiene anandamida
  (el «cannabinoide endógeno» del cuerpo) e inhibe la enzima que la degrada,
  lo que amplifica la señal cannabinoide. No es casualidad que los brownies
  sean el comestible de cannabis más famoso de la historia.</li>

  <li>🥑 <strong>Las grasas importan mucho.</strong> El THC es liposoluble.
  Un comestible cocinado con mantequilla o aceite de coco se absorbe
  significativamente mejor que uno con poca grasa. Si comes el comestible
  con un aguacate o frutos secos, el efecto será más intenso.</li>

  <li>⏱️ <strong>El ayuno lo acelera, la comida lo amortigua.</strong>
  Con el estómago vacío, el THC se absorbe más rápido pero el efecto
  puede ser más imprevisible. Después de una comida abundante,
  el pico tarda más pero suele ser más suave y gradual.</li>

  <li>🧬 <strong>El CYP2C9 varía por genética.</strong>
  Hay personas con variantes genéticas que metabolizan el THC más
  lentamente — les dura más el efecto y con menos cantidad.
  Otras lo metabolizan muy rápido y sienten poco con la misma dosis.
  Explica por qué la misma galleta afecta de forma tan diferente
  a personas distintas.</li>

  <li>🌿 <strong>El CBD ralentiza la degradación del THC.</strong>
  Cuando un comestible tiene tanto THC como CBD, el CBD compite
  por las mismas enzimas hepáticas, lo que puede prolongar los
  efectos del THC. Más motivo para leer bien las etiquetas.</li>
</ul>

<blockquote>
<strong>Fuentes:</strong> di Marzo, V. y Piscitelli, F.,
«The Endocannabinoid System and its Modulation by Phytocannabinoids»,
<em>Neurotherapeutics</em>, vol. 12, 2015; Grotenhermen, F.,
«Pharmacokinetics and Pharmacodynamics of Cannabinoids»,
<em>Clinical Pharmacokinetics</em>, vol. 42, n.º 4, 2003, pp. 327-360.
</blockquote>

<h2>La regla de oro: «empieza bajo, ve despacio»</h2>

<p>La guía de daños reducidos más citada en la literatura médica cannábica
es el principio <strong><em>«start low, go slow»</em></strong>
(empieza con dosis baja, espera suficiente tiempo antes de repetir).
Para comestibles, los expertos recomiendan:</p>

<ul>
  <li>Dosis inicial: <strong>2,5-5 mg de THC</strong> para principiantes.</li>
  <li>Esperar al menos <strong>2 horas</strong> antes de considerar repetir.</li>
  <li>El error más común es asumir que «no hace efecto» a los 45 minutos
  y tomar más — el pico aún no ha llegado.</li>
</ul>

<hr>

<p style="color:#888;font-size:.9rem;">
<strong>Bibliografía:</strong> Huestis (2007) · Sharma et al. (2012) ·
MacCallum & Russo (2019) · di Marzo & Piscitelli (2015) · Grotenhermen (2003).
</p>
"""


# ─────────────────────────────────────────────────────────────────
# MIGRACIÓN
# ─────────────────────────────────────────────────────────────────

def crear_articulos(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')

    BlogPost.objects.get_or_create(
        slug=SLUG_1,
        defaults={
            'titulo':    TITULO_1,
            'resumen':   RESUMEN_1,
            'contenido': CONTENIDO_1,
            'autor':     'Green Dome',
            'publicado': True,
            'fecha_pub': timezone.make_aware(datetime(2025, 12, 1, 10, 0, 0)),
        }
    )

    BlogPost.objects.get_or_create(
        slug=SLUG_2,
        defaults={
            'titulo':    TITULO_2,
            'resumen':   RESUMEN_2,
            'contenido': CONTENIDO_2,
            'autor':     'Green Dome',
            'publicado': True,
            'fecha_pub': timezone.make_aware(datetime(2025, 12, 10, 10, 0, 0)),
        }
    )


def eliminar_articulos(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    BlogPost.objects.filter(slug__in=[SLUG_1, SLUG_2]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_fix_slug_articulo_prohibicion'),
    ]

    operations = [
        migrations.RunPython(crear_articulos, eliminar_articulos),
    ]
