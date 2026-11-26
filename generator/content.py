"""Contenuti bilingui del sito Eiraman 0.3. Struttura: Perché -> Come -> Cosa."""

SLUG = {  # chiave: (it, en)
    "home": ("index", "index"), "metodo": ("metodo", "method"),
    "principi": ("principi", "principles"), "ruoli": ("ruoli", "roles"), "fasi": ("fasi", "phases"),
    "decisioni": ("decisioni", "decisions"), "qualita": ("qualita", "quality"), "ritmo": ("ritmo", "rhythm"),
    "livelli": ("livelli", "levels"), "documenti": ("documenti", "documents"), "profili": ("profili", "profiles"),
    "sicurezza": ("sicurezza", "security"), "specifica": ("specifica", "specification"),
    "mappa": ("mappa", "map"), "pilota": ("pilota", "pilot"), "progetti": ("progetti", "projects"),
}
ORDER = ["principi", "ruoli", "fasi", "decisioni", "qualita", "ritmo", "livelli", "documenti", "profili", "sicurezza"]

UI = {
    "it": dict(skip="Vai al contenuto", nav=[("metodo", "Il metodo"), ("livelli", "Livelli"), ("progetti", "I progetti"), ("specifica", "Specifica")],
               menu="Menu", home="Home", method="Il metodo", part="Parte {n} di {t}", prev="Precedente", next="Successiva",
               how="Come funziona", what="Che cosa prevede", norm="Testo normativo completo", specref="Leggi nella specifica",
               foot="© 2026 Paolo Ungari e contributori · Testi della Guida e del sito CC BY-SA 4.0 · Role Profile CC BY 4.0 · Codice Apache 2.0 · Nome e logo Eiraman: marchio, vedi <a href=\"https://github.com/eiraman/community/blob/main/TRADEMARK.md\" rel=\"noopener\">TRADEMARK.md</a>", tog="TOGAF® è un marchio registrato di The Open Group.",
               footnav=[("metodo", "Il metodo"), ("mappa", "Mappa funzionale"), ("progetti", "I progetti"), ("specifica", "Specifica 0.3")],
               lang_label="Lingua", explore="Esplora"),
    "en": dict(skip="Skip to content", nav=[("metodo", "The method"), ("livelli", "Levels"), ("progetti", "Projects"), ("specifica", "Specification")],
               menu="Menu", home="Home", method="The method", part="Part {n} of {t}", prev="Previous", next="Next",
               how="How it works", what="What it requires", norm="Full normative text", specref="Read in the specification",
               foot="© 2026 Paolo Ungari and contributors · Guide and site text CC BY-SA 4.0 · Role Profiles CC BY 4.0 · Code Apache 2.0 · Eiraman name and logo: trademark, see <a href=\"https://github.com/eiraman/community/blob/main/TRADEMARK.md\" rel=\"noopener\">TRADEMARK.md</a>", tog="TOGAF® is a registered trademark of The Open Group.",
               footnav=[("metodo", "The method"), ("mappa", "Functional map"), ("progetti", "Projects"), ("specifica", "Specification 0.3")],
               lang_label="Language", explore="Explore"),
}

EMBLEM = {
    "it": dict(why="Perché", how=["Decidi", "Esegui", "Dimostra"], what="COSA · IL METODO EIRAMAN · LIVELLI · REGOLE · PROVE ·",
               label="Emblema Eiraman: al centro il perché; intorno il come, in tre tempi: decidi, esegui, dimostra; all'esterno il cosa, il metodo."),
    "en": dict(why="Why", how=["Decide", "Execute", "Prove"], what="WHAT · THE EIRAMAN METHOD · LEVELS · RULES · EVIDENCE ·",
               label="Eiraman emblem: the why at the centre; around it the how, in three moves: decide, execute, prove; on the outside the what, the method."),
}

HOME = {
    "it": dict(
        title="Eiraman · Software dall'AI, decisioni tue",
        desc="Eiraman è il metodo per far costruire software da squadre di AI restando padroni delle decisioni, anche senza saper leggere il codice.",
        kicker="Perché",
        h1="Chi ha l'idea deve restarne padrone, anche senza leggere il codice.",
        sub="Per imprenditori, manager e uffici senza programmatori. Oggi l'AI costruisce software: Eiraman lascia le decisioni a chi conosce il business.",
        cta1="Scopri come", cta2="Vedi i dati del pilota",
        prob_tag="Perché serve", prob_h="Che cosa manca oggi?",
        prob=[("nospec", "Nessun team di sviluppo", "Molte idee nascono dove non ci sono programmatori."),
              ("eye", "Controlli che nessuno legge", "Cento approvazioni tecniche non sono governo."),
              ("coin", "Costi e rischi invisibili", "Senza misure, l'AI sembra gratis e sicura.")],
        how_tag="Come funziona", how_h="Tre tempi, sempre gli stessi.",
        how=[("pen", "human", "Decidi prima", "Obiettivo, budget e limiti, scritti prima."),
             ("team", "ai", "L'AI esegue", "Agenti che costruiscono e si controllano."),
             ("stamp", "ai", "Le prove dimostrano", "Finito vuol dire provato.")],
        who_h="Chi fa che cosa?",
        who_h1="Tu", who1=[("target", "Fissi obiettivi e budget"), ("door1", "Decidi ciò che non si annulla"), ("check", "Accetti il risultato")],
        who_h2="L'AI Squad", who2=[("gear", "Progetta e costruisce"), ("scale", "Fa controllare il lavoro da altri agenti"), ("doc", "Ti porta solo scelte di business")],
        what_tag="Che cosa contiene", what_h="Fin dove arriva?",
        stairs=[("person", "0", "Per me", "Strumenti personali."),
                ("group", "1", "Per il mio team", "Colleghi, con accesso aziendale."),
                ("globe", "2", "Per i clienti", "Utenti esterni, con test di sicurezza.")],
        out=("lock", "Fuori", "Dati sanitari, pagamenti gestiti nel codice, AI ad alto rischio."),
        stairs_note="Un gradino alla volta, con prove.",
        invite="Che cosa c'è nel metodo?", invite_btn="Esplora il metodo"),
    "en": dict(
        title="Eiraman · Software from AI, decisions yours",
        desc="Eiraman is the method for having AI Squads build software while you keep control of the decisions, even if you cannot read code.",
        kicker="Why",
        h1="Whoever has the idea should stay in charge of it, even without reading code.",
        sub="For business owners, managers and teams without programmers. AI now builds software: Eiraman leaves the decisions to those who know the business.",
        cta1="See how", cta2="See the pilot data",
        prob_tag="Why it is needed", prob_h="What is missing today?",
        prob=[("nospec", "No development team", "Many ideas start where there are no programmers."),
              ("eye", "Checks nobody reads", "A hundred technical approvals are not governance."),
              ("coin", "Hidden costs and risks", "Without measures, AI looks free and safe.")],
        how_tag="How it works", how_h="Three moves, always the same.",
        how=[("pen", "human", "Decide first", "Goal, budget and limits, written first."),
             ("team", "ai", "AI executes", "Agents that build and check themselves."),
             ("stamp", "ai", "Evidence proves", "Finished means proven.")],
        who_h="Who does what?",
        who_h1="You", who1=[("target", "Set goals and budget"), ("door1", "Decide what cannot be undone"), ("check", "Accept the result")],
        who_h2="The AI Squad", who2=[("gear", "Designs and builds"), ("scale", "Has its work checked by other agents"), ("doc", "Brings you business choices only")],
        what_tag="What it contains", what_h="How far does it go?",
        stairs=[("person", "0", "For me", "Personal tools."),
                ("group", "1", "For my team", "Colleagues, with company sign-in."),
                ("globe", "2", "For customers", "External users, with security tests.")],
        out=("lock", "Out", "Health data, payments handled in the code, high-risk AI."),
        stairs_note="One step at a time, with evidence.",
        invite="What is inside the method?", invite_btn="Explore the method"),
}

METHOD = {
    "it": dict(
        title="Il metodo · Eiraman", desc="Panoramica del metodo Eiraman: perché esiste, come funziona, che cosa contiene.",
        h1="Il metodo Eiraman",
        why="Un modo per governare da manager il lavoro di squadre di AI: regole semplici da capire, prove da verificare.",
        cols=[("why", "Perché esiste", "Il business può già far scrivere software all'AI. Manca il modo di restarne padroni: sapere chi decide, quando un lavoro è davvero finito, quanto costa."),
              ("how", "Come funziona", "Tu decidi prima, con un mandato. L'AI Squad svolge tutte le fasi e risolve da sola ciò che si può annullare. A te arrivano poche decisioni, sempre in linguaggio di business."),
              ("what", "Che cosa contiene", "Principi, ruoli, fasi, regole per le decisioni e per la qualità, un ritmo di lavoro, livelli di applicabilità, documenti, competenze e sicurezza. Ogni parte ha la sua pagina.")],
        explore_h="Esplora il metodo", explore_p="Dieci parti, dalla più semplice alla più tecnica. Ognuna parte dal perché.",
        ref_h="Per approfondire", ref=[("specifica", "doc", "La specifica 0.2", "Il testo normativo completo, sezione per sezione."),
                                        ("mappa", "layers", "La mappa funzionale", "Cinque schemi tecnici del funzionamento."),
                                        ("progetti", "target", "I progetti", "Che cosa è stato costruito con il metodo, con i numeri.")],
        note="Le pagine seguono lo schema Perché, Come, Cosa (S. Sinek, Start with Why, 2009)."),
    "en": dict(
        title="The method · Eiraman", desc="Overview of the Eiraman method: why it exists, how it works, what it contains.",
        h1="The Eiraman method",
        why="A way to govern the work of AI Squads as a manager: rules that are simple to understand, evidence that can be checked.",
        cols=[("why", "Why it exists", "The business can already have AI write software. What is missing is a way to stay in charge: knowing who decides, when work is really finished, what it costs."),
              ("how", "How it works", "You decide first, with a mandate. The AI Squad carries out every phase and settles on its own whatever can be undone. Only a few decisions reach you, always in business language."),
              ("what", "What it contains", "Principles, roles, phases, rules for decisions and quality, a working rhythm, applicability levels, documents, expertise and security. Each part has its own page.")],
        explore_h="Explore the method", explore_p="Ten parts, from the simplest to the most technical. Each one starts from the why.",
        ref_h="Go deeper", ref=[("specifica", "doc", "Specification 0.2", "The full normative text, section by section."),
                                 ("mappa", "layers", "Functional map", "Five technical diagrams of how it works."),
                                 ("progetti", "target", "Projects", "What has been built with the method, with the numbers.")],
        note="Pages follow the Why, How, What pattern (S. Sinek, Start with Why, 2009)."),
}

# Pagine componente: card (icona, tono, titolo breve, riga), titolo pagina, perché, come (testo), tessere, cosa (regole), sezioni normative
COMP = {
 "principi": dict(icon="flag", tone="fw", spec=(1,), norm=["s1"],
  it=dict(card="Principi", line="Otto idee che guidano ogni scelta.", h1="Quali idee guidano il metodo?",
    why="Otto principi bastano per capire come ragiona Eiraman e per accorgersi subito quando qualcosa non va.",
    how="Ogni regola del metodo discende da uno di questi principi. Se una pratica li contraddice, è la pratica a essere sbagliata.",
    tiles=[("nospec","fw","La competenza sta nei profili, non in ogni progetto","Eiraman non sostituisce chi sviluppa: ne sposta la competenza nei profili che guidano gli agenti."),
           ("pen","human","Decidi prima, non a ogni passo","Un buon mandato vale più di cento approvazioni."),
           ("door1","human","Ciò che non si annulla lo decidi tu","Il resto lo decide l'AI Squad."),
           ("silence","deny","Il silenzio non approva mai","Senza risposta si ferma solo il lavoro che ne dipende."),
           ("stamp","ai","Finito vuol dire provato","Un lavoro si chiude solo con un'evidenza."),
           ("eye","ai","Chi verifica non è chi esegue","Giudici indipendenti, di un modello diverso."),
           ("alert","fw","Prima le cattive notizie","Ogni documento apre con ciò che non va, perché un agente tende a compiacere chi legge."),
           ("coin","fw","Ogni costo conta","Anche i tentativi e le candidate scartate.")],
    rules=[("1","La competenza sta nei profili, non in ogni progetto: chi sviluppa porta la propria competenza nei Role Profile qualificati; l'operatore umano del progetto decide su funzioni e costi."),
           ("2","Human as a Manager: l'umano agisce prima, con mandato, principi, deleghe, riserve e budget; non supervisiona l'esecuzione."),
           ("3","Esclusioni: il metodo non si applica ai sistemi AI vietati o ad alto rischio e agli altri casi fuori perimetro.")]),
  en=dict(card="Principles", line="Eight ideas behind every choice.", h1="What ideas drive the method?",
    why="Eight principles are enough to understand how Eiraman thinks and to notice at once when something is wrong.",
    how="Every rule of the method comes from one of these principles. If a practice contradicts them, the practice is wrong.",
    tiles=[("nospec","fw","Competence lives in profiles, not in every project","Eiraman does not replace those who develop software: it moves their competence into the profiles that guide the agents."),
           ("pen","human","Decide first, not at every step","A good mandate is worth more than a hundred approvals."),
           ("door1","human","What cannot be undone is yours","The AI Squad decides the rest."),
           ("silence","deny","Silence never approves","Without an answer, only the work that depends on it stops."),
           ("stamp","ai","Finished means proven","Work closes only with evidence."),
           ("eye","ai","Whoever checks does not execute","Independent judges, on a different model."),
           ("alert","fw","Bad news first","Every document opens with what is wrong, because an agent tends to please its reader."),
           ("coin","fw","Every cost counts","Including discarded attempts and candidates.")],
    rules=[("1","Competence lives in profiles, not in every project: those who develop software bring their competence into qualified Role Profiles; the human operator of the project decides on functions and costs."),
           ("2","Human as a Manager: the human acts first, with mandate, principles, delegations, reserved matters and budget; they do not supervise execution."),
           ("3","Exclusions: the method does not apply to prohibited or high-risk AI systems or to the other out-of-scope cases.")])),
 "ruoli": dict(icon="manager", tone="human", spec=(2,), norm=["s2"],
  it=dict(card="Ruoli", line="Chi decide, chi esegue, chi risponde.", h1="Chi decide, chi esegue, chi risponde?",
    why="Sapere chi fa che cosa è la condizione per delegare all'AI senza perdere il controllo.",
    how="Tu rispondi delle tue decisioni. Le AI rispondono in senso operativo: ogni chiusura ha una prova. Verso clienti e terzi risponde il titolare: tu, se il progetto è per te; la tua organizzazione, se è per altri.",
    tiles=[("manager","human","Product Owner","Tu: mandato, budget, decisioni di business, accettazione."),
           ("team","ai","Coordinatore AI","Pianifica, assegna il lavoro, lo chiude solo con prove."),
           ("gear","ai","Ruoli specialistici AI","Analisti, architetti, sviluppatori, tester e revisori."),
           ("eye","ai","Revisore di processo","Controlla a campione che le decisioni giuste ti siano arrivate."),
           ("building","fw","Manutentori","Esperti dell'organizzazione che qualificano le competenze.")],
    rules=[("A","Accountability interna: ciascuno risponde di ciò che decide; la responsabilità delle AI è operativa, non giuridica."),
           ("B","Verso terzi risponde il titolare: la persona al livello 0, l'organizzazione ai livelli 1 e 2."),
           ("C","Ai livelli 1 e 2 il Product Owner agisce con un mandato formale dell'organizzazione.")]),
  en=dict(card="Roles", line="Who decides, who executes, who answers.", h1="Who decides, who executes, who answers?",
    why="Knowing who does what is the condition for delegating to AI without losing control.",
    how="You answer for your decisions. The AIs answer operationally: every closure has evidence. Towards customers and third parties the owner answers: you, if the project is for yourself; your organisation, if it is for others.",
    tiles=[("manager","human","Product Owner","You: mandate, budget, business decisions, acceptance."),
           ("team","ai","AI coordinator","Plans, assigns work, closes it only with evidence."),
           ("gear","ai","Specialist AI roles","Analysts, architects, developers, testers and reviewers."),
           ("eye","ai","Process reviewer","Samples work to check the right decisions reached you."),
           ("building","fw","Maintainers","Experts in the organisation who qualify the expertise.")],
    rules=[("A","Internal accountability: each answers for what they decide; the AIs' responsibility is operational, not legal."),
           ("B","Towards third parties the owner answers: the person at level 0, the organisation at levels 1 and 2."),
           ("C","At levels 1 and 2 the Product Owner acts under a formal mandate from the organisation.")])),
 "fasi": dict(icon="compass", tone="ai", spec=(5,), norm=["governare-lo-scopo", "ciclo-di-produzione"], norm_en=["governing-the-scope", "production-cycle"],
  it=dict(card="Fasi", line="Dalla prima idea al servizio in esercizio.", h1="Dalla prima idea al servizio: che cosa succede?",
    story=dict(h="La perla d'amore", src="H. G. Wells, «The Pearl of Love» · Wikisource",
      p="In un racconto di H. G. Wells un principe dedica la vita a costruire un mausoleo per la donna amata. Anno dopo anno lo amplia e lo perfeziona, finché il sarcofago gli sembra fuori posto nella composizione e ordina: «Portate via quella cosa». Eiraman protegge la Visione perché l'opera non divori il proprio scopo: cambiarla significa aprire un nuovo progetto."),
    why="Tutte le fasi le svolge l'AI Squad. Tu intervieni solo nei momenti in cui la scelta è tua.",
    how="Ogni fase è fatta di cicli di lavoro brevi, con le stesse regole: decisioni, controllo di qualità, chiusura su prova, costi registrati.",
    phases=[("lens","Scoperta","Approvi la Visione"),("gear","POC","Intervieni solo se va male"),("layers","Design e planning","Approvi principi e budget"),("team","Scale","Una revisione a settimana"),("check","Accettazione ed esercizio","Accetti il risultato")],
    you="Tu:",
    rules=[("V","La Visione diventa vincolante con il mandato; cambiarla significa aprire un nuovo progetto."),
           ("P","I Principi si congelano alla fine del planning; un cambio durante l'installazione rende la versione fallita."),
           ("A","Il mandato contiene i criteri di arresto: spesa, cicli senza risultati, POC negativo.")]),
  en=dict(card="Phases", line="From the first idea to a running service.", h1="From first idea to service: what happens?",
    story=dict(h="The Pearl of Love", src="H. G. Wells, “The Pearl of Love” · Wikisource",
      p="In a story by H. G. Wells, a prince devotes his life to building a mausoleum for the woman he loved. Year after year he enlarges and refines it, until the sarcophagus seems out of place in the composition and he orders: “Take that thing away.” Eiraman protects the Vision so that the work does not consume its own purpose: changing it means opening a new project."),
    why="The AI Squad carries out every phase. You step in only when the choice is yours.",
    how="Each phase is made of short work cycles with the same rules: decisions, quality control, closure on evidence, costs recorded.",
    phases=[("lens","Discovery","You approve the Vision"),("gear","POC","You step in only if it fails"),("layers","Design and planning","You approve principles and budget"),("team","Scale","One review a week"),("check","Acceptance and operation","You accept the result")],
    you="You:",
    rules=[("V","The Vision becomes binding with the mandate; changing it means opening a new project."),
           ("P","Principles are frozen at the end of planning; a change during installation marks the version as failed."),
           ("S","The mandate contains stopping criteria: spend, cycles without results, a negative POC.")])),
 "decisioni": dict(icon="door1", tone="human", spec=(3,), norm=["s3"],
  it=dict(card="Decisioni", line="Quali scelte arrivano a te, e quali no.", h1="Quali decisioni arrivano a te?",
    why="Solo quelle che non si possono annullare o che toccano ciò che ti sei riservato. Tutto il resto lo decide l'AI Squad.",
    how="Il criterio viene dalle «porte a una via» e «a due vie» di Jeff Bezos: una porta a due vie si può riattraversare a un costo noto. Nel dubbio, la si tratta come una porta a una via.",
    trio=[("lock","deny","Deny · bloccato","Ciò che il mandato vieta deve impedirlo l'ambiente, non l'agente."),
          ("door2","ai","Delegate · decide l'AI","Scelte reversibili a costo noto: porte a due vie."),
          ("door1","human","Do · decidi tu","Scelte irreversibili e riserve del mandato: porte a una via.")],
    silence="Il silenzio non approva mai: senza risposta si ferma solo il lavoro che ne dipende, il resto prosegue, e la scelta irreversibile non viene eseguita.",
    rules=[("E1","Il mandato elenca le riserve; a te arriva il loro impatto di business, non la scelta tecnica."),
           ("E2","La reversibilità decide tra Delegate e Do."),
           ("E3","Ogni scelta non banale è registrata come micro-decisione."),
           ("E4","Un classificatore su un modello diverso decide che cosa sale a te; in disaccordo, sale."),
           ("E5","Gli scostamenti dal piano si sommano in un budget di deriva."),
           ("E6","Si misurano le decisioni che non ti sono arrivate e quelle arrivate senza motivo.")]),
  en=dict(card="Decisions", line="Which choices reach you, and which do not.", h1="Which decisions reach you?",
    why="Only those that cannot be undone or that touch what you reserved for yourself. The AI Squad decides everything else.",
    how="The criterion comes from Jeff Bezos's one-way and two-way doors: a two-way door can be walked back through at a known cost. When in doubt, treat it as a one-way door.",
    trio=[("lock","deny","Deny · blocked","What the mandate forbids must be prevented by the environment, not by the agent."),
          ("door2","ai","Delegate · AI decides","Reversible choices at a known cost: two-way doors."),
          ("door1","human","Do · you decide","Irreversible choices and reserved matters: one-way doors.")],
    silence="Silence never approves: without an answer only the work that depends on it stops, the rest carries on, and the irreversible option is never carried out.",
    rules=[("E1","The mandate lists reserved matters; you receive their business impact, not the technical choice."),
           ("E2","Reversibility decides between Delegate and Do."),
           ("E3","Every non-trivial choice is recorded as a micro-decision."),
           ("E4","A classifier on a different model decides what reaches you; if it disagrees, it reaches you."),
           ("E5","Deviations from the plan add up in a drift budget."),
           ("E6","Decisions that should have reached you, and those that reached you needlessly, are measured.")])),
 "qualita": dict(icon="scale", tone="ai", spec=(4, 6), norm=["s4", "chiusura"], norm_en=["s4", "closure"],
  it=dict(card="Qualità", line="Come l'AI si controlla da sola.", h1="Come fa l'AI a controllarsi da sola?",
    why="Non basta che un agente dica «fatto». Servono prove, giudici indipendenti e, quando conviene, più proposte a confronto.",
    how="Per i lavori più delicati si preparano due o tre proposte; un giudice di un altro modello le valuta con criteri fissati prima. Poi le critiche delle perdenti migliorano la vincitrice.",
    flow=[("doc","Lavoro"),("layers","1–3 proposte"),("scale","Giudice di un altro modello"),("check","Selezione"),("stamp","Chiusura su prova")],
    tiles=[("stamp","ai","Chiusura su prova","Si chiude solo se i controlli obbligatori passano."),
           ("eye","ai","Verifica indipendente","Chi verifica non vede la discussione di chi esegue."),
           ("gear","fw","Controlli automatici","Analisi del codice, dipendenze, licenze, segreti."),
           ("coin","fw","Concorrenza solo se conviene","Se non batte un esecutore singolo, si torna a uno.")],
    rules=[("K1","Più proposte solo con un selettore affidabile: test, criteri misurabili o una rubrica fissata prima."),
           ("K2","Si registra quanto sono diverse le proposte: modello, fornitore o strategia."),
           ("K3","Di norma una sola proposta; da 2 a 3 solo per lavori molto variabili o costosi da sbagliare."),
           ("K4","Le critiche delle proposte perdenti migliorano la vincitrice."),
           ("K5","Parte dei criteri resta nascosta e i giudici ruotano."),
           ("K6","Se il confronto non batte l'esecutore singolo, per quel tipo di lavoro si torna a una proposta."),
           ("K7–K9","Proposte molto divergenti: si sceglie ciò che costa meno annullare; i casi ripetuti diventano un tema per te.")]),
  en=dict(card="Quality", line="How AI checks itself.", h1="How does AI check itself?",
    why="An agent saying “done” is not enough. You need evidence, independent judges and, when worth it, several proposals compared.",
    how="For the most delicate work two or three proposals are prepared; a judge on another model assesses them against criteria fixed in advance. The losers' critiques then improve the winner.",
    flow=[("doc","Work"),("layers","1–3 proposals"),("scale","Judge on another model"),("check","Selection"),("stamp","Closure on evidence")],
    tiles=[("stamp","ai","Closure on evidence","It closes only if the mandatory checks pass."),
           ("eye","ai","Independent check","The checker does not see the executor's discussion."),
           ("gear","fw","Automatic checks","Code analysis, dependencies, licences, secrets."),
           ("coin","fw","Competition only if it pays","If it does not beat a single executor, back to one.")],
    rules=[("K1","Several proposals only with a reliable selector: tests, measurable criteria or a rubric fixed in advance."),
           ("K2","How different the proposals are is recorded: model, provider or strategy."),
           ("K3","Normally one proposal; 2 to 3 only for highly variable work or costly mistakes."),
           ("K4","The losing proposals' critiques improve the winner."),
           ("K5","Some criteria stay hidden and judges rotate."),
           ("K6","If comparison does not beat the single executor, that type of work goes back to one proposal."),
           ("K7–K9","Very divergent proposals: choose what is cheapest to undo; repeated cases become a topic for you.")])),
 "ritmo": dict(icon="calendar", tone="human", spec=(5,), norm=["wave-e-ciclo-di-governo", "scadenze-e-urgenze"], norm_en=["waves-and-the-governance-cycle", "deadlines-and-urgencies"],
  it=dict(card="Ritmo", line="Mezz'ora a settimana: come è possibile.", h1="Mezz'ora a settimana: come è possibile?",
    why="Le AI lavorano a cicli brevi; tu decidi con il tuo ritmo, una volta a settimana, su una sola pagina.",
    how="Le Wave dell'AI Squad si susseguono in automatico entro budget e mandato. Il ciclo di governo raccoglie tutto in una revisione: consegne, spesa, decisioni aperte, proposta per la settimana dopo.",
    lane_ai="Wave dell'AI Squad", lane_po="Il tuo ciclo di governo", review="revisione",
    tiles=[("calendar","human","Una revisione a settimana","Una pagina, in linguaggio di business."),
           ("cycle","ai","Wave brevi e automatiche","Con tetto di spesa e durata massima."),
           ("silence","deny","Il silenzio non approva","Senza risposta il lavoro resta sospeso; alla seconda scadenza esce dalla Wave."),
           ("alert","deny","Urgenze già previste","Azioni di contenimento reversibili, autorizzate nel mandato.")],
    rules=[("≈3","Riferimento: circa 3 decisioni per ciclo e 30 minuti a settimana; ognuno può fissare i propri valori."),
           ("80%","All'80% del budget di una Wave arriva un avviso; al 100% non si apre nuovo lavoro."),
           ("3+3","Decisione ordinaria: 3 giorni lavorativi, poi altri 3; urgente: 4 ore.")]),
  en=dict(card="Rhythm", line="Half an hour a week: how it can work.", h1="Half an hour a week: how can it work?",
    why="The AIs work in short cycles; you decide at your own pace, once a week, on a single page.",
    how="The AI Squad's Waves follow one another automatically within budget and mandate. The governance cycle gathers everything into one review: deliveries, spend, open decisions, a proposal for next week.",
    lane_ai="AI Squad Waves", lane_po="Your governance cycle", review="review",
    tiles=[("calendar","human","One review a week","One page, in business language."),
           ("cycle","ai","Short, automatic Waves","With a spending cap and maximum duration."),
           ("silence","deny","Silence does not approve","Without an answer the work stays suspended; at the second deadline it leaves the Wave."),
           ("alert","deny","Emergencies planned ahead","Reversible containment actions, authorised in the mandate.")],
    rules=[("≈3","Reference: about 3 decisions per cycle and 30 minutes a week; anyone can set their own values."),
           ("80%","At 80% of a Wave's budget a warning arrives; at 100% no new work starts."),
           ("3+3","Ordinary decision: 3 working days, then 3 more; urgent: 4 hours.")])),
 "livelli": dict(icon="steps", tone="fw", spec=(10,), norm=["s10"],
  it=dict(card="Livelli", line="Fin dove si arriva senza uno specialista in ogni progetto.", h1="Fin dove si arriva senza uno specialista in ogni progetto?",
    why="Il metodo limita il rischio in partenza: si comincia per sé, si sale un gradino alla volta con prove, alcuni casi restano esclusi.",
    how="Ogni progetto ha una classe, ogni adozione un livello. Un progetto parte solo se la sua classe non supera il livello di chi lo usa. Un controllo automatico lo verifica all'inizio, a ogni Wave e a ogni cambio di mandato; nel dubbio, il progetto è fuori.",
    rules=[("0","Per me: nessun dato personale di altri; controlli automatici su codice, dipendenze e segreti."),
           ("1","Per il mio team: accesso aziendale, prova di ripristino, procedura per le violazioni di dati entro 72 ore."),
           ("2","Per i clienti: requisiti OWASP ASVS, scansioni a ogni rilascio, penetration test esterno acquistato."),
           ("✕","Fuori: dati particolari (come salute) o giudiziari, minori, pagamenti nel codice, AI ad alto rischio, NIS2, software distribuito.")]),
  en=dict(card="Levels", line="How far you can go without a specialist in every project.", h1="How far can you go without a specialist in every project?",
    why="The method limits risk up front: you start for yourself, climb one step at a time with evidence, and some cases stay excluded.",
    how="Each project has a class, each adoption a level. A project starts only if its class does not exceed the level of whoever uses it. An automatic gate checks this at the start, at every Wave and at every change of mandate; when in doubt, the project is out.",
    rules=[("0","For me: no personal data about others; automatic checks on code, dependencies and secrets."),
           ("1","For my team: company sign-in, restore test, a 72-hour data-breach procedure."),
           ("2","For customers: OWASP ASVS requirements, scans at every release, a purchased external penetration test."),
           ("✕","Out: special-category (such as health) or criminal data, minors, payments in the code, high-risk AI, NIS2, distributed software.")])),
 "documenti": dict(icon="doc", tone="fw", spec=(8,), norm=["s8"],
  it=dict(card="Documenti", line="Che cosa leggi tu, che cosa leggono gli altri.", h1="Che cosa leggi tu, e che cosa no?",
    why="Leggi poche pagine scritte per un manager. Il resto lo leggono e lo verificano gli agenti.",
    how="I documenti hanno tre livelli. Quelli per te sono brevi, in linguaggio di business, e aprono con le cattive notizie: gli agenti usano modelli linguistici, che tendono a compiacere chi li interroga e ad attenuare ciò che è andato male. Per auditor e clienti esiste un pacchetto di prove separato.",
    pyr=[("Strategico","Approvi: Visione, Principi, mandato","human"),("Manageriale","Leggi e decidi: una pagina per decisione","human"),("Operativo","Solo agenti: architettura, registri, test","ai")],
    third="Pacchetto di prove per terzi",
    tiles=[("alert","deny","Prima le cattive notizie","Test falliti, rischi aperti, dissensi: in apertura."),
           ("doc","fw","Una pagina per decisione","Cosa cambia, cosa si chiede, entro quando."),
           ("stamp","ai","Ogni affermazione ha una prova","Il revisore controlla il collegamento."),
           ("lens","ai","Un'omissione blocca il documento","Come un test fallito blocca il lavoro.")],
    rules=[("1–6","Linguaggio di business; quattro domande in apertura; prima le variazioni; una pagina; esiti, non procedure; ogni affermazione con prova."),
           ("7","Un agente con il profilo del Product Owner prova a capire il documento prima della consegna."),
           ("8–12","Set minimo per livello; prima le cattive notizie; controllo di completezza; pacchetto per terzi; modelli qualificati.")]),
  en=dict(card="Documents", line="What you read, and what others read.", h1="What do you read, and what not?",
    why="You read a few pages written for a manager. The agents read and check the rest.",
    how="Documents come in three levels. Yours are short, in business language, and open with the bad news: agents run on language models, which tend to please whoever is asking and to play down what went wrong. For auditors and customers there is a separate evidence pack.",
    pyr=[("Strategic","You approve: Vision, Principles, mandate","human"),("Managerial","You read and decide: one page per decision","human"),("Operational","Agents only: architecture, logs, tests","ai")],
    third="Evidence pack for third parties",
    tiles=[("alert","deny","Bad news first","Failed tests, open risks, dissent: up front."),
           ("doc","fw","One page per decision","What changed, what is asked, by when."),
           ("stamp","ai","Every claim has evidence","The reviewer checks the link."),
           ("lens","ai","An omission blocks the document","Like a failed test blocks the work.")],
    rules=[("1–6","Business language; four questions up front; changes first; one page; outcomes, not procedures; every claim with evidence."),
           ("7","An agent with the Product Owner's profile tries to understand the document before delivery."),
           ("8–12","Minimum set per level; bad news first; completeness check; evidence pack for third parties; qualified templates.")])),
 "profili": dict(icon="layers", tone="fw", spec=(9,), norm=["s9"],
  it=dict(card="Competenze", line="Dove stanno gli esperti che non hai.", h1="Dove stanno gli esperti che non hai?",
    why="Nelle competenze scritte per gli agenti, i Role Profile, verificate una volta per tutte da esperti della tua organizzazione.",
    how="Un esperto scrive o aggiorna un profilo; un LLM lo pre-valuta e può solo respingerlo; un revisore esperto, diverso dall'autore, lo pubblica. I progetti usano solo profili qualificati.",
    flow=[("pen","Un esperto scrive"),("gear","Un LLM pre-valuta"),("eye","Un revisore pubblica"),("team","I progetti usano")],
    tiles=[("building","fw","Esperti nell'organizzazione","Cloud, sicurezza, dati, test, privacy, legale."),
           ("check","ai","Suite di qualificazione","Casi a risposta nota da superare."),
           ("cycle","ai","Riqualifica a ogni modello","Il revisore guarda solo le differenze."),
           ("eye","human","Quattro occhi","Chi scrive non approva.")],
    rules=[("◆","Ogni regola di un profilo rimanda alla clausola di uno standard pubblico."),
           ("◆","Un profilo non riqualificato entro il termine viene sospeso."),
           ("◆","Le stesse regole valgono per i modelli di documento e per la checklist del gate.")]),
  en=dict(card="Expertise", line="Where the experts you lack live.", h1="Where are the experts you do not have?",
    why="In the expertise written for agents, the Role Profiles, checked once and for all by experts in your organisation.",
    how="An expert writes or updates a profile; an LLM pre-assesses it and can only reject it; an expert reviewer, not the author, publishes it. Projects use qualified profiles only.",
    flow=[("pen","An expert writes"),("gear","An LLM pre-assesses"),("eye","A reviewer publishes"),("team","Projects use it")],
    tiles=[("building","fw","Experts in the organisation","Cloud, security, data, testing, privacy, legal."),
           ("check","ai","Qualification suite","Known-answer cases to pass."),
           ("cycle","ai","Requalified for every model","The reviewer looks only at differences."),
           ("eye","human","Four eyes","Whoever writes does not approve.")],
    rules=[("◆","Every rule in a profile points to a clause of a public standard."),
           ("◆","A profile not requalified on time is suspended."),
           ("◆","The same rules apply to document templates and to the gate checklist.")])),
 "sicurezza": dict(icon="lock", tone="ai", spec=(7,), norm=["s7"],
  it=dict(card="Sicurezza", line="Che cosa resta tuo e che cosa esce.", h1="Che cosa resta tuo, e che cosa esce?",
    why="Stato, registri, codice e segreti restano nel tuo ambiente. Escono solo i dati che il mandato autorizza, verso i motori AI ammessi.",
    how="Ciò che è vietato deve bloccarlo l'ambiente, non l'agente. Ogni esecuzione è registrata e si può riprendere dopo un'interruzione senza fare due volte la stessa cosa.",
    inside="Resta nel tuo ambiente", inside_items=["Stato e registri","Codice e repository","Segreti e credenziali"],
    outside="Esce solo se autorizzato", outside_items=["Prompt verso motori ammessi","Dati della classe consentita","Connettori previsti dal mandato"],
    tiles=[("shield","ai","Istruzioni ostili bloccate","Un input malevolo deve produrre un blocco registrato."),
           ("log","fw","Tutto registrato","Profilo, modello esatto, configurazione e costo di ogni esecuzione."),
           ("lock","fw","Segreti protetti","Nel deposito credenziali della piattaforma."),
           ("cycle","ai","Ripresa pulita","Dopo un'interruzione si riconcilia prima di ripartire.")],
    rules=[("◆","La Security Risk Posture ha una sezione Agenti: strumenti, destinazioni, dati e azioni irreversibili per ruolo."),
           ("◆","Il prodotto include una SBOM; l'obiettivo è la tracciabilità."),
           ("◆","Il mandato contiene la tabella delle classi di dati per fornitore.")]),
  en=dict(card="Security", line="What stays yours and what goes out.", h1="What stays yours, and what goes out?",
    why="State, logs, code and secrets stay in your environment. Only the data the mandate authorises goes out, to approved AI engines.",
    how="What is forbidden must be blocked by the environment, not by the agent. Every run is recorded and can resume after an interruption without doing the same thing twice.",
    inside="Stays in your environment", inside_items=["State and logs","Code and repository","Secrets and credentials"],
    outside="Goes out only if authorised", outside_items=["Prompts to approved engines","Data of the allowed class","Connectors in the mandate"],
    tiles=[("shield","ai","Hostile instructions blocked","Malicious input must produce a recorded block."),
           ("log","fw","Everything recorded","Profile, exact model, configuration and cost of every run."),
           ("lock","fw","Secrets protected","In the platform's credential store."),
           ("cycle","ai","Clean recovery","After an interruption, reconcile before restarting.")],
    rules=[("◆","The Security Risk Posture has an Agents section: tools, destinations, data and irreversible actions per role."),
           ("◆","The product includes an SBOM; the goal is traceability."),
           ("◆","The mandate contains the table of data classes per provider.")])),
}

