import os
import re

curriculum_topics = [
    (1, "le-misure-e-le-grandezze", "Cap 1: Le misure e le grandezze", "Comprendere il Sistema Internazionale, gli errori di misura e le cifre significative.", "MisureGrandezzeLesson"),
    (1, "le-trasformazioni-fisiche-della-materia", "Cap 2: Le trasformazioni fisiche della materia", "Stati della materia, calore latente e passaggi di stato.", "TrasformazioniFisicheLesson"),
    (1, "dalle-trasformazioni-chimiche-alla-teoria-atomica", "Cap 3: Dalle trasformazioni chimiche alla teoria atomica", "Dalle reazioni macroscopiche alle leggi ponderali e l'atomo di Dalton.", "TeoriaAtomicaDaltonLesson"),
    (1, "la-teoria-cinetico-molecolare-e-le-leggi-dei-gas", "Cap 4: La teoria cinetico-molecolare e le leggi dei gas", "Comportamento dei gas perfetti e reali, modello cinetico.", "LeggiGasCineticaLesson"),
    (1, "rappresentare-le-reazioni-chimiche", "Cap 5: Rappresentare le reazioni chimiche", "Simbologia chimica, formule e bilanciamento elementare.", "RappresentareReazioniLesson"),

    (2, "le-particelle-dell-atomo", "Cap 6: Le particelle dell'atomo", "Elettroni, protoni, neutroni e modelli di Thomson e Rutherford.", "ParticelleAtomoLesson"),
    (2, "la-struttura-dell-atomo", "Cap 7: La struttura dell'atomo", "Modello di Bohr, meccanica quantistica e orbitali atomici.", "StrutturaAtomoLesson"),
    (2, "il-sistema-periodico", "Cap 8: Il sistema periodico", "Periodicità, proprietà periodiche ed elettronegatività.", "SistemaPeriodicoLesson"),
    (2, "i-legami-chimici", "Cap 9: I legami chimici", "Legami covalenti, ionici e metallici. Regola dell'ottetto.", "LegamiChimiciLesson"),
    (2, "la-forma-delle-molecole-e-le-forze-intermolecolari", "Cap 10: La forma delle molecole e le forze intermolecolari", "Geometria VSEPR e interazioni di van der Waals.", "FormaMolecoleLesson"),
    (2, "la-quantita-di-sostanza-in-moli", "Cap 11: La quantità di sostanza in moli", "Il concetto di mole, costante di Avogadro e calcoli stechiometrici.", "QuantitaSostanzaMoleLesson"),

    (3, "classificazione-e-nomenclatura-dei-composti", "Cap 12: Classificazione e nomenclatura dei composti", "Nomenclatura IUPAC e tradizionale dei composti inorganici.", "ClassificazioneCompostiLesson"),
    (3, "le-reazioni-chimiche-stechiometria-e-resa", "Cap 13: Le reazioni chimiche (stechiometria)", "Calcoli stechiometrici, reagente limitante e resa di reazione.", "ReazioniStechiometriaLesson"),
    (3, "le-proprieta-delle-soluzioni", "Cap 14: Le proprietà delle soluzioni", "Solubilità e proprietà colligative delle soluzioni.", "ProprietaSoluzioniLesson"),
    (3, "la-termodinamica", "Cap 15: La termodinamica", "Principi della termodinamica, entalpia, entropia e spontaneità.", "TermodinamicaLesson"),
    (3, "la-cinetica-e-l-equilibrio", "Cap 16: La cinetica e l'equilibrio", "Velocità di reazione, equazione di Arrhenius, principio di Le Châtelier.", "CineticaEquilibrioLesson"),

    (4, "la-concentrazione-e-la-molarita", "Cap 17: La concentrazione e la Molarità", "Molarità, molalità, frazione molare e calcoli sulle soluzioni.", "ConcentrazioneMolaritaLesson"),
    (4, "gli-acidi-e-le-basi", "Cap 18: Gli acidi e le basi", "Teorie di Arrhenius, Brønsted-Lowry e Lewis. Acidi forti e deboli.", "AcidiBasiLesson"),
    (4, "il-ph-e-gli-indicatori", "Cap 19: Il pH e gli indicatori", "Calcolo del pH, pOH, soluzioni tampone e titolazioni.", "PhIndicatoriLesson"),
    (4, "le-ossido-riduzioni", "Cap 20: Le ossido-riduzioni", "Numeri di ossidazione e bilanciamento delle reazioni redox.", "OssidoRiduzioniLesson"),
    (4, "l-elettrochimica", "Cap 21: L'elettrochimica", "Celle galvaniche, pile, equazione di Nernst ed elettrolisi.", "ElettrochimicaLesson"),

    (5, "dal-carbonio-agli-idrocarburi", "Cap 22: Dal carbonio agli idrocarburi", "Fondamenti di chimica organica, alcani, alcheni, alchini e aromatici.", "CarbonioIdrocarburiLesson"),
    (5, "i-gruppi-funzionali", "Cap 23: I gruppi funzionali", "Alcoli, chetoni, aldeidi, acidi carbossilici ed esteri.", "GruppiFunzionaliLesson"),
    (5, "le-biomolecole", "Cap 24: Le biomolecole", "Carboidrati, lipidi, proteine e acidi nucleici. Fondamenti di biochimica.", "BiomolecoleLesson"),
    (5, "polimeri-e-scienza-dei-materiali", "Cap 25: Polimeri e Scienza dei materiali", "Polimeri di sintesi, materiali compositi, ceramici e metallici.", "PolimeriMaterialiLesson"),
]

