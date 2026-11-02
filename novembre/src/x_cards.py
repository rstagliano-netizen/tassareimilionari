"""Card in stile tweet (fondo bianco) per i post Typefully: X, Threads, Bluesky, Note Substack.

Uso: python3 x_cards.py  -> scrive novembre/x/<nome>.png
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
from render import render_sanders

OUT = Path(__file__).resolve().parent.parent / "x"

CARDS = [
    ("x02_norvegia_lugano", 68, [
        "L'ex uomo più ricco della Norvegia, 5,5 miliardi di dollari, è andato in esilio a Lugano. Come Mazzini.",
        "Il tiranno da cui fuggiva: una patrimoniale dell'1,1%.",
        "Ricchi norvegesi che emigrano: sotto il 3%. Come tutti gli altri."]),
    ("x03_travaso_sole24ore", 72, [
        "«Quel travaso pazzesco di ricchezza dal lavoro al capitale».",
        "Lotta Comunista? No, Il Sole 24\u00a0Ore.",
        "2020-2023: la quota di valore aggiunto andata al lavoro −12\u00a0punti. Quella andata agli utili +14."]),
    ("x04_irpef_1974", 70, [
        "1974: l'Irpef ha 32 scaglioni e l'aliquota massima al 72%.",
        "Oggi: 4 scaglioni, e ci si ferma al 43%.",
        "Così un impiegato paga la stessa aliquota marginale di un milionario.",
        "La chiamano semplificazione."]),
    ("x05_esodo_uk", 74, [
        "Esodo dei milionari dal Regno Unito?",
        "11 mila articoli con una sola fonte. Un'azienda che vende passaporti d'oro.",
        "Esodo reale: vicino allo zero."]),
    ("x06_crisi_2008", 70, [
        "Dopo il crollo del 1929 la ricchezza dello 0,1% più ricco crollò. Dopo quello del 2008, no.",
        "Finiti in carcere per la crisi: 55. Quasi tutti in Islanda.",
        "Negli Usa, dove era scoppiata: zero."]),
    ("x07_svizzera_chaplin", 66, [
        "Paese con una patrimoniale dal X secolo: la Svizzera. Sì, quella delle banche.",
        "Però nel 1953, quando arrivò Charlie Chaplin, gli confezionarono una legge su misura per pagare un forfait: la Lex Chaplin.",
        "Tempi moderni."]),
]

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    (OUT / "html").mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for nome, size, testo in CARDS:
            hp = OUT / "html" / f"{nome}.html"
            hp.write_text(render_sanders({"testo": testo, "size": size, "handle": "@rsta"}), encoding="utf-8")
            pg.goto(hp.as_uri()); pg.wait_for_selector("body[data-ready='1']"); pg.wait_for_timeout(150)
            pg.screenshot(path=str(OUT / f"{nome}.png"), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            print(nome)
        b.close()
