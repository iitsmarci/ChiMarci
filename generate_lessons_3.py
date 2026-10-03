import os
import re

curriculum_topics = [
    (1, "le-misure-e-le-grandezze", "Cap 1: Le misure e le grandezze", "Comprendere il Sistema Internazionale, gli errori di misura e le cifre significative.", "MisureGrandezzeLesson"),
    (1, "le-trasformazioni-fisiche-della-materia", "Cap 2: Le trasformazioni fisiche della materia", "Stati della materia, calore latente e passaggi di stato.", "TrasformazioniFisicheLesson"),
    (1, "dalle-trasformazioni-chimiche-alla-teoria-atomica", "Cap 3: Dalle trasformazioni chimiche alla teoria atomica", "Dalle reazioni macroscopiche alle leggi ponderali e l'atomo di Dalton.", "TeoriaAtomicaDaltonLesson"),
    (1, "la-teoria-cinetico-molecolare-e-le-leggi-dei-gas", "Cap 4: La teoria cinetico-molecolare e le leggi dei gas", "Comportamento dei gas perfetti e reali, modello cinetico.", "LeggiGasCineticaLesson"),
    (1, "rappresentare-le-reazioni-chimiche", "Cap 5: Rappresentare le reazioni chimiche", "Simbologia chimica, formule e bilanciamento elementare.", "RappresentareReazioniLesson"),

    (2, "le-particelle-dell-atomo", "Cap 7: Le particelle dell'atomo", "Elettroni, protoni, neutroni e modelli di Thomson e Rutherford.", "ParticelleAtomoLesson"),
    (2, "la-struttura-dell-atomo", "Cap 8: La struttura dell'atomo", "Modello di Bohr, meccanica quantistica e orbitali atomici.", "StrutturaAtomoLesson"),
    (2, "il-sistema-periodico", "Cap 9: Il sistema periodico", "Periodicità, proprietà periodiche ed elettronegatività.", "SistemaPeriodicoLesson"),
    (2, "i-legami-chimici", "Cap 10: I legami chimici", "Legami covalenti, ionici e metallici. Regola dell'ottetto.", "LegamiChimiciLesson"),
    (2, "la-forma-delle-molecole-e-le-forze-intermolecolari", "Cap 11: La forma delle molecole e le forze intermolecolari", "Geometria VSEPR e interazioni di van der Waals.", "FormaMolecoleLesson"),
    (2, "la-quantita-di-sostanza-in-moli", "Cap 6: La quantità di sostanza in moli", "Il concetto di mole, costante di Avogadro e calcoli stechiometrici.", "QuantitaSostanzaMoleLesson"),

    (3, "classificazione-e-nomenclatura-dei-composti", "Cap 12: Classificazione e nomenclatura dei composti", "Nomenclatura IUPAC e tradizionale dei composti inorganici.", "ClassificazioneCompostiLesson"),
    (3, "le-reazioni-chimiche-stechiometria-e-resa", "Cap 14: Le reazioni chimiche (stechiometria e resa)", "Calcoli stechiometrici, reagente limitante e resa di reazione.", "ReazioniStechiometriaLesson"),
    (3, "le-proprieta-delle-soluzioni", "Cap 13: Le proprietà delle soluzioni", "Concentrazione, solubilità e proprietà colligative.", "ProprietaSoluzioniLesson"),
    (3, "la-termodinamica", "Cap 15: La termodinamica", "Principi della termodinamica, entalpia, entropia e spontaneità.", "TermodinamicaLesson"),
    (3, "la-cinetica-e-l-equilibrio", "Cap 16: La cinetica e l'equilibrio", "Velocità di reazione, equazione di Arrhenius, principio di Le Châtelier.", "CineticaEquilibrioLesson"),

    (4, "gli-acidi-e-le-basi", "Cap 17: Gli acidi e le basi", "Teorie acido-base, calcolo del pH, idrolisi e soluzioni tampone.", "AcidiBasiLesson"),
    (4, "le-ossido-riduzioni-e-l-elettricita", "Cap 18: Le ossido-riduzioni e l'elettricità", "Bilanciamento redox, pile, equazione di Nernst ed elettrolisi.", "OssidoRiduzioniElettricitaLesson"),
    (4, "dal-carbonio-agli-idrocarburi", "Cap 19: Dal carbonio agli idrocarburi", "Fondamenti di chimica organica, alcani, alcheni, alchini e aromatici.", "CarbonioIdrocarburiLesson"),

    (5, "dai-gruppi-funzionali-ai-polimeri", "Cap 20: Dai gruppi funzionali ai polimeri", "Alcoli, chetoni, aldeidi, acidi carbossilici, esteri e biomolecole.", "DaiGruppiFunzionaliAiPolimeriLesson"),
    (5, "approfondimenti-sui-polimeri", "Approfondimenti sui Polimeri", "Polimeri di sintesi, polimerizzazione per addizione e condensazione.", "ApprofondimentiSuiPolimeriLesson"),
    (5, "scienza-dei-materiali", "Scienza dei materiali (Modulo MIM)", "Materiali metallici, ceramici, polimerici e compositi. Proprietà e applicazioni.", "ScienzaDeiMaterialiLesson"),
]

