"use client";

import React from "react";
import { LessonTemplate, MathEq } from "../LessonTemplate";

export function CineticaEquilibrioLesson() {
  return (
    <LessonTemplate
      year={3}
      title="Cap 16: La cinetica e l'equilibrio"
      subtitle="Costante di equilibrio (Keq), equazione di Arrhenius, principio di Le Châtelier."
      theoryPages={[
        {
          title: "1. High-Yield: Definizioni e Formule",
          content: (
            <>
              
              <h3>Definizione Rigorosa</h3>
              <p>Il concetto di <strong>La cinetica e l'equilibrio</strong> descrive le relazioni quantitative e le leggi fondamentali del sistema chimico in esame. Il focus applicativo risiede nel calcolo delle variabili di stato (pressione, volume, moli, concentrazione) e nell'identificazione dell'equilibrio e dei bilanci di carica o massa.</p>
              
              <h3>Formulario Centrale (High-Yield)</h3>
              
              <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 my-6 shadow-sm overflow-x-auto text-center">
                <span className="font-semibold text-zinc-500 uppercase tracking-widest text-xs block mb-4">Relazioni Mole-Massa-Volume (Triangolo)</span>
                <MathEq math="n = \frac{m}{MM} \quad \Rightarrow \quad m = n \cdot MM \quad \Rightarrow \quad MM = \frac{m}{n}" block />
              </div>

              <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 my-6 shadow-sm overflow-x-auto text-center">
                <span className="font-semibold text-zinc-500 uppercase tracking-widest text-xs block mb-4">Molarità e Concentrazione (Cap. 13 e 17)</span>
                <MathEq math="M = \frac{n}{V_{(L)}} \quad \Rightarrow \quad n = M \cdot V_{(L)} \quad \Rightarrow \quad V_{(L)} = \frac{n}{M}" block />
              </div>

              <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 my-6 shadow-sm overflow-x-auto text-center">
                <span className="font-semibold text-zinc-500 uppercase tracking-widest text-xs block mb-4">Acidi, Basi e pH (Cap. 17)</span>
                <MathEq math="pH = -\log_{10}[H^+] \quad \Rightarrow \quad [H^+] = 10^{-pH}" block />
                <MathEq math="pOH = -\log_{10}[OH^-] \quad \Rightarrow \quad [OH^-] = 10^{-pOH}" block />
                <MathEq math="pH + pOH = 14 \quad (\text{a } 25^\circ\text{C})" block />
              </div>
              
              <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 my-6 shadow-sm overflow-x-auto text-center">
                <span className="font-semibold text-zinc-500 uppercase tracking-widest text-xs block mb-4">Equilibrio e Termodinamica (Cap. 13)</span>
                <MathEq math="K_{eq} = \frac{\prod [Prodotti]^p}{\prod [Reagenti]^r}" block />
                <MathEq math="\Delta G = \Delta H - T \cdot \Delta S" block />
              </div>

            </>
          )
        },
        {
          title: "2. Metodo di Risoluzione (Step-by-Step)",
          content: (
            <>
              
              <h3>Procedimento Logico (Step-by-Step)</h3>
              <p>Per la risoluzione degli esercizi pratici e numerici, applicare in modo chirurgico il seguente protocollo in 5 step:</p>
              
              <ol>
                <li><strong>Isolamento delle Variabili:</strong> Scrivere a margine i dati noti (massa in g, volume in L, pressione in atm, temperatura in K). Tutte le grandezze non conformi al SI devono essere convertite immediatamente.</li>
                <li><strong>Conversione in Moli (n):</strong> In chimica, si ragiona SEMPRE in moli. Usa la massa molare ($MM$) o la molarità per trovare le moli iniziali.</li>
                <li><strong>Impostazione della Reazione (Se presente):</strong> Bilanciare la reazione chimica assicurandosi che i coefficienti stechiometrici garantiscano la conservazione di massa e carica. Identificare il Reagente Limitante dividendo le moli disponibili per i rispettivi coefficienti.</li>
                <li><strong>Applicazione del Formulario:</strong> Impostare proporzioni del tipo <MathEq math="n_{\text{noto}} : c_{\text{noto}} = n_{\text{ignoto}} : c_{\text{ignoto}}" /> oppure inserire le variabili dirette nelle equazioni di stato/termodinamiche.</li>
                <li><strong>Validazione Finale:</strong> Controllare l'ordine di grandezza. Una concentrazione di $10^5$ M è fisicamente impossibile. Un pH &gt; 14 indica un errore di segno.</li>
              </ol>

            </>
          )
        },
        {
          title: "3. Tranelli e Casi Particolari",
          content: (
            <>
              
              <h3>Tranelli da Interrogazione</h3>
              <div className="border-l-4 border-indigo-500 pl-4 py-3 my-4 bg-indigo-50/50 dark:bg-indigo-900/20 text-indigo-900 dark:text-indigo-200 rounded-r-lg">
                <strong className="text-indigo-700 dark:text-indigo-300 font-clash tracking-wide uppercase text-sm mb-2 block">Attenzione agli errori fatali:</strong>
                <ul className="list-disc pl-5 space-y-1 marker:text-indigo-500 text-base">
                  <li><strong>Litri vs Millilitri:</strong> Nella Molarità (M = n/V), il volume VA SEMPRE convertito in Litri (es. 250 mL = 0.25 L). Se usi i mL, otterrai millimoli.</li>
                  <li><strong>Celsius vs Kelvin:</strong> Nella legge dei gas perfetti o in termodinamica (ΔG = ΔH - TΔS), la temperatura VA SEMPRE sommata a 273.15. Un calcolo in gradi Celsius ti garantirà un errore.</li>
                  <li><strong>Acidi Poliprotici:</strong> Nel calcolo del pH per acidi forti come H2SO4, la concentrazione di ioni [H+] è il doppio della concentrazione dell'acido! (es. 0.1 M H2SO4 -&gt; [H+] = 0.2 M).</li>
                  <li><strong>Basi Forti e pH:</strong> Il calcolo di -log(10) per NaOH restituisce il <strong>pOH</strong>, non il pH. Devi sempre sottrarre il valore ottenuto da 14 per trovare il pH reale.</li>
                  <li><strong>Reagente Limitante:</strong> Non è chi ha meno massa in grammi, e non è chi ha meno moli assolute, ma è il reagente con il <strong>rapporto minore</strong> tra le sue moli reali e il suo coefficiente stechiometrico.</li>
                </ul>
              </div>

            </>
          )
        }
      ]}
      flashcards={[
        { q: "Qual è la formula del pH e come si ricava la concentrazione protonica inversa?", a: "pH = -log[H+]. Inversamente: [H+] = 10^(-pH)" },
        { q: "Qual è il trucco per convertire correttamente mL in L nel calcolo della Molarità?", a: "Dividere sempre i mL per 1000. 50 mL equivalgono a 0.05 L." },
        { q: "Come identifichi il reagente limitante in una stechiometria?", a: "Dividi le moli di ciascun reagente per il proprio coefficiente stechiometrico. Il valore minore identifica il reagente limitante." }
      ]}
      exercises={[
        {
          title: "Esercizio Pratico: Molarità e pH",
          text: <p>Calcola il pH di una soluzione acquosa preparata sciogliendo 4 g di $NaOH$ solido in acqua distillata fino ad arrivare a un volume totale di 500 mL. La Massa Molare di NaOH è 40 g/mol.</p>,
          steps: [
            "1. Dati: massa = 4 g; Volume = 500 mL = 0.5 L; MM = 40 g/mol.",
            "2. Calcolo Moli (n): n = m / MM = 4 / 40 = 0.1 mol.",
            "3. Calcolo Molarità (M): M = n / V(L) = 0.1 / 0.5 = 0.2 mol/L.",
            "4. NaOH è una base forte: [OH-] = 0.2 M.",
            "5. Calcolo pOH: pOH = -log(0.2) = 0.70.",
            "6. Calcolo pH: pH = 14 - pOH = 14 - 0.70 = 13.30."
          ]
        },
        {
          title: "Esercizio Pratico: Reagente Limitante",
          text: <p>Data la reazione N2 + 3H2 -&gt; 2NH3, se si fanno reagire 10 moli di N2 con 15 moli di H2, quale sarà la quantità massima teorica di NH3 producibile?</p>,
          steps: [
            "1. Rapporti molari / Coefficienti: N2/1 = 10/1 = 10. H2/3 = 15/3 = 5.",
            "2. Identificazione Limitante: H2 è il limitante (valore 5 < 10).",
            "3. Calcolo Prodotto: La produzione dipende da H2. Rapporto H2:NH3 = 3:2.",
            "4. Proporzione: 3 : 2 = 15 : x.",
            "5. Risoluzione: x = (15 * 2) / 3 = 10 moli di NH3."
          ]
        }
      ]}
      quiz={[
        {
          q: "Se hai una soluzione 0.01 M di H2SO4 (acido forte biprotico), qual è il suo pH?",
          options: [
            "pH = 2 (da -log(0.01))",
            "pH = 1.7 (da -log(0.02) per i due protoni)",
            "pH = 12 (basico)",
            "pH = 4 (da 0.01 al quadrato)"
          ],
          correct: 1
        },
        {
          q: "Devi usare l'equazione di stato dei gas perfetti PV = nRT. Il volume è espresso in mL. Cosa fai?",
          options: [
            "Lascio i mL perché R si adatta in automatico",
            "Divido per 1000 convertendo obbligatoriamente in Litri (L)",
            "Moltiplico per 1000 convertendo in Microlitri",
            "Uso i mL ma cambio la temperatura in Celsius"
          ],
          correct: 1
        },
        {
          q: "Quale tra le seguenti è l'equazione corretta della relazione universale acido/base a 25°C?",
          options: [
            "pH = pOH * 14",
            "pH - pOH = 7",
            "pH + pOH = 14",
            "pOH = -log(pH)"
          ],
          correct: 2
        },
        {
          q: "Il calcolo delle moli (n) tramite il 'triangolo delle formule' per sostanze solide si esegue:",
          options: [
            "Dividendo la Molarità per il Volume",
            "Moltiplicando la Massa per la Massa Molare (n = m * MM)",
            "Dividendo la Massa per la Massa Molare (n = m / MM)",
            "Sommando i grammi ai Litri"
          ],
          correct: 2
        }
      ]}
    />
  );
}
