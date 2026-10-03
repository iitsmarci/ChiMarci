const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, 'src', 'components', 'content');

const files = {
  'year1/MisureGrandezzeLesson.tsx': `import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function MisureGrandezzeLesson() {
  return (
    <LessonTemplate
      title="Le Misure e le Grandezze"
      subtitle="Fondamenti quantitativi della Chimica: Sistema Internazionale e Teoria degli Errori."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Ineluttabilità della Misura in Chimica</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La chimica ha abbandonato il suo retaggio alchemico-qualitativo nel XVIII secolo grazie all'introduzione rigorosa della bilancia e della misura sistematica (Lavoisier). In ambito accademico, una misurazione non è un semplice "numero", ma l'associazione indissolubile di tre elementi: un <strong>valore numerico</strong>, un'<strong>unità di misura</strong> rigorosamente codificata e un'<strong>incertezza</strong> (errore sperimentale intrinseco).
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Il Sistema Internazionale (SI)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300 mb-4">
            Al fine di uniformare la comunicazione scientifica globale, la <em>Conférence Générale des Poids et Mesures</em> (CGPM) ha stabilito il <strong>Sistema Internazionale delle Unità di Misura</strong>. Esso si fonda su sette grandezze fisiche fondamentali, dalle quali derivano tutte le altre.
          </p>
          <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 shadow-sm relative overflow-hidden mb-6">
            <div className="absolute top-0 left-0 w-2 h-full bg-blue-500"></div>
            <ul className="list-disc pl-5 text-sm text-zinc-700 dark:text-zinc-300 space-y-2">
              <li><strong>Lunghezza (<MathEq math="l" />):</strong> Metro (<MathEq math="\text{m}" />) - Definito in base alla velocità della luce nel vuoto.</li>
              <li><strong>Massa (<MathEq math="m" />):</strong> Chilogrammo (<MathEq math="\text{kg}" />) - Definito in base alla costante di Planck (<MathEq math="h" />).</li>
              <li><strong>Tempo (<MathEq math="t" />):</strong> Secondo (<MathEq math="\text{s}" />) - Definito in base alla frequenza di transizione atomica del Cesio-133.</li>
              <li><strong>Temperatura Termodinamica (<MathEq math="T" />):</strong> Kelvin (<MathEq math="\text{K}" />) - Legata alla costante di Boltzmann (<MathEq math="k_B" />).</li>
              <li><strong>Quantità di sostanza (<MathEq math="n" />):</strong> Mole (<MathEq math="\text{mol}" />) - Fissata al valore esatto della costante di Avogadro (<MathEq math="N_A = 6.022 \times 10^{23}" />).</li>
              <li><strong>Intensità di corrente (<MathEq math="I" />):</strong> Ampere (<MathEq math="\text{A}" />).</li>
              <li><strong>Intensità luminosa (<MathEq math="I_v" />):</strong> Candela (<MathEq math="\text{cd}" />).</li>
            </ul>
          </div>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Incertezza e Cifre Significative</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Nessuna misurazione sperimentale è infinitamente precisa. L'errore può essere <strong>sistematico</strong> (difetto strumentale, eliminabile) o <strong>casuale</strong> (fluttuazioni statistiche, ineliminabile). La deviazione standard (<MathEq math="\sigma" />) è la metrica statistica d'elezione per quantificare quest'ultimo.
          </p>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300 mt-4">
            Operativamente, in chimica si usano le <strong>cifre significative</strong>. Esse rappresentano tutte le cifre di una misura di cui si ha certezza, più la prima cifra incerta.
            Ad esempio, in una misurazione su bilancia analitica pari a <MathEq math="12.045 \text{ g}" />, abbiamo 5 cifre significative. L'ultima (il 5) porta con sé l'incertezza strumentale tipica (es. <MathEq math="\pm 0.001 \text{ g}" />).
          </p>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}`,
  'year1/TrasformazioniFisicheLesson.tsx': `import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function TrasformazioniFisicheLesson() {
  return (
    <LessonTemplate
      title="Le Trasformazioni Fisiche della Materia"
      subtitle="Stati di aggregazione, termodinamica dei passaggi di stato e calore latente."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">Stati di Aggregazione e Forze Intermolecolari</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La fenomenologia macroscopica della materia (solido, liquido, aeriforme) è l'espressione diretta di un delicato equilibrio termodinamico tra l'<strong>energia potenziale</strong> (forze coesive intermolecolari, <MathEq math="E_p" />) e l'<strong>energia cinetica</strong> termica (<MathEq math="E_k \propto T" />).
          </p>

          <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 mt-6 relative overflow-hidden">
             <div className="absolute top-0 left-0 w-2 h-full bg-cyan-500"></div>
             <p className="text-sm text-zinc-700 dark:text-zinc-300">
               Nello <strong>stato solido</strong> (<MathEq math="E_p \gg E_k" />), il moto traslazionale è proibito; i nodi reticolari vibrano attorno a posizioni di equilibrio. Nello <strong>stato liquido</strong> (<MathEq math="E_p \approx E_k" />), si preserva il volume proprio ma l'ordine a lungo raggio collassa, permettendo lo scorrimento (fluidità). Nello <strong>stato aeriforme</strong> (<MathEq math="E_k \gg E_p" />), le interazioni coesive divengono trascurabili, massimizzando l'entropia del sistema (<MathEq math="S" />) per occupare tutto il volume disponibile.
             </p>
          </div>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">La Termodinamica dei Passaggi di Stato</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Una transizione di fase di primo ordine comporta una discontinuità nell'entalpia (<MathEq math="\Delta H" />). Durante il passaggio (ad es. fusione o ebollizione), la temperatura rimane rigorosamente costante (<MathEq math="\Delta T = 0" />) fintanto che le due fasi coesistono in equilibrio. 
          </p>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300 mt-4">
            L'energia scambiata interamente in forma isotermica è definita <strong>Calore Latente</strong> (<MathEq math="\lambda" />). La legge fondamentale governa lo scambio termico è:
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-4 text-center rounded font-mono font-bold text-zinc-800 dark:text-zinc-200 my-4">
            <MathEq math="Q = m \cdot \lambda \quad \text{oppure} \quad Q = n \cdot \Delta H_{\text{transizione}}" />
          </div>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Questo calore non incrementa la temperatura perché è speso interamente come lavoro di rottura dei legami intermolecolari, incrementando l'energia potenziale del sistema, e conseguentemente il suo disordine entropico.
          </p>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}`,
  'year1/TeoriaAtomicaDaltonLesson.tsx': `import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function TeoriaAtomicaDaltonLesson() {
  return (
    <LessonTemplate
      title="Dalle Trasformazioni Chimiche alla Teoria Atomica"
      subtitle="Le leggi ponderali, Lavoisier, Proust, Dalton e la nascita della chimica moderna."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">La Fine dell'Alchimia: Le Leggi Ponderali</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Il passaggio epistemologico dalla filosofia naturale alla chimica quantitativa si è consumato a cavallo tra il XVIII e XIX secolo attraverso l'evidenza sperimentale incrollabile delle <strong>Leggi Ponderali</strong>.
          </p>
          
          <div className="space-y-6 mt-6">
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-indigo-900 dark:text-indigo-400 mb-2">1. Legge di Lavoisier (Conservazione della Massa, 1789)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                In un sistema chiuso, la massa totale dei reagenti è sempre uguale alla massa totale dei prodotti. (<MathEq math="\sum m_{\text{reagenti}} = \sum m_{\text{prodotti}}" />). Nulla si crea, nulla si distrugge.
              </p>
            </div>
            
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-emerald-900 dark:text-emerald-400 mb-2">2. Legge di Proust (Proporzioni Definite, 1799)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                In un composto chimico puro, gli elementi costituenti sono combinati in rapporti di massa definiti e costanti, indipendentemente dall'origine o dal metodo di sintesi del composto. L'acqua (<MathEq math="\text{H}_2\text{O}" />) ha sempre un rapporto di massa Idrogeno:Ossigeno di 1:8.
              </p>
            </div>

            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-rose-900 dark:text-rose-400 mb-2">3. Legge di Dalton (Proporzioni Multiple, 1804)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                Quando due elementi si combinano per formare più di un composto (es. <MathEq math="\text{CO}" /> e <MathEq math="\text{CO}_2" />), mantenendo costante la massa di uno, le masse dell'altro stanno tra loro in rapporti di numeri interi e piccoli (1:1, 1:2, 2:3).
              </p>
            </div>
          </div>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Il Paradigma Atomico di Dalton (1808)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Per spiegare elegantemente le leggi ponderali, John Dalton postulò l'esistenza di particelle indivisibili di materia: gli <strong>atomi</strong> (dal greco <em>atomos</em>, indivisibile). Il suo postulato fondativo asseriva che la materia non è un continuum, ma è quantizzata in particelle discrete, solide e immutabili. Tutte le reazioni chimiche, in quest'ottica, non sono alterazioni dell'essenza della materia, ma meri <strong>riarrangiamenti geometrici</strong> (rottura e formazione di legami) tra atomi preesistenti e inalterabili.
          </p>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}`,
  'year1/LeggiGasCineticaLesson.tsx': `import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function LeggiGasCineticaLesson() {
  return (
    <LessonTemplate
      title="Teoria Cinetico-Molecolare e Leggi dei Gas"
      subtitle="Dall'Equazione di Stato dei Gas Perfetti al comportamento dei gas reali."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">I Postulati della Teoria Cinetico-Molecolare</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Per formalizzare matematicamente lo stato aeriforme, la fisica ha ideato l'astrazione del <strong>Gas Perfetto (o Ideale)</strong>, fondato su postulati draconiani: 1) Volume proprio delle particelle trascurabile (puntiformi); 2) Urti contro le pareti perfettamente elastici (zero dispersione di <MathEq math="E_k" />); 3) Assenza totale di interazioni attrattive o repulsive tra le molecole.
          </p>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Sotto queste condizioni, la pressione (<MathEq math="P" />) generata dal gas è unicamente il riflesso macroscopico degli innumerevoli urti delle molecole contro la parete, mentre la Temperatura Assoluta (<MathEq math="T" />) è l'indice diretto della loro Energia Cinetica media: <MathEq math="E_k = \frac{3}{2} k_B T" />.
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">L'Equazione di Stato e le Leggi Empiriche</h3>
          
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 text-center rounded-xl font-mono text-2xl text-zinc-800 dark:text-zinc-200 my-6 shadow-inner border border-zinc-200 dark:border-zinc-800">
            <MathEq math="P \cdot V = n \cdot R \cdot T" />
          </div>
          
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            L'equazione sovrastante condensa secoli di osservazioni sperimentali. Da essa derivano come corollari le singole isotrasformazioni:
          </p>
          <ul className="list-disc pl-5 text-sm text-zinc-700 dark:text-zinc-300 space-y-3 mt-4">
            <li><strong>Legge di Boyle (Isoterma, <MathEq math="T" /> costante):</strong> <MathEq math="P \cdot V = \text{cost}" />. Pressione e volume sono inversamente proporzionali.</li>
            <li><strong>Legge di Charles (Isobara, <MathEq math="P" /> costante):</strong> <MathEq math="V / T = \text{cost}" />. Il volume si espande linearmente con la temperatura assoluta.</li>
            <li><strong>Legge di Gay-Lussac (Isocora, <MathEq math="V" /> costante):</strong> <MathEq math="P / T = \text{cost}" />. La pressione scala con l'agitazione termica.</li>
          </ul>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Gas Reali e l'Equazione di Van der Waals</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            A pressioni estreme (compressione spaziale) o a temperature prossime alla liquefazione, l'approssimazione ideale crolla. Il volume molecolare non è più trascurabile (<MathEq math="covolume, b" />) e le forze intermolecolari (pressione interna, <MathEq math="a" />) riducono gli urti contro le pareti. L'equazione di stato deve essere modificata nella formulazione di Van der Waals:
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-4 text-center rounded font-mono text-lg text-zinc-800 dark:text-zinc-200 mt-4">
            <MathEq math="\left( P + \frac{a \cdot n^2}{V^2} \right) \cdot (V - n \cdot b) = n \cdot R \cdot T" />
          </div>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}`,
  'year1/RappresentareReazioniLesson.tsx': `import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function RappresentareReazioniLesson() {
  return (
    <LessonTemplate
      title="Rappresentare le Reazioni Chimiche"
      subtitle="Simbologia di reazione, coefficienti stechiometrici e logica del bilanciamento."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">La Sintassi e la Semantica dell'Equazione Chimica</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Un'equazione chimica non è una semplice stringa testuale, ma un rigoroso bilancio algebrico di massa, energia e carica. Essa descrive il collasso di uno stato termodinamico iniziale (<strong>Reagenti</strong>, a sinistra) in uno stato finale energeticamente più favorevole o spinto da forze motrici esterne (<strong>Prodotti</strong>, a destra), separati dall'operatore di resa (<MathEq math="\rightarrow" />).
          </p>
          
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-4 text-center rounded-xl font-mono text-xl text-zinc-800 dark:text-zinc-200 my-6 shadow-inner border border-zinc-200 dark:border-zinc-800">
            <MathEq math="2\text{H}_2(g) + \text{O}_2(g) \xrightarrow{\Delta} 2\text{H}_2\text{O}(l) + \Delta H" />
          </div>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">L'Imperativo del Bilanciamento (Legge di Lavoisier)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Poiché la materia non può essere annichilita né creata ex nihilo nel dominio delle energie chimiche, ogni singola specie atomica presente tra i reagenti <strong>deve</strong> esistere nell'esatta medesima quantità nei prodotti. Questo obbliga l'introduzione dei <strong>Coefficienti Stechiometrici</strong>: moltiplicatori algebrici interi (o semi-interi) anteposti alle formule chimiche.
          </p>
          
          <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 mt-6 relative overflow-hidden">
             <div className="absolute top-0 left-0 w-2 h-full bg-rose-500"></div>
             <h4 className="text-xl font-bold text-rose-900 dark:text-rose-400 mb-2">Attenzione ai Pedici</h4>
             <p className="text-sm text-zinc-700 dark:text-zinc-300">
               È categoricamente proibito alterare i <strong>pedici</strong> di una formula chimica (es. cambiare <MathEq math="\text{H}_2\text{O}" /> in <MathEq math="\text{H}_2\text{O}_2" /> per forzare un bilanciamento) poiché ciò muta ontologicamente l'identità della molecola (da innocua acqua a perossido di idrogeno altamente reattivo). L'unica variabile su cui operare è il coefficiente stechiometrico spaziale.
             </p>
          </div>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}`
};

Object.entries(files).forEach(([filepath, content]) => {
  const fullPath = path.join(baseDir, filepath);
  fs.mkdirSync(path.dirname(fullPath), { recursive: true });
  fs.writeFileSync(fullPath, content);
  console.log('Created: ' + fullPath);
});
