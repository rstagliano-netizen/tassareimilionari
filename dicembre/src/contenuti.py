# Contenuti delle grafiche dal 23 novembre al 23 dicembre 2026. Tutti i dati vengono da «Tassare i milionari».
# **testo** = evidenziato in oro.

GRAFICHE = [
    # ───────── LUN 23 NOV · LAPIDARIO ─────────
    {"nome": "d01_lap_fumo", "tipo": "sanders", "size": 66,
     "testo": ["«Pensavamo che il fumo facesse bene. Poi abbiamo scoperto che uccide. Lo stesso sta accadendo con la ricchezza estrema».",
               "Mark Bou Mansour, Tax Justice Network.",
               "Ci avevano promesso che, se i ricchi diventano più ricchi, prima o poi conviene a tutti. Stiamo ancora aspettando lo sgocciolamento."]},

    # ───────── LUN 30 NOV · LAPIDARIO ─────────
    {"nome": "d02_lap_bezos", "tipo": "sanders", "size": 78,
     "testo": ["Nel 2011 Jeff Bezos, già uno degli uomini più ricchi del pianeta, ha pagato zero dollari di tasse sul reddito.",
               "Zero.",
               "Tu, quell'anno, quasi certamente di più."]},

    # ───────── GIO 3 DIC · POST ─────────
    {"nome": "d03_post_mamdani", "tipo": "post", "bg": "#0f4a4a", "slide": [
        {"tipo": "testo", "label": "New York, novembre 2025", "size": 116,
         "titolo": "Ha promesso\ndi **tassare**\ni milionari.\nHa vinto.",
         "testo": ["Zohran Mamdani ha fatto campagna per una New York «abbordabile» per i comuni mortali, da pagare alzando le tasse a milionari e miliardari.",
                   "Lo chiamavano radicale. È diventato sindaco. Da noi, intanto, si discute ancora se se ne possa **parlare**."]},
    ]},

    # ───────── VEN 4 DIC · LAPIDARIO ─────────
    {"nome": "d04_lap_lakoff", "tipo": "sanders", "size": 70,
     "testo": ["Le tasse non sono un peso.",
               "Sono la quota d'iscrizione per vivere in un Paese civile.",
               "Chi le paga è un patriota. Chi le evade, e manda in rovina il suo Paese, un traditore.",
               "(Copyright: George Lakoff, linguista. Mica Lenin.)"]},

    # ───────── LUN 7 DIC · LAPIDARIO ─────────
    {"nome": "d05_lap_thiel", "tipo": "sanders", "size": 72,
     "testo": ["Negli Stati Uniti esiste un conto pensionistico esentasse pensato per i risparmi della gente comune.",
               "Il miliardario Peter Thiel ci ha fatto crescere dentro la sua fortuna per oltre vent'anni. Tasse pagate: zero.",
               "Anche lui, in fondo, pensa alla pensione."]},

    # ───────── MAR 8 DIC · CAROSELLO EREDITÀ ─────────
    {"nome": "d06_car_eredita", "tipo": "carosello", "bg": "#3a1f5c", "slide": [
        {"tipo": "cover", "label": "Eredità all'italiana", "n": "1/6", "scorri": True, "size": 150,
         "titolo": "Ereditare\n**senza pagare**:\nistruzioni\nper l'uso",
         "sub": "Quattro scappatoie, tutte perfettamente legali. La terza è piaciuta molto a una famiglia di Arcore."},
        {"tipo": "barre", "label": "Scappatoia n. 1 · esenti coniuge e figli fino a", "n": "2/6", "scorri": True, "size": 96,
         "titolo": "Il primo\n**milione** è gratis",
         "barre": [("Spagna", 16, False, "16 mila €"), ("Francia", 160, False, "160 mila €"),
                   ("Germania", 400, False, "400 mila €"), ("Stati Uniti", 507, False, "507 mila $"),
                   ("Italia", 1000, True, "1 milione €")]},
        {"tipo": "testo", "label": "Scappatoia n. 2 · il catasto", "n": "3/6", "scorri": True, "size": 120,
         "titolo": "Il castello\nche vale **zero**",
         "punti": ["Lasci ai tuoi due figli una casa che sul mercato vale 3 milioni.",
                   "Per il catasto, con estimi preistorici, ne vale circa 1. Diviso due: 500 mila a testa.",
                   "Sotto la soglia. Per lo Stato: **zero euro**."]},
        {"tipo": "testo", "label": "Scappatoia n. 3 · l'azienda", "n": "4/6", "scorri": True, "size": 120,
         "titolo": "423 milioni,\ntasse **zero**",
         "punti": ["Le quote d'azienda passate ai familiari sono esenti.",
                   "È così che i figli di Berlusconi non hanno pagato un euro sui 423 milioni di quote Fininvest ricevuti dal padre."]},
        {"tipo": "testo", "label": "Scappatoia n. 4 · il regalo in vita", "n": "5/6", "scorri": True, "size": 116,
         "titolo": "999 mila\n+ 500 mila\n= **niente**",
         "punti": ["Tuo padre ti lascia 999 mila euro, sotto la soglia. Ma in vita te ne aveva già regalati 500 mila.",
                   "Prima si sommavano e la soglia era superata. Il governo Meloni ha abolito il cosiddetto coacervo: ora non si paga."]},
        {"tipo": "cover", "label": "Il conto", "n": "6/6", "size": 136,
         "titolo": "250 miliardi\nereditati,\n**meno di 1**\nincassato",
         "sub": "Ogni anno, tra eredità e donazioni. La Francia, su cifre simili, ne incassa 21. Salvatore Morelli (Roma Tre) propone una soglia a 360 mila euro: pagherebbero soprattutto i lasciti sopra il milione."},
    ]},

    # ───────── MER 9 DIC · LAPIDARIO ─────────
    {"nome": "d07_lap_limitarianismo", "tipo": "sanders", "size": 70,
     "testo": ["C'è chi trova estremista una patrimoniale dall'1 al 3% sopra i 5,4 milioni.",
               "Intanto filosofe come Ingrid Robeyns propongono un tetto alla ricchezza: oltre i dieci milioni, moralmente indifendibile.",
               "Al confronto, sono un moderato."]},

    # ───────── GIO 10 DIC · POST ─────────
    {"nome": "d08_post_zugo", "tipo": "post", "bg": "#5b3a0c", "slide": [
        {"tipo": "duo", "label": "Svizzera, reddito da 500 mila franchi", "size": 108,
         "titolo": "Stessa Svizzera,\naltro **conto**",
         "duo": [("Zurigo", "31%", "di aliquota", False), ("Zugo", "18%", "di aliquota", True)],
         "testo": ["Pochi chilometri, regole cantonali diverse (calcoli di Enrico Rubolino, Università di Losanna). A Zugo aveva la residenza fiscale anche Sergio **Marchionne**.",
                   "Quando ognuno decide da solo, vince chi chiede meno. Per questo una tassa minima sui super ricchi va decisa insieme."]},
    ]},

    # ───────── VEN 11 DIC · LAPIDARIO ─────────
    {"nome": "d09_lap_trump", "tipo": "sanders", "size": 76,
     "testo": ["Donald Trump ha ricevuto dal padre circa mezzo miliardo di dollari.",
               "Entro il 2015 l'aveva sostanzialmente dilapidato.",
               "Ricordatevelo, la prossima volta che vi parlano del self-made man."]},

    # ───────── LUN 14 DIC · LAPIDARIO ─────────
    {"nome": "d10_lap_palazzo_chigi", "tipo": "sanders", "size": 64,
     "testo": ["I funzionari di Palazzo Chigi guadagnano già circa il doppio di un dipendente ministeriale medio.",
               "Avranno 168 euro in più al mese.",
               "Intanto un dipendente privato su quattro guadagna meno di quanto dava, al massimo, il reddito di cittadinanza.",
               "Priorità."]},

    # ───────── MAR 15 DIC · CAROSELLO QUIZ ─────────
    {"nome": "d11_quiz_chi_lha_detto_2", "tipo": "carosello", "bg": "#164a3a", "slide": [
        {"tipo": "cover", "label": "Quiz", "n": "1/6", "scorri": True, "size": 210,
         "titolo": "Chi l'ha\ndetto?\n**Parte 2**",
         "sub": "Due frasi sulle tasse. Rispondi prima di scorrere: niente Google."},
        {"tipo": "domanda", "label": "Domanda 1 · una citazione", "n": "2/6", "scorri": True, "size": 58,
         "domanda": "«Affinché i contribuenti siano onesti, fa d'uopo anzitutto sia onesto lo Stato»",
         "opzioni": [("A", "Beppe Grillo"), ("B", "Silvio Berlusconi"), ("C", "Luigi Einaudi")]},
        {"tipo": "risposta", "label": "Risposta 1", "n": "3/6", "scorri": True, "size": 140,
         "titolo": "**C.** Luigi\nEinaudi",
         "testo": ["Economista liberale, presidente della Repubblica dal 1948 al 1955.",
                   "L'ha scritto in un saggio intitolato, pensa un po', **L'imposta patrimoniale**. Altro che bolscevico."]},
        {"tipo": "domanda", "label": "Domanda 2 · un post", "n": "4/6", "scorri": True, "size": 58,
         "domanda": "«Alla fine finiscono i soldi degli altri, e allora vengono a prendere te»",
         "opzioni": [("A", "Margaret Thatcher"), ("B", "Elon Musk"), ("C", "Ronald Reagan")]},
        {"tipo": "risposta", "label": "Risposta 2", "n": "5/6", "scorri": True, "size": 140,
         "titolo": "**B.** Elon\nMusk",
         "testo": ["Ottobre 2021, su quello che allora si chiamava Twitter, mentre a Washington si discuteva di tassare i miliardari. Riecheggiava Thatcher, che però parlava del socialismo.",
                   "Tre anni prima aveva pagato poco più di **8.000 dollari** di tasse sul reddito. Paura comprensibile."]},
        {"tipo": "cover", "label": "Quante ne hai indovinate?", "n": "6/6", "size": 150,
         "titolo": "Einaudi la\nstudiava.\nMusk ne ha\n**paura**.",
         "sub": "Basterebbe questo per capire da che parte stare. Scrivi il tuo punteggio nei commenti: 0, 1 o 2."},
    ]},

    # ───────── MER 16 DIC · LAPIDARIO ─────────
    {"nome": "d12_lap_shafir", "tipo": "sanders", "size": 70,
     "testo": ["Si dice che i poveri votino contro il proprio interesse.",
               "Anche i ricchi, osserva lo psicologo Eldar Shafir: pagando un po' più di tasse vivrebbero in città più sicure e più pulite.",
               "Pensateci, la prossima volta che chiudete il cancello della villa."]},

    # ───────── GIO 17 DIC · POST ─────────
    {"nome": "d13_post_under16", "tipo": "post", "bg": "#1d4a2a", "slide": [
        {"tipo": "duo", "label": "Istat, 2024", "size": 112,
         "titolo": "Un ragazzo\nsu **quattro**",
         "duo": [("Italia", "27%", "degli under 16 a rischio povertà o esclusione sociale", True),
                 ("Sud e isole", "×2", "la quota quasi raddoppia", False)],
         "testo": ["Sono quelli a cui fra dieci anni chiederemo di restare, lavorare e pagare le pensioni.",
                   "Con 13 miliardi l'anno dallo 0,1% più ricco si fanno asili, tempo pieno, mense, borse di studio. **Basta volerlo.**"]},
    ]},

    # ───────── VEN 18 DIC · LAPIDARIO ─────────
    {"nome": "d14_lap_ottanta", "tipo": "sanders", "size": 72,
     "testo": ["Lavoratori dipendenti e pensionati versano oltre l'80% dell'Irpef.",
               "Sono loro a tenere in piedi ospedali, scuole e treni.",
               "Chiedere qualcosa a chi ha più di 5,4 milioni non è un esproprio. È dare il cambio a chi tira la carretta da quarant'anni."]},

    # ───────── LUN 21 DIC · LAPIDARIO ─────────
    {"nome": "d15_lap_sperate", "tipo": "sanders", "size": 76,
     "testo": ["Molti si oppongono alla patrimoniale perché sperano, un giorno, di diventare milionari.",
               "Tranquilli: scatterebbe sopra i 5,4 milioni di patrimonio.",
               "Se ci arrivate, il caffè lo offrite voi."]},

    # ───────── MAR 22 DIC · CAROSELLO MONOPOLY ─────────
    {"nome": "d16_car_monopoly", "tipo": "carosello", "bg": "#6b1d1d", "slide": [
        {"tipo": "cover", "label": "Natale, giochi da tavola", "n": "1/6", "scorri": True, "size": 136,
         "titolo": "L'unico posto\nin Italia con la\n**patrimoniale**?\nIl Monopoly",
         "sub": "Breve storia di una parola che da trent'anni fa paura. Soprattutto a chi non la pagherebbe mai."},
        {"tipo": "testo", "label": "Dicembre 1998", "n": "2/6", "scorri": True, "size": 120,
         "titolo": "Fausto,\nSilvio e\n**Massimo**",
         "testo": ["Prima serata di Rai1, spot del Monopoly. Tre bambini giocano facendo il verso a Bertinotti, Berlusconi e D'Alema.",
                   "«Consentimi Fausto, cosa dovrei dire io che devo pagare la tassa patrimoniale?». «Silvio, tutti paghiamo le tasse, sennò si finisce qui». E indica la casella **In prigione**."]},
        {"tipo": "testo", "label": "2006", "n": "3/6", "scorri": True, "size": 116,
         "titolo": "«Anche\ni ricchi\n**piangano**»",
         "testo": ["La Rifondazione di Bertinotti, nella maggioranza di Prodi, chiede di più ai ricchi con un manifesto: uno yacht.",
                   "D'Alema, che di yacht ne ha uno da 22 metri: «Uno dei manifesti più cretini che abbia mai visto». Berlusconi: «Vi porteranno via il 50% del patrimonio». Poco dopo il governo va in pezzi."]},
        {"tipo": "testo", "label": "Estate 2011", "n": "4/6", "scorri": True, "size": 116,
         "titolo": "Favorevoli\nperfino\n**Briatore**",
         "testo": ["Spread alle stelle, lettera della Bce. Per un attimo la patrimoniale la vogliono quasi tutti: Amato, Veltroni, Fini, Casini, Calderoli, Confalonieri. E Flavio Briatore.",
                   "Poi arriva Monti e non se ne fa niente, per paura di una fuga di capitali."]},
        {"tipo": "testo", "label": "Agosto 2023", "n": "5/6", "scorri": True, "size": 120,
         "titolo": "Approvata.\nPer **errore**",
         "testo": ["Un ordine del giorno di Fratoianni chiede una patrimoniale sui redditi oltre i 500 mila euro, per combattere la dispersione scolastica.",
                   "Il rappresentante del governo Meloni lo sottoscrive. Per sbaglio. Passa alla Camera e finisce lì."]},
        {"tipo": "cover", "label": "Fine partita?", "n": "6/6", "size": 150,
         "titolo": "Trent'anni\nsulla casella\n**sbagliata**",
         "sub": "Una patrimoniale dall'1 al 3% sullo 0,1% più ricco porterebbe circa 13 miliardi l'anno. Quest'anno, sotto l'albero, un gioco nuovo: farla davvero."},
    ]},

    # ───────── MER 23 DIC · LAPIDARIO ─────────
    {"nome": "d17_lap_babbo_natale", "tipo": "sanders", "size": 76,
     "testo": ["Caro Babbo Natale,",
               "quest'anno vorrei una cosa sola: che lo 0,1% più ricco pagasse le tasse almeno come un infermiere.",
               "Non chiedo regali. Chiedo che smettano di farli a loro."]},
]
