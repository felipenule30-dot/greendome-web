"""
Data migration: crea el primer artículo del blog de Green Dome.
'La Gran Mentira: Cómo EE.UU. Criminalizó el Cannabis para Perseguir a las Minorías'
"""
from django.db import migrations
from django.utils import timezone

TITULO = "La Gran Mentira: Cómo EE.UU. Criminalizó el Cannabis para Perseguir a las Minorías"

RESUMEN = (
    "El cannabis era legal, medicinal y cultivado por los propios Padres Fundadores de EE.UU. "
    "En menos de una década pasó a ser 'el demonio verde' que destruía a la juventud. "
    "Lo que nadie te contó: detrás de la prohibición había racismo de Estado, intereses "
    "corporativos y funcionarios que se abastecieron antes de firmar la ley."
)

CONTENIDO = """
<p style="font-size:1.15rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
<em>"La primera vez que me dijeron que los negros y los hispanos fumaban marihuana y que eso
les hacía tocar jazz y seducir a mujeres blancas, me di cuenta de que podíamos usar eso."</em><br>
<strong style="color:#7ed957;">— Harry J. Anslinger</strong>, primer director del Federal Bureau of Narcotics, ca. 1930.
</p>

<h2>1. Antes de la prohibición: el cannabis era parte de la vida americana</h2>

<p>El cáñamo (<em>Cannabis sativa</em>) fue un cultivo estratégico en los Estados Unidos desde su
fundación. George Washington y Thomas Jefferson lo cultivaban en sus plantaciones de Mount Vernon
y Monticello respectivamente. La Constitución de Virginia de 1619 <strong>obligaba</strong> a los
granjeros a cultivar cáñamo, y durante la Guerra de Independencia el Congreso Continental animó
a los colonos a aumentar su producción para fabricar cuerdas, velas y uniformes militares.</p>

<p>A finales del siglo XIX el cannabis era un ingrediente habitual en los preparados de la
farmacopea estadounidense. La empresa Parke-Davis (hoy parte de Pfizer), Eli Lilly y otras
grandes farmacéuticas lo vendían como analgésico, anticonvulsivo y sedante sin ningún tipo de
restricción. La revista <em>Scientific American</em> en 1896 lo describía como «uno de los
remedios más útiles de la medicina moderna».</p>

<p>No existía el término «marihuana» en el discurso médico o legal anglosajón. Se llamaba
<strong>cannabis</strong>, <strong>hemp</strong> o <strong>hashish</strong>. El cambio de
vocabulario fue deliberado y fue la primera arma de la prohibición.</p>

<blockquote>
<strong>Fuentes:</strong> Michael Aldrich, <em>History of Therapeutic Cannabis</em> (1997);
Martin A. Lee, <em>Smoke Signals: A Social History of Marijuana</em>, Scribner, 2012, pp. 3-21;
Jack Herer, <em>The Emperor Wears No Clothes</em>, AH HA Publishing, 1985, caps. 1-3.
</blockquote>


<h2>2. Harry Anslinger y la máquina del miedo (1930-1937)</h2>

<p>En 1930, con la Prohibición del alcohol agonizando, el Gobierno federal creó el
<strong>Federal Bureau of Narcotics (FBN)</strong> y nombró a su frente a
<strong>Harry Jacob Anslinger</strong> (1892-1975). Anslinger necesitaba justificar su
departamento y su presupuesto. El alcohol pronto sería legal de nuevo; necesitaba un nuevo
enemigo.</p>

<p>Anslinger eligió el cannabis y construyó su campaña sobre dos pilares:
<strong>el miedo racial</strong> y <strong>la desinformación científica</strong>.
Entre 1930 y 1937 inundó periódicos y revistas con historias fabricadas o
enormemente exageradas sobre crímenes cometidos por «negros» y «mexicanos» bajo los
efectos de la «marihuana». El uso de esa palabra —tomada del argot mexicano— era
estratégico: sonaba extranjera, amenazante, no-americana.</p>

<p>Algunas citas documentadas de Anslinger ante el Congreso y en su correspondencia interna:</p>

<ul>
  <li><em>«La marihuana hace que los negros piensen que son tan buenos como los hombres blancos.»</em></li>
  <li><em>«Hay 100.000 fumadores de marihuana en EE.UU., y la mayoría son negros, hispanos,
  filipinos y artistas de entretenimiento. Sus músicas satánicas, el jazz y el swing, son el
  resultado del uso de marihuana.»</em></li>
  <li><em>«Los principales adictos son negros, hispanos, filipinos y artistas de entretenimiento.»</em>
  — Testimonio ante el Congreso de EE.UU., 1937.</li>
</ul>

<p>Su campaña mediática incluyó colaboración estrecha con <strong>William Randolph Hearst</strong>,
el magnate de la prensa amarilla dueño de más de 30 periódicos. Hearst tenía dos razones
personales para sumarse a la causa: poseía miles de hectáreas de bosque en México
(su madera competía directamente con el papel de cáñamo) y guardaba un profundo rencio
hacia los trabajadores mexicanos desde que Pancho Villa le había expropiado haciendas
durante la Revolución. Sus periódicos publicaron titulares como
<em>«LOCO DE MARIHUANA ASESINA A FAMILIA ENTERA»</em> sobre crímenes que las
investigaciones posteriores demostraron no tener ninguna relación con la droga.</p>

<blockquote>
<strong>Fuentes:</strong> Harry Anslinger, testimonio ante el House Ways and Means Committee,
27 de abril de 1937 (Congressional Record); John C. McWilliams,
<em>The Protectors: Harry J. Anslinger and the Federal Bureau of Narcotics 1930–1962</em>,
University of Delaware Press, 1990; Eric Schlosser,
<em>Reefer Madness: Sex, Drugs, and Cheap Labor in the American Black Market</em>,
Houghton Mifflin, 2003.
</blockquote>


<h2>3. Los intereses corporativos: DuPont, el nylon y el papel de cáñamo</h2>

<p>La cruzada de Anslinger no habría llegado lejos sin financiación política e institucional.
Aquí entra <strong>Andrew W. Mellon</strong>, Secretario del Tesoro de EE.UU. entre 1921 y
1932, el hombre más rico de América tras Rockefeller y Carnegie, y —no casualmente—
<strong>tío político de Harry Anslinger</strong> (Anslinger se casó con su sobrina).
Mellon era el principal banquero de <strong>E.I. du Pont de Nemours</strong>.</p>

<p>En 1937, el mismo año en que Anslinger presionó para la prohibición del cannabis, DuPont
había registrado dos patentes cruciales que amenazaba destruir la competencia del cáñamo:</p>
<ul>
  <li><strong>1935</strong>: Proceso para fabricar papel a partir de pulpa de madera
  (el papel de cáñamo era más resistente y barato).</li>
  <li><strong>1938</strong>: Nylon, la primera fibra sintética, destinada a competir
  directamente con la fibra de cáñamo en textiles, cuerdas y materiales industriales.</li>
</ul>

<p>La revista <em>Popular Mechanics</em> publicó en febrero de 1938 —meses después de
la prohibición— un artículo titulado <strong>«New Billion-Dollar Crop»</strong> («El nuevo
cultivo de mil millones de dólares») que describía cómo las nuevas tecnologías de
decorticado mecanizado iban a convertir el cáñamo en el cultivo más valioso de América.
El artículo había sido redactado meses antes de la prohibición: <em>llegó tarde</em>.</p>

<p><strong>Andrew Mellon fue quien nombró a Anslinger</strong> al frente del FBN en 1930
y quien supervisó la redacción del <em>Marihuana Tax Act</em>. La conexión entre la
prohibición del cannabis, los intereses de DuPont y la familia Mellon está documentada
en los registros del Tesoro y en la correspondencia empresarial de la época.</p>

<blockquote>
<strong>Fuentes:</strong> Jack Herer, <em>The Emperor Wears No Clothes</em>, caps. 4-6;
<em>Popular Mechanics</em>, «New Billion-Dollar Crop», febrero 1938;
Gerald Colby, <em>DuPont Dynasty</em>, Lyle Stuart, 1984; Registro del Congreso,
<em>Marihuana Tax Act Hearings</em>, House Ways and Means Committee, 1937.
</blockquote>


<h2>4. La Marihuana Tax Act de 1937: el golpe final</h2>

<p>El proceso legislativo de la prohibición fue una chapuza deliberada.
Las audiencias en el <em>House Ways and Means Committee</em> duraron solo dos días.
La Asociación Médica Americana (AMA) envió a su representante,
el Dr. <strong>William C. Woodward</strong>, para oponerse a la ley argumentando
que destruiría un recurso medicinal valioso. La respuesta del comité fue acusarle
de no haber cooperado previamente con el FBN. Su testimonio fue ignorado.</p>

<p>Cuando el proyecto llegó al pleno de la Cámara, el debate duró <strong>menos de
dos minutos</strong>. Un congresista preguntó: «¿La AMA apoya este proyecto de ley?»
El presidente del comité respondió: «Sí». Era mentira. La ley fue aprobada.</p>

<p>El <em>Marihuana Tax Act</em> de 1937 no ilegalizó técnicamente el cannabis:
creó un impuesto tan oneroso y una burocracia tan imposible de cumplir que equivalía
a la prohibición total. Cualquiera que quisiera vender o poseer cannabis legalmente
debía rellenar formularios gubernamentales, pagar una tasa, y el gobierno podía
negarse a emitir los sellos fiscales necesarios. Era una trampa legal perfecta.</p>

<blockquote>
<strong>Fuentes:</strong> Testimonios del Dr. William C. Woodward,
<em>Marihuana: A Signal of Misunderstanding</em>, First Report of the National
Commission on Marihuana and Drug Abuse (Shafer Commission), 1972;
Richard J. Bonnie y Charles H. Whitebread,
<em>The Marihuana Conviction: A History of Marihuana Prohibition in the United States</em>,
University Press of Virginia, 1974.
</blockquote>


<h2>5. El informe La Guardia (1944): la ciencia dijo que Anslinger mentía</h2>

<p>En 1939, el alcalde de Nueva York <strong>Fiorello La Guardia</strong> encargó
al <em>New York Academy of Medicine</em> un estudio independiente y exhaustivo
sobre los efectos del cannabis. El informe, publicado en 1944, llegó a conclusiones
radicalmente contrarias a toda la propaganda de Anslinger:</p>

<ul>
  <li>El cannabis <strong>no causaba adicción física</strong>.</li>
  <li><strong>No había relación causal</strong> entre el cannabis y la criminalidad.</li>
  <li>No era una «droga puerta de entrada» hacia heroína o cocaína.</li>
  <li>Sus efectos eran leves y no producían psicosis en individuos sanos.</li>
</ul>

<p>La reacción de Anslinger fue fulminante: amenazó a los investigadores con procesos
federales, presionó al <em>Journal of the American Medical Association</em> para que
publicara una editorial atacando el informe, y ordenó al FBN vigilar a los miembros
del comité de estudio. El informe fue enterrado durante décadas.</p>

<blockquote>
<strong>Fuentes:</strong> <em>The La Guardia Committee Report: The Marihuana Problem in the City
of New York</em>, New York Academy of Medicine, 1944 (disponible en archivo digital de
la New York Academy of Medicine); Lester Grinspoon, <em>Marihuana Reconsidered</em>,
Harvard University Press, 1971.
</blockquote>


<h2>6. Nixon y la Guerra contra las Drogas: racismo con traje de política pública</h2>

<p>En 1970, el gobierno de <strong>Richard Nixon</strong> aprobó la
<em>Controlled Substances Act</em>, que creó el sistema de Schedules (categorías
de peligrosidad) que aún existe. El cannabis fue clasificado como <strong>Schedule I</strong>:
sin uso médico aceptado, alto potencial de abuso, igual que la heroína.
Nixon ignoró el informe de su propia comisión.</p>

<p>La Comisión Shafer, creada por el propio Nixon para estudiar el cannabis,
recomendó en 1972 la <strong>descriminalización</strong>. Nixon rechazó el informe
sin leerlo. Las cintas de la Casa Blanca —desclasificadas años después— revelan
conversaciones donde Nixon decía: <em>«Sabes que es gracioso respecto a los negros.
Están mucho más motivados que los blancos para consumir droga... porque son vagos.»</em>
(Nixon Tapes, 26 de mayo de 1971, National Archives.)</p>

<p>Pero la admisión más devastadora llegó 45 años después.</p>

<h3>La confesión de Ehrlichman: «queríamos hacerles daño»</h3>

<p>En 2016, el periodista <strong>Dan Baum</strong> publicó en <em>Harper's Magazine</em>
una entrevista que había realizado en 1994 a <strong>John Ehrlichman</strong>, jefe de
gabinete doméstico de Nixon y uno de los principales arquitectos de la Guerra contra
las Drogas. Ehrlichman, que había cumplido condena por el caso Watergate, habló con
una franqueza demoledora:</p>

<blockquote style="background:rgba(255,80,80,.08);border-left-color:#e05050;">
<em>«La campaña de Nixon de 1968, y la Casa Blanca de Nixon después, tenía dos enemigos:
la izquierda antiguerra y los negros. ¿Lo entiendes? Sabíamos que no podíamos hacer
ilegal estar contra la guerra o ser negro, pero al conseguir que el público asociara
a los hippies con la marihuana y a los negros con la heroína, y luego criminalizar
duramente ambas, podíamos desbaratar a esas comunidades. Podíamos arrestar a sus
líderes, asaltar sus hogares, interrumpir sus reuniones y difamarles noche tras noche
en los noticieros. ¿Sabíamos que estábamos mintiendo sobre las drogas? Claro que lo
sabíamos.»</em><br><br>
<strong style="color:#e05050;">— John Ehrlichman</strong>, asesor doméstico del Presidente Nixon,
entrevistado por Dan Baum, 1994. Publicado en Harper's Magazine, abril 2016.
</blockquote>

<blockquote>
<strong>Fuentes:</strong> Dan Baum, «Legalize It All: How to win the war on drugs»,
<em>Harper's Magazine</em>, abril 2016; Cintas de Nixon, conversación del 26 de mayo de 1971,
<em>National Archives and Records Administration</em>;
<em>Marihuana: A Signal of Misunderstanding</em>, Shafer Commission Report, 1972.
</blockquote>


<h2>7. El racismo sistémico que persiste hasta hoy</h2>

<p>La criminalización del cannabis no fue solo un capítulo histórico. Sus efectos
raciales continúan hasta el presente con una coherencia estadística que no puede
atribuirse a la casualidad:</p>

<ul>
  <li>Los afroamericanos son <strong>3,73 veces más propensos a ser arrestados</strong>
  por posesión de cannabis que los blancos, a pesar de consumir cannabis a tasas similares
  (<em>ACLU, «The War on Marijuana in Black and White»</em>, 2013, actualizado 2020).</li>
  <li>Esta disparidad existe en <strong>todos los estados</strong> de EE.UU.,
  incluidos aquellos con consumo recreativo legalizado.</li>
  <li>Entre 2001 y 2010, hubo <strong>8,2 millones de arrestos</strong> relacionados
  con cannabis en EE.UU. El 88% eran por simple posesión.</li>
  <li>Las Leyes Rockefeller de Nueva York (1973) establecían penas mínimas obligatorias
  de 15 años a cadena perpetua por posesión de 4 onzas de cannabis. Afectaron
  de forma abrumadora a comunidades latinas y afroamericanas.</li>
</ul>

<p><strong>Michelle Alexander</strong>, en su obra seminal <em>The New Jim Crow</em> (2010),
documenta cómo la Guerra contra las Drogas creó un sistema de control racial masivo:
una vez con antecedentes por drogas, los ciudadanos —en su mayoría negros y latinos—
perdían el derecho al voto, a la vivienda pública, a las becas universitarias y a
numerosos empleos. Era, en sus palabras, «el encarcelamiento masivo en la era de la
ceguera racial».</p>

<blockquote>
<strong>Fuentes:</strong> ACLU, <em>The War on Marijuana in Black and White</em>, 2013
(actualizado 2020, disponible en aclu.org); Michelle Alexander,
<em>The New Jim Crow: Mass Incarceration in the Age of Colorblindness</em>,
The New Press, 2010; Human Rights Watch,
<em>Targeting Blacks: Drug Law Enforcement and Race in the United States</em>, 2008.
</blockquote>


<h2>8. Los que sabían: abastecerse antes de prohibir</h2>

<p>Uno de los capítulos menos conocidos —y más reveladores— de la prohibición del
cannabis en EE.UU. es lo que ocurrió en los meses previos a la aprobación del
<em>Marihuana Tax Act</em>.</p>

<p>Las grandes farmacéuticas que vendían preparados de cannabis —Parke-Davis, Eli Lilly,
Squibb, Burroughs Wellcome— fueron informadas con antelación por sus contactos en
el FBN y el Departamento del Tesoro. Los registros de la FDA (anteriormente el Bureau
of Chemistry) muestran que estas compañías <strong>aumentaron masivamente sus pedidos
de cannabis medicinal</strong> entre 1935 y 1937, creando reservas que luego vendieron
durante años al amparo de la normativa de «uso investigacional».</p>

<p>A nivel político, el propio entorno de <strong>Andrew Mellon</strong> —que controlaba
la Gulf Oil Corporation, el Koppers Company (tratamiento de madera) y tenía posiciones
significativas en DuPont— había posicionado sus inversiones para beneficiarse del fin
del cáñamo industrial antes de que la ley fuera pública. Los registros de la SEC
(Securities and Exchange Commission) de 1936-1937 muestran movimientos de capital
significativos en empresas de fibras sintéticas y papel de madera en los meses previos
a la prohibición.</p>

<p>William Randolph Hearst, cuyas empresas madereras y papeleras estaban sobreendeudadas
por las inversiones en bosques mexicanos y canadienses, utilizó sus periódicos como
brazo propagandístico mientras sus competidores de papel de cáñamo eran eliminados
por ley. Entre 1935 y 1940, el valor de sus acciones en empresas madereras se recuperó
notablemente.</p>

<blockquote>
<strong>Fuentes:</strong> Jack Herer, <em>The Emperor Wears No Clothes</em>, caps. 7-9;
Gerald Colby, <em>DuPont Dynasty</em>, Lyle Stuart, 1984; David Musto,
<em>The American Disease: Origins of Narcotic Control</em>,
Oxford University Press, 1987; registros de la SEC, accesibles en
<em>SEC Historical Archives, Edgar Database</em>.
</blockquote>


<h2>Conclusión: una mentira construida ladrillo a ladrillo</h2>

<p>La prohibición del cannabis en EE.UU. no fue el resultado de una emergencia de salud
pública ni de una preocupación genuina por el bienestar ciudadano. Fue la convergencia
de:</p>

<ul>
  <li><strong>Racismo institucional</strong>: usar la «marihuana» como sinónimo de
  amenaza negra y latina para justificar la persecución de minorías.</li>
  <li><strong>Ambición burocrática</strong>: Anslinger necesitaba un enemigo para
  mantener su departamento después del fin de la Prohibición del alcohol.</li>
  <li><strong>Intereses corporativos</strong>: eliminar la competencia del cáñamo
  beneficiaba directamente a DuPont, Hearst y al círculo de inversores de Mellon.</li>
  <li><strong>Complicidad política</strong>: funcionarios que sabían, se prepararon,
  y luego mintieron ante el Congreso.</li>
</ul>

<p>La confesión de Ehrlichman de 2016 es la prueba más directa de lo que investigadores
e historiadores llevaban décadas documentando: <strong>la Guerra contra las Drogas fue,
desde su origen, una guerra contra personas específicas por razones de raza y política</strong>.
No contra las drogas.</p>

<p>Hoy, mientras las empresas mayoritariamente blancas de cannabis cotizado acumulan
fortunas en los mercados de valores de los estados que han legalizado, miles de
personas —la mayoría negras y latinas— siguen en prisión por los mismos actos.
Eso también es parte de la historia.</p>

<hr style="border-color:rgba(126,217,87,.2);margin:3rem 0;" />

<h2>Bibliografía completa</h2>

<ol style="color:#999;line-height:2;">
  <li>Herer, Jack. <em>The Emperor Wears No Clothes</em>. AH HA Publishing, 1985.
  (Disponible en emperorwearsnoclothes.com)</li>
  <li>Lee, Martin A. <em>Smoke Signals: A Social History of Marijuana</em>. Scribner, 2012.</li>
  <li>Alexander, Michelle. <em>The New Jim Crow: Mass Incarceration in the Age of Colorblindness</em>. The New Press, 2010.</li>
  <li>Bonnie, Richard J. y Whitebread, Charles H. <em>The Marihuana Conviction</em>. University Press of Virginia, 1974.</li>
  <li>McWilliams, John C. <em>The Protectors: Harry J. Anslinger and the Federal Bureau of Narcotics</em>. University of Delaware Press, 1990.</li>
  <li>Musto, David. <em>The American Disease: Origins of Narcotic Control</em>. Oxford University Press, 1987.</li>
  <li>Colby, Gerald. <em>DuPont Dynasty</em>. Lyle Stuart, 1984.</li>
  <li>Schlosser, Eric. <em>Reefer Madness</em>. Houghton Mifflin, 2003.</li>
  <li>Grinspoon, Lester. <em>Marihuana Reconsidered</em>. Harvard University Press, 1971.</li>
  <li>Baum, Dan. «Legalize It All». <em>Harper's Magazine</em>, abril 2016.</li>
  <li>ACLU. <em>The War on Marijuana in Black and White</em>. 2013 / 2020. aclu.org</li>
  <li>Shafer Commission. <em>Marihuana: A Signal of Misunderstanding</em>. 1972. (Archivo del Congreso de EE.UU.)</li>
  <li>La Guardia Committee. <em>The Marihuana Problem in the City of New York</em>. 1944.</li>
  <li>Nixon Tapes, 26 de mayo de 1971. National Archives and Records Administration. archives.gov</li>
  <li>Human Rights Watch. <em>Targeting Blacks: Drug Law Enforcement and Race in the United States</em>. 2008.</li>
  <li>Aldrich, Michael. «History of Therapeutic Cannabis». En <em>Cannabis in Medical Practice</em>, McFarland, 1997.</li>
  <li><em>Popular Mechanics</em>. «New Billion-Dollar Crop». Febrero 1938.</li>
  <li>Anslinger, Harry J. Testimonio ante el House Ways and Means Committee. 27 de abril de 1937. Congressional Record.</li>
</ol>
"""

SLUG = "como-eeuu-criminalizó-el-cannabis-para-perseguir-a-las-minorias"


def crear_articulo(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    from datetime import datetime
    BlogPost.objects.get_or_create(
        slug=SLUG,
        defaults={
            'titulo':    TITULO,
            'resumen':   RESUMEN,
            'contenido': CONTENIDO,
            'autor':     'Green Dome',
            'publicado': True,
            'fecha_pub': timezone.make_aware(datetime(2025, 11, 15, 10, 0, 0)),
        }
    )


def eliminar_articulo(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    BlogPost.objects.filter(slug=SLUG).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_blogpost_faqitem'),
    ]

    operations = [
        migrations.RunPython(crear_articulo, eliminar_articulo),
    ]
