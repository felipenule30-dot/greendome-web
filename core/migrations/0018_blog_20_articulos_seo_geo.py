"""
Data migration: 20 artículos nuevos del blog de Green Dome.
Temáticas: sistema endocannabinoide, cannabinoides, efectos,
microdosis, vaporización, legalización Europa, cannabis medicinal, etc.
"""
from django.db import migrations
from django.utils import timezone
from datetime import datetime

# ─── ARTÍCULO 1 — Sistema endocannabinoide ───────────────────────
TITULO_1 = "El sistema endocannabinoide: el sistema que nadie te enseñó en biología"
SLUG_1   = "sistema-endocannabinoide-que-es-como-funciona"
RESUMEN_1 = (
    "Tu cuerpo tiene un sistema diseñado para interactuar con el cannabis. "
    "El sistema endocannabinoide regula el dolor, el sueño, el apetito y el estado de ánimo. "
    "Guía completa con ciencia real."
)
CONTENIDO_1 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
El sistema endocannabinoide (SEC) es uno de los sistemas fisiológicos más importantes del cuerpo humano
y, sin embargo, apenas se estudia en educación secundaria ni en muchas facultades de medicina.
Fue descubierto precisamente porque los investigadores buscaban entender cómo actúa el cannabis.
</p>

<h2>¿Qué es el sistema endocannabinoide?</h2>
<p>El SEC es una red de receptores, moléculas señalizadoras (endocannabinoides) y enzimas
distribuida por todo el organismo. Su función principal es mantener la <strong>homeostasis</strong>:
el equilibrio interno del cuerpo ante cambios externos e internos.</p>

<p>Fue descubierto en los años 90 por el equipo del Dr. <strong>Raphael Mechoulam</strong>
en la Universidad Hebrea de Jerusalén, el mismo investigador que había aislado el THC
en 1964. Al estudiar cómo el THC afectaba al cerebro, encontraron receptores específicos
(CB1) y después los ligandos naturales del cuerpo que los activan: los endocannabinoides.</p>

<blockquote>
<strong>Fuente:</strong> Devane, W.A. et al., «Isolation and structure of a brain constituent
that binds to the cannabinoid receptor», <em>Science</em>, vol. 258, 1992, pp. 1946-1949.
Primer aislamiento de la anandamida (AEA), el principal endocannabinoide endógeno.
</blockquote>

<h2>Los tres componentes del SEC</h2>
<ul>
  <li><strong>Receptores cannabinoides:</strong> CB1 (principalmente en sistema nervioso central)
  y CB2 (principalmente en sistema inmune y tejidos periféricos).</li>
  <li><strong>Endocannabinoides:</strong> moléculas producidas por el propio cuerpo. Las principales son
  la <strong>anandamida (AEA)</strong> — llamada «la molécula de la beatitud» — y el
  <strong>2-araquidonoilglicerol (2-AG)</strong>.</li>
  <li><strong>Enzimas:</strong> producen y degradan los endocannabinoides según necesidad
  (FAAH degrada AEA; MAGL degrada 2-AG).</li>
</ul>

<h2>¿Qué regula el sistema endocannabinoide?</h2>
<ul>
  <li>🧠 <strong>Dolor y nocicepción</strong> — modula la percepción del dolor crónico y agudo.</li>
  <li>😴 <strong>Ciclos de sueño</strong> — la anandamida promueve el sueño profundo.</li>
  <li>🍽️ <strong>Apetito y metabolismo</strong> — CB1 activa el apetito (el clásico «munchies»).</li>
  <li>😰 <strong>Respuesta al estrés y ansiedad</strong> — modula el eje hipotálamo-hipófisis-suprarrenal.</li>
  <li>🧠 <strong>Memoria y aprendizaje</strong> — el olvido adaptativo es parcialmente endocannabinoide.</li>
  <li>🛡️ <strong>Inflamación e inmunidad</strong> — CB2 regula la respuesta inflamatoria.</li>
</ul>

<h2>¿Por qué el cannabis afecta al SEC?</h2>
<p>Los fitocannabinoides (cannabinoides de la planta, como THC y CBD) son molecularmente
similares a los endocannabinoides del cuerpo. El THC se une directamente a los receptores CB1
imitando a la anandamida — pero con mayor potencia y duración. El CBD actúa de forma
más indirecta, modulando el SEC sin unirse con fuerza a CB1 o CB2.</p>

<h2>Deficiencia endocannabinoide clínica</h2>
<p>El Dr. <strong>Ethan Russo</strong> propuso en 2004 la hipótesis de la
<em>«deficiencia endocannabinoide clínica»</em>: condiciones como la migraña,
el síndrome del intestino irritable y la fibromialgia podrían estar relacionadas
con un SEC hipoactivo. Esta hipótesis sigue siendo investigada activamente.</p>

<blockquote>
<strong>Fuente:</strong> Russo, E.B., «Clinical Endocannabinoid Deficiency»,
<em>Neuroendocrinology Letters</em>, vol. 25, 2004, pp. 31-39.
</blockquote>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Devane et al. (Science, 1992) · Mechoulam (Hebrew University) ·
Russo (2004, Neuroendocrinology Letters) · Di Marzo, V., «The endocannabinoid system»,
<em>Nature Reviews Drug Discovery</em>, 2018.
</p>
"""

# ─── ARTÍCULO 2 — Receptores CB1 y CB2 ──────────────────────────
TITULO_2 = "Receptores CB1 y CB2: dónde están, qué hacen y por qué importan"
SLUG_2   = "receptores-cb1-cb2-diferencias-funciones"
RESUMEN_2 = (
    "Los receptores CB1 y CB2 son la puerta de entrada del cannabis a tu cuerpo. "
    "Descubre dónde se concentran, qué efectos activan y por qué son el objetivo "
    "de los nuevos medicamentos cannabinoides."
)
CONTENIDO_2 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
Los receptores cannabinoides CB1 y CB2 son proteínas de membrana que actúan como
interruptores moleculares. Cuando un cannabinoide — propio del cuerpo o de la planta —
se une a ellos, desencadena una cascada de efectos fisiológicos. Entenderlos es la clave
para entender qué hace el cannabis en cada parte del cuerpo.
</p>

<h2>El receptor CB1: el gran actor del sistema nervioso</h2>
<p>El receptor <strong>CB1</strong> fue clonado por primera vez en 1990 por Matsuda et al.
Es el receptor más abundante del sistema nervioso central — hay más receptores CB1
en el cerebro que de cualquier otro tipo de receptor acoplado a proteína G.</p>

<p>Se concentra especialmente en:</p>
<ul>
  <li><strong>Corteza cerebral</strong> — cognición, toma de decisiones, percepción.</li>
  <li><strong>Hipocampo</strong> — memoria y aprendizaje.</li>
  <li><strong>Ganglios basales</strong> — coordinación motora.</li>
  <li><strong>Cerebelo</strong> — equilibrio y movimiento.</li>
  <li><strong>Amígdala</strong> — respuesta emocional y ansiedad.</li>
  <li><strong>Tronco encefálico</strong> — pero NO en los centros respiratorios
  (razón por la que el cannabis no puede causar sobredosis respiratoria).</li>
</ul>

<blockquote>
<strong>Fuente:</strong> Matsuda, L.A. et al., «Structure of a cannabinoid receptor
and functional expression of the cloned cDNA», <em>Nature</em>, vol. 346, 1990, pp. 561-564.
Clonación del receptor CB1 — artículo fundacional de la neurociencia cannábica.
</blockquote>

<h2>El receptor CB2: el guardián del sistema inmune</h2>
<p>El receptor <strong>CB2</strong> fue clonado en 1993 por Munro et al. A diferencia del CB1,
se encuentra principalmente fuera del sistema nervioso central:</p>
<ul>
  <li><strong>Células inmunes:</strong> linfocitos T, macrófagos, células NK, células B.</li>
  <li><strong>Bazo, amígdalas, timo</strong> — órganos inmunes.</li>
  <li><strong>Médula ósea</strong> — producción de células sanguíneas.</li>
  <li><strong>Hígado y tracto gastrointestinal</strong> — en menor densidad.</li>
</ul>

<p>Su activación reduce la respuesta inflamatoria y modula el sistema inmune,
lo que lo convierte en diana terapéutica para enfermedades autoinmunes,
dolor crónico inflamatorio y condiciones neurológicas como el Alzheimer.</p>

<blockquote>
<strong>Fuente:</strong> Munro, S. et al., «Molecular characterization of a peripheral
receptor for cannabinoids», <em>Nature</em>, vol. 365, 1993, pp. 61-65.
</blockquote>

<h2>CB1 vs CB2: tabla comparativa</h2>
<table style="width:100%;border-collapse:collapse;margin:2rem 0;color:#ddd;">
  <thead>
    <tr style="background:rgba(126,217,87,.1);border-bottom:2px solid rgba(126,217,87,.3);">
      <th style="text-align:left;padding:.8rem;color:#7ed957;">Característica</th>
      <th style="text-align:left;padding:.8rem;color:#7ed957;">CB1</th>
      <th style="text-align:left;padding:.8rem;color:#7ed957;">CB2</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);">
      <td style="padding:.8rem;"><strong>Localización principal</strong></td>
      <td style="padding:.8rem;">Sistema nervioso central</td>
      <td style="padding:.8rem;">Sistema inmune, tejidos periféricos</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);background:rgba(255,255,255,.02);">
      <td style="padding:.8rem;"><strong>Efectos al activarse</strong></td>
      <td style="padding:.8rem;">Euforia, analgesia, apetito, sedación</td>
      <td style="padding:.8rem;">Antiinflamatorio, inmunomodulador</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);">
      <td style="padding:.8rem;"><strong>THC se une a</strong></td>
      <td style="padding:.8rem;">Sí (agonista parcial)</td>
      <td style="padding:.8rem;">Sí (agonista parcial)</td>
    </tr>
    <tr style="background:rgba(255,255,255,.02);">
      <td style="padding:.8rem;"><strong>CBD actúa en</strong></td>
      <td style="padding:.8rem;">Antagonista/modulador alostérico</td>
      <td style="padding:.8rem;">Modulador indirecto</td>
    </tr>
  </tbody>
</table>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Matsuda et al. (Nature, 1990) · Munro et al. (Nature, 1993) ·
Pertwee, R.G., «Cannabinoid pharmacology: the first 66 years»,
<em>British Journal of Pharmacology</em>, 2006.
</p>
"""

# ─── ARTÍCULO 3 — Nuevos cannabinoides (HHC, THCV, CBG, CBN) ────
TITULO_3 = "HHC, THCV, CBG, CBN: guía de los nuevos cannabinoides que están cambiando el mercado"
SLUG_3   = "nuevos-cannabinoides-hhc-thcv-cbg-cbn-guia"
RESUMEN_3 = (
    "Más allá del THC y el CBD, existe un universo de cannabinoides con propiedades únicas. "
    "HHC, THCV, CBG y CBN: qué son, qué efectos tienen y qué dice la ciencia sobre cada uno."
)
CONTENIDO_3 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
Durante décadas, el debate sobre el cannabis se redujo a dos nombres: THC y CBD.
Hoy, la investigación cannábica ha identificado más de 140 cannabinoides distintos,
muchos con propiedades farmacológicas únicas. Este es el mapa de los más relevantes.
</p>

