"use client";

import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import katex from "katex";
import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from "@/components/ui/accordion";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { RefreshCcw, CheckCircle, XCircle } from "lucide-react";

export function MathEq({ math, block = false }: { math: string, block?: boolean }) {
  const html = katex.renderToString(math, { displayMode: block, throwOnError: false });
  return <span dangerouslySetInnerHTML={{ __html: html }} />;
}

export function Flashcard({ q, a }: { q: string, a: string }) {
  const [flipped, setFlipped] = useState(false);
  return (
    <div 
      className="relative w-full h-48 cursor-pointer perspective-1000 group"
      onClick={() => setFlipped(!flipped)}
    >
      <motion.div
        className="w-full h-full relative preserve-3d"
        animate={{ rotateY: flipped ? 180 : 0 }}
        transition={{ type: "spring", stiffness: 200, damping: 20 }}
      >
        {/* Front */}
        <div className="absolute inset-0 w-full h-full backface-hidden bg-white dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 rounded-2xl p-6 flex flex-col justify-center items-center text-center shadow-sm hover:shadow-md transition-all duration-300">
          <span className="font-clash text-xs text-zinc-500 dark:text-zinc-400 font-semibold mb-2 uppercase tracking-widest">Domanda</span>
          <p className="font-medium text-lg leading-snug text-zinc-900 dark:text-zinc-50">{q}</p>
        </div>
        {/* Back */}
        <div className="absolute inset-0 w-full h-full backface-hidden bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-2xl p-6 flex flex-col justify-center items-center text-center rotate-y-180 shadow-md">
          <span className="font-clash text-xs text-zinc-500 dark:text-zinc-400 font-semibold mb-2 uppercase tracking-widest">Risposta</span>
          <p className="font-medium text-lg text-zinc-900 dark:text-zinc-50 leading-snug">{a}</p>
        </div>
      </motion.div>
    </div>
  );
}

export type QuizQuestion = {
  q: string;
  options: string[];
  correct: number;
};

export type Exercise = {
  title: string;
  text: React.ReactNode;
  steps: React.ReactNode[];
};

type LessonTemplateProps = {
  year: number;
  title: string;
  subtitle: string;
  theoryContent?: React.ReactNode;
  theoryPages?: { title: string; content: React.ReactNode }[];
  flashcards?: { q: string; a: string }[];
  exercises?: Exercise[];
  quiz?: QuizQuestion[];
};

