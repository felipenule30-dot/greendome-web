"""
Green Dome — Generador de GIFs animados
Ejecutar: venv/Scripts/python generate_gifs.py
Requiere: Pillow (ya instalado)
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = os.path.join("static", "img")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Paleta de colores ──────────────────────────────────────────────────────────
PURPLE_DEEP   = (13,  10,  20)
PURPLE_DARK   = (26,  13,  46)
PURPLE_MID    = (45,  26,  69)
GREEN_BRIGHT  = (126, 217, 87)
GREEN_MID     = (93,  184, 69)
GREEN_DARK    = (58,  125, 44)
WHITE         = (240, 240, 232)
TRANSPARENT   = (0, 0, 0, 0)

# ─────────────────────────────────────────────────────────────────────────────
# GIF 1: mascota flotante (bouncing mascot)
# ─────────────────────────────────────────────────────────────────────────────
def draw_mascot(draw, cx, cy, scale=1.0, eye_open=True):
    """Dibuja el monstruito peludo de Green Dome."""
    r = int(55 * scale)

    # Pelo exterior (spikes irregulares)
    spike_data = [
        (0, -r-14), (20, -r-10), (r+10, -10), (r+14, 15),
        (r+8, r+5), (10, r+12), (-10, r+12), (-r-8, r+5),
        (-r-14, 15), (-r-10, -10), (-20, -r-10),
    ]
    spike_poly = [(cx + int(x*scale), cy + int(y*scale)) for x, y in spike_data]
    draw.polygon(spike_poly, fill=(80, 160, 65))

    # Cuerpo principal (círculo verde)
    body_color = (110, 185, 90)
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=body_color, outline=(40, 80, 30), width=3)

    # Highlights del pelo (líneas curvas simuladas con arcos)
    hl = (130, 200, 110)
    draw.arc([cx-r+8, cy-r+8, cx-r+28, cy-r+28], 200, 320, fill=hl, width=2)
    draw.arc([cx+r-30, cy-r+12, cx+r-8, cy-r+32], 220, 340, fill=hl, width=2)
    draw.arc([cx-15, cy-r+5, cx+15, cy-r+20], 180, 360, fill=hl, width=2)

    # Ojos
    eye_y = cy - int(10 * scale)
    eye_rx = int(18 * scale)
    eye_ry = int(10 * scale) if eye_open else int(3 * scale)

    # Ojo izquierdo
    draw.ellipse([cx-eye_rx-int(16*scale), eye_y-eye_ry,
                  cx-eye_rx+int(16*scale), eye_y+eye_ry],
                 fill=(230, 190, 30), outline=(20, 10, 0), width=2)
    # Pupila izq
    if eye_open:
        draw.ellipse([cx-eye_rx-int(5*scale), eye_y-int(5*scale),
                      cx-eye_rx+int(5*scale), eye_y+int(5*scale)],
                     fill=(20, 10, 0))

    # Ojo derecho
    draw.ellipse([cx+eye_rx-int(16*scale), eye_y-eye_ry,
                  cx+eye_rx+int(16*scale), eye_y+eye_ry],
                 fill=(230, 190, 30), outline=(20, 10, 0), width=2)
    if eye_open:
        draw.ellipse([cx+eye_rx-int(5*scale), eye_y-int(5*scale),
                      cx+eye_rx+int(5*scale), eye_y+int(5*scale)],
                     fill=(20, 10, 0))

    # Boca (sonrisa)
    mouth_y = cy + int(18 * scale)
    draw.arc([cx - int(22*scale), mouth_y - int(12*scale),
              cx + int(22*scale), mouth_y + int(8*scale)],
             start=10, end=170, fill=(20, 10, 0), width=3)
    # Lengua
    draw.ellipse([cx - int(10*scale), mouth_y - int(2*scale),
                  cx + int(10*scale), mouth_y + int(10*scale)],
                 fill=(220, 80, 80))


def make_gif_mascot():
    frames = []
    n_frames = 24
    W, H = 300, 340

    for i in range(n_frames):
        img = Image.new("RGBA", (W, H), (*PURPLE_MID, 255))
        draw = ImageDraw.Draw(img)

        # Sombra en el suelo (elipse)
        t = i / n_frames
        bounce = math.sin(t * math.pi * 2)
        shadow_scale = 0.7 + 0.3 * (1 - abs(bounce) * 0.5)
        shadow_alpha = int(80 + 40 * (1 - abs(bounce)))
        shadow_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(shadow_img)
        sx = W // 2
        sy = H - 40
        sdraw.ellipse([sx - int(60*shadow_scale), sy - 12,
                       sx + int(60*shadow_scale), sy + 12],
                      fill=(20, 10, 40, shadow_alpha))
        img = Image.alpha_composite(img, shadow_img)
        draw = ImageDraw.Draw(img)

        # Posición flotante
        cy = int(H // 2 - 10 + bounce * 18)
        cx = W // 2

        # Parpadeo en frame 8-9
        eye_open = not (i in (8, 9))
        draw_mascot(draw, cx, cy, scale=1.0, eye_open=eye_open)

        # Partículas verdes flotando
        for j in range(5):
            px = int(30 + (j * 57 + i * 3) % (W - 60))
            py = int(H - 30 - ((i * 8 + j * 41) % (H - 80)))
            alpha_p = int(80 + 60 * math.sin((i + j * 5) / n_frames * math.pi * 2))
            pdot = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            pd = ImageDraw.Draw(pdot)
            pd.ellipse([px-3, py-3, px+3, py+3], fill=(*GREEN_BRIGHT, alpha_p))
            img = Image.alpha_composite(img, pdot)

        frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=128))

    path = os.path.join(OUTPUT_DIR, "mascot-bounce.gif")
    frames[0].save(
        path, save_all=True, append_images=frames[1:],
        optimize=True, duration=60, loop=0, disposal=2,
    )
    print(f"[OK]  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# GIF 2: logo pulse (el arco domo pulsando)
# ─────────────────────────────────────────────────────────────────────────────
def make_gif_logo_pulse():
    frames = []
    n_frames = 20
    W, H = 280, 200

    for i in range(n_frames):
        img = Image.new("RGBA", (W, H), (*PURPLE_DARK, 255))
        draw = ImageDraw.Draw(img)
        t = i / n_frames
        glow = 0.5 + 0.5 * math.sin(t * math.pi * 2)

        cx, cy = W // 2, H // 2 + 10
        r_outer = 70
        r_inner = 42

        # Glow externo
        for g in range(6, 0, -1):
            alpha_g = int(30 * glow * (g / 6))
            gimg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            gd = ImageDraw.Draw(gimg)
            gr = r_outer + g * 4
            gd.arc([cx - gr, cy - gr + 10, cx + gr, cy + gr],
                   start=180, end=0,
                   fill=(*GREEN_BRIGHT, alpha_g), width=8 + g * 2)
            img = Image.alpha_composite(img, gimg)

        # Arco exterior
        width_outer = int(14 + 4 * glow)
        draw.arc([cx - r_outer, cy - r_outer + 10, cx + r_outer, cy + r_outer],
                 start=180, end=0,
                 fill=(*GREEN_BRIGHT, 255), width=width_outer)

        # Arco interior
        width_inner = int(9 + 2 * glow)
        inner_alpha = int(130 + 80 * glow)
        iimg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        id_ = ImageDraw.Draw(iimg)
        id_.arc([cx - r_inner, cy - r_inner + 14, cx + r_inner, cy + r_inner],
                start=180, end=0,
                fill=(*GREEN_BRIGHT, inner_alpha), width=width_inner)
        img = Image.alpha_composite(img, iimg)

        # Texto "GREEN DOME" simulado con rectángulos
        draw2 = ImageDraw.Draw(img)
        text_alpha = int(200 + 55 * glow)
        try:
            # Intentar cargar fuente del sistema
            fnt = ImageFont.truetype("arial.ttf", 20)
        except Exception:
            fnt = ImageFont.load_default()
        timg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        td = ImageDraw.Draw(timg)
        td.text((W // 2, H - 35), "GREEN DOME",
                fill=(*GREEN_BRIGHT, text_alpha),
                font=fnt, anchor="mm")
        img = Image.alpha_composite(img, timg)

        frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=64))

    path = os.path.join(OUTPUT_DIR, "logo-pulse.gif")
    frames[0].save(
        path, save_all=True, append_images=frames[1:],
        optimize=True, duration=80, loop=0, disposal=2,
    )
    print(f"[OK]  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# GIF 3: partículas flotantes (para hero background)
# ─────────────────────────────────────────────────────────────────────────────
def make_gif_particles():
    frames = []
    n_frames = 30
    W, H = 600, 400
    n_dots = 40

    import random
    random.seed(42)
    dots = [
        {
            "x": random.uniform(0, W),
            "y": random.uniform(0, H),
            "r": random.uniform(1.5, 4),
            "vx": random.uniform(-0.5, 0.5),
            "vy": random.uniform(-1.2, -0.3),
            "color": random.choice([GREEN_BRIGHT, GREEN_MID, GREEN_DARK, (200, 160, 60)]),
            "phase": random.uniform(0, math.pi * 2),
        }
        for _ in range(n_dots)
    ]

    for i in range(n_frames):
        img = Image.new("RGBA", (W, H), (*PURPLE_DEEP, 255))

        # Fondo gradiente simulado
        for row in range(0, H, 4):
            progress = row / H
            r = int(PURPLE_DEEP[0] + (PURPLE_MID[0] - PURPLE_DEEP[0]) * progress * 0.4)
            g = int(PURPLE_DEEP[1] + (PURPLE_MID[1] - PURPLE_DEEP[1]) * progress * 0.4)
            b = int(PURPLE_DEEP[2] + (PURPLE_MID[2] - PURPLE_DEEP[2]) * progress * 0.4)
            draw = ImageDraw.Draw(img)
            draw.rectangle([0, row, W, row+4], fill=(r, g, b, 255))

        # Dibujar partículas
        for dot in dots:
            dot["x"] = (dot["x"] + dot["vx"]) % W
            dot["y"] = dot["y"] + dot["vy"]
            if dot["y"] < -10:
                dot["y"] = H + 5
                dot["x"] = random.uniform(0, W)

            # Alpha pulsante
            alpha = int(100 + 100 * math.sin(i / n_frames * math.pi * 2 + dot["phase"]))
            alpha = max(20, min(200, alpha))

            pdot = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            pd = ImageDraw.Draw(pdot)
            x, y, r = dot["x"], dot["y"], dot["r"]
            pd.ellipse([x-r, y-r, x+r, y+r], fill=(*dot["color"], alpha))
            img = Image.alpha_composite(img, pdot)

        frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=64))

    path = os.path.join(OUTPUT_DIR, "hero-particles.gif")
    frames[0].save(
        path, save_all=True, append_images=frames[1:],
        optimize=True, duration=80, loop=0, disposal=2,
    )
    print(f"[OK]  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# Placeholder PNG para hero poster y og-image
# ─────────────────────────────────────────────────────────────────────────────
def make_placeholder_images():
    # hero-poster.jpg
    img = Image.new("RGB", (1920, 1080), PURPLE_DARK)
    draw = ImageDraw.Draw(img)
    # Gradiente simulado
    for y in range(0, 1080, 2):
        t = y / 1080
        r = int(PURPLE_DARK[0] + (PURPLE_MID[0] - PURPLE_DARK[0]) * t)
        g = int(PURPLE_DARK[1] + (PURPLE_MID[1] - PURPLE_DARK[1]) * t)
        b = int(PURPLE_DARK[2] + (PURPLE_MID[2] - PURPLE_DARK[2]) * t)
        draw.rectangle([0, y, 1920, y+2], fill=(r, g, b))
    # Texto centrado
    try:
        fnt = ImageFont.truetype("arial.ttf", 80)
        fnt_small = ImageFont.truetype("arial.ttf", 30)
    except Exception:
        fnt = fnt_small = ImageFont.load_default()
    draw.text((960, 480), "GREEN DOME", fill=GREEN_BRIGHT, font=fnt, anchor="mm")
    draw.text((960, 580), "Asociación Cannábica · Sevilla", fill=(200, 200, 190), font=fnt_small, anchor="mm")
    img.save(os.path.join(OUTPUT_DIR, "hero-poster.jpg"), quality=85)
    print(f"[OK]  {os.path.join(OUTPUT_DIR, 'hero-poster.jpg')}")

    # og-image.jpg (1200×630)
    img2 = Image.new("RGB", (1200, 630), PURPLE_MID)
    draw2 = ImageDraw.Draw(img2)
    for y in range(0, 630, 2):
        t = y / 630
        r = int(PURPLE_DARK[0] + (PURPLE_MID[0]-PURPLE_DARK[0])*t)
        g = int(PURPLE_DARK[1] + (PURPLE_MID[1]-PURPLE_DARK[1])*t)
        b = int(PURPLE_DARK[2] + (PURPLE_MID[2]-PURPLE_DARK[2])*t)
        draw2.rectangle([0, y, 1200, y+2], fill=(r, g, b))
    try:
        fnt2 = ImageFont.truetype("arial.ttf", 72)
        fnt2s = ImageFont.truetype("arial.ttf", 28)
    except Exception:
        fnt2 = fnt2s = ImageFont.load_default()
    draw2.text((600, 270), "GREEN DOME", fill=GREEN_BRIGHT, font=fnt2, anchor="mm")
    draw2.text((600, 370), "Cultura · Comunidad · Sevilla", fill=(200, 200, 190), font=fnt2s, anchor="mm")
    img2.save(os.path.join(OUTPUT_DIR, "og-image.jpg"), quality=85)
    print(f"[OK]  {os.path.join(OUTPUT_DIR, 'og-image.jpg')}")

    # mascot-placeholder.png (500×600 con fondo púrpura)
    img3 = Image.new("RGBA", (500, 600), (*PURPLE_MID, 255))
    draw3 = ImageDraw.Draw(img3)
    draw_mascot(draw3, 250, 300, scale=1.8)
    img3.save(os.path.join(OUTPUT_DIR, "mascot-main.png"))
    print(f"[OK]  {os.path.join(OUTPUT_DIR, 'mascot-main.png')}")


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n[GD] Green Dome — Generando assets...\n")
    make_gif_mascot()
    make_gif_logo_pulse()
    make_gif_particles()
    make_placeholder_images()
    print("\n[OK]  Todos los assets generados en static/img/\n")
    print("[DIR]  Archivos creados:")
    print("    - static/img/mascot-bounce.gif  → mascota flotante")
    print("    - static/img/logo-pulse.gif     → logo animado")
    print("    - static/img/hero-particles.gif → partículas hero")
    print("    - static/img/hero-poster.jpg    → poster del hero")
    print("    - static/img/og-image.jpg       → imagen Open Graph")
    print("    - static/img/mascot-main.png    → mascota generada")
    print("\n[TIP]  Para mejores resultados, reemplaza los PNG/JPG con tus")
    print("    imágenes reales manteniendo los mismos nombres de archivo.")
    print("\n[PIN]  Rutas donde guardar tus imágenes:")
    print("    Tu personaje principal  → static/img/mascot-main.png")
    print("    Logo con fondo          → static/img/logo-full.png")
    print("    Foto hero de fondo      → static/img/hero-poster.jpg")