<h2>CBG — Cannabigerol: el «cannabinoide madre»</h2>
<p>El CBG es el precursor biosintético de todos los demás cannabinoides.
La planta produce primero CBGA (ácido cannabigerólico), que luego se convierte
en THCA, CBDA y CBCA. Por eso se le llama el «cannabinoide madre».</p>
<ul>
  <li>No es psicoactivo.</li>
  <li>Estudios preliminares sugieren propiedades antibacterianas, neuroprotectoras
  y como posible agente contra el glaucoma (reduce presión intraocular).</li>
  <li>Antagonista de los receptores CB1 a dosis altas — puede moderar el efecto del THC.</li>
</ul>

<h2>CBN — Cannabinol: el cannabinoide del sueño</h2>
<p>El CBN se forma por oxidación del THC: cuando el cannabis envejece o se expone
al oxígeno, el THC se degrada en CBN. Tiene muy baja psicoactividad
(estimada en un 10% del THC).</p>
<ul>
  <li>Su fama principal es como <strong>sedante</strong> — aunque la evidencia clínica
  directa es todavía limitada.</li>
  <li>Combina bien con terpenos como el mirceno y el linalool para efectos relajantes.</li>
  <li>Puede tener propiedades antibacterianas contra MRSA (Staphylococcus resistente).</li>
</ul>

<h2>THCV — Tetrahidrocannabivarina: el «THC de dieta»</h2>
<p>El THCV tiene una estructura similar al THC pero con efectos muy diferentes:</p>
<ul>
  <li>A <strong>dosis bajas</strong>: bloquea los receptores CB1 — suprime el apetito
  (efecto opuesto al «munchies» del THC).</li>
  <li>A <strong>dosis altas</strong>: activa CB1 y produce un efecto psicoactivo
  más claro, corto y estimulante.</li>
  <li>Investigado como potencial tratamiento para la diabetes tipo 2 y la obesidad.</li>
</ul>

<blockquote>
<strong>Fuente:</strong> Abioye, A. et al., «Δ9-Tetrahydrocannabivarin (THCV):
a commentary on potential therapeutic benefit for the management of obesity and diabetes»,
<em>Journal of Cannabis Research</em>, 2020.
</blockquote>

<h2>HHC — Hexahidrocannabinol: el cannabinoide semisintético</h2>
<p>El HHC existe de forma natural en el cannabis (en concentraciones muy bajas)
pero en el mercado actual se produce <strong>semisintéticamente</strong>
por hidrogenación del THC — el mismo proceso que convierte aceite vegetal en margarina.</p>
<ul>
  <li>Tiene efectos psicoactivos comparables al THC, aunque generalmente descritos
  como más suaves y de mayor duración.</li>
  <li>Su estatus legal en Europa es confuso: como no deriva directamente del THC
  de planta, algunos países no lo clasifican igual.</li>
  <li>⚠️ La investigación sobre seguridad a largo plazo es muy limitada.</li>
</ul>

<h2>La regla de oro: confía en lo que conoces</h2>
<p>En <strong>Green Dome</strong>, nuestro enfoque es el cannabis tradicional de calidad:
variedades probadas, terpenos naturales, efecto conocido. Los nuevos cannabinoides
son interesantes desde el punto de vista científico, pero la falta de estudios
de seguridad a largo plazo invita a la prudencia.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Abioye et al. (2020, Journal of Cannabis Research) ·
Pertwee, R.G. (ed.), <em>Handbook of Cannabis</em>, Oxford University Press, 2014 ·
EMCDDA, <em>New cannabis-type substances</em>, 2023.
</p>
"""

# ─── ARTÍCULO 4 — THCP vs THC ────────────────────────────────────
TITULO_4 = "THCP vs THC: el cannabinoide 33 veces más potente que está revolucionando la ciencia"
SLUG_4   = "thcp-vs-thc-cannabinoide-potente-diferencias"
RESUMEN_4 = (
    "En 2019, investigadores italianos descubrieron el THCP: un cannabinoide natural "
    "con una afinidad por los receptores CB1 hasta 33 veces mayor que el THC. "
    "Qué implica este descubrimiento y por qué importa."
)
CONTENIDO_4 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
En diciembre de 2019, un equipo de investigadores italianos publicó en <em>Nature Scientific Reports</em>
el descubrimiento de dos nuevos cannabinoides naturales en la planta de cannabis:
el <strong>THCP</strong> (Δ9-tetrahidrocannabiphorol) y el CBDP.
El THCP demostró en pruebas in vitro una afinidad por los receptores CB1 hasta
<strong>33 veces mayor que el THC</strong>.
</p>

<h2>¿Qué es el THCP?</h2>
<p>El THCP es un fitocanabinoide homólogo del THC: tiene la misma estructura básica
pero con una cadena lateral alquílica de <strong>7 carbonos</strong> en lugar de los
5 que tiene el THC. Esa diferencia estructural aparentemente pequeña tiene
consecuencias enormes en su afinidad por los receptores CB1.</p>

<p>En las pruebas de unión a receptor in vitro del estudio italiano,
el THCP mostró una afinidad por CB1 <strong>33 veces superior al THC</strong>
y 5-10 veces superior por CB2. En modelos animales, los efectos tetráédicos,
hipotérmicos y analgésicos fueron significativamente más potentes que los del THC.</p>

<blockquote>
<strong>Fuente primaria:</strong> Citti, C. et al., «A novel phytocannabinoid isolated from
Cannabis sativa L. with an in vivo cannabimimetic activity higher than Δ9-tetrahydrocannabinol:
Δ9-Tetrahydrocannabiphorol», <em>Scientific Reports</em>, vol. 9, art. 20335, 2019.
</blockquote>

<h2>¿Qué implica para entender la potencia del cannabis?</h2>
<p>Este descubrimiento tiene implicaciones importantes:</p>
<ul>
  <li>El porcentaje de THC puede no explicar completamente la potencia subjetiva
  de una variedad — el THCP (aunque en concentraciones muy bajas) podría contribuir.</li>
  <li>Algunas variedades legendariamente potentes podrían serlo en parte
  por su contenido en THCP u otros cannabinoides menores aún no catalogados.</li>
  <li>Abre nuevas vías de investigación farmacológica para condiciones que requieren
  cannabinoides de alta potencia (dolor crónico severo, espasticidad).</li>
</ul>

<h2>Cautela: in vitro ≠ in vivo en humanos</h2>
<p>Es crucial entender que los datos de afinidad de receptor son estudios
<em>in vitro</em> — en células, no en personas. La potencia en humanos
depende de factores adicionales: absorción, metabolismo, distribución,
tolerancia individual. <strong>No hay estudios clínicos en humanos sobre THCP</strong>
a la fecha de publicación de este artículo.</p>

<h2>¿Está disponible el THCP?</h2>
<p>Sí, en el mercado europeo ya existen productos con THCP semisintético
o concentrado de extracto. Sin embargo, su estatus legal varía según el país
y la investigación de seguridad es mínima. En <strong>Green Dome</strong>
apostamos por cannabinoides bien estudiados y producto de autocultivo propio
con trazabilidad completa — no por novedades sin respaldo científico suficiente.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Citti et al. (<em>Scientific Reports</em>, 2019) ·
Pertwee, R.G., <em>Handbook of Cannabis</em>, Oxford University Press, 2014 ·
EMCDDA, <em>Cannabis drug profile</em>, 2023.
</p>
"""

# ─── ARTÍCULO 5 — Cannabis y dopamina ────────────────────────────
TITULO_5 = "Cannabis y dopamina: lo que la neurociencia dice sobre el placer, la motivación y la dependencia"
SLUG_5   = "cannabis-dopamina-neurociencia-placer-motivacion"
RESUMEN_5 = (
    "¿El cannabis sube o baja la dopamina? La relación entre el THC y el sistema "
    "de recompensa del cerebro es más compleja de lo que crees. "
    "Neurociencia clara para consumidores informados."
)
CONTENIDO_5 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
La dopamina es el neurotransmisor del deseo, la anticipación y el refuerzo.
Todas las sustancias con potencial de uso problemático — desde el azúcar hasta los opioides —
tienen en común que aumentan la dopamina en el núcleo accumbens, el centro de recompensa del cerebro.
¿Qué hace exactamente el cannabis?
</p>

<h2>El mecanismo: cómo el THC afecta a la dopamina</h2>
<p>El THC no actúa directamente sobre los receptores de dopamina.
Su vía es <strong>indirecta</strong>:</p>
<ol>
  <li>El THC se une a receptores CB1 en las neuronas GABAérgicas del área tegmental ventral (ATV).</li>
  <li>Estas neuronas GABA normalmente <em>inhiben</em> las neuronas dopaminérgicas.</li>
  <li>Al bloquear esa inhibición, el THC <strong>desinhibe</strong> las neuronas de dopamina —
  es decir, las libera para disparar más.</li>
  <li>Resultado: aumento de dopamina en el núcleo accumbens y la corteza prefrontal.</li>
</ol>

<blockquote>
<strong>Fuente:</strong> Tanda, G. et al., «Cannabinoid and heroin activation of mesolimbic
dopamine transmission by a common µ1 opioid receptor mechanism»,
<em>Science</em>, vol. 276, 1997, pp. 2048-2050.
</blockquote>

<h2>Consumo crónico: la historia cambia</h2>
<p>Con el consumo frecuente y a largo plazo, los estudios muestran
<strong>reducción de la respuesta dopaminérgica</strong>:</p>
<ul>
  <li>Menos receptores CB1 disponibles (down-regulation).</li>
  <li>Menor liberación de dopamina en el núcleo accumbens ante estímulos de recompensa.</li>
  <li>Este fenómeno puede manifestarse como <strong>síndrome amotivacional</strong>:
  reducción del interés, la iniciativa y la satisfacción por actividades cotidianas.</li>
</ul>

<p>Importante: estos efectos son <strong>reversibles</strong> tras el cese del consumo,
según múltiples estudios de neuroimagen con fMRI y PET.</p>

<blockquote>
<strong>Fuente:</strong> Volkow, N.D. et al., «Decreased dopamine brain reactivity in marijuana
abusers is associated with negative emotionality and addiction severity»,
<em>Proceedings of the National Academy of Sciences</em>, vol. 111, 2014.
</blockquote>

<h2>¿El cannabis crea dependencia?</h2>
<p>La dependencia al cannabis existe pero es menos intensa que la del alcohol, tabaco u opioides.
Aproximadamente un <strong>9% de los usuarios</strong> desarrollará dependencia
(frente al 15% del alcohol, 32% del tabaco y 23% de la heroína),
según el análisis clásico de Anthony et al. (1994).</p>

<p>Los factores de riesgo incluyen inicio temprano (antes de los 18 años),
consumo diario, variedades de alto THC y predisposición genética.</p>