export function LessonTemplate({ year, title, subtitle, theoryContent, theoryPages, flashcards, exercises, quiz }: LessonTemplateProps) {
  const [selectedOptions, setSelectedOptions] = useState<Record<number, number | null>>({});
  const [quizSubmitted, setQuizSubmitted] = useState<Record<number, boolean>>({});

  // Flashcard State
  const [fcIndex, setFcIndex] = useState(0);

  // Quiz Navigation State
  const [currentQuizIndex, setCurrentQuizIndex] = useState(0);

  const safeFlashcards = flashcards || [];
  const safeQuiz = quiz || [];
  const safeExercises = exercises || [];

  const handleNextFc = () => {
    if (fcIndex < safeFlashcards.length - 1) setFcIndex(fcIndex + 1);
  };
  const handlePrevFc = () => {
    if (fcIndex > 0) setFcIndex(fcIndex - 1);
  };
  const handleResetFc = () => {
    setFcIndex(0);
  };

  const handleNextQuiz = () => {
    if (currentQuizIndex < safeQuiz.length - 1) setCurrentQuizIndex(currentQuizIndex + 1);
  };
  const handleResetQuiz = () => {
    setCurrentQuizIndex(0);
    setQuizSubmitted({});
    setSelectedOptions({});
  };

  return (
    <div className="w-full max-w-4xl mx-auto flex flex-col space-y-12 pb-16">
      {/* Header */}
      <div className="space-y-4">
        <motion.div
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          className="inline-block px-3 py-1 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-200 text-sm font-medium border border-zinc-200 dark:border-zinc-700 mb-2"
        >
          {year}° Anno
        </motion.div>
        <h1 className="font-clash text-4xl md:text-5xl font-extrabold tracking-tight text-zinc-900 dark:text-zinc-50">
          {title}
        </h1>
        <p className="text-xl text-zinc-600 dark:text-zinc-400">
          {subtitle}
        </p>
      </div>

      {/* 1. Teoria Livello Zero */}
      <motion.section 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="space-y-6"
      >
        <h2 className="font-clash text-2xl font-bold flex items-center gap-2 text-zinc-900 dark:text-zinc-50">
          <span className="bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 w-8 h-8 rounded-full flex items-center justify-center text-sm">1</span>
          Teoria Accademica
        </h2>
        <Card className="bg-white dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 shadow-sm">
          <CardContent className="p-6 md:p-8 space-y-6">
            {theoryPages && theoryPages.length > 0 ? (
              <Tabs defaultValue="page-0" className="w-full flex flex-col">
                <TabsList className="mb-8 w-full flex flex-col sm:flex-row flex-wrap gap-2 h-auto p-1.5 bg-zinc-100 dark:bg-zinc-900 rounded-xl justify-start">
                  {theoryPages.map((page, i) => (
                    <TabsTrigger 
                      key={`trigger-${i}`} 
                      value={`page-${i}`} 
                      className="flex-1 text-base sm:text-lg font-medium px-4 py-3 rounded-lg data-[state=active]:bg-white data-[state=active]:text-zinc-900 data-[state=active]:shadow-sm dark:data-[state=active]:bg-zinc-800 dark:data-[state=active]:text-zinc-50 transition-all whitespace-nowrap"
                    >
                      {page.title}
                    </TabsTrigger>
                  ))}
                </TabsList>
                {theoryPages.map((page, i) => (
                  <TabsContent key={`content-${i}`} value={`page-${i}`} className="mt-4 focus-visible:outline-none animate-in fade-in-50 duration-500">
                    <div className="prose prose-zinc dark:prose-invert prose-lg max-w-none prose-headings:font-clash">
                      {page.content}
                    </div>
                  </TabsContent>
                ))}
              </Tabs>
            ) : (
              theoryContent
            )}
          </CardContent>
        </Card>
      </motion.section>

      {/* 2. Flashcard Interattive */}
      <motion.section 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="space-y-6"
      >
        <h2 className="font-clash text-2xl font-bold flex items-center gap-2 text-zinc-900 dark:text-zinc-50">
          <span className="bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 w-8 h-8 rounded-full flex items-center justify-center text-sm">2</span>
          Flashcard Interattive
        </h2>
        
        {safeFlashcards.length === 0 ? (
          <div className="p-6 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-2xl text-zinc-500 text-center">
            Flashcard in arrivo...
          </div>
        ) : (
          <div className="flex flex-col items-center max-w-2xl mx-auto w-full">
            <p className="text-zinc-600 dark:text-zinc-400 mb-6">Tocca la carta per girarla e ripassare i concetti chiave.</p>
            
            <AnimatePresence mode="wait">
              <motion.div 
                key={`fc-${fcIndex}`}
                initial={{ opacity: 0, x: 50 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -50 }}
                transition={{ duration: 0.3 }}
                className="w-full"
              >
                <Flashcard q={safeFlashcards[fcIndex].q} a={safeFlashcards[fcIndex].a} />
              </motion.div>
            </AnimatePresence>

            <div className="flex items-center justify-between w-full mt-8">
              <Button 
                variant="outline" 
                onClick={handlePrevFc} 
                disabled={fcIndex === 0}
                className="font-medium"
              >
                Precedente
              </Button>
              <span className="text-zinc-500 font-medium">
                {fcIndex + 1} / {safeFlashcards.length}
              </span>
              <Button 
                variant="outline" 
                onClick={handleNextFc} 
                disabled={fcIndex === safeFlashcards.length - 1}
                className="font-medium"
              >
                Avanti
              </Button>
            </div>

            <div className="mt-8">
              <Button 
                onClick={handleResetFc}
                variant="ghost"
                className="text-zinc-500 hover:text-zinc-900 dark:hover:text-zinc-100"
              >
                <RefreshCcw className="w-4 h-4 mr-2" />
                Ricomincia
              </Button>
            </div>
          </div>
        )}
      </motion.section>

      {/* 3. Esercizi Guidati */}
      <motion.section 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="space-y-6"
      >
        <h2 className="font-clash text-2xl font-bold flex items-center gap-2 text-zinc-900 dark:text-zinc-50">
          <span className="bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 w-8 h-8 rounded-full flex items-center justify-center text-sm">3</span>
          Esercizi Guidati
        </h2>
        
        {safeExercises.length === 0 ? (
          <div className="p-6 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-2xl text-zinc-500 text-center">
            Esercizi in arrivo...
          </div>
        ) : (
          <div className="w-full space-y-4">
            <Accordion type="single" collapsible className="w-full space-y-4">
              {safeExercises.map((ex, i) => (
                <AccordionItem key={i} value={`item-${i}`} className="border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900 rounded-xl px-4 overflow-hidden data-[state=open]:border-zinc-300 dark:data-[state=open]:border-zinc-700 transition-colors shadow-sm">
                  <AccordionTrigger className="font-clash text-lg font-medium py-4 hover:no-underline text-left text-zinc-900 dark:text-zinc-50">
                    {ex.title}
                  </AccordionTrigger>
                  <AccordionContent className="text-base text-zinc-700 dark:text-zinc-300 space-y-4 pb-6">
                    {ex.text}
                    <div className="bg-white dark:bg-zinc-950 p-4 rounded-lg border border-zinc-200 dark:border-zinc-800 font-mono text-sm space-y-2">
                      {ex.steps?.map((step, idx) => (
                        <div key={idx}>{step}</div>
                      ))}
                    </div>
                  </AccordionContent>
                </AccordionItem>
              ))}
            </Accordion>
          </div>
        )}
      </motion.section>

      {/* 4. Mini-Quiz */}
      <motion.section 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className="space-y-6"
      >
        <h2 className="font-clash text-2xl font-bold flex items-center gap-2 text-zinc-900 dark:text-zinc-50">
          <span className="bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 w-8 h-8 rounded-full flex items-center justify-center text-sm">4</span>
          Mini-Quiz
        </h2>
        {safeQuiz.length === 0 ? (
          <div className="p-6 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-2xl text-zinc-500 text-center">
            Quiz in arrivo...
          </div>
        ) : (
          <div className="space-y-6 max-w-3xl mx-auto w-full">
            <div className="flex items-center justify-between mb-4">
              <span className="text-sm font-semibold text-zinc-500 uppercase tracking-widest">Domanda {currentQuizIndex + 1} di {safeQuiz.length}</span>
              <Button variant="ghost" size="sm" onClick={handleResetQuiz} className="text-zinc-500 hover:text-zinc-900 dark:hover:text-zinc-100">
                <RefreshCcw className="w-4 h-4 mr-2" />
                Ricomincia Quiz
              </Button>
            </div>
            <AnimatePresence mode="wait">
              <motion.div
                key={`quiz-${currentQuizIndex}`}
                initial={{ opacity: 0, x: 50 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -50 }}
                transition={{ duration: 0.3 }}
              >
                <Card className="bg-white dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 overflow-hidden relative shadow-sm">
                  <CardContent className="p-6 md:p-8">
                    <h3 className="font-clash text-xl font-medium mb-6 text-zinc-900 dark:text-zinc-50">{safeQuiz[currentQuizIndex].q}</h3>
                    
                    <div className="grid grid-cols-1 gap-3 mb-6">
                      {safeQuiz[currentQuizIndex].options?.map((opt, i) => {
                        const isSelected = selectedOptions[currentQuizIndex] === i;
                        const isSubmitted = quizSubmitted[currentQuizIndex];
                        const isOptCorrect = i === safeQuiz[currentQuizIndex].correct;
                        
                        let btnStyle = "border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-zinc-900 dark:text-zinc-100";
                        
                        if (isSubmitted) {
                          if (isOptCorrect) btnStyle = "border-emerald-500 bg-emerald-50 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-400";
                          else if (isSelected && !isOptCorrect) btnStyle = "border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-400";
                          else btnStyle = "border-zinc-200 dark:border-zinc-800 bg-transparent opacity-50";
                        } else if (isSelected) {
                          btnStyle = "border-zinc-900 bg-zinc-100 text-zinc-900 dark:border-zinc-50 dark:bg-zinc-800 dark:text-zinc-50";
                        }

                        return (
                          <Button
                            key={i}
                            variant="outline"
                            className={`h-auto py-4 text-lg justify-start px-6 transition-all whitespace-normal text-left ${btnStyle}`}
                            onClick={() => {
                              if (!quizSubmitted[currentQuizIndex]) {
                                setSelectedOptions(prev => ({ ...prev, [currentQuizIndex]: i }));
                              }
                            }}
                            disabled={isSubmitted}
                          >
                            <span className="flex-1">{opt}</span>
                            {isSubmitted && isOptCorrect && <CheckCircle className="ml-3 shrink-0 w-5 h-5 text-emerald-500" />}
                            {isSubmitted && isSelected && !isOptCorrect && <XCircle className="ml-3 shrink-0 w-5 h-5 text-red-500" />}
                          </Button>
                        );
                      })}
                    </div>

                    <div className="flex items-center justify-between">
                      {!quizSubmitted[currentQuizIndex] ? (
                        <Button 
                          onClick={() => setQuizSubmitted(prev => ({ ...prev, [currentQuizIndex]: true }))}
                          disabled={selectedOptions[currentQuizIndex] === undefined || selectedOptions[currentQuizIndex] === null}
                          className="bg-indigo-600 hover:bg-indigo-700 text-white dark:bg-indigo-400 dark:text-zinc-900 dark:hover:bg-indigo-300 font-medium px-8 shadow-sm w-full md:w-auto"
                        >
                          Conferma Risposta
                        </Button>
                      ) : (
                        <div className="flex flex-col md:flex-row items-center justify-between w-full gap-4">
                          <span className={`font-semibold text-lg ${selectedOptions[currentQuizIndex] === safeQuiz[currentQuizIndex].correct ? "text-emerald-600 dark:text-emerald-400" : "text-red-600 dark:text-red-400"}`}>
                            {selectedOptions[currentQuizIndex] === safeQuiz[currentQuizIndex].correct ? "Esatto! Ottimo lavoro." : "Risposta errata."}
                          </span>
                          
                          <div className="flex gap-3 w-full md:w-auto">
                            {currentQuizIndex < safeQuiz.length - 1 ? (
                              <Button onClick={handleNextQuiz} className="bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 px-8 w-full md:w-auto">
                                Prossima Domanda
                              </Button>
                            ) : (
                              <Button onClick={handleResetQuiz} className="bg-indigo-600 text-white hover:bg-indigo-700 px-8 w-full md:w-auto">
                                <RefreshCcw className="w-4 h-4 mr-2" /> Hai finito! Ricomincia
                              </Button>
                            )}
                          </div>
                        </div>
                      )}
                    </div>
                  </CardContent>
                </Card>
              </motion.div>
            </AnimatePresence>
          </div>
        )}
      </motion.section>
    </div>
  );
}
