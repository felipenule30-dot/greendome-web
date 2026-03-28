"""
Data migration: cuatro artículos nuevos del blog de Green Dome.

Artículos ordenados por prioridad SEO:
1. Cómo hacerse socio de un cannabis club en España (alta intención de búsqueda)
2. CBD vs THC: diferencias, efectos y usos — guía básica (altísimo volumen)
3. Historia de los clubes cannábicos en España (autoridad temática local)
4. Autocultivo de cannabis en España: qué dice la ley (alta intención local)
"""
from django.db import migrations
from django.utils import timezone
from datetime import datetime


# ─────────────────────────────────────────────────────────────────
# ARTÍCULO 1 — Cómo hacerse socio de un cannabis club en España
# ─────────────────────────────────────────────────────────────────

TITULO_1 = "Cómo hacerse socio de un cannabis club en España: guía paso a paso"
SLUG_1   = "como-hacerse-socio-cannabis-club-espana-guia"
RESUMEN_1 = (
    "¿Quieres unirte a un cannabis social club en España pero no sabes por dónde empezar? "
    "Te explicamos exactamente cómo funciona el proceso de membresía, qué requisitos necesitas "
    "y qué esperar una vez dentro. Sin misterios."
)
CONTENIDO_1 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
Los cannabis social clubs en España no son tiendas ni bares: son asociaciones privadas
con un modelo de membresía muy específico. Entender cómo funcionan es el primer paso
para disfrutar de ellos de forma responsable y legal.
</p>

<h2>¿Qué es exactamente un cannabis social club?</h2>

<p>Un cannabis social club (también llamado asociación cannábica) es una entidad privada
sin ánimo de lucro formada por adultos que se asocian para <strong>el consumo compartido
de cannabis en un espacio privado</strong>. No es un comercio: no hay venta al público,
no hay precios de mercado y no es accesible sin membresía previa.</p>

<p>El modelo se sustenta en la jurisprudencia del <strong>Tribunal Supremo español</strong>,
que desde los años 90 ha consolidado que el consumo compartido entre adultos en espacios
privados no es punible, siempre que se cumplan ciertos requisitos (cantidad limitada,
espacio realmente privado, número acotado de socios).</p>

<blockquote>
<strong>Fuente legal:</strong> Sentencia del Tribunal Supremo 484/2015, de 7 de septiembre,
y doctrina consolidada sobre el consumo compartido. Federación de Asociaciones Cannábicas (FAC),
<a href="https://federacioncannabica.org/" target="_blank" rel="noopener noreferrer"
   style="color:#7ed957;">federacioncannabica.org</a>.
</blockquote>

<h2>Requisitos para hacerse socio</h2>

<p>Cada club establece sus propias normas de admisión dentro del marco legal, pero
los requisitos habituales son:</p>

<ul>
  <li>✅ <strong>Ser mayor de 18 años</strong> (o la mayoría de edad legal del país de residencia).</li>
  <li>✅ <strong>Ser presentado por un socio existente</strong> — la mayoría de clubes requieren
  que un miembro actual te avale o invite. Esto garantiza que el club siga siendo una comunidad
  real y no una puerta abierta al público general.</li>
  <li>✅ <strong>Firmar el reglamento interno</strong> — al hacerte socio aceptas las normas
  del club: horarios, comportamiento, cantidades permitidas, etc.</li>
  <li>✅ <strong>Pagar la cuota de membresía</strong> — no es el precio de un producto, sino
  la contribución al mantenimiento de la asociación (local, suministros, gestión).</li>
</ul>

<h2>El proceso paso a paso</h2>

<ol>
  <li><strong>Contacta con el club</strong> — por WhatsApp, email o redes sociales.
  No vayas directamente a la dirección sin contacto previo: los clubes privados no tienen
  entrada libre.</li>
  <li><strong>Conóceles</strong> — muchos clubes hacen una breve reunión o entrevista
  para asegurarse de que encajas en la comunidad y entiendes el modelo.</li>
  <li><strong>Presenta tu documentación</strong> — DNI o pasaporte. Algunos clubes
  también piden domicilio en España o en la región.</li>
  <li><strong>Firma el reglamento</strong> — lee bien las normas antes de firmar.
  Es un compromiso real.</li>
  <li><strong>Abona la cuota</strong> — y ya eres socio. A partir de aquí tienes acceso
  al espacio y a los productos del club según las normas internas.</li>
