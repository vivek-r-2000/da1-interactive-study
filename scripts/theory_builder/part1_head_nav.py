# -*- coding: utf-8 -*-

part1_html = r"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Endsem 2026: Master Theory Blueprint | CS4.405 Data Analytics I | IIIT Hyderabad</title>
<script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css"/>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}]});"></script>
<style>
  :root {
    --bg-main: #090d16;
    --bg-card: #0f1420;
    --bg-elevated: #172033;
    --text-main: #f1f5f9;
    --text-muted: #94a3b8;
    --border: rgba(255, 255, 255, 0.08);
    --border-strong: rgba(255, 255, 255, 0.16);
    --brand-primary: #6366f1;
    --brand-secondary: #0ea5e9;
    --brand-emerald: #10b981;
    --brand-amber: #f59e0b;
    --brand-rose: #f43f5e;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: var(--bg-main);
    color: var(--text-main);
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    line-height: 1.6;
    font-feature-settings: "cv02", "cv03", "cv04", "cv11";
  }

  /* Custom Scrollbar */
  ::-webkit-scrollbar { width: 6px; height: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg-main); }
  ::-webkit-scrollbar-thumb { background: #334155; border-radius: 3px; }

  /* Surface Cards */
  .surface-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
  }
  .surface-elevated {
    background: var(--bg-elevated);
    border: 1px solid var(--border-strong);
    border-radius: 12px;
  }

  /* Low-Attention Chunking Boxes */
  .tldr-box {
    background: rgba(99, 102, 241, 0.08);
    border-left: 3px solid #6366f1;
    padding: 0.75rem 1rem;
    border-radius: 0 8px 8px 0;
    margin: 0.75rem 0;
  }
  .analogy-box {
    background: rgba(14, 165, 233, 0.08);
    border-left: 3px solid #0ea5e9;
    padding: 0.75rem 1rem;
    border-radius: 0 8px 8px 0;
    margin: 0.75rem 0;
  }
  .formula-box {
    background: #060911;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 8px;
    padding: 1rem;
    margin: 0.75rem 0;
  }
  .trap-box {
    background: rgba(244, 63, 94, 0.08);
    border-left: 3px solid #f43f5e;
    padding: 0.75rem 1rem;
    border-radius: 0 8px 8px 0;
    margin: 0.75rem 0;
  }
  .example-box {
    background: rgba(16, 185, 129, 0.06);
    border: 1px solid rgba(16, 185, 129, 0.2);
    padding: 1rem;
    border-radius: 8px;
    margin: 0.75rem 0;
  }

  /* Sticky Navigation */
  .sticky-nav-item.active {
    background: rgba(99, 102, 241, 0.15);
    color: #818cf8;
    border-left: 2px solid #6366f1;
    font-weight: 600;
  }

  /* Collapsible Toggle */
  details summary {
    cursor: pointer;
    user-select: none;
    list-style: none;
  }
  details summary::-webkit-details-marker { display: none; }
  details[open] summary .toggle-icon { transform: rotate(90deg); }

  /* Print Styles */
  @media print {
    #sidebar-left, #top-controls { display: none !important; }
    body { background: #fff !important; color: #000 !important; }
    .surface-card, .surface-elevated, .formula-box {
      border: 1px solid #ccc !important;
      background: #fff !important;
      color: #000 !important;
      box-shadow: none !important;
      page-break-inside: avoid;
    }
    #main-content { margin-left: 0 !important; width: 100% !important; }
  }
</style>
</head>
<body class="min-h-screen text-slate-100 antialiased">

  <!-- TOP PROGRESS BAR -->
  <div id="read-progress-bar" class="fixed top-0 left-0 h-1 bg-indigo-500 z-50 transition-all" style="width: 0%;"></div>

  <!-- TOP CONTROLS & HEADER -->
  <header id="top-controls" class="sticky top-0 z-40 bg-[#090d16]/95 backdrop-blur border-b border-white/10 px-4 py-3">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3">
      <div class="flex items-center gap-3">
        <a href="../index.html" class="px-2.5 py-1 text-xs font-semibold rounded bg-slate-800 text-slate-300 hover:text-white border border-white/10 transition-colors">
          &larr; Home
        </a>
        <a href="../Exam_Preparation/index.html" class="px-2.5 py-1 text-xs font-semibold rounded bg-indigo-950 text-indigo-300 hover:text-white border border-indigo-800 transition-colors">
          Exam Prep Portal &rarr;
        </a>
        <span class="text-xs text-slate-400 font-mono hidden sm:inline">CS4.405 Data Analytics I</span>
      </div>

      <!-- Live Search Box -->
      <div class="relative flex-1 max-w-md">
        <span class="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-xs">&#128269;</span>
        <input 
          type="text" 
          id="theory-search-input" 
          placeholder="Search theory (e.g. BUC, LOF, Backprop, Laplace, BIRCH, SVM)..." 
          class="w-full bg-[#131b2e] border border-white/10 rounded-lg pl-8 pr-3 py-1.5 text-xs text-white placeholder-slate-400 focus:outline-none focus:border-indigo-500 transition-colors"
          oninput="filterTheoryTopics()"
        />
      </div>

      <div class="flex items-center gap-2">
        <button onclick="window.print()" class="px-2.5 py-1 text-xs font-semibold rounded bg-slate-800 text-slate-300 hover:text-white border border-white/10 transition-colors">
          &#128424; Print / PDF
        </button>
      </div>
    </div>
  </header>

  <!-- MAIN WRAPPER: SIDEBAR + CONTENT -->
  <div class="max-w-7xl mx-auto px-4 py-6 flex flex-col lg:flex-row gap-8">

    <!-- LEFT STICKY NAVIGATION -->
    <aside id="sidebar-left" class="lg:w-72 shrink-0 hidden lg:block">
      <div class="sticky top-20 surface-card p-4 space-y-3 max-h-[calc(100vh-6rem)] overflow-y-auto text-xs">
        <div class="pb-2 border-b border-white/10 flex items-center justify-between">
          <span class="font-bold text-white uppercase tracking-wider text-[11px]">Blueprint Topics</span>
          <span class="px-1.5 py-0.5 rounded bg-indigo-500/20 text-indigo-300 font-mono text-[10px]">12 Sections</span>
        </div>

        <nav class="space-y-1 font-medium">
          <a href="#topic-1" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>1. Intro & DIKW Pipeline</span>
            <span class="text-[10px] text-slate-500 font-mono">~8m</span>
          </a>
          <a href="#topic-2" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>2. Preprocessing & Stats</span>
            <span class="text-[10px] text-slate-500 font-mono">~18m</span>
          </a>
          <a href="#topic-3" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>3. Warehousing, OLAP & BUC</span>
            <span class="text-[10px] text-slate-500 font-mono">~15m</span>
          </a>
          <a href="#topic-4" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>4. Pattern Mining Basic</span>
            <span class="text-[10px] text-slate-500 font-mono">~15m</span>
          </a>
          <a href="#topic-5" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>5. Adv. Patterns & 3 Papers</span>
            <span class="text-[10px] text-slate-500 font-mono">~15m</span>
          </a>
          <a href="#topic-6" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>6. Classification Basic</span>
            <span class="text-[10px] text-slate-500 font-mono">~20m</span>
          </a>
          <a href="#topic-7" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>7. Classification Advanced</span>
            <span class="text-[10px] text-slate-500 font-mono">~20m</span>
          </a>
          <a href="#topic-8" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>8. Clustering & 4 Papers</span>
            <span class="text-[10px] text-slate-500 font-mono">~22m</span>
          </a>
          <a href="#topic-9" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>9. Deep Learning (Han §10.1)</span>
            <span class="text-[10px] text-slate-500 font-mono">~18m</span>
          </a>
          <a href="#topic-10" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>10. Outliers & Trends (PPTs)</span>
            <span class="text-[10px] text-slate-500 font-mono">~18m</span>
          </a>
          <a href="#topic-11" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>11. Scientific Calculator Guide</span>
            <span class="text-[10px] text-slate-500 font-mono">~6m</span>
          </a>
          <a href="#topic-12" class="sticky-nav-item block px-2.5 py-1.5 rounded text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors flex items-center justify-between">
            <span>12. Cross-Chapter Synthesis</span>
            <span class="text-[10px] text-slate-500 font-mono">~12m</span>
          </a>
        </nav>
      </div>
    </aside>

    <!-- MAIN CONTENT COLUMN -->
    <main id="main-content" class="flex-1 space-y-12 min-w-0">

      <!-- HERO BANNER -->
      <section class="surface-card p-6 md:p-8 space-y-4 border-l-4 border-l-indigo-500">
        <div class="flex flex-wrap items-center gap-2">
          <span class="px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 font-mono text-xs border border-indigo-500/30 font-semibold">Confirmed Blueprint</span>
          <span class="px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 font-mono text-xs border border-emerald-500/30 font-semibold">Scientific Calculators Allowed</span>
          <span class="px-2.5 py-0.5 rounded-full bg-purple-500/20 text-purple-300 font-mono text-xs border border-purple-500/30 font-semibold">All 10 Topics &bull; 7 Papers &bull; 14 Exercises</span>
        </div>
        <h1 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
          Endsem 2026: Master Theory Blueprint
        </h1>
        <p class="text-sm text-slate-300 leading-relaxed max-w-3xl">
          Everything you need for the CS4.405 Endsem examination in <strong>one single, unified place</strong>. Explained in simple, accessible language for rapid understanding: <em>Intuition &rarr; Mechanism &rarr; KaTeX Math &rarr; Solved Numerical &rarr; Exam Traps</em>.
        </p>
      </section>
"""