<h2>Consumo consciente: la diferencia que importa</h2>
<p>En <strong>Green Dome</strong> promovemos el consumo adulto e informado.
Conocer la neurociencia del cannabis — incluyendo los riesgos reales —
es parte de pertenecer a una comunidad cannábica responsable.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Tanda et al. (Science, 1997) · Volkow et al. (PNAS, 2014) ·
Anthony, J.C. et al., «Comparative epidemiology of dependence on tobacco, alcohol, controlled
substances and inhalants», <em>Experimental and Clinical Psychopharmacology</em>, 1994.
</p>
"""

# ─── ARTÍCULO 6 — High vs Stoned ─────────────────────────────────
TITULO_6 = "High vs Stoned: la diferencia real entre los dos estados del cannabis"
SLUG_6   = "high-vs-stoned-diferencia-sativa-indica-efectos"
RESUMEN_6 = (
    "¿Por qué con una variedad te sientes eufórico y creativo, y con otra pegado al sofá? "
    "La diferencia entre 'high' y 'stoned' va más allá de sativa vs indica. "
    "La ciencia detrás de los efectos del cannabis."
)
CONTENIDO_6 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
En la cultura cannábica, «high» y «stoned» describen dos experiencias claramente distintas.
El primero es mental, eufórico, cerebral. El segundo es corporal, pesado, sedante.
¿Qué hay detrás de esta diferencia?
</p>

<h2>El mito sativa/indica</h2>
<p>Durante décadas, la explicación popular fue simple: <em>sativa = high cerebral,
indica = stoned corporal</em>. Sin embargo, la investigación genética moderna
ha demostrado que esta clasificación es <strong>insuficiente y en muchos casos engañosa</strong>.</p>

<p>Un estudio de 2015 publicado en <em>PLOS ONE</em> analizó genéticamente cientos de variedades
comerciales «sativa» e «indica» y encontró que la clasificación botánica y la experiencia subjetiva
correlacionan pobremente. Las variedades han sido tan cruzadas durante décadas que
la mayoría son <strong>híbridos genéticamente indefinidos</strong>.</p>

<blockquote>
<strong>Fuente:</strong> Sawler, J. et al., «The Genetic Structure of Marijuana and Hemp»,
<em>PLOS ONE</em>, vol. 10, n.º 8, 2015.
</blockquote>

<h2>Los terpenos: la explicación más sólida</h2>
<p>La clave real parece estar en los <strong>terpenos</strong> — los compuestos aromáticos
responsables del olor y sabor de cada variedad, y que modulan cómo actúan los cannabinoides
(<em>entourage effect</em>):</p>
<ul>
  <li>🌱 <strong>Mirceno</strong> (olor a tierra, mango): efecto sedante, «stoned».
  Es el terpeno más común en cannabis. Facilita la entrada del THC al cerebro.</li>
  <li>🍋 <strong>Limoneno</strong> (cítrico): efecto estimulante, eufórico, ansiolítico.
  Asociado al «high» mental.</li>
  <li>🌲 <strong>Pineno</strong> (pino): potencial efecto nootrópico leve,
  puede contrarrestar parcialmente la pérdida de memoria del THC.</li>
  <li>🌸 <strong>Linalool</strong> (lavanda): sedante, ansiolítico, similar al mirceno.</li>
  <li>🌶️ <strong>Beta-cariofileno</strong> (pimienta): único terpeno que activa CB2,
  efecto antiinflamatorio y sin psicoactividad propia.</li>
</ul>

<h2>El ratio THC:CBD también importa</h2>
<p>El CBD modula los efectos del THC sobre CB1. Variedades con ratio equilibrado
(1:1 o 2:1 THC:CBD) tienden a producir experiencias más cerebrales y menos sedantes
que variedades de THC alto con CBD mínimo.</p>

<h2>Factores individuales</h2>
<ul>
  <li><strong>Tolerancia:</strong> usuarios frecuentes experimentan menos sedación.</li>
  <li><strong>Método de consumo:</strong> vaporizado tiende hacia high más limpio;
  combustionado añade productos de pirolisis que pueden aumentar la sedación.</li>
  <li><strong>Estado mental y entorno (set &amp; setting):</strong>
  el estado emocional previo amplifica ciertos efectos.</li>
</ul>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Sawler et al. (PLOS ONE, 2015) ·
Russo, E.B. (2011, BJP) · Piomelli, D. &amp; Russo, E.B.,
«The Cannabis sativa versus Cannabis indica debate», <em>Cannabis and Cannabinoid Research</em>, 2016.
</p>
"""

# ─── ARTÍCULO 7 — Genética y metabolismo del cannabis ────────────
TITULO_7 = "Por qué el cannabis te afecta diferente que a los demás: genética y metabolismo"
SLUG_7   = "cannabis-genetica-metabolismo-cyp2c9-diferencias-individuales"
RESUMEN_7 = (
    "La misma variedad, la misma dosis, experiencias completamente distintas. "
    "La genética individual — especialmente el enzima CYP2C9 — determina "
    "cómo metabolizas el THC y qué efectos experimentas."
)
CONTENIDO_7 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
¿Por qué tu amigo puede consumir dosis altas sin problema mientras tú con la mitad
ya estás sobrepasado? No es cuestión de voluntad ni de experiencia exclusivamente:
la respuesta está en tu ADN.
</p>

<h2>El metabolismo del THC: hígado como protagonista</h2>
<p>Cuando consumes cannabis, el THC viaja por el torrente sanguíneo hasta el hígado,
donde es metabolizado principalmente por el <strong>enzima CYP2C9</strong>
(citocromo P450 2C9) en su metabolito activo: el <strong>11-OH-THC</strong>
(11-hidroxitetrahidrocannabinol).</p>

<p>El 11-OH-THC es <strong>más potente que el THC original</strong> — cruza
más fácilmente la barrera hematoencefálica y produce efectos más intensos y prolongados.
Esto explica en parte por qué los comestibles (que se metabolizan antes en el hígado
que el cannabis inhalado) producen efectos tan diferentes y más impredecibles.</p>

<h2>Variantes genéticas del CYP2C9</h2>
<p>El gen CYP2C9 tiene variantes (polimorfismos) que determinan la velocidad del metabolismo:</p>
<ul>
  <li><strong>Metabolizadores rápidos (normal/ultrarrápido):</strong> convierten el THC
  en 11-OH-THC rápidamente. Pueden necesitar dosis mayores para el mismo efecto.</li>
  <li><strong>Metabolizadores lentos (CYP2C9*3 y otras variantes):</strong>
  el THC permanece más tiempo activo. Los efectos son más intensos y duraderos.
  Se estima que entre el 6-10% de la población europea tiene estas variantes.</li>
</ul>

<blockquote>
<strong>Fuente:</strong> Sachse-Seeboth, C. et al., «Interindividual variation in the pharmacokinetics
of Δ9-tetrahydrocannabinol as related to genetic polymorphisms in CYP2C9»,
<em>Clinical Pharmacology &amp; Therapeutics</em>, vol. 85, 2009, pp. 273-276.
</blockquote>

<h2>El papel de los receptores CB1 (gen CNR1)</h2>
<p>Las variantes en el gen <strong>CNR1</strong> (que codifica el receptor CB1)
también modulan la respuesta subjetiva al cannabis:</p>
<ul>
  <li>Algunas variantes se asocian a mayor sensibilidad ansiolítica o euforizante.</li>
  <li>El polimorfismo AAT del CNR1 se ha relacionado con mayor riesgo de dependencia
  en consumidores frecuentes.</li>
</ul>

<h2>Implicaciones prácticas</h2>
<p>Para el consumidor, esto significa una sola cosa: <strong>empieza bajo, ve despacio</strong>.
No existe una dosis universal. Lo que te siente bien a ti puede ser insuficiente
para otra persona — o excesivo. La autoexperimentación consciente y pausada
es la única forma de encontrar tu ventana terapéutica personal.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Sachse-Seeboth et al. (Clinical Pharmacology &amp; Therapeutics, 2009) ·
Stott, C. et al., pharmacokinetics review, <em>Epilepsia Open</em>, 2019 ·
Huestis, M.A., «Human cannabinoid pharmacokinetics», <em>Chemistry &amp; Biodiversity</em>, 2007.
</p>
"""

# ─── ARTÍCULO 8 — Cannabis y memoria ─────────────────────────────
TITULO_8 = "Cannabis y memoria: lo que realmente dice la ciencia (y lo que exageran los medios)"
SLUG_8   = "cannabis-memoria-ciencia-efectos-largo-plazo"
RESUMEN_8 = (
    "¿El cannabis destruye la memoria? La respuesta es más matizada que los titulares. "
    "Diferencia entre efectos agudos y crónicos, qué es reversible y qué no, "
    "y cómo proteger tu memoria si consumes."
)
CONTENIDO_8 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
El efecto del cannabis sobre la memoria es probablemente el tema más malinterpretado
de toda la neurociencia cannábica. Los medios simplifican, los activistas minimizan
y la realidad — como siempre — está en un punto medio que requiere matices.
</p>

<h2>Efectos agudos: la amnesia transitoria del THC</h2>
<p>Durante el episodio de consumo activo, el THC produce
<strong>alteraciones claras en la memoria a corto plazo</strong>:</p>
<ul>
  <li>Dificultad para consolidar nueva información (memoria declarativa episódica).</li>
  <li>Interferencia en la memoria de trabajo (working memory).</li>
  <li>El mecanismo: el THC en el hipocampo altera la potenciación a largo plazo (LTP),
  el mecanismo celular de la formación de recuerdos.</li>
</ul>
<p>Estos efectos son <strong>transitorios</strong> y desaparecen cuando el THC
se elimina del organismo (normalmente entre 3-6 horas para efectos cognitivos agudos).</p>

<h2>Consumo crónico: la evidencia real</h2>
<p>Aquí la investigación es más compleja:</p>
<ul>
  <li>Estudios de neuroimagen muestran diferencias volumétricas en el hipocampo
  de consumidores crónicos de inicio temprano — pero el efecto varía enormemente.</li>
  <li>Un metaanálisis de 2012 (Grant et al.) encontró que los déficits cognitivos
  en consumidores crónicos son <strong>moderados y en gran parte reversibles</strong>
  tras 72 horas de abstinencia.</li>
  <li>El inicio durante la adolescencia (antes de los 16-18 años) sí muestra
  efectos más duraderos sobre la cognición — el cerebro en desarrollo es más vulnerable.</li>
</ul>

<blockquote>
<strong>Fuente:</strong> Grant, I. et al., «Non-acute (residual) neurocognitive effects
of cannabis use: a meta-analytic study»,
<em>Journal of the International Neuropsychological Society</em>, vol. 9, 2003.
</blockquote>

<h2>El olvido adaptativo: una función del SEC</h2>
<p>Un aspecto contraintuitivo: el sistema endocannabinoide tiene un papel
<strong>esencial en el olvido adaptativo</strong> — la capacidad de borrar
recuerdos irrelevantes o perturbadores para mantener la función cognitiva normal.</p>

<p>Estudios en ratones knock-out para el receptor CB1 muestran incapacidad
para olvidar miedos condicionados — lo que refuerza la hipótesis de que
el SEC regula la extinción de recuerdos traumáticos. Esta es la base científica
de la investigación sobre cannabis/CBD para PTSD.</p>

<h2>Cómo minimizar el impacto en la memoria</h2>
<ul>
  <li>✅ No consumir antes de los 18 años.</li>
  <li>✅ Preferir variedades con CBD moderado — modula el efecto amnésico del THC.</li>
  <li>✅ No consumir durante el trabajo o estudio activo.</li>
  <li>✅ Mantener días de descanso (tolerance breaks).</li>
  <li>✅ Vaporizar en lugar de combustionar — menos productos de pirolisis.</li>
</ul>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Grant et al. (JINS, 2003) ·
Bhattacharyya, S. et al., «Modulation of mediotemporal and ventrostriatal function
in humans by Δ9-tetrahydrocannabinol», <em>Archives of General Psychiatry</em>, 2009 ·
Marsicano, G. et al., «The endogenous cannabinoid system controls extinction
of aversive memories», <em>Nature</em>, 2002.
</p>
"""

