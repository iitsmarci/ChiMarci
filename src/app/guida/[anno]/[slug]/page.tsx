import { notFound } from "next/navigation";
import { getTopicBySlug } from "@/data/curriculum";
import { FallbackLesson } from "@/components/content/FallbackLesson";
import { LessonWrapper } from "@/components/content/LessonWrapper";

// Year 1
import { MisureGrandezzeLesson } from "@/components/content/year1/MisureGrandezzeLesson";
import { TrasformazioniFisicheLesson } from "@/components/content/year1/TrasformazioniFisicheLesson";
import { TeoriaAtomicaDaltonLesson } from "@/components/content/year1/TeoriaAtomicaDaltonLesson";
import { LeggiGasCineticaLesson } from "@/components/content/year1/LeggiGasCineticaLesson";
import { RappresentareReazioniLesson } from "@/components/content/year1/RappresentareReazioniLesson";

// Year 2
import { ParticelleAtomoLesson } from "@/components/content/year2/ParticelleAtomoLesson";
import { StrutturaAtomoLesson } from "@/components/content/year2/StrutturaAtomoLesson";
import { SistemaPeriodicoLesson } from "@/components/content/year2/SistemaPeriodicoLesson";
import { LegamiChimiciLesson } from "@/components/content/year2/LegamiChimiciLesson";
import { FormaMolecoleLesson } from "@/components/content/year2/FormaMolecoleLesson";
import { QuantitaSostanzaMoleLesson } from "@/components/content/year2/QuantitaSostanzaMoleLesson";

// Year 3
import { ClassificazioneCompostiLesson } from "@/components/content/year3/ClassificazioneCompostiLesson";
import { ReazioniStechiometriaLesson } from "@/components/content/year3/ReazioniStechiometriaLesson";
import { ProprietaSoluzioniLesson } from "@/components/content/year3/ProprietaSoluzioniLesson";
import { TermodinamicaLesson } from "@/components/content/year3/TermodinamicaLesson";
import { CineticaEquilibrioLesson } from "@/components/content/year3/CineticaEquilibrioLesson";

// Year 4
import { ConcentrazioneMolaritaLesson } from "@/components/content/year4/ConcentrazioneMolaritaLesson";
import { AcidiBasiLesson } from "@/components/content/year4/AcidiBasiLesson";
import { PhIndicatoriLesson } from "@/components/content/year4/PhIndicatoriLesson";
import { OssidoRiduzioniLesson } from "@/components/content/year4/OssidoRiduzioniLesson";
import { ElettrochimicaLesson } from "@/components/content/year4/ElettrochimicaLesson";

// Year 5
import { CarbonioIdrocarburiLesson } from "@/components/content/year5/CarbonioIdrocarburiLesson";
import { GruppiFunzionaliLesson } from "@/components/content/year5/GruppiFunzionaliLesson";
import { BiomolecoleLesson } from "@/components/content/year5/BiomolecoleLesson";
import { PolimeriMaterialiLesson } from "@/components/content/year5/PolimeriMaterialiLesson";



export default async function LessonPage({ params }: { params: Promise<{ anno: string; slug: string }> }) {
  const { anno, slug } = await params;
  const data = getTopicBySlug(anno, slug);

  if (!data || !data.topic || !data.year || !data.topic.hasContent) {
    const slugTitle = slug.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    const fallbackTopic = {
      title: slugTitle,
      objectives: "Lezione in stesura o dati mancanti",
      hasContent: false,
    } as any;
    const fallbackYear = {
      title: anno.toUpperCase(),
      topics: []
    } as any;
    return <FallbackLesson topic={fallbackTopic} year={fallbackYear} />;
  }

  const { topic, year } = data;
  let LessonContent = null;

  switch (slug) {
    // Year 1
    case "le-misure-e-le-grandezze":
      LessonContent = <MisureGrandezzeLesson />;
      break;
    case "le-trasformazioni-fisiche-della-materia":
      LessonContent = <TrasformazioniFisicheLesson />;
      break;
    case "dalle-trasformazioni-chimiche-alla-teoria-atomica":
      LessonContent = <TeoriaAtomicaDaltonLesson />;
      break;
    case "la-teoria-cinetico-molecolare-e-le-leggi-dei-gas":
      LessonContent = <LeggiGasCineticaLesson />;
      break;
    case "rappresentare-le-reazioni-chimiche":
      LessonContent = <RappresentareReazioniLesson />;
      break;

    // Year 2
    case "le-particelle-dell-atomo":
      LessonContent = <ParticelleAtomoLesson />;
      break;
    case "la-struttura-dell-atomo":
      LessonContent = <StrutturaAtomoLesson />;
      break;
    case "il-sistema-periodico":
      LessonContent = <SistemaPeriodicoLesson />;
      break;
    case "i-legami-chimici":
      LessonContent = <LegamiChimiciLesson />;
      break;
    case "la-forma-delle-molecole-e-le-forze-intermolecolari":
      LessonContent = <FormaMolecoleLesson />;
      break;
    case "la-quantita-di-sostanza-in-moli":
      LessonContent = <QuantitaSostanzaMoleLesson />;
      break;

    // Year 3
    case "classificazione-e-nomenclatura-dei-composti":
      LessonContent = <ClassificazioneCompostiLesson />;
      break;
    case "le-reazioni-chimiche-stechiometria-e-resa":
      LessonContent = <ReazioniStechiometriaLesson />;
      break;
    case "le-proprieta-delle-soluzioni":
      LessonContent = <ProprietaSoluzioniLesson />;
      break;
    case "la-termodinamica":
      LessonContent = <TermodinamicaLesson />;
      break;
    case "la-cinetica-e-l-equilibrio":
      LessonContent = <CineticaEquilibrioLesson />;
      break;

    // Year 4
    case "la-concentrazione-e-la-molarita":
      LessonContent = <ConcentrazioneMolaritaLesson />;
      break;
    case "gli-acidi-e-le-basi":
      LessonContent = <AcidiBasiLesson />;
      break;
    case "il-ph-e-gli-indicatori":
      LessonContent = <PhIndicatoriLesson />;
      break;
    case "le-ossido-riduzioni":
      LessonContent = <OssidoRiduzioniLesson />;
      break;
    case "l-elettrochimica":
      LessonContent = <ElettrochimicaLesson />;
      break;

    // Year 5
    case "dal-carbonio-agli-idrocarburi":
      LessonContent = <CarbonioIdrocarburiLesson />;
      break;
    case "i-gruppi-funzionali":
      LessonContent = <GruppiFunzionaliLesson />;
      break;
    case "le-biomolecole":
      LessonContent = <BiomolecoleLesson />;
      break;
    case "polimeri-e-scienza-dei-materiali":
      LessonContent = <PolimeriMaterialiLesson />;
      break;


  }

  if (LessonContent) {
    return (
      <LessonWrapper key={slug} title={topic.title} objectives={topic.objectives}>
        {LessonContent}
      </LessonWrapper>
    );
  }

  return <FallbackLesson key={slug} topic={topic} year={year} />;
}
