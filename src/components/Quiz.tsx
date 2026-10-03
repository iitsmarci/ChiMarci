"use client";

import { useState } from "react";
import { CheckCircle2, XCircle } from "lucide-react";

interface Option {
  id: string;
  text: string;
  isCorrect: boolean;
  explanation: string;
}

interface QuizProps {
  question: string;
  options: Option[];
}

export function Quiz({ question, options }: QuizProps) {
  const [selected, setSelected] = useState<string | null>(null);

  return (
    <div className="bg-white dark:bg-black border border-neutral-200 dark:border-neutral-800 rounded-xl p-6 shadow-sm my-8">
      <h3 className="text-lg font-bold mb-4">{question}</h3>
      <div className="space-y-3">
        {options.map((opt) => {
          const isSelected = selected === opt.id;
          const showCorrect = selected !== null && opt.isCorrect;
          const showWrong = isSelected && !opt.isCorrect;

          let btnClass = "border-neutral-200 dark:border-neutral-800 hover:bg-neutral-50 dark:hover:bg-neutral-900";
          if (showCorrect) btnClass = "border-green-500 bg-green-50 dark:bg-green-950/30 text-green-900 dark:text-green-100";
          else if (showWrong) btnClass = "border-red-500 bg-red-50 dark:bg-red-950/30 text-red-900 dark:text-red-100";

          return (
            <div key={opt.id} className="space-y-2">
              <button
                onClick={() => setSelected(opt.id)}
                disabled={selected !== null}
                className={`w-full text-left p-4 rounded-lg border-2 transition-all ${btnClass}`}
              >
                <div className="flex items-center justify-between">
                  <span>{opt.text}</span>
                  {showCorrect && <CheckCircle2 className="w-5 h-5 text-green-600" />}
                  {showWrong && <XCircle className="w-5 h-5 text-red-600" />}
                </div>
              </button>
              {(isSelected || showCorrect) && (
                <div className={`text-sm px-4 py-2 rounded-md ${showCorrect ? "text-green-800 dark:text-green-300 bg-green-100/50 dark:bg-green-900/20" : "text-red-800 dark:text-red-300 bg-red-100/50 dark:bg-red-900/20"}`}>
                  {opt.explanation}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