</ol>

<h2>Qué esperar dentro del club</h2>

<p>Los cannabis social clubs de calidad ofrecen mucho más que acceso a producto.
En un buen club encontrarás:</p>

<ul>
  <li>🌿 <strong>Producto de calidad</strong> — idealmente de autocultivo propio,
  con trazabilidad y variedad.</li>
  <li>🤝 <strong>Comunidad real</strong> — personas con intereses comunes, no un
  local anónimo.</li>
  <li>📚 <strong>Información y educación</strong> — sobre variedades, consumo responsable,
  reducción de riesgos.</li>
  <li>🎵 <strong>Eventos y actividades</strong> — charlas, música, exposiciones.</li>
</ul>

<h2>Cómo unirte a Green Dome en Sevilla</h2>

<p>En <strong>Green Dome</strong>, nuestro cannabis social club privado en Sevilla (barrio de Nervión),
el proceso es sencillo: contáctanos por WhatsApp o Instagram, te explicamos todo en persona
y si encajas en nuestra comunidad, eres bienvenido. Somos una asociación sin ánimo de lucro
con autocultivo propio y una comunidad activa desde noviembre de 2025.</p>

<ul>
  <li>📱 WhatsApp: <strong>+34681296703</strong></li>
  <li>📸 Instagram: <a href="https://instagram.com/greendomegd" target="_blank" rel="noopener noreferrer"
      style="color:#7ed957;">@greendomegd</a></li>
  <li>📧 Email: lacupulaverdesv@gmail.com</li>
</ul>

<hr>

