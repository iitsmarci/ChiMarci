import os

base_dir = os.path.join(os.path.dirname(__file__), 'src', 'components', 'content')

files = {
  'year1/MisureGrandezzeLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
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
}""",
  'year1/TrasformazioniFisicheLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
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
}""",
  'year1/TeoriaAtomicaDaltonLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
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
}""",
  'year1/LeggiGasCineticaLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
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
}""",
  'year1/RappresentareReazioniLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
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
}""",
  'year2/ParticelleAtomoLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function ParticelleAtomoLesson() {
  return (
    <LessonTemplate
      title="Le Particelle dell'Atomo"
      subtitle="Elettroni, Protoni, Neutroni e la caduta del modello di Thomson."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Architettura Subatomica</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            L'assunto dell'indivisibilità atomica (Dalton) venne infranto alla fine del XIX secolo dalle indagini sui raggi catodici. L'atomo si rivelò essere un aggregato strutturato di fermioni e bosoni fondamentali, sebbene per la chimica la triade fondamentale rimanga confinata a: Elettrone (<MathEq math="e^-" />), Protone (<MathEq math="p^+" />) e Neutrone (<MathEq math="n^0" />).
          </p>
          <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 relative overflow-hidden mt-6">
            <div className="absolute top-0 left-0 w-2 h-full bg-cyan-500"></div>
            <ul className="list-disc pl-5 text-sm text-zinc-700 dark:text-zinc-300 space-y-3">
              <li><strong>Elettrone (1897, Thomson):</strong> Particella elementare leptone. Possiede carica elettrica <MathEq math="-1.602 \times 10^{-19} \text{ C}" /> (definita come -1) e una massa a riposo quasi trascurabile (<MathEq math="9.109 \times 10^{-31} \text{ kg}" />). Custode di tutte le interazioni chimiche.</li>
              <li><strong>Protone (1919, Rutherford):</strong> Adrone composto. Carica identica in modulo ma opposta all'elettrone (+1). La sua massa è circa 1836 volte superiore a quella dell'elettrone (<MathEq math="1.672 \times 10^{-27} \text{ kg}" />).</li>
              <li><strong>Neutrone (1932, Chadwick):</strong> Adrone privo di carica elettrica, con massa marginalmente superiore a quella del protone. Cruciale per la coesione del nucleo tramite interazione nucleare forte (mitigando la repulsione coulombiana tra i protoni).</li>
            </ul>
          </div>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">L'Esperimento della Lamina d'Oro (Rutherford, 1911)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Fino al 1911 imperava il modello a "Panettone" di Thomson (carica positiva diffusa e elettroni incastonati). L'esperimento di Geiger e Marsden (sotto la direzione di Rutherford) bombardando un sottilissimo foglio d'oro con particelle <MathEq math="\alpha" /> (<MathEq math="\text{He}^{2+}" />) destabilizzò l'intera fisica classica.
          </p>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300 mt-4">
            Mentre la maggior parte delle particelle attraversava la lamina indisturbata, una frazione minuscola subiva drammatiche deviazioni, talvolta rimbalzando all'indietro. La deduzione termodinamica ed elettrostatica fu drastica: l'atomo è per il 99.99% spazio vuoto. La totalità della massa e della carica positiva è condensata in una singolarità centrale dal raggio di appena <MathEq math="10^{-15} \text{ m}" />: il <strong>Nucleo Atomico</strong>.
          </p>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year2/StrutturaAtomoLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function StrutturaAtomoLesson() {
  return (
    <LessonTemplate
      title="La Struttura dell'Atomo"
      subtitle="La Meccanica Quantistica, l'atomo di Bohr e la probabilità orbitale."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">La Crisi del Modello Planetario e i Quanti</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Il modello di Rutherford, per quanto elegante, conteneva un paradosso letale per l'elettrodinamica classica (equazioni di Maxwell): una carica accelerata in moto circolare (l'elettrone) deve irradiare energia, collassando in una spirale di morte verso il nucleo in frazioni di millisecondo.
          </p>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300 mt-4">
            La salvezza giunse nel 1913 con <strong>Niels Bohr</strong>, che impose una quantizzazione <em>ad hoc</em> del momento angolare elettronico: l'elettrone non irradia energia se orbita in specifici livelli energetici "stazionari", e lo scambio energetico (emissione/assorbimento di un fotone) avviene solo durante il salto quantico da un'orbita all'altra: <MathEq math="\Delta E = h \cdot \nu" />.
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">L'Orbitale e la Meccanica Ondulatoria</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Negli anni '20, con l'ipotesi del dualismo onda-corpuscolo di De Broglie (<MathEq math="\lambda = h / (mv)" />) e l'insopprimibile <strong>Principio di Indeterminazione di Heisenberg</strong> (<MathEq math="\Delta x \cdot \Delta p \ge \frac{h}{4\pi}" />), l'idea della "traiettoria certa" fu disintegrata. 
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 text-center rounded-xl font-mono text-xl text-zinc-800 dark:text-zinc-200 my-6 shadow-inner border border-zinc-200 dark:border-zinc-800">
            <MathEq math="\hat{H}\Psi = E\Psi" />
          </div>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Risolvendo l'equazione differenziale di Schrödinger per l'atomo di Idrogeno, l'elettrone diviene una nuvola di densità probabilistica spaziale descritta dalla funzione d'onda <MathEq math="\Psi" />. La regione di spazio in cui vi è una probabilità predeterminata (solitamente 90-95%) di intercettare l'elettrone è definita <strong>Orbitale Atomico</strong>, caratterizzato da quattro numeri quantici (<MathEq math="n, l, m_l, m_s" />).
          </p>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year2/SistemaPeriodicoLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function SistemaPeriodicoLesson() {
  return (
    <LessonTemplate
      title="Il Sistema Periodico"
      subtitle="La Legge della Periodicità e le Proprietà Periodiche (Energia di Ionizzazione ed Elettronegatività)."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Architettura di Mendeleev e Moseley</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La Tavola Periodica non è una mera tabulazione catalogatrice, ma la massima espressione della simmetria quantistica sottostante la materia. Mentre Mendeleev ordinò empiricamente gli elementi per massa atomica crescente individuando andamenti periodici delle loro reattività, H. Moseley (attraverso la spettroscopia a raggi X) corresse il tiro: l'ordinamento naturale è imposto dal <strong>Numero Atomico (Z)</strong>, ossia il numero di protoni nucleari.
          </p>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300 mt-4">
            La struttura in <strong>Periodi</strong> (righe orizzontali) rappresenta il riempimento progressivo di un guscio quantico principale (<MathEq math="n" />), mentre i <strong>Gruppi</strong> (colonne verticali) raccolgono elementi con un'isomorfica configurazione elettronica di valenza, garantendo loro comportamenti chimici (reazioni e stechiometrie) quasi identici.
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">I Vettori delle Proprietà Periodiche</h3>
          <div className="space-y-6 mt-6">
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-amber-900 dark:text-amber-400 mb-2">Energia di Ionizzazione (<MathEq math="E_i" />)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                L'energia minimale (espressa in kJ/mol o eV) necessaria per strappare un elettrone a un atomo isolato allo stato gassoso. Aumenta lungo il periodo (causa innalzamento della carica nucleare efficace, <MathEq math="Z_{eff}" />) e diminuisce scendendo lungo il gruppo (causa incremento del raggio atomico ed effetto schermo).
              </p>
            </div>
            
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-purple-900 dark:text-purple-400 mb-2">Elettronegatività (<MathEq math="\chi" />)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                A differenza di <MathEq math="E_i" /> (misurabile termodinamicamente), l'elettronegatività è un costrutto empirico (scala Pauling) che quantifica la tendenza competitiva di un atomo ad attrarre su di sé il doppietto elettronico condiviso in un <strong>legame covalente</strong>. Il Fluoro (<MathEq math="F" />, 3.98) è l'apice, mentre i metalli alcalini giacciono al fondo.
              </p>
            </div>
          </div>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year2/LegamiChimiciLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function LegamiChimiciLesson() {
  return (
    <LessonTemplate
      title="I Legami Chimici"
      subtitle="Regola dell'ottetto, legame ionico, covalente e teoria VB."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Imperativo Termodinamico dell'Ottetto</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            In natura, gli atomi isolati (ad eccezione dei Gas Nobili) occupano posizioni ad alta instabilità energetica. Il legame chimico sorge spontaneamente come processo esoergonico per far collassare l'energia potenziale del sistema, raggiungendo l'isoelettronicità con il gas nobile più vicino, saturando l'orbitale di valenza (Regola dell'Ottetto di Lewis, 8 elettroni nel guscio <MathEq math="ns^2 np^6" />).
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">La Spettro dei Legami Interatomici</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-blue-900 dark:text-blue-400 mb-2">1. Legame Ionico (<MathEq math="\Delta \chi > 1.7" />)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                Si verifica un asimmetrico trasferimento totale di elettroni dal metallo (che si ossida a Catione) al non-metallo (che si riduce ad Anione). Il legame risultante non è direzionale, ma si esprime come un'immensa rete tridimensionale di attrazioni coulombiane (<strong>Reticolo Cristallino</strong>), conferendo altissimi punti di fusione (es. <MathEq math="\text{NaCl}" />).
              </p>
            </div>
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-emerald-900 dark:text-emerald-400 mb-2">2. Legame Covalente (<MathEq math="\Delta \chi < 1.7" />)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                Condivisione degenerata di uno o più doppietti elettronici (<MathEq math="e^-" />). Se <MathEq math="\Delta \chi \approx 0" /> il legame è <em>puro o apolare</em> (es. <MathEq math="\text{O}_2" />); se esiste un debole gradiente, è <em>polare</em> (es. <MathEq math="\text{H-Cl}" />). La Teoria del Legame di Valenza (VB) lo descrive come la compenetrazione (overlap) costruttiva delle funzioni d'onda degli orbitali atomici parzialmente vuoti.
              </p>
            </div>
          </div>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year2/FormaMolecoleLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function FormaMolecoleLesson() {
  return (
    <LessonTemplate
      title="La Forma delle Molecole e le Forze Intermolecolari"
      subtitle="Geometria VSEPR, ibridazione degli orbitali e Forze di Van der Waals."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">La Teoria VSEPR (Valence Shell Electron Pair Repulsion)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La topologia tridimensionale di una molecola (essenziale per determinare la sua polarità globale e le interazioni biologiche) è dettata dalla repulsione elettrostatica minimizzata. Le coppie elettroniche (sia di legame che solitarie, o <em>lone pairs</em>) localizzate sul guscio di valenza dell'atomo centrale si dispongono alla massima distanza angolare possibile sulla superficie di una sfera immaginaria.
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 rounded-xl my-6">
            <ul className="list-disc pl-5 text-sm text-zinc-700 dark:text-zinc-300 space-y-2">
              <li><strong>2 Domini elettronici:</strong> Geometria Lineare (<MathEq math="180^\circ" />, Ibridazione <MathEq math="sp" />, es. <MathEq math="\text{CO}_2" />).</li>
              <li><strong>3 Domini elettronici:</strong> Geometria Planare Trigonale (<MathEq math="120^\circ" />, Ibridazione <MathEq math="sp^2" />, es. <MathEq math="\text{BF}_3" />).</li>
              <li><strong>4 Domini elettronici:</strong> Geometria Tetraedrica (<MathEq math="109.5^\circ" />, Ibridazione <MathEq math="sp^3" />, es. <MathEq math="\text{CH}_4" />).</li>
            </ul>
          </div>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Tuttavia, i <em>lone pairs</em> esercitano un'ingombro sterico repulsivo maggiore rispetto alle coppie di legame, comprimendo gli angoli. Ad esempio, nell'acqua (<MathEq math="\text{H}_2\text{O}" />), i due <em>lone pairs</em> dell'ossigeno schiacciano l'angolo H-O-H da <MathEq math="109.5^\circ" /> a circa <MathEq math="104.5^\circ" />.
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Interazioni Deboli: Le Forze Intermolecolari</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Mentre i legami intramolecolari dictano l'identità chimica (centinaia di kJ/mol), i legami <em>intermolecolari</em> determinano lo stato di aggregazione a temperatura ambiente (1-40 kJ/mol). L'intero spettro è definito come Forze di Van der Waals:
          </p>
          <div className="grid grid-cols-1 gap-4 mt-6">
            <div className="bg-white dark:bg-zinc-950 p-4 border border-zinc-200 dark:border-zinc-800 rounded">
              <strong className="text-zinc-900 dark:text-zinc-50">1. Dipolo-Dipolo:</strong> Attrazione puramente elettrostatica tra molecole permanentemente asimmetriche (polari, es. HCl).
            </div>
            <div className="bg-white dark:bg-zinc-950 p-4 border border-zinc-200 dark:border-zinc-800 rounded">
              <strong className="text-zinc-900 dark:text-zinc-50">2. Legame a Idrogeno:</strong> L'interazione intermolecolare suprema. Richiede un idrogeno legato a un atomo minuscolo e iper-elettronegativo (N, O, F). La parziale carica positiva estrema dell'idrogeno funge da ponte gravitazionale verso i <em>lone pairs</em> adiacenti (fondamentale in H2O e DNA).
            </div>
            <div className="bg-white dark:bg-zinc-950 p-4 border border-zinc-200 dark:border-zinc-800 rounded">
              <strong className="text-zinc-900 dark:text-zinc-50">3. Forze di dispersione di London:</strong> Dominanti nelle molecole apolari e gas nobili. Generato da asimmetrie temporanee istantanee della nuvola elettronica (dipolo indotto). Crescono linearmente col peso molecolare (polarizzabilità).
            </div>
          </div>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year2/QuantitaSostanzaMoleLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function QuantitaSostanzaMoleLesson() {
  return (
    <LessonTemplate
      title="La Quantità di Sostanza in Moli"
      subtitle="La Mole, la Costante di Avogadro e il ponte tra macro e microscopico."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">Il Paradosso Quantitativo del Chimico</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Le reazioni chimiche avvengono su base particellare (1 atomo di Carbonio + 1 molecola di <MathEq math="\text{O}_2" /> <MathEq math="\rightarrow" /> 1 molecola di <MathEq math="\text{CO}_2" />), tuttavia in laboratorio i reagenti si pesano su scale macroscopiche (in grammi). Poiché un singolo atomo possiede una massa irrisoria (dell'ordine dei <MathEq math="10^{-24} \text{ g}" />, calcolata in u.m.a.), era necessario un ponte di conversione colossale.
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">La Mole e il Numero di Avogadro</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La <strong>Mole (mol)</strong> è la grandezza base del S.I. per la "quantità di sostanza". Essa è definita rigorosamente come la quantità di materia che contiene esattamente un numero di entità elementari (atomi, molecole, ioni) pari alla <strong>Costante di Avogadro</strong>:
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 text-center rounded-xl font-mono text-2xl text-zinc-800 dark:text-zinc-200 my-6 shadow-inner border border-zinc-200 dark:border-zinc-800">
            <MathEq math="N_A = 6.02214076 \times 10^{23} \text{ entità/mol}" />
          </div>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La magia della mole consiste in questo: una mole di <em>qualsiasi sostanza</em> possiede una massa in grammi (<strong>Massa Molare, <MathEq math="MM" /></strong>) numericamente identica al suo Peso Atomico / Molecolare letto sulla Tavola Periodica. 
            Ad esempio, un atomo di Carbonio-12 pesa <MathEq math="12 \text{ u}" />; un'intera mole di Carbonio-12 pesa esattamente <MathEq math="12 \text{ grammi}" />.
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Calcolo Stechiometrico Fondamentale</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La conversione tra la massa misurabile e le particelle reattive sfrutta la formula regina della stechiometria ponderale:
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-4 text-center rounded font-mono text-xl text-zinc-800 dark:text-zinc-200 mt-4">
            <MathEq math="n \, (\text{moli}) = \frac{m \, (\text{massa in g})}{MM \, (\text{massa molare in g/mol})}" />
          </div>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year3/ClassificazioneCompostiLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function ClassificazioneCompostiLesson() {
  return (
    <LessonTemplate
      title="Classificazione e Nomenclatura dei Composti"
      subtitle="Nomenclatura IUPAC, tradizionale e i numeri di ossidazione."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">Il Numero di Ossidazione (n.o.)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Prima di procedere all'assegnazione nomenclaturale (il naming), è imperativo dominare il concetto di <strong>Numero di Ossidazione</strong>. Si tratta di una carica formale (fittizia in molecole covalenti, reale nei composti ionici) assegnata ad un atomo in una molecola assumendo che gli elettroni di legame siano trasferiti totalmente all'atomo più elettronegativo. La somma dei n.o. in una molecola neutra deve sempre annullarsi (<MathEq math="\Sigma = 0" />).
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Tassonomia Inorganica e Nomenclatura</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La classificazione primaria si biforca basandosi sull'elettronegatività dell'elemento principale reagito con ossigeno (<MathEq math="\text{O}" />) o idrogeno (<MathEq math="\text{H}" />). Attualmente convivono due sistemi: il sistema tradizionale (suffissi <em>-oso/-ico</em>, desueto ma endemico) e il sistema razionale IUPAC.
          </p>
          
          <div className="space-y-6 mt-6">
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-blue-900 dark:text-blue-400 mb-2">Ossidi (con Ossigeno <MathEq math="O^{2-}" />)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                L'unione di O con metalli genera <strong>Ossidi Basici</strong> (es. <MathEq math="\text{Na}_2\text{O}" />), che reagendo in acqua formeranno gli <strong>Idrossidi</strong> (Basi forti, <MathEq math="\text{NaOH}" />).
                L'unione di O con non-metalli genera <strong>Ossidi Acidi o Anidridi</strong> (es. <MathEq math="\text{SO}_3" />), che in acqua collasseranno in <strong>Ossidacidi</strong> (<MathEq math="\text{H}_2\text{SO}_4" />).
              </p>
            </div>

            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-green-900 dark:text-green-400 mb-2">Composti con Idrogeno (Idruri e Idracidi)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                L'unione con metalli a bassa elettronegatività (<MathEq math="H" /> a <MathEq math="-1" />) produce <strong>Idruri salini</strong> (<MathEq math="\text{NaH}" />). L'unione con i potentissimi non-metalli dei gruppi 16 e 17 (alogeni) cede il protone (<MathEq math="H^+" />) formando gli <strong>Idracidi</strong> gassosi (<MathEq math="\text{HCl}, \text{H}_2\text{S}" />), altamente dissociativi in acqua.
              </p>
            </div>

            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-red-900 dark:text-red-400 mb-2">Sali: Ternari e Binari</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                La fusione di un catione metallico (proveniente da una base) e l'anione (proveniente dalla de-protonazione di un acido). Se non possiedono Ossigeno sono Binari (<MathEq math="\text{NaCl}" />, Cloruro di Sodio); se possiedono l'anione poliatomico ossigenato sono Ternari (<MathEq math="\text{CaSO}_4" />, Solfato di Calcio).
              </p>
            </div>
          </div>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year3/ReazioniStechiometriaLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function ReazioniStechiometriaLesson() {
  return (
    <LessonTemplate
      title="Le Reazioni Chimiche: Stechiometria e Resa"
      subtitle="Analisi termodinamica della resa, reagente limitante e purezza."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Architettura Quantitativa delle Reazioni</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Una reazione chimica, per le equazioni di calcolo quantitativo, è gestita come una funzione matematica strettamente proporzionale. I coefficienti stechiometrici (i numeri davanti alle formule) non indicano mai rapporti di masse in grammi, bensì esclusivi <strong>rapporti molari</strong> (o rapporti di volumi se si lavora esclusivamente con gas in condizioni PVT costanti).
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Il Reagente Limitante</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Nei processi sintetici reali, i reagenti non sono forniti nell'esatta e asettica proporzione stechiometrica imposta dall'equazione chimica bilanciata. Per ragioni economiche o termodinamiche, un reagente è solitamente somministrato in forte eccesso. 
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 my-6 shadow-sm">
            <p className="text-zinc-700 dark:text-zinc-300">
              Il <strong>Reagente Limitante</strong> è il reagente che possiede il rapporto molecolare inferiore (Moli Reali / Coefficiente Stechiometrico). La sua fine decreta l'arresto immediato e insindacabile della reazione, determinando da solo la massa massima teorica di prodotto generabile.
            </p>
          </div>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Resa Teorica vs Resa Effettiva</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            L'espressione stoichio-matematica fornisce sempre un picco di perfezione irrealistico: la <strong>Resa Teorica</strong> (il 100% della materia trasferita dai reagenti ai prodotti). 
            Tuttavia, le collisioni intermolecolari inefficaci, reazioni secondarie collaterali (reazioni parassite) ed inevitabili perdite meccaniche durante l'estrazione e cristallizzazione del prodotto abbattono vertiginosamente la sintesi.
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-4 text-center rounded font-mono text-xl text-zinc-800 dark:text-zinc-200 mt-4">
            <MathEq math="\text{Resa Percentuale} (\%) = \left( \frac{\text{Resa Effettiva}}{\text{Resa Teorica}} \right) \times 100" />
          </div>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year3/ProprietaSoluzioniLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function ProprietaSoluzioniLesson() {
  return (
    <LessonTemplate
      title="Le Proprietà delle Soluzioni"
      subtitle="Concentrazione molare, dissociazione elettrolitica e proprietà colligative."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">Solvatazione e Dissociazione Elettrolitica</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Una soluzione è una fase macroscopica perfettamente omogenea derivata dalla miscelazione di un Solvent (sostanza maggioritaria) e di un Soluto. L'acqua (solvente universale) disintegra il reticolo ionico dei sali grazie alla sua estrema costante dielettrica (<MathEq math="\epsilon \approx 80" />). Gli ioni dissociati (<MathEq math="\text{Na}^+, \text{Cl}^-" />) vengono avvolti (solvatati) dal dipolo dell'acqua, garantendo conducibilità elettrica (<strong>Soluzioni Elettrolitiche</strong>).
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Unità di Concentrazione in Chimica</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300 mb-4">
            A livello accademico la concentrazione percentuale peso/volume (<MathEq math="\% p/V" />) è deprecata, adottando grandezze molari esatte:
          </p>
          <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 space-y-4">
            <div>
              <h4 className="font-bold text-zinc-900 dark:text-zinc-50 mb-1">Molarità (<MathEq math="M" />)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">Moli di soluto per Litro di soluzione. È fortemente dipendente dalla temperatura (poiché il volume si espande termicamente). <MathEq math="M = \frac{n}{V}" /></p>
            </div>
            <div>
              <h4 className="font-bold text-zinc-900 dark:text-zinc-50 mb-1">Molalità (<MathEq math="m" />)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">Moli di soluto per kg di Solvent puro. È termodinamicamente indipendente dalla T, indispensabile per le proprietà colligative. <MathEq math="m = \frac{n}{m_{\text{kg}}}" /></p>
            </div>
            <div>
              <h4 className="font-bold text-zinc-900 dark:text-zinc-50 mb-1">Frazione Molare (<MathEq math="X_i" />)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">Rapporto puro (adimensionale) tra le moli della sostanza e le moli totali in soluzione. Usato nella Legge di Raoult.</p>
            </div>
          </div>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Le Proprietà Colligative</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Sono anomalie termodinamiche della soluzione. Dipendono <em>esclusivamente</em> dal numero totale (concentrazione) delle particelle di soluto, ma sono totalmente cieche alla natura chimica o alla massa della particella (che sia enorme glucosio o un piccolo ione sodio). 
            Ricordando il coefficiente di dissociazione (o di van 't Hoff, <MathEq math="i" />), le proprietà colligative includono:
          </p>
          <ul className="list-disc pl-5 text-sm text-zinc-700 dark:text-zinc-300 space-y-3 mt-4">
            <li><strong>Abbassamento Tensione di Vapore (Legge di Raoult):</strong> Il soluto interferisce superficialmente con l'evaporazione del solvente, rallentandola.</li>
            <li><strong>Innalzamento Ebullioscopico (<MathEq math="\Delta T_b = K_b \cdot m \cdot i" />):</strong> Il solvente "fatica" a eguagliare la pressione atmosferica, l'ebollizione richiede temperatura superiore (es. l'acqua salata bolle oltre 100°C).</li>
            <li><strong>Abbassamento Crioscopico (<MathEq math="\Delta T_c = K_c \cdot m \cdot i" />):</strong> Il disordine del soluto impedisce al solvente di cristallizzare agevolmente (il mare gela sotto 0°C).</li>
            <li><strong>Pressione Osmotica (<MathEq math="\Pi = M \cdot R \cdot T \cdot i" />):</strong> La gigantesca pressione idrostatica generata dal differenziale di densità entropica attraverso una membrana semi-permeabile, base propulsiva della botanica vitale e dei globuli rossi.</li>
          </ul>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year3/TermodinamicaLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function TermodinamicaLesson() {
  return (
    <LessonTemplate
      title="La Termodinamica"
      subtitle="Entalpia, Entropia e l'inesorabile scorrere del tempo molecolare (Gibbs)."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Architettura Energetica della Materia (Entalpia, <MathEq math="H" />)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La Prima Legge della Termodinamica postula l'incorruttibilità dell'energia interna dell'universo. Nelle reazioni chimiche operanti in recipienti aperti (esobariche, <MathEq math="P = \text{cost}" />), il calore scambiato corrisponde a una funzione di stato fondamentale: l'<strong>Entalpia (<MathEq math="\Delta H" />)</strong>.
            Una reazione che spezza legami stabili e crea configurazioni precarie richiede iniezione di calore (<strong>Endotermica</strong>, <MathEq math="\Delta H > 0" />). Inversamente, la transizione verso legami forti emette calore distruttivo nell'ambiente (<strong>Esotermica</strong>, <MathEq math="\Delta H < 0" /> come la combustione).
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">L'Inesorabile Disordine Universale (Entropia, <MathEq math="S" />)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Se l'Entalpia giustifica il calore, fallisce nello spiegare la spontaneità. Perché il ghiaccio fonde a 25°C pur dovendo *assorbire* calore termico sfavorevole? 
            La risposta giace nella Seconda Legge della Termodinamica: la Freccia del Tempo asseconda unicamente e inevitabilmente l'aumento dell'<strong>Entropia (<MathEq math="\Delta S" />)</strong>, ossia il disordine probabilistico micro-stati. Fondere un cristallo perfettamente ordinato in liquido turbolento aumenta drammaticamente <MathEq math="S" />.
          </p>
          
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Il Verdetto di Spontaneità: Energia Libera di Gibbs</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Josiah Willard Gibbs fuse nel 1876 l'Entalpia e l'Entropia in un'unica, brutale equazione magistrale in grado di diagnosticare a priori la fattibilità e spontaneità di qualsiasi processo chimico:
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 text-center rounded-xl font-mono text-2xl text-zinc-800 dark:text-zinc-200 my-6 shadow-inner border border-zinc-200 dark:border-zinc-800">
            <MathEq math="\Delta G = \Delta H - T \cdot \Delta S" />
          </div>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La spontaneità chimica non è un'opinione; essa esiste <em>esclusivamente</em> se il saldo totale energetico per produrre lavoro utile, <MathEq math="\Delta G" />, assume un valore rigorosamente negativo (<MathEq math="\Delta G < 0" /> - reazione esoergonica).
          </p>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year3/CineticaEquilibrioLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function CineticaEquilibrioLesson() {
  return (
    <LessonTemplate
      title="La Cinetica e l'Equilibrio"
      subtitle="La velocità molecolare, Arrhenius e l'Equilibrio di Le Châtelier."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">Cinetica: Teoria degli Urti e Attivazione</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La Termodinamica preannuncia la spontaneità (il 'se'), ma è la <strong>Cinetica Chimica</strong> a governare le tempistiche termiche (il 'quando'). Onde affinché una reazione avvenga, le molecole dei reagenti devono scontrarsi collidendo (Teoria degli Urti). Non basta scontrarsi: la collisione deve possedere un orientamento spaziale rigoroso e, criticamente, energia traslazionale sufficiente a lacerare l'involucro elettronico dei legami. 
            Questo muro energetico iniziale è la formidabile <strong>Energia di Attivazione (<MathEq math="E_a" />)</strong>.
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 text-center rounded-xl font-mono text-xl text-zinc-800 dark:text-zinc-200 my-6 shadow-inner border border-zinc-200 dark:border-zinc-800">
            <MathEq math="k = A \cdot e^{-\frac{E_a}{R T}}" />
          </div>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            L'espressione esponenziale di Arrhenius sentenzia che un irrisorio incremento termico (in T) amplifica colossalmante la frazione di molecole dotate di <MathEq math="E_a" />, impennando violentemente la costante cinetica <MathEq math="k" />. L'uso dei <strong>Catalizzatori</strong> altera invece chimicamente il percorso reattivo interponendo stati di transizione complessi a bassissima <MathEq math="E_a" />, operando magicamente sull'esponente <MathEq math="e" />.
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">L'Equilibrio Dinamico (Legge di Azione di Massa)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La quasi totalità delle reazioni chimiche (in recipienti sigillati) non giunge mai a compimento terminale (100% resa). Essendo fenomeni bidirezionali e reversibili, non appena i prodotti vengono forgiati, essi iniziano immediatamente a scontrarsi ricostruendo all'indietro i reagenti nativi (<MathEq math="v_{\text{diretta}} \rightleftharpoons v_{\text{inversa}}" />).
            Quando le velocità si equivalgono, si instaura un "stallo dinamico apparentemente immobile": l'Equilibrio. 
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-4 text-center rounded font-mono text-xl text-zinc-800 dark:text-zinc-200 mt-4 mb-4">
            <MathEq math="K_{eq} = \frac{[\text{Prodotti}]}{[\text{Reagenti}]}" />
          </div>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Il geniale <strong>Principio di Le Châtelier-Braun</strong> codifica la resilienza del sistema chimico: perturbando un equilibrio tramite iniezioni di pressione, estrazioni forzate di prodotto o sbalzi isotermici, il sistema genererà un contro-feedback endogeno per fagocitare la perturbazione e ritornare nel bacino gravitazionale dell'Equilibrio.
          </p>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}"""
}

for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {full_path}')
