# -*- coding: utf-8 -*-

part3_html = r"""
      <!-- ==========================================
           TOPIC 3: CHAPTER 3 DATA WAREHOUSING, OLAP & BUC
      ========================================== -->
      <section id="topic-3" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-purple-400 uppercase tracking-wider font-semibold">Topic 3 &bull; Han Chapter 3</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Chapter 3: Data Warehousing, OLAP & BUC Algorithm</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~15 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 TL;DR:</strong>
          A Data Warehouse is a subject-oriented, integrated, time-variant, non-volatile database optimized for complex analytical queries (OLAP). The BUC algorithm computes Iceberg Cubes bottom-up, recursively pruning entire lattice subtrees whenever tuple counts drop below <code>min_sup</code>. Mandated exercises: 3.15, 3.17, 3.18, 3.22.
        </div>

        <!-- 3.1 Warehouse Characteristics & Schemas -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">3.1 Warehouse Architecture & Multidimensional Schemas</h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-indigo-400 block mb-1">1. Star Schema</strong>
              <p class="text-slate-300">Single central Fact table referencing multiple un-normalized Dimension tables. Simplest query joins, fastest aggregations, high data redundancy.</p>
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-sky-400 block mb-1">2. Snowflake Schema</strong>
              <p class="text-slate-300">Dimension tables are normalized into hierarchies (e.g. Item &rarr; Subcategory &rarr; Category). Zero redundancy, but requires slower multi-table joins.</p>
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-emerald-400 block mb-1">3. Fact Constellation</strong>
              <p class="text-slate-300">Multiple fact tables sharing common conformed dimension tables (e.g. Sales Fact and Shipping Fact sharing Item and Time dimensions).</p>
            </div>
          </div>
        </div>

        <!-- 3.2 OLAP Operations & Measure Types -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">3.2 OLAP Operations & Cube Measure Categories</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-amber-400 block mb-1">5 Core OLAP Operations:</strong>
              <p>&bull; <strong>Roll-Up:</strong> Climbing concept hierarchy (Day &rarr; Month &rarr; Year) or dimension reduction.</p>
              <p>&bull; <strong>Drill-Down:</strong> Stepping down hierarchy (Quarter &rarr; Month) or introducing new dimensions.</p>
              <p>&bull; <strong>Slice:</strong> Selecting a specific single value along one dimension (e.g. <code>Time = '2026'</code>).</p>
              <p>&bull; <strong>Dice:</strong> Defining a subcube via conditions across 2+ dimensions.</p>
              <p>&bull; <strong>Pivot:</strong> Rotating 3D axes to provide alternative cross-tabulation perspectives.</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-pink-400 block mb-1">3 Aggregation Measure Categories:</strong>
              <p>&bull; <strong>Distributive:</strong> Computed by partitioning data, computing sub-aggregates, and combining directly: <code>COUNT</code>, <code>SUM</code>, <code>MIN</code>, <code>MAX</code>.</p>
              <p>&bull; <strong>Algebraic:</strong> Computed using algebraic functions over $M$ distributive measures: <code>AVG = SUM / COUNT</code>, <code>STDDEV</code>.</p>
              <p>&bull; <strong>Holistic:</strong> Cannot be computed from sub-aggregates; requires full dataset: <code>MEDIAN</code>, <code>MODE</code>, <code>RANK</code>.</p>
            </div>
          </div>
        </div>

        <!-- 3.3 The BUC Algorithm -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">3.3 The BUC Algorithm (Bottom-Up Computation, Beyer & Ramakrishnan 1999)</h3>
          <div class="analogy-box text-xs">
            <strong class="text-sky-300 block mb-0.5">💡 Real-World Analogy:</strong>
            Imagine looking for big revenue branches in a multi-level organizational directory. Instead of checking every individual employee and aggregating upwards, you check the top division: if the entire "Footwear" division in Chicago sold only 3 pairs (below threshold 10), there is <strong>zero point</strong> checking running shoes, boots, or socks in that division! You prune the entire recursive tree immediately.
          </div>

          <div class="formula-box text-xs">
            <strong class="text-indigo-400 block mb-1">BUC Apriori Pruning Property:</strong>
            <p class="text-slate-300 font-mono">
              $$\text{If } \text{count}(c) < \text{min\_sup}, \text{ then for any descendant cell } c' \supset c, \; \text{count}(c') \le \text{count}(c) < \text{min\_sup}$$
            </p>
            <p class="text-slate-400 mt-1">
              BUC explores cuboids bottom-up (1-D &rarr; 2-D &rarr; 3-D). It partitions data in memory and sorts dimensions in <strong>decreasing order of cardinality</strong> (dimensions with most unique values first) to maximize early pruning of sparse branches!
            </p>
          </div>
        </div>

        <!-- 3.4 MANDATED TEXTBOOK EXERCISES CHAPTER 3 -->
        <div class="surface-elevated p-5 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-amber-300">Mandated Solved Textbook Exercises (Han 4th Ed. Chapter 3)</h3>
            <span class="text-xs font-mono text-amber-400">Ex 3.15, 3.17, 3.18, 3.22</span>
          </div>

          <!-- Ex 3.15 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 3.15 (Book pp. 137–138 / PDF pp. 168–169): ROLAP, MOLAP &amp; HOLAP Implementations</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> A multidimensional view can be implemented by a relational technique (<em>ROLAP</em>), a multidimensional technique (<em>MOLAP</em>), or a hybrid technique (<em>HOLAP</em>). (a) Briefly describe each. (b) Explain how each implements: (i) warehouse generation (incl. aggregation), (ii) roll-up, (iii) drill-down, (iv) incremental updating. (c) Which do you prefer, and why?</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a) Descriptions:</strong> <strong>ROLAP</strong> uses relational tables (star/snowflake) + OLAP middleware generating SQL. <strong>MOLAP</strong> stores cuboids directly in compressed array-based multidimensional structures. <strong>HOLAP</strong> combines both: atomic base data in ROLAP + high-level summary cubes in MOLAP.</p>
                <p><strong>(b) Operations Matrix:</strong></p>
                <div class="overflow-x-auto my-1">
                  <table class="w-full text-[10px] text-left border border-white/10">
                    <tr class="bg-slate-900 text-amber-300"><th class="p-1.5">Operation</th><th class="p-1.5">ROLAP</th><th class="p-1.5">MOLAP</th><th class="p-1.5">HOLAP</th></tr>
                    <tr><td class="p-1.5 font-bold">i. Generation</td><td class="p-1.5">Load fact/dim tables; compute SQL GROUP BY / CUBE summary tables.</td><td class="p-1.5">Map dims to array indices; MultiWay array cubing with sparse compression.</td><td class="p-1.5">Load base rows to ROLAP; materialize upper summary cuboids in MOLAP.</td></tr>
                    <tr><td class="p-1.5 font-bold">ii. Roll-up</td><td class="p-1.5">Join dims to parent level + SQL GROUP BY (or redirect to coarser table).</td><td class="p-1.5">Index directly into coarser cuboid array or sum along axis.</td><td class="p-1.5">Read precomputed MOLAP array; fall back to ROLAP if not materialized.</td></tr>
                    <tr><td class="p-1.5 font-bold">iii. Drill-down</td><td class="p-1.5">SQL query with WHERE on parent + GROUP BY finer dim attribute.</td><td class="p-1.5">Index lower-level array chunk along refined dim coordinates.</td><td class="p-1.5">Traverse MOLAP arrays; switch to ROLAP SQL for raw drill-through.</td></tr>
                    <tr><td class="p-1.5 font-bold">iv. Incremental Update</td><td class="p-1.5">Append deltas to fact table; update affected summary rows via MERGE.</td><td class="p-1.5">Insert into chunks; expand/re-chunk arrays for new members; propagate ancestors.</td><td class="p-1.5">Append raw deltas to ROLAP, then propagate delta aggregates to MOLAP.</td></tr>
                  </table>
                </div>
                <p><strong>(c) Preference:</strong> <strong>HOLAP</strong> is best overall for large enterprise warehouses: massive sparse atomic data scales cleanly in ROLAP while frequent summary analytics run at MOLAP array speed.</p>
              </div>
            </div>
          </details>

          <!-- Ex 3.17 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 3.17 (Book p. 138 / PDF p. 169): Max &amp; Min Cells in an n-D Data Cube (p Distinct Values)</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> A data cube $C$ has $n$ dimensions, each with exactly $p$ distinct values in the base cuboid (no concept hierarchies). Find: (a) max cells in base cuboid, (b) min cells in base cuboid, (c) max cells in $C$ (base + aggregate), (d) min cells in $C$.</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a) Max base cells:</strong> All Cartesian tuples present $\implies \mathbf{p^n}$.</p>
                <p><strong>(b) Min base cells:</strong> Every dimension still exhibits all $p$ distinct values; placing values diagonally $(v_{1,i}, \dots, v_{n,i})$ requires at least $\mathbf{p}$ cells.</p>
                <p><strong>(c) Max total cells in $C$:</strong> Each coordinate takes $p$ values or $*$ (<code>all</code>): $\sum_{k=0}^n \binom{n}{k} p^k = \mathbf{(p + 1)^n}$.</p>
                <p><strong>(d) Min total cells in $C$:</strong> Out of $2^n$ cuboids, the $0$-D apex has $1$ cell, and all $2^n - 1$ non-apex cuboids retain $\ge 1$ dimension with $p$ distinct values ($\ge p$ cells each; achieved by $p$ diagonal base cells) $\implies \mathbf{p(2^n - 1) + 1 = p \cdot 2^n - p + 1}$.</p>
              </div>
            </div>
          </details>

          <!-- Ex 3.18 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 3.18 (Book p. 138 / PDF p. 169): 10-D Base Cuboid (3 Cells) — Full, Iceberg &amp; Closed Cells</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> A 10-D base cuboid has 3 base cells: (1) $(a_1, d_2, d_3, d_4, \dots, d_{10})$, (2) $(d_1, b_2, d_3, d_4, \dots, d_{10})$, (3) $(d_1, d_2, c_3, d_4, \dots, d_{10})$, with $a_1 \ne d_1, b_2 \ne d_2, c_3 \ne d_3$ and measure <code>count()</code>. Find: (a) nonempty cuboids, (b) nonempty aggregate (nonbase) cells, (c) nonempty aggregate cells with <code>count >= 2</code>, (d) closed cells in the full cube.</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p>Let dims $\{4,\dots,10\}$ have $2^7 = 128$ keep/$*$ subsets (values never differ there).</p>
                <p><strong>(a) Nonempty cuboids:</strong> Every projection of 3 base cells is nonempty $\implies 2^{10} = \mathbf{1024}$.</p>
                <p><strong>(b) Nonempty aggregate cells:</strong> Over dims $\{1,2,3\}$: $\emptyset$ gives $1$ cell (count 3); 1 kept dim ($3$ choices) gives $2$ cells each (count 2 and 1); 2 kept dims ($3$ choices) give $3$ cells each; all 3 kept dims give $3$ cells in $128 - 1 = 127$ nonbase cuboids. Sum $= (1 + 6 + 9) \times 128 + 3 \times 127 = \mathbf{2429}$ (total $2432 - 3$ base).</p>
                <p><strong>(c) Iceberg aggregate cells ($\text{count} \ge 2$):</strong> Only $\emptyset$ on $\{1,2,3\}$ ($1$ cell, count 3) and single kept dim on $\{1,2,3\}$ ($3 \times 1$ cells with $d_i$, count 2) pass $\implies (1 + 3) \times 128 = \mathbf{512}$.</p>
                <p><strong>(d) Closed cells:</strong> Closed cells must fix $d_4,\dots,d_{10}$. Over $\{1,2,3\}$: count 3 gives $(*, *, *, d_4\dots)$ ($1$ cell); count 2 gives $(d_1,*,*)$, $(*,d_2,*)$, $(*,*,d_3)$ ($3$ cells); count 1 gives the $3$ base cells $\implies 1 + 3 + 3 = \mathbf{7}$.</p>
              </div>
            </div>
          </details>

          <!-- Ex 3.22 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 3.22 (Book p. 139 / PDF p. 170): Curse of Dimensionality in 100-D Full, Iceberg &amp; Closed Cubes</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> Consider 100-D base cells $(a_1, a_2, a_3, \dots, a_{100})$ and $(a_1, a_2, b_3, \dots, b_{100})$. (a) Find number of nonempty aggregate cells + storage/time comment. (b) If iceberg condition is $\text{count} \ge 2$, how many aggregate cells and which? (c) If 20 tuples map to those two base cells with count 10 each and $\text{min\_sup}=10$: (i) how many aggregate cells appear, (ii) ignoring redundant constant-to-$*$ generalizations with same measure, how many distinct (closed) cells remain?</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a) Nonempty aggregate cells:</strong> Each cell produces $2^{100}-1$ aggregate cells, overlapping only when dims $3\dots 100$ are all $*$ ($2^2 = 4$ cells) $\implies 2(2^{100}-1) - 4 = \mathbf{2^{101} - 6} \approx 2.535 \times 10^{30}$ cells. Completely intractable in time and space ($O(2^D)$).</p>
                <p><strong>(b) Iceberg ($\text{min\_sup}=2$ from count-1 cells):</strong> Only the $\mathbf{4}$ overlapping aggregate cells pass: $(a_1,a_2,*,\dots,*)$, $(a_1,*,*,\dots,*)$, $(*,a_2,*,\dots,*)$, $(*,*,*,\dots,*)$.</p>
                <p><strong>(c)(i) Iceberg ($\text{min\_sup}=10$ on count-10 base cells):</strong> Every cell has count $10$ or $20 \ge 10$, so all $\mathbf{2^{101} - 6}$ aggregate cells survive ($2^{101}-10$ with count $10$, and $4$ with count $20$)!</p>
                <p><strong>(c)(ii) Closed cells remaining:</strong> $\mathbf{3}$ cells: $(a_1, a_2, a_3, \dots, a_{100}):10$, $(a_1, a_2, b_3, \dots, b_{100}):10$, and $(a_1, a_2, *, \dots, *):20$.</p>
              </div>
            </div>
          </details>
        </div>
      </section>

      <!-- ==========================================
           TOPIC 4: CHAPTER 4 PATTERN MINING BASIC
      ========================================== -->
      <section id="topic-4" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-pink-400 uppercase tracking-wider font-semibold">Topic 4 &bull; Han Chapter 4</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Chapter 4: Pattern Mining Basic Concepts & Methods</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~15 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 TL;DR:</strong>
          Pattern mining discovers itemsets and rules that exceed minimum support and confidence thresholds. The Apriori algorithm generates candidates using downward closure ($L_{k-1} \bowtie L_{k-1}$); FP-Growth compresses the database into an FP-Tree to avoid candidate generation entirely. Mandated exercises: 4.3, 4.6, 4.10.
        </div>

        <!-- 4.1 Core Definitions -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">4.1 Core Definitions: Support, Confidence & Closed/Max Patterns</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="formula-box">
              <strong class="text-indigo-400 block mb-1">Support & Confidence:</strong>
              $$\text{Support}(A \implies B) = P(A \cup B) = \frac{\text{count}(A \cup B)}{N}$$
              $$\text{Confidence}(A \implies B) = P(B|A) = \frac{\text{count}(A \cup B)}{\text{count}(A)}$$
              <p class="text-slate-400 mt-1">A rule is <em>strong</em> if $\text{support} \ge \text{min\_sup}$ and $\text{confidence} \ge \text{min\_conf}$.</p>
            </div>

            <div class="formula-box">
              <strong class="text-sky-400 block mb-1">Closed vs Maximal Itemsets:</strong>
              <p class="text-slate-300 mb-1"><strong>Closed Itemset:</strong> An itemset $X$ is closed if there exists <em>no proper superset</em> $Y \supset X$ with $\text{support}(Y) = \text{support}(X)$. (Lossless compression!)</p>
              <p class="text-slate-300"><strong>Maximal Itemset:</strong> An itemset $X$ is maximal frequent if there exists <em>no frequent proper superset</em> $Y \supset X$. (Lossy compression: supports of sub-itemsets are lost).</p>
            </div>
          </div>
        </div>

        <!-- 4.2 Apriori vs FP-Growth -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">4.2 Apriori vs FP-Growth Algorithm Comparison</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1.5">
              <strong class="text-pink-400 block mb-1">Apriori Algorithm (Generate-and-Test):</strong>
              <p>&bull; <strong>The Apriori Property:</strong> Any subset of a frequent itemset must also be frequent. (If $\{Bread\}$ is infrequent, then $\{Bread, Milk\}$ is guaranteed infrequent!).</p>
              <p>&bull; <strong>Join Step:</strong> $L_{k-1} \bowtie L_{k-1}$ on matching first $(k-2)$ items.</p>
              <p>&bull; <strong>Prune Step:</strong> Drop candidate $c \in C_k$ if any $(k-1)$ subset $\notin L_{k-1}$.</p>
              <p>&bull; <em>Bottleneck:</em> Multiple costly full-database scans ($k$ passes) and astronomical candidate explosion ($|C_2| = \binom{10^4}{2} \approx 5 \times 10^7$).</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1.5">
              <strong class="text-emerald-400 block mb-1">FP-Growth (Divide-and-Conquer):</strong>
              <p>&bull; <strong>Scan 1:</strong> Find frequent 1-itemsets; sort items in descending order of frequency (F-List).</p>
              <p>&bull; <strong>Scan 2:</strong> Build FP-Tree by inserting each transaction ordered by F-List, sharing common prefixes with counter increments.</p>
              <p>&bull; <strong>Header Table:</strong> Linked-list pointers linking all nodes of the same item across branches.</p>
              <p>&bull; <strong>Mining:</strong> Bottom-up from rarest item: extract Conditional Pattern Base &rarr; build Conditional FP-Tree &rarr; mine recursively. <strong>Zero candidate generation!</strong></p>
            </div>
          </div>
        </div>

        <!-- 4.3 MANDATED TEXTBOOK EXERCISES CHAPTER 4 -->
        <div class="surface-elevated p-5 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-amber-300">Mandated Solved Textbook Exercises (Han 4th Ed. Chapter 4)</h3>
            <span class="text-xs font-mono text-amber-400">Ex 4.3, 4.6, 4.10 (plus 4.1)</span>
          </div>

          <!-- Ex 4.1 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 4.1 (Book p. 170 / PDF p. 201 — Included for Moodle "4.1Chapter 5" Check): Frequent Check from Closed Itemsets $\mathcal{C}$</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> Suppose you have the set $\mathcal{C}$ of all frequent closed itemsets on a data set $D$, as well as the support count for each frequent closed itemset. Describe an algorithm to determine whether a given itemset $X$ is frequent or not, and the support of $X$ if it is frequent.</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p>1. Find all frequent closed supersets: $S = \{ Y \in \mathcal{C} \mid X \subseteq Y \}$.</p>
                <p>2. If $S = \emptyset$: return <strong>not frequent</strong> (no closed frequent superset covers $X$, so $\text{closure}(X)$ cannot be frequent).</p>
                <p>3. Otherwise ($S \ne \emptyset$): return <strong>frequent</strong> with exact support count $\text{support\_count}(X) = \max_{Y \in S} \text{support\_count}(Y)$ (because $\text{closure}(X) \in S$ has $\text{support}(X) = \text{support}(\text{closure}(X)) \ge \text{support}(Y)$ for every superset $Y \supseteq \text{closure}(X)$).</p>
              </div>
            </div>
          </details>

          <!-- Ex 4.3 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 4.3 (Book p. 170 / PDF p. 201): Proofs of Apriori Subset Support, Confidence &amp; Partition Properties</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> The Apriori algorithm uses prior knowledge of subset support properties. (a) Prove all nonempty subsets of a frequent itemset must be frequent. (b) Prove $\text{support}(s') \ge \text{support}(s)$ for any nonempty subset $s' \subseteq s$. (c) Given frequent itemset $l$ and $s \subset l, s' \subseteq s$, prove $\text{conf}(s' \Rightarrow (l-s')) \le \text{conf}(s \Rightarrow (l-s))$. (d) If $D$ is divided into $n$ nonoverlapping partitions, prove any globally frequent itemset in $D$ is frequent in at least one partition.</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a) &amp; (b):</strong> Every transaction $T \in D$ containing $s$ also contains any subset $s' \subseteq s$, so $\{T \mid s \subseteq T\} \subseteq \{T \mid s' \subseteq T\} \implies \text{sup\_count}(s') \ge \text{sup\_count}(s)$. Dividing by $|D|$ gives $\text{support}(s') \ge \text{support}(s)$. Hence if $s$ is frequent ($\ge \text{min\_sup}$), every nonempty subset $s'$ is also frequent.</p>
                <p><strong>(c):</strong> $\text{conf}(s' \Rightarrow (l-s')) = \frac{\text{sup}(l)}{\text{sup}(s')}$ and $\text{conf}(s \Rightarrow (l-s)) = \frac{\text{sup}(l)}{\text{sup}(s)}$. By (b), $\text{sup}(s') \ge \text{sup}(s) \gt 0 \implies \frac{\text{sup}(l)}{\text{sup}(s')} \le \frac{\text{sup}(l)}{\text{sup}(s)}$.</p>
                <p><strong>(d) Proof by contradiction:</strong> Suppose $X$ is infrequent in all partitions $D_1,\dots,D_n$: $\text{sup\_count}_{D_i}(X) \lt \sigma |D_i|$ for all $i$. Summing over $i=1\dots n$ yields $\text{sup\_count}_D(X) \lt \sigma \sum |D_i| = \sigma |D|$, contradicting that $X$ is frequent in $D$.</p>
              </div>
            </div>
          </details>

          <!-- Ex 4.6 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 4.6 (Book p. 171 / PDF p. 202): MONKEY 5-Transaction Database — Apriori, FP-Growth &amp; Metarules</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> A database has 5 transactions ($\text{min\_sup} = 60\% \implies 3$, $\text{min\_conf} = 80\%$): <code>T100: {M,O,N,K,E,Y}</code>, <code>T200: {D,O,N,K,E,Y}</code>, <code>T300: {M,A,K,E}</code>, <code>T400: {M,U,C,K,Y}</code>, <code>T500: {C,O,O,K,I,E}</code> (as distinct item set: <code>{C,O,K,I,E}</code>). (a) Find all frequent itemsets via Apriori &amp; FP-growth and compare efficiency. (b) List all strong rules matching $\forall x \in \text{transaction},\; \text{buys}(X, \text{item}_1) \land \text{buys}(X, \text{item}_2) \Rightarrow \text{buys}(X, \text{item}_3)\; [s, c]$.</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a1) Apriori (3 DB scans):</strong></p>
                <p>&bull; $L_1$ (count $\ge 3$): <code>{E}:4, {K}:5, {M}:3, {O}:3, {Y}:3</code> (dropped: A:1, C:2, D:1, I:1, N:2, U:1).</p>
                <p>&bull; $C_2 \to L_2$ (5 of 10 pairs pass): <code>{E,K}:4, {E,O}:3, {K,M}:3, {K,O}:3, {K,Y}:3</code>.</p>
                <p>&bull; $C_3$ after Apriori prune: <code>{K,M,O}, {K,M,Y}, {K,O,Y}</code> pruned (2-subsets missing in $L_2$); only <code>{E,K,O}</code> remains &rarr; $L_3 = \{\{E,K,O\}:3\}$. (Total: <strong>11 frequent itemsets</strong>.)</p>
                <p><strong>(a2) FP-Growth (2 DB scans, zero candidates):</strong> F-list <code>K:5, E:4, M:3, O:3, Y:3</code>.</p>
                <p>&bull; Ordered DB: <code>KEMOY, KEOY, KEM, KMY, KEO</code> &rarr; Root branches via shared prefix <code>K:5 &rarr; E:4</code>.</p>
                <p>&bull; Mining suffix <code>Y</code>: prefix base <code>{KEMO:1, KEO:1, KM:1}</code> &rarr; cond tree <code>K:3</code> &rarr; <code>{Y}:3, {K,Y}:3</code>. Suffix <code>O</code>: <code>{KEM:1, KE:2}</code> &rarr; <code>K:3, E:3</code> &rarr; <code>{O}:3, {K,O}:3, {E,O}:3, {E,K,O}:3</code>. Suffix <code>M</code>: <code>{K,M}:3</code>. Suffix <code>E</code>: <code>{K,E}:4</code>. Suffix <code>K</code>: <code>{K}:5</code>.</p>
                <p>&bull; <strong>Efficiency:</strong> FP-growth needs 2 scans (vs 3) and generates 0 candidates (vs 22 tested + 3 pruned).</p>
                <p><strong>(b) Strong Metarules (from $L_3 = \{E, K, O\}$, $s = 3/5 = 60\%$):</strong></p>
                <p>&bull; $E \land K \Rightarrow O$: conf $= 3/4 = 75\%$ (Fail $&lt; 80\%$).</p>
                <p>&bull; $\mathbf{E \land O \Rightarrow K}$: $\text{sup}=60\%, \text{conf}=3/3=\mathbf{100\%}$ (Strong!).</p>
                <p>&bull; $\mathbf{K \land O \Rightarrow E}$: $\text{sup}=60\%, \text{conf}=3/3=\mathbf{100\%}$ (Strong!).</p>
              </div>
            </div>
          </details>

          <!-- Ex 4.10 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 4.10 (Book p. 172 / PDF p. 203): Incremental Association Rule Mining on $DB \cup \Delta DB$</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> Suppose that frequent itemsets are saved for a large transactional database, $DB$. Discuss how to efficiently mine the (global) association rules under the same minimum support threshold, if a set of new transactions, denoted as $\Delta DB$, is (incrementally) added in?</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p>Threshold becomes $\sigma(|DB| + |\Delta DB|)$. By the partition property (Ex. 4.3d), any globally frequent itemset in $DB' = DB \cup \Delta DB$ must be frequent in $DB$ or $\Delta DB$ (or both), giving the <strong>FUP Incremental Mining Strategy</strong>:</p>
                <p>&bull; <strong>Case 1 ($X \in L^{DB}, X \in L^{\Delta DB}$):</strong> Automatically frequent in $DB'$; simply add counts ($\text{no } DB \text{ scan}$).</p>
                <p>&bull; <strong>Case 2 ($X \in L^{DB}, X \notin L^{\Delta DB}$):</strong> Count $X$ in small $\Delta DB$ only. If sum $&lt; \sigma(|DB|+|\Delta DB|)$, discard "loser" + its supersets ($\text{no } DB \text{ scan}$).</p>
                <p>&bull; <strong>Case 3 ($X \notin L^{DB}, X \in L^{\Delta DB}$):</strong> Candidate new "winner"; scan original $DB$ <em>only</em> for these surviving candidates (whose $(k-1)$-subsets are globally frequent).</p>
                <p>&bull; <strong>Case 4 ($X \notin L^{DB}, X \notin L^{\Delta DB}$):</strong> Impossible to be globally frequent; prune immediately. Finally generate strong rules directly from updated $L^{DB'}$ in memory.</p>
              </div>
            </div>
          </details>
        </div>
      </section>
"""