<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Federación de Asociaciones Cannábicas (FAC) ·
STS 484/2015 del Tribunal Supremo español ·
Observatorio Español de la Droga y las Adicciones (OEDA), Ministerio de Sanidad, 2023.
</p>
"""


# ─────────────────────────────────────────────────────────────────
# ARTÍCULO 2 — CBD vs THC
# ─────────────────────────────────────────────────────────────────

TITULO_2 = "CBD vs THC: diferencias, efectos y usos — la guía definitiva"
SLUG_2   = "cbd-vs-thc-diferencias-efectos-usos-guia"
RESUMEN_2 = (
    "CBD y THC son los dos cannabinoides más conocidos del cannabis, pero actúan "
    "de forma completamente diferente en tu cuerpo. Te explicamos la ciencia detrás "
    "de cada uno, sus efectos, usos y por qué no son lo mismo."
)
CONTENIDO_2 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
El cannabis contiene más de 100 cannabinoides, pero dos dominan la conversación:
el <strong>THC</strong> (tetrahidrocannabinol) y el <strong>CBD</strong> (cannabidiol).
Entender su diferencia es fundamental para cualquier consumidor informado.
</p>

<h2>¿Qué es el THC?</h2>

<p>El <strong>tetrahidrocannabinol (THC)</strong> es el principal cannabinoide psicoactivo
del cannabis. Es responsable del efecto euforizante («el subidón») que muchas personas
asocian con el consumo de marihuana.</p>

<p>El THC actúa principalmente sobre los <strong>receptores CB1</strong> del sistema
endocannabinoide, concentrados en el cerebro y el sistema nervioso central.
Al unirse a estos receptores, altera la liberación de neurotransmisores como la
dopamina y el GABA, produciendo cambios en la percepción, el estado de ánimo,
la memoria a corto plazo y el apetito.</p>

<blockquote>
<strong>Fuente científica:</strong> Mechoulam, R. y Gaoni, Y.,
«A Total Synthesis of dl-Δ1-Tetrahydrocannabinol, the Active Constituent of Hashish»,
<em>Journal of the American Chemical Society</em>, 1965.
Este fue el primer aislamiento y síntesis total del THC —
uno de los artículos más citados en la historia de la química médica.
</blockquote>

<h2>¿Qué es el CBD?</h2>

<p>El <strong>cannabidiol (CBD)</strong> es el segundo cannabinoide más abundante en el cannabis.
A diferencia del THC, <strong>no es psicoactivo</strong>: no produce euforia ni altera
la percepción de forma significativa.</p>

<p>El CBD actúa sobre múltiples receptores — CB1 y CB2, pero también sobre receptores
de serotonina (5-HT1A), receptores de vainilloide (TRPV1) y otros —
lo que explica su amplio espectro de efectos potenciales. Investigaciones clínicas han
respaldado su uso en el tratamiento de la epilepsia refractaria
(la FDA aprobó Epidiolex, un medicamento de CBD, en 2018).</p>

<blockquote>
<strong>Fuente científica:</strong> Devinsky, O. et al.,
«Cannabidiol in Dravet Syndrome Study Group»,
<em>New England Journal of Medicine</em>, vol. 376, 2017, pp. 2011-2020.
Estudio clínico de referencia sobre el uso de CBD en epilepsia pediátrica.
</blockquote>

<h2>Tabla comparativa: CBD vs THC</h2>

<table style="width:100%;border-collapse:collapse;margin:2rem 0;color:#ddd;">
  <thead>
    <tr style="background:rgba(126,217,87,.1);border-bottom:2px solid rgba(126,217,87,.3);">
      <th style="text-align:left;padding:.8rem 1rem;color:#7ed957;">Característica</th>
      <th style="text-align:left;padding:.8rem 1rem;color:#7ed957;">THC</th>
      <th style="text-align:left;padding:.8rem 1rem;color:#7ed957;">CBD</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);">
      <td style="padding:.8rem 1rem;"><strong>Psicoactividad</strong></td>
      <td style="padding:.8rem 1rem;">Sí — produce euforia</td>
      <td style="padding:.8rem 1rem;">No</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);background:rgba(255,255,255,.02);">
      <td style="padding:.8rem 1rem;"><strong>Receptor principal</strong></td>
      <td style="padding:.8rem 1rem;">CB1 (cerebro)</td>
      <td style="padding:.8rem 1rem;">Múltiples (CB2, 5-HT1A, TRPV1…)</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);">
      <td style="padding:.8rem 1rem;"><strong>Efectos comunes</strong></td>
      <td style="padding:.8rem 1rem;">Euforia, relajación, aumento apetito, analgesia</td>
      <td style="padding:.8rem 1rem;">Ansiolítico, antiinflamatorio, antiepiléptico, antipsicótico</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);background:rgba(255,255,255,.02);">
      <td style="padding:.8rem 1rem;"><strong>Efectos adversos</strong></td>
      <td style="padding:.8rem 1rem;">Ansiedad (dosis alta), memoria a corto plazo, paranoia</td>
      <td style="padding:.8rem 1rem;">Muy pocos; posible somnolencia en dosis altas</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);">
      <td style="padding:.8rem 1rem;"><strong>Estado legal España</strong></td>
      <td style="padding:.8rem 1rem;">Controlado (consumo privado no penalizado)</td>
      <td style="padding:.8rem 1rem;">Legal si &lt;0,2% THC (uso tópico/alimentario)</td>
    </tr>
    <tr style="background:rgba(255,255,255,.02);">
      <td style="padding:.8rem 1rem;"><strong>Detectado en test de drogas</strong></td>
      <td style="padding:.8rem 1rem;">Sí (hasta 30 días en orina)</td>
      <td style="padding:.8rem 1rem;">No (si es CBD puro sin THC)</td>
    </tr>
  </tbody>
</table>

<h2>El efecto séquito: cuando CBD y THC se necesitan mutuamente</h2>

<p>Una de las ideas más interesantes de la investigación cannábica moderna es el
<strong>«efecto séquito»</strong> (<em>entourage effect</em>), propuesto por el
investigador israelí <strong>Raphael Mechoulam</strong> (el mismo que aisló el THC en 1964).
La tesis: los cannabinoides, terpenos y flavonoides del cannabis actúan
<em>sinérgicamente</em> — el conjunto produce efectos diferentes (y a menudo más beneficiosos)
que cada componente por separado.</p>

<p>En la práctica, esto significa que el CBD puede <strong>modular los efectos del THC</strong>:
reduce la ansiedad y los efectos psicóticos que algunos experimentan con el THC solo.
Las variedades con ratio THC:CBD equilibrado (por ejemplo, 1:1) suelen producir
experiencias más suaves y manejables que las variedades de THC alto puro.</p>

<blockquote>
<strong>Fuente:</strong> Russo, E.B., «Taming THC: potential cannabis synergy and phytocannabinoid-terpenoid entourage effects»,
<em>British Journal of Pharmacology</em>, vol. 163, n.º 7, 2011, pp. 1344-1364.
</blockquote>

<h2>¿CBD o THC? Depende de lo que busques</h2>

<ul>
  <li>🧘 Si buscas <strong>relajación sin euforia</strong>: CBD o variedades de ratio alto CBD:THC.</li>
  <li>🌙 Si buscas <strong>alivio del insomnio</strong>: variedades con terpenos como mirceno y linalool,
  con THC moderado.</li>
  <li>😌 Si buscas <strong>experiencia social y recreativa</strong>: variedades equilibradas o de THC moderado.</li>
  <li>⚠️ Si eres <strong>principiante</strong>: empieza siempre con dosis bajas de THC
  y variedades con CBD para modular el efecto.</li>
</ul>

<hr>

<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Mechoulam & Gaoni (1965) · Devinsky et al. (2017, NEJM) ·
Russo (2011, BJP) · European Monitoring Centre for Drugs and Drug Addiction (EMCDDA),
<em>Cannabis drug profile</em>, 2023 ·
Agencia Española de Medicamentos (AEMPS), ficha técnica de Epidiolex.
</p>
"""