SLUG["originalita"] = ("originalita", "originality")
UI["it"]["footnav"].insert(1, ("originalita", "Che cosa c'è di nuovo"))
UI["en"]["footnav"].insert(1, ("originalita", "What's new about it"))

SRC = {
    "bezos": ("Amazon, lettera agli azionisti 2015 (J. Bezos)", "Amazon, 2015 letter to shareholders (J. Bezos)", "https://s2.q4cdn.com/299287126/files/doc_financials/annual/2015-Letter-to-Shareholders.PDF"),
    "autonomy": ("Feng, McDonald, Zhang · Levels of Autonomy for AI Agents · arXiv 2506.12469", None, "https://arxiv.org/abs/2506.12469"),
    "slsa": ("SLSA · Verifying artifacts", None, "https://slsa.dev/spec/v1.2/verifying-artifacts"),
    "sase": ("Hassan et al. · Agentic Software Engineering (SASE) · arXiv 2509.06216", None, "https://arxiv.org/abs/2509.06216"),
    "monkeys": ("Brown et al. · Large Language Monkeys · arXiv 2407.21787", None, "https://arxiv.org/abs/2407.21787"),
    "cop": ("Erol et al. · Cost-of-Pass · arXiv 2504.13359", None, "https://arxiv.org/abs/2504.13359"),
}

ORIG = {
    "it": dict(
        card="Che cosa c'è di nuovo", line="Che cosa è nostro e che cosa riprendiamo da altri.",
        title="Che cosa c'è di nuovo · Eiraman", h1="Che cosa c'è di nuovo in Eiraman?",
        why="Chi conosce il business oggi non ha un metodo per governare l'AI che costruisce per lui. Eiraman nasce per questo.",
        how_h="Come: mattoni già noti, messi insieme", how_p="Quasi ogni meccanismo di Eiraman esiste già altrove. Li citiamo, e li combiniamo per un destinatario preciso.",
        bricks=[("door2", "Delega per reversibilità", "Le scelte che si possono annullare restano agli agenti.", ["bezos", "autonomy"]),
                ("stamp", "Prova legata alla versione", "Si accetta solo ciò che corrisponde alla versione verificata.", ["slsa", "sase"]),
                ("layers", "Più candidate e un selettore", "Generare più proposte serve solo se qualcuno sa scegliere.", ["monkeys"]),
                ("coin", "Costo per risultato accettato", "Il costo vero include i tentativi falliti.", ["cop"]),
                ("steps", "Livelli a zone", "Più rischio, più requisiti: come la governance a zone delle piattaforme low-code.", []),
                ("team", "AI Squad con ruoli", "Lo sviluppo come lavoro organizzato tra agenti e persone.", ["sase"])],
        own_h="Che cosa porta di proprio", own_p="Nelle fonti che abbiamo consultato non abbiamo trovato questi tre elementi. Restano da provare.",
        own=[("nospec", "La competenza sta nei profili, non in ogni progetto", "Eiraman non sostituisce chi sviluppa: ne sposta la competenza in profili qualificati dall'organizzazione, che guidano gli agenti."),
             ("check", "Due accettazioni distinte", "Si accetta il software e, separatamente, ciò che il software produce."),
             ("shield", "Un perimetro guidato dalle norme UE", "AI Act, GDPR, NIS2 e Cyber Resilience Act decidono fin dove si può costruire quando la competenza sta nei profili, non in ogni progetto.")],
        not_h="Che cosa non rivendichiamo",
        not_list=["La delega per reversibilità non è un'invenzione nostra.", "Il costo per risultato accettato non è un'invenzione nostra.", "La concorrenza tra più candidate non è un'invenzione nostra.", "La prova legata alla versione non è un'invenzione nostra."],
        proof_h="Stato delle prove", proof_p="Per ora c'è un solo pilota in corso e nessun confronto controllato. I risultati, buoni o cattivi, saranno pubblicati nella pagina dei dati.",
        proof_btn="Vedi i dati del pilota", src_lbl="Fonti di ispirazione"),
    "en": dict(
        card="What's new about it", line="What is ours and what we take from others.",
        title="What's new about it · Eiraman", h1="What is new about Eiraman?",
        why="Those who know the business have no method today to govern the AI that builds for them. Eiraman exists for them.",
        how_h="How: known building blocks, put together", how_p="Almost every mechanism in Eiraman already exists elsewhere. We cite them and combine them for a specific audience.",
        bricks=[("door2", "Delegation by reversibility", "Choices that can be undone stay with the agents.", ["bezos", "autonomy"]),
                ("stamp", "Evidence tied to the version", "Only what matches the verified version is accepted.", ["slsa", "sase"]),
                ("layers", "Several candidates and a selector", "Generating more proposals helps only if someone can choose.", ["monkeys"]),
                ("coin", "Cost per accepted result", "The real cost includes the failed attempts.", ["cop"]),
                ("steps", "Levels as zones", "More risk, more requirements: like zone-based governance on low-code platforms.", []),
                ("team", "Agent teams with roles", "Development as organised work between agents and people.", ["sase"])],
        own_h="What it brings of its own", own_p="We did not find these three elements in the sources we reviewed. They still have to be proven.",
        own=[("nospec", "Competence lives in profiles, not in every project", "Eiraman does not replace those who develop software: it moves their competence into profiles qualified by the organisation, which guide the agents."),
             ("check", "Two separate acceptances", "You accept the software and, separately, what the software produces."),
             ("shield", "A scope driven by EU rules", "The AI Act, GDPR, NIS2 and the Cyber Resilience Act decide how far you can build when competence lives in the profiles, not in every project.")],
        not_h="What we do not claim",
        not_list=["Delegation by reversibility is not our invention.", "Cost per accepted result is not our invention.", "Competition between candidates is not our invention.", "Evidence tied to the version is not our invention."],
        proof_h="State of the evidence", proof_p="For now there is a single pilot under way and no controlled comparison. Results, good or bad, will be published on the data page.",
        proof_btn="Projects developed with the method", src_lbl="Sources of inspiration"),
}

# =====================================================================
# Aggiornamento alla specifica 0.3: management tradizionale applicato all'AI,
# AI Squad e Scrum, architettura componibile, scoperta con Design Thinking, DevSecOps.
# =====================================================================
for lang, lab in (("it", "Specifica 0.3"), ("en", "Specification 0.3")):
    UI[lang]["footnav"] = [(k, (lab if k == "specifica" else v)) for k, v in UI[lang]["footnav"]]
UI["it"]["origin"] = "Dal management"
UI["en"]["origin"] = "From management"
UI["it"]["see"] = "Vedi anche"
UI["en"]["see"] = "See also"

ORDER[:] = ["principi", "ruoli", "squadre", "fasi", "scoperta", "architettura", "decisioni", "qualita", "ritmo", "livelli", "documenti", "profili", "sicurezza"]
SLUG.update({"squadre": ("squadre", "teams"), "architettura": ("architettura", "architecture"), "scoperta": ("scoperta", "discovery")})

HOME["it"].update(
    title="Eiraman · Governa l'AI come governi un'organizzazione",
    desc="Eiraman applica all'AI le pratiche di management che già conosci: obiettivi, deleghe, squadre, revisioni.",
    h1="Chi ha l'idea deve restarne padrone, anche senza leggere il codice.",
    sub="Oggi l'AI costruisce software. Eiraman lascia le decisioni a chi conosce il business.",
    prob=[("nospec", "Nessun team di sviluppo", "Molte idee nascono dove non ci sono programmatori."),
          ("eye", "Controlli che nessuno legge", "Cento approvazioni tecniche non sono governo."),
          ("coin", "Costi e rischi invisibili", "Senza misure, l'AI sembra gratis e sicura.")],
    bridge_tag="Il management che conosci", bridge_h="Stessi strumenti, nuova squadra.",
    bridges=[("target", "Obiettivi", "Mandato"), ("door1", "Delega", "Porte a una e due vie"),
             ("team", "Squadre", "AI Squad"), ("calendar", "Revisioni", "Una pagina a settimana")])
HOME["en"].update(
    title="Eiraman · Govern AI the way you govern an organisation",
    desc="Eiraman applies the management practices you already know to AI: objectives, delegation, teams, reviews.",
    h1="Whoever has the idea should stay in charge of it, even without reading code.",
    sub="AI now builds software. Eiraman leaves the decisions to those who know the business.",
    bridge_tag="The management you know", bridge_h="Same tools, a new team.",
    bridges=[("target", "Objectives", "Mandate"), ("door1", "Delegation", "One-way and two-way doors"),
             ("team", "Teams", "AI Squads"), ("calendar", "Reviews", "One page a week")])

METHOD["it"].update(
    why="Eiraman riparte dal management tradizionale e lo applica all'AI: chi decide governa gli agenti come governa un'organizzazione.",
    explore_p="Tredici parti, dalla più semplice alla più tecnica. Ognuna parte dal perché e dalla pratica di management da cui nasce.",
    ref=[("specifica", "doc", "La specifica 0.3", "Il testo normativo completo, sezione per sezione.")] + METHOD["it"]["ref"][1:],
    mg_h="Le pratiche di management che Eiraman applica all'AI",
    mg_p="Ogni regola del metodo traspone una pratica nota. Cambia solo ciò che serve, perché chi esegue è un agente.",
    mg=[("target", "Obiettivi e mandato", "Mandato, Visione, criteri misurati", "fasi"),
        ("door1", "Delega e RACI", "Porte a una e due vie, il silenzio non approva", "decisioni"),
        ("pyramid", "Organigramma e staff planning", "Piramide delle AI Squad, Unit Cost", "squadre"),
        ("team", "Scrum e Scrum of Scrums", "Squadre per pacchetto, Scrum Master AI", "squadre"),
        ("bulb", "Design Thinking", "Più modelli divergono, un analista converge", "scoperta"),
        ("spine", "Architettura d'impresa e componibile", "Backbone, Brain, interfacce, Hairs", "architettura"),
        ("steps", "Gestione di scope e rischi", "Livelli di applicabilità, Risk Log", "livelli"),
        ("scale", "Controllo indipendente", "Chiusura su prova, giudici di altri modelli", "qualita"),
        ("doc", "Reporting al management", "Prima le cattive notizie, completezza verificata", "documenti"),
        ("shield", "DevSecOps", "Git leggibile, test automatici, sicurezza dal progetto", "qualita")],
    note="Le pagine seguono lo schema Perché, Come, Cosa (S. Sinek, Start with Why, 2009). TOGAF®, Scrum e Design Thinking sono citati come pratiche di riferimento.")
METHOD["en"].update(
    why="Eiraman starts again from traditional management and applies it to AI: whoever decides governs agents the way they govern an organisation.",
    explore_p="Thirteen parts, from the simplest to the most technical. Each starts from the why and from the management practice it comes from.",
    ref=[("specifica", "doc", "Specification 0.3", "The full normative text, section by section.")] + METHOD["en"]["ref"][1:],
    mg_h="The management practices Eiraman applies to AI",
    mg_p="Every rule of the method transposes a known practice. Only what must change changes, because the one executing is an agent.",
    mg=[("target", "Objectives and mandate", "Mandate, Vision, measured criteria", "fasi"),
        ("door1", "Delegation and RACI", "One-way and two-way doors, silence never approves", "decisioni"),
        ("pyramid", "Organisation chart and staff planning", "Pyramid of AI Squads, Unit Cost", "squadre"),
        ("team", "Scrum and Scrum of Scrums", "Teams per package, AI Scrum Master", "squadre"),
        ("bulb", "Design Thinking", "Several models diverge, one analyst converges", "scoperta"),
        ("spine", "Enterprise and composable architecture", "Backbone, Brain, interfaces, Hairs", "architettura"),
        ("steps", "Scope and risk management", "Applicability levels, Risk Log", "livelli"),
        ("scale", "Independent control", "Closure on evidence, judges on other models", "qualita"),
        ("doc", "Management reporting", "Bad news first, completeness checked", "documenti"),
        ("shield", "DevSecOps", "Readable Git, automated tests, security from the design", "qualita")],
    note="Pages follow the Why, How, What pattern (S. Sinek, Start with Why, 2009). TOGAF®, Scrum and Design Thinking are cited as reference practices.")

ORIGINS = {
    "principi": ("Governo per obiettivi e principi", "Governance by objectives and principles"),
    "ruoli": ("Organigramma e matrice RACI", "Organisation chart and RACI matrix"),
    "squadre": ("Scrum, staff planning e seniority", "Scrum, staff planning and seniority"),
    "fasi": ("Ciclo di vita del progetto", "Project life cycle"),
    "scoperta": ("Design Thinking", "Design Thinking"),
    "architettura": ("Architettura d'impresa (TOGAF) e Composable Architecture", "Enterprise architecture (TOGAF) and Composable Architecture"),
    "decisioni": ("Delega e matrice RACI", "Delegation and RACI matrix"),
    "qualita": ("Controllo indipendente della qualità e DevSecOps", "Independent quality control and DevSecOps"),
    "ritmo": ("Reporting e ciclo di governo", "Reporting and governance cycle"),
    "livelli": ("Gestione del rischio", "Risk management"),
    "documenti": ("Reporting al management", "Management reporting"),
    "profili": ("Gestione e certificazione delle competenze", "Competence management and certification"),
    "sicurezza": ("Security by Design e gestione del rischio IT", "Security by Design and IT risk management"),
}

COMP["squadre"] = dict(icon="pyramid", tone="ai", spec=("4bis",), norm=["s4bis"],
  it=dict(card="AI Squad e Scrum", line="Come si organizzano gli agenti.", h1="Come si organizza un'AI Squad?",
    why="Come in un'azienda: ruoli diversi, una squadra per ogni pacchetto di lavoro, un responsabile che coordina e una retrospettiva che migliora la squadra.",
    how="Il Coordinatore AI forma una squadra per ogni pacchetto, con uno Scrum Master AI che la coordina e gli rende conto. Niente Sprint: i limiti sono costo, contesto e quote, non le ore delle persone.",
    pyr=[("Coordinatore AI, analisti, architetti", "Personas con un profilo professionale", "fw"),
         ("Scrum Master AI, revisori", "Coordinano e verificano", "ai"),
         ("Esecutori, unit tester", "Ruoli molto automatizzati", "ai")],
    pyr_note="Ogni ruolo ha uno Unit Cost, anche sui motori locali.",
    flow=[("doc", "Pacchetto di lavoro"), ("team", "Squadra con Scrum Master AI"), ("log", "Report"), ("manager", "Coordinatore AI"), ("cycle", "Retrospettiva")],
    tiles=[("team", "ai", "Contesto condiviso", "Tranne il tester, che non vede la discussione."),
           ("layers", "ai", "Squadre in concorrenza", "Solo per lavori generativi complessi, con un giudice."),
           ("gear", "fw", "Mode e Role", "Ogni ruolo segue le linee guida del fornitore del modello."),
           ("cycle", "human", "Retrospettiva", "Migliora la composizione; le Decisioni restano tue.")],
    rules=[("1", "Una squadra per Work Package, con i ruoli necessari, fino alle squad dello Staff Planning."),
           ("2", "Lo Scrum Master AI coordina, tiene il Log Tracker e consegna un report sul template del Coordinatore AI."),
           ("3", "Lo unit tester non vede la discussione; per sicurezza e dati personali usa un modello diverso."),
           ("4", "Il Coordinatore AI valida tecnica e conformità e chiude la Wave dopo l'incremento integrato."),
           ("5", "I risparmi entro tolleranza si applicano da soli; il cambio di una Decisione torna a te con la SWOT.")]),
  en=dict(card="AI Squads and Scrum", line="How agents are organised.", h1="How is an AI Squad organised?",
    why="As in a company: different roles, one team per work package, a lead who coordinates and a retrospective that improves the team.",
    how="The AI Coordinator forms a team for each package, with an AI Scrum Master who coordinates it and reports back. No Sprints: the limits are cost, context and quotas, not people's hours.",
    pyr=[("AI Coordinator, analysts, architects", "Personas with a professional profile", "fw"),
         ("AI Scrum Master, reviewers", "Coordinate and verify", "ai"),
         ("Executors, unit testers", "Highly automated roles", "ai")],
    pyr_note="Every role has a Unit Cost, local engines included.",
    flow=[("doc", "Work package"), ("team", "Team with AI Scrum Master"), ("log", "Report"), ("manager", "AI Coordinator"), ("cycle", "Retrospective")],
    tiles=[("team", "ai", "Shared context", "Except the tester, who does not see the discussion."),
           ("layers", "ai", "Competing teams", "Only for complex generative work, with a judge."),
           ("gear", "fw", "Mode and Role", "Each role follows the model provider's guidelines."),
           ("cycle", "human", "Retrospective", "Improves the composition; Decisions stay yours.")],
    rules=[("1", "One team per Work Package, with the roles needed, up to the squads of the Staff Planning."),
           ("2", "The AI Scrum Master coordinates, keeps the Log Tracker and delivers a report on the AI Coordinator's template."),
           ("3", "The unit tester does not see the discussion; for security and personal data it uses a different model."),
           ("4", "The AI Coordinator validates technique and compliance and closes the Wave after the integrated increment."),
           ("5", "Savings within tolerance apply on their own; changing a Decision comes back to you with a SWOT.")]))

