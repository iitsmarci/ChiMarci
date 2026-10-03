"use client";

import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { usePathname } from "next/navigation";
import { Play } from "lucide-react";
import { Button } from "@/components/ui/button";

interface LessonWrapperProps {
  title: string;
  objectives: string;
  children: React.ReactNode;
}

export function LessonWrapper({ title, objectives, children }: LessonWrapperProps) {
  const [isStarted, setIsStarted] = useState(false);
  const pathname = usePathname();

  useEffect(() => {
    if (typeof window !== "undefined") {
      localStorage.setItem("lastViewedLesson", JSON.stringify({ url: pathname, title }));
    }
  }, [pathname, title]);

  // Divide the objectives string into bullet points. We can assume it's a comma separated or just show it as a paragraph if not.
  // We'll split by common separators or just show it cleanly.
  const bulletPoints = objectives.split(/(?:;|\.)+/).map(s => s.trim()).filter(s => s.length > 5);

  if (!isStarted) {
    return (
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full flex flex-col items-center justify-center min-h-[60vh] text-center space-y-10"
      >
        <div className="space-y-6 max-w-2xl mx-auto">
          <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight text-zinc-900 dark:text-zinc-50 leading-tight">
            {title}
          </h1>
          
          <div className="bg-white dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 rounded-2xl p-8 shadow-sm text-left mt-8">
            <h3 className="text-lg font-semibold text-zinc-900 dark:text-zinc-50 mb-4 uppercase tracking-wider text-center">
              In questa lezione imparerai:
            </h3>
            <ul className="space-y-3">
              {bulletPoints.length > 0 ? (
                bulletPoints.map((bp, i) => (
                  <li key={i} className="flex items-start gap-3">
                    <span className="mt-1.5 w-1.5 h-1.5 rounded-full bg-zinc-900 dark:bg-zinc-50 shrink-0" />
                    <span className="text-zinc-700 dark:text-zinc-300 text-lg">{bp}</span>
                  </li>
                ))
              ) : (
                <li className="flex items-start gap-3">
                  <span className="mt-1.5 w-1.5 h-1.5 rounded-full bg-zinc-900 dark:bg-zinc-50 shrink-0" />
                  <span className="text-zinc-700 dark:text-zinc-300 text-lg">{objectives}</span>
                </li>
              )}
            </ul>
          </div>
        </div>

        <Button 
          onClick={() => setIsStarted(true)}
          className="group relative inline-flex items-center justify-center px-10 py-8 text-xl font-semibold text-white dark:text-zinc-900 bg-indigo-600 dark:bg-indigo-400 hover:bg-indigo-700 dark:hover:bg-indigo-300 rounded-full overflow-hidden transition-all hover:scale-105 active:scale-95 shadow-sm"
        >
          <span className="relative flex items-center gap-3">
            INIZIA LEZIONE <Play className="w-6 h-6 group-hover:translate-x-1 transition-transform fill-current" />
          </span>
        </Button>
      </motion.div>
    );
  }

  return (
    <motion.div
      key="lesson-content"
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
    >
      {children}
    </motion.div>
  );
}
