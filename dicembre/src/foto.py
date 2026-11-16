"""Lapidari di dicembre con foto di sfondo (card bianca stile Sanders), stesso modello di src/lapidari_foto/build.py.

Uso: python3 foto.py  -> scrive dicembre/foto/<nome>_foto.png
Le foto le fornisce Riccardo; vanno in dicembre/foto/src/.
"""
import html
import sys
from pathlib import Path
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))
from contenuti import GRAFICHE  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "dicembre" / "foto" / "src"
OUT = ROOT / "dicembre" / "foto"
AVATAR = ROOT / "src" / "lapidari_foto" / "avatar.png"
TESTI = {g["nome"]: g["testo"] for g in GRAFICHE if g["tipo"] == "sanders"}

# nome grafica, file foto, fuoco x, fuoco y, posizione card, spostamento in su della foto (px), corpo testo, credito
ITEMS = [
    ("d01_lap_fumo", "sigarette.jpg", 0.5, 0.0, "bottom", 0, 36, ""),
    ("d02_lap_bezos", "bezos.jpg", 0.5, 0.0, "bottom", 0, 40, ""),
    ("d05_lap_thiel", "thiel.jpg", 0.5, 0.0, "bottom_low", 260, 32, ""),
    ("d09_lap_trump", "trump.jpg", 0.5, 0.0, "bottom", 0, 40, ""),
    ("d10_lap_palazzo_chigi", "chigi.jpg", 0.5, 0.0, "top_high", 0, 32, ""),
]

CSS = """
html,body{margin:0;padding:0}
.frame{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif}
.bg{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}
.card{position:absolute;left:84px;right:84px;box-sizing:border-box;
 background:#fff;border-radius:36px;padding:44px 52px 36px;box-shadow:0 12px 44px rgba(0,0,0,.22)}
.head{display:flex;align-items:center;gap:24px;margin-bottom:30px}
.avatar{width:104px;height:104px;border-radius:50%;object-fit:cover;flex:none}
.name{font-weight:700;font-size:35px;color:#0f1419;line-height:1.15}
.handle{font-size:28px;color:#536471;line-height:1.25}
.body p{margin:0 0 26px;line-height:1.3;color:#0f1419;letter-spacing:-0.2px}
.foot{display:flex;justify-content:space-between;margin-top:30px;font-size:22px;color:#8b98a5}
.credit{position:absolute;left:20px;bottom:16px;color:#fff;font-size:20px;opacity:.9;text-shadow:0 1px 4px rgba(0,0,0,.7)}
"""


def prep_bg(src, name, fx, fy, shift):
    im = Image.open(src).convert("RGB")
    W, H = 1080, 1350
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = round((im.width - W) * fx); y = round((im.height - H) * fy)
    im = im.crop((x, y, x + W, y + H))
    if s > 1.6:  # foto piccola: ammorbidisco l'upscale perché non sembri sgranata
        im = im.filter(ImageFilter.GaussianBlur(1.2))
    if shift:  # sposto la foto in su per lasciare il volto sopra la card; sotto, il colore dell'ultima riga
        canvas = Image.new("RGB", (W, H))
        canvas.paste(im, (0, -shift))
        fill = im.crop((60, H - 6, 160, H)).resize((1, 1)).getpixel((0, 0))  # bordo sinistro, sul vestito
        canvas.paste(Image.new("RGB", (W, shift), fill), (0, H - shift))
        im = canvas
    out = OUT / f"bg_{name}.jpg"
    im.save(out, quality=92)
    return out


def page(bg, paras, pos, size, credit):
    style = {"center": "top:50%;transform:translateY(-50%)", "top": "top:96px", "bottom": "bottom:96px", "bottom_low": "bottom:44px", "top_high": "top:48px"}[pos]
    ps = "".join(f'<p style="color:#0f1419;font-size:{size}px">{html.escape(t)}</p>' for t in paras)
    cr = f'<div class="credit">{html.escape(credit)}</div>' if credit else ""
    return f"""<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="frame" style="width:1080px;height:1350px"><img class="bg" src="{bg.as_uri()}">
<div class="card" style="background:#ffffff;{style}"><div class="head"><img class="avatar" src="{AVATAR.as_uri()}">
<div><div class="name" style="color:#0f1419">Riccardo Staglianò</div><div class="handle" style="color:#536471">@rstagliano</div></div></div>
<div class="body">{ps}</div>
<div class="foot" style="color:#8b98a5"><span>Tassare i milionari · Einaudi</span><span>@einaudieditore</span></div></div>
{cr}</div></body></html>"""


def main():
    pref = sys.argv[1] if len(sys.argv) > 1 else ""
    (OUT / "html").mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for name, foto, fx, fy, pos, shift, size, credit in ITEMS:
            if not name.startswith(pref):
                continue
            bg = prep_bg(SRC / foto, name, fx, fy, shift)
            f = OUT / "html" / f"{name}_foto.html"
            f.write_text(page(bg, TESTI[name], pos, size, credit), encoding="utf-8")
            pg.goto(f.as_uri()); pg.wait_for_timeout(300)
            pg.screenshot(path=str(OUT / f"{name}_foto.png"))
            print("ok", name)
        b.close()


if __name__ == "__main__":
    main()
