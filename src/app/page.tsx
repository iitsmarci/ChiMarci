"use client";

import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import Link from "next/link";
import { ArrowRight, BookOpen, Layers, Zap } from "lucide-react";

export default function Home() {
  const [lastViewed, setLastViewed] = useState<{ url: string; title: string } | null>(null);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    if (typeof window !== "undefined") {
      const saved = localStorage.getItem("lastViewedLesson");
      if (saved) {
        try {
          setLastViewed(JSON.parse(saved));
        } catch (e) {}
      }
    }
  }, []);
  return (
    <div className="w-full flex flex-col items-center justify-center min-h-[80vh] text-center space-y-16">
      
      {/* Morbido blob di sfondo */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-indigo-500/10 blur-3xl rounded-full pointer-events-none -z-10" />

      {/* Hero Section */}
      <motion.div 
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: "easeOut" }}
        className="space-y-6 max-w-3xl"
      >
        <div className="inline-block px-3 py-1 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-200 text-sm font-medium border border-zinc-200 dark:border-zinc-700 mb-4">
          Liceo Scientifico MIM
        </div>
        <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight leading-tight text-zinc-900 dark:text-zinc-50 pb-2 font-melodrama">
          La Chimica, Finalmente<br/>Spiegata Bene.
        </h1>
        <p className="text-xl md:text-2xl text-zinc-600 dark:text-zinc-400 leading-relaxed">
          Dalla struttura dell'atomo alla biochimica del quinto anno. Appunti chiari come l'acqua, pratica infinita e zero paroloni incomprensibili. Il tuo 10 in pagella parte da qui.
        </p>
        
        <div className="pt-8">
          <Link href={mounted && lastViewed ? lastViewed.url : "/guida/anno-4/molarita-e-ph"}>
            <button className="font-clash group relative inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-white bg-indigo-600 hover:bg-indigo-700 rounded-full overflow-hidden transition-transform hover:scale-105 active:scale-95 shadow-sm">
              <span className="relative flex items-center gap-2">
                {mounted && lastViewed ? `Continua: ${lastViewed.title}` : "Inizia la Magia"} <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </span>
            </button>
          </Link>
        </div>
      </motion.div>

      {/* Features Section */}
      <motion.div 
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.2, ease: "easeOut" }}
        className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full"
      >
        <div className="p-6 rounded-2xl glass-panel group hover:shadow-md transition-all">
          <BookOpen className="w-10 h-10 text-zinc-900 dark:text-zinc-50 mb-4 group-hover:scale-110 transition-transform" />
          <h3 className="font-clash text-xl font-bold mb-2 text-zinc-900 dark:text-zinc-50">Teoria Dritta al Punto</h3>
          <p className="text-zinc-600 dark:text-zinc-400">Spiegazioni senza giri di parole, visive ed estremamente efficaci. Smettila di perderti in muri di testo che non portano a nulla.</p>
        </div>
        
        <div className="p-6 rounded-2xl glass-panel group hover:shadow-md transition-all">
          <Layers className="w-10 h-10 text-zinc-900 dark:text-zinc-50 mb-4 group-hover:scale-110 transition-transform" />
          <h3 className="font-clash text-xl font-bold mb-2 text-zinc-900 dark:text-zinc-50">Pratica Senza Limiti</h3>
          <p className="text-zinc-600 dark:text-zinc-400">Mettiti alla prova! Flashcard 3D, quiz animati ed esercizi guidati per trasformare ogni concetto astratto in competenza reale.</p>
        </div>
        
        <div className="p-6 rounded-2xl glass-panel group hover:shadow-md transition-all">
          <Zap className="w-10 h-10 text-zinc-900 dark:text-zinc-50 mb-4 group-hover:scale-110 transition-transform" />
          <h3 className="font-clash text-xl font-bold mb-2 text-zinc-900 dark:text-zinc-50">A Prova di Interrogazione</h3>
          <p className="text-zinc-600 dark:text-zinc-400">Tutti gli argomenti ministeriali perfettamente allineati. Un percorso di studio che ti accompagna senza intoppi fino al bel voto.</p>
        </div>
      </motion.div>
    </div>
  );
}
