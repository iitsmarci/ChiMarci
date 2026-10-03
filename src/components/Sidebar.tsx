"use client";

import Link from "next/link";
import { ThemeToggle } from "./ThemeToggle";
import { Book, LayoutDashboard, Settings } from "lucide-react";

export function Sidebar() {
  return (
    <aside className="w-64 border-r border-gray-200 dark:border-gray-800 bg-gray-50 dark:bg-gray-900 h-screen flex flex-col">
      <div className="p-6">
        <h1 className="text-2xl font-bold text-blue-600 dark:text-blue-400">ChiMarci</h1>
        <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">Apprendimento Chimica</p>
      </div>

      <nav className="flex-1 px-4 space-y-2">
        <Link href="/" className="flex items-center gap-3 px-3 py-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors">
          <LayoutDashboard className="w-5 h-5" />
          Dashboard
        </Link>
        {[1, 2, 3, 4, 5].map((year) => (
          <Link
            key={year}
            href={`/year/${year}`}
            className="flex items-center gap-3 px-3 py-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors"
          >
            <Book className="w-5 h-5" />
            Anno {year}
          </Link>
        ))}
      </nav>

      <div className="p-4 border-t border-gray-200 dark:border-gray-800 flex items-center justify-between">
        <Link href="/settings" className="flex items-center gap-3 px-3 py-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors flex-1">
          <Settings className="w-5 h-5" />
          Impostazioni
        </Link>
        <ThemeToggle />
      </div>
    </aside>
  );
}
