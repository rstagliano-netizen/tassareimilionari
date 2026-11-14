"""Genera i lapidari 'stile Sanders' con foto di sfondo (1080x1350)."""
import html, sys
from pathlib import Path
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright

D = Path(__file__).parent
U = "/mnt/user-data/uploads/"
ITEMS = [
    ("f10_zucman", U + "eec78219-image.jpg", (0.6,0.7,"top"), [
        "I circa 3.000 miliardari del pianeta pagano in tasse lo 0,3% della loro ricchezza.",
        "La proposta di Gabriel Zucman: almeno il 2%.",
        "Ecco, questo sarebbe l'estremismo."]),
    ("f11_panda", U + "139b5018-image.jpg", (0.55,0.5,"bottom"), [
        "Nel 2010 a un prof servivano 5,4 stipendi per comprare una Panda. Oggi quasi 9.",
        "Nel frattempo la Panda non è diventata una Ferrari.",
        "È lo stipendio che è diventato una Panda."]),
    ("f12_segreto_bancario", U + "1b22741f-image.jpg", (0.5,0.3,"bottom"), [
        "Vent'anni fa il segreto bancario svizzero sembrava eterno.",
        "È caduto nel 2015.",
        "Oggi una patrimoniale sui multimilionari sembra impossibile. Finché non lo è più."]),
    ("f13_rendite_ufficio", U + "9c9e4710-image.jpg", (0.5,0.5,"center"), [
        "Chi vive di dividendi paga il 26%. Chi vive di affitti, il 21%.",
        "Chi alle sette di sera è ancora in ufficio, fino al 43%.",
        "Poi dicono che il merito va premiato."]),
    ("f14_vienna", U + "d9bed6ba-image.jpg", (0.42,0.5,"top"), [
        "A Vienna le case popolari sono il 40%. In Italia meno del 5.",
        "Questa è la Karl-Marx-Hof: costruita nel 1930, abitata ancora oggi.",
        "Noi intanto discutiamo di bonus."]),
]

CSS = """
html,body{margin:0;padding:0}
.frame{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif}
.bg{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}
.card{position:absolute;left:84px;right:84px;box-sizing:border-box;
 background:#fff;border-radius:36px;padding:48px 52px 40px;box-shadow:0 12px 44px rgba(0,0,0,.22)}
.head{display:flex;align-items:center;gap:24px;margin-bottom:34px}
.avatar{width:104px;height:104px;border-radius:50%;object-fit:cover;flex:none}
.name{font-weight:700;font-size:35px;color:#0f1419;line-height:1.15}
.handle{font-size:28px;color:#536471;line-height:1.25}
.body p{margin:0 0 30px;font-size:40px;line-height:1.32;color:#0f1419;letter-spacing:-0.2px}
.foot{display:flex;justify-content:space-between;margin-top:36px;font-size:22px;color:#8b98a5}
.credit{position:absolute;left:20px;bottom:16px;color:#fff;font-size:20px;opacity:.9;text-shadow:0 1px 4px rgba(0,0,0,.7)}
"""

def prep_bg(src, name, focus_x, focus_y):
    im = Image.open(src).convert("RGB")
    W, H = 1080, 1350
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = round((im.width - W) * focus_x); y = round((im.height - H) * focus_y)
    im = im.crop((x, y, x + W, y + H))
    if s > 1.6:  # foto piccola: ammorbidisco l'upscale perché non sembri sgranata
        im = im.filter(ImageFilter.GaussianBlur(1.2))
    out = D / f"bg_{name}.jpg"; im.save(out, quality=92)
    return out.name

def page(name, bg, paras, pos, credit=""):
    style = {"center":"top:50%;transform:translateY(-50%)","top":"top:96px","bottom":"bottom:96px"}[pos]
    ps = "".join(f'<p style="color:#0f1419">{html.escape(t)}</p>' for t in paras)
    cr = f'<div class="credit">{html.escape(credit)}</div>' if credit else ""
    return f"""<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="frame" style="width:1080px;height:1350px"><img class="bg" src="{bg}">
<div class="card" style="background:#ffffff;{style}"><div class="head"><img class="avatar" src="avatar.png">
<div><div class="name" style="color:#0f1419">Riccardo Staglianò</div><div class="handle" style="color:#536471">@rstagliano</div></div></div>
<div class="body">{ps}</div>
<div class="foot" style="color:#8b98a5"><span>Tassare i milionari · Einaudi</span><span>@einaudieditore</span></div></div>
{cr}</div></body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    for name, src, (fx, fy, pos), paras in ITEMS:
        bg = prep_bg(src, name, fx, fy)
        f = D / f"{name}.html"; f.write_text(page(name, bg, paras, pos), encoding="utf-8")
        pg.goto(f.as_uri()); pg.wait_for_timeout(300)
        pg.screenshot(path=str(D / f"{name}.png"))
        print("ok", name)
    b.close()