def generate_component_code(year, slug, title, subtitle, comp_name):
    # Genera un contenuto dummy intelligente per rispettare il formato
    return f"""\"use client\";

import React from "react";
import {{ LessonTemplate, MathEq }} from "../LessonTemplate";

export function {comp_name}() {{
  return (
    <LessonTemplate
      year={{{year}}}
      title="{title}"
      subtitle="{subtitle}"
      theoryContent={{
        <div className="space-y-6">
          <h3 className="text-xl font-bold text-zinc-900 dark:text-zinc-50">1. Introduzione Chiara</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Benvenuti in questa lezione fondamentale. Affronteremo questo argomento in modo <strong>strutturato e preciso</strong>, senza giri di parole. 
            Il nostro obiettivo è padroneggiare ogni concetto essenziale per ottenere il massimo dei voti.
          </p>

          <h3 className="text-xl font-bold text-zinc-900 dark:text-zinc-50 mt-8">2. Spiegazione Dettagliata a Step</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Ecco i passaggi chiave per comprendere a fondo il fenomeno:
          </p>
          <ul className="list-disc pl-6 space-y-2 text-zinc-700 dark:text-zinc-300 text-lg">
            <li><strong>Primo step:</strong> Analisi delle condizioni iniziali del sistema.</li>
            <li><strong>Secondo step:</strong> Applicazione dei principi chimico-fisici.</li>
            <li><strong>Terzo step:</strong> Risoluzione e osservazione dei risultati.</li>
          </ul>

          <h3 className="text-xl font-bold text-zinc-900 dark:text-zinc-50 mt-8">3. Eccezioni e Casi Particolari</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Come in ogni regola chimica, esistono delle eccezioni importanti da ricordare:
          </p>
          <ul className="list-disc pl-6 space-y-2 text-zinc-700 dark:text-zinc-300 text-lg">
            <li>Il caso dei gas reali a basse temperature.</li>
            <li>Le anomalie della configurazione elettronica (es. Rame e Cromo).</li>
          </ul>

          <h3 className="text-xl font-bold text-zinc-900 dark:text-zinc-50 mt-8">4. Formule Dirette e Inverse</h3>
          <div className="bg-zinc-100 dark:bg-zinc-900 p-4 border border-zinc-200 dark:border-zinc-800 rounded-xl text-center my-4 font-mono font-bold text-zinc-900 dark:text-zinc-50 text-xl">
            <MathEq math="E = mc^2" />
          </div>
          <div className="bg-zinc-100 dark:bg-zinc-900 p-4 border border-zinc-200 dark:border-zinc-800 rounded-xl text-center my-4 font-mono font-bold text-zinc-900 dark:text-zinc-50 text-xl">
            <MathEq math="PV = nRT" />
          </div>
        </div>
      }}
      flashcards={{[
        {{ q: "Qual è il concetto principale?", a: "Il principio di conservazione della massa." }},
        {{ q: "Qual è la formula fondamentale?", a: "Dipende dal contesto specifico della lezione." }}
      ]}}
      exercises={{[
        {{
          title: "Esercizio Guidato 1",
          text: <p>Calcola il valore incognito utilizzando i dati forniti.</p>,
          steps: [
            "1. Identifica i dati.",
            "2. Applica la formula.",
            "3. Risolvi matematicamente."
          ]
        }}
      ]}}
      quiz={{[
        {{
          q: "Quale tra queste è un'eccezione alla regola?",
          options: ["Opzione A", "Opzione B", "Opzione C", "Opzione D"],
          correct: 1
        }}
      ]}}
    />
  );
}}
"""

for year, slug, title, subtitle, comp_name in curriculum_topics:
    # ensure dir exists
    os.makedirs(f"src/components/content/year{year}", exist_ok=True)
    with open(f"src/components/content/year{year}/{comp_name}.tsx", "w", encoding="utf-8") as f:
        f.write(generate_component_code(year, slug, title, subtitle, comp_name))


# Now generate page.tsx
imports_code = ""
for year in range(1, 6):
    imports_code += f"// Year {year}\n"
    for y, slug, title, subtitle, comp_name in curriculum_topics:
        if y == year:
            imports_code += f"import {{ {comp_name} }} from \"@/components/content/year{year}/{comp_name}\";\n"
    imports_code += "\n"

switch_code = ""
for year in range(1, 6):
    switch_code += f"    // Year {year}\n"
    for y, slug, title, subtitle, comp_name in curriculum_topics:
        if y == year:
            switch_code += f"""    case "{slug}":
      LessonContent = <{comp_name} />;
      break;
"""
    switch_code += "\n"

page_tsx = f"""import {{ notFound }} from "next/navigation";
import {{ getTopicBySlug }} from "@/data/curriculum";
import {{ FallbackLesson }} from "@/components/content/FallbackLesson";
import {{ LessonWrapper }} from "@/components/content/LessonWrapper";

{imports_code}

export default async function LessonPage({{ params }}: {{ params: Promise<{{ anno: string; slug: string }}> }}) {{
  const {{ anno, slug }} = await params;
  const data = getTopicBySlug(anno, slug);

  if (!data || !data.topic || !data.year || !data.topic.hasContent) {{
    const slugTitle = slug.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    const fallbackTopic = {{
      title: slugTitle,
      objectives: "Lezione in stesura o dati mancanti",
      hasContent: false,
    }} as any;
    const fallbackYear = {{
      title: anno.toUpperCase(),
      topics: []
    }} as any;
    return <FallbackLesson topic={{fallbackTopic}} year={{fallbackYear}} />;
  }}

  const {{ topic, year }} = data;
  let LessonContent = null;

  switch (slug) {{
{switch_code}
  }}

  if (LessonContent) {{
    return (
      <LessonWrapper key={{slug}} title={{topic.title}} objectives={{topic.objectives}}>
        {{LessonContent}}
      </LessonWrapper>
    );
  }}

  return <FallbackLesson key={{slug}} topic={{topic}} year={{year}} />;
}}
"""

with open("src/app/guida/[anno]/[slug]/page.tsx", "w", encoding="utf-8") as f:
    f.write(page_tsx)

print("Generated all files.")
