"use client";

import React from "react";
import { LessonTemplate, MathEq } from "./LessonTemplate";

export function MolaritaPhLesson() {
  return (
    <LessonTemplate
      year={4}
      title="Molarità e Calcolo del pH"
      subtitle="La concentrazione delle soluzioni e il mondo degli acidi e delle basi."
      theoryContent={
        <div className="space-y-6">
          <h3 className="text-xl font-semibold text-zinc-900 dark:text-zinc-50">La Molarità (M)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            In chimica, quando sciogliamo qualcosa (soluto) nell'acqua (solvente), ci serve sapere esattamente <em>quanto</em> ne abbiamo sciolto. La <strong>Molarità</strong> è la misura regina della concentrazione.
          </p>

          <div className="bg-zinc-100 dark:bg-zinc-900 p-4 border border-zinc-200 dark:border-zinc-800 rounded text-center my-4 font-mono font-bold text-zinc-900 dark:text-zinc-50 text-xl">
            <MathEq math="\text{Molarità (M)} = \frac{\text{Moli di soluto (n)}}{\text{Volume di soluzione in Litri (V)}}" />
          </div>
          
          <div className="bg-zinc-50 dark:bg-zinc-900 p-4 border-l-4 border-zinc-900 dark:border-zinc-50 rounded-r-xl">
            <p className="text-sm font-medium text-zinc-900 dark:text-zinc-50">💡 Micro-esempio</p>
            <p className="text-sm text-zinc-700 dark:text-zinc-300 mt-1">
              Se sciogli 2 moli di sale in 1 Litro d'acqua, hai una soluzione 2 M (si legge "2 Molare"). Se le stesse 2 moli le sciogli in 2 Litri d'acqua, la Molarità dimezza: 1 M.
            </p>
          </div>

          <h3 className="text-xl font-semibold text-zinc-900 dark:text-zinc-50 mt-8">Acidi, Basi e la formula del pH</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Secondo la teoria di Brønsted-Lowry, un <strong>Acido</strong> è una sostanza che dona ioni idrogeno (<MathEq math="H^+" />), mentre una <strong>Base</strong> li accetta. 
            Più ioni <MathEq math="H^+" /> ci sono in giro, più la soluzione è acida. Per misurare questa acidità usiamo la scala logaritmica del pH.
          </p>

          <div className="bg-zinc-100 dark:bg-zinc-900 p-4 border border-zinc-200 dark:border-zinc-800 rounded text-center my-4 font-mono font-bold text-zinc-900 dark:text-zinc-50 text-xl">
            <MathEq math="\text{pH} = -\log_{10}[H^+]" />
          </div>

          <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 shadow-sm mt-4">
            <h4 className="text-lg font-bold text-zinc-900 dark:text-zinc-50 mb-4">La Scala del pH (da 0 a 14)</h4>
            <ul className="space-y-4 text-zinc-700 dark:text-zinc-300 text-sm">
              <li className="flex items-center gap-3">
                <span className="w-4 h-4 rounded-full bg-red-500 flex-shrink-0"></span>
                <span><strong>Da 0 a 6.9: ACIDO.</strong> (<MathEq math="[H^+]" /> &gt; <MathEq math="[OH^-]" />). Esempi: Succo di limone, Coca Cola, Acido muriatico.</span>
              </li>
              <li className="flex items-center gap-3">
                <span className="w-4 h-4 rounded-full bg-emerald-500 flex-shrink-0"></span>
                <span><strong>7.0: NEUTRO.</strong> (<MathEq math="[H^+]" /> = <MathEq math="[OH^-]" />). Esempio: Acqua pura.</span>
              </li>
              <li className="flex items-center gap-3">
                <span className="w-4 h-4 rounded-full bg-blue-500 flex-shrink-0"></span>
                <span><strong>Da 7.1 a 14: BASICO (Alcalino).</strong> (<MathEq math="[OH^-]" /> &gt; <MathEq math="[H^+]" />). Esempi: Sapone, Bicarbonato, Candeggina.</span>
              </li>
            </ul>
          </div>
          
          <div className="mt-4 bg-zinc-50 dark:bg-zinc-900 p-4 rounded border border-zinc-200 dark:border-zinc-800">
            <p className="text-sm font-medium text-zinc-900 dark:text-zinc-50 mb-1">⚠️ Attenzione ai Logaritmi!</p>
            <p className="text-sm text-zinc-700 dark:text-zinc-300">
              Essendo una scala logaritmica negativa, <strong>un pH PIÙ BASSO significa MOLTA PIÙ acidità</strong>. 
              Inoltre, passare da pH 4 a pH 3 non raddoppia l'acidità, ma la decuplica (diventa 10 volte più acido)!
            </p>
          </div>
        </div>
      }
      flashcards={[
        { q: "Qual è la formula della Molarità?", a: "M = n / V (Moli di soluto diviso Volume in Litri della soluzione)." },
        { q: "Se la concentrazione di ioni [H+] aumenta, il pH sale o scende?", a: "Il pH SCENDE. Più H+ ci sono, più è acido, quindi il pH si avvicina allo 0." },
        { q: "Una soluzione con pH = 2 è quante volte più acida di una con pH = 3?", a: "10 volte più acida, poiché la scala del pH è logaritmica in base 10." }
      ]}
      exercises={[
        {
          title: "Calcolo della Molarità",
          text: <p>Sciogli 0.5 moli di sale in 250 mL di acqua. Qual è la Molarità (M) della soluzione?</p>,
          steps: [
            "1. Per prima cosa, converti sempre i mL in Litri! 250 mL = 0.250 L.",
            "2. Usa la formula M = n / V.",
            "3. M = 0.5 / 0.250",
            "4. M = 2. La soluzione è 2 Molare (2 M)."
          ]
        },
        {
          title: "Calcolo Diretto del pH",
          text: <p>Hai un acido forte (tutto dissociato) con una concentrazione di ioni [H+] pari a <MathEq math="10^{-4}" /> M. Calcola il pH.</p>,
          steps: [
            "1. La formula è pH = -log([H+]).",
            "2. pH = -log(10⁻⁴).",
            "3. La base del logaritmo e la base dell'esponenziale (10) si elidono, rimane -(-4).",
            "4. pH = 4. (Soluzione acida)."
          ]
        }
      ]}
      quiz={[
        {
          q: "La Molarità si esprime in:",
          options: ["Litri / moli", "grammi / moli", "moli / Litro (mol/L)", "moli / grammi"],
          correct: 2
        },
        {
          q: "Una soluzione di candeggina ha pH = 12. È considerata:",
          options: ["Fortemente acida", "Neutra", "Debolmente acida", "Fortemente basica (alcalina)"],
          correct: 3
        },
        {
          q: "Secondo Brønsted-Lowry, una base è una sostanza in grado di:",
          options: ["Donare protoni (H+)", "Accettare protoni (H+)", "Diventare un solido", "Aumentare il numero di ossidazione"],
          correct: 1
        }
      ]}
    />
  );
}