# ─── ARTÍCULO 9 — Microdosificación de cannabis ───────────────────
TITULO_9 = "Microdosificación de cannabis: la guía práctica para empezar con menos"
SLUG_9   = "microdosificacion-cannabis-guia-practica-beneficios"
RESUMEN_9 = (
    "La microdosis de cannabis consiste en consumir cantidades sub-perceptibles "
    "para obtener beneficios terapéuticos sin el efecto psicoactivo intenso. "
    "Guía práctica con protocolos reales."
)
CONTENIDO_9 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
La microdosificación no es una moda — es una estrategia de consumo respaldada
por un creciente cuerpo de evidencia que sugiere que dosis sub-terapéuticas
de cannabis pueden ofrecer beneficios sin los efectos secundarios de dosis más altas.
</p>

<h2>¿Qué es una microdosis de cannabis?</h2>
<p>En el contexto del cannabis, una microdosis se suele definir como
<strong>1 a 5 mg de THC</strong> — significativamente por debajo del «umbral psicoactivo»
estándar (que ronda los 5-10 mg según la tolerancia individual).</p>

<p>El objetivo no es «colocarse» sino obtener efectos sutiles:
reducción de la ansiedad de fondo, mejora del foco, alivio de dolor leve,
mejor calidad del sueño — sin alterar significativamente la función cognitiva o motora.</p>

<h2>La evidencia detrás de la microdosificación</h2>
<p>Un estudio de 2012 del Dr. <strong>Mark Wallace</strong> en UC San Diego
encontró que dosis muy bajas de THC (1,3 mg) producían reducción del dolor neuropático,
mientras que dosis medias (3,5 mg) no mostraban diferencia significativa con placebo
y dosis altas (9,4 mg) aumentaban el dolor en algunos pacientes — una curva
de respuesta en forma de U invertida, o <em>respuesta bifásica</em>.</p>

<blockquote>
<strong>Fuente:</strong> Wallace, M. et al., «Dose-dependent effects of smoked cannabis
on capsaicin-induced pain and hyperalgesia in healthy volunteers»,
<em>Anesthesiology</em>, vol. 107, 2007.
</blockquote>

<h2>Protocolo básico para empezar</h2>
<ol>
  <li><strong>Día 1-3:</strong> 1 mg de THC (o 1 calada suave de vaporizador,
  sin retener). Observa durante 2 horas.</li>
  <li><strong>Día 4-7:</strong> Si toleras bien, sube a 2 mg. Mantén un diario
  de efectos: energía, foco, ansiedad, dolor, sueño.</li>
  <li><strong>Semana 2-3:</strong> Ajusta según el diario. El objetivo es
  encontrar la <em>dosis mínima efectiva</em> para tu objetivo concreto.</li>
  <li><strong>Frecuencia:</strong> Muchos practicantes usan microdosis
  1-2 veces al día, con 2-3 días de descanso por semana para evitar tolerancia.</li>
</ol>

<h2>Métodos óptimos para microdosificar</h2>
<ul>
  <li>🌡️ <strong>Vaporizador de hierba seca:</strong> la opción más precisa.
  Temperatura 170-185°C para efectos más cerebrales y menos sedantes.</li>
  <li>💧 <strong>Tintura sublingual (CBD:THC):</strong> absorción en 15-30 minutos,
  efectos reproducibles.</li>
  <li>⚠️ <strong>Comestibles:</strong> difíciles de microdosificar por la variabilidad
  del metabolismo hepático — requieren mayor control.</li>
</ul>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Wallace et al. (Anesthesiology, 2007) ·
Grotenhermen, F. &amp; Müller-Vahl, K., <em>Cannabis als Medizin</em>, 2017 ·
MacCallum, C.A. &amp; Russo, E.B., «Practical considerations in medical cannabis administration
and dosing», <em>European Journal of Internal Medicine</em>, 2018.
</p>
"""

# ─── ARTÍCULO 10 — Cannabis funcional ────────────────────────────
TITULO_10 = "Cannabis funcional: la nueva tendencia del consumo consciente y orientado"
SLUG_10   = "cannabis-funcional-consumo-consciente-tendencias-2025"
RESUMEN_10 = (
    "El cannabis funcional es consumir con intención: para crear, para rendir, "
    "para recuperarse. Cómo seleccionar variedad, dosis y método según tu objetivo. "
    "La tendencia que está redefiniendo el consumo adulto."
)
CONTENIDO_10 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
La era del consumo recreational-solamente está evolucionando.
Una generación de consumidores informados está adoptando el <strong>cannabis funcional</strong>:
un enfoque intencional donde el qué consumes, cuándo y cómo está alineado
con un objetivo específico — no solo el ocio.
</p>

<h2>¿Qué es el cannabis funcional?</h2>
<p>El cannabis funcional no es un producto diferente — es un <em>enfoque</em> diferente.
Consiste en:</p>
<ul>
  <li>Seleccionar la variedad según el perfil de terpenos y cannabinoides relevantes para tu objetivo.</li>
  <li>Controlar la dosis para obtener el efecto deseado sin exceso.</li>
  <li>Elegir el método de consumo adecuado (vaporizador para efecto limpio y controlado).</li>
  <li>Definir el momento adecuado en tu jornada o semana.</li>
</ul>

<h2>Los cinco arquetipos del cannabis funcional</h2>

<h3>1. Cannabis para la creatividad</h3>
<p>Variedades con alto limoneno y pineno, THC moderado (10-16%).
Efecto: pensamiento divergente, asociaciones inesperadas, reducción del autocensor.
Ideal para: sesiones creativas, brainstorming, música, artes visuales.</p>

<h3>2. Cannabis para la recuperación física</h3>
<p>Variedades con alto beta-cariofileno, mirceno y CBD moderado.
Efecto: antiinflamatorio, relajación muscular, reducción de dolor de ejercicio.
Ideal para: post-entrenamiento, dolor muscular, insomnio de recuperación.</p>

<h3>3. Cannabis para el foco</h3>
<p>Microdosis + terpenos pineno y limoneno.
Efecto: sutil claridad mental sin sedación.
Ideal para: trabajo creativo repetitivo, estado de flow.
⚠️ No funciona para todos — puede aumentar la ansiedad en algunas personas.</p>

<h3>4. Cannabis para el sueño</h3>
<p>Variedades con alto mirceno y linalool, THC moderado-alto, consumo 1-2h antes de dormir.
Efecto: reducción de la latencia del sueño, aumento del sueño profundo.
Nota: puede reducir sueño REM con uso crónico.</p>

<h3>5. Cannabis para la socialización</h3>
<p>Variedades equilibradas THC:CBD, limoneno dominante.
Efecto: euforia controlada, fluidez social, reducción de la inhibición.
Ideal para: eventos sociales, conversaciones profundas.</p>

<h2>La clave: conocer tu producto</h2>
<p>El cannabis funcional requiere acceso a producto con perfil de terpenos conocido.
En <strong>Green Dome</strong>, el autocultivo propio nos permite conocer con exactitud
el perfil de cada variedad: porcentaje de cannabinoides y terpenos predominantes,
condiciones de cultivo y momento de cosecha.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Russo (2011, BJP) — entourage effect ·
MacCallum &amp; Russo (2018, EJIM) · Steep Hill Labs,
<em>Cannabis Terpene Report</em>, 2022 (datos de terpenos por fenotipo).
</p>
"""

# ─── ARTÍCULO 11 — CBD en 2025 ───────────────────────────────────
TITULO_11 = "CBD en 2025: qué funciona, qué no, y qué prometió pero no cumplió"
SLUG_11   = "cbd-2025-que-funciona-evidencia-cientifica"
RESUMEN_11 = (
    "El CBD fue el ingrediente del momento entre 2018 y 2022. "
    "En 2025, la ciencia ha separado los usos con evidencia sólida "
    "de los que fueron solo marketing. La guía definitiva basada en datos reales."
)
CONTENIDO_11 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
Entre 2018 y 2022, el CBD se vendió como solución para casi todo: ansiedad,
dolor crónico, acné, cáncer, demencia, insomnio. En 2025, con más de cinco años
de ensayos clínicos adicionales, podemos ser más precisos sobre qué dice realmente la ciencia.
</p>

<h2>Lo que funciona: evidencia sólida</h2>

<h3>Epilepsia refractaria — Evidencia nivel A</h3>
<p>El único uso con aprobación regulatoria de agencia (FDA y EMA):
<strong>Epidiolex/Epidyolex</strong> (CBD farmacéutico al 100 mg/ml).
Ensayos clínicos randomizados de fase III demuestran reducción significativa
de convulsiones en síndrome de Dravet y síndrome de Lennox-Gastaut.</p>

<blockquote>
<strong>Fuente:</strong> Devinsky, O. et al., <em>New England Journal of Medicine</em>,
vol. 376, 2017 · NICE Technology Appraisal TA614 (Reino Unido, 2019).
</blockquote>

<h3>Ansiedad — Evidencia moderada</h3>
<p>Varios ensayos han mostrado efectos ansiolíticos del CBD (300-600 mg/día)
en modelos de ansiedad social y PTSD. Sin embargo, la mayoría usan
<strong>dosis muy superiores</strong> a las que contienen los productos de consumo habitual
(típicamente 10-30 mg/día en el mercado).</p>

<h3>Dolor neuropático — Evidencia prometedora</h3>
<p>Sativex (nabiximols, spray THC:CBD 1:1) tiene aprobación en España para
espasticidad por esclerosis múltiple. El CBD solo tiene evidencia más limitada
pero prometedora para dolor neuropático periférico.</p>

<h2>Lo que NO ha cumplido las expectativas</h2>
<ul>
  <li>❌ <strong>Acné y piel:</strong> evidencia solo in vitro y animal, ningún ensayo clínico robusto.</li>
  <li>❌ <strong>Cáncer (tratamiento directo):</strong> estudios in vitro prometedores
  pero sin evidencia clínica de eficacia antitumoral en humanos.</li>
  <li>❌ <strong>Alzheimer:</strong> modelos animales prometedores, nada confirmado en humanos.</li>
  <li>❌ <strong>Bienestar general (dosis bajas en gummies):</strong>
  el efecto placebo es alto y la biodisponibilidad oral del CBD es solo del 6-13%.</li>