COMP["architettura"] = dict(icon="spine", tone="fw", spec=("6bis",), norm=["s6bis"],
  it=dict(card="Architettura componibile", line="Prima l'essenziale, poi il resto.", h1="In che ordine si costruisce un'applicazione?",
    why="Con l'AI aggiungere pezzi è facile: senza un ordine si costruisce un patchwork. Come un buon architetto d'impresa, Eiraman parte dall'essenziale.",
    how="L'applicazione si scompone in componenti per funzione, come un corpo: prima la spina dorsale, poi il cervello, poi mani, piedi, occhi e orecchie, infine i capelli, che si possono tagliare.",
    body=[("spine", "Backbone", "Il nucleo, per primo"), ("brain", "Brain", "La logica e i motori AI"), ("hand", "Hands, Foot, Eyes, Ears", "Le interfacce"), ("feather", "Hairs", "Le funzioni periferiche")],
    tiles=[("shield", "ai", "Trusted e untrusted", "I compiti del Brain non fidati hanno un controllo deterministico."),
           ("layers", "fw", "Backlog etichettato", "Ogni workstream porta componente e priorità."),
           ("gear", "fw", "Motore locale o esterno", "Richieste piccole in locale, una richiesta unica all'esterno."),
           ("alert", "deny", "Niente patchwork", "Le interfacce avanzate solo su un nucleo stabile.")],
    rules=[("1", "Backbone per primo: copre in forma minima i percorsi principali del risultato."),
           ("2", "Brain: i compiti si classificano trusted o untrusted; da qui dipende che cosa si delega."),
           ("3", "Interfacce: presto in forma essenziale, in forma avanzata solo dopo Backbone e Brain."),
           ("4", "Hairs: si aggiungono o si tolgono in ogni momento, verificando la regressione del nucleo."),
           ("5", "Il documento architetturale segue le viste TOGAF e misura la scelta tra motore locale ed esterno.")]),
  en=dict(card="Composable architecture", line="The essentials first, then the rest.", h1="In what order is an application built?",
    why="With AI, adding pieces is easy: without an order you build a patchwork. Like a good enterprise architect, Eiraman starts from the essentials.",
    how="The application is broken into components by function, like a body: first the backbone, then the brain, then hands, feet, eyes and ears, and finally the hair, which can be cut.",
    body=[("spine", "Backbone", "The core, first"), ("brain", "Brain", "Logic and AI engines"), ("hand", "Hands, Foot, Eyes, Ears", "The interfaces"), ("feather", "Hairs", "Peripheral functions")],
    tiles=[("shield", "ai", "Trusted and untrusted", "Untrusted Brain tasks get a deterministic check."),
           ("layers", "fw", "Labelled backlog", "Each workstream carries its component and priority."),
           ("gear", "fw", "Local or external engine", "Small requests locally, a single request externally."),
           ("alert", "deny", "No patchwork", "Advanced interfaces only on a stable core.")],
    rules=[("1", "Backbone first: it covers, in minimal form, the main paths of the result."),
           ("2", "Brain: tasks are classed trusted or untrusted; this decides what is delegated."),
           ("3", "Interfaces: early in essential form, in advanced form only after Backbone and Brain."),
           ("4", "Hairs: added or removed at any time, checking the core's regression."),
           ("5", "The architecture document follows the TOGAF views and measures the choice between local and external engines.")]))

COMP["scoperta"] = dict(icon="bulb", tone="ai", spec=(5,), norm=["design-thinking-affidato-all-ai-fase-1"], norm_en=["design-thinking-delegated-to-ai-phase-1"],
  it=dict(card="Scoperta con il Design Thinking", line="Molte idee, poi una sola Visione.", h1="Come nasce un'idea condivisa?",
    why="Come in un workshop di Design Thinking: prima si aprono le idee, poi si converge. Le macchine però non hanno buon senso, quindi servono confini chiari.",
    how="Più modelli, ognuno con un ruolo, esplorano il problema in modo indipendente. Tu puoi intervenire a momenti fissi. Poi un analista raccoglie, sceglie e scrive la prima Visione.",
    flow=[("diverge", "Divergenza tra più modelli"), ("manager", "I tuoi spunti, a gate fissi"), ("funnel", "Convergenza dell'analista"), ("flag", "Bozza di Visione e scope")],
    tiles=[("alert", "deny", "Guardrail", "Numero di giri, fonti e dati ammessi, criteri per scartare."),
           ("team", "ai", "Ruoli definiti", "Ogni modello ha un ruolo e un comportamento."),
           ("lens", "ai", "Evidenze degli utenti", "L'analista riconduce le idee a ciò che gli utenti vivono."),
           ("check", "human", "Decidi tu", "Approvi la Visione o rilanci l'esplorazione.")],
    rules=[("1", "Divergenza: più modelli con ruoli definiti generano ipotesi, problemi, benefici e principi."),
           ("2", "Gate: in momenti prefissati il Manager umano aggiunge spunti, che rilanciano la divergenza."),
           ("3", "Convergenza: un solo analista raccoglie, rivede e produce la bozza di Visione e dello Scope Management."),
           ("4", "Il Manager umano approva la Visione oppure rilancia l'esplorazione.")]),
  en=dict(card="Discovery with Design Thinking", line="Many ideas, then one Vision.", h1="How does a shared idea take shape?",
    why="As in a Design Thinking workshop: first ideas open up, then they converge. Machines have no common sense, though, so clear boundaries are needed.",
    how="Several models, each with a role, explore the problem independently. You can step in at fixed moments. Then an analyst gathers, chooses and writes the first Vision.",
    flow=[("diverge", "Divergence across models"), ("manager", "Your inputs, at fixed gates"), ("funnel", "Analyst's convergence"), ("flag", "Draft Vision and scope")],
    tiles=[("alert", "deny", "Guardrails", "Number of rounds, permitted sources and data, criteria for discarding."),
           ("team", "ai", "Defined roles", "Each model has a role and a behaviour."),
           ("lens", "ai", "User evidence", "The analyst relates ideas to what users actually experience."),
           ("check", "human", "You decide", "You approve the Vision or relaunch the exploration.")],
    rules=[("1", "Divergence: several models with defined roles generate hypotheses, problems, benefits and principles."),
           ("2", "Gates: at predefined moments the Human Manager adds inputs, which relaunch divergence."),
           ("3", "Convergence: a single analyst gathers, reviews and produces the draft Vision and Scope Management."),
           ("4", "The Human Manager approves the Vision or relaunches the exploration.")]))

# Qualità: i 4 tipi di test DevSecOps
COMP["qualita"]["norm"] = ["s4", "chiusura", "devsecops-e-test"]
COMP["qualita"]["norm_en"] = ["s4", "closure", "devsecops-and-tests"]
COMP["qualita"]["it"]["tests_h"] = "I quattro tipi di test (DevSecOps)"
COMP["qualita"]["it"]["tests"] = [("gear", "ai", "Unit test", "A fine pacchetto, dal tester indipendente; aggiornano sicurezza e prestazioni."),
    ("log", "ai", "Funzionale con script", "L'agente lancia lo script e registra i log; corregge da solo gli errori banali."),
    ("person", "ai", "Funzionale con utente simulato", "Un agente usa l'applicazione come una persona."),
    ("check", "human", "Collaudo (UAT)", "Una persona svolge il compito; l'AI registra.")]
COMP["qualita"]["en"]["tests_h"] = "The four kinds of test (DevSecOps)"
COMP["qualita"]["en"]["tests"] = [("gear", "ai", "Unit test", "At the end of a package, by the independent tester; they update security and performance."),
    ("log", "ai", "Functional with script", "The agent runs the script and records the logs; it fixes trivial errors itself."),
    ("person", "ai", "Functional with simulated user", "An agent uses the application as a person would."),
    ("check", "human", "Acceptance (UAT)", "A person performs the task; the AI records.")]
COMP["qualita"]["see"] = ["squadre"]
COMP["fasi"]["see"] = ["scoperta", "architettura", "qualita"]
COMP["decisioni"]["see"] = ["ruoli", "ritmo"]

ORIG["it"].update(
    why="Chi conosce il business sa già governare persone, progetti e fornitori. Eiraman nasce per fargli governare l'AI con gli stessi strumenti.",
    own_p="La novità non è un meccanismo tecnico: è la trasposizione sistematica del management tradizionale al governo degli agenti, per chi conosce il business. La ricerca di anteriorità su questo punto è ancora in corso. Resta da provare.",
    own=[("bridge", "Il management, trasposto agli agenti", "Ogni regola nasce da una pratica di management nota: obiettivi, delega, squadre, revisioni, gestione del rischio."),
         ("nospec", "La competenza sta nei profili, non in ogni progetto", "Eiraman non sostituisce chi sviluppa: ne sposta la competenza in profili qualificati dall'organizzazione; il perimetro segue le norme UE."),
         ("check", "Due accettazioni distinte", "Si accetta il software e, separatamente, ciò che il software produce.")])
ORIG["en"].update(
    why="Those who know the business already know how to govern people, projects and suppliers. Eiraman exists so they can govern AI with the same tools.",
    own_p="The novelty is not a technical mechanism: it is the systematic transposition of traditional management to the governance of agents, for those who know the business. The prior-art search on this point is still in progress. It still has to be proven.",
    own=[("bridge", "Management, transposed to agents", "Every rule comes from a known management practice: objectives, delegation, teams, reviews, risk management."),
         ("nospec", "Competence lives in profiles, not in every project", "Eiraman does not replace those who develop software: it moves their competence into profiles qualified by the organisation; the scope follows EU rules."),
         ("check", "Two separate acceptances", "You accept the software and, separately, what the software produces.")])

# Home: entro ~200 parole visibili
HOME["it"].update(
    sub="Per imprenditori, manager e uffici senza programmatori: gli strumenti di management che già usi, applicati alle squadre di AI.",
    prob=[("nospec", "Nessun team di sviluppo", "Le idee nascono dove mancano programmatori."),
          ("eye", "Controlli che nessuno legge", "Cento approvazioni tecniche non sono governo."),
          ("coin", "Costi e rischi invisibili", "Senza misure, l'AI sembra gratis.")],
    stairs_note="Un gradino alla volta.")
HOME["en"].update(
    sub="For business owners, managers and teams without programmers: the management tools you already use, applied to AI Squads.",
    prob=[("nospec", "No development team", "Ideas start where programmers are missing."),
          ("eye", "Checks nobody reads", "A hundred technical approvals are not governance."),
          ("coin", "Hidden costs and risks", "Without measures, AI looks free.")],
    stairs_note="One step at a time.")
HOME["it"].update(
    sub="Per imprenditori, manager e uffici senza programmatori: il management che già usi, applicato all'AI.",
    prob=[("nospec", "Nessun team di sviluppo", "Mancano programmatori."),
          ("eye", "Controlli che nessuno legge", "Approvare non è governare."),
          ("coin", "Costi e rischi invisibili", "L'AI sembra gratis.")],
    how=[("pen", "human", "Decidi prima", "Obiettivo, budget e limiti."),
         ("team", "ai", "L'AI esegue", "Agenti che costruiscono e si controllano."),
         ("stamp", "ai", "Le prove dimostrano", "Finito vuol dire provato.")],
    who2=[("gear", "Progetta e costruisce"), ("scale", "Si fa controllare da altri agenti"), ("doc", "Ti porta solo scelte di business")],
    what_tag="Che cosa",
    stairs=[("person", "0", "Per me", "Strumenti personali."), ("group", "1", "Per il mio team", "Colleghi."), ("globe", "2", "Per i clienti", "Utenti esterni.")],
    out=("lock", "Fuori", "Dati sanitari, pagamenti nel codice, AI ad alto rischio."))
HOME["en"].update(
    sub="For business owners, managers and teams without programmers: the management you already use, applied to AI.",
    prob=[("nospec", "No development team", "No programmers."),
          ("eye", "Checks nobody reads", "Approving is not governing."),
          ("coin", "Hidden costs and risks", "AI looks free.")],
    how=[("pen", "human", "Decide first", "Goal, budget and limits."),
         ("team", "ai", "AI executes", "Agents that build and check themselves."),
         ("stamp", "ai", "Evidence proves", "Finished means proven.")],
    who2=[("gear", "Designs and builds"), ("scale", "Gets checked by other agents"), ("doc", "Brings you business choices only")],
    what_tag="What",
    stairs=[("person", "0", "For me", "Personal tools."), ("group", "1", "For my team", "Colleagues."), ("globe", "2", "For customers", "External users.")],
    out=("lock", "Out", "Health data, payments in the code, high-risk AI."))

HOME["it"]["stairs_note"] = "Un gradino per volta."
HOME["it"]["who_h"] = "Chi fa cosa?"
HOME["en"]["stairs_note"] = "Step by step."

HOME["it"]["how_h"] = "Tre tempi, sempre uguali."
HOME["it"]["invite"] = "Che cosa contiene il metodo?"
HOME["it"]["stairs_note"] = "Passo dopo passo."

# ---------- pagina Autore e comunità (biografia approvata dall'Autore) ----------
SLUG["chi"] = ("chi-sono", "about")
UI["it"]["footnav"].append(("chi", "Autore e comunità"))
UI["en"]["footnav"].append(("chi", "Author & community"))
ABOUT = {
 "it": dict(title="Autore e comunità · Eiraman", crumb="Autore e comunità",
   desc="Paolo Ungari, autore di Eiraman, e la comunità del progetto: governance, gruppi di lavoro, come contribuire, codice di condotta e licenze.",
   name="Paolo Ungari", role="Technology Strategy & Applied AI Leader · Roma",
   why_h="Perché Eiraman",
   why="Ho passato la carriera a far lavorare insieme persone, architetture e contratti. Ho guidato practice cloud, team di prevendita e di delivery, progetti dalla vendita all'esercizio. Eiraman nasce da qui: applicare all'intelligenza artificiale gli strumenti di management che ho usato ogni giorno con le persone.",
   path_h="Percorso",
   path=[("building", "Oggi", "Progetto soluzioni di AI applicata e promuovo l'uso dell'AI nel lavoro tecnico e commerciale."),
         ("steps", "In passato", "Ho guidato una practice cloud nazionale, ho portato un team da 5 a 35 persone, ho coordinato prevendite oltre i 10 milioni di euro e ho lavorato come solution architect su outsourcing, cloud ed enterprise architecture.")],
   edu_h="Formazione e certificazioni",
   edu=[("bulb", "Formazione", "Laurea in Ingegneria elettrica, MBA all'Università di Roma Tor Vergata, Master in Innovazione e Trasformazione Digitale nella PA. Executive education a Oxford Saïd Business School e MIT Sloan («Artificial Intelligence: Implications for Business Strategy»)."),
        ("stamp", "Certificazioni", "ITIL 4 Master, Scrum Master, Scrum Product Owner, architetto cloud su AWS, Google Cloud e Azure.")],
   alt="Paolo Ungari", li="Profilo LinkedIn", back="Esplora il metodo", teaser="Chi c'è dietro Eiraman e come partecipare"),
 "en": dict(title="Author & community · Eiraman", crumb="Author & community",
   desc="Paolo Ungari, author of Eiraman, and the project community: governance, working groups, how to contribute, code of conduct and licences.",
   name="Paolo Ungari", role="Technology Strategy & Applied AI Leader · Rome",
   why_h="Why Eiraman",
   why="I have spent my career making people, architectures and contracts work together. I have led cloud practices, presales and delivery teams, and projects from sale to operation. Eiraman comes from there: applying to artificial intelligence the management tools I have used every day with people.",
   path_h="Path",
   path=[("building", "Today", "I design applied AI solutions and promote the use of AI in technical and commercial work."),
         ("steps", "Previously", "I led a national cloud practice, grew a team from 5 to 35 people, coordinated presales above €10 million, and worked as a solution architect on outsourcing, cloud and enterprise architecture.")],
   edu_h="Education and certifications",
   edu=[("bulb", "Education", "Degree in Electrical Engineering, MBA at the University of Rome Tor Vergata, Master in Innovation and Digital Transformation in Public Administration. Executive education at Oxford Saïd Business School and MIT Sloan (\"Artificial Intelligence: Implications for Business Strategy\")."),
        ("stamp", "Certifications", "ITIL 4 Master, Scrum Master, Scrum Product Owner, cloud architect on AWS, Google Cloud and Azure.")],
   alt="Paolo Ungari", li="LinkedIn profile", back="Explore the method", teaser="Who is behind Eiraman, and how to take part"),
}

# Sezioni della comunità. I repository sono in preparazione: i link puntano agli indirizzi previsti.
COMMUNITY_REPO = "https://github.com/eiraman/"
ABOUT["it"].update(
  author_h="L'autore",
  com_h="La comunità",
  com_p="Eiraman è un progetto aperto. La Guida, i Role Profile e gli strumenti si sviluppano in pubblico, con regole scritte su chi decide e su come si contribuisce. I documenti della comunità sono in bozza e i repository sono in preparazione.",
  gov_h="Governance a tappe",
  gov_p="Il progetto cresce in tre tappe. Si passa alla successiva quando sono raggiunte soglie scritte, annunciate in pubblico con le prove.",
  gov=[("person", "Tappa 1 · Steward indipendente", "Il fondatore è Steward e Autore, a titolo personale. Nomina i primi responsabili e revisori con motivazioni scritte e non revisiona i propri cambiamenti."),
       ("group", "Tappa 2 · Steering Committee", "I maintainer eleggono uno Steering Committee, con un seggio permanente per l'Autore. Servono, tra l'altro, gruppi di lavoro attivi, maintainer di più organizzazioni e adottanti dichiarati."),
       ("building", "Tappa 3 · Fondazione neutrale", "Progetto, marchio e repository passano a una fondazione senza scopo di lucro. L'Autore mantiene il seggio permanente e la cura editoriale della Guida.")],
  gov_link="Leggi la governance",
  wg_h="Gruppi di lavoro",
  wg=[("shield", "Gruppi di dominio", "Cloud Architecture, Security, Application & Data Architecture, Test & Quality, Privacy, Legal & Compliance. Ognuno ha un revisore titolare e un sostituto: un dominio senza revisore non pubblica profili."),
      ("team", "Gruppi di famiglia", "Azure, AWS, Databricks, FinOps, Analisi funzionale, Web design, Sviluppo. Scrivono e mantengono i Role Profile della famiglia; li pubblica il dominio competente."),
      ("gear", "Gruppi trasversali", "DevSecOps & Tooling, Adoption & Evidence, Translation & Education: strumenti e pipeline, adottanti e misure, traduzioni e formazione.")],
  wg_link="Leggi la carta dei gruppi di lavoro",
  ct_h="Come contribuire",
  ct=[("compass", "Scegli un percorso", "Autore di Role Profile, esperto di sicurezza, sviluppatore DevSecOps, adottante, traduttore, formatore, ricercatore, manager non tecnico come utente di prova."),
      ("stamp", "Firma DCO", "Ogni commit porta una riga Signed-off-by con il nome reale di chi certifica il diritto a proporlo (git commit -s). Firma sempre una persona, mai un agente."),
      ("hand", "Dichiara l'uso dell'AI", "Ogni pull request dichiara AI-Use (none, review, partial, substantial) e la persona responsabile. I commit assistiti portano una riga Assisted-by per strumento. L'uso dell'AI non è motivo di rifiuto; un contributo senza responsabile sì.")],
  ct_link="Leggi la guida per contribuire", path_link="Scegli il tuo percorso",
  coc_h="Codice di condotta",
  coc_p="Il progetto adotta il Contributor Covenant 2.1 in tutti i suoi spazi. Le segnalazioni sono riservate; nella tappa 1 le decide lo Steward con almeno un altro maintainer, mai una persona da sola.",
  coc_link="Leggi il codice di condotta",
  lic_h="Licenze",
  lic=["Testi della Guida e del sito: CC BY-SA 4.0.", "Role Profile: CC BY 4.0.", "Codice: Apache 2.0.",
       "Nome e logo Eiraman: marchio, regolato da TRADEMARK.md ed escluso dalle licenze CC e Apache."],
  lic_note="Le copie distribuite fino alla versione 0.3.x restano disponibili ai loro titolari con le licenze originali (CC BY-NC-ND 4.0 per testi e Role Profile, MIT per gli script).",
  lic_link="Leggi la politica delle licenze", tm_link="Leggi la politica del marchio",
  repos_h="Repository", repos_note="in preparazione",
)
ABOUT["en"].update(
  author_h="The author",
  com_h="The community",
  com_p="Eiraman is an open project. The Guide, the Role Profiles and the tools are developed in public, with written rules on who decides and how to contribute. The community documents are drafts and the repositories are being prepared.",
  gov_h="Staged governance",
  gov_p="The project grows in three stages. It moves to the next one when written thresholds are met, announced in public with the evidence.",
  gov=[("person", "Stage 1 · Independent Steward", "The founder acts as Steward and Author, in a personal capacity. The Steward appoints the first leads and reviewers with written reasons and does not review their own changes."),
       ("group", "Stage 2 · Steering Committee", "The maintainers elect a Steering Committee, with a permanent seat for the Author. It needs, among other things, active working groups, maintainers from several organisations and declared adopters."),
       ("building", "Stage 3 · Neutral foundation", "The project, its trademark and its repositories move to a non-profit foundation. The Author keeps the permanent seat and the editorial curation of the Guide.")],
  gov_link="Read the governance",
  wg_h="Working groups",
  wg=[("shield", "Domain groups", "Cloud Architecture, Security, Application & Data Architecture, Test & Quality, Privacy, Legal & Compliance. Each has a titular and a substitute reviewer: a domain without a reviewer cannot publish profiles."),
      ("team", "Family groups", "Azure, AWS, Databricks, FinOps, Functional Analysis, Web Design, Development. They write and maintain the Role Profiles of their family; the competent domain publishes them."),
      ("gear", "Cross-cutting groups", "DevSecOps & Tooling, Adoption & Evidence, Translation & Education: tools and pipeline, adopters and measurement, translations and training.")],
  wg_link="Read the working groups charter",
  ct_h="How to contribute",
  ct=[("compass", "Choose a pathway", "Role Profile author, security expert, DevSecOps developer, adopter, translator, trainer, researcher, non-technical manager as test user."),
      ("stamp", "DCO sign-off", "Every commit carries a Signed-off-by line with the real name of the person who certifies the right to submit it (git commit -s). A person always signs, never an agent."),
      ("hand", "Declare AI use", "Every pull request declares AI-Use (none, review, partial, substantial) and the accountable human. Assisted commits carry one Assisted-by line per tool. AI use is not a reason for rejection; an unaccountable contribution is.")],
  ct_link="Read the contributing guide", path_link="Choose your pathway",
  coc_h="Code of conduct",
  coc_p="The project adopts the Contributor Covenant 2.1 in all its spaces. Reports are handled confidentially; in Stage 1 the Steward decides with at least one other maintainer, never one person alone.",
  coc_link="Read the code of conduct",
  lic_h="Licences",
  lic=["Guide and site text: CC BY-SA 4.0.", "Role Profiles: CC BY 4.0.", "Code: Apache 2.0.",
       "Eiraman name and logo: trademark, governed by TRADEMARK.md and excluded from the CC and Apache licences."],
  lic_note="Copies distributed up to version 0.3.x remain available to their holders under their original licences (CC BY-NC-ND 4.0 for texts and Role Profiles, MIT for scripts).",
  lic_link="Read the licensing policy", tm_link="Read the trademark policy",
  repos_h="Repositories", repos_note="being prepared",
)
COMMUNITY_LINKS = dict(
  gov=COMMUNITY_REPO + "community/blob/main/GOVERNANCE.md",
  wg=COMMUNITY_REPO + "community/blob/main/WORKING-GROUPS.md",
  path=COMMUNITY_REPO + "community/blob/main/PATHWAYS.md",
  ct=COMMUNITY_REPO + ".github/blob/main/CONTRIBUTING.md",
  coc=COMMUNITY_REPO + ".github/blob/main/CODE_OF_CONDUCT.md",
  lic=COMMUNITY_REPO + "community/blob/main/LICENSING.md",
  tm=COMMUNITY_REPO + "community/blob/main/TRADEMARK.md",
)
COMMUNITY_REPOS = [("guide", "The Eiraman Guide"), ("role-profiles", "Role Profiles"), ("tools", "Tools"),
                   ("site", "Site generator"), ("community", "Governance, working groups, licensing"), (".github", "Contributing, security, code of conduct")]

# ---------- HOME-V4: framework ripensati per l'AI + settimana con quiz delle porte ----------
TM_IT = "Scrum, Design Thinking e TOGAF® appartengono ai rispettivi autori; Eiraman ne propone un adattamento agli agenti."
TM_EN = "Scrum, Design Thinking and TOGAF® belong to their respective authors; Eiraman proposes an adaptation of them to agents."
HOME4 = {
 "it": dict(
  kicker="Perché",
  h1="Chi ha l'idea deve restarne padrone, anche senza leggere il codice.",
  sub="Oggi l'AI costruisce software. Eiraman lascia le decisioni a chi conosce il business.",
  cta1="Vivi una settimana con Eiraman", cta2="I framework ripensati",
  tiles_cap="Il management che conosci, ripensato per un'AI Squad.",
  tiles=[("team", "Scrum", "AI Scrum"), ("bulb", "Design Thinking", "AI Design Thinking"), ("door1", "Delega e RACI", "Porte a una e due vie"),
         ("spine", "Architettura d'impresa", "AI Enterprise Architecture"), ("shield", "DevSecOps", "AI DevSecOps"), ("doc", "Reporting", "Una pagina a settimana")],
  fw_tag="Come", fw_h="Il management che conosci, ripensato per l'AI",
  fw_p="Stessi framework, nuova squadra.",
  keep="Cosa resta", change="Cosa cambia con gli agenti", more="Approfondisci",
  pairs=[("team", "Scrum", "AI Scrum", "Squadre e retrospettiva.", "AI Squad, senza timebox umani.", "squadre"),
         ("bulb", "Design Thinking", "AI Design Thinking", "Divergere, poi convergere.", "Più modelli esplorano, uno converge.", "scoperta"),
         ("door1", "Delega e RACI", "Porte a una e due vie", "Chi decide che cosa.", "Ciò che si annulla lo decide l'AI.", "decisioni"),
         ("spine", "Architettura d'impresa (TOGAF®)", "AI Enterprise Architecture", "Viste e priorità.", "Prima la spina, poi il cervello.", "architettura"),
         ("shield", "DevSecOps", "AI DevSecOps", "Test e sicurezza dal progetto.", "Testa chi non ha costruito.", "qualita"),
         ("doc", "Reporting al management", "Una pagina a settimana", "Si decide sui fatti.", "Prima le cattive notizie.", "documenti")],
  tm=TM_IT,
  wk_tag="Una settimana con Eiraman", wk_h="Che cosa fai tu, che cosa fa l'AI.",
  wk_note="Esempio illustrativo: i numeri non sono dati del pilota.",
  days=[("Lunedì", "human", "pen", "Scrivi il mandato", "Una pagina: obiettivo, budget, limiti."),
        ("Martedì → giovedì", "ai", "team", "L'AI Squad lavora", ""),
        ("Mercoledì", "human", "door1", "Una domanda per te: quale porta?", ""),
        ("Venerdì", "human", "doc", "Ricevi una pagina", "")],
  counters=[("12", "Wave chiuse"), ("48", "prove superate"), ("€ 23", "spesa stimata"), ("1", "scelta reversibile presa da sola")],
  q_ai="l'AI Squad", q_ai_s="Porta a due vie", q_me="tu", q_me_s="Porta a una via",
  q_ok="Giusto.", q_no="Non proprio.", q_show="Vedi la risposta",
  quiz=[("Cambiare una libreria interna", "ai", "Porta a due vie: si annulla a costo noto. Decide l'AI Squad."),
        ("Mandare i dati dei clienti a un nuovo fornitore", "me", "Porta a una via: dati personali e nuovo fornitore sono riserve del mandato. Decidi tu."),
        ("Eliminare una funzione già usata dagli utenti", "me", "Porta a una via: toglie qualcosa a chi la usa e non si annulla senza danno. Decidi tu.")],
  rev_t="Revisione del ciclo · settimana 1", rev_bad="Prima le cattive notizie",
  rev_bad_l=["1 test fallito, corretto e ripetuto.", "1 scelta in attesa di te: il nuovo fornitore."],
  rev_ok="Consegnato", rev_ok_l=["2 funzioni accettate, con prove."],
  rev_ask="Ti chiediamo", rev_ask_l=["1 decisione, entro martedì."],
  time="Il tuo tempo questa settimana: circa 30 minuti.", time_s="esempio",
  what_tag="Cosa", what_h="Fin dove arriva?",
  invite_btn="Esplora il metodo"),
 "en": dict(
  kicker="Why",
  h1="Whoever has the idea should stay in charge of it, even without reading code.",
  sub="AI now builds software. Eiraman leaves the decisions to those who know the business.",
  cta1="Live a week with Eiraman", cta2="The frameworks, rethought",
  tiles_cap="The management you know, rethought for an AI Squad.",
  tiles=[("team", "Scrum", "AI Scrum"), ("bulb", "Design Thinking", "AI Design Thinking"), ("door1", "Delegation and RACI", "One-way and two-way doors"),
         ("spine", "Enterprise architecture", "AI Enterprise Architecture"), ("shield", "DevSecOps", "AI DevSecOps"), ("doc", "Reporting", "One page a week")],
  fw_tag="How", fw_h="The management you know, rethought for AI",
  fw_p="Same frameworks, a new team.",
  keep="What stays", change="What changes with agents", more="Read more",
  pairs=[("team", "Scrum", "AI Scrum", "Teams and retrospective.", "Agent teams, no human timebox.", "squadre"),
         ("bulb", "Design Thinking", "AI Design Thinking", "Diverge, then converge.", "Several models explore, one converges.", "scoperta"),
         ("door1", "Delegation and RACI", "One-way and two-way doors", "Who decides what.", "AI decides what can be undone.", "decisioni"),
         ("spine", "Enterprise architecture (TOGAF®)", "AI Enterprise Architecture", "Views and priorities.", "Spine first, then brain.", "architettura"),
         ("shield", "DevSecOps", "AI DevSecOps", "Tests and security from the design.", "Whoever tests did not build.", "qualita"),
         ("doc", "Management reporting", "One page a week", "Decisions rest on facts.", "Bad news first.", "documenti")],
  tm=TM_EN,
  wk_tag="A week with Eiraman", wk_h="What you do, what AI does.",
  wk_note="Illustrative example: the numbers are not pilot data.",
  days=[("Monday", "human", "pen", "You write the mandate", "One page: goal, budget, limits."),
        ("Tuesday → Thursday", "ai", "team", "The AI Squad works", ""),
        ("Wednesday", "human", "door1", "A question reaches you. Which door?", ""),
        ("Friday", "human", "doc", "You receive one page", "")],
  counters=[("12", "Waves closed"), ("48", "checks passed"), ("€ 23", "estimated spend"), ("1", "reversible choice made on its own")],
  q_ai="the AI Squad", q_ai_s="Two-way door", q_me="you", q_me_s="One-way door",
  q_ok="Right.", q_no="Not quite.", q_show="See the answer",
  quiz=[("Change an internal library", "ai", "Two-way door: it can be undone at a known cost. The AI Squad decides."),
        ("Send customer data to a new provider", "me", "One-way door: personal data and a new provider are reserved in the mandate. You decide."),
        ("Remove a feature people already use", "me", "One-way door: it takes something away from users and cannot be undone without harm. You decide.")],
  rev_t="Cycle review · week 1", rev_bad="Bad news first",
  rev_bad_l=["1 test failed, fixed and rerun.", "1 choice waiting for you: the new provider."],
  rev_ok="Delivered", rev_ok_l=["2 features accepted, with evidence."],
  rev_ask="We ask you", rev_ask_l=["1 decision, by Tuesday."],
  time="Your time this week: about 30 minutes.", time_s="example",
  what_tag="What", what_h="How far does it go?",
  invite_btn="Explore the method"),
}