# ─────────────────────────────────────────────────────────────────
# ARTÍCULO 3 — Historia de los clubes cannábicos en España
# ─────────────────────────────────────────────────────────────────

TITULO_3 = "Historia de los clubes cannábicos en España: del underground a la legalidad"
SLUG_3   = "historia-clubes-cannabicos-espana-modelo-asociativo"
RESUMEN_3 = (
    "España tiene uno de los modelos de cannabis más originales del mundo: "
    "las asociaciones cannábicas privadas. ¿Cómo surgieron? ¿Qué dice la ley? "
    "Y por qué Sevilla se ha convertido en uno de sus epicentros. Historia completa."
)
CONTENIDO_3 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
El modelo asociativo cannábico español es único en el mundo: no es legal en el sentido de
«tienda abierta», pero tampoco es ilegal si se cumplen ciertos principios.
Es un espacio jurídico peculiar que ha permitido desarrollar una cultura cannábica
organizada, responsable y comunitaria.
</p>

<h2>Los orígenes: el País Vasco y la ARSECA (1991)</h2>

<p>Todo comenzó en el País Vasco. En <strong>1991</strong>, un grupo de activistas cannábicos
vascos fundó la primera asociación de este tipo en España:
la <strong>ARSECA</strong> (Asociación Ramón Santos de Estudios sobre el Cannabis).
Su propósito era crear un espacio de estudio, debate e información sobre el cannabis.</p>

<p>La ARSECA inspiró el surgimiento de la <strong>Kalamudia</strong> en 1993,
considerada el primer club cannábico en sentido moderno: un espacio privado donde
los socios podían cultivar y consumir de forma colectiva. La Policía los investigó,
pero el juicio resultó en sobreseimiento — sentando uno de los primeros precedentes
jurídicos del modelo.</p>

<blockquote>
<strong>Fuente:</strong> Arana, X. y Markez, I., «Cannabis Policies in the Basque Country»,
en <em>A Cannabis Reader: Global Issues and Local Experiences</em>,
European Monitoring Centre for Drugs and Drug Addiction (EMCDDA), 2008.
</blockquote>

<h2>La jurisprudencia del Tribunal Supremo (1990-2015)</h2>

<p>El andamiaje jurídico del modelo español se construyó, ladrillo a ladrillo,
a través de sentencias del Tribunal Supremo que fueron delimitando qué constituía
consumo compartido «no punible»:</p>

<ul>
  <li><strong>STS de 1993</strong>: establece que la tenencia de cannabis para consumo propio
  no es tráfico de drogas.</li>
  <li><strong>STS 679/1996</strong>: el consumo compartido entre adultos en espacio privado
  no es delito, siempre que sea inmediato, entre número reducido de personas
  y sin ánimo de lucro.</li>
  <li><strong>STS 484/2015</strong>: la sentencia más citada. Establece los cuatro requisitos
  del consumo compartido impune: <em>(1) cantidad limitada, (2) inmediatez en el consumo,
  (3) número reducido de socios, (4) espacio realmente privado y cerrado</em>.</li>
