"use client";

import React from "react";
import { motion } from "framer-motion";
import { Lock, BookOpen, LayoutList, CheckSquare, Layers } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Topic, YearCurriculum } from "@/data/curriculum";

export function FallbackLesson({ topic, year }: { topic: Topic, year: YearCurriculum }) {
  const blocks = [
    { title: "Teoria Livello Zero", icon: BookOpen, desc: "Semplificazione estrema dei concetti chiave." },
    { title: "Flashcard Interattive", icon: Layers, desc: "Ripasso veloce con effetto flip 3D." },
    { title: "Esercizi Guidati", icon: LayoutList, desc: "Esercizi passo-passo sbloccati." },
    { title: "Mini-Quiz", icon: CheckSquare, desc: "Verifica finale dell'apprendimento." },
  ];

  return (
    <div className="w-full flex flex-col space-y-8 mt-4">
      <div className="text-center space-y-4 mb-8">
        <motion.div
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          className="inline-block px-3 py-1 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-200 text-sm font-medium border border-zinc-200 dark:border-zinc-700 mb-2"
        >
          {year.title}
        </motion.div>
        <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight text-zinc-900 dark:text-zinc-50">
          {topic.title}
        </h1>
        <p className="text-xl text-zinc-600 dark:text-zinc-400 max-w-2xl mx-auto">
          {topic.objectives}
        </p>
      </div>

      <div className="relative p-1 rounded-2xl bg-white dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 overflow-hidden group shadow-sm">
        <div className="absolute inset-0 bg-white/80 dark:bg-black/80 backdrop-blur-sm z-10 flex flex-col items-center justify-center">
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="p-4 rounded-full bg-zinc-100 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 shadow-sm mb-4"
          >
            <Lock className="w-8 h-8 text-zinc-500" />
          </motion.div>
          <h2 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50 mb-2">In Lavorazione</h2>
          <p className="text-zinc-600 dark:text-zinc-400 text-center max-w-sm px-4">
            Stiamo preparando i materiali didattici interattivi per questo capitolo seguendo le direttive ministeriali.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 p-6 opacity-30 select-none">
          {blocks.map((block, i) => {
            const Icon = block.icon;
            return (
              <Card key={i} className="bg-transparent border-zinc-200 dark:border-zinc-800">
                <CardContent className="p-6 flex flex-col items-center text-center space-y-4">
                  <Icon className="w-8 h-8 text-zinc-500" />
                  <h3 className="font-semibold text-lg text-zinc-900 dark:text-zinc-50">{block.title}</h3>
                  <p className="text-sm text-zinc-500">{block.desc}</p>
                </CardContent>
              </Card>
            );
          })}
        </div>
      </div>
    </div>
  );
}
