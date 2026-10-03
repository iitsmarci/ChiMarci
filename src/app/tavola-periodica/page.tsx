"use client";

import React, { useState } from "react";
import { motion } from "framer-motion";
import { ArrowLeft, Atom, Zap, AlignLeft } from "lucide-react";
import Link from "next/link";
import { Sheet, SheetContent, SheetHeader, SheetTitle, SheetDescription } from "@/components/ui/sheet";

import { elements, type ElementData } from "@/data/periodicTable";

const getGroupStyle = (group: string) => {
  switch (group) {
    case "alkali": return "bg-rose-100 dark:bg-rose-500/20 text-rose-900 dark:text-rose-100 border-rose-200 dark:border-rose-900/50";
    case "alkaline-earth": return "bg-orange-100 dark:bg-orange-500/20 text-orange-900 dark:text-orange-100 border-orange-200 dark:border-orange-900/50";
    case "transition": return "bg-blue-100 dark:bg-blue-500/20 text-blue-900 dark:text-blue-100 border-blue-200 dark:border-blue-900/50";
    case "post-transition": return "bg-sky-100 dark:bg-sky-500/20 text-sky-900 dark:text-sky-100 border-sky-200 dark:border-sky-900/50";
    case "metalloid": return "bg-teal-100 dark:bg-teal-500/20 text-teal-900 dark:text-teal-100 border-teal-200 dark:border-teal-900/50";
    case "non-metal": return "bg-yellow-100 dark:bg-yellow-500/20 text-yellow-900 dark:text-yellow-100 border-yellow-200 dark:border-yellow-900/50";
    case "halogen": return "bg-emerald-100 dark:bg-emerald-500/20 text-emerald-900 dark:text-emerald-100 border-emerald-200 dark:border-emerald-900/50";
    case "noble": return "bg-purple-100 dark:bg-purple-500/20 text-purple-900 dark:text-purple-100 border-purple-200 dark:border-purple-900/50";
    case "lanthanide": return "bg-zinc-200 dark:bg-zinc-500/20 text-zinc-900 dark:text-zinc-100 border-zinc-300 dark:border-zinc-700";
    case "actinide": return "bg-zinc-200 dark:bg-zinc-500/20 text-zinc-900 dark:text-zinc-100 border-zinc-300 dark:border-zinc-700";
    default: return "bg-zinc-100 dark:bg-zinc-800 text-zinc-900 dark:text-zinc-100 border-zinc-200 dark:border-zinc-700";
  }
};

const getGroupName = (group: string) => {
  switch (group) {
    case "alkali": return "Metalli Alcalini";
    case "alkaline-earth": return "Metalli Alcalino-Terrosi";
    case "transition": return "Metalli di Transizione";
    case "post-transition": return "Metalli Post-Transizione";
    case "metalloid": return "Semimetalli";
    case "non-metal": return "Non Metalli";
    case "halogen": return "Alogeni";
    case "noble": return "Gas Nobili";
    case "lanthanide": return "Lantanidi";
    case "actinide": return "Attinidi";
    default: return "Sconosciuto";
  }
};