</ul>

<p>Esta jurisprudencia acumulada no equivale a legalización, pero crea un espacio
de tolerancia real que los clubs han aprovechado para organizarse.</p>

<blockquote>
<strong>Fuente:</strong> Sentencia del Tribunal Supremo 484/2015, Sala de lo Penal,
de 7 de septiembre de 2015. Ponente: José Ramón Soriano Soriano.
</blockquote>

<h2>El boom de los clubs: 2010-2018</h2>

<p>Entre 2010 y 2018 el modelo explotó, especialmente en el País Vasco,
Cataluña y Andalucía. La razón fue la conjunción de varios factores:</p>

<ul>
  <li>🌱 La consolidación jurisprudencial daba mayor seguridad legal.</li>
  <li>📱 Las redes sociales permitieron visibilizar los clubs y atraer socios.</li>
  <li>🌍 El modelo se exportó internacionalmente — Uruguay, Bélgica y otros países
  lo estudiaron como alternativa a la prohibición total.</li>
  <li>💪 La <strong>Federación de Asociaciones Cannábicas (FAC)</strong>, fundada en 2010,
  ofreció respaldo, formación y lobby político.</li>
</ul>

<p>En 2015, España tenía más de <strong>800 clubs registrados</strong>, según estimaciones
de la FAC, con una concentración especial en Barcelona y el País Vasco.</p>

<h2>Andalucía y Sevilla: el sur se incorpora</h2>

<p>Mientras el norte llevaba la delantera, Andalucía tardó algo más en desarrollar
su escena asociativa. Sin embargo, la calidad del clima y la cultura del sur pronto
convirtieron a ciudades como Sevilla, Málaga y Granada en polos de crecimiento.</p>

<p>En Sevilla, el barrio de <strong>Nervión</strong> se ha convertido en uno de los
epicentros de la cultura cannábica sevillana. La mezcla de barrio universitario,
clase media joven y cultura de barrio ha favorecido el surgimiento de clubs como
<strong>Green Dome</strong>, comprometidos con la calidad del producto,
la educación y la construcción de comunidad real.</p>

<h2>El debate legal actual: ¿hacia la regulación?</h2>

<p>Desde 2018, el debate político sobre la regulación del cannabis en España
se ha intensificado. Varios partidos (Más País, Podemos, algunos sectores del PSOE)
han presentado proposiciones de ley. Sin embargo, ninguna ha prosperado
en el Congreso hasta la fecha.</p>

<p>La posición de la mayoría de clubs no es tanto pedir la legalización comercial
como el <strong>reconocimiento explícito del modelo asociativo</strong>:
un marco legal claro que proteja a los socios y a las asociaciones de la
inseguridad jurídica actual.</p>

<blockquote>
<strong>Fuente:</strong> Observatorio Español de la Droga y las Adicciones (OEDA),
<em>Informe 2023 sobre el cannabis en España</em>.
Ministerio de Sanidad, Gobierno de España. Disponible en
<a href="https://pnsd.sanidad.gob.es/" target="_blank" rel="noopener noreferrer"
   style="color:#7ed957;">pnsd.sanidad.gob.es</a>.
</blockquote>

<hr>

