"""
Genera imágenes temporales (placeholder) para el proyecto Reef to Table.
Este script NO forma parte del sitio final: es una utilidad de un solo uso
para dejar el proyecto navegable antes de reemplazar las imágenes reales.
"""

from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = "images"
os.makedirs(OUT_DIR, exist_ok=True)

NAVY = (45, 50, 120)
NAVY_DARK = (30, 41, 90)
CREAM = (245, 245, 245)
WHITE = (255, 255, 255)


def get_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_centered(draw, text, y, font, fill, width):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((width - w) / 2, y), text, font=font, fill=fill)


def make_placeholder(filename, w, h, label, sublabel=""):
    img = Image.new("RGB", (w, h), NAVY)
    draw = ImageDraw.Draw(img)

    # Borde decorativo simple
    draw.rectangle([8, 8, w - 9, h - 9], outline=CREAM, width=2)

    # Patrón diagonal sutil
    step = 40
    for x in range(-h, w, step):
        draw.line([(x, 0), (x + h, h)], fill=NAVY_DARK, width=1)

    font_label = get_font(max(16, w // 22), bold=True)
    font_sub = get_font(max(12, w // 32))
    font_dim = get_font(max(11, w // 36))

    draw_centered(draw, label, h / 2 - 26, font_label, WHITE, w)
    if sublabel:
        draw_centered(draw, sublabel, h / 2 + 8, font_sub, CREAM, w)
    draw_centered(draw, f"{w} x {h}", h - 34, font_dim, CREAM, w)

    img.save(os.path.join(OUT_DIR, filename), quality=85)
    print(f"OK  {filename}  ({w}x{h})")


def make_logo(filename="logo.png"):
    w, h = 520, 190
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Ícono simple tipo "concha" (círculo + líneas), como referencia de reemplazo
    cx, cy, r = 85, 95, 60
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=4)
    for angle_offset in range(-2, 3):
        draw.line([(cx, cy), (cx + angle_offset * 18, cy - r + 10)], fill=NAVY, width=3)

    font_word = get_font(46, bold=True)
    draw.text((160, h / 2 - 28), "Reef to Table", font=font_word, fill=NAVY)

    img.save(os.path.join(OUT_DIR, filename))
    print(f"OK  {filename}  ({w}x{h})")


def make_favicon(filename="favicon.png"):
    w = h = 64
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([4, 4, w - 4, h - 4], fill=NAVY)
    font = get_font(30, bold=True)
    draw.text((w / 2 - 12, h / 2 - 17), "R", font=font, fill=WHITE)
    img.save(os.path.join(OUT_DIR, filename))
    print(f"OK  {filename}  ({w}x{h})")


# ---------------------------------------------------------------------
# Logo y favicon
# ---------------------------------------------------------------------
make_logo()
make_favicon()

# ---------------------------------------------------------------------
# Home (index.html)
# ---------------------------------------------------------------------
make_placeholder("hero.jpg", 900, 1100, "hero.jpg", "Imagen principal del home")
make_placeholder("oyster-closeup.jpg", 700, 500, "oyster-closeup.jpg", "Ostra en primer plano")
make_placeholder("platter.jpg", 900, 600, "platter.jpg", "Bandeja de ostras con romero")

# ---------------------------------------------------------------------
# Product (product.html)
# ---------------------------------------------------------------------
make_placeholder("product-01.jpg", 700, 900, "product-01.jpg", "Manos abriendo ostras")
make_placeholder("product-02.jpg", 700, 900, "product-02.jpg", "Ostras horneadas con toppings")
make_placeholder("product-03.jpg", 700, 900, "product-03.jpg", "Food truck / trailer de marca")

# ---------------------------------------------------------------------
# Businesses (businesses.html)
# ---------------------------------------------------------------------
make_placeholder("business-01.jpg", 700, 900, "business-01.jpg", "Manos abriendo ostras")
make_placeholder("business-02.jpg", 700, 900, "business-02.jpg", "Ostras horneadas con toppings")
make_placeholder("business-03.jpg", 700, 900, "business-03.jpg", "Food truck / trailer de marca")

# ---------------------------------------------------------------------
# Gallery (gallery.html) — 19 imágenes (12 + 7)
# ---------------------------------------------------------------------
gallery_labels = [
    "Trailer / señalética de marca",
    "Exprimiendo limón frente al trailer",
    "Ventana del food truck con personal",
    "Bandeja de ostras sobre hielo",
    "Bandeja para evento privado",
    "Ostras horneadas para evento",
    "Porciones individuales en bandeja",
    "Ostras con cerveza",
    "Proceso de shucking en estudio",
    "Ostras horneadas",
    "Manos abriendo ostras",
    "Ostras horneadas con toppings",
    "Ingredientes para ostras horneadas",
    "Tostada / flatbread con ostra",
    "Brocheta de mejillones",
    "Paella de mariscos",
    "Sándwich tipo po'boy",
    "Preparación de rollo / bowl de arroz",
    "Tostada / flatbread con ostra (2)",
]

for i, label in enumerate(gallery_labels, start=1):
    fname = f"gallery-{i:02d}.jpg"
    make_placeholder(fname, 700, 700, fname, label)

print("\nListo. Se generaron", len(gallery_labels) + 8, "imágenes en la carpeta 'images/'.")
