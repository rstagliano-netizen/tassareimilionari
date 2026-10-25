"""Genera le grafiche di novembre (1080x1350) da contenuti.py con Playwright.

Uso: python3 render.py [prefisso]   -> rende solo le grafiche il cui nome inizia col prefisso
"""
import re
import sys
import html
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))
from contenuti import GRAFICHE  # noqa: E402

FONTS = Path("/tmp/claude-0/-home-claude/7482c459-19c8-502e-9f2e-d77429f3e3b2/scratchpad/fonts")
OUT = Path(__file__).resolve().parent.parent
GOLD = "#f0b429"
FOOTER = "Tassare i milionari · Einaudi · @rstagliano · @einaudieditore"


def ff(family, weight, style, path):
    return (f"@font-face{{font-family:'{family}';font-weight:{weight};font-style:{style};"
            f"src:url('file://{path}') format('woff2');}}")


FONT_CSS = "".join([
    ff("Barlow Condensed", w, "normal",
       (FONTS / "fontsource-barlow-condensed-5.3.0") / f"files/barlow-condensed-latin-{w}-normal.woff2")
    for w in (600, 700, 800)
] + [
    ff("DM Sans", w, s, (FONTS / "fontsource-dm-sans-5.3.0") / f"files/dm-sans-latin-{w}-{s}.woff2")
    for w in (400, 500, 700) for s in ("normal", "italic")
])


def md(text):
    """**oro**, \n -> <br>, escape del resto."""
    t = html.escape(text)
    t = re.sub(r"\*\*(.+?)\*\*", rf'<span style="color:{GOLD}" class="g">\1</span>', t, flags=re.S)
    return t.replace("\n", "<br>")


BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:'DM Sans',sans-serif;color:#fff;-webkit-font-smoothing:antialiased}
.frame{position:relative;width:1080px;height:1350px;padding:84px 84px 0 104px;display:flex;flex-direction:column}
.stripe{position:absolute;left:0;top:0;bottom:0;width:16px}
.label{font-family:'Barlow Condensed';font-weight:700;font-size:30px;letter-spacing:4px;text-transform:uppercase}
.counter{position:absolute;right:84px;top:84px;font-family:'Barlow Condensed';font-weight:600;font-size:30px;letter-spacing:2px;color:rgba(255,255,255,.75)}
.title{font-family:'Barlow Condensed';font-weight:800;text-transform:uppercase;line-height:.93;letter-spacing:-.5px}
.content{flex:1;display:flex;flex-direction:column;justify-content:center;padding:30px 0 150px}
.content.cover{justify-content:space-between;padding-top:56px}
.body{font-size:42px;line-height:1.38;color:rgba(255,255,255,.92)}
.body p+p{margin-top:24px}
.sub{font-size:46px;line-height:1.36;color:rgba(255,255,255,.9);margin-top:44px}
.bul{list-style:none;margin-top:36px}
.bul li{font-size:41px;line-height:1.35;padding-left:56px;position:relative;margin-bottom:22px;color:rgba(255,255,255,.92)}
.bul li:before{content:'—';position:absolute;left:0;font-weight:700}
.big{font-family:'Barlow Condensed';font-weight:800;line-height:.9;margin-top:46px}
.big small{font-size:.38em;margin-left:14px;letter-spacing:1px}
.foot{position:absolute;left:104px;right:84px;bottom:46px;font-size:22px;color:rgba(255,255,255,.62);display:flex;justify-content:space-between;align-items:center}
.next{font-family:'Barlow Condensed';font-weight:700;font-size:32px;letter-spacing:3px}
.opt{display:flex;align-items:center;border:3px solid rgba(255,255,255,.35);border-radius:16px;padding:34px 36px;margin-top:26px;font-size:46px;font-weight:500}
.opt b{font-family:'Barlow Condensed';font-weight:800;font-size:54px;width:72px}
.quote{font-family:'DM Sans';font-weight:700;font-style:italic;line-height:1.2;margin-bottom:30px}
.cta{margin-top:56px;font-size:38px;font-weight:500}
.bars{margin-top:50px}
.bar{margin-bottom:34px}
.bar .lab{display:flex;justify-content:space-between;align-items:baseline;font-size:40px;margin-bottom:12px}
.bar .lab span:last-child{font-family:'Barlow Condensed';font-weight:800;font-size:64px}
.bar .track{position:relative;height:40px;background:rgba(255,255,255,.12);border-radius:4px;overflow:hidden}
.bar .zero{position:absolute;top:-6px;bottom:-6px;width:4px;background:#fff}
.bar .fill{position:absolute;top:0;height:100%;border-radius:3px}
.duo{display:flex;gap:28px;margin-top:56px}
.duo>div{flex:1;border-radius:18px;padding:40px 34px;background:rgba(255,255,255,.08)}
.duo .k{font-family:'Barlow Condensed';font-weight:700;font-size:34px;letter-spacing:3px;text-transform:uppercase}
.duo .v{font-family:'Barlow Condensed';font-weight:800;font-size:130px;line-height:1;margin-top:18px}
.duo .d{font-size:32px;line-height:1.3;margin-top:14px;color:rgba(255,255,255,.88)}
"""

FIT_JS = """
document.fonts.ready.then(()=>{document.querySelectorAll('[data-fit]').forEach(el=>{
  const max=parseFloat(el.dataset.fit);let s=parseFloat(getComputedStyle(el).fontSize);
  while(el.scrollHeight>max && s>20){s-=2;el.style.fontSize=s+'px';}
});document.body.dataset.ready='1';});
"""


def page(bg, inner, counter=None, nxt=False, label=None, accent=GOLD, kind=""):
    lab = (f'<div class="label" style="color:{accent}">{md(label)}</div>' if label else "")
    cnt = f'<div class="counter">{counter}</div>' if counter else ""
    arrow = f'<span class="next" style="color:{accent}">SCORRI →</span>' if nxt else "<span></span>"
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}{BASE_CSS}</style></head>
<body style="background:{bg}"><div class="frame" style="background:{bg}">
<div class="stripe" style="background:{accent}"></div>{cnt}{lab}<div class="content {kind}">{inner}</div>
<div class="foot"><span>{FOOTER}</span>{arrow}</div></div>
<script>{FIT_JS}</script></body></html>"""


def render_slide(s, bg):
    t = s["tipo"]
    counter, nxt, label = s.get("n"), s.get("scorri", False), s.get("label")
    if t == "cover":
        inner = (f'<div class="title" data-fit="720" style="font-size:{s.get("size",170)}px">{md(s["titolo"])}</div>'
                 + (f'<div class="sub">{md(s["sub"])}</div>' if s.get("sub") else ""))
    elif t == "testo":
        inner = f'<div class="title" data-fit="420" style="font-size:{s.get("size",120)}px">{md(s["titolo"])}</div>'
        if s.get("big"):
            main_, _, small_ = s["big"].partition("|")
            inner += (f'<div class="big" style="font-size:{s.get("bigsize",250)}px;color:{GOLD}">{md(main_)}'
                      + (f'<small>{md(small_)}</small>' if small_ else "") + '</div>')
        if s.get("punti"):
            inner += '<ul class="bul" data-fit="640">' + "".join(
                f'<li><span style="position:absolute;left:0;color:{GOLD}">—</span>{md(p)}</li>' for p in s["punti"]) + "</ul>"
        if s.get("testo"):
            inner += '<div class="body" data-fit="620" style="margin-top:44px">' + "".join(
                f"<p>{md(p)}</p>" for p in s["testo"]) + "</div>"
    elif t == "domanda":
        inner = f'<div class="quote" data-fit="470" style="font-size:{s.get("size",66)}px">{md(s["domanda"])}</div>'
        inner += "".join(f'<div class="opt"><b style="color:{GOLD}">{k}</b>{md(v)}</div>' for k, v in s["opzioni"])
        inner += f'<div class="cta" style="color:{GOLD}">{md(s.get("cta","Scrivi la tua risposta nei commenti, poi scorri."))}</div>'
    elif t == "risposta":
        inner = (f'<div class="title" data-fit="360" style="font-size:{s.get("size",150)}px">{md(s["titolo"])}</div>'
                 f'<div class="body" data-fit="660" style="margin-top:48px">' + "".join(f"<p>{md(p)}</p>" for p in s["testo"]) + "</div>")
    elif t == "barre":
        lo = min(0, min(b[1] for b in s["barre"])); hi = max(b[1] for b in s["barre"]); rng = hi - lo; z = -lo / rng * 100
        inner = f'<div class="title" data-fit="330" style="font-size:{s.get("size",100)}px">{md(s["titolo"])}</div><div class="bars">'
        for lab_, v, col, disp in s["barre"]:
            c = GOLD if col else "rgba(255,255,255,.55)"
            inner += (f'<div class="bar"><div class="lab"><span>{md(lab_)}</span><span style="color:{c}">{disp}</span></div>'
                      f'<div class="track"><div class="fill" style="left:{z + min(v,0)/rng*100:.1f}%;width:{abs(v)/rng*100:.1f}%;background:{c}"></div>'
                      + (f'<div class="zero" style="left:calc({z:.1f}% - 2px)"></div>' if lo < 0 else "") + '</div></div>')
        inner += "</div>"
        if s.get("testo"):
            inner += '<div class="body" style="margin-top:30px;font-size:38px">' + "".join(f"<p>{md(p)}</p>" for p in s["testo"]) + "</div>"
    elif t == "duo":
        inner = f'<div class="title" data-fit="360" style="font-size:{s.get("size",104)}px">{md(s["titolo"])}</div><div class="duo">'
        for k, v, d, gold in s["duo"]:
            col = GOLD if gold else "#fff"
            inner += f'<div><div class="k" style="color:{col}">{md(k)}</div><div class="v" style="color:{col}">{md(v)}</div><div class="d">{md(d)}</div></div>'
        inner += "</div>"
        if s.get("testo"):
            inner += '<div class="body" style="margin-top:48px">' + "".join(f"<p>{md(p)}</p>" for p in s["testo"]) + "</div>"
    else:
        raise ValueError(t)
    return page(bg, inner, counter, nxt, label, kind="cover" if t == "cover" else "")


SANDERS_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;background:#fff}
body{font-family:'DM Sans',sans-serif;color:#0f1419;-webkit-font-smoothing:antialiased}
.wrap{width:1080px;height:1350px;padding:0 96px;display:flex;flex-direction:column;justify-content:center}
.head{display:flex;align-items:center;gap:30px;margin-bottom:54px}
.av{width:132px;height:132px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Barlow Condensed';font-weight:800;font-size:60px;letter-spacing:1px}
.name{font-weight:700;font-size:46px;line-height:1.1}
.handle{font-size:38px;color:#536471;margin-top:6px}
.txt{font-weight:500;line-height:1.28;letter-spacing:-.3px}
.txt p+p{margin-top:.62em}
.meta{margin-top:54px;padding-top:30px;border-top:2px solid #eff3f4;font-size:30px;color:#536471;display:flex;justify-content:space-between}
"""


def render_sanders(s):
    paras = "".join(f"<p>{html.escape(p)}</p>" for p in s["testo"])
    av_bg, av_fg = s.get("avatar", ("#0e2a47", GOLD))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}{SANDERS_CSS}</style></head>
<body><div class="wrap">
<div class="head"><div class="av" style="background:{av_bg};color:{av_fg}">RS</div>
<div><div class="name">Riccardo Staglianò</div><div class="handle">@rstagliano</div></div></div>
<div class="txt" data-fit="760" style="font-size:{s.get("size",64)}px">{paras}</div>
<div class="meta"><span>Tassare i milionari · Einaudi</span><span>@einaudieditore</span></div>
</div><script>{FIT_JS}</script></body></html>"""


def main():
    pref = sys.argv[1] if len(sys.argv) > 1 else ""
    built = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for g in GRAFICHE:
            if not g["nome"].startswith(pref):
                continue
            slides = g.get("slide") or [g]
            for i, s in enumerate(slides, 1):
                doc = render_sanders(s) if g["tipo"] == "sanders" else render_slide(s, g["bg"])
                name = g["nome"] if len(slides) == 1 else f'{g["nome"]}_{i}'
                (OUT / "src" / "html").mkdir(parents=True, exist_ok=True)
                hp = OUT / "src" / "html" / f"{name}.html"
                hp.write_text(doc, encoding="utf-8")
                pg.goto(hp.as_uri())
                pg.wait_for_selector("body[data-ready='1']")
                pg.wait_for_timeout(150)
                pg.screenshot(path=str(OUT / f"{name}.png"), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
                built.append(name)
        b.close()
    print("\n".join(built))


if __name__ == "__main__":
    main()
