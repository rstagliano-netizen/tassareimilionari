# Ricarica automatica serale (Buffer, Typefully, Metricool)

Procedura eseguita ogni sera alle 21 dall'attività programmata «Ricarica coda social».

## Fonti
- `novembre/coda_novembre.json`: lista di voci Buffer (LinkedIn, Instagram, TikTok) fino al 2 dicembre.
- `dicembre/coda_dicembre.json`: chiave `buffer` (voci dal 23 novembre al 23 dicembre, più i reel da recuperare su TikTok, chiave `video`) e chiave `lapidari_da_riciclare` (per X, Threads, Bluesky e Note Substack).

## Buffer (organizzazione «My Organization», 678e577a2982e948e675fc12; piano gratuito: massimo 10 post in coda)
1. Leggi le voci di entrambi i file con `dueAt` successivo ad adesso + 30 minuti.
2. Elenca i post Buffer con stato scheduled, sending, sent ed error da 7 giorni fa in avanti. Una voce è già fatta se esiste un post sullo stesso `channelId` con lo stesso `dueAt` (stesso minuto). Saltala.
3. Conta i post in stato scheduled: i posti liberi sono 10 meno quel numero.
4. Aggiungi le voci mancanti in ordine di `dueAt`, la più vicina per prima, finché ci sono posti: `create_post` con `channelId`, `schedulingType` automatic, `mode` customScheduled, `dueAt`, `text`, `assets` (per ogni immagine `{image: {url, metadata: {altText}}}`, per il video `{video: {url}}`); per Instagram `metadata.instagram` = `{type: "post", shouldShareToFeed: true}`.
5. Se Buffer rifiuta una voce, non riprovare più di una volta; annotala nel resoconto.

## Typefully (social set 352215; piano gratuito: 10 post al mese)
- Dal 1° di ogni mese, se ci sono post Typefully ancora disponibili nel mese, programma i `lapidari_da_riciclare` con `data` futura alle 12:00 (ora di Roma), uno per giorno, su X, Threads, Bluesky e Substack, con la stessa immagine (caricala con create_media_upload). Testo: `hook` + «\n\n#tassareimilionari @einaudieditore»; su Substack `hook` + «\n\nDa «Tassare i milionari» (Einaudi)». Non superare 10 post pubblicati o programmati nel mese.

## Metricool (brand 7901406; piano gratuito: 20 post pubblicati al mese)
- Se Threads e Bluesky risultano collegati al brand (getBrandSettings), usali per i lapidari che non trovano posto su Typefully, sempre alle 12:00, senza superare 20 post nel mese contando gli Shorts di YouTube già programmati (e contando come due un post che esce su due reti).

## Dopo
- Aggiorna il registro dei post nella memoria del progetto (areas/registro-post.md) con cosa hai messo in coda.
- Manda a Riccardo un messaggio breve solo se qualcosa è andato storto o se le code si stanno svuotando (meno di 3 giorni di contenuti futuri rimasti nei file).
