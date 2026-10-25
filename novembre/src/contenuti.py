# Contenuti delle grafiche di novembre. Tutti i dati vengono da «Tassare i milionari».
# **testo** = evidenziato in oro.

GRAFICHE = [
    # ───────── MAR 3 NOV · CAROSELLO QUIZ ─────────
    {"nome": "n01_quiz_chi_lha_detto", "tipo": "carosello", "bg": "#0e3b43", "slide": [
        {"tipo": "cover", "label": "Quiz", "n": "1/6", "scorri": True, "size": 230,
         "titolo": "Indovina\nchi l'ha\n**detto**",
         "sub": "Due frasi sulla ricchezza e sulle tasse ai ricchi. Rispondi prima di scorrere: niente Google."},
        {"tipo": "domanda", "label": "Domanda 1 · un titolo di giornale", "n": "2/6", "scorri": True,
         "domanda": "«Quel travaso pazzesco di ricchezza dal lavoro al capitale»",
         "opzioni": [("A", "Lotta Comunista"), ("B", "il manifesto"), ("C", "Il Sole 24 Ore")]},
        {"tipo": "risposta", "label": "Risposta 1", "n": "3/6", "scorri": True, "size": 140,
         "titolo": "**C.** Il Sole\n24 Ore",
         "testo": ["Il quotidiano di Confindustria. Firma Riccardo Gallo, professore alla Sapienza, consulente di ministri perlopiù repubblicani.",
                   "Il dato: dal 2020 al 2023 la quota di valore aggiunto che va al lavoro perde **12 punti**. Quella che va agli utili ne guadagna **14**."]},
        {"tipo": "domanda", "label": "Domanda 2 · una citazione", "n": "4/6", "scorri": True, "size": 60,
         "domanda": "«Per difendere il capitalismo dobbiamo liberarci dei ricchi oziosi tassando eredità e patrimoni»",
         "opzioni": [("A", "Karl Marx"), ("B", "Bernie Sanders"), ("C", "Winston Churchill")]},
        {"tipo": "risposta", "label": "Risposta 2", "n": "5/6", "scorri": True, "size": 140,
         "titolo": "**C.** Winston\nChurchill",
         "testo": ["Proprio lui, il sigaro più conservatore d'Europa. Temeva la concorrenza ideologica del modello sovietico e pensava che tassare i ricchi oziosi servisse a salvare il capitalismo, non ad abbatterlo.",
                   "Oggi lo dice quasi solo Bernie Sanders. E lo chiamano estremista."]},
        {"tipo": "cover", "label": "Quante ne hai indovinate?", "n": "6/6", "size": 150,
         "titolo": "Se sono\nestremisti\nil Sole 24 Ore\ne Churchill…",
         "sub": "…allora tassare dall'1 al 3% lo 0,1% più ricco è una proposta piuttosto **moderata**. Scrivi nei commenti il tuo punteggio: 0, 1 o 2."},
    ]},

    # ───────── MER 4 NOV · LAPIDARIO ─────────
    {"nome": "n02_lap_prof_tedesco", "tipo": "sanders", "size": 74,
     "testo": ["Un insegnante italiano, a fine carriera, guadagna meno di un collega tedesco al primo giorno di scuola.",
               "43 mila euro lordi l'anno contro 61 mila.",
               "Poi ci stupiamo se nessuno vuole più farlo."]},

    # ───────── GIO 5 NOV · POST ─────────
    {"nome": "n03_post_salari", "tipo": "post", "bg": "#4a1531",
     "tipo_slide": "barre", "slide": [
        {"tipo": "barre", "label": "Salari reali dal 2008", "size": 104,
         "titolo": "Noi **indietro**,\ngli altri avanti",
         "barre": [("Germania", 14, False, "+14%"), ("Francia", 5, False, "+5%"), ("Italia", -9, True, "−9%")],
         "testo": ["Germania **+14%**, Francia **+5%**, Italia **−9%** circa (fonte: Ilo). Le nostre buste paga non si sono mai riprese dalla crisi del 2008. Unici in Europa.",
                   "«Soffrono tutti» è una scusa. Soffriamo **noi**."]},
    ]},

    # ───────── VEN 6 NOV · LAPIDARIO ─────────
    {"nome": "n04_lap_crisi_2008", "tipo": "sanders", "size": 74,
     "testo": ["Per la crisi finanziaria del 2008 sono finite in carcere 55 persone.",
               "Quasi tutte in Islanda.",
               "In America, epicentro del disastro: zero.",
               "A pagare il conto, invece, ci hanno pensato tutti gli altri."]},

    # ───────── MAR 10 NOV · CAROSELLO CASA ─────────
    {"nome": "n05_car_casa", "tipo": "carosello", "bg": "#123d2a", "slide": [
        {"tipo": "cover", "label": "Questione di casa", "n": "1/6", "scorri": True, "size": 215,
         "titolo": "Vienna 40\nRoma **7**",
         "sub": "Perché non trovi casa, in cinque numeri. Il primo è il più umiliante."},
        {"tipo": "testo", "label": "Milano", "n": "2/6", "scorri": True,
         "titolo": "Un bilocale\nin affitto (2023)", "big": "1.850 €|AL MESE", "bigsize": 220,
         "punti": ["Terza città più cara d'Europa (Scenari Immobiliari). Peggio fanno solo Amsterdam e Lisbona.",
                   "Ai ragazzi resta Cormano o Cologno, dove si compra a metà prezzo."]},
        {"tipo": "testo", "label": "Firenze", "n": "3/6", "scorri": True,
         "titolo": "Annunci Airbnb:\nda 6 mila a **14 mila**", "big": "+42%",
         "punti": ["È quanto è salito l'affitto medio in città.",
                   "Se pagavi 1.000 euro, oggi ne paghi 1.400. Oppure, più probabilmente, abiti in periferia."]},
        {"tipo": "testo", "label": "Milano, ancora", "n": "4/6", "scorri": True, "size": 92,
         "titolo": "«Se sei un povero di m***a non puoi stare qui»",
         "testo": ["È il commento che riceve una copywriter trentenne che racconta online la sua ricerca di casa.",
                   "Stipendio: 1.700 euro. La banca le offre un mutuo da 150 mila. **Sufficienti per un box.**"]},
        {"tipo": "duo", "label": "Case popolari sul totale", "n": "5/6", "scorri": True, "size": 104,
         "titolo": "Il vero\nproblema",
         "duo": [("Italia", "<5%", "meno di una casa su venti", False), ("Roma", "7%", "", False), ("Vienna", "40%", "quasi una su due", True)],
         "testo": ["Lo dice il sindaco di Roma, Roberto Gualtieri: da trent'anni mancano politiche per la casa."]},
        {"tipo": "cover", "label": "L'ultima volta", "n": "6/6", "size": 170,
         "titolo": "Fanfani,\n**355 mila**\ncase popolari",
         "sub": "Era il Piano Ina-Casa, nel dopoguerra. Da allora niente di paragonabile. Per costruire servono soldi: sappiamo benissimo dove sono."},
    ]},

    # ───────── MER 11 NOV · LAPIDARIO ─────────
    {"nome": "n06_lap_rendite", "tipo": "sanders", "size": 72,
     "testo": ["In Italia chi incassa affitti paga il 21%.",
               "Chi incassa dividendi, il 26%.",
               "Chi lavora come dipendente, quasi il doppio.",
               "E poi ci dicono che il lavoro va premiato."]},

    # ───────── GIO 12 NOV · POST ─────────
    {"nome": "n07_post_angeli", "tipo": "post", "bg": "#221c52", "slide": [
        {"tipo": "testo", "label": "Sanità, ieri e oggi", "size": 108,
         "titolo": "2020: «Siete\nnostri **angeli**»",
         "big": "27.000 €", "bigsize": 200,
         "testo": ["Autunno 2023: è la multa arrivata a tre primari per aver concesso troppi straordinari.",
                   "Cantavamo dai balconi. Poi la spesa sanitaria è scesa al **6,1%** del Pil, come nel 2004."]},
    ]},

    # ───────── VEN 13 NOV · LAPIDARIO ─────────
    {"nome": "n08_lap_mentone", "tipo": "sanders", "size": 74,
     "testo": ["Milionario francese con un'eredità da lasciare?",
               "Trasferisciti in Liguria. In Francia lo Stato può prendersi fino al 60%. Da noi, tra il 4 e l'8.",
               "Il paradiso fiscale dove in più si mangia bene."]},

    # ───────── MAR 17 NOV · CAROSELLO MILIARDARI ─────────
    {"nome": "n09_car_miliardari", "tipo": "carosello", "bg": "#1b3352", "slide": [
        {"tipo": "cover", "label": "Classifica 2024", "n": "1/6", "scorri": True, "size": 136,
         "titolo": "4 miliardari\nitaliani di cui\n**non hai mai\nsentito parlare**",
         "sub": "Ti dicono molto su come si fanno i soldi oggi. E su quante tasse si pagano."},
        {"tipo": "testo", "label": "Andrea Pignataro", "n": "2/6", "scorri": True,
         "titolo": "Il finanziere\nsenza volto", "big": "27 MLD|DI DOLLARI", "bigsize": 190,
         "punti": ["Ion Trading. Secondo in Italia, dietro a Ferrero. In giro c'è praticamente una sola sua foto.",
                   "Il fisco gli ha contestato 1,25 miliardi: dichiarava di vivere in Svizzera. Ha chiuso pagando 280 milioni, senza ammettere colpe."]},
        {"tipo": "testo", "label": "Giancarlo Devasini", "n": "3/6", "scorri": True,
         "titolo": "Dal bisturi\nalle cripto", "big": "9 MLD|E ROTTI", "bigsize": 190,
         "punti": ["Ex chirurgo plastico torinese. Ha creato Tether, la stablecoin più importante al mondo.",
                   "Ha messo 750 milioni in Rumble, la piattaforma amata da Trump e dall'alt-right."]},
        {"tipo": "testo", "label": "Giuseppe Crippa", "n": "4/6", "scorri": True,
         "titolo": "Il pensionato\nche si annoiava", "big": "4,7 MLD", "bigsize": 190,
         "punti": ["Classe 1935, ex tecnico STMicroelectronics. In pensione fonda Technoprobe, che testa i chip.",
                   "Non si compra isole: ha creato un orto solidale per disabili vicino a Cernusco. Rispetto."]},
        {"tipo": "testo", "label": "Alessandro Rosano", "n": "5/6", "scorri": True,
         "titolo": "Le scarpe da\nGrande Lebowski", "big": "2,5 MLD", "bigsize": 190,
         "punti": ["Durante il Covid inventa le HeyDude: brutte, comode, senza stringhe.",
                   "Crocs le compra per 2,5 miliardi. Più della metà finisce a lui, che entra nella stessa classifica di Armani."]},
        {"tipo": "cover", "label": "Il punto", "n": "6/6", "size": 200,
         "titolo": "**+10%**\nin un anno",
         "sub": "Tanto sono cresciuti i miliardari italiani: venti volte più della crescita del Pil (classifica Ubs). Una patrimoniale dall'1 al 3% non li renderebbe poveri. Solo un po' meno miliardari."},
    ]},

    # ───────── MER 18 NOV · LAPIDARIO ─────────
    {"nome": "n10_lap_zucman", "tipo": "sanders", "size": 74,
     "testo": ["I circa 3.000 miliardari del pianeta pagano in tasse lo 0,3% della loro ricchezza.",
               "La proposta di Gabriel Zucman: almeno il 2%.",
               "Ecco, questo sarebbe l'estremismo."]},

    # ───────── GIO 19 NOV · POST ─────────
    {"nome": "n11_post_panda", "tipo": "post", "bg": "#5a2318", "slide": [
        {"tipo": "duo", "label": "Quanto costa una Panda a un prof", "size": 112,
         "titolo": "Stipendi\nche servono",
         "duo": [("2010", "5,4", "mensilità", False), ("Oggi", "quasi 9", "mensilità", True)],
         "testo": ["Il calcolo è del Coordinamento Amaldi, prof di un liceo di Tor Bella Monaca, su dati Cgil. Stimano in un **32%** l'effetto dell'inflazione dal 2010.",
                   "Nel frattempo, la Panda non è diventata una Ferrari."]},
    ]},

    # ───────── VEN 20 NOV · LAPIDARIO ─────────
    {"nome": "n12_lap_segreto_bancario", "tipo": "sanders", "size": 74,
     "testo": ["Vent'anni fa il segreto bancario svizzero sembrava eterno.",
               "È caduto nel 2015.",
               "Oggi una patrimoniale sui multimilionari sembra impossibile.",
               "Finché non lo è più."]},

    # ───────── MAR 24 NOV · CAROSELLO QUIZ ─────────
    {"nome": "n13_quiz_chi_vive", "tipo": "carosello", "bg": "#14324f", "slide": [
        {"tipo": "cover", "label": "Quiz", "n": "1/6", "scorri": True, "size": 230,
         "titolo": "Chi vive\npiù a\n**lungo?**",
         "sub": "Un milionario americano o un povero svedese? Pensaci tre secondi, poi scorri."},
        {"tipo": "domanda", "label": "La domanda", "n": "2/6", "scorri": True, "size": 64,
         "domanda": "Chi ha più probabilità di arrivare in salute alla vecchiaia?",
         "opzioni": [("A", "Un milionario del New Jersey"), ("B", "Un povero di Stoccolma"), ("C", "Più o meno pari")]},
        {"tipo": "risposta", "label": "Risposta", "n": "3/6", "scorri": True, "size": 150,
         "titolo": "**C.** Quasi\npari",
         "testo": ["Uno studio del New England Journal of Medicine ha seguito per dodici anni 74 mila anziani, negli Stati Uniti e in sedici Paesi europei.",
                   "Conclusione: un milionario del New Jersey ha quasi le stesse chance di un povero di Stoccolma. O di un esponente del ceto medio di Bucarest."]},
        {"tipo": "barre", "label": "Morti all'anno ogni 1.000 anziani", "n": "4/6", "scorri": True, "size": 104,
         "titolo": "Si muore più tardi\na **Sofia** che a Chicago",
         "barre": [("Stati Uniti", 6.5, True, "6,5"), ("Europa dell'est", 5.8, False, "5,8"), ("Europa del sud", 4.9, False, "4,9"), ("Europa del nord e dell'ovest", 2.9, False, "2,9")]},
        {"tipo": "risposta", "label": "Perché", "n": "5/6", "scorri": True, "size": 120,
         "titolo": "Il welfare\nconviene a\n**tutti**",
         "testo": ["Lo stato sociale va a beneficio di tutti, ricchi compresi, spiega Martin McKee della London School of Hygiene, tra gli autori.",
                   "Un'ovvietà. Che conviene ripetere ogni volta che qualcuno vuole americanizzare il nostro Servizio sanitario."]},
        {"tipo": "cover", "label": "E noi?", "n": "6/6", "size": 170,
         "titolo": "Spesa\nsanitaria:\n**6,1%** del Pil",
         "sub": "Come nel 2004. E un italiano su dieci rinuncia alle cure perché non può pagarle. I soldi per salvare il Ssn ci sono: stanno nello 0,1% più ricco."},
    ]},

    # ───────── MER 25 NOV · LAPIDARIO ─────────
    {"nome": "n14_lap_quota_ricchezza", "tipo": "sanders", "size": 70,
     "testo": ["Dal 1995 al 2016 lo 0,1% più ricco degli italiani ha quasi raddoppiato la sua fetta di ricchezza: da meno del 6 a quasi il 10%.",
               "La metà più povera, oltre 25 milioni di persone, è scesa dal 12 a meno del 4%.",
               "Ma il problema, ci dicevano, era il reddito di cittadinanza."]},

    # ───────── GIO 26 NOV · POST ─────────
    {"nome": "n15_post_henley", "tipo": "post", "bg": "#4a1531", "slide": [
        {"tipo": "testo", "label": "Stessa fonte, due titoli", "size": 96,
         "titolo": "«I milionari\n**fuggono** da Londra»\n«I milionari\n**arrivano** in Italia»",
         "testo": ["Entrambe le stime vengono da Henley & Partners. Mestiere: vendere consulenze e visti dorati a chi vuole cambiare residenza.",
                   "Per l'esodo britannico contavano i profili LinkedIn. Letto bene, lo stesso rapporto dava un tasso di migrazione dei super ricchi dello **0,3%**."]},
    ]},

    # ───────── VEN 27 NOV · LAPIDARIO (BLACK FRIDAY) ─────────
    {"nome": "n16_lap_black_friday", "tipo": "sanders", "size": 70,
     "testo": ["Oggi è il Black Friday.",
               "Per i milionari italiani dura tutto l'anno.",
               "Affitti al 21%. Dividendi, via holding, intorno all'1%. Eredità a figli e coniuge al 4%, sopra il primo milione esente.",
               "Sconti che noi comuni mortali non vedremo mai."]},

    # ───────── MAR 1 DIC · CAROSELLO EUROPA ─────────
    {"nome": "n17_car_europa", "tipo": "carosello", "bg": "#123d2a", "slide": [
        {"tipo": "cover", "label": "Viaggio in Europa", "n": "1/6", "scorri": True, "size": 142,
         "titolo": "Tre covi di\npericolosi\nestremisti\n(con la **patrimoniale**)",
         "sub": "Paesi ricchi, moderati, civilissimi. Che i ricchi li tassano già."},
        {"tipo": "testo", "label": "Svizzera", "n": "2/6", "scorri": True,
         "titolo": "Banche, cioccolato\ne patrimoniale", "big": "0,6%", "bigsize": 230,
         "punti": ["È l'aliquota media sui patrimoni sopra il milione di franchi, decisa cantone per cantone.",
                   "Esiste dal X secolo. Sì, il decimo. Vale circa il 4% delle entrate fiscali."]},
        {"tipo": "testo", "label": "Norvegia", "n": "3/6", "scorri": True,
         "titolo": "La fuga\nche non c'è stata", "big": "+55%", "bigsize": 230,
         "punti": ["La formueskatt esiste dal 1890. Nel 2022 l'aliquota sale all'1,1% e il gettito tocca il record: 2,4 miliardi di euro.",
                   "I ricchissimi che emigrano? Meno del 3%. Come il resto dei norvegesi."]},
        {"tipo": "testo", "label": "Spagna", "n": "4/6", "scorri": True,
         "titolo": "Nata con\nla democrazia", "big": "2 MLD+", "bigsize": 230,
         "punti": ["Introdotta nel 1977, coi patti della Moncloa che archiviano Franco. Dal 2022 c'è anche un'imposta di solidarietà sopra i 3 milioni.",
                   "Gettito 2023: oltre 2 miliardi. E nessun fuggi fuggi di miliardari."]},
        {"tipo": "testo", "label": "Italia", "n": "5/6", "scorri": True,
         "titolo": "Patrimoniale\nsui super ricchi", "big": "ZERO", "bigsize": 260,
         "punti": ["In compenso abbiamo un forfait da 200 mila euro l'anno per i milionari stranieri, qualunque cifra guadagnino all'estero.",
                   "Il paradiso fiscale, di solito, è un'isola. Il nostro è una penisola."]},
        {"tipo": "cover", "label": "Facciamo due conti", "n": "6/6", "size": 170,
         "titolo": "Anche poco\nfarebbe\n**3 miliardi**",
         "sub": "Se raccogliessimo appena quanto la Spagna, lo 0,5% delle entrate. Con la proposta di Oxfam Italia, dall'1 al 3% sullo 0,1% più ricco: circa 13 miliardi l'anno."},
    ]},

    # ───────── MER 2 DIC · LAPIDARIO ─────────
    {"nome": "n18_lap_davvero", "tipo": "sanders", "size": 78,
     "testo": ["Se sei milionario puoi, anzi dovresti, pagare molte più tasse di un impiegato.",
               "Se sei miliardario, mille volte di più.",
               "Davvero c'è bisogno di spiegarlo?"]},
]