# Panoramica e origini: nomi «AI …»
METHOD["it"]["mg_h"] = "I framework del management, ripensati per l'AI"
METHOD["en"]["mg_h"] = "Management frameworks, rethought for AI"
_ren_it = {"Scrum e Scrum of Scrums": ("Scrum e Scrum of Scrums", "AI Scrum · AI Squad per pacchetto, Scrum Master AI"),
           "Design Thinking": ("Design Thinking", "AI Design Thinking · più modelli divergono, un analista converge"),
           "Architettura d'impresa e componibile": ("Architettura d'impresa (TOGAF®) e componibile", "AI Enterprise Architecture · Backbone, Brain, interfacce, Hairs"),
           "DevSecOps": ("DevSecOps", "AI DevSecOps · test di agenti indipendenti, sicurezza dal progetto")}
_ren_en = {"Scrum and Scrum of Scrums": ("Scrum and Scrum of Scrums", "AI Scrum · agent teams per package, AI Scrum Master"),
           "Design Thinking": ("Design Thinking", "AI Design Thinking · several models diverge, one analyst converges"),
           "Enterprise and composable architecture": ("Enterprise (TOGAF®) and composable architecture", "AI Enterprise Architecture · Backbone, Brain, interfaces, Hairs"),
           "DevSecOps": ("DevSecOps", "AI DevSecOps · tests by independent agents, security from the design")}
METHOD["it"]["mg"] = [(ic, *_ren_it.get(a, (a, b)), k) for ic, a, b, k in METHOD["it"]["mg"]]
METHOD["en"]["mg"] = [(ic, *_ren_en.get(a, (a, b)), k) for ic, a, b, k in METHOD["en"]["mg"]]
METHOD["it"]["note"] = "Le pagine seguono lo schema Perché, Come, Cosa (S. Sinek, Start with Why, 2009). " + TM_IT
METHOD["en"]["note"] = "Pages follow the Why, How, What pattern (S. Sinek, Start with Why, 2009). " + TM_EN
ORIGINS.update({
    "squadre": ("Scrum e staff planning → AI Scrum", "Scrum and staff planning → AI Scrum"),
    "scoperta": ("Design Thinking → AI Design Thinking", "Design Thinking → AI Design Thinking"),
    "architettura": ("Architettura d'impresa (TOGAF®) e Composable Architecture → AI Enterprise Architecture", "Enterprise architecture (TOGAF®) and Composable Architecture → AI Enterprise Architecture"),
    "qualita": ("Controllo indipendente e DevSecOps → AI DevSecOps", "Independent control and DevSecOps → AI DevSecOps"),
})

# ---------- HOME-V4b: cambio di rotta del Manager umano (framework fusi nella settimana, nomi che dicono chi fa cosa) ----------
HOME4["it"].update(
  cta2="I framework ripensati",
  tiles_cap="Framework che conosci, ripensati per gli agenti. Il manager resti tu.",
  tiles=[("bulb", "Design Thinking", "Design Thinking tra più AI"), ("target", "Obiettivi", "Mandato di una pagina"),
         ("team", "Scrum", "Scrum, fatto dagli agenti"), ("door1", "Delega", "Delega con due porte"), ("doc", "Reporting", "Reporting in una pagina")],
  wk_tag="Una settimana con Eiraman", wk_h="I framework li applicano gli agenti. Il manager resti tu.",
  wk_note="Esempio illustrativo: i numeri non sono dati del pilota.", you="Tu fai:",
  stages=[
   dict(lab="Settimana zero · L'idea", tone="ai", ic="bulb", frm="Design Thinking", to="Design Thinking tra più AI",
        desc="Più modelli esplorano il problema, un analista converge.", you="approvi la Visione.", key="scoperta", extra=""),
   dict(lab="Lunedì", tone="human", ic="target", frm="Obiettivi e mandato", to="Mandato di una pagina",
        desc="Obiettivo, budget, limiti, ciò che resta a te.", you="scrivi il mandato.", key="fasi", extra=""),
   dict(lab="Lunedì → giovedì", tone="ai", ic="team", frm="Scrum", to="Scrum, fatto dagli agenti",
        desc="Squadre per pacchetto, uno Scrum Master AI, nessuna riunione per te.", you="niente, finché non serve.", key="squadre", extra="counters"),
   dict(lab="Mercoledì", tone="human", ic="door1", frm="Delega", to="Delega con due porte",
        desc="Una domanda per te: quale porta?", you="decidi solo le porte a una via.", key="decisioni", extra="quiz"),
   dict(lab="Venerdì", tone="human", ic="doc", frm="Reporting al management", to="Reporting in una pagina",
        desc="Prima le cattive notizie.", you="leggi e approvi il ciclo successivo.", key="documenti", extra="rev")],
  more="Approfondisci")
HOME4["en"].update(
  cta2="The frameworks, rethought",
  tiles_cap="Frameworks you know, rethought for agents. You stay the manager.",
  tiles=[("bulb", "Design Thinking", "Multi-AI Design Thinking"), ("target", "Objectives", "One-page mandate"),
         ("team", "Scrum", "Agent Scrum"), ("door1", "Delegation", "Two-door delegation"), ("doc", "Reporting", "One-page reporting")],
  wk_tag="A week with Eiraman", wk_h="Agents apply the frameworks. You stay the manager.",
  wk_note="Illustrative example: the numbers are not pilot data.", you="You:",
  stages=[
   dict(lab="Week zero · The idea", tone="ai", ic="bulb", frm="Design Thinking", to="Multi-AI Design Thinking",
        desc="Several models explore the problem, one analyst converges.", you="approve the Vision.", key="scoperta", extra=""),
   dict(lab="Monday", tone="human", ic="target", frm="Objectives and mandate", to="One-page mandate",
        desc="Goal, budget, limits, what stays with you.", you="write the mandate.", key="fasi", extra=""),
   dict(lab="Monday → Thursday", tone="ai", ic="team", frm="Scrum", to="Agent Scrum",
        desc="Teams per package, an AI Scrum Master, no meetings for you.", you="nothing, until it matters.", key="squadre", extra="counters"),
   dict(lab="Wednesday", tone="human", ic="door1", frm="Delegation", to="Two-door delegation",
        desc="A question for you: which door?", you="decide only the one-way doors.", key="decisioni", extra="quiz"),
   dict(lab="Friday", tone="human", ic="doc", frm="Management reporting", to="One-page reporting",
        desc="Bad news first.", you="read it and approve the next cycle.", key="documenti", extra="rev")],
  more="Read more")
HOME4["it"]["time"] = "Circa 30 minuti del tuo tempo."
HOME4["en"]["time"] = "About 30 minutes of your time."

# Panoramica: tutte le coppie, con Cosa resta / Cosa cambia / Tu fai
PRACT = {
 "it": dict(h="I framework del management, ripensati per l'AI",
   p="Il valore non sono i framework fatti dagli agenti: sei tu che resti il manager di quei framework.",
   keep="Cosa resta", change="Cosa cambia", you="Tu fai",
   tm="Scrum, Design Thinking e TOGAF® appartengono ai rispettivi autori; Eiraman ne propone un adattamento agli agenti.",
   rows=[("target", "Obiettivi e mandato", "Mandato di una pagina", "Obiettivi chiari.", "Diventano criteri misurati che gli agenti eseguono.", "Scrivi il mandato.", "fasi"),
         ("door1", "Delega e RACI", "Delega con due porte", "Chi decide che cosa.", "Ciò che si annulla lo decidono gli agenti.", "Decidi le porte a una via.", "decisioni"),
         ("pyramid", "Organigramma e staff planning", "Organigramma di agenti", "Ruoli e competenze.", "I ruoli vanno a modelli diversi e si ricompongono a ogni retrospettiva.", "Approvi budget e livello.", "squadre"),
         ("team", "Scrum e Scrum of Scrums", "Scrum, fatto dagli agenti", "Squadre, backlog, retrospettiva.", "AI Squad per pacchetto, senza timebox umani.", "Nessuna riunione: ricevi il ciclo.", "squadre"),
         ("bulb", "Design Thinking", "Design Thinking tra più AI", "Divergere, poi convergere.", "Più modelli esplorano, un analista converge.", "Approvi la Visione ai gate.", "scoperta"),
         ("spine", "Architettura d'impresa (ispirata a TOGAF®)", "Architettura componibile per agenti", "Viste e priorità.", "Si costruisce in ordine: spina, cervello, interfacce.", "Approvi Principi e Decisioni.", "architettura"),
         ("steps", "Gestione di scope e rischi", "Livelli di applicabilità", "Limitare il rischio.", "Il perimetro si fissa prima, perché la competenza sta nei profili, non in ogni progetto.", "Scegli la classe del progetto.", "livelli"),
         ("scale", "Controllo indipendente", "Verifica tra agenti indipendenti", "Chi controlla non è chi fa.", "Altri modelli verificano; si chiude solo con una prova.", "Accetti il risultato.", "qualita"),
         ("shield", "DevSecOps", "DevSecOps fatto dagli agenti", "Test e sicurezza dal progetto.", "Test automatici, eseguiti da agenti indipendenti.", "Niente di tecnico: vedi gli esiti.", "qualita"),
         ("doc", "Reporting al management", "Reporting in una pagina", "Si decide sui fatti.", "Prima le cattive notizie; le omissioni bloccano il report.", "Leggi e approvi il ciclo.", "documenti")]),
 "en": dict(h="Management frameworks, rethought for AI",
   p="The value is not frameworks run by agents: it is that you stay the manager of those frameworks.",
   keep="What stays", change="What changes", you="You",
   tm="Scrum, Design Thinking and TOGAF® belong to their respective authors; Eiraman proposes an adaptation of them to agents.",
   rows=[("target", "Objectives and mandate", "One-page mandate", "Clear objectives.", "They become measured criteria that agents execute.", "Write the mandate.", "fasi"),
         ("door1", "Delegation and RACI", "Two-door delegation", "Who decides what.", "What can be undone is decided by agents.", "Decide the one-way doors.", "decisioni"),
         ("pyramid", "Organisation chart and staff planning", "Agent organisation chart", "Roles and skills.", "Roles go to different models and are recomposed at every retrospective.", "Approve budget and level.", "squadre"),
         ("team", "Scrum and Scrum of Scrums", "Agent Scrum", "Teams, backlog, retrospective.", "Agent teams per package, with no human timebox.", "No meetings: you receive the cycle.", "squadre"),
         ("bulb", "Design Thinking", "Multi-AI Design Thinking", "Diverge, then converge.", "Several models explore, one analyst converges.", "Approve the Vision at the gates.", "scoperta"),
         ("spine", "Enterprise architecture (inspired by TOGAF®)", "Composable architecture for agents", "Views and priorities.", "Built in order: spine, brain, interfaces.", "Approve Principles and Decisions.", "architettura"),
         ("steps", "Scope and risk management", "Applicability levels", "Limiting risk.", "The scope is fixed up front, because competence lives in the profiles, not in every project.", "Choose the project class.", "livelli"),
         ("scale", "Independent control", "Cross-checking agents", "Whoever checks is not whoever builds.", "Other models check; work closes only on evidence.", "Accept the result.", "qualita"),
         ("shield", "DevSecOps", "Agent DevSecOps", "Tests and security from the design.", "Automated tests, run by independent agents.", "Nothing technical: you see the results.", "qualita"),
         ("doc", "Management reporting", "One-page reporting", "Decisions rest on facts.", "Bad news first; omissions block the report.", "Read and approve the cycle.", "documenti")]),
}
ORIGINS.update({
    "squadre": ("Scrum e staff planning → Scrum, fatto dagli agenti", "Scrum and staff planning → Agent Scrum"),
    "scoperta": ("Design Thinking → Design Thinking tra più AI", "Design Thinking → Multi-AI Design Thinking"),
    "architettura": ("Architettura d'impresa (ispirata a TOGAF®) e Composable Architecture → Architettura componibile per agenti", "Enterprise architecture (inspired by TOGAF®) and Composable Architecture → Composable architecture for agents"),
    "qualita": ("Controllo indipendente e DevSecOps → Verifica tra agenti indipendenti, DevSecOps fatto dagli agenti", "Independent control and DevSecOps → Cross-checking agents, Agent DevSecOps"),
    "decisioni": ("Delega e matrice RACI → Delega con due porte", "Delegation and RACI matrix → Two-door delegation"),
    "documenti": ("Reporting al management → Reporting in una pagina", "Management reporting → One-page reporting"),
})

# ---------- Pagina «I framework ripensati» ----------
SLUG["framework"] = ("framework", "frameworks")
UI["it"]["nav"].insert(1, ("framework", "I framework"))
UI["en"]["nav"].insert(1, ("framework", "Frameworks"))
BEZOS = "https://s2.q4cdn.com/299287126/files/doc_financials/annual/2015-Letter-to-Shareholders.PDF"
FWPAGE = {
 "it": dict(title="I framework ripensati · Eiraman", crumb="I framework ripensati",
  desc="Come Eiraman ripensa sei framework del management per AI Squad: Design Thinking, Scrum, delega, architettura, DevSecOps, reporting.",
  h1="I framework ripensati",
  why="Il management funziona già. Lo ripensiamo per AI Squad, e il manager resti tu.",
  idx_h="Sei framework, un solo schema", idx_p="Per ognuno: l'originale, che cosa resta, che cosa cambia e perché, che cosa fai tu, le regole.",
  lab=dict(orig="Il framework originale", keep="Che cosa conserva Eiraman", change="Che cosa cambia con gli agenti, e perché", you="Tu fai",
           rules="Le regole nel metodo", before="Con le persone", after="Con gli agenti", src="Fonte", spec="Specifica"),
  diff_h="Perché cambiare qualcosa", diff=[("cycle", "Ritmo di lavoro", "I limiti non sono più il tempo delle persone, ma costo, contesto e quote dei fornitori."),
     ("alert", "Niente buon senso", "Servono confini espliciti: ruoli, guardrail, criteri di arresto."),
     ("team", "Nessuna armonia da preservare", "Si possono mettere in concorrenza, se il selettore è affidabile."),
     ("scale", "Verificatori indipendenti", "Lo stesso modello sbaglia negli stessi punti: chi verifica usa un contesto o un modello diverso.")],
  more="Approfondisci", tm="Scrum, Design Thinking e TOGAF® appartengono ai rispettivi autori; Eiraman ne propone un adattamento agli agenti.",
  fws=[
   dict(id="design-thinking", ic="bulb", old="Design Thinking", new="Design Thinking tra più AI",
        orig="Esplorare il problema con gli utenti, divergere sulle idee, poi convergere e prototipare.",
        src=[("Stanford d.school", "https://dschool.stanford.edu/tools/design-thinking-bootleg"), ("Design Council", "https://www.designcouncil.org.uk/resources/framework-for-innovation")],
        before=["Workshop", "Post-it", "Sintesi del facilitatore"], after=["Più modelli divergono", "Gate del Manager umano", "Un analista converge"],
        keep=["Prima divergere, poi convergere.", "Partire dal problema e dagli utenti."],
        change=["Più modelli, ciascuno con un ruolo, esplorano in modo indipendente.", "Le macchine non hanno buon senso: giri, fonti e criteri per scartare sono fissati prima."],
        you="Porti spunti ai gate e approvi la Visione.",
        rules=[("Divergenza tra più modelli con guardrail, convergenza di un solo analista.", "scoperta", "s5"),
               ("La convergenza produce la bozza di Visione e dello Scope Management.", "scoperta", "s5")]),
   dict(id="scrum", ic="team", old="Scrum e Scrum of Scrums", new="Scrum, fatto dagli agenti",
        orig="Team piccoli e autogestiti, Sprint a tempo fisso, backlog ordinato, retrospettiva; Scrum of Scrums per coordinare più team.",
        src=[("Scrum Guide", "https://scrumguides.org/download"), ("Scrum@Scale Guide", "https://www.scrumatscale.com/scrum-at-scale-guide-online/")],
        before=["Sprint di 2 settimane", "Daily meeting", "Team di 3-9 persone"], after=["Wave a costo e durata", "Report allo Scrum Master AI", "Squadre per pacchetto"],
        keep=["Backlog ordinato, squadre, retrospettiva.", "Un coordinamento tra squadre: lo Scrum of Scrums."],
        change=["Niente timebox umani: la Wave è limitata da costo e durata.", "Un'AI Squad per Work Package; il tester lavora senza il contesto della squadra.", "Il Coordinatore AI valida e ricompone le squadre a ogni retrospettiva."],
        you="Nessuna riunione: ricevi una revisione per ciclo.",
        rules=[("Una squadra per Work Package con uno Scrum Master AI e un report al Coordinatore AI.", "squadre", "s4bis"),
               ("La retrospettiva ottimizza le squadre; i cambi di Decisione salgono a te con una SWOT.", "squadre", "s4bis"),
               ("Più squadre in concorrenza solo con un selettore affidabile.", "qualita", "s4")]),
   dict(id="delega", ic="door1", old="Delega e RACI", new="Delega con due porte",
        orig="Chiarire chi esegue, chi risponde, chi è consultato e chi è informato; delegare in base al rischio della decisione.",
        src=[("Lettera agli azionisti Amazon 2015 (porte a una e due vie)", BEZOS)],
        before=["Approvazioni caso per caso", "Matrice RACI"], after=["Porta a due vie: decide l'AI", "Porta a una via: decidi tu", "Il silenzio non approva"],
        keep=["Ognuno risponde di ciò che decide.", "Delegare ciò che si può correggere."],
        change=["La reversibilità decide: ciò che si annulla a costo noto lo decidono gli agenti.", "Un classificatore su un modello diverso decide che cosa sale a te; nel dubbio, sale.", "Si misura quante decisioni non ti sono arrivate e quante ti sono arrivate senza motivo."],
        you="Decidi solo le porte a una via e le riserve del mandato.",
        rules=[("Deny: ciò che il mandato vieta deve bloccarlo l'ambiente, non l'agente.", "decisioni", "s3"),
               ("Delegate: porte a due vie agli agenti. Do: porte a una via a te.", "decisioni", "s3"),
               ("Senza risposta si ferma solo il lavoro che ne dipende.", "decisioni", "s3")]),
   dict(id="architettura", ic="spine", old="Architettura d'impresa (ispirata a TOGAF®) e Composable Architecture", new="Architettura componibile per agenti",
        orig="Viste di business, applicazioni, dati e tecnologia; sistemi fatti di componenti indipendenti e sostituibili.",
        src=[("The Open Group · TOGAF®", "https://help.opengroup.org/hc/en-us/articles/32726995273362-Understanding-the-TOGAF-Standard"), ("MACH Alliance", "https://machalliance.org/")],
        before=["Documento architetturale", "Revisione degli architetti"], after=["Backbone", "Brain", "Interfacce", "Hairs"],
        keep=["Le quattro viste e un documento architetturale.", "Componenti indipendenti con un contratto."],
        change=["L'AI aggiunge pezzi con facilità: senza priorità nasce un patchwork. Si costruisce in ordine: spina, cervello, interfacce, periferiche.", "I compiti del Brain sono trusted o untrusted: quelli untrusted non si delegano senza un controllo deterministico."],
        you="Approvi Principi e Decisioni con impatto di business.",
        rules=[("Backbone per primo, poi Brain, poi interfacce; le funzioni Hairs si tolgono solo se il nucleo regge.", "architettura", "s6bis"),
               ("Richieste diverse a motori locali ed esterni, scelte misurando lo stesso carico.", "architettura", "s6bis")]),
   dict(id="devsecops", ic="shield", old="DevSecOps e test", new="DevSecOps fatto dagli agenti",
        orig="Sviluppo, sicurezza ed esercizio integrati, con controlli automatici lungo tutta la consegna.",
        src=[("NIST SP 800-218 (SSDF)", "https://csrc.nist.gov/pubs/sp/800/218/final"), ("OWASP ASVS", "https://asvs.owasp.org/")],
        before=["Code review umana", "QA manuale"], after=["Unit test indipendenti", "Script e utente simulato", "UAT con te"],
        keep=["Git leggibile, sicurezza fin dal progetto, test automatici.", "Analisi statica, dipendenze, segreti a ogni rilascio."],
        change=["Testa un agente che non ha costruito, e per sicurezza e dati personali un modello diverso.", "Un pacchetto si chiude solo con una prova positiva sulla versione esatta."],
        you="Il responsabile di business svolge il collaudo finale sul compito di business; nessuna attività tecnica.",
        rules=[("Quattro tipi di test: unit, funzionale con script, funzionale con utente simulato, UAT.", "qualita", "s6"),
               ("Ancore deterministiche: gli agenti interpretano gli esiti, non li sostituiscono.", "qualita", "s6")]),
   dict(id="reporting", ic="doc", old="Reporting e governo", new="Reporting in una pagina",
        orig="Il management decide su report periodici, con un ritmo di revisione e un'agenda delle decisioni.",
        src=[],
        before=["Status meeting", "Report lunghi"], after=["Ciclo di governo settimanale", "Una pagina", "Prima le cattive notizie"],
        keep=["Un ritmo fisso di revisione.", "Si decide sui fatti.", "Le cattive notizie salgono per prime."],
        change=["Gli agenti lavorano in Wave brevi: tu ricevi una sola revisione per ciclo.", "Il riassunto di un agente può essere compiacente: per questo la buona pratica diventa una regola. Ogni report apre con le cattive notizie, e un'omissione rispetto ai registri lo blocca."],
        you="Leggi una pagina e approvi il ciclo successivo.",
        rules=[("Ciclo di governo a cadenza fissa; circa tre decisioni e trenta minuti come riferimento.", "ritmo", "s5"),
               ("Prima le cattive notizie e controllo di completezza bloccante.", "documenti", "s8")]),
  ]),
}
FWPAGE["en"] = dict(title="Frameworks rethought · Eiraman", crumb="Frameworks rethought",
  desc="How Eiraman rethinks six management frameworks for teams of AI agents: Design Thinking, Scrum, delegation, architecture, DevSecOps, reporting.",
  h1="Frameworks rethought",
  why="Management already works. We rethink it for AI Squads, and you stay the manager.",
  idx_h="Six frameworks, one pattern", idx_p="For each: the original, what stays, what changes and why, what you do, the rules.",
  lab=dict(orig="The original framework", keep="What Eiraman keeps", change="What changes with agents, and why", you="You",
           rules="The rules in the method", before="With people", after="With agents", src="Source", spec="Specification"),
  diff_h="Why change anything", diff=[("cycle", "Pace of work", "The limits are no longer people's time, but cost, context and provider quotas."),
     ("alert", "No common sense", "Explicit boundaries are needed: roles, guardrails, stop criteria."),
     ("team", "No harmony to preserve", "They can be made to compete, if the selector is reliable."),
     ("scale", "Independent checkers", "The same model errs in the same places: whoever checks uses a different context or model.")],
  more="Read more", tm="Scrum, Design Thinking and TOGAF® belong to their respective authors; Eiraman proposes an adaptation of them to agents.",
  fws=[
   dict(id="design-thinking", ic="bulb", old="Design Thinking", new="Multi-AI Design Thinking",
        orig="Explore the problem with users, diverge on ideas, then converge and prototype.",
        src=FWPAGE["it"]["fws"][0]["src"],
        before=["Workshops", "Sticky notes", "Facilitator's synthesis"], after=["Several models diverge", "Manager umano gates", "One analyst converges"],
        keep=["Diverge first, then converge.", "Start from the problem and the users."],
        change=["Several models, each with a role, explore independently.", "Machines have no common sense: rounds, sources and discard criteria are set up front."],
        you="Bring ideas at the gates and approve the Vision.",
        rules=[("Divergence across several models with guardrails, convergence by a single analyst.", "scoperta", "s5"),
               ("Convergence produces the draft Vision and Scope Management.", "scoperta", "s5")]),
   dict(id="scrum", ic="team", old="Scrum and Scrum of Scrums", new="Agent Scrum",
        orig="Small self-managing teams, fixed-length Sprints, an ordered backlog, retrospectives; Scrum of Scrums to coordinate several teams.",
        src=FWPAGE["it"]["fws"][1]["src"],
        before=["Two-week Sprints", "Daily meeting", "Teams of 3-9 people"], after=["Waves bounded by cost and time", "Reports to the AI Scrum Master", "Teams per package"],
        keep=["Ordered backlog, teams, retrospective.", "Coordination across teams: Scrum of Scrums."],
        change=["No human timebox: a Wave is bounded by cost and duration.", "One AI Squad per Work Package; the tester works without the team's context.", "The AI Coordinator validates and recomposes teams at every retrospective."],
        you="No meetings: you receive one review per cycle.",
        rules=[("One team per Work Package with an AI Scrum Master and a report to the AI Coordinator.", "squadre", "s4bis"),
               ("The retrospective optimises teams; Decision changes come to you with a SWOT.", "squadre", "s4bis"),
               ("Several competing teams only with a reliable selector.", "qualita", "s4")]),
   dict(id="delega", ic="door1", old="Delegation and RACI", new="Two-door delegation",
        orig="Clarify who executes, who is accountable, who is consulted and who is informed; delegate according to the risk of the decision.",
        src=[("Amazon 2015 letter to shareholders (one-way and two-way doors)", BEZOS)],
        before=["Case-by-case approvals", "RACI matrix"], after=["Two-way door: AI decides", "One-way door: you decide", "Silence never approves"],
        keep=["Everyone answers for what they decide.", "Delegate what can be corrected."],
        change=["Reversibility decides: what can be undone at a known cost is decided by agents.", "A classifier on a different model decides what comes to you; when in doubt, it comes.", "We measure how many decisions failed to reach you and how many reached you for no reason."],
        you="Decide only the one-way doors and the matters reserved in the mandate.",
        rules=[("Deny: what the mandate forbids must be blocked by the environment, not by the agent.", "decisioni", "s3"),
               ("Delegate: two-way doors to agents. Do: one-way doors to you.", "decisioni", "s3"),
               ("Without an answer, only the work that depends on it stops.", "decisioni", "s3")]),
   dict(id="architettura", ic="spine", old="Enterprise architecture (inspired by TOGAF®) and Composable Architecture", new="Composable architecture for agents",
        orig="Business, application, data and technology views; systems made of independent, replaceable components.",
        src=FWPAGE["it"]["fws"][3]["src"],
        before=["Architecture document", "Architects' review"], after=["Backbone", "Brain", "Interfaces", "Hairs"],
        keep=["The four views and an architecture document.", "Independent components with a contract."],
        change=["AI adds pieces easily: without priorities you get a patchwork. Build in order: spine, brain, interfaces, periphery.", "Brain tasks are trusted or untrusted: untrusted ones are not delegated without a deterministic check."],
        you="Approve Principles and Decisions with business impact.",
        rules=[("Backbone first, then Brain, then interfaces; Hairs are removed only if the core still holds.", "architettura", "s6bis"),
               ("Different requests to local and external engines, chosen by measuring the same load.", "architettura", "s6bis")]),
   dict(id="devsecops", ic="shield", old="DevSecOps and testing", new="Agent DevSecOps",
        orig="Development, security and operations integrated, with automated checks throughout delivery.",
        src=FWPAGE["it"]["fws"][4]["src"],
        before=["Human code review", "Manual QA"], after=["Independent unit tests", "Script and simulated user", "UAT with you"],
        keep=["Readable Git, security from the design, automated tests.", "Static analysis, dependencies and secrets at every release."],
        change=["Testing is done by an agent that did not build, and for security and personal data by a different model.", "A package closes only with positive evidence on the exact version."],
        you="The business owner performs the final acceptance on the business task; no technical activity.",
        rules=[("Four kinds of test: unit, scripted functional, simulated-user functional, UAT.", "qualita", "s6"),
               ("Deterministic anchors: agents interpret results, they do not replace them.", "qualita", "s6")]),
   dict(id="reporting", ic="doc", old="Reporting and governance", new="One-page reporting",
        orig="Management decides on periodic reports, with a fixed review rhythm and a decision agenda.",
        src=[],
        before=["Status meetings", "Long reports"], after=["Weekly governance cycle", "One page", "Bad news first"],
        keep=["A fixed review rhythm.", "Decisions rest on facts.", "Bad news travels up first."],
        change=["Agents work in short Waves: you receive a single review per cycle.", "An agent's summary can be flattering: that is why good practice becomes a rule. Every report opens with the bad news, and an omission against the records blocks it."],
        you="Read one page and approve the next cycle.",
        rules=[("Governance cycle at a fixed cadence; about three decisions and thirty minutes as a reference.", "ritmo", "s5"),
               ("Bad news first and a blocking completeness check.", "documenti", "s8")]),
  ])