</ul>

<h2>El problema de la biodisponibilidad</h2>
<p>El CBD oral tiene una biodisponibilidad muy baja: solo el <strong>6-13%</strong>
de lo que ingieres llega al torrente sanguíneo (efecto de primer paso hepático).
Esto significa que un gummy de 25 mg de CBD equivale funcionalmente a ~1,5-3,25 mg en sangre
— muy por debajo de las dosis usadas en ensayos clínicos.</p>

<p>Las formulaciones con mayor biodisponibilidad:
aceite sublingual (15-25%), spray oromucosal (>25%), inhalado (30-40%).</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Devinsky et al. (NEJM, 2017) · NICE TA614 ·
Huestis et al., <em>Trends in Pharmacological Sciences</em>, 2019 ·
Millar, S.A. et al., «A Systematic Review on the Pharmacokinetics of Cannabidiol in Humans»,
<em>Frontiers in Pharmacology</em>, 2019.
</p>
"""

# ─── ARTÍCULO 12 — Vaporización vs combustión ────────────────────
TITULO_12 = "Vaporización vs combustión: por qué el vaporizador es la opción más inteligente"
SLUG_12   = "vaporizacion-vs-combustion-cannabis-diferencias-salud"
RESUMEN_12 = (
    "¿Joint o vaporizador? La diferencia no es solo de sabor: es de salud, "
    "eficiencia y calidad de experiencia. La ciencia comparativa entre combustión "
    "y vaporización del cannabis explicada en detalle."
)
CONTENIDO_12 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
La combustión del cannabis produce, además de cannabinoides y terpenos,
más de <strong>100 compuestos tóxicos</strong> — muchos de los mismos que el humo
del tabaco. La vaporización elimina la combustión y con ella la mayoría de esos compuestos.
La ciencia sobre esta diferencia es clara y relevante.
</p>

<h2>¿Qué ocurre al combustionar cannabis?</h2>
<p>A temperaturas de 230-350°C+ (combustión), se producen:</p>
<ul>
  <li>Monóxido de carbono (CO) — reduce el transporte de oxígeno.</li>
  <li>Alquitranes y partículas — irritación bronquial, inflamación pulmonar crónica.</li>
  <li>Hidrocarburos aromáticos policíclicos (HAP) — potencialmente carcinogénicos.</li>
  <li>Acroleína — irritante pulmonar severo.</li>
  <li>Benzopireno — carcinógeno conocido.</li>
</ul>
<p>Al mismo tiempo, la combustión destruye parcialmente los cannabinoides y terpenos más delicados.</p>

<h2>La vaporización: qué ocurre físicamente</h2>
<p>Los vaporizadores de hierba seca calientan el cannabis a <strong>160-220°C</strong>
— por debajo del punto de combustión (230°C+). Esto:</p>
<ul>
  <li>Volatiliza los cannabinoides y terpenos sin quemarlos.</li>
  <li>Produce un vapor sin monóxido de carbono ni productos de pirolisis.</li>
  <li>Preserva mejor el perfil de terpenos (que se degradan a alta temperatura).</li>
</ul>

<blockquote>
<strong>Fuente:</strong> Abrams, D.I. et al., «Vaporization as a smokeless cannabis
delivery system: a pilot study», <em>Clinical Pharmacology &amp; Therapeutics</em>,
vol. 82, 2007. Primer estudio clínico comparativo sistemático de vaporización vs inhalación.
</blockquote>

<h2>Comparativa de cannabinoides entregados</h2>
<p>Un estudio de la Universidad de California San Francisco encontró que
la vaporización a 200°C entrega aproximadamente el <strong>mismo nivel de THC</strong>
que la combustión pero con significativamente menos subproductos tóxicos.
A 210°C, la eficiencia de extracción es de ~73% vs ~35% en combustión
(el resto se destruye por el calor).</p>

<h2>Temperaturas y efectos: guía práctica</h2>
<table style="width:100%;border-collapse:collapse;margin:2rem 0;color:#ddd;">
  <thead>
    <tr style="background:rgba(126,217,87,.1);border-bottom:2px solid rgba(126,217,87,.3);">
      <th style="text-align:left;padding:.8rem;color:#7ed957;">Temperatura</th>
      <th style="text-align:left;padding:.8rem;color:#7ed957;">Terpenos activos</th>
      <th style="text-align:left;padding:.8rem;color:#7ed957;">Efecto típico</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);">
      <td style="padding:.8rem;">160-170°C</td>
      <td style="padding:.8rem;">Limoneno, pineno</td>
      <td style="padding:.8rem;">Cerebral, energético</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);background:rgba(255,255,255,.02);">
      <td style="padding:.8rem;">175-185°C</td>
      <td style="padding:.8rem;">Mirceno, linalool</td>
      <td style="padding:.8rem;">Equilibrado, relajante</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);">
      <td style="padding:.8rem;">185-200°C</td>
      <td style="padding:.8rem;">Beta-cariofileno, humuleno</td>
      <td style="padding:.8rem;">Sedante, antiinflamatorio</td>
    </tr>
    <tr style="background:rgba(255,255,255,.02);">
      <td style="padding:.8rem;">&gt;210°C</td>
      <td style="padding:.8rem;">Degradación de terpenos</td>
      <td style="padding:.8rem;">Potente, sabor empeorado</td>
    </tr>
  </tbody>
</table>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Abrams et al. (2007, Clinical Pharmacology &amp; Therapeutics) ·
Pomahacova, B. et al., «Cannabis smoke condensate III»,
<em>Inhalation Toxicology</em>, 2009 ·
Lanz, C. et al., «Comparison of vaporization and smoking», <em>CHIMIA</em>, 2016.
</p>
"""

# ─── ARTÍCULO 13 — Bebidas con cannabis ──────────────────────────
TITULO_13 = "Bebidas con cannabis: la revolución del cannabis líquido que llega a Europa"
SLUG_13   = "bebidas-cannabis-thc-cbd-mercado-europa-2025"
RESUMEN_13 = (
    "El mercado de bebidas con cannabis alcanzó 3.000 millones de dólares en 2024 "
    "en Norteamérica. ¿Qué son? ¿Cómo actúan? ¿Llegarán a España? "
    "Todo sobre el cannabis en formato líquido."
)
CONTENIDO_13 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
En los estados legalizados de EE.UU. y en Canadá, las bebidas con cannabis
son ya el segmento de mayor crecimiento del mercado cannábico — superando incluso
a los comestibles. ¿Por qué? Y más importante: ¿qué implica esto para el futuro?
</p>

<h2>¿Qué son las bebidas con cannabis?</h2>
<p>Las bebidas con cannabis son productos que contienen cannabinoides — principalmente
THC, CBD o ambos — en formato líquido. Pueden ser:</p>
<ul>
  <li><strong>Bebidas de CBD:</strong> aguas, tés, refrescos con CBD.
  Legales en muchos países de la UE (si el CBD es de cáñamo industrial con &lt;0.2% THC).</li>
  <li><strong>Bebidas de THC:</strong> cervezas, refrescos, infusiones con THC.
  Solo legales en mercados regulados (Canadá, ciertos estados de EE.UU.).</li>
  <li><strong>Infusiones y tés:</strong> el formato más antiguo — la infusión de cannabis
  existe desde hace milenios en culturas de Asia, África y América.</li>
</ul>

<h2>El problema de la solubilidad: por qué el cannabis líquido es difícil</h2>
<p>El THC y el CBD son moléculas <strong>hidrofóbicas</strong> (no solubles en agua).
Incorporarlas a bebidas sin que se separen requiere tecnología de emulsificación:</p>
<ul>
  <li><strong>Nanoemulsificación:</strong> reduce los glóbulos de cannabinoide a nanoescala (20-200 nm),
  logrando una dispersión estable en agua. Aumenta la biodisponibilidad y reduce el tiempo de inicio.</li>
  <li><strong>Liposomas:</strong> encapsulan los cannabinoides en vesículas lipídicas.
  Mayor estabilidad pero proceso más complejo.</li>
</ul>

<blockquote>
<strong>Fuente:</strong> Perucca, E. &amp; Bialer, M., «Critical aspects affecting cannabidiol
oral bioavailability and metabolic elimination, and related clinical implications»,
<em>CNS Drugs</em>, 2020.
</blockquote>

<h2>El inicio más rápido: la gran ventaja</h2>
<p>Una de las quejas clásicas de los comestibles de cannabis es el inicio tardío
(30-90 minutos) que lleva a consumir en exceso por impaciencia.
Las bebidas con nanoemulsificación pueden reducir este tiempo a
<strong>10-20 minutos</strong>, haciendo la experiencia más predecible y controlable.</p>

