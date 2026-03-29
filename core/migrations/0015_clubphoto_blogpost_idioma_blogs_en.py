"""
Migration 0015:
1. Add idioma field to BlogPost (es/en/it)
2. Add ClubPhoto model
3. Add 5 English blog posts for /cannabis-club-seville/
"""
from django.db import migrations, models
from django.utils import timezone
from datetime import datetime


POSTS_EN = [
    {
        'titulo': 'What is a cannabis social club in Spain? A complete guide for visitors to Seville',
        'slug': 'what-is-cannabis-social-club-spain-guide-seville',
        'resumen': (
            "Spain's cannabis social clubs are unlike anything you'll find in Amsterdam or a US dispensary. "
            "Here's everything you need to know about how they work — and why Seville's Green Dome is a prime example."
        ),
        'contenido': """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
<em>&laquo;Spain has some of the most interesting cannabis culture in Europe &mdash; not despite its laws, but because of them.&raquo;</em>
</p>

<h2>Cannabis is not legal in Spain &mdash; so what exactly are social clubs?</h2>

<p>Let's clear up the most common misconception first: <strong>cannabis is not fully legal in Spain</strong>.
Possession and consumption in public remain prohibited under the 1992 Citizens' Security Law.
However, Spanish courts have consistently ruled that <strong>private consumption and collective cultivation
among adults is decriminalised</strong> &mdash; meaning it falls outside criminal law as long as it is
private, non-commercial and between adults.</p>

<p>Cannabis social clubs (<em>asociaciones cann&aacute;bicas</em>) exploit this legal grey zone.
They are registered <strong>non-profit private associations</strong> whose members collectively
cultivate cannabis for their own consumption. Key principles:</p>

<ul>
  <li><strong>Non-profit</strong>: no one earns money selling cannabis. Members contribute to costs.</li>
  <li><strong>Closed membership</strong>: you must be invited by an existing member and register formally.</li>
  <li><strong>Adults only</strong>: minimum age is 18 in Spain.</li>
  <li><strong>Private premises</strong>: consumption happens inside the club, never in public.</li>
  <li><strong>Collective cultivation</strong>: the club grows its own; nothing is bought or sold commercially.</li>
</ul>

<blockquote>
<strong>Source:</strong> Decoroso Ramos Padilla, &laquo;El cannabis en Espa&ntilde;a: entre la prohibici&oacute;n y la tolerancia&raquo;,
<em>Revista de Derecho Penal y Criminolog&iacute;a</em>, UNED, 2019.
</blockquote>

<h2>How does Green Dome work in Seville?</h2>

<p>Green Dome is a registered <em>asociaci&oacute;n cann&aacute;bica</em> in Seville's <strong>Nervi&oacute;n neighbourhood</strong>.
It operates as a genuinely private social club &mdash; not a store, not a dispensary, not open to the general public.
All products are grown by the association itself (<em>autocultivo propio</em>), ensuring quality control
at every stage with no commercial intermediaries.</p>

<h2>Cannabis social clubs vs. Amsterdam coffeeshops</h2>

<p>Many visitors confuse Spanish clubs with Dutch coffeeshops. The differences are fundamental:</p>
<ul>
  <li>Coffeeshops are retail outlets &mdash; anyone can walk in and buy. They are commercial businesses.</li>
  <li>Spanish social clubs are private associations. You need to be a registered member.
  There is no retail sale.</li>
</ul>

<blockquote>
<strong>Sources:</strong> Tom Decorte et al., &laquo;A world survey of cannabis social clubs&raquo;,
<em>Drugs: Education, Prevention and Policy</em>, vol. 24, 2017;
M&agrave;rius Oller Sala, &laquo;Cannabis social clubs in Spain&raquo;, Global Drug Policy Observatory, 2015.
</blockquote>

<hr>
<p style="color:#888;font-size:.9rem;"><strong>Bibliography:</strong> Ramos Padilla (2019) &middot; Decorte et al. (2017) &middot; Oller Sala (2015).</p>
""",
        'fecha': datetime(2026, 1, 10, 10, 0, 0),
    },
    {
        'titulo': 'Cannabis clubs vs dispensaries: why Spain is different from the rest of Europe',
        'slug': 'cannabis-clubs-vs-dispensaries-spain-different-europe',
        'resumen': (
            "From Amsterdam to Barcelona, every country has its own cannabis culture. "
            "Spain's private club model is unique &mdash; and increasingly influential worldwide. Here's why."
        ),
        'contenido': """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
<em>&laquo;The Spanish model is the most community-oriented cannabis framework in Europe.&raquo;</em><br>
<strong style="color:#7ed957;">&mdash; Global Drug Policy Observatory, Swansea University</strong>
</p>

<h2>The European cannabis patchwork</h2>

<ul>
  <li>Netherlands: retail tolerated in coffeeshops, cultivation still illegal. Commercial, open to tourists.</li>
  <li>Portugal: all drugs decriminalised since 2001, but no regulated retail.</li>
  <li>Germany: social clubs legalised in 2024, modelled partly on the Spanish system.</li>
  <li>Spain: private consumption and collective cultivation decriminalised, social clubs operate in a legally protected grey zone.</li>
</ul>

<h2>Why the Spanish model matters globally</h2>

<p>When Germany legalised cannabis social clubs in 2024, it explicitly referenced the Spanish model as inspiration.
Studies show that club members report higher awareness of harm reduction, lower rates of problematic use
and stronger social bonds compared to retail-only markets.</p>

<blockquote>
<strong>Sources:</strong> Decorte, T. et al., <em>International Journal of Drug Policy</em>, 2017;
Hughes, B. &amp; Collin, C., EMCDDA, 2019.
</blockquote>

<hr>
<p style="color:#888;font-size:.9rem;"><strong>Bibliography:</strong> Decorte et al. (2017) &middot; EMCDDA (2019).</p>
""",
        'fecha': datetime(2026, 1, 20, 10, 0, 0),
    },
    {
        'titulo': 'How to join a cannabis club in Seville: a step-by-step guide',
        'slug': 'how-to-join-cannabis-club-seville-step-by-step-guide',
        'resumen': (
            "Thinking about joining a cannabis social club in Seville? Here's exactly how the membership "
            "process works at Green Dome &mdash; from first contact to becoming a full member."
        ),
        'contenido': """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
<em>&laquo;Membership is not a purchase &mdash; it's an invitation into a community.&raquo;</em>
</p>

<h2>Can anyone join a cannabis club in Seville?</h2>

<p>Not quite. Spanish cannabis social clubs operate as <strong>private, closed associations</strong>.
Membership requires:</p>
<ul>
  <li>Being at least <strong>18 years old</strong></li>
  <li>Being <strong>referred by an existing member</strong> or making direct contact with the club</li>
  <li>Completing a <strong>formal registration</strong> as a member of the association</li>
</ul>

<h2>Step 1 &mdash; Make contact</h2>
<p>Reach out to Green Dome directly:</p>
<ul>
  <li>WhatsApp: <strong>+34 681 296 703</strong></li>
  <li>Email: <strong>lacupulaverdesv@gmail.com</strong></li>
  <li>Instagram: <strong>@greendomegd</strong></li>
</ul>

<h2>Step 2 &mdash; Registration</h2>
<p>Complete a brief registration as a member of the association. This formalises your status
as a private member and is what distinguishes the club from any kind of retail operation.</p>

<h2>Step 3 &mdash; Visit the club</h2>
<p>After registration you can visit Green Dome in Seville's <strong>Nervi&oacute;n neighbourhood</strong>.
The exact address is provided to registered members.</p>

<h2>What to expect as a member</h2>
<ul>
  <li>Access to high-quality products from our own cultivation</li>
  <li>A genuine community with regular events</li>
  <li>Education sessions on responsible consumption</li>
  <li>A completely private, safe space</li>
</ul>

<hr>
<p style="color:#888;font-size:.9rem;">Contact: <strong>lacupulaverdesv@gmail.com</strong> | WhatsApp <strong>+34 681 296 703</strong></p>
""",
        'fecha': datetime(2026, 2, 1, 10, 0, 0),
    },
    {
        'titulo': 'Terpenes 101: why cannabis smells the way it does &mdash; and why it matters',
        'slug': 'terpenes-101-why-cannabis-smells-different-varieties-explained',
        'resumen': (
            "Earthy, citrusy, piney, sweet &mdash; the scent of cannabis is not random. "
            "Terpenes are the molecules behind the aroma and, increasingly, scientists think they shape the effect too."
        ),
        'contenido': """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
<em>&laquo;The nose knows. Terpenes are nature's chemical fingerprints &mdash; and cannabis has over 200 of them.&raquo;</em>
</p>

<h2>What are terpenes?</h2>
<p>Terpenes are <strong>aromatic organic compounds</strong> produced by many plants &mdash; not just cannabis.
In cannabis, terpenes are produced in the same trichomes that produce cannabinoids like THC and CBD.
The cannabis plant produces over <strong>200 different terpenes</strong>, though only a handful
appear in significant concentrations in any given variety.</p>

<h2>The most important cannabis terpenes</h2>
<ul>
  <li><strong>Myrcene</strong> (earthy, musky) &mdash; the most abundant. Also in hops and mangoes. Associated with relaxing effects.</li>
  <li><strong>Limonene</strong> (citrus) &mdash; found in citrus rinds. Associated with mood elevation and stress relief.</li>
  <li><strong>Pinene</strong> (pine, fresh) &mdash; the most widespread terpene in nature. Associated with alertness.</li>
  <li><strong>Caryophyllene</strong> (spicy, peppery) &mdash; unique: also binds to CB2 receptors. Anti-inflammatory.</li>
  <li><strong>Linalool</strong> (floral, lavender) &mdash; the same terpene in lavender. Associated with calming effects.</li>
</ul>

<blockquote>
<strong>Sources:</strong> Russo, E.B., &laquo;Taming THC&raquo;, <em>British Journal of Pharmacology</em>, 2011;
Sommano, S.R. et al., <em>Molecules</em>, 2020.
</blockquote>

<h2>The entourage effect</h2>
<p>The hypothesis: cannabinoids and terpenes work together synergistically, with terpenes potentially
modifying how THC affects the brain. The scientific evidence is still building, but the clinical
implications are significant for medical cannabis research.</p>

<hr>
<p style="color:#888;font-size:.9rem;"><strong>Bibliography:</strong> Russo (2011) &middot; Sommano et al. (2020) &middot; Ben-Shabat &amp; Mechoulam (1998).</p>
""",
        'fecha': datetime(2026, 2, 15, 10, 0, 0),
    },
    {
        'titulo': 'Sativa, indica, hybrid: is the classification system actually useful?',
        'slug': 'sativa-indica-hybrid-classification-cannabis-science-explained',
        'resumen': (
            "For decades everyone assumed sativas gave energy and indicas gave relaxation. "
            "Modern cannabis science says it's far more complicated &mdash; and the old labels may be misleading you."
        ),
        'contenido': """
<p style="font-size:1.1rem;color:#ddd;line-height:1.9;border-left:4px solid #7ed957;padding-left:1.2rem;margin-bottom:2.5rem;">
<em>&laquo;Calling cannabis &lsquo;sativa&rsquo; or &lsquo;indica&rsquo; is a bit like judging wine only by the shape of the bottle.&raquo;</em>
</p>

<h2>Where did sativa and indica come from?</h2>
<p><em>Cannabis sativa</em> was classified by Linnaeus in 1753, describing tall hemp plants.
<em>Cannabis indica</em> was named by Lamarck in 1785, describing shorter plants from India used for hashish.
The modern association of &ldquo;sativa = energising, indica = sedating&rdquo; is largely a
<strong>folk taxonomy that emerged in the North American cannabis market in the 1970s-80s</strong>,
spread by growers and users, not scientists.</p>

<h2>What does the science say?</h2>
<p>A 2015 study by Sawler et al. in <em>PLOS ONE</em> found that genetic analysis of 81 strains
showed <strong>significant overlap between plants labelled sativa and indica</strong> &mdash;
many were genetically indistinguishable. A 2018 meta-analysis confirmed that
<strong>terpene profiles, not indica/sativa labels, better predicted reported effects</strong>.</p>

<blockquote>
<strong>Sources:</strong> Sawler, J. et al., <em>PLOS ONE</em>, 2015;
Lewis, M.A. et al., <em>Cannabis and Cannabinoid Research</em>, 2018.
</blockquote>

<h2>What actually predicts the effect?</h2>
<ol>
  <li><strong>Your individual biology</strong> &mdash; genetics, tolerance, prior experience, mood, setting.</li>
  <li><strong>The terpene profile</strong> &mdash; myrcene toward relaxation, limonene toward mood elevation.</li>
  <li><strong>THC:CBD ratio</strong> &mdash; high-THC with little CBD tends to be more intoxicating.</li>
</ol>

<hr>
<p style="color:#888;font-size:.9rem;"><strong>Bibliography:</strong> Sawler et al. (2015) &middot; Lewis et al. (2018).</p>
""",
        'fecha': datetime(2026, 3, 1, 10, 0, 0),
    },
]