for _l in ("it", "en"):
    HOME4[_l]["fwlink"] = "Vedi come ripensiamo i framework" if _l == "it" else "See how we rethink the frameworks"
    PRACT[_l]["fwlink"] = "Ogni framework, in dettaglio" if _l == "it" else "Each framework, in detail"
FW_SEE = {"scoperta": "design-thinking", "squadre": "scrum", "decisioni": "delega", "architettura": "architettura", "qualita": "devsecops", "ritmo": "reporting", "documenti": "reporting"}

# ---------- Home: solo la settimana, con La perla d'amore in alto ----------
HOME4["it"]["pearl"] = dict(tag="La perla d'amore · H. G. Wells",
  story="Un principe passa anni a costruire un mausoleo per la donna amata. Lo amplia e lo perfeziona, finché il sarcofago gli sembra fuori posto. Allora ordina:",
  quote="«Portate via quella cosa.»",
  thesis="Con l'AI costruire è facile. Restare fedeli allo scopo, no.",
  src="Leggi il racconto su Wikisource")
HOME4["en"]["pearl"] = dict(tag="The Pearl of Love · H. G. Wells",
  story="A prince spends years building a mausoleum for the woman he loved. He enlarges and refines it, until the sarcophagus seems out of place. Then he orders:",
  quote="“Take that thing away.”",
  thesis="With AI, building is easy. Staying true to the purpose is not.",
  src="Read the story on Wikisource")

# ---------- Correzioni della revisione indipendente (R1–R10) ----------
def _swap(obj, a, b):
    if isinstance(obj, str): return obj.replace(a, b)
    if isinstance(obj, list): return [_swap(x, a, b) for x in obj]
    if isinstance(obj, tuple): return tuple(_swap(x, a, b) for x in obj)
    if isinstance(obj, dict): return {k: _swap(v, a, b) for k, v in obj.items()}
    return obj
for _l in ("it", "en"):
    HOME4[_l] = _swap(HOME4[_l], "Mandato di una pagina", "Mandato e riserve")
    HOME4[_l] = _swap(HOME4[_l], "One-page mandate", "Mandate and reservations")
    PRACT[_l] = _swap(PRACT[_l], "Mandato di una pagina", "Mandato e riserve")
    PRACT[_l] = _swap(PRACT[_l], "One-page mandate", "Mandate and reservations")
    FWPAGE[_l] = _swap(FWPAGE[_l], "Mandato di una pagina", "Mandato e riserve")
    FWPAGE[_l] = _swap(FWPAGE[_l], "One-page mandate", "Mandate and reservations")
# R2 quiz
HOME4["it"]["stages"][3]["desc"] = "Prova tu: quale porta? Nel metodo lo decide un classificatore indipendente; nel dubbio la scelta sale a te."
HOME4["en"]["stages"][3]["desc"] = "Try it: which door? In the method an independent classifier decides; when in doubt, the choice comes to you."
# R3 reporting rule
FWPAGE["it"]["fws"][5]["rules"].append(("Una pagina per scheda decisione (§8, regola 4).", "documenti", "s8"))
FWPAGE["en"]["fws"][5]["rules"].append(("One page per decision sheet (§8, rule 4).", "documenti", "s8"))
# R4 Scrum Guide 2020
FWPAGE["it"]["fws"][1]["before"] = ["Sprint fino a un mese", "Daily Scrum", "Team di 10 persone o meno"]
FWPAGE["en"]["fws"][1]["before"] = ["Sprints of up to a month", "Daily Scrum", "Teams of 10 or fewer"]
FWPAGE["it"]["fws"][1]["orig"] = "Team piccoli e autogestiti (10 persone o meno), Sprint fino a un mese, backlog ordinato, retrospettiva; Scrum of Scrums per coordinare più team."
FWPAGE["en"]["fws"][1]["orig"] = "Small self-managing teams (10 people or fewer), Sprints of up to a month, an ordered backlog, retrospectives; Scrum of Scrums to coordinate several teams."
# R7
ORIGINS["squadre"] = ("Scrum e Scrum of Scrums → Scrum, fatto dagli agenti", "Scrum and Scrum of Scrums → Agent Scrum")
FW_SEE["fasi"] = ""
# R8
HOME4["it"]["wk_tag"] = "Come · Una settimana con Eiraman"
HOME4["en"]["wk_tag"] = "How · A week with Eiraman"
# R9
HOME["it"]["title"] = "Eiraman · Chi ha l'idea deve restarne padrone"
HOME["it"]["desc"] = "Chi ha l'idea deve restarne padrone, anche senza leggere il codice. Oggi l'AI costruisce software: Eiraman lascia le decisioni a chi conosce il business."
HOME["en"]["title"] = "Eiraman · Whoever has the idea should stay in charge"
HOME["en"]["desc"] = "Whoever has the idea should stay in charge of it, even without reading code. AI now builds software: Eiraman leaves the decisions to those who know the business."
# R10 glosse
HOME4["it"]["counters"] = [("12", "Wave chiuse (cicli di lavoro)"), ("€ 23", "spesa stimata")]
HOME4["en"]["counters"] = [("12", "Waves closed (work cycles)"), ("€ 23", "estimated spend")]
HOME4["it"]["quiz"][0] = ("Cambiare una libreria interna (un componente tecnico del software)",) + HOME4["it"]["quiz"][0][1:]
HOME4["en"]["quiz"][0] = ("Change an internal library (a technical component of the software)",) + HOME4["en"]["quiz"][0][1:]
HOME4["it"]["stages"][0]["you"] = "approvi la Visione (lo scopo del progetto)."
HOME4["en"]["stages"][0]["you"] = "approve the Vision (the purpose of the project)."

# ---------- Le due porte in parole semplici: «Delega per reversibilità» ----------
for _l in ("it", "en"):
    for _a, _b in (("Delega con due porte", "Delega per reversibilità"), ("Two-door delegation", "Delegation by reversibility")):
        HOME4[_l] = _swap(HOME4[_l], _a, _b); PRACT[_l] = _swap(PRACT[_l], _a, _b); FWPAGE[_l] = _swap(FWPAGE[_l], _a, _b)
        METHOD[_l] = _swap(METHOD[_l], _a, _b); HOME[_l] = _swap(HOME[_l], _a, _b)
    for _k in COMP:
        for _a, _b in (("Delega con due porte", "Delega per reversibilità"), ("Two-door delegation", "Delegation by reversibility")):
            COMP[_k][_l] = _swap(COMP[_k][_l], _a, _b)
ORIGINS["decisioni"] = ("Delega e matrice RACI → Delega per reversibilità", "Delegation and RACI matrix → Delegation by reversibility")
REV_SUB = {"it": "Ciò che si può annullare lo decide l'AI Squad, ciò che non si può annullare lo decidi tu.",
           "en": "What can be undone is decided by the AI Squad; what cannot be undone is decided by you."}
BEZOS_LINE = {"it": "Jeff Bezos le chiama porte a due vie e porte a una via.",
              "en": "Jeff Bezos calls them two-way doors and one-way doors."}
# Home, tappa del mercoledì e quiz
HOME4["it"]["stages"][3].update(desc="Si può tornare indietro senza danni? Prova tu. Nel metodo lo decide un classificatore indipendente; nel dubbio la scelta sale a te.",
                                you="decidi solo ciò che non si può annullare.")
HOME4["en"]["stages"][3].update(desc="Can it be undone without harm? Try it. In the method an independent classifier decides; when in doubt, the choice comes to you.",
                                you="decide only what cannot be undone.")
HOME4["it"].update(q_ai="Sì, si può annullare → decide l'AI Squad", q_ai_s="", q_me="No, non si torna indietro (o tocca una tua riserva) → decidi tu", q_me_s="",
  quiz=[("Cambiare una libreria interna (un componente tecnico del software)", "ai", "Si annulla a costo noto: decide l'AI Squad."),
        ("Mandare i dati dei clienti a un nuovo fornitore", "me", "Dati personali e nuovo fornitore sono riserve del tuo mandato: decidi tu."),
        ("Eliminare una funzione già usata dagli utenti", "me", "Toglie qualcosa a chi la usa e non si annulla senza danno: decidi tu.")])
HOME4["en"].update(q_ai="Yes, it can be undone → the AI Squad decides", q_ai_s="", q_me="No, there is no going back (or it touches one of your reservations) → you decide", q_me_s="",
  quiz=[("Change an internal library (a technical component of the software)", "ai", "It can be undone at a known cost: the AI Squad decides."),
        ("Send customer data to a new provider", "me", "Personal data and a new provider are reserved in your mandate: you decide."),
        ("Remove a feature people already use", "me", "It takes something away from users and cannot be undone without harm: you decide.")])
# Panoramica e pagina framework
for _l in ("it", "en"):
    PRACT[_l]["rows"] = [r if r[2] != ("Delega per reversibilità" if _l == "it" else "Delegation by reversibility") else
                         (r[0], r[1], r[2], r[3], REV_SUB[_l], r[5], r[6]) for r in PRACT[_l]["rows"]]
    FWPAGE[_l]["fws"][2]["sub"] = REV_SUB[_l]
    FWPAGE[_l]["fws"][2]["bezos"] = BEZOS_LINE[_l]
FWPAGE["it"]["fws"][2]["after"] = ["Si può annullare: decide l'AI", "Non si può annullare: decidi tu", "Il silenzio non approva"]
FWPAGE["en"]["fws"][2]["after"] = ["Can be undone: AI decides", "Cannot be undone: you decide", "Silence never approves"]
FWPAGE["it"]["fws"][2]["you"] = "Decidi solo ciò che non si può annullare e le riserve del mandato."
FWPAGE["en"]["fws"][2]["you"] = "Decide only what cannot be undone and the matters reserved in the mandate."

HOME4["it"]["rev_ok_l"] = []
HOME4["en"]["rev_ok_l"] = []

# ---------- Home v6 (25 novembre 2026): posizionamento approvato dal Manager umano, molto grafica ----------
HOME6 = {
  "it": dict(
    title="Eiraman · Chi ha l'idea deve restarne padrone",
    desc="Eiraman applica all'AI i modelli di management che funzionano già: servizi IT su misura, governati dal business, entro un perimetro di rischio dichiarato.",
    h1="Chi ha l'idea deve restarne padrone, anche senza leggere il codice.",
    sub="Oggi l'AI costruisce software. Eiraman lascia le decisioni a chi conosce il business.",
    path_label="Il percorso di questa pagina",
    path=[("why", "Perché", "perche"), ("bridge", "Come", "come"), ("building", "Cosa", "cosa")],
    why_tag="Perché",
    a_h="Il software tradizionale costa troppo per un bisogno solo.",
    a_p="Grandi investimenti e tempi lunghi: si costruisce per molti, e le esigenze specifiche restano scoperte.",
    a_lbl=dict(top="uguale per tutti", cost="costi e tempi", need1="esigenze", need2="scoperte"),
    a_aria="Un unico grande edificio uguale per tutti, con molte persone in fila; accanto, costi e tempi lunghi; fuori restano tre esigenze specifiche, di forme diverse, che non trovano posto.",
    b_h="L'AI può costruire su misura, ma senza metodo si perde il controllo.",
    b_p="Oggi resta in mano ai tecnici, oppure il business la usa da solo, senza governo.",
    b_lbl=dict(left="solo tecnici", right="senza governo", gap="manca il ponte"),
    b_aria="Un bivio tra due sponde. A sinistra l'AI è chiusa dietro una porta riservata ai tecnici; a destra l'AI è libera ma senza governo, con fili aggrovigliati e un segnale di allerta. Al centro manca il ponte e la persona di business resta in basso.",
    how_tag="Come",
    how_h="Applichiamo all'AI i modelli di management che funzionano già.",
    how_p1="Scrum, Design Thinking, architettura, delega, reporting: adattati alle AI Squad.",
    how_p2="Il business governa come governa già progetti, fornitori e persone. Chi sviluppa porta la propria competenza nei profili che guidano gli agenti.",
    how_lbl=dict(models=["Scrum", "Design Thinking", "Architettura", "Delega", "Reporting"], gov="governi tu", teams="AI Squad", prof1="profili qualificati", prof2="da chi sviluppa"),
    how_aria="Il ponte che mancava: cinque modelli di management noti, Scrum, Design Thinking, architettura, delega e reporting, attraversano un ponte e diventano AI Squad. Sopra, la persona di business governa. Sotto, i profili qualificati da chi sviluppa alimentano gli agenti.",
    what_tag="Cosa",
    what_h="Servizi IT su misura, prodotti vicino a chi li usa.",
    what_p="Spostiamo la produzione verso il business, entro un perimetro di rischio dichiarato.",
    what_lbl=dict(far="una fabbrica lontana", fence="perimetro di rischio"),
    what_aria="La produzione si sposta da una fabbrica lontana a tanti piccoli servizi su misura, accanto a ciascuna persona, dentro un recinto leggero che rappresenta il perimetro di rischio dichiarato.",
    cta="Esplora il metodo"),
  "en": dict(
    title="Eiraman · Whoever has the idea should stay in charge",
    desc="Eiraman applies to AI the management models that already work: tailored IT services, governed by the business, within a declared risk perimeter.",
    h1="Whoever has the idea should stay in charge of it, even without reading code.",
    sub="AI now builds software. Eiraman leaves the decisions to those who know the business.",
    path_label="The path of this page",
    path=[("why", "Why", "perche"), ("bridge", "How", "come"), ("building", "What", "cosa")],
    why_tag="Why",
    a_h="Traditional software costs too much for a single need.",
    a_p="Large investments and long lead times: software is built for many, and specific needs stay uncovered.",
    a_lbl=dict(top="the same for all", cost="cost and time", need1="needs", need2="left out"),
    a_aria="One big building, the same for everyone, with many people queuing; beside it, high cost and long lead times; outside, three specific needs of different shapes find no place.",
    b_h="AI can build to measure, but without a method you lose control.",
    b_p="Today it stays with technical staff, or the business uses it alone, without governance.",
    b_lbl=dict(left="technical staff only", right="no governance", gap="the bridge is missing"),
    b_aria="A fork between two banks. On the left, AI is locked behind a door for technical staff only; on the right, AI is free but ungoverned, with tangled wires and a warning sign. In the middle the bridge is missing and the business person stays below.",
    how_tag="How",
    how_h="We apply to AI the management models that already work.",
    how_p1="Scrum, Design Thinking, architecture, delegation, reporting: adapted to AI Squads.",
    how_p2="The business governs the way it already governs projects, suppliers and people. Those who develop software bring their competence into the profiles that guide the agents.",
    how_lbl=dict(models=["Scrum", "Design Thinking", "Architecture", "Delegation", "Reporting"], gov="you govern", teams="AI Squads", prof1="qualified profiles", prof2="from developers"),
    how_aria="The missing bridge: five well-known management models, Scrum, Design Thinking, architecture, delegation and reporting, cross a bridge and become AI Squads. Above, the business person governs. Below, profiles qualified by those who develop software feed the agents.",
    what_tag="What",
    what_h="Tailored IT services, produced close to the people who use them.",
    what_p="We move production towards the business, within a declared risk perimeter.",
    what_lbl=dict(far="a distant factory", fence="risk perimeter"),
    what_aria="Production moves from a distant factory to many small tailored services, next to each person, inside a light fence that stands for the declared risk perimeter.",
    cta="Explore the method"),
}

# ---------- Richieste del Manager umano del 25 novembre 2026 (giudizio di contesto, niente cancellature, architettura) ----------
_JUDG = {"it": "Gli agenti non hanno il giudizio di contesto di una persona: seguono le istruzioni alla lettera e non capiscono da soli quando stanno uscendo dallo scopo.",
         "en": "Agents lack a person's contextual judgement: they follow instructions literally and do not realise on their own when they are drifting out of scope."}
_SW = [
  ("Le macchine però non hanno buon senso, quindi servono confini chiari.", "Ma gli agenti non hanno il giudizio di contesto di una persona: seguono le istruzioni alla lettera, quindi servono confini chiari."),
  ("Machines have no common sense, though, so clear boundaries are needed.", "But agents lack a person's contextual judgement: they follow instructions literally, so clear boundaries are needed."),
  ("Le macchine non hanno buon senso: giri, fonti e criteri per scartare sono fissati prima.", "Gli agenti non hanno il giudizio di contesto di una persona: giri, fonti e criteri per scartare sono fissati prima."),
  ("Machines have no common sense: rounds, sources and discard criteria are set up front.", "Agents lack a person's contextual judgement: rounds, sources and discard criteria are set up front."),
  ("Niente buon senso", "Niente giudizio di contesto"),
  ("No common sense", "No contextual judgement"),
  ("Servono confini espliciti: ruoli, guardrail, criteri di arresto.", "Seguono le istruzioni alla lettera e non capiscono da soli quando escono dallo scopo: servono ruoli, guardrail, criteri di arresto."),
  ("Explicit boundaries are needed: roles, guardrails, stop criteria.", "They follow instructions literally and do not notice when they drift out of scope: roles, guardrails and stop criteria are needed."),
]
for _a, _b in _SW:
    COMP = _swap(COMP, _a, _b); FWPAGE = _swap(FWPAGE, _a, _b); PRACT = _swap(PRACT, _a, _b); METHOD = _swap(METHOD, _a, _b); HOME4 = _swap(HOME4, _a, _b)

# niente cancellature: i framework tradizionali si rileggono, non si cancellano
FWPAGE["it"]["why"] = "Il management funziona già. Non lo cancelliamo: lo rileggiamo in chiave agentica, e il manager resti tu."
FWPAGE["en"]["why"] = "Management already works. We do not erase it: we reread it for agents, and you stay the manager."
FWPAGE["it"]["idx_p"] = "Framework tradizionale → riletto per gli agenti. Per ognuno: l'originale, che cosa resta, che cosa cambia e perché, che cosa fai tu, le regole."
FWPAGE["en"]["idx_p"] = "Traditional framework → reread for agents. For each: the original, what stays, what changes and why, what you do, the rules."

# architettura: rafforzare prioritizzazione e scope, togliere complessità di review e shadow IT
for _l, _d in (("it", dict(
        before=["Documento architetturale", "Cicli di review architetturale"],
        after=["Viste e Principi nel metodo", "Priorità Backbone → Brain → interfacce → Hairs", "Applicate a ogni pacchetto"],
        keep=["Non togliamo nulla all'architettura d'impresa: le viste di business, applicazioni, dati e tecnologia e il documento architetturale restano.",
              "Rafforziamo prioritizzazione e scope management: con gli agenti diventano ancora più critici, perché l'AI rende facile aggiungere pezzi e costruire patchwork."],
        change=["Togliamo la complessità dei cicli di review architetturali e il rischio di shadow IT.",
                "Le viste, la priorità Backbone → Brain → interfacce → Hairs e i Principi sono nel metodo, e gli agenti li applicano a ogni pacchetto.",
                "I compiti del Brain sono trusted o untrusted: quelli untrusted non si delegano senza un controllo deterministico."],
        you="Approvi Principi e Decisioni con impatto di business; non servono cicli di review architetturali.")),
     ("en", dict(
        before=["Architecture document", "Architecture review cycles"],
        after=["Views and Principles in the method", "Priority Backbone → Brain → interfaces → Hairs", "Applied to every package"],
        keep=["We take nothing away from enterprise architecture: the business, application, data and technology views and the architecture document stay.",
              "We strengthen prioritisation and scope management: with agents they become even more critical, because AI makes it easy to add pieces and build patchworks."],
        change=["We remove the complexity of architecture review cycles and the risk of shadow IT.",
                "The views, the Backbone → Brain → interfaces → Hairs priority and the Principles are in the method, and the agents apply them to every package.",
                "Brain tasks are trusted or untrusted: untrusted ones are not delegated without a deterministic check."],
        you="Approve Principles and Decisions with a business impact; no architecture review cycles are needed."))):
    for _fw in FWPAGE[_l]["fws"]:
        if _fw["id"] == "architettura": _fw.update(_d)
COMP["architettura"]["it"]["why"] = "Non togliamo nulla all'architettura d'impresa: rafforziamo prioritizzazione e scope, che con gli agenti diventano ancora più critici perché l'AI rende facile costruire patchwork. Togliamo la complessità dei cicli di review architetturali e il rischio di shadow IT: le regole sono nel metodo e gli agenti le applicano a ogni pacchetto, con verifiche indipendenti e chiusura su prova."
COMP["architettura"]["en"]["why"] = "We take nothing away from enterprise architecture: we strengthen prioritisation and scope, which become even more critical with agents because AI makes patchworks easy. We remove the complexity of architectural review cycles and the risk of shadow IT: the rules are in the method and the agents apply them to every package, with independent checks and evidence-based closure."

# ---------- SITO-V7 · pagina Livelli riprogettata per chi non conosce il contesto ----------
COMP["livelli"]["it"].update(
    card="Livelli",
    line="Che cosa puoi costruire, e per chi.",
    h1="Che cosa puoi costruire, e per chi?",
    why="Non tutto si può costruire con lo stesso rischio. Più persone usano ciò che costruisci, più servono garanzie.",
    how="Il livello dipende da chi userà il risultato: solo tu, i tuoi colleghi o i tuoi clienti. Prima di iniziare, e a ogni ciclo di lavoro, un controllo verifica che il progetto resti nel suo livello. Nel dubbio, si ferma.")
COMP["livelli"]["en"].update(
    card="Levels",
    line="What you can build, and for whom.",
    h1="What can you build, and for whom?",
    why="Not everything can be built with the same risk. The more people use what you build, the more safeguards you need.",
    how="The level depends on who will use the result: only you, your colleagues or your customers. Before starting, and at every work cycle, a check makes sure the project stays within its level. When in doubt, it stops.")
LEVELS = {
 "it": dict(
   rings=["Per me", "Per il mio team", "Per i clienti"], ring_out="Fuori",
   rings_label="Tre cerchi concentrici: per me, per il mio team, per i clienti. Fuori dai cerchi, ciò che Eiraman non fa.",
   who_lbl="Chi lo usa", ex_lbl="Esempi", need_lbl="Che cosa serve",
   levels=[
     dict(n="0", ic="person", h="Per me", who="Solo tu.",
          ex=["Un generatore di report personali", "Un assistente per i tuoi documenti"],
          need=["I controlli di base del metodo, niente di particolare"]),
     dict(n="1", ic="group", h="Per il mio team", who="I tuoi colleghi.",
          ex=["Un'app di reparto per le richieste interne"],
          need=["Accesso con l'identità aziendale", "Una prova che i dati si possono ripristinare", "Regole sui dati dei colleghi", "Un'organizzazione che ne risponde"]),
     dict(n="2", ic="globe", h="Per i clienti", who="Persone fuori dall'organizzazione.",
          ex=["Un portale per i clienti"],
          need=["Un test di sicurezza fatto da esperti esterni", "Aggiornamenti di sicurezza costanti", "Pagamenti e login affidati a fornitori certificati"]),
   ],
   out=dict(h="Fuori: che cosa Eiraman non fa", p="Ci sono casi in cui il rischio è troppo alto per costruire senza specialisti dedicati. Qui il metodo si ferma, a qualunque livello.",
            items=["Dati sanitari o giudiziari", "Dati di minori", "Pagamenti gestiti in proprio", "Decisioni automatiche su persone", "AI ad alto rischio", "Infrastrutture critiche", "Software da installare venduto sul mercato"]),
   up_h="Come si sale di livello",
   up=[("stamp", "Dimostri i risultati", "Al livello attuale, con prove misurate."),
       ("check", "Soddisfi i requisiti in più", "Quelli del livello successivo, tutti."),
       ("manager", "Lo decidi tu", "È una scelta da cui non si torna indietro facilmente.")],
   down="Se un requisito decade, si scende in automatico: finché non si rimedia, si possono solo correggere errori.",
   ex_h="Esempio: un'idea che cresce",
   story=[("0", "Uno strumento tuo", "Un assistente che prepara il riepilogo settimanale delle tue riunioni."),
          ("1", "Lo usa il tuo team", "Lo chiedono i colleghi: diventa un'app di reparto, con accesso aziendale e regole sui loro dati."),
          ("2", "Lo usano i clienti", "Diventa un servizio per i clienti: test di sicurezza esterno e login tramite un fornitore certificato.")],
   details_h="Per chi vuole i dettagli"),
 "en": dict(
   rings=["For me", "For my team", "For customers"], ring_out="Out",
   rings_label="Three concentric circles: for me, for my team, for customers. Outside the circles, what Eiraman does not do.",
   who_lbl="Who uses it", ex_lbl="Examples", need_lbl="What it takes",
   levels=[
     dict(n="0", ic="person", h="For me", who="Only you.",
          ex=["A personal report generator", "An assistant for your documents"],
          need=["The method's basic checks, nothing special"]),
     dict(n="1", ic="group", h="For my team", who="Your colleagues.",
          ex=["A department app for internal requests"],
          need=["Sign-in with the company identity", "Proof that data can be restored", "Rules on colleagues' data", "An organisation that is accountable"]),
     dict(n="2", ic="globe", h="For customers", who="People outside the organisation.",
          ex=["A customer portal"],
          need=["A security test by external experts", "Ongoing security updates", "Payments and sign-in through certified providers"]),
   ],
   out=dict(h="Out: what Eiraman does not do", p="In some cases the risk is too high to build without dedicated specialists. Here the method stops, at any level.",
            items=["Health or criminal-record data", "Children's data", "Payments handled in-house", "Automated decisions about people", "High-risk AI", "Critical infrastructure", "Installable software sold on the market"]),
   up_h="How you move up a level",
   up=[("stamp", "Show the results", "At the current level, with measured evidence."),
       ("check", "Meet the extra requirements", "All those of the next level."),
       ("manager", "You decide", "It is a choice that is not easily undone.")],
   down="If a requirement lapses, you step down automatically: until it is fixed, only error corrections are allowed.",
   ex_h="Example: an idea that grows",
   story=[("0", "A tool of your own", "An assistant that prepares the weekly summary of your meetings."),
          ("1", "Your team uses it", "Colleagues ask for it: it becomes a department app, with company sign-in and rules on their data."),
          ("2", "Customers use it", "It becomes a customer service: external security test and sign-in through a certified provider.")],
   details_h="For those who want the details"),
}