<h2>El modelo español: CBD legal, THC en asociaciones</h2>
<p>En España, las bebidas con CBD de cáñamo industrial (&lt;0.2% THC) son legales
y ya disponibles en herboristerías y tiendas especializadas.
Las bebidas con THC solo son posibles en el contexto de asociaciones cannábicas privadas,
donde los socios pueden consumir productos derivados del cannabis dentro del local.
Esta es precisamente una de las innovaciones que estamos explorando en <strong>Green Dome</strong>.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Brightfield Group, <em>Cannabis Beverages Market Report</em>, 2024 ·
Perucca &amp; Bialer (CNS Drugs, 2020) ·
New Frontier Data, <em>Cannabis Consumer Report</em>, 2023.
</p>
"""

# ─── ARTÍCULO 14 — Legalización en Europa ────────────────────────
TITULO_14 = "Legalización del cannabis en Europa: estado actual en 2025 país a país"
SLUG_14   = "legalizacion-cannabis-europa-2025-paises-regulacion"
RESUMEN_14 = (
    "Alemania, Malta, Luxemburgo, Países Bajos — Europa está en medio de "
    "una transformación histórica respecto al cannabis. "
    "Mapa completo de la regulación por países en 2025."
)
CONTENIDO_14 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
El mapa europeo del cannabis está cambiando a una velocidad sin precedentes.
En 2025, el continente presenta un mosaico de regulaciones que va desde
la prohibición estricta hasta la legalización regulada — con España ocupando
una posición peculiar en el medio.
</p>

<h2>Alemania: el mayor mercado europeo en transición (abril 2024)</h2>
<p>El 1 de abril de 2024, entró en vigor en Alemania la primera fase
de la <strong>CanG (Cannabisgesetz)</strong>, la ley de cannabis más importante
de Europa hasta la fecha:</p>
<ul>
  <li>Adultos (+18) pueden poseer hasta <strong>25 g en público</strong> y 50 g en casa.</li>
  <li>Cultivo de hasta <strong>3 plantas por adulto</strong> para consumo propio.</li>
  <li><strong>Cannabis Social Clubs</strong> (asociaciones sin ánimo de lucro)
  pueden cultivar para sus socios — máximo 500 miembros, 25 g/mes/socio.</li>
  <li>La venta comercial (segunda fase de la ley) está siendo pilotada en varias ciudades.</li>
</ul>

<blockquote>
<strong>Fuente:</strong> Bundesministerium für Gesundheit,
<em>Gesetz zum kontrollierten Umgang mit Cannabis (CanG)</em>, BGBl. 2024 I Nr. 109.
En vigor desde el 1 de abril de 2024.
</blockquote>

<h2>Malta: primera legalización completa de la UE (2021)</h2>
<p>Malta fue el primer país de la UE en legalizar la posesión y cultivo de cannabis
para adultos (diciembre 2021):</p>
<ul>
  <li>Posesión hasta 7 g en público.</li>
  <li>Cultivo de hasta 4 plantas por adulto en domicilio privado.</li>
  <li>Asociaciones cannábicas no lucrativas reguladas.</li>
</ul>

<h2>Países Bajos: el experimento de los coffee shops</h2>
<p>Los Países Bajos llevan desde los años 70 con los famosos <em>coffee shops</em>:
venta tolerada (gedoogbeleid) de hasta 5 g al público adulto.
En 2023 lanzaron un experimento de regulación completa del suministro
(cultivo regulado → coffee shops) en 10 municipios piloto.</p>

<h2>Luxemburgo: primera legalización del consumo doméstico (2023)</h2>
<p>En julio de 2023, Luxemburgo legalizó el cultivo de hasta 4 plantas por adulto
y la posesión de hasta 3 g en espacios públicos.</p>

<h2>España: el modelo asociativo — ¿alegal o prelegalización?</h2>
<p>España no ha legalizado el cannabis comercial, pero el modelo asociativo cannábico
lleva décadas funcionando bajo la tolerancia jurisprudencial del Tribunal Supremo.
En 2025, el debate político está más activo que nunca:</p>
<ul>
  <li>Más País, Sumar y sectores del PSOE han presentado proposiciones.</li>
  <li>El modelo alemán de Cannabis Social Clubs es prácticamente idéntico
  al modelo español — lo que da argumentos para su reconocimiento explícito.</li>
  <li>Ninguna ley ha prosperado en el Congreso hasta la fecha.</li>
</ul>

<h2>Francia, Italia, Portugal: entre prohibición y tolerancia</h2>
<ul>
  <li><strong>Portugal:</strong> despenalización desde 2001 (toda droga para consumo personal)
  pero sin legalización ni clubes regulados.</li>
  <li><strong>Italia:</strong> posesión personal tolerada en la práctica pero no despenalizada formalmente.
  Los clubs cannábicos existen en zona gris similar a España.</li>
  <li><strong>Francia:</strong> una de las posiciones más restrictivas de Europa occidental.
  Sin embargo, aprobó cannabis medicinal en 2021.</li>
</ul>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> CanG (Alemania, 2024) · Malta Cannabis Authority ·
EMCDDA, <em>Cannabis Legislation in Europe: An Overview</em>, 2023 ·
Transform Drug Policy Foundation, <em>Drug Policy Guide</em>, 2024.
</p>
"""

# ─── ARTÍCULO 15 — El modelo alemán de cannabis social clubs ─────
TITULO_15 = "El modelo alemán de Cannabis Social Clubs: cómo funciona y qué puede aprender España"
SLUG_15   = "modelo-aleman-cannabis-social-clubs-espana-comparativa"
RESUMEN_15 = (
    "Alemania ha adoptado el modelo de Cannabis Social Clubs — el mismo que España "
    "lleva practicando desde los años 90 sin marco legal explícito. "
    "Comparativa completa y qué significa para el futuro en España."
)
CONTENIDO_15 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
Cuando Alemania diseñó su modelo de Cannabis Social Clubs en 2024,
miró directamente al modelo español como referente. El resultado es una regulación
que codifica por ley lo que España lleva haciendo por jurisprudencia durante 30 años.
</p>

<h2>Los Cannabis Social Clubs en la CanG alemana</h2>
<p>La ley alemana define los <em>Anbauvereinigungen</em> (asociaciones de cultivo):</p>
<ul>
  <li><strong>Forma jurídica:</strong> asociación no lucrativa registrada (eingetragener Verein).</li>
  <li><strong>Máximo de socios:</strong> 500 por club.</li>
  <li><strong>Cantidad mensual por socio:</strong> 25 g (50 g para socios &gt;21 años en los primeros meses).</li>
  <li><strong>Autocultivo:</strong> el club cultiva para sus socios, sin venta externa.</li>
  <li><strong>Prohibición de consumo en el local</strong> (al menos en la primera fase de la ley).</li>
  <li><strong>Distancia mínima a centros educativos y de menores:</strong> 200 m.</li>
  <li><strong>Responsable de protección de menores:</strong> obligatorio en cada club.</li>
</ul>

<blockquote>
<strong>Fuente:</strong> §2 y §26-§34 de la <em>Cannabisgesetz (CanG)</em>,
Bundesgesetzblatt 2024 I Nr. 109, 27 de marzo de 2024.
</blockquote>

<h2>Comparativa: modelo español vs modelo alemán</h2>
<table style="width:100%;border-collapse:collapse;margin:2rem 0;color:#ddd;">
  <thead>
    <tr style="background:rgba(126,217,87,.1);border-bottom:2px solid rgba(126,217,87,.3);">
      <th style="text-align:left;padding:.8rem;color:#7ed957;">Aspecto</th>
      <th style="text-align:left;padding:.8rem;color:#7ed957;">España (modelo asociativo)</th>
      <th style="text-align:left;padding:.8rem;color:#7ed957;">Alemania (CanG 2024)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);">
      <td style="padding:.8rem;"><strong>Base legal</strong></td>
      <td style="padding:.8rem;">Jurisprudencia TS + estatutos privados</td>
      <td style="padding:.8rem;">Ley federal explícita (CanG)</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);background:rgba(255,255,255,.02);">
      <td style="padding:.8rem;"><strong>Máximo de socios</strong></td>
      <td style="padding:.8rem;">No definido legalmente (práctica: reducido)</td>
      <td style="padding:.8rem;">500 socios</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);">
      <td style="padding:.8rem;"><strong>Consumo en local</strong></td>
      <td style="padding:.8rem;">Sí (condición central del modelo)</td>
      <td style="padding:.8rem;">No (fase 1) / en revisión</td>
    </tr>
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);background:rgba(255,255,255,.02);">
      <td style="padding:.8rem;"><strong>Registro/licencia</strong></td>
      <td style="padding:.8rem;">Asociación registrada en Registro de Asociaciones</td>
      <td style="padding:.8rem;">Autorización adicional del Land</td>
    </tr>
    <tr>
      <td style="padding:.8rem;"><strong>Inspección/control</strong></td>
      <td style="padding:.8rem;">Mínima (no hay marco específico)</td>
      <td style="padding:.8rem;">Inspecciones regulares obligatorias</td>
    </tr>
  </tbody>
</table>

<h2>Lo que España podría aprender del modelo alemán</h2>
<p>El modelo alemán ofrece lo que el modelo español no tiene: <strong>certeza jurídica</strong>.
Un marco legal explícito protegería tanto a los clubs como a los socios,
eliminaría la dependencia de criterios judiciales variables y permitiría
el desarrollo de estándares de calidad y seguridad obligatorios para el producto.</p>

<p>En <strong>Green Dome</strong>, seguimos de cerca este debate.
Operamos conforme al modelo asociativo español y aplaudimos cualquier avance
que dé más seguridad jurídica a un sector que lleva décadas funcionando
de forma responsable.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> CanG, BGBl. 2024 I Nr. 109 ·
FAC (Federación de Asociaciones Cannábicas) ·
EMCDDA, <em>Cannabis legislation in Europe</em>, 2023.
</p>
"""

# ─── ARTÍCULO 16 — Percepción social del cannabis en España ──────
TITULO_16 = "Cómo ha cambiado la percepción social del cannabis en España (2000-2025)"
SLUG_16   = "percepcion-social-cannabis-espana-2025-encuestas"
RESUMEN_16 = (
    "En 25 años, España ha pasado de la prohibición cultural del cannabis "
    "a un apoyo mayoritario a su regulación. Datos de encuestas, tendencias "
    "generacionales y el cambio de paradigma que nadie puede ignorar."
)
CONTENIDO_16 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
La transformación de la opinión pública española sobre el cannabis en las últimas
dos décadas es uno de los cambios culturales más significativos y menos comentados
del país. Los datos son claros: España ya no es la sociedad prohibicionista de los 90.
</p>

<h2>Los datos: de minoría a mayoría</h2>
<p>Según el <strong>Observatorio Español de la Droga y las Adicciones (OEDA)</strong>
del Ministerio de Sanidad:</p>
<ul>
  <li>En 2003, el <strong>67%</strong> de los españoles consideraba que el cannabis
  era «bastante» o «muy peligroso».</li>
  <li>En 2023, ese porcentaje había caído al <strong>44%</strong>.</li>
  <li>La encuesta del CIS de 2022 encontró que el <strong>56%</strong> de los españoles
  apoya la regulación del cannabis para adultos.</li>
  <li>Entre los 25-45 años, ese apoyo supera el <strong>65%</strong>.</li>
</ul>

<blockquote>
<strong>Fuente:</strong> OEDA, <em>Encuesta sobre Alcohol y otras Drogas en España (EDADES)</em>,
ediciones 2003 y 2023. Ministerio de Sanidad, Gobierno de España. ·
CIS, Estudio nº 3377, «Actitudes ante el cannabis», 2022.
</blockquote>

<h2>El consumo: normalización creciente</h2>
<p>España tiene una de las tasas de consumo de cannabis más altas de Europa:</p>
<ul>
  <li>Consumo alguna vez en la vida: <strong>40%</strong> de adultos (18-64 años).</li>
  <li>Consumo en el último año: <strong>11,5%</strong> — entre los más altos de la UE.</li>
  <li>Consumo diario o casi diario: <strong>2,7%</strong>.</li>
</ul>

<h2>El rol de los clubs cannábicos en la normalización</h2>
<p>Los cannabis social clubs han jugado un papel activo en este cambio:
han ofrecido un espacio de consumo visible, organizado y responsable
que desmiente los estereotipos del «yonki» o el «dealer».</p>

<p>Cuando alguien entra en un club y ve médicos, abogados, profesores y artistas
compartiendo un espacio de forma adulta y tranquila, su percepción cambia.
Este es el efecto de normalización positiva que clubs como <strong>Green Dome</strong>
producen en sus comunidades locales.</p>

<h2>La brecha generacional</h2>
<p>El cambio de percepción está claramente correlacionado con la edad:</p>
<ul>
  <li>18-35 años: apoyo a regulación ~70%.</li>
  <li>36-55 años: apoyo ~52%.</li>
  <li>56+ años: apoyo ~31%.</li>
</ul>
<p>A medida que los cohortes jóvenes envejezcan, el apoyo social a la regulación
tenderá a aumentar simplemente por demografía.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> OEDA, EDADES 2003 y 2023 (Ministerio de Sanidad) ·
CIS, Estudio nº 3377 (2022) ·
EMCDDA, <em>Spain Drug Report</em>, 2024.
</p>
"""

