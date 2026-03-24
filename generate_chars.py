"""
Genera las tarjetas de personaje para Green Dome.
Cada imagen: 600x750px, estilo ilustrado con los colores de marca.
"""
from PIL import Image, ImageDraw, ImageFilter
import math, os

OUT = "static/img"
os.makedirs(OUT, exist_ok=True)

# ── Paleta de marca ─────────────────────────────────────────────
PURPLE_DEEP  = (13,  10,  20)
PURPLE_DARK  = (26,  13,  46)
PURPLE_MID   = (45,  26,  69)
GREEN_BRIGHT = (126, 217, 87)
GREEN_MID    = (93,  184, 69)
GREEN_DARK   = (26,  74,  14)
GREEN_FOREST = (58,  125, 44)
GOLD         = (201, 168, 76)
WHITE        = (240, 240, 232)

W, H = 600, 750

def lerp_color(a, b, t):
    return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

def gradient_bg(draw, w, h, top_color, bot_color):
    for y in range(h):
        t = y / h
        c = lerp_color(top_color, bot_color, t)
        draw.line([(0, y), (w, y)], fill=c)

def draw_circle(draw, cx, cy, r, fill):
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=fill)

def draw_fur_blob(draw, cx, cy, rx, ry, color, spikes=28, spike_len=22):
    draw.ellipse([cx-rx, cy-ry, cx+rx, cy+ry], fill=color)
    for i in range(spikes):
        angle = (2*math.pi/spikes)*i
        bx = cx + rx*math.cos(angle)
        by = cy + ry*math.sin(angle)
        sl = spike_len * (0.7 + 0.6*((i*7) % 3)/3)
        px = bx + sl*math.cos(angle)
        py = by + sl*math.sin(angle)
        draw.polygon([
            (bx + 4*math.cos(angle+1.5), by + 4*math.sin(angle+1.5)),
            (bx + 4*math.cos(angle-1.5), by + 4*math.sin(angle-1.5)),
            (px, py)
        ], fill=color)