# ---------- SITO-V7 · §06 Reporting: controllo costi rafforzato ----------
FWPAGE["it"]["fws"][5].update(
    old="Reporting, governo e controllo costi", new="Reporting in una pagina, costi sotto controllo",
    sub="Con gli agenti il costo non è più il tempo delle persone: sono token, motori, tentativi e proposte scartate. Eiraman lo rende visibile e governabile come un budget di progetto.",
    orig="Il management decide su report periodici e controlla i costi con budget, consuntivi e soglie di spesa.",
    before=["Status meeting", "Report lunghi", "Costo = ore delle persone"],
    after=["Ciclo di governo settimanale", "Una pagina, prima le cattive notizie", "Costo per risultato accettato"],
    keep=["Un ritmo fisso di revisione.", "Si decide sui fatti.", "Le cattive notizie salgono per prime.", "Un budget approvato prima di spendere."],
    change=["Gli agenti lavorano in Wave brevi: tu ricevi una sola revisione per ciclo.",
            "Il costo nasce da token, motori e tentativi, comprese le proposte scartate: si conta tutto, anche quello che non arriva in consegna.",
            "Ogni Wave ha un tetto di spesa: avviso all'80%, stop al nuovo lavoro al 100%.",
            "Ogni profilo ha un costo unitario per motore, anche per i motori locali.",
            "Il riassunto di un agente può essere compiacente: per questo la buona pratica diventa una regola. Ogni report apre con le cattive notizie, e un'omissione rispetto ai registri lo blocca."],
    you="Fissi il budget nel mandato e ogni settimana leggi una riga di costi: spesa, costo per risultato accettato, scostamento.",
    rules=[("Ciclo di governo a cadenza fissa; circa tre decisioni e trenta minuti come riferimento.", "ritmo", "s5"),
           ("Tetto di spesa per Wave: avviso all'80%, blocco del nuovo lavoro al 100%; criteri di arresto per spesa nel mandato.", "ritmo", "s5"),
           ("Costo per incremento accettato, incluse le candidate scartate; Unit Cost per profilo e motore, anche locale.", "qualita", "s4"),
           ("Budget di deriva cumulativo sul progetto, riportato a ogni ciclo.", "decisioni", "s3"),
           ("Rendiconto separato tra costi di sviluppo e costi di utilizzo; le spese non misurate restano «sconosciute», mai zero.", "documenti", "s8"),
           ("Prima le cattive notizie e controllo di completezza bloccante; una pagina per scheda decisione.", "documenti", "s8")])
FWPAGE["en"]["fws"][5].update(
    old="Reporting, governance and cost control", new="One-page reporting, costs under control",
    sub="With agents, cost is no longer people's time: it is tokens, engines, attempts and discarded proposals. Eiraman makes it visible and governable like a project budget.",
    orig="Management decides on periodic reports and controls costs with budgets, actuals and spending thresholds.",
    before=["Status meetings", "Long reports", "Cost = people's hours"],
    after=["Weekly governance cycle", "One page, bad news first", "Cost per accepted result"],
    keep=["A fixed review rhythm.", "Decisions rest on facts.", "Bad news travels up first.", "A budget approved before spending."],
    change=["Agents work in short Waves: you receive a single review per cycle.",
            "Cost comes from tokens, engines and attempts, including discarded proposals: everything is counted, even what never gets delivered.",
            "Every Wave has a spending cap: warning at 80%, new work stops at 100%.",
            "Every profile has a unit cost per engine, local engines included.",
            "An agent's summary can be flattering: that is why good practice becomes a rule. Every report opens with the bad news, and an omission against the records blocks it."],
    you="You set the budget in the mandate and each week read one line of costs: spend, cost per accepted result, drift.",
    rules=[("Governance cycle at a fixed cadence; about three decisions and thirty minutes as a reference.", "ritmo", "s5"),
           ("Spending cap per Wave: warning at 80%, new work blocked at 100%; spending stop criteria in the mandate.", "ritmo", "s5"),
           ("Cost per accepted increment, discarded candidates included; Unit Cost per profile and engine, local ones too.", "qualita", "s4"),
           ("Cumulative drift budget on the project, reported every cycle.", "decisioni", "s3"),
           ("Separate accounts for development and running costs; unmeasured spend stays “unknown”, never zero.", "documenti", "s8"),
           ("Bad news first and a blocking completeness check; one page per decision sheet.", "documenti", "s8")])
COSTDASH = {
 "it": dict(h="Cruscotto dei costi (esempio illustrativo)", label="Cruscotto dei costi: barra del budget della Wave con soglia di avviso all'80% e blocco al 100%; sotto, costo per risultato accettato e voci del rendiconto.",
            bar="Budget della Wave", warn="80% avviso", stop="100% stop", spent="speso 64%",
            kpis=[("Costo per risultato accettato", "incluse le proposte scartate"), ("Sviluppo · Utilizzo", "rendiconti separati"), ("Sconosciuto", "mai contato come zero")]),
 "en": dict(h="Cost dashboard (illustrative example)", label="Cost dashboard: Wave budget bar with an 80% warning and a 100% stop; below, cost per accepted result and the report items.",
            bar="Wave budget", warn="80% warning", stop="100% stop", spent="spent 64%",
            kpis=[("Cost per accepted result", "discarded proposals included"), ("Development · Running", "separate accounts"), ("Unknown", "never counted as zero")]),
}

# ---------- HOME-V7 · solo testo, senza grafici ----------
HOME7 = {
 "it": dict(title="Eiraman · Chi ha l'idea deve restarne padrone",
   desc="Eiraman è un metodo per far costruire all'AI il software di cui la tua azienda ha bisogno, governandolo con gli strumenti di management che già usi.",
   h1="Chi ha l'idea deve restarne padrone, anche senza leggere il codice.",
   lead="Eiraman è un metodo per far costruire all'AI il software di cui la tua azienda ha bisogno, governandolo con gli strumenti di management che già usi.",
   blocks=[("Il problema", "Il software su misura costa troppo, e l'AI senza regole è un rischio.",
            "Un'esigenza del tuo reparto resta scoperta perché «non vale l'investimento». Intanto qualcuno usa l'AI da solo, senza controlli."),
           ("La soluzione", "Gestisci l'AI come gestisci un progetto.",
            "Obiettivi, deleghe, squadre e un resoconto settimanale: i metodi che conosci, applicati agli agenti AI. Gli sviluppatori mettono la loro competenza nelle regole che gli agenti seguono."),
           ("Cosa ottieni", "Servizi IT su misura, in tempi brevi, con costi e rischi sotto controllo.", "")],
   btn="Scopri il metodo"),
 "en": dict(title="Eiraman · Whoever has the idea should stay in charge of it",
   desc="Eiraman is a method for having AI build the software your company needs, governed with the management tools you already use.",
   h1="Whoever has the idea should stay in charge of it, even without reading code.",
   lead="Eiraman is a method for having AI build the software your company needs, governed with the management tools you already use.",
   blocks=[("The problem", "Custom software costs too much, and AI without rules is a risk.",
            "A need in your department goes unmet because it is “not worth the investment”. Meanwhile, someone is using AI on their own, with no controls."),
           ("The solution", "Manage AI the way you manage a project.",
            "Objectives, delegation, teams and a weekly report: the methods you know, applied to AI agents. Developers put their expertise into the rules the agents follow."),
           ("What you get", "Tailored IT services, delivered quickly, with costs and risks under control.", "")],
   btn="Discover the method"),
}

# ===================== SITO-TONO (25 novembre 2026): registro da documento di metodo =====================
def _tset(obj, path, val):
    """Imposta un valore lungo un percorso di chiavi/indici, ricostruendo le tuple."""
    k = path[0]
    if len(path) == 1:
        if isinstance(obj, tuple):
            l = list(obj); l[k] = val; return tuple(l)
        obj[k] = val; return obj
    child = obj[k]
    new = _tset(child, path[1:], val)
    if isinstance(obj, tuple):
        l = list(obj); l[k] = new; return tuple(l)
    obj[k] = new; return obj

def _T(root, path, it, en):
    _tset(root["it"], path, it); _tset(root["en"], path, en)

# --- Titoli e aperture delle pagine di dettaglio: nomi dei componenti, frasi descrittive ---
_COMP_HEAD = {
 "principi": ("Principi del metodo", "Otto principi orientano le scelte del metodo.",
   "Otto principi descrivono il modo in cui il metodo ragiona e permettono di riconoscere quando un'esecuzione se ne discosta.",
   "Principles of the method", "Eight principles guide the choices of the method.",
   "Eight principles describe how the method reasons and make it possible to recognise when execution departs from them."),
 "ruoli": ("Ruoli e responsabilità", "Chi decide, chi esegue, chi risponde.",
   "Una ripartizione esplicita dei ruoli è la condizione per delegare il lavoro agli agenti mantenendone il governo.",
   "Roles and responsibilities", "Who decides, who executes, who is accountable.",
   "An explicit division of roles is the condition for delegating work to agents while keeping it under governance."),
 "fasi": ("Fasi del ciclo di produzione", "Dalla prima idea al servizio in esercizio.",
   "Tutte le fasi sono svolte dall'AI Squad. Il responsabile di business interviene nei punti di decisione previsti per ciascuna fase.",
   "Phases of the production cycle", "From the first idea to a running service.",
   "The agent team carries out every phase. The business owner intervenes at the decision points set for each phase."),
 "decisioni": ("Decisioni ed escalation", "Quali decisioni salgono al responsabile di business.",
   "Salgono al responsabile di business le decisioni che non si possono annullare e quelle che toccano le riserve del mandato. Le altre sono prese dall'AI Squad.",
   "Decisions and escalation", "Which decisions are escalated to the business owner.",
   "Decisions that cannot be undone and those that touch the matters reserved in the mandate are escalated to the business owner. The agent team takes the others."),
 "qualita": ("Qualità e verifiche", "Come si verifica il lavoro degli agenti.",
   "La dichiarazione di un agente non basta a chiudere un lavoro. Servono prove sulla versione consegnata, verifiche indipendenti e, quando il costo lo giustifica, più proposte a confronto.",
   "Quality and verification", "How the agents' work is verified.",
   "An agent's statement is not enough to close a piece of work. It requires evidence on the delivered version, independent checks and, where the cost justifies it, several proposals compared."),
 "ritmo": ("Ritmo di lavoro e ciclo di governo", "Wave degli agenti e revisione periodica.",
   "Gli agenti lavorano in cicli brevi. Il responsabile di business decide con una cadenza propria, indicativamente settimanale, su una revisione di una pagina.",
   "Work rhythm and governance cycle", "Agent Waves and periodic review.",
   "Agents work in short cycles. The business owner decides at their own cadence, indicatively weekly, on a one-page review."),
 "livelli": ("Livelli di applicabilità", "Che cosa si può costruire, e per chi.",
   "Non tutto si può costruire con lo stesso livello di rischio. Più sono le persone che useranno il risultato, più garanzie sono richieste.",
   "Applicability levels", "What can be built, and for whom.",
   "Not everything can be built at the same level of risk. The more people will use the result, the more safeguards are required."),
 "documenti": ("Documentazione", "Che cosa legge il responsabile di business, e che cosa leggono gli agenti.",
   "Il responsabile di business legge poche pagine scritte per un manager. La documentazione operativa è prodotta e verificata dagli agenti.",
   "Documentation", "What the business owner reads, and what the agents read.",
   "The business owner reads a few pages written for a manager. Operational documentation is produced and checked by the agents."),
 "profili": ("Role Profile e competenze", "Dove risiede la competenza specialistica.",
   "La competenza specialistica è scritta nei Role Profile e qualificata una volta per tutti i progetti da esperti dell'organizzazione.",
   "Role Profiles and expertise", "Where specialist expertise resides.",
   "Specialist expertise is written into Role Profiles and qualified once, for all projects, by experts of the organisation."),
 "sicurezza": ("Sicurezza e tracciabilità", "Che cosa resta nell'ambiente e che cosa ne esce.",
   "Stato, registri, codice e segreti restano nell'ambiente del progetto. Escono solo i dati autorizzati dal mandato, verso i motori AI ammessi.",
   "Security and traceability", "What stays in the environment and what leaves it.",
   "State, logs, code and secrets stay in the project environment. Only the data authorised by the mandate leaves it, towards approved AI engines."),
 "squadre": ("AI Squad e Scrum", "Come si organizzano le AI Squad.",
   "Le AI Squad si organizzano come in un'azienda: ruoli diversi, una squadra per pacchetto di lavoro, un coordinatore e una retrospettiva che ne migliora la composizione.",
   "AI Squads and Scrum", "How agent teams are organised.",
   "Agent teams are organised as in a company: different roles, one team per work package, a coordinator and a retrospective that improves their composition."),
 "architettura": ("Architettura componibile", "Prima l'essenziale, poi il resto.",
   "Il metodo mantiene l'architettura d'impresa e ne rafforza la prioritizzazione e lo scope management, più critici con gli agenti perché l'AI rende facile aggiungere componenti. Riduce la complessità dei cicli di review architetturali e il rischio di shadow IT: le regole sono nel metodo e gli agenti le applicano a ogni pacchetto, con verifiche indipendenti e chiusura su prova.",
   "Composable architecture", "The essentials first, then the rest.",
   "The method keeps enterprise architecture and strengthens its prioritisation and scope management, which are more critical with agents because AI makes adding components easy. It reduces the complexity of architectural review cycles and the risk of shadow IT: the rules are in the method and the agents apply them to every package, with independent checks and evidence-based closure."),
 "scoperta": ("Scoperta con il Design Thinking", "Più ipotesi, poi una sola Visione.",
   "La scoperta segue il Design Thinking: prima si aprono le ipotesi, poi si converge. Gli agenti non hanno il giudizio di contesto di una persona e seguono le istruzioni alla lettera: per questo il metodo fissa confini e criteri espliciti.",
   "Discovery with Design Thinking", "Several hypotheses, then one Vision.",
   "Discovery follows Design Thinking: hypotheses are opened up first, then converge. Agents lack a person's contextual judgement and follow instructions literally: this is why the method sets explicit boundaries and criteria."),
}
for _k, (_h1, _ln, _why, _h1e, _lne, _whye) in _COMP_HEAD.items():
    COMP[_k]["it"].update(h1=_h1, line=_ln, why=_why)
    COMP[_k]["en"].update(h1=_h1e, line=_lne, why=_whye)

_HOW = {
 "ruoli": ("Il responsabile di business risponde delle proprie decisioni. Gli agenti rispondono in senso operativo: ogni chiusura ha una prova. Verso clienti e terzi risponde il titolare: la persona, se il progetto è per uso personale; l'organizzazione, se è per altri.",
           "The business owner is accountable for their own decisions. The agents are accountable operationally: every closure has evidence. Towards customers and third parties the owner of the project is accountable: the person, for personal use; the organisation, when it serves others."),
 "livelli": ("Il livello dipende da chi userà il risultato: solo chi lo costruisce, i colleghi, oppure clienti esterni. Prima di iniziare e a ogni ciclo di lavoro un controllo verifica che il progetto resti nel suo livello; nel dubbio, il lavoro si ferma.",
             "The level depends on who will use the result: only its builder, colleagues, or external customers. Before starting and at every work cycle a check verifies that the project stays within its level; when in doubt, work stops."),
 "documenti": ("La documentazione ha tre livelli. Quella destinata al responsabile di business è breve, in linguaggio di business, e apre con le cattive notizie: gli agenti usano modelli linguistici, che tendono a compiacere chi li interroga e ad attenuare ciò che è andato male. Per auditor e clienti è previsto un pacchetto di evidenze separato.",
               "Documentation has three levels. What is meant for the business owner is short, in business language, and opens with the bad news: agents run on language models, which tend to please whoever is asking and to play down what went wrong. For auditors and customers a separate evidence pack is provided."),
 "scoperta": ("Più modelli, ciascuno con un ruolo, esplorano il problema in modo indipendente. Il responsabile di business può intervenire in momenti prestabiliti. Un analista raccoglie i contributi, sceglie e redige la prima Visione.",
              "Several models, each with a role, explore the problem independently. The business owner can intervene at set moments. An analyst gathers the contributions, chooses and drafts the first Vision."),
 "principi": ("Ogni regola del metodo discende da uno di questi principi. Una pratica che li contraddice va corretta.",
              "Every rule of the method derives from one of these principles. A practice that contradicts them must be corrected."),
}
for _k, (_i, _e) in _HOW.items():
    COMP[_k]["it"]["how"] = _i; COMP[_k]["en"]["how"] = _e

# --- Testi puntuali in seconda persona ---
_T(COMP["principi"], ["tiles", 1, 2], "Si decide prima, non a ogni passo", "Decisions are taken up front, not at every step")
_T(COMP["principi"], ["tiles", 1, 3], "Un mandato chiaro sostituisce le approvazioni puntuali.", "A clear mandate replaces step-by-step approvals.")
_T(COMP["principi"], ["tiles", 2, 2], "Ciò che non si annulla lo decide una persona", "What cannot be undone is decided by a person")
_T(COMP["principi"], ["tiles", 2, 3], "Il resto lo decide l'AI Squad.", "The agent team decides the rest.")
_T(COMP["principi"], ["tiles", 5, 3], "Verificatori indipendenti; per sicurezza e dati personali, di un modello diverso.", "Independent checkers; for security and personal data, on a different model.")
_T(COMP["ruoli"], ["tiles", 0, 3], "Responsabile di business: mandato, budget, decisioni di business, accettazione.", "Business owner: mandate, budget, business decisions, acceptance.")
_T(COMP["ruoli"], ["tiles", 3, 3], "Controlla a campione che le decisioni dovute siano state sottoposte al responsabile di business.", "Samples work to check that due decisions were escalated to the business owner.")
for _i, (_a, _b) in enumerate([("Approva la Visione", "Approves the Vision"), ("Interviene solo se l'esito è negativo", "Intervenes only if the outcome is negative"),
                               ("Approva Principi e budget", "Approves Principles and budget"), ("Una revisione a settimana", "One review a week"),
                               ("Accetta il risultato", "Accepts the result")]):
    _T(COMP["fasi"], ["phases", _i, 2], _a, _b)
_T(COMP["fasi"], ["you"], "Responsabile di business:", "Business owner:")
_T(COMP["decisioni"], ["trio", 2, 2], "Do · decide il responsabile di business", "Do · the business owner decides")
_T(COMP["decisioni"], ["rules", 0, 1], "Il mandato elenca le riserve; al responsabile di business arriva il loro impatto di business, non la scelta tecnica.", "The mandate lists reserved matters; the business owner receives their business impact, not the technical choice.")
_T(COMP["decisioni"], ["rules", 3, 1], "Un classificatore su un modello diverso stabilisce che cosa sale al responsabile di business; in caso di disaccordo, la decisione sale.", "A classifier on a different model determines what is escalated to the business owner; in case of disagreement, the decision is escalated.")
_T(COMP["decisioni"], ["rules", 5, 1], "Si misurano le decisioni che avrebbero dovuto salire e non sono salite, e quelle salite senza motivo.", "Decisions that should have been escalated and were not, and those escalated needlessly, are measured.")
_T(COMP["qualita"], ["rules", 6, 1], "Proposte molto divergenti: si sceglie ciò che costa meno annullare; i casi ripetuti diventano un tema per il responsabile di business.", "Highly divergent proposals: the option cheapest to undo is chosen; repeated cases become a topic for the business owner.")
_T(COMP["ritmo"], ["lane_po"], "Ciclo di governo del responsabile di business", "Business owner's governance cycle")
_T(COMP["documenti"], ["pyr", 0, 1], "Approvazione: Visione, Principi, mandato", "Approval: Vision, Principles, mandate")
_T(COMP["documenti"], ["pyr", 1, 1], "Lettura e decisione: una pagina per decisione", "Reading and decision: one page per decision")
_T(COMP["sicurezza"], ["inside"], "Resta nell'ambiente del progetto", "Stays in the project environment")
_T(COMP["squadre"], ["tiles", 3, 3], "Migliora la composizione delle squadre; le Decisioni restano al responsabile di business.", "Improves team composition; Decisions stay with the business owner.")
_T(COMP["squadre"], ["rules", 4, 1], "I risparmi entro tolleranza si applicano senza escalation; il cambio di una Decisione sale al responsabile di business con una SWOT.", "Savings within tolerance apply without escalation; changing a Decision is escalated to the business owner with a SWOT.")
_T(COMP["scoperta"], ["flow", 1, 1], "Contributi del responsabile di business, a gate fissi", "Business owner's input, at fixed gates")
_T(COMP["scoperta"], ["tiles", 3, 2], "Decisione del responsabile di business", "Business owner's decision")
_T(COMP["scoperta"], ["tiles", 3, 3], "Approva la Visione o rilancia l'esplorazione.", "Approves the Vision or relaunches the exploration.")

# --- Home testuale ---
HOME7["it"].update(
  desc="Eiraman è un metodo con cui un'organizzazione fa costruire software ad AI Squad e lo governa con le pratiche di management che già utilizza.",
  lead="Eiraman è un metodo con cui un'organizzazione fa costruire software ad AI Squad e lo governa con le pratiche di management che già utilizza.",
  blocks=[("Contesto", "Il software su misura richiede investimenti elevati; l'uso dell'AI senza regole introduce rischi.",
           "Molte esigenze specifiche restano senza soluzione perché non giustificano lo sviluppo tradizionale. Nel frattempo l'AI viene usata in modo autonomo, senza un governo esplicito."),
          ("Approccio", "Le pratiche di management esistenti, applicate agli agenti AI.",
           "Obiettivi e mandato, delega, squadre, verifiche indipendenti e un resoconto periodico. La competenza degli sviluppatori è incorporata nelle regole che gli agenti seguono."),
          ("Risultato atteso", "Servizi IT su misura, con budget, rischi e prove dichiarati e verificati a ogni rilascio.",
           "È l'obiettivo del metodo; la sua efficacia è in corso di verifica nel pilota.")],
  btn="Leggi il metodo")
HOME7["en"].update(
  desc="Eiraman is a method through which an organisation has software built by teams of AI agents and governs it with the management practices it already uses.",
  lead="Eiraman is a method through which an organisation has software built by teams of AI agents and governs it with the management practices it already uses.",
  blocks=[("Context", "Bespoke software requires high investment; using AI without rules introduces risk.",
           "Many specific needs remain unmet because they do not justify traditional development. Meanwhile AI is used independently, without explicit governance."),
          ("Approach", "Existing management practices, applied to AI agents.",
           "Objectives and mandate, delegation, teams, independent checks and a periodic report. Developers' expertise is built into the rules the agents follow."),
          ("Expected outcome", "Bespoke IT services, with budget, risks and evidence declared and checked at every release.",
           "This is the aim of the method; its effectiveness is being verified in the pilot.")],
  btn="Read the method")

# --- Panoramica del metodo ---
METHOD["it"].update(
  why="Eiraman riprende le pratiche del management tradizionale e le applica al lavoro degli agenti AI: chi decide governa gli agenti come governa un'organizzazione.",
  explore_h="Componenti del metodo",
  explore_p="Tredici pagine, dalla più generale alla più tecnica. Ognuna indica la pratica di management da cui deriva.")
METHOD["en"].update(
  why="Eiraman takes the practices of traditional management and applies them to the work of AI agents: those who decide govern the agents as they govern an organisation.",
  explore_h="Components of the method",
  explore_p="Thirteen pages, from the most general to the most technical. Each states the management practice it derives from.")
_T(METHOD, ["cols", 0, 2], "Il business può già far scrivere software all'AI. Mancano regole su chi decide, su quando un lavoro è concluso e su quanto costa.",
   "Business can already have AI write software. What is missing are rules on who decides, on when work is finished and on what it costs.")
_T(METHOD, ["cols", 1, 2], "Il responsabile di business decide prima, con un mandato. L'AI Squad svolge tutte le fasi e risolve ciò che si può annullare. Al responsabile salgono le decisioni irreversibili e le riserve, espresse in termini di business.",
   "The business owner decides up front, with a mandate. The agent team carries out every phase and settles what can be undone. Irreversible decisions and reserved matters are escalated to the owner, expressed in business terms.")
for _i, _it, _en in [(3, "AI Squad per pacchetto, Scrum Master AI", "Agent teams per package, AI Scrum Master"),
                     (4, "Più modelli divergono, un analista converge", "Several models diverge, one analyst converges"),
                     (5, "Backbone, Brain, interfacce, Hairs", "Backbone, Brain, interfaces, Hairs"),
                     (9, "Test eseguiti da agenti indipendenti, sicurezza dalla progettazione", "Tests run by independent agents, security by design"),
                     (1, "Delega per reversibilità; il silenzio non vale come approvazione", "Delegation by reversibility; silence does not count as approval")]:
    _T(METHOD, ["mg", _i, 2], _it, _en)

# --- Pratiche ripensate (tabella della panoramica) ---
PRACT["it"].update(p="Gli agenti eseguono le pratiche; il responsabile di business resta chi le governa.", you="Ruolo del responsabile di business")
PRACT["en"].update(p="Agents execute the practices; the business owner remains the one who governs them.", you="Business owner's role")
for _i, (_a, _b) in enumerate([("Redige il mandato.", "Drafts the mandate."), ("Decide ciò che non si può annullare.", "Decides what cannot be undone."),
                               ("Approva budget e livello.", "Approves budget and level."), ("Riceve una revisione per ciclo, senza riunioni.", "Receives one review per cycle, without meetings."),
                               ("Approva la Visione ai gate.", "Approves the Vision at the gates."), ("Approva Principi e Decisioni.", "Approves Principles and Decisions."),
                               ("Sceglie la classe del progetto.", "Chooses the project class."), ("Accetta il risultato.", "Accepts the result."),
                               ("Consulta gli esiti, senza dettagli tecnici.", "Reviews the results, without technical detail."), ("Legge e approva il ciclo.", "Reads and approves the cycle.")]):
    _T(PRACT, ["rows", _i, 5], _a, _b)
_T(PRACT, ["rows", 1, 4], "Ciò che si può annullare lo decide l'AI Squad; ciò che non si può annullare, il responsabile di business.", "What can be undone is decided by the agent team; what cannot, by the business owner.")

# --- Pagina dei framework ---
FWPAGE["it"].update(why="Le pratiche di management esistenti restano valide. Il metodo le rilegge per AI Squad; il responsabile di business continua a governarle.",
                    idx_p="Framework tradizionale → riletto per gli agenti. Per ciascuno: l'originale, che cosa resta, che cosa cambia e perché, il ruolo del responsabile di business, le regole.",
                    more="Dettagli")
FWPAGE["en"].update(why="Existing management practices remain valid. The method rereads them for agent teams; the business owner continues to govern them.",
                    idx_p="Traditional framework → reread for agents. For each: the original, what stays, what changes and why, the business owner's role, the rules.",
                    more="Details")
