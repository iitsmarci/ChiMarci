"use client";

import React, { useEffect, useState } from "react";
import { motion, useScroll, useSpring } from "framer-motion";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Menu, X, BookOpen, ChevronRight, Moon, Sun, FlaskConical, Atom, Zap, Dna, Grid, Home, ArrowRight } from "lucide-react";
import { curriculum } from "@/data/curriculum";
import { useTheme } from "next-themes";
import { Sheet, SheetContent, SheetTrigger, SheetTitle } from "@/components/ui/sheet";
import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from "@/components/ui/accordion";

export function ClientLayout({ children }: { children: React.ReactNode }) {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 100, damping: 30, restDelta: 0.001 });
  const [mounted, setMounted] = useState(false);
  const { theme, setTheme } = useTheme();
  const pathname = usePathname();

  const [lastViewed, setLastViewed] = useState<{ url: string; title: string } | null>(null);

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
  }, [pathname]);

  return (
    <div className="min-h-screen flex flex-col w-full bg-background dark:bg-black font-sans selection:bg-zinc-200 dark:selection:bg-zinc-800">
      {/* Reading Progress Bar */}
      <motion.div
        className="fixed top-0 left-0 right-0 h-[2px] bg-indigo-600 dark:bg-indigo-400 origin-left z-50"
        style={{ scaleX }}
      />

      {/* Top Navbar */}
      <header className="sticky top-0 z-40 w-full glass-panel border-b border-border/50">
        <div className="flex h-16 items-center px-4 md:px-6 w-full max-w-7xl mx-auto justify-between">
          <div className="flex items-center gap-2">
            <Sheet>
              <SheetTrigger asChild>
                <button className="mr-2 p-2 rounded-md hover:bg-zinc-100 dark:hover:bg-zinc-900 transition-colors md:hidden">
                  <Menu className="w-5 h-5 text-zinc-900 dark:text-zinc-50" />
                  <span className="sr-only">Menu</span>
                </button>
              </SheetTrigger>
              <SheetContent side="left" className="w-[300px] sm:w-[350px] glass-panel border-r border-zinc-200 dark:border-zinc-800 p-0">
                <SheetTitle className="sr-only">Navigation Menu</SheetTitle>
                <SidebarContent pathname={pathname} isMobile />
              </SheetContent>
            </Sheet>
            <Link href="/" className="flex items-center gap-2 group hover:opacity-80 transition-opacity">
              <div className="bg-indigo-100 dark:bg-indigo-900/30 p-2 rounded-lg group-hover:scale-105 transition-transform">
                <Home className="w-5 h-5 text-indigo-600 dark:text-indigo-400" />
              </div>
              <span className="font-clash font-bold text-lg hidden sm:inline-block text-zinc-900 dark:text-zinc-50">Guida di Chimica</span>
            </Link>
          </div>

          <div className="flex items-center gap-4">
            {mounted && lastViewed && pathname !== lastViewed.url && pathname !== "/" && (
              <Link href={lastViewed.url} className="hidden md:flex items-center text-sm font-medium text-zinc-500 hover:text-indigo-600 dark:text-zinc-400 dark:hover:text-indigo-400 transition-colors">
                Continua dove hai lasciato <ArrowRight className="w-4 h-4 ml-1" />
              </Link>
            )}
            <Link href="/tavola-periodica" className="p-2 rounded-full hover:bg-zinc-100 dark:hover:bg-zinc-900 transition-colors" title="Tavola Periodica">
              <Grid className="w-5 h-5 text-zinc-900 dark:text-zinc-50" />
            </Link>
            {mounted && (
              <button
                onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
                className="p-2 rounded-full hover:bg-zinc-100 dark:hover:bg-zinc-900 transition-colors"
              >
                {theme === "dark" ? <Sun className="w-5 h-5 text-zinc-50" /> : <Moon className="w-5 h-5 text-zinc-900" />}
              </button>
            )}
          </div>
        </div>
      </header>

      <div className="flex flex-1 w-full max-w-7xl mx-auto">
        {/* Desktop Sidebar */}
        <aside className="hidden md:block w-72 shrink-0 border-r border-border/50 glass-panel h-[calc(100vh-4rem)] sticky top-16 overflow-y-auto">
          <SidebarContent pathname={pathname} />
        </aside>

        {/* Main Content */}
        <main className="flex-1 w-full overflow-hidden relative">
          <div className="px-4 py-8 md:px-8 max-w-4xl mx-auto w-full pb-32">
              <motion.div
                key={pathname}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3, ease: "easeOut" }}
              >
                {children}
              </motion.div>
          </div>
        </main>
      </div>
    </div>
  );
}

const getYearIcon = (year: number) => {
  switch (year) {
    case 1: return <FlaskConical className="w-4 h-4 mr-2 text-zinc-500" />;
    case 2: return <Atom className="w-4 h-4 mr-2 text-zinc-500" />;
    case 3: return <BookOpen className="w-4 h-4 mr-2 text-zinc-500" />;
    case 4: return <Zap className="w-4 h-4 mr-2 text-zinc-500" />;
    case 5: return <Dna className="w-4 h-4 mr-2 text-zinc-500" />;
    default: return <BookOpen className="w-4 h-4 mr-2 text-zinc-500" />;
  }
};

function SidebarContent({ pathname, isMobile = false }: { pathname: string, isMobile?: boolean }) {
  return (
    <div className="py-6 px-4">
      <div className="mb-8 px-2">
        <h2 className="font-clash text-xs font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase">Indice Argomenti</h2>
      </div>
      <Accordion type="multiple" className="w-full space-y-1" defaultValue={curriculum.map(c => `anno-${c.year}`)}>
        {curriculum.map((year) => (
          <AccordionItem value={`anno-${year.year}`} key={year.year} className="border-none">
            <AccordionTrigger className="hover:no-underline py-2.5 px-3 rounded-lg hover:bg-zinc-100 dark:hover:bg-zinc-900 transition-colors text-zinc-900 dark:text-zinc-50">
              <div className="flex items-center font-semibold text-sm">
                {getYearIcon(year.year)}
                {year.title}
              </div>
            </AccordionTrigger>
            <AccordionContent className="pb-4 pt-1">
              <div className="flex flex-col space-y-1 mt-1 pl-4">
                {year.topics.map((topic) => {
                  const href = `/guida/anno-${year.year}/${topic.slug}`;
                  const isActive = pathname === href;
                  return (
                    <Link
                      key={topic.slug}
                      href={href}
                      className={`relative px-3 py-2 text-sm rounded-md transition-all flex items-center gap-2 group border-l-2 ${
                        isActive 
                          ? "bg-indigo-50 dark:bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 font-bold border-indigo-600 dark:border-indigo-400" 
                          : "text-zinc-600 dark:text-zinc-400 border-transparent hover:text-zinc-900 dark:hover:text-zinc-50 hover:bg-zinc-50 dark:hover:bg-zinc-900/50 hover:border-zinc-300 dark:hover:border-zinc-700"
                      }`}
                    >
                      <span className="truncate">{topic.title}</span>
                      {topic.hasContent && !isActive && (
                        <span className="w-1.5 h-1.5 rounded-full bg-zinc-300 dark:bg-zinc-700 ml-auto flex-shrink-0" />
                      )}
                    </Link>
                  );
                })}
              </div>
            </AccordionContent>
          </AccordionItem>
        ))}
      </Accordion>
    </div>
  );
}