export default function TavolaPeriodicaPage() {
  const [selectedEl, setSelectedEl] = useState<ElementData | null>(null);

  return (
    <div className="w-full flex flex-col items-center">
      <div className="w-full mb-6 flex flex-col md:flex-row md:items-start justify-between gap-4">
        <div>
          <h1 className="text-3xl md:text-5xl font-extrabold tracking-tight text-zinc-900 dark:text-zinc-50 mb-2">
            Tavola Periodica
          </h1>
          <p className="text-zinc-600 dark:text-zinc-400">
            Categorie dei colori in stile Zanichelli. Clicca su un elemento per i dettagli.
          </p>
        </div>
        <Link href="/" className="inline-flex items-center text-sm font-medium text-indigo-600 dark:text-indigo-400 hover:underline shrink-0">
          <ArrowLeft className="w-4 h-4 mr-1" />
          Torna all'indice
        </Link>
      </div>

      {/* Legend */}
      <div className="w-full flex flex-wrap gap-2 mb-8 text-[11px] font-medium">
        <span className="px-2 py-1 bg-rose-100 dark:bg-rose-500/20 text-rose-900 dark:text-rose-100 border border-rose-200 dark:border-rose-900/50 rounded shadow-sm">Metalli Alcalini</span>
        <span className="px-2 py-1 bg-orange-100 dark:bg-orange-500/20 text-orange-900 dark:text-orange-100 border border-orange-200 dark:border-orange-900/50 rounded shadow-sm">Alcalino-Terrosi</span>
        <span className="px-2 py-1 bg-blue-100 dark:bg-blue-500/20 text-blue-900 dark:text-blue-100 border border-blue-200 dark:border-blue-900/50 rounded shadow-sm">Transizione</span>
        <span className="px-2 py-1 bg-teal-100 dark:bg-teal-500/20 text-teal-900 dark:text-teal-100 border border-teal-200 dark:border-teal-900/50 rounded shadow-sm">Semimetalli</span>
        <span className="px-2 py-1 bg-yellow-100 dark:bg-yellow-500/20 text-yellow-900 dark:text-yellow-100 border border-yellow-200 dark:border-yellow-900/50 rounded shadow-sm">Non Metalli</span>
        <span className="px-2 py-1 bg-emerald-100 dark:bg-emerald-500/20 text-emerald-900 dark:text-emerald-100 border border-emerald-200 dark:border-emerald-900/50 rounded shadow-sm">Alogeni</span>
        <span className="px-2 py-1 bg-purple-100 dark:bg-purple-500/20 text-purple-900 dark:text-purple-100 border border-purple-200 dark:border-purple-900/50 rounded shadow-sm">Gas Nobili</span>
        <span className="px-2 py-1 bg-zinc-200 dark:bg-zinc-500/20 text-zinc-900 dark:text-zinc-100 border border-zinc-300 dark:border-zinc-700/50 rounded shadow-sm">Lantanidi / Attinidi</span>
      </div>
      
      <div className="w-full overflow-x-auto pb-8">
        <div className="min-w-[1000px] grid grid-cols-[repeat(18,minmax(0,1fr))] gap-1 p-2">
          {elements.map((el) => (
            <motion.div
              key={el.n}
              style={{
                gridColumn: el.c,
                gridRow: el.r,
              }}
              whileHover={{ scale: 1.15, zIndex: 10 }}
              onClick={() => setSelectedEl(el)}
              className={`relative flex flex-col p-1.5 h-16 w-full border rounded-[4px] cursor-pointer shadow-sm transition-colors ${getGroupStyle(el.group)}`}
            >
              <div className="text-[9px] font-semibold opacity-70 leading-none">{el.n}</div>
              <div className="flex-1 flex items-center justify-center font-bold text-xl leading-none font-sans">
                {el.sym}
              </div>
              <div className="text-[8px] text-center opacity-70 leading-none truncate w-full">
                {el.mass}
              </div>
            </motion.div>
          ))}
        </div>
      </div>

      <Sheet open={!!selectedEl} onOpenChange={(open) => !open && setSelectedEl(null)}>
        <SheetContent side="right" className="w-[400px] sm:w-[540px] glass-panel border-l border-zinc-200 dark:border-zinc-800 overflow-y-auto">
          {selectedEl && (
            <>
              <SheetHeader className="mb-6 mt-4">
                <SheetTitle className="text-3xl font-extrabold flex items-center gap-3">
                  <div className={`w-14 h-14 rounded-lg flex items-center justify-center text-2xl border ${getGroupStyle(selectedEl.group)}`}>
                    {selectedEl.sym}
                  </div>
                  <div>
                    <div>{selectedEl.name}</div>
                    <div className="text-sm font-medium text-zinc-500 dark:text-zinc-400">
                      {getGroupName(selectedEl.group)}
                    </div>
                  </div>
                </SheetTitle>
              </SheetHeader>

              <div className="space-y-6">
                <div className="grid grid-cols-2 gap-4">
                  <div className="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
                    <div className="text-xs text-zinc-500 uppercase font-bold tracking-wider mb-1 flex items-center gap-1">
                      <Atom className="w-3 h-3" /> Numero Atomico (Z)
                    </div>
                    <div className="text-2xl font-semibold text-zinc-900 dark:text-zinc-50">
                      {selectedEl.n}
                    </div>
                  </div>
                  <div className="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
                    <div className="text-xs text-zinc-500 uppercase font-bold tracking-wider mb-1">
                      Massa Atomica
                    </div>
                    <div className="text-2xl font-semibold text-zinc-900 dark:text-zinc-50">
                      {selectedEl.mass}
                    </div>
                  </div>
                </div>

                <div className="space-y-3">
                  <div className="flex justify-between items-center p-3 border-b border-zinc-200 dark:border-zinc-800">
                    <span className="text-sm font-semibold text-zinc-600 dark:text-zinc-400">Numeri di Ossidazione</span>
                    <span className="font-mono text-zinc-900 dark:text-zinc-50">{selectedEl?.ox ?? "N/D"}</span>
                  </div>
                  <div className="flex justify-between items-center p-3 border-b border-zinc-200 dark:border-zinc-800">
                    <span className="text-sm font-semibold text-zinc-600 dark:text-zinc-400 flex items-center gap-2">
                      <Zap className="w-4 h-4 text-amber-500" /> Elettronegatività
                    </span>
                    <span className="font-mono text-zinc-900 dark:text-zinc-50">{selectedEl?.elneg ?? "N/D"}</span>
                  </div>
                  <div className="flex flex-col gap-2 p-3 border-b border-zinc-200 dark:border-zinc-800">
                    <span className="text-sm font-semibold text-zinc-600 dark:text-zinc-400 flex items-center gap-2">
                      <AlignLeft className="w-4 h-4 text-indigo-500" /> Configurazione Elettronica
                    </span>
                    <span className="font-mono bg-zinc-100 dark:bg-zinc-950 p-2 rounded text-zinc-900 dark:text-zinc-50 text-sm">
                      {selectedEl?.conf ?? "N/D"}
                    </span>
                  </div>
                </div>
              </div>
            </>
          )}
        </SheetContent>
      </Sheet>
    </div>
  );
}