FWPAGE["it"]["lab"]["you"] = "Ruolo del responsabile di business"; FWPAGE["en"]["lab"]["you"] = "Business owner's role"
_T(FWPAGE, ["fws", 0, "you"], "Porta contributi ai gate e approva la Visione.", "Brings input at the gates and approves the Vision.")
_T(FWPAGE, ["fws", 1, "you"], "Non partecipa a riunioni: riceve una revisione per ciclo.", "Attends no meetings: receives one review per cycle.")
_T(FWPAGE, ["fws", 1, "rules", 1, 0], "La retrospettiva ottimizza le squadre; i cambi di Decisione salgono al responsabile di business con una SWOT.", "The retrospective optimises teams; Decision changes are escalated to the business owner with a SWOT.")
_T(FWPAGE, ["fws", 2, "after", 1], "Non si può annullare: decide il responsabile di business", "Cannot be undone: the business owner decides")
_T(FWPAGE, ["fws", 2, "change", 1], "Un classificatore su un modello diverso stabilisce che cosa sale; nel dubbio, la decisione sale.", "A classifier on a different model determines what is escalated; when in doubt, the decision is escalated.")
_T(FWPAGE, ["fws", 2, "change", 2], "Si misurano le decisioni non salite che dovevano salire e quelle salite senza motivo.", "Decisions that should have been escalated and were not, and those escalated needlessly, are measured.")
_T(FWPAGE, ["fws", 2, "you"], "Decide ciò che non si può annullare e le riserve del mandato.", "Decides what cannot be undone and the matters reserved in the mandate.")
_T(FWPAGE, ["fws", 2, "rules", 1, 0], "Delegate: porte a due vie agli agenti. Do: porte a una via al responsabile di business.", "Delegate: two-way doors to agents. Do: one-way doors to the business owner.")
_T(FWPAGE, ["fws", 2, "sub"], "Ciò che si può annullare lo decide l'AI Squad; ciò che non si può annullare, il responsabile di business.", "What can be undone is decided by the agent team; what cannot, by the business owner.")
_T(FWPAGE, ["fws", 3, "you"], "Approva Principi e Decisioni con impatto di business.", "Approves Principles and Decisions with business impact.")
_T(FWPAGE, ["fws", 4, "after", 2], "UAT con il responsabile di business", "UAT with the business owner")
_T(FWPAGE, ["fws", 5, "change", 0], "Gli agenti lavorano in Wave brevi; il responsabile di business riceve una sola revisione per ciclo.", "Agents work in short Waves; the business owner receives a single review per cycle.")
_T(FWPAGE, ["fws", 5, "you"], "Fissa il budget nel mandato e legge ogni settimana una riga di costi: spesa, costo per risultato accettato, scostamento.", "Sets the budget in the mandate and reads one line of costs each week: spend, cost per accepted result, drift.")
_T(FWPAGE, ["fws", 5, "new"], "Reporting in una pagina e controllo dei costi", "One-page reporting and cost control")
_T(FWPAGE, ["fws", 5, "sub"], "Con gli agenti il costo non è più il tempo delle persone: sono token, motori, tentativi e proposte scartate. Il metodo lo registra e lo governa come un budget di progetto.", "With agents, cost is no longer people's time: it is tokens, engines, attempts and discarded proposals. The method records it and governs it like a project budget.")

# --- Livelli ---
LEVELS["it"].update(up_h="Passaggio a un livello superiore", ex_h="Esempio: un'idea che cresce", details_h="Dettagli normativi",
                    down="Se un requisito decade, il progetto scende automaticamente di livello: fino al ripristino sono ammessi solo rilasci correttivi.")
LEVELS["en"].update(up_h="Moving to a higher level", ex_h="Example: an idea that grows", details_h="Normative details",
                    down="If a requirement lapses, the project automatically drops a level: until it is restored, only corrective releases are allowed.")
_T(LEVELS, ["up", 0, 1], "Risultati dimostrati", "Results demonstrated")
_T(LEVELS, ["up", 1, 1], "Requisiti aggiuntivi soddisfatti", "Additional requirements met")
_T(LEVELS, ["up", 2, 1], "Decisione del responsabile di business", "Business owner's decision")
_T(LEVELS, ["levels", 0, "who"], "Solo chi lo costruisce.", "Only its builder.")
_T(LEVELS, ["levels", 0, "ex", 1], "Un assistente per i propri documenti", "An assistant for one's own documents")
_T(LEVELS, ["levels", 1, "who"], "I colleghi della stessa organizzazione.", "Colleagues in the same organisation.")
_T(LEVELS, ["story", 0, 1], "Strumento personale", "Personal tool")
_T(LEVELS, ["story", 0, 2], "Un assistente che prepara il riepilogo settimanale delle proprie riunioni.", "An assistant that prepares the weekly summary of one's own meetings.")
_T(LEVELS, ["story", 1, 1], "Uso nel team", "Team use")

# --- Originalità ---
ORIG["it"].update(h1="Elementi originali e riferimenti", proof_btn="I progetti sviluppati con il metodo")
ORIG["en"].update(h1="Original elements and references", proof_btn="Pilot data")
_T(ORIG, ["own", 2, 2], "Si accetta il software e, separatamente, ciò che il software produce.", "The software is accepted and, separately, what the software produces.")

# --- Etichette comuni ---
UI["it"].update(specref="Riferimento nella specifica", explore="Componenti")
UI["en"].update(specref="Reference in the specification", explore="Components")

# ===================== Correzioni (25 novembre 2026) =====================
# 1. §06 framework: «spese sconosciute, mai zero» non è nella specifica 0.3 → tolto dalle regole; rimandi corretti
for _L, _rules in (("it", [
        ("Ciclo di governo a cadenza fissa; circa tre decisioni e trenta minuti come riferimento.", "ritmo", "s5"),
        ("Tetto di spesa per Wave: avviso all'80%, blocco del nuovo lavoro al 100%; criteri di arresto per spesa nel mandato.", "ritmo", "s5"),
        ("Costo per incremento accettato rispetto all'esecutore singolo; il consuntivo include le candidate scartate.", "qualita", "s6"),
        ("Unit Cost per profilo e per motore, anche locale.", "squadre", "s4bis"),
        ("Budget di deriva cumulativo sul progetto, riportato a ogni ciclo.", "decisioni", "s3"),
        ("Rendiconto separato tra costi di sviluppo e costi di utilizzo.", "documenti", "s8"),
        ("Prima le cattive notizie e controllo di completezza bloccante; una pagina per scheda decisione.", "documenti", "s8")]),
     ("en", [
        ("Governance cycle at a fixed cadence; about three decisions and thirty minutes as a reference.", "ritmo", "s5"),
        ("Spending cap per Wave: warning at 80%, new work blocked at 100%; spending stop criteria in the mandate.", "ritmo", "s5"),
        ("Cost per accepted increment compared with a single executor; the final account includes discarded candidates.", "qualita", "s6"),
        ("Unit Cost per profile and per engine, local ones too.", "squadre", "s4bis"),
        ("Cumulative drift budget on the project, reported every cycle.", "decisioni", "s3"),
        ("Separate accounts for development and running costs.", "documenti", "s8"),
        ("Bad news first and a blocking completeness check; one page per decision sheet.", "documenti", "s8")])):
    FWPAGE[_L]["fws"][5]["rules"] = _rules
COSTDASH["it"]["kpis"] = [("Costo per risultato accettato", "incluse le proposte scartate"), ("Sviluppo · Utilizzo", "rendiconti separati"), ("Convenzione del pilota", "spese non misurate indicate come sconosciute")]
COSTDASH["en"]["kpis"] = [("Cost per accepted result", "discarded proposals included"), ("Development · Running", "separate accounts"), ("Pilot convention", "unmeasured spend shown as unknown")]
# 2. Livelli
_T(LEVELS, ["levels", 0, "ex", 1], "Il riordino delle proprie note e dei propri documenti", "Tidying one's own notes and documents")
_T(LEVELS, ["story", 0, 2], "Un assistente che riordina le proprie note e i propri documenti.", "An assistant that tidies one's own notes and documents.")
LEVELS["it"]["out"]["items"] = ["Dati particolari (come salute o opinioni) e giudiziari", "Dati di minori", "Pagamenti gestiti in proprio",
                                "Decisioni automatiche su persone", "AI ad alto rischio", "Software distribuito da installare",
                                "Trattamenti su larga scala, normative di settore, sicurezza fisica e altri casi: vedi l'elenco completo"]
LEVELS["en"]["out"]["items"] = ["Special-category data (such as health or opinions) and criminal-record data", "Children's data", "Payments handled in-house",
                                "Automated decisions about people", "High-risk AI", "Distributed software to be installed",
                                "Large-scale processing, sector regulations, physical safety and other cases: see the full list"]
COMP["livelli"]["it"]["how"] = "La classe di un progetto dipende da chi userà il risultato: solo chi lo costruisce, i colleghi, oppure clienti esterni; non può superare il livello di chi adotta il metodo. Prima di iniziare e a ogni ciclo di lavoro un controllo verifica che il progetto resti nella sua classe; nel dubbio, il lavoro si ferma."
COMP["livelli"]["en"]["how"] = "A project's class depends on who will use the result: only its builder, colleagues, or external customers; it cannot exceed the level of whoever adopts the method. Before starting and at every work cycle a check verifies that the project stays within its class; when in doubt, work stops."
# 3. Shadow IT: «riduce», non «toglie»
for _L, _old, _new in (("it", "Togliamo la complessità dei cicli di review architetturali e il rischio di shadow IT.", "Si riducono la complessità dei cicli di review architetturali e il rischio di shadow IT."),
                       ("en", "We remove the complexity of architecture review cycles and the risk of shadow IT.", "The complexity of architecture review cycles and the risk of shadow IT are reduced.")):
    for _fw in FWPAGE[_L]["fws"]:
        if isinstance(_fw.get("change"), list):
            _fw["change"] = [(_new if x == _old else x) for x in _fw["change"]]
        if _fw.get("you", "").startswith(("Approvi Principi", "Approve Principles")):
            _fw["you"] = "Approva Principi e Decisioni con impatto di business." if _L == "it" else "Approves Principles and Decisions with business impact."
# 4. Classe del progetto
_T(PRACT, ["rows", 6, 5], "Approva la classe del progetto, proposta dal controllo di applicabilità.", "Approves the project class proposed by the applicability check.")
# 5. Home: risultato atteso
HOME7["it"]["blocks"][2] = ("Risultato atteso", "Servizi IT su misura, con un tetto di spesa, rischi limitati in partenza e prove verificate a ogni rilascio.",
                            "È l'obiettivo del metodo; la sua efficacia è in corso di verifica nel pilota.")
HOME7["en"]["blocks"][2] = ("Expected outcome", "Bespoke IT services, with a spending cap, risks limited from the outset and evidence checked at every release.",
                            "This is the aim of the method; its effectiveness is being verified in the pilot.")

# ===================== Bilanciamento: una frase forte per pagina, numeri-chiave in home =====================
HOME7["it"].update(keys_label="Parametri del metodo",
  keys=[("1", "Chi decide legge una revisione di una pagina a settimana."), ("0", "Gli agenti lavorano; nessun lavoro si chiude senza una prova."), ("3", "Tre livelli: per sé, per il proprio team, per i clienti.")])
HOME7["en"].update(keys_label="Parameters of the method",
  keys=[("1", "The decision-maker reads a one-page review each week."), ("0", "Agents do the work; nothing is closed without evidence."), ("3", "Three levels: for oneself, for one's team, for customers.")])
_CLAIM = {
 "principi": ("Ogni regola del metodo discende da otto principi.", "Every rule of the method derives from eight principles."),
 "ruoli": ("Ognuno risponde di ciò che decide.", "Everyone is accountable for what they decide."),
 "fasi": ("Gli agenti svolgono tutte le fasi; le decisioni previste restano a una persona.", "Agents carry out every phase; the planned decisions remain with a person."),
 "decisioni": ("Ciò che non si può annullare lo decide una persona.", "What cannot be undone is decided by a person."),
 "qualita": ("Nessun lavoro si chiude senza una prova.", "No piece of work closes without evidence."),
 "ritmo": ("Il responsabile di business legge una pagina a settimana. Gli agenti fanno il resto, e lo documentano.", "The business owner reads one page a week. The agents do the rest, and document it."),
 "livelli": ("Più persone useranno il risultato, più garanzie servono.", "The more people will use the result, the more safeguards are needed."),
 "documenti": ("Ogni documento per il responsabile di business apre con ciò che non va.", "Every document for the business owner opens with what is wrong."),
 "profili": ("La competenza si scrive una volta e serve molti progetti.", "Expertise is written once and serves many projects."),
 "sicurezza": ("Ciò che è vietato deve bloccarlo l'ambiente, non l'agente.", "What is forbidden must be blocked by the environment, not by the agent."),
 "squadre": ("Un'AI Squad per ogni pacchetto di lavoro.", "One agent team for every work package."),
 "architettura": ("Con l'AI aggiungere componenti è facile: per questo la priorità conta di più.", "With AI, adding components is easy: that is why priority matters more."),
 "scoperta": ("Molte ipotesi, una sola Visione approvata.", "Many hypotheses, one approved Vision."),
}
for _k, (_i, _e) in _CLAIM.items():
    COMP[_k]["it"]["claim"] = _i; COMP[_k]["en"]["claim"] = _e
# Nota di stato: la regola del metodo non è ancora un blocco tecnico nel kit di avvio
COMP["sicurezza"]["it"]["status"] = ("Questa è la regola del metodo. Nel kit di avvio attuale i divieti sono istruzioni seguite dal Coordinatore AI, "
                                     "non ancora un blocco tecnico dell'ambiente: il blocco tecnico è un lavoro aperto.")
COMP["sicurezza"]["en"]["status"] = ("This is the rule of the method. In the current start-up kit the prohibitions are instructions followed by the AI Coordinator, "
                                     "not yet a technical block in the environment: the technical block is open work.")
FWPAGE["it"]["why"] = "Le pratiche di management restano valide. Il metodo le rilegge per AI Squad, e chi le governa resta una persona."
FWPAGE["en"]["why"] = "Management practices remain valid. The method rereads them for agent teams, and the one who governs them remains a person."
ABOUT["it"]["back"] = "Panoramica del metodo"; ABOUT["en"]["back"] = "Method overview"
for _L, _v in (("it", "Panoramica del metodo"), ("en", "Method overview")):
    for _k, _x in list(FWPAGE[_L].items()):
        if _x in ("Esplora il metodo", "Explore the method"):
            FWPAGE[_L][_k] = _v

HOME4["it"]["invite_btn"] = "Panoramica del metodo"; HOME4["en"]["invite_btn"] = "Method overview"

# ---------- COME USARLO ----------
SLUG["uso"] = ("come-usarlo", "how-to-use")
UI["it"]["nav"].insert(2, ("uso", "Come usarlo"))
UI["en"]["nav"].insert(2, ("uso", "How to use it"))
USO = {
 "it": dict(
  title="Come usarlo · Eiraman", desc="Come si avvia un progetto Eiraman e come il Manager umano lo governa dalla Vista del Manager.",
  crumb="Come usarlo", h1="Come usarlo",
  why="Governi il progetto da una pagina, senza leggere il codice: vedi che cosa è pronto, che cosa costa e che cosa aspetta una tua decisione.",
  how_h="Come si avvia",
  steps=[("layers", "Apri una cartella vuota", "Installa Claude Code o Codex e avvialo in una cartella vuota, che conterrà il tuo progetto."),
         ("gear", "Incolla il prompt di avvio", "Un solo prompt da copiare: il Coordinatore AI scarica il pacchetto nella cartella, ne verifica l'impronta e assume il suo ruolo."),
         ("bulb", "Descrivi la tua richiesta", "In linguaggio di business: problema, utenti, beneficio, vincoli e criterio di successo. Il Coordinatore AI chiarisce e ti propone la Visione."),
         ("stamp", "Approva il mandato", "Il Coordinatore AI ti propone in una pagina classe, budget, deleghe e riserve. Finché non lo approvi, nessun lavoro esecutivo parte."),
         ("manager", "Governa dalla Vista", "Il Coordinatore AI apre la Vista del Manager e la aggiorna mentre lavora. Rispondi alle decisioni nella chat della sessione.")],
  what_h="Che cosa vedi nella Vista del Manager",
  what=[("alert", "Prima le cattive notizie", "Prove fallite, rischi, decisioni scadute e soglie di budget superate, in apertura."),
        ("calendar", "Decisioni per te", "Ogni decisione con opzioni, raccomandazione, scadenza e che cosa succede se non rispondi."),
        ("coin", "Budget", "Spesa sul tetto, con avviso all'80% e blocco al 100%. Ciò che non è misurato resta «sconosciuto»."),
        ("steps", "Albero del progetto", "I Work Package completati, in corso con la percentuale di completamento e da fare, con la stima di costo sui rami. Cliccando un pacchetto vedi deliverable e AI Squad per Role Profile."),
        ("doc", "Documenti di progetto", "Mandato, High Level Architectural View, piano, decisioni, rischi e revisioni del ciclo, in linguaggio di business."),
        ("building", "Vista architetturale", "Di quali parti è fatto il prodotto: pagine web, dove stanno i dati, servizi esterni, che cosa esce dall'organizzazione. Senza sistemi operativi né versioni.")],
  tree_h="L'albero del progetto (esempio illustrativo)",
  tree_label="Albero di esempio: il progetto si divide in due Wave; ogni Work Package mostra lo stato e, sul ramo, la stima di costo.",
  own_h="La forma della vista la decidi tu",
  own=["La Vista del Manager è un punto di partenza, non un modello obbligato. In logica Scrum, ogni progetto e ogni manager decidono la forma degli artefatti che usano per il controllo.",
       "Puoi chiedere al Coordinatore AI di aggiungere, togliere o riorganizzare sezioni, indicatori e documenti nel ciclo di sviluppo e controllo dell'applicazione. La scelta si registra come una delle decisioni di progetto.",
       "Restano fermi i contenuti minimi del metodo: le cattive notizie in apertura, le decisioni con scadenza, il budget e lo stato di ogni pacchetto."],
  state="Il kit di avvio è in qualificazione nel progetto pilota: il Role Profile del Coordinatore AI resta una bozza finché un revisore esperto non lo qualifica.",
  back="Leggi il metodo"),
 "en": dict(
  title="How to use it · Eiraman", desc="How to start an Eiraman project and how the Human Manager governs it from the Manager view.",
  crumb="How to use it", h1="How to use it",
  why="You govern the project from one page, without reading code: you see what is ready, what it costs and what is waiting for your decision.",
  how_h="How to start",
  steps=[("layers", "Open an empty folder", "Install Claude Code or Codex and start it in an empty folder that will hold your project."),
         ("gear", "Paste the start-up prompt", "A single prompt to copy: the AI Coordinator downloads the package into the folder, checks its fingerprint and takes on its role."),
         ("bulb", "Describe your request", "In business language: problem, users, benefit, constraints and success criterion. The AI Coordinator clarifies and proposes the Vision."),
         ("stamp", "Approve the mandate", "The AI Coordinator proposes, on one page, class, budget, delegations and reserved matters. Until you approve it, no execution work starts."),
         ("manager", "Govern from the view", "The AI Coordinator opens the Manager view and keeps it updated while it works. You answer decisions in the session chat.")],
  what_h="What you see in the Manager view",
  what=[("alert", "Bad news first", "Failed tests, risks, overdue decisions and budget thresholds crossed, at the top."),
        ("calendar", "Decisions for you", "Each decision with options, recommendation, deadline and what happens if you do not answer."),
        ("coin", "Budget", "Spend against the cap, with a warning at 80% and a stop at 100%. What is not measured stays “unknown”."),
        ("steps", "Project tree", "Work Packages completed, in progress with their percentage, and to do, with the cost estimate on the branches. Click a package to see its deliverables and AI Squad by Role Profile."),
        ("doc", "Project documents", "Mandate, High Level Architectural View, plan, decisions, risks and cycle reviews, in business language."),
        ("building", "Architectural view", "What the product is made of: web pages, where the data lives, external services, what leaves the organisation. No operating systems or versions.")],
  tree_h="The project tree (illustrative example)",
  tree_label="Example tree: the project is split into two Waves; each Work Package shows its state and, on the branch, its cost estimate.",
  own_h="You decide the shape of the view",
  own=["The Manager view is a starting point, not a mandatory template. In Scrum terms, every project and every manager decide the shape of the artefacts they use for control.",
       "You can ask the AI Coordinator to add, remove or rearrange sections, indicators and documents within the application's development and control cycle. The choice is recorded as one of the project decisions.",
       "The method's minimum content stays fixed: bad news first, decisions with a deadline, the budget and the state of every package."],
  state="The start-up kit is being qualified in the pilot project: the AI Coordinator's Role Profile remains a draft until an expert reviewer qualifies it.",
  back="Read the method"),
}

# ---------- GUIDA OPERATIVA ANIMATA (Come usarlo) ----------
KIT_URL = None  # repository pubblico del kit, es. https://github.com/<proprietario>/eiraman-kit : si imposta alla pubblicazione
CC_URL = "https://docs.claude.com/en/docs/claude-code/overview"
CODEX_URL = "https://developers.openai.com/codex"
PY_URL = "https://www.python.org/downloads/"
KIT_ZIP = "https://eiraman.tech/kit/eiraman-kit.zip"  # pacchetto generato con il sito
def kit_zip(u): return KIT_ZIP
# {sha} è l'impronta SHA-256 dello zip, calcolata da build.py dopo aver costruito il pacchetto
AVVIO_IT = ("Questa cartella vuota conterrà il mio progetto. "
            "1) Scarica il pacchetto Eiraman dal sito {zip} e mettilo in questa cartella. "
            "Prima di estrarlo calcola lo SHA-256 del file: deve essere {sha}. Se è diverso, fermati e dimmelo. "
            "Se coincide, estraine qui il contenuto. "
            "2) Leggi CONTROLLORE.md e framework/Eiraman.md. "
            "3) Da ora sei il Coordinatore AI Eiraman di questo progetto e io sono il Manager umano: segui la procedura di avvio del profilo, apri la Vista del Manager e chiedimi la mia richiesta.")
AVVIO_EN = ("This empty folder will hold my project. "
            "1) Download the Eiraman package from the site {zip} and put it in this folder. "
            "Before extracting it, compute the file's SHA-256: it must be {sha}. If it differs, stop and tell me. "
            "If it matches, extract its content here. "
            "2) Read CONTROLLORE.md and framework/Eiraman.md. "
            "3) From now on you are the Eiraman AI Coordinator of this project and I am the Human Manager: follow the profile's start-up procedure, open the Manager view and ask me for my request.")
GUIDE = {
 "it": dict(
  hint="Passa con il mouse su un passo, oppure toccalo, per aprire la guida operativa.",
  close="Chiudi la guida", copy="Copia", copied="Copiato", dl="Scarica il pacchetto a mano (Role Profile CC BY 4.0, codice Apache 2.0)",
  need_h="Che cosa serve", need=["Claude Code oppure Codex, con il relativo abbonamento", "Python 3, per la Vista del Manager"],
  nokit="Il repository pubblico del kit è in preparazione: il prompt sarà utilizzabile dalla sua pubblicazione.",
  steps=[
   dict(t="Apri una cartella vuota", screen="terminal", wtitle="Terminale",
        lines=["$ mkdir mio-progetto", "$ cd mio-progetto", "$ claude", "● Pronto. Come posso aiutarti?"],
        items=[("Installa Claude Code oppure Codex seguendo la guida ufficiale.", "LINKS"),
               ("Crea una cartella vuota per il tuo progetto e avvia lì lo strumento: «claude» per Claude Code, «codex» per Codex.", "mkdir mio-progetto\ncd mio-progetto\nclaude")]),
   dict(t="Incolla il prompt di avvio", screen="folder", wtitle="mio-progetto",
        files=["CONTROLLORE.md", "STATO.md", "tools/vista_manager.py", "framework/Eiraman.md", "role-profiles/"],
        items=[("Copia questo prompt e incollalo nella sessione.", "AVVIO"),
               ("Il Coordinatore AI scarica il kit nella cartella, legge il proprio Role Profile e la specifica e assume il ruolo. Concedi soltanto questi permessi: scaricare quel file da eiraman.tech, calcolarne l'impronta, estrarlo e creare file dentro la cartella del progetto. Qualsiasi altra richiesta di permesso non fa parte dell'avvio.", None)]),
   dict(t="Descrivi la tua richiesta", screen="chat", wtitle="Sessione",
        bubbles=[("ai", "Sono il Coordinatore AI. Qual è la tua richiesta?"),
                 ("me", "Problema: le richieste di acquisto arrivano via email e alcune si perdono. Utenti: 15 colleghi degli acquisti. Beneficio: nessuna richiesta persa. Vincoli: 50 € al mese, entro gennaio. Successo: un mese senza richieste perse."),
                 ("ai", "Due domande: le richieste contengono dati personali oltre a nome e reparto? Serve l'accesso da telefono?"),
                 ("me", "Solo nome e reparto. Sì, anche da telefono."),
                 ("ai", "Progetto di classe 1: lo useranno colleghi della tua organizzazione. Avvio la Scoperta e ti propongo la Visione.")],
        items=[("Quando il Coordinatore AI te lo chiede, descrivi che cosa vuoi ottenere in linguaggio di business. Non serve sapere come sarà fatto il software. Puoi copiare questo schema:", "REQ"),
               ("Il Coordinatore AI ti fa poche domande di chiarimento, classifica il progetto e ti dice subito se è fuori perimetro, per esempio con dati sanitari.", None),
               ("L'esempio presuppone un'organizzazione già qualificata al livello 1: la prima adozione parte dal livello 0, con un progetto per uso proprio.", None),
               ("Poi avvia la Scoperta: più modelli esplorano il problema con il Design Thinking AI e ti propone la Visione, che puoi correggere prima del mandato.", None)]),
   dict(t="Approva il mandato", screen="chat", wtitle="Sessione",
        bubbles=[("ai", "Ti propongo il mandato: classe 1, budget 50 € al mese, ciclo settimanale. Le riserve restano a te."),
                 ("me", "Il budget va bene. Aggiungi tra le riserve l'invio di email esterne."),
                 ("ai", "Aggiunto. Approvi il mandato?"), ("me", "Approvo il mandato.")],
        items=[("Il Coordinatore AI ti propone il mandato in una pagina: classe, budget, deleghe, riserve, criteri di successo e di arresto.", None),
               ("Rispondi con parole tue: chiedi modifiche oppure scrivi «Approvo il mandato».", None),
               ("Finché non approvi, non parte nessun lavoro esecutivo. Il silenzio non vale mai come approvazione.", None)]),
   dict(t="Governa dalla Vista", screen="vista", wtitle="Vista del Manager",
        items=[("Il Coordinatore AI apre la Vista del Manager e la aggiorna mentre lavora.", None),
               ("In alto trovi le cattive notizie e le decisioni che ti aspettano, ciascuna con una scadenza.", None),
               ("Rispondi alle decisioni in chat, per esempio «Do-03: scelgo A». Nell'albero segui avanzamento e costi; nei documenti trovi mandato, architettura e piano.", None)])]),
 "en": dict(
  hint="Hover over a step, or tap it, to open the operational guide.",
  close="Close the guide", copy="Copy", copied="Copied", dl="Download the package manually (Role Profiles CC BY 4.0, code Apache 2.0)",
  need_h="What you need", need=["Claude Code or Codex, with its subscription", "Python 3, for the Manager view"],
  nokit="The public kit repository is being prepared: the prompt will work once it is published.",
  steps=[
   dict(t="Open an empty folder", screen="terminal", wtitle="Terminal",
        lines=["$ mkdir my-project", "$ cd my-project", "$ claude", "● Ready. How can I help?"],
        items=[("Install Claude Code or Codex following the official guide.", "LINKS"),
               ("Create an empty folder for your project and start the tool there: “claude” for Claude Code, “codex” for Codex.", "mkdir my-project\ncd my-project\nclaude")]),
   dict(t="Paste the start-up prompt", screen="folder", wtitle="my-project",
        files=["CONTROLLORE.md", "STATO.md", "tools/vista_manager.py", "framework/Eiraman.md", "role-profiles/"],
        items=[("Copy this prompt and paste it into the session.", "AVVIO"),
               ("The AI Coordinator downloads the kit into the folder, reads its Role Profile and the specification and takes on the role. Grant only these permissions: downloading that file from eiraman.tech, computing its fingerprint, extracting it and creating files inside the project folder. Any other permission request is not part of the start-up.", None)]),
   dict(t="Describe your request", screen="chat", wtitle="Session",
        bubbles=[("ai", "I am the AI Coordinator. What is your request?"),
                 ("me", "Problem: purchase requests arrive by email and some get lost. Users: 15 colleagues in purchasing. Benefit: no request lost. Constraints: €50 per month, by January. Success: one month with no lost requests."),
                 ("ai", "Two questions: do requests contain personal data beyond name and department? Is phone access needed?"),
                 ("me", "Only name and department. Yes, from phones too."),
                 ("ai", "Class 1 project: colleagues in your organisation will use it. I am starting Discovery and will propose the Vision.")],
        items=[("When the AI Coordinator asks, describe what you want to achieve in business language. You do not need to know how the software will be built. You can copy this outline:", "REQ"),
               ("The AI Coordinator asks a few clarifying questions, classifies the project and tells you straight away if it is out of scope, for example with health data.", None),
               ("The example assumes an organisation already qualified at level 1: a first adoption starts at level 0, with a project for one's own use.", None),
               ("Then it starts Discovery: several models explore the problem with AI Design Thinking, and it proposes the Vision, which you can correct before the mandate.", None)]),
   dict(t="Approve the mandate", screen="chat", wtitle="Session",
        bubbles=[("ai", "Here is the proposed mandate: class 1, budget €50 per month, weekly cycle. Reserved matters stay with you."),
                 ("me", "The budget is fine. Add sending external emails to the reserved matters."),
                 ("ai", "Added. Do you approve the mandate?"), ("me", "I approve the mandate.")],
        items=[("The AI Coordinator proposes the mandate on one page: class, budget, delegations, reserved matters, success and stop criteria.", None),
               ("Answer in your own words: ask for changes or write “I approve the mandate”.", None),
               ("Until you approve, no execution work starts. Silence never counts as approval.", None)]),
   dict(t="Govern from the view", screen="vista", wtitle="Manager view",
        items=[("The AI Coordinator opens the Manager view and keeps it updated while it works.", None),
               ("At the top you find bad news and the decisions waiting for you, each with a deadline.", None),
               ("Answer decisions in the chat, for example “Do-03: I choose A”. Follow progress and costs in the tree; the documents hold mandate, architecture and plan.", None)])]),
}

