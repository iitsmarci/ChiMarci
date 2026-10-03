import os

base_dir = os.path.join(os.path.dirname(__file__), 'src', 'components', 'content')

files = {
  'year4/AcidiBasiLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function AcidiBasiLesson() {
  return (
    <LessonTemplate
      title="Gli Acidi e le Basi"
      subtitle="Teorie di Arrhenius, Brønsted-Lowry, Lewis e il prodotto ionico dell'acqua."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Evoluzione del Paradigma Acido-Base</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La dicotomia acido-base ha attraversato tre rivoluzioni teoriche successive, espandendo progressivamente il dominio di applicabilità.
          </p>
          
          <div className="space-y-6 mt-6">
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-indigo-900 dark:text-indigo-400 mb-2">1. Teoria di Arrhenius (1887)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                La prima formalizzazione. Un <strong>Acido</strong> è una specie che, in soluzione acquosa, libera ioni Idrogeno (<MathEq math="H^+" />). Una <strong>Base</strong> libera ioni idrossido (<MathEq math="OH^-" />). Questa teoria, seppur pionieristica, è castrata dall'obbligo del solvente acqua.
              </p>
            </div>
            
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-emerald-900 dark:text-emerald-400 mb-2">2. Teoria di Brønsted-Lowry (1923)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                La rivoluzione del protone. Un <strong>Acido</strong> è un <em>donatore</em> di protoni (<MathEq math="H^+" />), mentre una <strong>Base</strong> è un <em>accettore</em> di protoni. L'acqua non è più necessaria. Da qui nasce il concetto di <strong>Coppie Coniugate</strong>: un acido, cedendo il protone, si converte nella sua "base coniugata".
              </p>
            </div>

            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-rose-900 dark:text-rose-400 mb-2">3. Teoria di Lewis (1923)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                L'astrazione definitiva basata sugli orbitali. Un <strong>Acido di Lewis</strong> è un accettore di un <em>doppietto elettronico</em> (possiede un orbitale vuoto, es. <MathEq math="BF_3" />). Una <strong>Base di Lewis</strong> è un donatore di un doppietto elettronico (possiede un <em>lone pair</em>, es. <MathEq math="NH_3" />).
              </p>
            </div>
          </div>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">L'Autoprotolisi dell'Acqua e il pKw</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            L'acqua pura non è inerte, ma si auto-dissocia (anfoteria) in misura minuscola: 
            <MathEq math="\text{H}_2\text{O} + \text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{OH}^-" />. 
            La costante di questo equilibrio a 25°C è il Prodotto Ionico (<MathEq math="K_w" />):
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-4 text-center rounded font-mono text-xl text-zinc-800 dark:text-zinc-200 my-4">
            <MathEq math="K_w = [H_3O^+][OH^-] = 1.0 \times 10^{-14}" />
          </div>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year4/PhIndicatoriLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function PhIndicatoriLesson() {
  return (
    <LessonTemplate
      title="Il Calcolo del pH e gli Indicatori"
      subtitle="La scala logaritmica del pH, soluzioni tampone e titolazioni."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">La Matematica del pH</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Poiché la concentrazione degli ioni idronio (<MathEq math="[H_3O^+]" />) varia su scale spaventosamente ampie (da <MathEq math="10^0" /> a <MathEq math="10^{-14} \text{ M}" />), S.P.L. Sørensen nel 1909 introdusse l'operatore matematico "p" (logaritmo decimale negativo) per linearizzare la lettura:
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-6 text-center rounded-xl font-mono text-2xl text-zinc-800 dark:text-zinc-200 my-6 shadow-inner border border-zinc-200 dark:border-zinc-800">
            <MathEq math="pH = -\log_{10}[H_3O^+]" />
          </div>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Trattandosi di scala logaritmica negativa, una diminuzione di 1 unità di pH corrisponde a un <strong>aumento di 10 volte</strong> dell'acidità reale. Un pH = 7.0 indica perfetta neutralità termodinamica a 25°C.
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Sistemi Tampone (Buffer)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Un <strong>Tampone</strong> è una soluzione chirurgicamente calibrata in grado di opporsi, assorbendole termodinamicamente, a variazioni drammatiche di pH in seguito all'aggiunta di acidi o basi forti. Biologicamente, il tampone Carbonato/Bicarbonato nel plasma sanguigno mantiene la vita ancorata al fragile pH 7.4.
          </p>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300 mt-4">
            Chimicamente, è composto da un Acido Debole mescolato a un suo sale (la sua Base Coniugata forte). Il pH di un tampone è dettato dalla regale Equazione di Henderson-Hasselbalch:
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-4 text-center rounded font-mono text-xl text-zinc-800 dark:text-zinc-200 my-4">
            <MathEq math="pH = pK_a + \log\left(\frac{[\text{Base Coniugata}]}{[\text{Acido}]}\right)" />
          </div>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Titolazione e Indicatori</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La <strong>Titolazione</strong> è l'analisi volumetrica regina per determinare la concentrazione incognita di un acido tramite l'aggiunta goccia-a-goccia di una base a titolo noto (o viceversa). 
            Il raggiungimento del Punto Equivalente (dove moli Acido = moli Base) è visivamente segnalato dal viraggio di colore degli <strong>Indicatori pH</strong>, organiche macromolecole il cui colore è dipendente dallo stato di protonazione (es. Fenolftaleina: incolore sotto pH 8.2, fucsia fiammante in ambiente basico).
          </p>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year4/ElettrochimicaLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function ElettrochimicaLesson() {
  return (
    <LessonTemplate
      title="Elettrochimica e Reazioni Redox"
      subtitle="Pile di Volta, equazione di Nernst e celle elettrolitiche."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Anatomia delle Reazioni di Ossidoreduzione</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            A differenza delle banali reazioni acido-base (scambio di protoni), le <strong>Redox</strong> implicano un trasferimento balistico di elettroni. 
            L'<strong>Ossidazione</strong> (Ox) è la brutale perdita di elettroni (aumento del n.o.), mentre la <strong>Riduzione</strong> (Red) è l'acquisizione rapace di elettroni (diminuzione del n.o.). Esse devono obbligatoriamente coesistere.
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">La Pila Galvanica (Cella Voltaica)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Il trionfo della termodinamica applicata: intercettare il flusso spontaneo di elettroni di una redox in un circuito esterno (filo di rame) per estrarre <strong>lavoro elettrico</strong> (<MathEq math="\Delta G < 0" />).
            La Pila Daniell separa fisicamente le semi-reazioni:
          </p>
          <ul className="list-disc pl-5 text-sm text-zinc-700 dark:text-zinc-300 space-y-3 mt-4">
            <li><strong>Anodo (Polo Negativo):</strong> L'elettrodo in cui avviene l'Ossidazione (es. Zinco metallico che si corrode in <MathEq math="Zn^{2+}" /> rilasciando e-).</li>
            <li><strong>Catodo (Polo Positivo):</strong> L'elettrodo in cui avviene la Riduzione (es. ioni <MathEq math="Cu^{2+}" /> che si riducono a Rame metallico assorbendo e-).</li>
            <li><strong>Ponte Salino:</strong> Tubo ionico indispensabile per neutralizzare l'accumulo di carica nelle semi-celle.</li>
          </ul>
          
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">L'Equazione di Nernst</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Il potenziale standard di cella (<MathEq math="\Delta E^\circ" />) calcolato dalle tabelle vale solo a 1M e 25°C. Il genio di Walther Nernst fornì l'equazione per il calcolo del potenziale reale dipendente dalla concentrazione:
          </p>
          <div className="bg-zinc-50 dark:bg-zinc-900/50 p-4 text-center rounded font-mono text-xl text-zinc-800 dark:text-zinc-200 my-4">
            <MathEq math="E = E^\circ - \frac{R T}{n F} \ln Q" />
          </div>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">La Cella Elettrolitica</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            L'esatto inverso della Pila: sfruttare una brutale d.d.p. esterna (un alimentatore) per pompare elettroni in salita contro il gradiente di potenziale, costringendo una reazione <strong>non spontanea</strong> (<MathEq math="\Delta G > 0" />) ad avvenire (es. ricarica della batteria, elettrolisi dell'acqua, placcatura galvanica). Qui l'Anodo diviene il polo Positivo e il Catodo il polo Negativo.
          </p>
        </div>
      }
      flashcards={[]}
      exercises={[]}
      quiz={[]}
    />
  );
}""",
  'year5/CarbonioIdrocarburiLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function CarbonioIdrocarburiLesson() {
  return (
    <LessonTemplate
      title="Il Carbonio e gli Idrocarburi"
      subtitle="Ibridazione, alcani, alcheni, alchini e la nomenclatura organica."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Unicità Quantistica del Carbonio</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La Chimica Organica (che permea il 95% della vita e dell'industria polimerica) poggia interamente sulla miracolosa flessibilità quantistica del Carbonio (Z=6). Situato esattamente al centro del periodo, il Carbonio possiede elettronegatività media e 4 elettroni di valenza. Promuovendo un elettrone dal 2s al 2p vuoto e mescolando le funzioni d'onda orbitaliche, attua il processo di <strong>Ibridazione</strong>:
          </p>
          <ul className="list-disc pl-5 text-sm text-zinc-700 dark:text-zinc-300 space-y-3 mt-4">
            <li><strong><MathEq math="sp^3" />:</strong> 4 legami singoli (<MathEq math="\sigma" />), geometria tetraedrica (109.5°), molecole sature tridimensionali (es. Metano).</li>
            <li><strong><MathEq math="sp^2" />:</strong> 3 legami <MathEq math="\sigma" /> e 1 legame <MathEq math="\pi" /> puro, geometria planare trigonale (120°), doppi legami (es. Etene).</li>
            <li><strong><MathEq math="sp" />:</strong> 2 legami <MathEq math="\sigma" /> e 2 legami <MathEq math="\pi" />, geometria lineare (180°), tripli legami (es. Etino).</li>
          </ul>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">La Tassonomia degli Idrocarburi (Alifatici)</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            Le catene scheletriche basali, formate da C e H:
          </p>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-blue-900 dark:text-blue-400 mb-2">Alcani (Saturi)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                Formula generale <MathEq math="C_n H_{2n+2}" />. Nomenclatura suffisso <strong>-ano</strong>. Essendo dominati da legami <MathEq math="\sigma" /> stabili ed apolari, sono chimicamente "paraffine" (poco affini a reagire), utilizzati primariamente come combustibili (Metano, Ottano).
              </p>
            </div>
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-amber-900 dark:text-amber-400 mb-2">Alcheni (Insaturi)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                Formula <MathEq math="C_n H_{2n}" />. Suffisso <strong>-ene</strong>. Presenza di un doppio legame (nuvola elettronica densa). Sono altamente reattivi verso agenti elettrofili (Addizione Elettrofila) e permettono la sintesi di plastiche (Polietilene).
              </p>
            </div>
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-rose-900 dark:text-rose-400 mb-2">Alchini (Insaturi)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                Formula <MathEq math="C_n H_{2n-2}" />. Suffisso <strong>-ino</strong>. Presenza di un triplo legame (<MathEq math="C \equiv C" />). La catena è lineare. Altissima densità energetica (es. acetilene per le fiamme ossidriche).
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
  'year5/GruppiFunzionaliLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function GruppiFunzionaliLesson() {
  return (
    <LessonTemplate
      title="I Gruppi Funzionali"
      subtitle="L'inserimento dell'eteroatomo: alcoli, aldeidi, acidi carbossilici ed esteri."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Eteroatomo e il Sito Reattivo</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La chimica organica acquista vita, tossicità, colore e fragranza quando l'anodina catena carboniosa viene interrotta da "eteroatomi" (Ossigeno, Azoto, Alogeni). L'atomo elettronegativo polarizza il legame (<MathEq math="C^{\delta+} - X^{\delta-}" />), creando un punto critico di vulnerabilità elettronica: il <strong>Gruppo Funzionale</strong>.
          </p>

          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mt-10">Tassonomia dei Derivati Ossigenati</h3>
          
          <div className="space-y-6 mt-6">
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 flex flex-col md:flex-row gap-6 items-center">
              <div className="w-full md:w-2/3">
                <h4 className="text-xl font-bold text-teal-900 dark:text-teal-400 mb-2">Alcoli (<MathEq math="-OH" />)</h4>
                <p className="text-sm text-zinc-700 dark:text-zinc-300">
                  Gruppo Idrossile (suffisso -olo). Permette il legame a idrogeno formidabile. Solubilizza le corte catene carboniose in acqua. (es. Etanolo, l'alcol del vino, letale tossina epatica a dosi sub-acute).
                </p>
              </div>
            </div>

            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 flex flex-col md:flex-row gap-6 items-center">
              <div className="w-full md:w-2/3">
                <h4 className="text-xl font-bold text-indigo-900 dark:text-indigo-400 mb-2">Aldeidi e Chetoni (<MathEq math="C=O" />)</h4>
                <p className="text-sm text-zinc-700 dark:text-zinc-300">
                  Gruppo Carbonilico. Nelle <strong>Aldeidi</strong> (-ale) è sul carbonio terminale, nei <strong>Chetoni</strong> (-one) è incastonato nella catena. Il doppio legame C=O è fortemente polarizzato, rendendo il carbonio un potente elettrofilo. Costituiscono molte essenze aromatiche (vanillina, canfora).
                </p>
              </div>
            </div>

            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 flex flex-col md:flex-row gap-6 items-center">
              <div className="w-full md:w-2/3">
                <h4 className="text-xl font-bold text-rose-900 dark:text-rose-400 mb-2">Acidi Carbossilici (<MathEq math="-COOH" />)</h4>
                <p className="text-sm text-zinc-700 dark:text-zinc-300">
                  Fusione tra carbonile e idrossile (suffisso -oico). L'ossigeno del C=O richiama elettroni, indebolendo il legame O-H e permettendo il rilascio del protone <MathEq math="H^+" />. Sono acidi deboli formidabili nell'aceto (Acido Acetico) e negli acidi grassi della dieta.
                </p>
              </div>
            </div>

            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 flex flex-col md:flex-row gap-6 items-center">
              <div className="w-full md:w-2/3">
                <h4 className="text-xl font-bold text-amber-900 dark:text-amber-400 mb-2">Ammine (<MathEq math="-NH_2" />) e Ammidi</h4>
                <p className="text-sm text-zinc-700 dark:text-zinc-300">
                  Derivati ammoniacali. Le <strong>Ammine</strong> sono le basi deboli organiche per eccellenza (e fondamento tossicologico per la putrescina e cadaverina). Le <strong>Ammidi</strong> fondono il gruppo amminico con il carbonile (C=O): questo legame ammidico è l'inossidabile "legame peptidico" che cementifica le proteine del tuo corpo.
                </p>
              </div>
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
  'year5/BiomolecoleLesson.tsx': r"""import { LessonTemplate } from "../LessonTemplate";
import { MathEq } from "../../ui/MathEq";

export function BiomolecoleLesson() {
  return (
    <LessonTemplate
      title="Le Biomolecole"
      subtitle="La biochimica della vita: Carboidrati, Lipidi, Proteine e Acidi Nucleici."
      theoryContent={
        <div className="space-y-8">
          <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">L'Ingegneria dei Polimeri Biologici</h3>
          <p className="text-lg leading-relaxed text-zinc-700 dark:text-zinc-300">
            La biologia cellulare non è altro che l'espressione macroscopica della chimica organica in ambiente acquoso confinato. La vita si fonda sull'assemblaggio modulare di monomeri organici semplici in titanici <strong>Biopolimeri</strong> direzionali.
          </p>

          <div className="space-y-6 mt-6">
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-amber-900 dark:text-amber-400 mb-2">1. Carboidrati (Glucidi)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                Poli-idrossi-aldeidi (o chetoni). Monomeri: <strong>Monosaccaridi</strong> (es. Glucosio, combustibile primario). Polimeri di stoccaggio energetico: Glicogeno (animali) e Amido (piante). Polimeri strutturali: Cellulosa, inattaccabile dai nostri enzimi ma base del legno. Il legame è <em>glicosidico</em>.
              </p>
            </div>
            
            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-yellow-900 dark:text-yellow-400 mb-2">2. Lipidi</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                Eterogenea categoria apolare. I <strong>Trigliceridi</strong> (esteri di glicerolo e tre acidi grassi) garantiscono stoccaggio energetico isolante (grasso viscerale). I <strong>Fosfolipidi</strong> (testa polare idrofila e code idrofobe) guidano l'auto-assemblaggio spontaneo delle membrane cellulari impermeabili a doppio strato (la barriera vitale primaria).
              </p>
            </div>

            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-rose-900 dark:text-rose-400 mb-2">3. Proteine (Polipeptidi)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                I veri "motori" molecolari. Monomeri: <strong>20 L-Amminoacidi</strong>, uniti tramite l'inossidabile legame peptidico. La catena lineare (struttura primaria) si auto-folda (ripiega) in un nano-secondo guidata dall'Entropia dell'acqua e dai ponti idrogeno (struttura secondaria/terziaria) in forme 3D iper-specifiche. Fungono da enzimi, anticorpi, canali recettoriali, pompe di membrana.
              </p>
            </div>

            <div className="bg-white dark:bg-zinc-950 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800">
              <h4 className="text-xl font-bold text-blue-900 dark:text-blue-400 mb-2">4. Acidi Nucleici (DNA e RNA)</h4>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                Monomeri: <strong>Nucleotidi</strong> (Zucchero pentoso, gruppo fosfato, base azotata A,T,C,G). Il DNA troneggia come immutabile archivio d'informazione protetto nella cassaforte nucleare, stabilizzato dal miracolo di Watson e Crick (appaiamento complementare A-T, G-C tramite ponti a Idrogeno). L'RNA ne è la trascrizione operativa, destinata ai ribosomi.
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
}"""
}

for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {full_path}')
