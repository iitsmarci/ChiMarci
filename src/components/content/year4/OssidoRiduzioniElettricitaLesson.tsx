"use client";

import React from "react";
import { LessonTemplate, MathEq } from "../LessonTemplate";

export function OssidoRiduzioniElettricitaLesson() {
  return (
    <LessonTemplate
      year={4}
      title="Cap 18: Le ossido-riduzioni e l'elettricità"
      subtitle="Bilanciamento redox, pile, equazione di Nernst ed elettrolisi."
      theoryContent={
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
      }
      flashcards={[
        { q: "Qual è il concetto principale?", a: "Il principio di conservazione della massa." },
        { q: "Qual è la formula fondamentale?", a: "Dipende dal contesto specifico della lezione." }
      ]}
      exercises={[
        {
          title: "Esercizio Guidato 1",
          text: <p>Calcola il valore incognito utilizzando i dati forniti.</p>,
          steps: [
            "1. Identifica i dati.",
            "2. Applica la formula.",
            "3. Risolvi matematicamente."
          ]
        }
      ]}
      quiz={[
        {
          q: "Quale tra queste è un'eccezione alla regola?",
          options: ["Opzione A", "Opzione B", "Opzione C", "Opzione D"],
          correct: 1
        }
      ]}
    />
  );
}