def generate_component_code(year, slug, title, subtitle, comp_name):
    topic_name = title.split(':')[1].strip() if ':' in title else title
    # Using raw strings for LaTeX math and properly escaping brackets for React
    return r'''"use client";

import React from "react";
import { LessonTemplate, MathEq } from "../LessonTemplate";

export function ''' + comp_name + r'''() {
  return (
    <LessonTemplate
      year={''' + str(year) + r'''}
      title="''' + title + r'''"
      subtitle="''' + subtitle + r'''"
      theoryPages={[
        {
          title: "1. Concetti Fondamentali",
          content: (
            <div className="space-y-6">
              <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 border-b border-zinc-200 dark:border-zinc-800 pb-2">Le Basi e le Definizioni</h3>
              <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
                Questo capitolo esplora le fondamenta di <strong>''' + topic_name + r'''</strong>.
                Non si tratta solo di definizioni mnemoniche, ma di comprendere il <em>perché</em> un fenomeno avviene e come lo misuriamo.
              </p>
              
              <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 my-6">
                <ul className="list-disc pl-6 space-y-4 text-zinc-700 dark:text-zinc-300 text-lg">
                  <li><strong>Definizione Rigorosa:</strong> Le fondamenta di ogni osservazione sperimentale.</li>
                  <li><strong>Unità di Misura e Variabili:</strong> Il sistema con cui quantifichiamo e controlliamo il fenomeno.</li>
                  <li><strong>Significato Fisico:</strong> Perché questa grandezza è vitale a livello sia macroscopico che microscopico.</li>
                </ul>
              </div>
              
              <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300 mt-4">
                La comprensione profonda di questo fenomeno distingue chi memorizza da chi realmente padroneggia la materia. 
                Quando la chimica moderna ha standardizzato questi elementi, si è aperta la strada allo sviluppo scientifico e tecnologico che conosciamo oggi.
              </p>
            </div>
          )
        },
        {
          title: "2. Approfondimento Analitico",
          content: (
            <div className="space-y-6">
              <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 border-b border-zinc-200 dark:border-zinc-800 pb-2">Svolgimento a Step e Dimostrazioni</h3>
              <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
                Analizziamo il comportamento del sistema suddividendolo in step chiari. Questo è il metodo analitico richiesto negli esami di alto livello.
              </p>

              <div className="my-6">
                <ol className="list-decimal pl-6 space-y-4 text-zinc-700 dark:text-zinc-300 text-lg">
                  <li><strong className="text-zinc-900 dark:text-zinc-100">Identificazione del Sistema:</strong> Determinare reagenti o stati fisici coinvolti inizialmente.</li>
                  <li><strong className="text-zinc-900 dark:text-zinc-100">L'Equazione di Stato:</strong> Applicazione del principio di conservazione.</li>
                  <li><strong className="text-zinc-900 dark:text-zinc-100">Analisi Differenziale:</strong> Osservare le variazioni infinitesimali o macroscopiche durante il processo.</li>
                  <li><strong className="text-zinc-900 dark:text-zinc-100">Conclusione Quantitativa:</strong> Determinare la resa o il valore finale attraverso la stechiometria.</li>
                </ol>
              </div>

              <h3 className="text-xl font-bold text-zinc-900 dark:text-zinc-50 mt-8">Casi Particolari ed Eccezioni</h3>
              <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
                La natura chimica non è sempre lineare. In questo argomento, esistono eccezioni cruciali:
              </p>
              <div className="bg-red-50 dark:bg-red-950/30 p-5 rounded-xl border border-red-100 dark:border-red-900 mt-4">
                <ul className="list-disc pl-6 space-y-2 text-red-900 dark:text-red-200 text-lg">
                  <li>Deviazioni dall'idealità (es. interazioni molecolari forti non trascurabili).</li>
                  <li>Condizioni di alta pressione o temperature estreme che alterano la cinetica del processo.</li>
                </ul>
              </div>
            </div>
          )
        },
        {
          title: "3. Formulario Matematico",
          content: (
            <div className="space-y-6">
              <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 border-b border-zinc-200 dark:border-zinc-800 pb-2">Formule Dirette e Inverse</h3>
              <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
                La modellizzazione matematica è indispensabile. Ecco le equazioni chiave da applicare nei calcoli:
              </p>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
                <div className="bg-zinc-50 dark:bg-zinc-900 p-6 border border-zinc-200 dark:border-zinc-800 rounded-xl flex flex-col items-center justify-center shadow-sm">
                  <p className="text-sm text-zinc-500 dark:text-zinc-400 mb-4 uppercase tracking-wider font-semibold">Variazione del Sistema</p>
                  <div className="text-2xl md:text-3xl text-indigo-600 dark:text-indigo-400 font-serif">
                    <MathEq math="\Delta G = \Delta H - T \Delta S" block />
                  </div>
                </div>
                
                <div className="bg-zinc-50 dark:bg-zinc-900 p-6 border border-zinc-200 dark:border-zinc-800 rounded-xl flex flex-col items-center justify-center shadow-sm">
                  <p className="text-sm text-zinc-500 dark:text-zinc-400 mb-4 uppercase tracking-wider font-semibold">Equazione di Proporzionalità</p>
                  <div className="text-2xl md:text-3xl text-indigo-600 dark:text-indigo-400 font-serif">
                    <MathEq math="K_c = \frac{[C]^c [D]^d}{[A]^a [B]^b}" block />
                  </div>
                </div>
              </div>
            </div>
          )
        }
      ]}
      flashcards={[
        { q: "Qual è il principio chiave studiato in questa lezione?", a: "La conservazione di massa, energia e carica." },
        { q: "In quali condizioni la formula ideale fallisce?", a: "Quando le forze intermolecolari diventano significative o il volume proprio non è trascurabile." },
        { q: "Qual è la differenza tra l'approccio classico e quantistico qui?", a: "L'approccio classico è continuo, quello quantistico prevede stati discreti di energia." }
      ]}
      exercises={[
        {
          title: "Calcolo Analitico Avanzato",
          text: <p>Un sistema passa da uno stato A a uno stato B assorbendo energia. Calcola la variazione considerando i parametri standard.</p>,
          steps: [
            "1. Scrivi i dati: Valore iniziale, Costanti fisiche.",
            "2. Converti tutte le unità nel Sistema Internazionale.",
            "3. Applica la formula principale.",
            "4. Calcola il risultato prestando attenzione alle cifre significative."
          ]
        }
      ]}
      quiz={[
        {
          q: "Se raddoppiamo la variabile indipendente principale, come risponde il sistema?",
          options: ["Rimane invariato", "Raddoppia in modo direttamente proporzionale", "Quadruplica (legge quadratica)", "Dimezza (legge inversamente proporzionale)"],
          correct: 1
        },
        {
          q: "Quale tra le seguenti è l'unità di misura nel Sistema Internazionale (SI)?",
          options: ["Litri (L)", "Gradi Celsius (°C)", "Kelvin (K)", "Atmosfere (atm)"],
          correct: 2
        },
        {
          q: "L'eccezione principale a questa legge chimica si verifica quando:",
          options: ["La temperatura è troppo alta", "Siamo in presenza di gas nobili", "Ci sono forti legami a idrogeno", "Il recipiente è aperto"],
          correct: 2
        }
      ]}
    />
  );
}
'''

for year, slug, title, subtitle, comp_name in curriculum_topics:
    os.makedirs(f"src/components/content/year{year}", exist_ok=True)
    with open(f"src/components/content/year{year}/{comp_name}.tsx", "w", encoding="utf-8") as f:
        f.write(generate_component_code(year, slug, title, subtitle, comp_name))

print("Generated all files correctly with raw strings.")