# ---------- ROLE PROFILE (pagina pubblica) ----------
SLUG["profili-ruolo"] = ("role-profile", "role-profiles")
UI["it"]["nav"].insert(3, ("profili-ruolo", "Role Profile"))
UI["en"]["nav"].insert(3, ("profili-ruolo", "Role Profiles"))
RP_FAM = [
 ("azure", "Azure", "Azure", "Progettare, costruire, proteggere e gestire soluzioni su Microsoft Azure.", "Design, build, secure and run solutions on Microsoft Azure.", "building"),
 ("aws", "AWS", "AWS", "Gli stessi ruoli per Amazon Web Services.", "The same roles for Amazon Web Services.", "building"),
 ("databricks", "Databricks", "Databricks", "Piattaforma dati: pipeline, governance, analisi e machine learning.", "Data platform: pipelines, governance, analytics and machine learning.", "layers"),
 ("finops", "FinOps", "FinOps", "Controllo dei costi del cloud e dei motori AI del progetto.", "Cost control for the cloud and for the project's AI engines.", "coin"),
 ("sviluppo", "Sviluppo", "Development", "Sviluppatori per linguaggio che seguono le regole del metodo e lo stile corretto di ogni linguaggio, con controlli automatici obbligatori.", "Language developers who follow the method's rules and each language's correct style, with mandatory automated checks.", "pen"),
 ("web-design", "Web design", "Web design", "Interfacce chiare e accessibili, con criteri di usabilità misurabili.", "Clear, accessible interfaces with measurable usability criteria.", "eye"),
 ("analisi-funzionale", "Analisi funzionale", "Functional analysis", "Dalla Visione ai requisiti, ai test e alla documentazione per il Manager umano.", "From the Vision to requirements, tests and documentation for the Human Manager.", "lens"),
 ("governo", "Governo", "Governance", "Sorveglianza del metodo in modo indipendente dal Coordinatore AI: segnalazioni al Coordinatore e al Manager umano, non comandi.", "Oversight of the method independently of the AI Coordinator: reports to the Coordinator and the Human Manager, not commands.", "shield"),
]
RPAGE = {
 "it": dict(title="Role Profile · Eiraman", desc="I Role Profile disponibili per le AI Squad di Eiraman, raggruppati per famiglia.",
   crumb="Role Profile", h1="Role Profile",
   why="La competenza specialistica sta nei Role Profile, non in ogni progetto. Ogni profilo porta in un agente le basi di una professione, le sue regole e i suoi limiti.",
   how_h="Come è fatto un Role Profile",
   how=[("doc", "Istruzioni del ruolo", "Un file per il motore AI: scopo, metodologie con le fonti, azioni consentite e vietate, regole di comunicazione, repository documentale."),
        ("gear", "Scheda tecnica", "Un file per il Coordinatore AI: motori abilitati, compiti per motore e livello di ragionamento, Unit Cost, qualificazione."),
        ("stamp", "Qualificazione", "Un profilo esce dalla bozza solo dopo una suite di casi a risposta nota e la firma di un revisore esperto diverso dall'autore.")],
   sd_h="Seniority Digitale", sd_p="Ogni agente lavora al livello di esperienza che il compito richiede, come in un'organizzazione. Il livello è dato dal motore e dal ragionamento con cui il Coordinatore AI lo attiva. Ogni profilo elenca i task che può ricevere, con il livello di ciascuno; un task fuori elenco si esegue a SD4.",
   sd_cols=("Livello", "Quando", "Esempio in Claude"),
   sd_rows=[("SD1 · Junior", "compiti ripetitivi verificabili da un controllo automatico", "Haiku, ragionamento basso"),
            ("SD2 · Professional", "lavoro corrente su specifica chiara", "Sonnet, ragionamento medio"),
            ("SD3 · Senior", "diagnosi, revisione, scelte locali", "Sonnet, ragionamento alto"),
            ("SD4 · Lead", "architettura, sicurezza, decisioni difficili da annullare; ripiego", "Opus, ragionamento alto"),
            ("SD5 · Principal", "problemi nuovi ad alto impatto, per eccezione", "Fable, ragionamento molto alto")],
   list_h="Profili disponibili", state="bozza non qualificata", n="profili", n1="profilo",
   rp_hint="Passa con il mouse su una famiglia, oppure toccala, per vedere i suoi profili.", close="Chiudi",
   ctrl_x="È il profilo che avvii con il prompt di «Come usarlo». Lavora sempre almeno a SD4 e sceglie il livello degli altri agenti dal loro catalogo.",
   pyr={"alto": "livello alto", "medio": "livello medio", "basso": "livello base"}, tasks="task nel catalogo", ex="Esempi di task",
   full="Il catalogo completo, con la configurazione per Claude Code, Codex e GitHub Copilot, è nel pacchetto del kit.",
   own="I profili sono un punto di partenza: ogni organizzazione li adatta alle proprie regole e li fa qualificare dai propri esperti.",
   git="Il dettaglio tecnico di ogni profilo è nel pacchetto del kit, scaricabile dalla pagina «Come usarlo»: Role Profile con licenza CC BY 4.0, codice con licenza Apache 2.0.", git_link="Apri il repository",
   ctrl="Coordinatore AI", ctrl_d="Conduce il progetto per conto del Manager umano: pianifica, assegna, verifica, chiude e rendiconta."),
 "en": dict(title="Role Profiles · Eiraman", desc="The Role Profiles available to Eiraman AI Squads, grouped by family.",
   crumb="Role Profiles", h1="Role Profiles",
   why="Specialist competence lives in Role Profiles, not in every project. Each profile brings into an agent the foundations of a profession, its rules and its limits.",
   how_h="What a Role Profile is made of",
   how=[("doc", "Role instructions", "A file for the AI engine: purpose, methods with sources, permitted and forbidden actions, communication rules, document repository."),
        ("gear", "Technical sheet", "A file for the AI Coordinator: enabled engines, tasks per engine and reasoning level, Unit Cost, qualification."),
        ("stamp", "Qualification", "A profile leaves draft status only after a suite of known-answer cases and the signature of an expert reviewer other than the author.")],
   sd_h="Digital Seniority", sd_p="Every agent works at the level of experience the task requires, as in an organisation. The level is set by the engine and the reasoning with which the AI Coordinator activates it. Every profile lists the tasks it can receive, with each one's level; a task outside the list runs at SD4.",
   sd_cols=("Level", "When", "Example in Claude"),
   sd_rows=[("SD1 · Junior", "repetitive tasks an automated check can verify", "Haiku, low reasoning"),
            ("SD2 · Professional", "routine work on a clear specification", "Sonnet, medium reasoning"),
            ("SD3 · Senior", "diagnosis, review, local choices", "Sonnet, high reasoning"),
            ("SD4 · Lead", "architecture, security, decisions hard to undo; fallback", "Opus, high reasoning"),
            ("SD5 · Principal", "new high-impact problems, by exception", "Fable, very high reasoning")],
   list_h="Available profiles", state="unqualified draft", n="profiles", n1="profile",
   rp_hint="Hover over a family, or tap it, to see its profiles.", close="Close",
   ctrl_x="It is the profile you start with the prompt in “How to use it”. It always works at SD4 or above and picks the other agents' level from their catalogue.",
   pyr={"alto": "senior tier", "medio": "middle tier", "basso": "base tier"}, tasks="tasks in the catalogue", ex="Example tasks",
   full="The full catalogue, with the configuration for Claude Code, Codex and GitHub Copilot, is in the kit package.",
   own="Profiles are a starting point: every organisation adapts them to its own rules and has its own experts qualify them.",
   git="The technical detail of each profile is in the kit package, downloadable from the “How to use it” page: Role Profiles under CC BY 4.0, code under Apache 2.0.", git_link="Open the repository",
   ctrl="AI Coordinator", ctrl_d="Runs the project on behalf of the Human Manager: plans, assigns, verifies, closes and reports."),
}

REQ_TEMPLATE = {
 "it": "Problema: che cosa non funziona oggi, e per chi.\nUtenti: chi userà il risultato (solo io, colleghi, clienti).\nBeneficio atteso: che cosa cambia quando funziona, se possibile con un numero.\nVincoli: budget, scadenza, dati che si possono o non si possono usare.\nSuccesso: come capirò che il lavoro è riuscito.",
 "en": "Problem: what does not work today, and for whom.\nUsers: who will use the result (only me, colleagues, customers).\nExpected benefit: what changes when it works, with a number if possible.\nConstraints: budget, deadline, data that may or may not be used.\nSuccess: how I will know the work succeeded.",
}

# ---------- I PROGETTI (dati al 25/11/2026, raccolti in sola lettura dai registri dei progetti) ----------
PROGETTI = {
 "it": dict(
  title="I progetti · Eiraman", desc="I progetti sviluppati con il metodo Eiraman, con i numeri: decisioni, Do, ruoli, Work Package e lavoro automatizzato.",
  crumb="I progetti", h1="I progetti",
  why="Un metodo si giudica da ciò che produce. Questi sono i progetti sviluppati con Eiraman, compreso il metodo stesso, con i numeri presi dai loro registri.",
  list_h="Progetti", hint="Passa con il mouse su un progetto, oppure toccalo, per vederne il dettaglio.", close="Chiudi",
  vision="Visione.", bad="Prima le cattive notizie",
  how_h="Come leggere i numeri",
  how=["Ogni numero viene dal registro del progetto, dalla storia delle versioni o dal conteggio delle sessioni di lavoro. Accanto c'è il grado di certezza: misurato (contato), ricostruito (dedotto incrociando le fonti) o stimato.",
       "Un Do è una decisione portata al Manager umano. Un Delegate è una decisione presa dagli agenti entro il mandato. Il rapporto tra lavoro automatico e interventi del Manager mostra quanto il progetto ha girato da solo.",
       "Un Work Package è un pacchetto di lavoro con obiettivo, criteri di accettazione e verifica; una Wave è un gruppo di pacchetti eseguiti insieme. Un Role Profile è la scheda professionale di un ruolo AI. Le fasi sono Scoperta, POC (prova di fattibilità), Design e planning, Scale (esecuzione) e Accettazione.",
       "I costi sono equivalenti a listino: il lavoro è avvenuto con abbonamenti già attivi, quindi la spesa reale aggiuntiva non è misurata e si dichiara sconosciuta. Dati al 25 novembre 2026."],
  items=[
   dict(name="NUR", icon="doc", state="sviluppato con Eiraman · in corso",
        short="Un'applicazione che trasforma una richiesta e poche fonti in un documento lungo, verificato e impaginato.",
        vision="Chi deve produrre un documento lungo e affidabile parte da una richiesta e da un piccolo fascicolo di fonti. NUR lo trasforma in un documento pronto da consegnare, con controlli che bloccano i difetti prima della stampa. Il progetto è stato sviluppato interamente con Eiraman, da zero, senza riusare il codice della versione precedente.",
        numbers=[("Work Package", "12", "misurato"), ("decisioni gestite", "13", "misurato"), ("Do al Manager umano", "8", "misurato"),
                 ("decise dagli agenti (Delegate)", "5", "misurato"), ("esecuzioni automatiche", "97", "misurato"),
                 ("interventi del Manager", "7", "misurato"), ("esecuzioni per intervento", "13,9", "misurato"), ("ruoli coinvolti", "5", "misurato")],
        bad=["Con il criterio iniziale del mandato (voto almeno 75 da due giudici) nessuno dei sei scenari era positivo. La soglia è stata portata a 70 dopo aver visto i voti, con una decisione esplicita del Manager.",
             "Le tre revisioni di sicurezza del codice fatte con un secondo motore hanno chiesto correzioni; l'ultima serie non è ancora stata riverificata.",
             "Il giudice Claude è della stessa famiglia del redattore: l'indipendenza piena viene dal secondo giudice, su un altro motore. La Scoperta ha avuto un'indipendenza solo di contesto.",
             "Il registro del progetto non è aggiornato in ogni parte e le ultime modifiche al codice non sono ancora salvate in una versione; il lavoro si è fermato circa due ore per il limite d'uso dell'abbonamento.",
             "Il collaudo finale con l'utente non è ancora iniziato."],
        sections=[
         ("Come funziona il deliverable", ["L'utente lavora da una pagina del browser servita dal proprio computer: scrive la richiesta e allega le fonti.",
                                         "Prima della stesura approva l'indice e una bozza dei contenuti, in cui ogni punto ha una fonte e una citazione verificata.",
                                         "Prima della stampa il programma controlla sezioni, tabelle senza celle vuote, valori dei grafici presenti nelle fonti e lunghezza dei capitoli. Un documento che non supera i controlli esce come bozza, non come definitivo."]),
         ("Come ha lavorato il metodo", ["Scoperta: tre agenti in parallelo hanno ricostruito specifiche, decisioni storiche e misure di partenza.",
                                        "POC: prova delle chiamate ai motori, del giudizio ripetibile e della stampa. Design e planning: il Manager ha scelto la tecnologia e approvato i principi.",
                                        "Scale: motore e interfaccia, revisioni di sicurezza, sei scenari generati e giudicati due volte da due motori diversi; poi correzioni mirate e sei esempi ripuliti per gli utenti."]),
         ("Ruoli coinvolti", ["Coordinatore AI; esploratori della Scoperta; redattore all'interno del prodotto; giudici esterni su due motori diversi (Claude e Codex); revisore di sicurezza su un motore diverso da quello dell'esecutore."]),
         ("Lavoro automatizzato", ["97 esecuzioni automatiche: 19 documenti generati, 72 sessioni di giudizio, 3 revisioni del codice, 3 agenti di esplorazione. Il Manager è intervenuto 7 volte: circa 14 esecuzioni per ogni suo intervento.",
                                  "Il 38% delle decisioni registrate è stato preso dagli agenti entro il mandato; tutte le altre sono andate al Manager come Do e hanno avuto risposta."]),
         ("Risultati", ["La versione precedente, sugli stessi sei scenari, aveva prodotto un solo documento, giudicato 30 e 49 su 100.",
                        "NUR sviluppato con Eiraman ha prodotto il documento in tutti e sei gli scenari. Negli esempi finali tre scenari superano anche il criterio iniziale (75), uno manca la soglia 70 di un punto e due restano bozze per numero di pagine; per uno dei due, inoltre, un giudizio non è andato a buon fine."]),
         ("Costo", ["Spesa reale: solo abbonamenti già attivi. Equivalente a listino della generazione dei documenti: circa 98 USD; il costo dei giudizi non è misurato."])],
        source="Fonti: registro del progetto (decisioni, run, esiti), storia delle versioni, sessioni di lavoro. Dati al 25/11/2026."),
   dict(name="Il metodo Eiraman", icon="layers", state="sviluppato con Eiraman · in corso",
        short="Il metodo stesso, gestito come un prodotto: specifica, Role Profile, Vista del Manager, sito e kit.",
        vision="Un metodo per far lavorare squadre di agenti AI sotto il governo di un manager umano deve restare coerente, verificabile e pubblicabile mentre cambia ogni giorno. Per questo Eiraman è gestito con Eiraman: ogni modifica della specifica e ogni pubblicazione è una decisione del Manager umano, ogni pacchetto chiuso passa da una revisione indipendente, il cui esito resta registrato.",
        numbers=[("Work Package", "39", "ricostruito"), ("decisioni del Manager (Do), di cui 3 aperte", "44", "ricostruito"), ("pubblicazioni verificate", "12", "ricostruito"),
                 ("agenti avviati", "45", "misurato"), ("revisioni indipendenti", "21", "misurato"), ("interventi del Manager", "117", "misurato"),
                 ("agenti per intervento", "0,4", "misurato"), ("Role Profile prodotti", "41", "misurato")],
        bad=["Il progetto ha richiesto molti interventi del Manager: il metodo veniva definito mentre si applicava, e ogni scelta di contenuto è una sua decisione.",
             "Le decisioni prese dagli agenti entro il mandato non sono state registrate: il numero dei Delegate è sconosciuto.",
             "Nove revisioni indipendenti hanno dato esito negativo prima delle correzioni. La famiglia di profili cloud e dati è stata chiusa senza un esito positivo finale e alcune correzioni non sono state riverificate. I Role Profile restano bozze non qualificate da un revisore esperto.",
             "La ricerca di anteriorità non è ancora stata fatta, e un conflitto di sincronizzazione delle cartelle ha costretto a spostare la generazione del sito.",
             "Le revisioni sono state fatte da agenti dello stesso fornitore dell'autore: un'indipendenza limitata."],
        sections=[
         ("Come funziona il deliverable", ["La specifica descrive come un Manager umano affida il lavoro a un Coordinatore AI e alle sue AI Squad, con decisioni, livelli e prove.",
                                         "Il registro dei Role Profile contiene 40 profili in 7 famiglie più il Coordinatore AI, con 350 task catalogati e la Seniority Digitale che sceglie motore e ragionamento.",
                                         "La Vista del Manager mostra decisioni, budget, albero del lavoro e documenti. Un pacchetto scaricabile è progettato per avviare il metodo in un nuovo progetto con un solo prompt (il percorso completo con un LLM non è ancora stato provato); il sito bilingue viene pubblicato solo dopo il via del Manager, verificando ogni file online."]),
         ("Come ha lavorato il metodo", ["Wave pilota e Wave di avvio: valutazione della proposta e prima specifica.",
                                        "W2: raffinamento con le decisioni su responsabilità, livelli, escalation e meccanismi concorrenziali; specifica 0.2.",
                                        "W3 e seguenti: pubblicazione del sito, Role Profile del Coordinatore AI, pilota NUR, specifica 0.3, Vista del Manager, registro dei Role Profile con sette Work Package in parallelo, Seniority Digitale."]),
         ("Ruoli coinvolti", ["Coordinatore AI; revisori indipendenti senza contesto; web designer; autori dei Role Profile, uno per famiglia; ricercatore. Il revisore esperto umano dei profili è ancora da nominare."]),
         ("Lavoro automatizzato", ["45 agenti avviati, di cui 20 esecutori, 21 revisori indipendenti e 4 agenti nella Wave pilota. 117 interventi del Manager: circa un agente ogni tre interventi.",
                                  "Ogni pubblicazione del sito è stata verificata confrontando l'impronta di ogni file online con quella generata."]),
         ("Costo", ["Spesa reale: solo abbonamenti già attivi. Equivalente a listino del lavoro di coordinamento misurato: circa 156 USD, dato parziale."])],
        source="Fonti: piano delle attività, registro delle decisioni, storia delle versioni, sessioni di lavoro. Il numero dei Work Package e dei Do è ricostruito dal piano. Dati al 25/11/2026."),
  ]),
 "en": dict(
  title="Projects · Eiraman", desc="Projects developed with the Eiraman method, with the numbers: decisions, Dos, roles, Work Packages and automated work.",
  crumb="Projects", h1="Projects",
  why="A method is judged by what it produces. These are the projects developed with Eiraman, the method itself included, with numbers taken from their records.",
  list_h="Projects", hint="Hover over a project, or tap it, to see the details.", close="Close",
  vision="Vision.", bad="Bad news first",
  how_h="How to read the numbers",
  how=["Every number comes from the project record, the version history or a count of the work sessions. Next to it is its certainty: measured (counted), reconstructed (inferred by cross-checking sources) or estimated.",
       "A Do is a decision taken to the Human Manager. A Delegate is a decision taken by the agents within the mandate. The ratio between automated work and Manager interventions shows how far the project ran on its own.",
       "A Work Package is a unit of work with goal, acceptance criteria and verification; a Wave is a group of packages run together. A Role Profile is the professional sheet of an AI role. The phases are Discovery, POC (feasibility test), Design and planning, Scale (execution) and Acceptance.",
       "Costs are list-price equivalents: the work ran on subscriptions already in place, so the actual extra spend is not measured and is declared unknown. Data as of 25 November 2026."],
  items=[
   dict(name="NUR", icon="doc", state="developed with Eiraman · in progress",
        short="An application that turns a request and a few sources into a long, verified, typeset document.",
        vision="People who must produce a long, reliable document start from a request and a small file of sources. NUR turns them into a document ready to deliver, with checks that block defects before printing. The project was developed entirely with Eiraman, from scratch, without reusing the previous version's code.",
        numbers=[("Work Packages", "12", "measured"), ("decisions handled", "13", "measured"), ("Dos to the Human Manager", "8", "measured"),
                 ("decided by agents (Delegate)", "5", "measured"), ("automated runs", "97", "measured"),
                 ("Manager interventions", "7", "measured"), ("runs per intervention", "13.9", "measured"), ("roles involved", "5", "measured")],
        bad=["Under the mandate's initial criterion (a score of at least 75 from two judges) none of the six scenarios passed. The threshold was moved to 70 after the scores were seen, by an explicit Manager decision.",
             "The three code security reviews done with a second engine asked for fixes; the last set has not been re-verified yet.",
             "The Claude judge belongs to the same family as the writer: full independence comes from the second judge, on another engine. Discovery had context-only independence.",
             "The project record is not up to date in every part and the latest code changes are not yet saved in a version; work stopped for about two hours because of the subscription usage limit.",
             "Final acceptance testing with the user has not started yet."],
        sections=[
         ("How the deliverable works", ["The user works from a browser page served by their own computer: they write the request and attach the sources.",
                                       "Before drafting they approve the outline and a content draft, where every point has a source and a verified quotation.",
                                       "Before printing the program checks sections, tables without empty cells, chart values present in the sources and chapter length. A document that fails the checks is issued as a draft, not as final."]),
         ("How the method worked", ["Discovery: three agents in parallel rebuilt specifications, past decisions and baseline measures.",
                                   "POC: tests of engine calls, repeatable judging and printing. Design and planning: the Manager chose the technology and approved the principles.",
                                   "Scale: engine and interface, security reviews, six scenarios generated and judged twice by two different engines; then targeted fixes and six cleaned examples for users."]),
         ("Roles involved", ["AI Coordinator; Discovery explorers; writer inside the product; external judges on two different engines (Claude and Codex); security reviewer on an engine different from the executor's."]),
         ("Automated work", ["97 automated runs: 19 documents generated, 72 judging sessions, 3 code reviews, 3 exploration agents. The Manager intervened 7 times: about 14 runs per intervention.",
                             "38% of recorded decisions were taken by agents within the mandate; all others went to the Manager as Dos and were answered."]),
         ("Results", ["The previous version, on the same six scenarios, had produced a single document, scored 30 and 49 out of 100.",
                      "NUR developed with Eiraman produced the document in all six scenarios. In the final examples three scenarios also meet the initial criterion (75), one misses the 70 threshold by one point and two remain drafts because of page count; for one of them a judgement also failed."]),
         ("Cost", ["Actual spend: only subscriptions already in place. List-price equivalent of document generation: about USD 98; the cost of judging is not measured."])],
        source="Sources: project record (decisions, runs, outcomes), version history, work sessions. Data as of 25/11/2026."),
   dict(name="The Eiraman method", icon="layers", state="developed with Eiraman · in progress",
        short="The method itself, managed as a product: specification, Role Profiles, Manager view, site and kit.",
        vision="A method for having AI agent teams work under the governance of a human manager must stay consistent, verifiable and publishable while it changes every day. That is why Eiraman is managed with Eiraman: every change to the specification and every publication is a Human Manager decision, every closed package goes through an independent review, whose outcome is recorded.",
        numbers=[("Work Packages", "39", "reconstructed"), ("Manager decisions (Do), 3 still open", "44", "reconstructed"), ("verified publications", "12", "reconstructed"),
                 ("agents started", "45", "measured"), ("independent reviews", "21", "measured"), ("Manager interventions", "117", "measured"),
                 ("agents per intervention", "0.4", "measured"), ("Role Profiles produced", "41", "measured")],
        bad=["The project needed many Manager interventions: the method was being defined while it was applied, and every content choice is the Manager's decision.",
             "Decisions taken by agents within the mandate were not recorded: the number of Delegates is unknown.",
             "Nine independent reviews failed before the fixes. The cloud and data profile family was closed without a final pass and some fixes were not re-verified. The Role Profiles remain drafts not qualified by an expert reviewer.",
             "The prior-art search has not been done yet, and a folder synchronisation conflict forced the site build to be moved.",
             "Reviews were done by agents from the author's own provider: limited independence."],
        sections=[
         ("How the deliverable works", ["The specification describes how a Human Manager entrusts work to an AI Coordinator and its AI Squads, with decisions, levels and evidence.",
                                       "The Role Profile registry holds 40 profiles in 7 families plus the AI Coordinator, with 350 catalogued tasks and the Digital Seniority that picks engine and reasoning.",
                                       "The Manager view shows decisions, budget, the work tree and documents. A downloadable package is designed to start the method in a new project with a single prompt (the full path with an LLM has not been tested yet); the bilingual site is published only after the Manager's go-ahead, verifying every file online."]),
         ("How the method worked", ["Pilot and start-up Waves: assessment of the proposal and first specification.",
                                   "W2: refinement with decisions on accountability, levels, escalation and competitive mechanisms; specification 0.2.",
                                   "W3 onwards: site publication, AI Coordinator Role Profile, NUR pilot, specification 0.3, Manager view, Role Profile registry with seven Work Packages in parallel, Digital Seniority."]),
         ("Roles involved", ["AI Coordinator; context-free independent reviewers; web designer; Role Profile authors, one per family; researcher. The human expert reviewer of the profiles is still to be appointed."]),
         ("Automated work", ["45 agents started: 20 executors, 21 independent reviewers and 4 agents in the pilot Wave. 117 Manager interventions: about one agent every three interventions.",
                             "Every site publication was verified by comparing each online file's fingerprint with the generated one."]),
         ("Cost", ["Actual spend: only subscriptions already in place. List-price equivalent of the measured coordination work: about USD 156, partial figure."])],
        source="Sources: activity plan, decision record, version history, work sessions. The number of Work Packages and Dos is reconstructed from the plan. Data as of 25/11/2026."),
  ]),
}
