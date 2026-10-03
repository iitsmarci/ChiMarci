"use client";

import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";

interface FlashcardProps {
  front: React.ReactNode;
  back: React.ReactNode;
}

export function Flashcard({ front, back }: FlashcardProps) {
  const [isFlipped, setIsFlipped] = useState(false);

  return (
    <div 
      className="relative w-full h-48 cursor-pointer [perspective:1000px] mb-6"
      onClick={() => setIsFlipped(!isFlipped)}
    >
      <div 
        className={`w-full h-full transition-all duration-500 [transform-style:preserve-3d] ${isFlipped ? '[transform:rotateY(180deg)]' : ''}`}
      >
        {/* Front */}
        <Card className="absolute w-full h-full [backface-visibility:hidden] flex items-center justify-center p-6 text-center border-2 border-neutral-200 dark:border-neutral-800 shadow-sm hover:shadow-md transition-shadow bg-white dark:bg-black">
          <CardContent className="p-0 flex flex-col items-center justify-center h-full w-full">
            {front}
            <span className="text-[10px] uppercase tracking-widest text-neutral-400 absolute bottom-3">Tocca per girare</span>
          </CardContent>
        </Card>

        {/* Back */}
        <Card className="absolute w-full h-full [backface-visibility:hidden] [transform:rotateY(180deg)] flex items-center justify-center p-6 text-center border-2 border-blue-200 dark:border-blue-900 bg-blue-50/50 dark:bg-blue-950/20 shadow-sm">
          <CardContent className="p-0 flex flex-col items-center justify-center h-full w-full text-blue-900 dark:text-blue-100">
            {back}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