<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Arana & Markez (EMCDDA, 2008) ·
STS 679/1996 · STS 484/2015 ·
Federación de Asociaciones Cannábicas (FAC) ·
OEDA, Informe sobre cannabis 2023, Ministerio de Sanidad.
</p>
"""


# ─────────────────────────────────────────────────────────────────
# ARTÍCULO 4 — Autocultivo de cannabis en España: qué dice la ley
# ─────────────────────────────────────────────────────────────────

TITULO_4 = "Autocultivo de cannabis en España: qué dice la ley y qué dice la realidad"
SLUG_4   = "autocultivo-cannabis-espana-que-dice-la-ley"
RESUMEN_4 = (
    "Cultivar cannabis en España es uno de los temas más confusos del panorama legal. "
    "¿Es legal? ¿Cuántas plantas puedo tener? ¿Qué diferencia hay entre interior y exterior? "
    "Analizamos la situación legal real y los límites que debes conocer."
)
CONTENIDO_4 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
El autocultivo de cannabis en España vive en una zona gris legal que genera mucha confusión.
No es completamente legal, pero tampoco es un delito penal si se hace en privado
y sin ánimo de lucro. La clave está en entender exactamente dónde están los límites.
</p>

<h2>El marco legal: Código Penal y Ley de Seguridad Ciudadana</h2>

<p>España regula el cannabis principalmente a través de dos normas:</p>

<ul>
  <li><strong>Código Penal (artículo 368)</strong>: penaliza el cultivo, elaboración,
  tráfico y posesión con fines de tráfico de sustancias ilícitas. La clave es
  el elemento <em>«para el tráfico»</em>: el consumo propio y el cultivo para
  consumo propio no están tipificados como delito penal, según la jurisprudencia
  consolidada del Tribunal Supremo.</li>
  <li><strong>Ley Orgánica 4/2015 de Seguridad Ciudadana («Ley Mordaza»,
  artículo 36.18)</strong>: tipifica como infracción administrativa grave
  el consumo o tenencia de drogas en la vía pública o en lugares de acceso público.
  La sanción es una multa de entre 601 y 30.000 €. Esto no implica antecedentes penales,
  pero sí económicos.</li>
</ul>

<blockquote>
<strong>Fuente legal:</strong> Código Penal español, LO 10/1995 (art. 368) ·
Ley Orgánica 4/2015 de Protección de la Seguridad Ciudadana (art. 36.18) ·
STS 484/2015, Sala de lo Penal.
</blockquote>

<h2>¿Cuántas plantas puedo cultivar?</h2>

<p>Esta es la pregunta más habitual — y la respuesta es que <strong>no hay un número mágico
establecido en la ley española</strong>. A diferencia de otros países (Alemania permite
3 plantas desde 2024; Holanda permite 5), España no ha fijado un umbral legal
explícito para el autocultivo.</p>

<p>Lo que establece la jurisprudencia es que el cultivo para consumo personal,
en espacio privado, sin ánimo de lucro y con cantidad razonable
puede no ser perseguido penalmente. Pero «razonable» es un concepto elástico
que depende del criterio del juez o fiscal.</p>

<p>En la práctica, las sentencias absolutorias suelen referirse a
<strong>1 a 3 plantas para consumo propio</strong>. A partir de 5-6 plantas,
los tribunales tienden a presumir intención de tráfico salvo prueba en contrario.</p>

<h2>Interior vs exterior: ¿importa dónde cultivas?</h2>

<p>Sí, importa mucho. El criterio fundamental es la <strong>visibilidad pública</strong>:</p>

<ul>
  <li>🏠 <strong>Interior (grow tent, armario, cuarto):</strong> es la opción con menor
  riesgo legal. Al estar en espacio privado y cerrado, cumple el requisito de
  «espacio privado» de la jurisprudencia del TS. Nadie puede ver las plantas
  sin entrar en tu domicilio (que requiere orden judicial).</li>
  <li>🌞 <strong>Terraza privada:</strong> zona gris. Si las plantas son visibles
  desde la calle, espacio público o propiedades vecinas, puede considerarse
  «difusión pública» y aplicarse la Ley de Seguridad Ciudadana.</li>
  <li>🌳 <strong>Exterior en jardín privado:</strong> similar a terraza. Depende
  de la visibilidad. Un jardín vallado y no visible desde el exterior reduce el riesgo.</li>
  <li>⚠️ <strong>Espacio público, comunidades o zonas comunes:</strong> siempre
  infracción administrativa y potencialmente penal si la cantidad es significativa.</li>
</ul>

<h2>Autocultivo colectivo: el modelo de los clubs cannábicos</h2>

<p>Una de las soluciones más elegantes al problema del autocultivo individual es el
<strong>autocultivo colectivo dentro de una asociación cannábica</strong>.
En este modelo:</p>

<ul>
  <li>🌿 El cultivo se realiza en nombre de la asociación (no de cada socio individualmente).</li>
  <li>📋 Está respaldado por los estatutos y el reglamento de la asociación.</li>
  <li>🔒 Tiene lugar en espacio privado y controlado.</li>
  <li>📊 La cantidad se determina por el número de socios y sus necesidades declaradas,
  no por criterios de mercado.</li>
</ul>

<p>En <strong>Green Dome</strong>, nuestro cannabis social club privado en Sevilla,
el autocultivo propio es uno de nuestros pilares. Nos permite garantizar
calidad premium, trazabilidad completa del proceso y precios accesibles para los socios,
todo dentro del marco del modelo asociativo español.</p>

<h2>Alemania 2024: un ejemplo a seguir</h2>

<p>En abril de 2024, Alemania entró en vigor la primera fase de su ley de legalización,
permitiendo hasta <strong>3 plantas por adulto para consumo propio</strong>
y clubs privados de hasta 500 miembros (llamados
<em>«Cannabis Social Clubs»</em>, calcado del modelo español).
Esta regulación ha dado un impulso enorme al debate en España sobre la necesidad
de clarificar el marco legal del autocultivo y el modelo asociativo.</p>

<blockquote>
<strong>Fuente:</strong> Bundesgesundheitsministerium (Ministerio Federal de Salud de Alemania),
<em>Gesetz zum kontrollierten Umgang mit Cannabis (CanG)</em>, en vigor desde el 1 de abril de 2024.
European Monitoring Centre for Drugs and Drug Addiction,
<a href="https://www.emcdda.europa.eu/" target="_blank" rel="noopener noreferrer"
   style="color:#7ed957;">emcdda.europa.eu</a> — informes de seguimiento.
</blockquote>

<hr>

<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Código Penal español, LO 10/1995 ·
Ley Orgánica 4/2015 de Seguridad Ciudadana ·
STS 484/2015 · Bundesgesundheitsministerium (Alemania, CanG 2024) ·
EMCDDA, <em>Drug Policy Profiles — Spain</em>, 2023.
</p>
"""