def add_posts_and_model(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    # Mark existing posts as Spanish
    BlogPost.objects.filter(idioma='').update(idioma='es')
    # Create 5 English posts
    for p in POSTS_EN:
        BlogPost.objects.get_or_create(
            slug=p['slug'],
            defaults={
                'titulo':    p['titulo'],
                'resumen':   p['resumen'],
                'contenido': p['contenido'],
                'autor':     'Green Dome',
                'idioma':    'en',
                'publicado': True,
                'fecha_pub': timezone.make_aware(p['fecha']),
            }
        )


def remove_en_posts(apps, schema_editor):
    BlogPost = apps.get_model('core', 'BlogPost')
    slugs = [p['slug'] for p in POSTS_EN]
    BlogPost.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_blog_cuatro_articulos_seo'),
    ]

    operations = [
        # 1. Add idioma field to BlogPost
        migrations.AddField(
            model_name='blogpost',
            name='idioma',
            field=models.CharField(
                choices=[('es', 'Español'), ('en', 'English'), ('it', 'Italiano')],
                default='es',
                help_text='Idioma del artículo.',
                max_length=2,
                verbose_name='Idioma',
            ),
        ),
        # 2. Add ClubPhoto model
        migrations.CreateModel(
            name='ClubPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(
                    help_text='Sube una foto del interior.',
                    upload_to='club/',
                    verbose_name='Foto',
                )),
                ('titulo', models.CharField(blank=True, max_length=150, verbose_name='Título / Pie de foto')),
                ('descripcion', models.CharField(blank=True, max_length=300, verbose_name='Descripción (alt)')),
                ('orden', models.PositiveSmallIntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Foto del club',
                'verbose_name_plural': 'The Club — Galería de fotos',
                'ordering': ['orden'],
            },
        ),
        # 3. Insert English blog posts
        migrations.RunPython(add_posts_and_model, remove_en_posts),
    ]
