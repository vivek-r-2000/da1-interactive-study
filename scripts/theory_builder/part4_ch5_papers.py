# -*- coding: utf-8 -*-

part4_html = r"""
      <!-- ==========================================
           TOPIC 5: CHAPTER 5 ADVANCED PATTERNS & 3 PAPERS
      ========================================== -->
      <section id="topic-5" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-semibold">Topic 5 &bull; Han Chapter 5 + 3 Research Papers</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Chapter 5: Advanced Pattern Mining & 3 Mandated Papers</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~15 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 TL;DR:</strong>
          Real-world data has hierarchies (Milk &rarr; Low-fat Milk), numeric measurements (Age: 20-30), and economic profit (a laptop yields more profit than 100 apples). Prof. Reddy's Endsem blueprint explicitly mandates 3 seminal research papers covering these exact domains!
        </div>

        <!-- 5.1 Overview -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">5.1 The 3 Frontiers of Advanced Pattern Mining</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            Standard Apriori assumes flat, binary transactions with identical unit values. The 3 mandated research papers each solve a fundamental limitation:
          </p>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <span class="text-[10px] font-mono text-indigo-400 font-bold block mb-1">PAPER 1: TAXONOMIES</span>
              <strong class="text-white block mb-1">Multi-Level Rules (Han & Fu 1999)</strong>
              <p class="text-slate-400">Items belong to concept hierarchies. How do we mine rules across abstract and granular levels without getting drowned in redundant rules?</p>
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <span class="text-[10px] font-mono text-sky-400 font-bold block mb-1">PAPER 2: NUMERIC RANGES</span>
              <strong class="text-white block mb-1">Quantitative Rules (Srikant 1996)</strong>
              <p class="text-slate-400">Relational attributes are continuous numbers (e.g. Age, Income). How do we bin and combine intervals without losing information?</p>
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <span class="text-[10px] font-mono text-emerald-400 font-bold block mb-1">PAPER 3: ECONOMIC PROFIT</span>
              <strong class="text-white block mb-1">High Utility (Liu et al. 2005)</strong>
              <p class="text-slate-400">Frequency &ne; Profit. How do we discover itemsets yielding high dollar margins using the two-phase TWU framework?</p>
            </div>
          </div>
        </div>

        <!-- 5.2 Paper 1: Multi-Level Association Rules -->
        <div class="surface-card p-5 space-y-3">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-indigo-300">Paper 1: Mining Multiple-Level Association Rules in Large Databases (Han & Fu 1999)</h3>
            <span class="text-xs font-mono px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300">Mandated Paper</span>
          </div>

          <div class="analogy-box text-xs">
            <strong class="text-sky-300 block mb-0.5">💡 Real-World Analogy:</strong>
            At a supermarket, 80% of shoppers buy "Dairy Products" (Level 1), 30% buy "Milk" (Level 2), and only 1.5% buy "Dairyland 1% Low-fat Organic Milk" (Level 3). If you set a single high support threshold (10%), you miss the low-fat milk rule completely. If you set it to 1%, you generate 50,000 trivial rules at the top level!
          </div>

          <div class="space-y-2 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-indigo-400 block mb-1">1. Uniform Support vs. Reduced Support:</strong>
              <p class="text-slate-300">&bull; <strong>Uniform Support:</strong> Same $\text{min\_sup}$ across all hierarchy levels. <em>Fatal flaw:</em> Low-level items have naturally lower frequencies and are pruned away.</p>
              <p class="text-slate-300">&bull; <strong>Reduced Support (Preferred):</strong> Progressive lower $\text{min\_sup}$ as depth increases (e.g., Level 1: 5%, Level 2: 2%, Level 3: 0.5%).</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-sky-400 block mb-1">2. Redundant Rule Filtering Principle:</strong>
              <p class="text-slate-300">
                A rule $r': A' \implies B'$ at level $l$ is a specialization of rule $r: A \implies B$ at level $l-1$. Rule $r'$ is deemed <strong>redundant</strong> if its confidence and support do not significantly deviate from expectations derived from $r$:
              </p>
              $$\text{Confidence}(r') \approx \text{Confidence}(r) \quad \text{and} \quad \text{Support}(r') \approx \text{Support}(r) \times P(A'|A)$$
              <p class="text-slate-400 mt-1">If "Milk &rarr; Bread" has 70% confidence, and "Lowfat Milk &rarr; Bread" also has 70% confidence, the low-fat rule provides zero new insight and is pruned!</p>
            </div>
          </div>
        </div>

        <!-- 5.3 Paper 2: Quantitative Association Rules -->
        <div class="surface-card p-5 space-y-3">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-sky-300">Paper 2: Mining Quantitative Association Rules in Large Relational Tables (Srikant & Agrawal 1996)</h3>
            <span class="text-xs font-mono px-2 py-0.5 rounded bg-sky-500/20 text-sky-300">Mandated Paper</span>
          </div>

          <p class="text-xs text-slate-300 leading-relaxed">
            Maps relational tuples containing categorical and continuous numeric fields into rules like: $\text{Age: } [30\dots 39] \land \text{Married: Yes} \implies \text{NumCars: } 2$ [Support 10%, Confidence 85%].
          </p>

          <div class="space-y-2 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-indigo-400 block mb-1">1. Equi-Depth Binning & Partial Completeness:</strong>
              <p class="text-slate-300">Partition numeric attributes into bins containing an equal number of tuples (equi-depth) rather than equal value ranges (equi-width). Prevents skew where dense regions are lumped together.</p>
              <p class="text-slate-300 mt-1"><strong>Partial Completeness:</strong> Guarantees that any rule with support $s$ and confidence $c$ will be discovered with support within a bounded distance $K$ of optimal intervals.</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-emerald-400 block mb-1">2. Minimum Win-Slack Heuristic:</strong>
              <p class="text-slate-300">Adjacent intervals are combined only if the combined interval provides substantially more support without dropping below minimum confidence. Prunes redundant sub-interval variants.</p>
            </div>
          </div>
        </div>

        <!-- 5.4 Paper 3: High Utility Itemsets -->
        <div class="surface-card p-5 space-y-3">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-emerald-300">Paper 3: A Two-Phase Algorithm for Fast Discovery of High Utility Itemsets (Liu, Liao & Choudhary 2005)</h3>
            <span class="text-xs font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300">Mandated Paper</span>
          </div>

          <div class="analogy-box text-xs">
            <strong class="text-sky-300 block mb-0.5">💡 Real-World Analogy:</strong>
            Selling 100 bubblegums at 10 cents profit generates \$10. Selling 2 Rolex watches at \$5,000 profit generates \$10,000. Traditional Apriori ignores the price tag and declares bubblegum a "frequent itemset" while discarding the watches as "rare noise"! High-utility mining factors in the actual profit.
          </div>

          <div class="formula-box text-xs space-y-2">
            <div>
              <strong class="text-indigo-400">1. Utility Definitions:</strong><br/>
              &bull; External Utility $p(i)$: Unit profit/value of item $i$ in utility table.<br/>
              &bull; Internal Utility $q(i, T)$: Quantity of item $i$ bought in transaction $T$.<br/>
              &bull; Utility of item in transaction: $u(i, T) = p(i) \times q(i, T)$.<br/>
              &bull; Transaction Utility: $TU(T) = \sum_{i \in T} u(i, T)$. Total dollar value of transaction $T$.
            </div>

            <div class="border-t border-white/10 pt-2">
              <strong class="text-sky-400">2. The Non-Monotonicity Problem:</strong><br/>
              Utility is <strong>NOT monotonic</strong>! A superset can have higher OR lower utility than its subsets. Hence, Apriori pruning cannot be applied directly to raw utility!
            </div>

            <div class="border-t border-white/10 pt-2">
              <strong class="text-emerald-400">3. The TWU Downward Closure Breakthrough:</strong><br/>
              $$\text{Transaction-Weighted Utilization (TWU): } TWU(X) = \sum_{T \supseteq X} TU(T)$$
              <p class="text-slate-300 mt-1">
                <strong>TWU Downward Closure Property:</strong> For any itemsets $X \subseteq Y$, we have $TWU(X) \ge TWU(Y)$. If $TWU(X) < \text{min\_util}$, then <strong>neither $X$ nor any of its supersets $Y$ can ever be high utility</strong>!
              </p>
            </div>

            <div class="border-t border-white/10 pt-2">
              <strong class="text-amber-400">4. The Two-Phase Algorithm:</strong><br/>
              &bull; <strong>Phase 1:</strong> Uses Apriori downward closure on $TWU$ to generate Candidate High Transaction-Weighted Utilization Itemsets (HTWUIs). (Over-generates, zero false negatives).<br/>
              &bull; <strong>Phase 2:</strong> Performs one database scan over raw transactions to compute the exact utility $u(X) = \sum_{T \supseteq X} u(X, T)$ for each candidate, filtering out those below $\text{min\_util}$.
            </div>
          </div>
        </div>
      </section>
"""