# ─── ARTÍCULO 17 — Cannabis medicinal en España ───────────────────
TITULO_17 = "Cannabis medicinal en España en 2025: qué está permitido, qué no y cómo acceder"
SLUG_17   = "cannabis-medicinal-espana-2025-acceso-regulacion"
RESUMEN_17 = (
    "España aprobó el cannabis medicinal con Sativex pero el acceso sigue siendo limitado. "
    "Qué medicamentos cannabinoides están aprobados, para qué condiciones "
    "y cuál es la situación real del paciente en España."
)
CONTENIDO_17 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
España tiene una relación ambivalente con el cannabis medicinal:
por un lado, permite el único medicamento cannabinoide aprobado por la EMA (Sativex);
por otro, no ha desarrollado un programa amplio de cannabis medicinal como
Alemania, Francia, Portugal o Italia. En 2025, la situación comienza a cambiar.
</p>

<h2>Medicamentos cannabinoides aprobados en España</h2>

<h3>Sativex (nabiximols) — Aprobado desde 2010</h3>
<ul>
  <li><strong>Composición:</strong> extracto de cannabis con THC y CBD en ratio 1:1 (spray oromucosal).</li>
  <li><strong>Indicación:</strong> espasticidad por esclerosis múltiple (EM) que no responde
  a otros tratamientos.</li>
  <li><strong>Prescripción:</strong> neurólogos en centros hospitalarios.</li>
  <li><strong>Financiación:</strong> incluido en el Sistema Nacional de Salud.</li>
</ul>

<h3>Epidyolex (cannabidiol) — Aprobado en UE desde 2019</h3>
<ul>
  <li><strong>Composición:</strong> CBD farmacéutico al 100 mg/ml.</li>
  <li><strong>Indicaciones:</strong> síndrome de Dravet, síndrome de Lennox-Gastaut
  (epilepsias refractarias pediátricas).</li>
  <li><strong>Financiación:</strong> financiado por el SNS para indicaciones aprobadas.</li>
</ul>

<blockquote>
<strong>Fuente:</strong> Agencia Española de Medicamentos y Productos Sanitarios (AEMPS),
fichas técnicas de Sativex y Epidyolex. Disponibles en
<a href="https://www.aemps.gob.es/" target="_blank" rel="noopener noreferrer"
   style="color:#7ed957;">aemps.gob.es</a>.
</blockquote>

<h2>La brecha: lo que no está disponible</h2>
<p>Más allá de Sativex y Epidyolex, el acceso al cannabis medicinal en España
es prácticamente nulo para el sistema público. Condiciones con evidencia
emergente como dolor crónico, PTSD, náuseas por quimioterapia o insomnio severo
no tienen opciones cannabinoides dentro del SNS.</p>

<p>Esto contrasta con Alemania (donde el cannabis medicinal está disponible
bajo prescripción desde 2017 para decenas de condiciones),
Francia (programa piloto desde 2021) o Portugal (prescripción permitida desde 2019).</p>

<h2>La Agencia Española de Medicamentos y el cáñamo medicinal</h2>
<p>En 2022, la AEMPS publicó un documento de posición reconociendo la necesidad
de una regulación específica para el cannabis medicinal, distinguiéndolo del cannabis
recreativo. Sin embargo, hasta la fecha de este artículo no se ha publicado
ninguna normativa que amplíe el acceso más allá de Sativex y Epidyolex.</p>

<h2>El papel de los clubs cannábicos para pacientes</h2>
<p>Muchos pacientes con condiciones crónicas que buscan alivio con cannabis
recurren a los clubs asociativos como única vía de acceso a producto controlado.
En <strong>Green Dome</strong> recibimos socios con diversas motivaciones —
la comunidad, la cultura, la recreación y también, en muchos casos, la búsqueda
de alivio personal. Sin pretender sustituir nunca la atención médica.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> AEMPS — fichas técnicas Sativex y Epidyolex ·
EMCDDA, <em>Medical use of cannabis and cannabinoids</em>, 2023 ·
Ministerio de Sanidad, <em>Informe sobre cannabis terapéutico</em>, 2022.
</p>
"""

# ─── ARTÍCULO 18 — Futuro industria cannabis ─────────────────────
TITULO_18 = "El futuro de la industria cannábica: tendencias globales para 2025-2030"
SLUG_18   = "futuro-industria-cannabis-tendencias-2025-2030"
RESUMEN_18 = (
    "El mercado global del cannabis alcanzará los 100.000 millones de dólares en 2030. "
    "Qué tendencias están definiendo el sector: biosíntesis, IA, nanotecnología, "
    "consolidación y el rol de Europa en la nueva industria global."
)
CONTENIDO_18 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
La industria del cannabis está en transición de un mercado informal a uno de los sectores
agroindustriales y farmacéuticos de mayor crecimiento mundial.
En 2030, el mercado global podría superar los 100.000 millones de dólares.
¿Qué fuerzas están dando forma a este futuro?
</p>

<h2>1. Biosíntesis de cannabinoides: el fin del cultivo tal como lo conocemos</h2>
<p>Empresas como <strong>Cronos Group</strong>, <strong>InMed Pharmaceuticals</strong>
y varias startups de biotech están desarrollando métodos para producir cannabinoides
mediante <strong>fermentación de levaduras o bacterias</strong> modificadas genéticamente.</p>

<p>La biosíntesis permite:</p>
<ul>
  <li>Producir cannabinoides raros (THCV, CBG, CBDV) en grandes cantidades.</li>
  <li>Costos de producción potencialmente inferiores al cultivo.</li>
  <li>Mayor consistencia y pureza.</li>
  <li>Sin los desafíos logísticos del cultivo (agua, tierra, energía).</li>
</ul>

<blockquote>
<strong>Fuente:</strong> Luo, X. et al., «Complete biosynthesis of cannabinoids
and their unnatural analogues in yeast», <em>Nature</em>, vol. 567, 2019, pp. 123-126.
</blockquote>

<h2>2. Inteligencia artificial en genómica y selección de variedades</h2>
<p>La secuenciación completa del genoma del cannabis (publicada en 2020)
ha abierto la puerta a la selección de variedades mediante IA:
predecir el perfil de terpenos y cannabinoides de una variedad antes de cultivarla,
optimizar condiciones de cultivo para maximizar compuestos específicos,
y desarrollar variedades adaptadas a usos médicos precisos.</p>

<h2>3. Nanotecnología: cannabinoides más biodisponibles</h2>
<p>La baja biodisponibilidad oral del CBD y THC (6-20%) es uno de los principales
obstáculos para el desarrollo farmacéutico. La nanotecnología —
nanopartículas lipídicas, nanoemulsiones, liposomas — puede elevar la biodisponibilidad
oral al 50-80%, según estudios in vitro.</p>

<h2>4. Consolidación del mercado: del microclub a la multinacional</h2>
<p>En mercados maduros como Canadá, estamos viendo una fase de consolidación intensa:
cientos de pequeñas empresas absorbidas por grandes grupos.
El modelo artesanal, de calidad y comunidad — como el de los clubs cannábicos europeos —
puede sobrevivir como nicho premium, al igual que las bodegas familiares
frente a las grandes corporaciones vitivinícolas.</p>

<h2>5. Europa: el próximo gran mercado</h2>
<p>Con Alemania como catalizador, la presión para la regulación en Francia,
Italia, Países Bajos (regulación completa) y España se intensificará.
Los analistas estiman que la UE podría convertirse en el mayor mercado legal
de cannabis del mundo para 2030 — superando a EE.UU. por población y poder adquisitivo.</p>

<p>En <strong>Green Dome</strong>, observamos este futuro con interés y optimismo.
Nuestro modelo — pequeño, artesanal, comunitario, enfocado en la calidad —
es precisamente el que históricamente ha sobrevivido y prosperado
en mercados que se industrializan.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Luo et al. (Nature, 2019) ·
Grand View Research, <em>Cannabis Market Size Report</em>, 2024 ·
New Frontier Data, <em>Global Cannabis Report</em>, 2024 ·
EMCDDA, <em>European Drug Report</em>, 2024.
</p>
"""

# ─── ARTÍCULO 19 — Cannabis y deporte ────────────────────────────
TITULO_19 = "Cannabis y deporte: lo que los atletas saben (y los organismos empiezan a aceptar)"
SLUG_19   = "cannabis-deporte-atletas-recuperacion-wada-2025"
RESUMEN_19 = (
    "La WADA eliminó el CBD de su lista de sustancias prohibidas en 2018. "
    "Cada vez más atletas usan cannabinoides para recuperación, dolor y ansiedad competitiva. "
    "Qué dice la ciencia y cuál es el estado actual en el deporte de élite."
)
CONTENIDO_19 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
Michael Phelps, Ricky Williams, Sha'Carri Richardson — las controversias entre cannabis
y deporte de élite han sido noticias internacionales. Pero más allá del escándalo,
existe una conversación científica seria sobre el papel de los cannabinoides
en la recuperación deportiva, la gestión del dolor y la ansiedad competitiva.
</p>

<h2>El giro de la WADA: CBD fuera de la lista (2018)</h2>
<p>En 2018, la <strong>Agencia Mundial Antidopaje (WADA)</strong> eliminó el CBD
de su Lista de Sustancias y Métodos Prohibidos. La razón: el CBD no tiene
propiedades que mejoren el rendimiento deportivo de forma directa.</p>

<p>El THC sigue prohibido en competición (umbral: 150 ng/mL en orina)
pero no fuera de ella. Esto significa que los atletas pueden usar productos
de CBD legalmente — con la cautela de que muchos productos del mercado contienen
trazas de THC que pueden acumularse.</p>

<blockquote>
<strong>Fuente:</strong> WADA, <em>World Anti-Doping Code International Standard:
Prohibited List 2018</em>. Decisión de exclusión del cannabidiol (CBD).
</blockquote>

<h2>Usos potenciales de los cannabinoides en deporte</h2>

<h3>Recuperación muscular y antiinflamación</h3>
<p>El CBD tiene propiedades antiinflamatorias (actuando sobre CB2 y TRPV1)
que podrían ayudar a reducir la inflamación muscular post-ejercicio.
Estudios en modelos animales son prometedores; la evidencia clínica en atletas humanos
es todavía limitada pero creciente.</p>

<h3>Manejo del dolor crónico sin opioides</h3>
<p>Muchos atletas de contacto (rugby, boxeo, fútbol americano, MMA) buscan
alternativas a los analgésicos opioides para el dolor crónico acumulado.
El CBD y los cannabinoides en general se perfilan como una alternativa
con menor potencial de dependencia y abuso.</p>

<h3>Ansiedad competitiva y sueño</h3>
<p>La ansiedad pre-competición es uno de los principales factores limitantes
del rendimiento deportivo. El CBD tiene propiedades ansiolíticas bien documentadas
(actúa sobre 5-HT1A) y puede mejorar la calidad del sueño —
fundamental para la recuperación y el rendimiento.</p>