def draw_eyes(draw, cx, cy, size, style="normal"):
    eye_sep = int(size * 1.4)
    for ex in [cx - eye_sep, cx + eye_sep]:
        draw_circle(draw, ex, cy, size, (230, 180, 0))
        draw_circle(draw, ex+2, cy+2, int(size*0.45), (20, 10, 30))
    if style == "halflidded":
        for ex in [cx - eye_sep, cx + eye_sep]:
            draw.arc([ex-size, cy-size, ex+size, cy+size//2],
                     start=200, end=340, fill=(30, 15, 50), width=size//2+2)
    elif style == "wide":
        for ex in [cx - eye_sep, cx + eye_sep]:
            draw_circle(draw, ex - size//4, cy - size//4, size//5, (255, 255, 200))

def draw_mouth(draw, cx, cy, w, style="smile"):
    if style == "smile":
        draw.arc([cx-w, cy, cx+w, cy+w], start=10, end=170, fill=(20, 10, 30), width=5)
        draw_circle(draw, cx, cy + w//2 + 8, w//4, (220, 80, 80))
    elif style == "open_happy":
        draw.arc([cx-w, cy-10, cx+w, cy+w+10], start=5, end=175,
                 fill=(20, 10, 30), width=6)
        draw.ellipse([cx-w+8, cy+8, cx+w-8, cy+w+6], fill=(180, 60, 60))
    elif style == "smirk":
        draw.arc([cx-w+10, cy, cx+w, cy+w-10], start=20, end=160,
                 fill=(20, 10, 30), width=5)

def add_glow(img, center, radius, color, intensity=60):
    glow = Image.new('RGBA', img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx, cy = center
    for r in range(radius, 0, -4):
        a = int(intensity * (1 - r/radius)**1.5)
        gd.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color + (a,))
    blurred = glow.filter(ImageFilter.GaussianBlur(28))
    return Image.alpha_composite(img.convert('RGBA'), blurred).convert('RGB')

def draw_shirt(draw, cx, top_y, shirt_color, text_color):
    pts = [
        (cx-90, top_y+20), (cx-110, top_y), (cx-72, top_y-18),
        (cx+72, top_y-18), (cx+110, top_y), (cx+90, top_y+20),
        (cx+100, top_y+160), (cx-100, top_y+160),
    ]
    draw.polygon(pts, fill=shirt_color)
    # "GREEN DOME" como bloques de color (sin fuente externa)
    for i, (txt, dy) in enumerate([("GREEN", 55), ("DOME", 105)]):
        bw = len(txt) * 16
        draw.rounded_rectangle(
            [cx - bw//2 - 4, top_y + dy - 18, cx + bw//2 + 4, top_y + dy + 8],
            radius=6, fill=text_color
        )

def noise_overlay(img, alpha=16):
    import random
    pixels = img.load()
    for y in range(0, img.height, 2):
        for x in range(0, img.width, 2):
            if random.random() < 0.10:
                r, g, b = pixels[x, y][:3]
                d = random.randint(-alpha, alpha)
                pixels[x, y] = (
                    min(255, max(0, r+d)),
                    min(255, max(0, g+d)),
                    min(255, max(0, b+d))
                )

# ─────────────────────────────────────────────────────────────
# FUNDADOR — slim, confiado, manos en bolsillos
# ─────────────────────────────────────────────────────────────
def make_fundador():
    img = Image.new('RGB', (W, H), PURPLE_DEEP)
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, W, H, (22, 42, 14), (10, 5, 20))
    img = add_glow(img, (W//2, 330), 210, GREEN_FOREST, 80)
    draw = ImageDraw.Draw(img)
    GC = (100, 170, 65)
    GD = (55, 115, 35)
    GL = (145, 215, 105)
    # piernas
    draw_fur_blob(draw, W//2-30, 590, 30, 60, GC, 20, 10)
    draw_fur_blob(draw, W//2+30, 590, 30, 60, GC, 20, 10)
    draw.ellipse([W//2-68, 628, W//2-8, 652], fill=GD)
    draw.ellipse([W//2+8,  628, W//2+68, 652], fill=GD)
    # torso
    draw_fur_blob(draw, W//2, 480, 82, 115, GC, 34, 16)
    draw_fur_blob(draw, W//2, 480, 66, 95, GC, 0, 0)
    # brazos (manos en bolsillos)
    draw_fur_blob(draw, W//2-95, 490, 24, 58, GC, 20, 10)
    draw_fur_blob(draw, W//2+95, 490, 24, 58, GC, 20, 10)
    # cabeza
    draw_fur_blob(draw, W//2, 292, 98, 94, GC, 38, 24)
    draw_fur_blob(draw, W//2, 292, 82, 78, GC, 0, 0)
    draw_eyes(draw, W//2, 278, 20, "halflidded")
    draw_mouth(draw, W//2, 318, 30, "smirk")
    draw.ellipse([W//2-42, 240, W//2-12, 260], fill=GL)
    noise_overlay(img)
    return img

# ─────────────────────────────────────────────────────────────
# SABIO — grande, bastón, dedo levantado
# ─────────────────────────────────────────────────────────────
def make_sabio():
    img = Image.new('RGB', (W, H), PURPLE_DEEP)
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, W, H, (20, 10, 42), (8, 4, 18))
    img = add_glow(img, (W//2, 380), 260, (45, 26, 69), 90)
    draw = ImageDraw.Draw(img)
    GC = (90, 155, 55)
    GD = (50, 100, 30)
    GL = (130, 200, 90)
    # piernas (agachado)
    draw_fur_blob(draw, W//2-55, 605, 42, 52, GC, 22, 12)
    draw_fur_blob(draw, W//2+38, 595, 40, 50, GC, 22, 12)
    # torso grande
    draw_fur_blob(draw, W//2, 495, 115, 135, GC, 42, 22)
    draw_fur_blob(draw, W//2, 495, 92, 112, GC, 0, 0)
    # brazo izq + bastón
    draw_fur_blob(draw, W//2-105, 525, 30, 72, GC, 22, 12)
    draw_circle(draw, W//2-105, 606, 26, GC)
    draw.rectangle([W//2-113, 595, W//2-97, 735], fill=(139, 90, 43))
    draw.ellipse([W//2-125, 726, W//2-85, 744], fill=(110, 70, 30))
    # brazo der + dedo arriba
    draw_fur_blob(draw, W//2+105, 445, 30, 72, GC, 22, 12)
    draw_circle(draw, W//2+105, 365, 30, GC)
    draw.rectangle([W//2+98, 322, W//2+112, 368], fill=GL)
    draw_circle(draw, W//2+105, 318, 14, GL)
    # cabeza grande
    draw_fur_blob(draw, W//2, 292, 118, 114, GC, 44, 28)
    draw_fur_blob(draw, W//2, 292, 98, 94, GC, 0, 0)
    # barba
    draw_fur_blob(draw, W//2, 358, 82, 48, GD, 26, 18)
    draw_eyes(draw, W//2, 272, 23, "halflidded")
    # diente
    draw.rectangle([W//2-7, 342, W//2+7, 362], fill=WHITE)
    draw_mouth(draw, W//2, 340, 30, "smirk")
    noise_overlay(img)
    return img

# ─────────────────────────────────────────────────────────────
# SOCIAL — ojos grandes, feliz, camiseta GD
# ─────────────────────────────────────────────────────────────
def make_social():
    img = Image.new('RGB', (W, H), (8, 30, 22))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, W, H, (10, 40, 28), (5, 15, 12))
    img = add_glow(img, (W//2, 350), 255, (20, 80, 50), 100)
    draw = ImageDraw.Draw(img)
    GC = (80, 170, 55)
    GD = (45, 110, 30)
    GL = (140, 215, 105)
    SHIRT = (90, 50, 140)
    # piernas
    draw_fur_blob(draw, W//2-44, 632, 40, 62, GC, 24, 12)
    draw_fur_blob(draw, W//2+44, 632, 40, 62, GC, 24, 12)
    # torso + camiseta
    draw_fur_blob(draw, W//2, 515, 105, 122, GC, 36, 18)
    draw_fur_blob(draw, W//2, 515, 85, 100, GC, 0, 0)
    draw_shirt(draw, W//2, 440, SHIRT, GREEN_BRIGHT)
    # brazos
    draw_fur_blob(draw, W//2-118, 508, 32, 68, GC, 24, 14)
    draw_fur_blob(draw, W//2+118, 508, 32, 68, GC, 24, 14)
    draw_circle(draw, W//2-118, 582, 30, GC)
    draw_circle(draw, W//2+118, 582, 30, GC)
    # cabeza grande redonda
    draw_fur_blob(draw, W//2, 292, 118, 112, GC, 42, 26)
    draw_fur_blob(draw, W//2, 292, 98, 92, GC, 0, 0)
    draw_eyes(draw, W//2, 272, 30, "wide")
    draw_mouth(draw, W//2, 322, 40, "open_happy")
    draw.ellipse([W//2-52, 234, W//2-16, 258], fill=GL)
    noise_overlay(img)
    return img

# ─────────────────────────────────────────────────────────────
# ZEN — relajado, camiseta GD, ojos entrecerrados
# ─────────────────────────────────────────────────────────────
def make_zen():
    img = Image.new('RGB', (W, H), PURPLE_DEEP)
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, W, H, (35, 15, 65), (8, 4, 20))
    img = add_glow(img, (W//2, 355), 245, (60, 30, 100), 90)
    draw = ImageDraw.Draw(img)
    GC = (85, 165, 60)
    GD = (48, 105, 32)
    SHIRT = (90, 50, 140)
    # piernas
    draw_fur_blob(draw, W//2-44, 628, 38, 60, GC, 22, 12)
    draw_fur_blob(draw, W//2+44, 628, 38, 60, GC, 22, 12)
    # torso + camiseta
    draw_fur_blob(draw, W//2, 508, 102, 120, GC, 36, 16)
    draw_fur_blob(draw, W//2, 508, 84, 100, GC, 0, 0)
    draw_shirt(draw, W//2, 432, SHIRT, GREEN_BRIGHT)
    # brazos relajados
    draw_fur_blob(draw, W//2-112, 522, 30, 64, GC, 22, 12)
    draw_fur_blob(draw, W//2+112, 522, 30, 64, GC, 22, 12)
    draw_circle(draw, W//2-112, 596, 28, GC)
    draw_circle(draw, W//2+112, 596, 28, GC)
    # cabeza
    draw_fur_blob(draw, W//2, 294, 110, 106, GC, 40, 24)
    draw_fur_blob(draw, W//2, 294, 92, 88, GC, 0, 0)
    draw_eyes(draw, W//2, 280, 22, "halflidded")
    # párpados extra pesados
    for ex in [W//2 - 30, W//2 + 30]:
        draw.arc([ex-22, 258, ex+22, 302], start=190, end=350, fill=GD, width=13)
    draw_mouth(draw, W//2, 322, 28, "smile")
    # humo abstracto
    for i in range(4):
        draw_circle(draw, W//2 - 55 + i*22, 215 - i*20, 6+i*4, (200, 175, 218))
    noise_overlay(img)
    return img

# ─────────────────────────────────────────────────────────────
# ARTESANO — robusto, camiseta GD, en mesa
# ─────────────────────────────────────────────────────────────
def make_artesano():
    img = Image.new('RGB', (W, H), (8, 30, 22))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, W, H, (10, 38, 25), (5, 15, 12))
    img = add_glow(img, (W//2, 345), 245, (20, 70, 40), 95)
    draw = ImageDraw.Draw(img)
    GC = (78, 168, 50)
    GD = (44, 108, 28)
    GL = (138, 210, 98)
    SHIRT = (90, 50, 140)
    TABLE = (160, 50, 40)
    # mesa
    draw.rectangle([0, 562, W, H], fill=TABLE)
    draw.rectangle([0, 558, W, 566], fill=(120, 35, 28))
    # torso grande
    draw_fur_blob(draw, W//2, 488, 122, 105, GC, 40, 20)
    draw_fur_blob(draw, W//2, 488, 100, 85, GC, 0, 0)
    draw_shirt(draw, W//2, 420, SHIRT, GREEN_BRIGHT)
    # brazos sobre mesa
    draw_fur_blob(draw, W//2-115, 548, 38, 40, GC, 22, 12)
    draw_fur_blob(draw, W//2+115, 548, 38, 40, GC, 22, 12)
    draw_circle(draw, W//2-115, 562, 32, GC)
    draw_circle(draw, W//2+115, 562, 32, GC)
    # cabeza grande y redonda
    draw_fur_blob(draw, W//2, 285, 128, 122, GC, 46, 28)
    draw_fur_blob(draw, W//2, 285, 106, 100, GC, 0, 0)
    draw_eyes(draw, W//2, 268, 28, "wide")
    draw_circle(draw, W//2, 308, 15, (60, 120, 40))
    draw_mouth(draw, W//2, 318, 44, "open_happy")
    draw.ellipse([W//2-54, 230, W//2-16, 254], fill=GL)
    # neón hoja abstracto
    for r in [32, 24, 16]:
        draw.ellipse([76-r, 96-r, 76+r, 96+r], outline=(220, 80, 200), width=3)
    draw.line([76, 128, 76, 162], fill=(220, 80, 200), width=3)
    noise_overlay(img)
    return img


# ─────────────────────────────────────────────────────────────
# EJECUTAR
# ─────────────────────────────────────────────────────────────
chars = [
    ("char-fundador.png", make_fundador),
    ("char-sabio.png",    make_sabio),
    ("char-social.png",   make_social),
    ("char-zen.png",      make_zen),
    ("char-artesano.png", make_artesano),
]

for fname, fn in chars:
    print(f"Generando {fname}...")
    im = fn()
    path = os.path.join(OUT, fname)
    im.save(path, "PNG", optimize=True)
    print(f"  guardado: {path}")

print("\nTodos los personajes generados.")
