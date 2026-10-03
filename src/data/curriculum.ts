export type Topic = {
  slug: string;
  title: string;
  objectives: string;
  hasContent?: boolean;
};

export type YearCurriculum = {
  year: number;
  title: string;
  topics: Topic[];
};

export const curriculum: YearCurriculum[] = [
  {
    year: 1,
    title: "1° Anno: Fondamenti, materia e linguaggio chimico",
    topics: [
      { slug: "le-misure-e-le-grandezze", title: "Cap 1: Le misure e le grandezze", objectives: "Comprendere il Sistema Internazionale, gli errori di misura e le cifre significative.", hasContent: true },
      { slug: "le-trasformazioni-fisiche-della-materia", title: "Cap 2: Le trasformazioni fisiche della materia", objectives: "Stati della materia, calore latente e passaggi di stato.", hasContent: true },
      { slug: "dalle-trasformazioni-chimiche-alla-teoria-atomica", title: "Cap 3: Dalle trasformazioni chimiche alla teoria atomica", objectives: "Dalle reazioni macroscopiche alle leggi ponderali e l'atomo di Dalton.", hasContent: true },
      { slug: "la-teoria-cinetico-molecolare-e-le-leggi-dei-gas", title: "Cap 4: La teoria cinetico-molecolare e le leggi dei gas", objectives: "Comportamento dei gas perfetti e reali, modello cinetico.", hasContent: true },
      { slug: "rappresentare-le-reazioni-chimiche", title: "Cap 5: Rappresentare le reazioni chimiche", objectives: "Simbologia chimica, formule e bilanciamento elementare.", hasContent: true },
    ]
  },
  {
    year: 2,
    title: "2° Anno: Atomo, tavola periodica, legami e quantità chimiche",
    topics: [
      { slug: "le-particelle-dell-atomo", title: "Cap 6: Le particelle dell'atomo", objectives: "Elettroni, protoni, neutroni e modelli di Thomson e Rutherford.", hasContent: true },
      { slug: "la-struttura-dell-atomo", title: "Cap 7: La struttura dell'atomo", objectives: "Modello di Bohr, meccanica quantistica e orbitali atomici.", hasContent: true },
      { slug: "il-sistema-periodico", title: "Cap 8: Il sistema periodico", objectives: "Periodicità, proprietà periodiche ed elettronegatività.", hasContent: true },
      { slug: "i-legami-chimici", title: "Cap 9: I legami chimici", objectives: "Legami covalenti, ionici e metallici. Regola dell'ottetto.", hasContent: true },
      { slug: "la-forma-delle-molecole-e-le-forze-intermolecolari", title: "Cap 10: La forma delle molecole e le forze intermolecolari", objectives: "Geometria VSEPR e interazioni di van der Waals.", hasContent: true },
      { slug: "la-quantita-di-sostanza-in-moli", title: "Cap 11: La quantità di sostanza in moli", objectives: "Il concetto di mole, costante di Avogadro e calcoli stechiometrici.", hasContent: true },
    ]
  },
  {
    year: 3,
    title: "3° Anno: Inorganica, stechiometria, energia, cinetica ed equilibrio",
    topics: [
      { slug: "classificazione-e-nomenclatura-dei-composti", title: "Cap 12: Classificazione e nomenclatura dei composti", objectives: "Nomenclatura IUPAC e tradizionale dei composti inorganici.", hasContent: true },
      { slug: "le-reazioni-chimiche-stechiometria-e-resa", title: "Cap 13: Le reazioni chimiche (stechiometria)", objectives: "Calcoli stechiometrici, reagente limitante e resa di reazione.", hasContent: true },
      { slug: "le-proprieta-delle-soluzioni", title: "Cap 14: Le proprietà delle soluzioni", objectives: "Solubilità e proprietà colligative delle soluzioni.", hasContent: true },
      { slug: "la-termodinamica", title: "Cap 15: La termodinamica", objectives: "Principi della termodinamica, entalpia, entropia e spontaneità.", hasContent: true },
      { slug: "la-cinetica-e-l-equilibrio", title: "Cap 16: La cinetica e l'equilibrio", objectives: "Velocità di reazione, equazione di Arrhenius, principio di Le Châtelier.", hasContent: true },
    ]
  },
  {
    year: 4,
    title: "4° Anno: Soluzioni, acidi, basi ed elettrochimica",
    topics: [
      { slug: "la-concentrazione-e-la-molarita", title: "Cap 17: La concentrazione e la Molarità", objectives: "Molarità, molalità, frazione molare e calcoli sulle soluzioni.", hasContent: true },
      { slug: "gli-acidi-e-le-basi", title: "Cap 18: Gli acidi e le basi", objectives: "Teorie di Arrhenius, Brønsted-Lowry e Lewis. Acidi forti e deboli.", hasContent: true },
      { slug: "il-ph-e-gli-indicatori", title: "Cap 19: Il pH e gli indicatori", objectives: "Calcolo del pH, pOH, soluzioni tampone e titolazioni.", hasContent: true },
      { slug: "le-ossido-riduzioni", title: "Cap 20: Le ossido-riduzioni", objectives: "Numeri di ossidazione e bilanciamento delle reazioni redox.", hasContent: true },
      { slug: "l-elettrochimica", title: "Cap 21: L'elettrochimica", objectives: "Celle galvaniche, pile, equazione di Nernst ed elettrolisi.", hasContent: true },
    ]
  },
  {
    year: 5,
    title: "5° Anno: Chimica organica, biochimica e materiali",
    topics: [
      { slug: "dal-carbonio-agli-idrocarburi", title: "Cap 22: Dal carbonio agli idrocarburi", objectives: "Fondamenti di chimica organica, alcani, alcheni, alchini e aromatici.", hasContent: true },
      { slug: "i-gruppi-funzionali", title: "Cap 23: I gruppi funzionali", objectives: "Alcoli, chetoni, aldeidi, acidi carbossilici ed esteri.", hasContent: true },
      { slug: "le-biomolecole", title: "Cap 24: Le biomolecole", objectives: "Carboidrati, lipidi, proteine e acidi nucleici. Fondamenti di biochimica.", hasContent: true },
      { slug: "polimeri-e-scienza-dei-materiali", title: "Cap 25: Polimeri e Scienza dei materiali", objectives: "Polimeri di sintesi, materiali compositi, ceramici e metallici.", hasContent: true },
    ]
  },
];

export function getTopicBySlug(anno: string, slug: string): { topic: Topic; year: YearCurriculum } | null {
  const y = parseInt(anno.replace("anno-", ""), 10);
  const yearObj = curriculum.find(c => c.year === y);
  if (!yearObj) return null;
  const topicObj = yearObj.topics.find(t => t.slug === slug);
  if (!topicObj) return null;
  return { topic: topicObj, year: yearObj };
}