<h2>El cannabis recreativo y el rendimiento</h2>
<p>El THC, por su parte, tiene efectos <strong>mixtos sobre el rendimiento</strong>:</p>
<ul>
  <li>✅ Puede reducir la percepción del dolor y el esfuerzo a corto plazo.</li>
  <li>✅ Reduce la ansiedad ante el error (útil en deportes de precisión para algunos).</li>
  <li>❌ Reduce la coordinación motora fina y el tiempo de reacción.</li>
  <li>❌ Aumenta la frecuencia cardíaca — contraindicado en deportes cardiovasculares intensos.</li>
</ul>

<h2>Verde en el vestuario: la conversación que ya está pasando</h2>
<p>En el vestuario de equipos de la NFL, NBA, rugby y atletismo,
el cannabis — especialmente el CBD — es ya parte de la conversación de recuperación.
La ciencia, lentamente, está dando soporte a lo que muchos atletas ya practicaban.</p>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> WADA Prohibited List 2018 ·
Rojas-Valverde, D. et al., «Potential role of cannabidiol on sports recovery»,
<em>Frontiers in Physiology</em>, 2021 ·
McCartney, D. et al., «Cannabidiol and Sports Performance»,
<em>Sports Medicine - Open</em>, 2020.
</p>
"""

# ─── ARTÍCULO 20 — Terpenos del cannabis ─────────────────────────
TITULO_20 = "Los terpenos del cannabis: la guía completa para entender el aroma, sabor y efecto"
SLUG_20   = "terpenos-cannabis-guia-completa-aromas-efectos"
RESUMEN_20 = (
    "Los terpenos son los compuestos aromáticos que dan a cada variedad de cannabis "
    "su aroma y sabor únicos — y que modulan significativamente sus efectos. "
    "Guía de los 10 terpenos más importantes con su perfil completo."
)
CONTENIDO_20 = """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
Cuando hueles un limón, la lavanda o el pino, lo que percibes son terpenos.
El cannabis produce más de 200 terpenos diferentes, y la combinación única
de cada variedad determina su aroma característico. Pero los terpenos hacen mucho más
que oler bien: son farmacológicamente activos y modulan cómo actúan los cannabinoides.
</p>

<h2>¿Qué son los terpenos?</h2>
<p>Los terpenos son hidrocarburos orgánicos producidos por las glándulas tricomas
de la planta de cannabis — las mismas que producen THC y CBD.
Evolutivamente, sirven como defensa contra plagas e insectos y como atractor
de polinizadores. En humanos, interactúan con el sistema nervioso,
el sistema endocannabinoide y otros receptores.</p>

<h2>Los 10 terpenos más importantes del cannabis</h2>

<h3>1. Mirceno 🌱</h3>
<p><strong>Aroma:</strong> tierra, mango, hierbas. <strong>Efecto:</strong> sedante, relajante muscular.
El más abundante en la mayoría de variedades de cannabis. Facilita la entrada del THC
al cerebro aumentando la permeabilidad de la barrera hematoencefálica.
Variedades: OG Kush, Blue Dream.</p>

<h3>2. Limoneno 🍋</h3>
<p><strong>Aroma:</strong> cítrico intenso. <strong>Efecto:</strong> estimulante, ansiolítico, antidepresivo.
Activa la serotonina (5-HT1A) y la dopamina. Estudios en modelos animales muestran
efectos antitumorales. Variedades: Super Lemon Haze, Lemon OG.</p>

<h3>3. Cariofileno (beta-cariofileno) 🌶️</h3>
<p><strong>Aroma:</strong> pimienta, madera especiada. <strong>Efecto:</strong> antiinflamatorio,
analgésico, ansiolítico. El único terpeno que activa receptores cannabinoides (CB2).
Sin psicoactividad. Variedades: Girl Scout Cookies, Bubba Kush.</p>

<h3>4. Linalool 🌸</h3>
<p><strong>Aroma:</strong> lavanda floral. <strong>Efecto:</strong> sedante, ansiolítico,
anticonvulsivo. El mismo terpeno responsable de los efectos relajantes de la lavanda.
Variedades: Amnesia Haze, LA Confidential.</p>

<h3>5. Pineno (alpha y beta) 🌲</h3>
<p><strong>Aroma:</strong> pino fresco. <strong>Efecto:</strong> alerta mental,
potencial nootrópico. Inhibe la enzima acetilcolinesterasa — puede contrarrestar
parcialmente la pérdida de memoria a corto plazo del THC.
Variedades: Jack Herer, Dutch Treat.</p>

<h3>6. Humuleno 🍺</h3>
<p><strong>Aroma:</strong> lúpulo terroso (el mismo terpeno de la cerveza IPA).
<strong>Efecto:</strong> supresor del apetito, antiinflamatorio.
Variedades: Headband, Sour Diesel.</p>

<h3>7. Terpinoleno 🍎</h3>
<p><strong>Aroma:</strong> floral, herbáceo, cítrico. <strong>Efecto:</strong> ligeramente sedante,
antioxidante. Raro como terpeno dominante — lo que lo hace diagnóstico de variedades específicas.
Variedades: Jack Herer, Ghost Train Haze.</p>

<h3>8. Ocimeno 🌺</h3>
<p><strong>Aroma:</strong> dulce, herbáceo, tropical. <strong>Efecto:</strong> antiviral,
antifúngico, decongestivo. Más raro pero aromáticamente potente.
Variedades: Golden Goat, Clementine.</p>

<h3>9. Bisabolol 🌼</h3>
<p><strong>Aroma:</strong> floral suave, manzanilla. <strong>Efecto:</strong> antiinflamatorio
cutáneo, sedante leve. Común en manzanilla; en cannabis asociado a efectos calmantes.
Variedades: ACDC, Headband.</p>

<h3>10. Valenceno 🍊</h3>
<p><strong>Aroma:</strong> naranja Valencia. <strong>Efecto:</strong> antiinflamatorio,
repelente de insectos. Llamado así por la naranja de Valencia — hay orgullo local en este.
Variedades: Tangie, Agent Orange.</p>

<h2>Cómo usar el perfil de terpenos para elegir</h2>
<p>En un mercado cannábico maduro, la clasificación por terpenos es más útil
que la clásica sativa/indica. En <strong>Green Dome</strong>, conocemos el perfil
de terpenos de nuestro autocultivo propio, lo que nos permite orientar a los socios
hacia la variedad más adecuada para su objetivo.</p>

<blockquote>
<strong>Fuente:</strong> Russo, E.B. (2011, BJP) — entourage effect y terpenos ·
Steep Hill Labs, <em>Terpene Report</em>, 2022 ·
Booth, J.K. &amp; Bohlmann, J., «Terpenes in Cannabis sativa»,
<em>Plant Science</em>, vol. 284, 2019.
</blockquote>

<hr>
<p style="color:#888;font-size:.9rem;">
<strong>Fuentes:</strong> Russo (2011, BJP) · Booth &amp; Bohlmann (Plant Science, 2019) ·
Steep Hill Labs Terpene Report (2022) · McPartland &amp; Russo,
«Cannabis and cannabis extracts: greater than the sum of their parts?»,
<em>Journal of Cannabis Therapeutics</em>, 2001.
</p>
"""


# ─────────────────────────────────────────────────────────────────
# FUNCIÓN DE MIGRACIÓN
# ─────────────────────────────────────────────────────────────────

def crear_articulos(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')

    articulos = [
        (SLUG_1,  TITULO_1,  RESUMEN_1,  CONTENIDO_1,  datetime(2026, 4, 14)),
        (SLUG_2,  TITULO_2,  RESUMEN_2,  CONTENIDO_2,  datetime(2026, 4, 21)),
        (SLUG_3,  TITULO_3,  RESUMEN_3,  CONTENIDO_3,  datetime(2026, 4, 28)),
        (SLUG_4,  TITULO_4,  RESUMEN_4,  CONTENIDO_4,  datetime(2026, 5, 5)),
        (SLUG_5,  TITULO_5,  RESUMEN_5,  CONTENIDO_5,  datetime(2026, 5, 12)),
        (SLUG_6,  TITULO_6,  RESUMEN_6,  CONTENIDO_6,  datetime(2026, 5, 19)),
        (SLUG_7,  TITULO_7,  RESUMEN_7,  CONTENIDO_7,  datetime(2026, 5, 26)),
        (SLUG_8,  TITULO_8,  RESUMEN_8,  CONTENIDO_8,  datetime(2026, 6, 2)),
        (SLUG_9,  TITULO_9,  RESUMEN_9,  CONTENIDO_9,  datetime(2026, 6, 9)),
        (SLUG_10, TITULO_10, RESUMEN_10, CONTENIDO_10, datetime(2026, 6, 16)),
        (SLUG_11, TITULO_11, RESUMEN_11, CONTENIDO_11, datetime(2026, 6, 23)),
        (SLUG_12, TITULO_12, RESUMEN_12, CONTENIDO_12, datetime(2026, 6, 30)),
        (SLUG_13, TITULO_13, RESUMEN_13, CONTENIDO_13, datetime(2026, 7, 7)),
        (SLUG_14, TITULO_14, RESUMEN_14, CONTENIDO_14, datetime(2026, 7, 14)),
        (SLUG_15, TITULO_15, RESUMEN_15, CONTENIDO_15, datetime(2026, 7, 21)),
        (SLUG_16, TITULO_16, RESUMEN_16, CONTENIDO_16, datetime(2026, 7, 28)),
        (SLUG_17, TITULO_17, RESUMEN_17, CONTENIDO_17, datetime(2026, 8, 4)),
        (SLUG_18, TITULO_18, RESUMEN_18, CONTENIDO_18, datetime(2026, 8, 11)),
        (SLUG_19, TITULO_19, RESUMEN_19, CONTENIDO_19, datetime(2026, 8, 18)),
        (SLUG_20, TITULO_20, RESUMEN_20, CONTENIDO_20, datetime(2026, 8, 25)),
    ]

    for slug, titulo, resumen, contenido, fecha in articulos:
        BlogPost.objects.get_or_create(
            slug=slug,
            defaults={
                'titulo':    titulo,
                'resumen':   resumen,
                'contenido': contenido,
                'autor':     'Green Dome',
                'publicado': True,
                'fecha_pub': timezone.make_aware(fecha.replace(hour=10, minute=0, second=0)),
            }
        )


def eliminar_articulos(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    slugs = [
        SLUG_1, SLUG_2, SLUG_3, SLUG_4, SLUG_5,
        SLUG_6, SLUG_7, SLUG_8, SLUG_9, SLUG_10,
        SLUG_11, SLUG_12, SLUG_13, SLUG_14, SLUG_15,
        SLUG_16, SLUG_17, SLUG_18, SLUG_19, SLUG_20,
    ]
    BlogPost.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_blog_internal_linking'),
        ('core', '0017_merge_20260410_1236'),
    ]

    operations = [
        migrations.RunPython(crear_articulos, eliminar_articulos),
    ]