# ─────────────────────────────────────────────────────────────────
# MIGRACIÓN
# ─────────────────────────────────────────────────────────────────

def crear_articulos(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')

    # Artículo 1 — Cómo hacerse socio
    BlogPost.objects.get_or_create(
        slug=SLUG_1,
        defaults={
            'titulo':    TITULO_1,
            'resumen':   RESUMEN_1,
            'contenido': CONTENIDO_1,
            'autor':     'Green Dome',
            'publicado': True,
            'fecha_pub': timezone.make_aware(datetime(2026, 1, 15, 10, 0, 0)),
        }
    )

    # Artículo 2 — CBD vs THC
    BlogPost.objects.get_or_create(
        slug=SLUG_2,
        defaults={
            'titulo':    TITULO_2,
            'resumen':   RESUMEN_2,
            'contenido': CONTENIDO_2,
            'autor':     'Green Dome',
            'publicado': True,
            'fecha_pub': timezone.make_aware(datetime(2026, 2, 5, 10, 0, 0)),
        }
    )

    # Artículo 3 — Historia clubs cannábicos España
    BlogPost.objects.get_or_create(
        slug=SLUG_3,
        defaults={
            'titulo':    TITULO_3,
            'resumen':   RESUMEN_3,
            'contenido': CONTENIDO_3,
            'autor':     'Green Dome',
            'publicado': True,
            'fecha_pub': timezone.make_aware(datetime(2026, 2, 20, 10, 0, 0)),
        }
    )

    # Artículo 4 — Autocultivo en España
    BlogPost.objects.get_or_create(
        slug=SLUG_4,
        defaults={
            'titulo':    TITULO_4,
            'resumen':   RESUMEN_4,
            'contenido': CONTENIDO_4,
            'autor':     'Green Dome',
            'publicado': True,
            'fecha_pub': timezone.make_aware(datetime(2026, 3, 10, 10, 0, 0)),
        }
    )


def eliminar_articulos(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    BlogPost.objects.filter(
        slug__in=[SLUG_1, SLUG_2, SLUG_3, SLUG_4]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_blog_rastafari_y_comestibles'),
    ]

    operations = [
        migrations.RunPython(crear_articulos, eliminar_articulos),
    ]
