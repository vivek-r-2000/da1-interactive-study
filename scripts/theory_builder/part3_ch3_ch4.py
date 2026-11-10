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
            <h3 class="text-base font-bold text-amber-300">Mandated Solved Textbook Exercises (Chapter 3)</h3>
            <span class="text-xs font-mono text-amber-400">Ex 3.15, 3.17, 3.18, 3.22</span>
          </div>

          <!-- Ex 3.15 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 3.15: Star Schema vs Snowflake Schema Design</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Design a Star Schema and Snowflake Schema for a University hospital tracking Patient Visits across Dimensions (Patient, Doctor, Department, Time). Compare their query trade-offs.</p>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                &bull; Fact Table: Patient_Visits_Fact(patient_id, doctor_id, dept_id, time_id, charge, length_of_stay)<br/>
                &bull; Star Schema: Dimensions patient_dim, doctor_dim, dept_dim, time_dim are denormalized.<br/>
                &bull; Snowflake Schema: dept_dim normalized into (dept_dim &rarr; hospital_branch_dim); time_dim normalized into (day &rarr; month &rarr; quarter &rarr; year).<br/>
                &bull; Trade-off: Snowflake saves disk space by removing redundant department descriptions, but Star schema answers aggregations ~3&times; faster due to zero dimension joins.
              </div>
            </div>
          </details>

          <!-- Ex 3.17 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 3.17: OLAP Operations Sequence Walkthrough</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Starting from total annual sales by country: <code>Sales(Country, Year)</code>, give the exact OLAP sequence to view quarterly sales of laptops in India for 2026.</p>
              <ol class="list-decimal ml-5 space-y-1 font-mono text-slate-200">
                <li><strong>Slice:</strong> Fix <code>Country = 'India'</code> and <code>Year = '2026'</code>.</li>
                <li><strong>Drill-Down:</strong> Descend on Time hierarchy from <code>Year</code> &rarr; <code>Quarter</code> (Q1, Q2, Q3, Q4).</li>
                <li><strong>Drill-Down (Dimension addition):</strong> Introduce the Item dimension hierarchy.</li>
                <li><strong>Slice:</strong> Filter <code>Item_Category = 'Laptops'</code>.</li>
              </ol>
            </div>
          </details>

          <!-- Ex 3.18 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 3.18: Distributive vs Algebraic vs Holistic Classification</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Classify the following aggregate functions and prove why <code>Median</code> is holistic:</p>
              <ul class="space-y-1 font-mono text-slate-200">
                <li>&bull; <code>SUM</code>, <code>MIN</code>, <code>MAX</code>, <code>COUNT</code> &rarr; <strong>Distributive</strong>: $SUM(D) = \sum_{k} SUM(D_k)$.</li>
                <li>&bull; <code>AVG</code>, <code>Standard Deviation</code> &rarr; <strong>Algebraic</strong>: $AVG(D) = \frac{\sum SUM(D_k)}{\sum COUNT(D_k)}$. Requires exactly 2 distributive tracking values.</li>
                <li>&bull; <code>MEDIAN</code> &rarr; <strong>Holistic</strong>: Given $Median(D_1) = 50$ and $Median(D_2) = 70$, the true median of $D_1 \cup D_2$ cannot be determined without knowing the full distribution of all individual raw elements!</li>
              </ul>
            </div>
          </details>

          <!-- Ex 3.22 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 3.22: BUC Recursive Bottom-Up Iceberg Pruning Trace</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Given 3 dimensions $A, B, C$ and threshold $\text{min\_sup} = 3$. Trace how BUC prunes when counting partition $A = a_1$.</p>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                1. BUC sorts dimensions by decreasing cardinality: say $A (10 \text{ vals}) > B (5 \text{ vals}) > C (2 \text{ vals})$.<br/>
                2. Base partition $(a_1, *, *)$ has count $= 2$.<br/>
                3. BUC tests: Is count $\ge \text{min\_sup}$? $2 < 3 \implies$ <strong>FAIL</strong>.<br/>
                4. Prune: BUC immediately skips evaluating $(a_1, b_1, *), (a_1, b_2, *), \dots, (a_1, b_k, c_j)$!<br/>
                5. Total savings: BUC avoids scanning all subcuboids under $a_1$, cutting recursion depth by 75%.
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
            <h3 class="text-base font-bold text-amber-300">Mandated Solved Textbook Exercises (Chapter 4)</h3>
            <span class="text-xs font-mono text-amber-400">Ex 4.3, 4.6, 4.10</span>
          </div>

          <!-- Ex 4.3 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 4.3: Apriori Candidate Join & Prune Step Trace</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Given $L_3 = \{\{a, b, c\}, \{a, b, d\}, \{a, c, d\}, \{a, c, e\}, \{b, c, d\}\}$. Trace the join step and prune step to find $C_4$.</p>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                1. Join Step ($L_3 \bowtie L_3$ on first 2 items):<br/>
                &bull; $\{a, b, c\} \bowtie \{a, b, d\} \implies \mathbf{\{a, b, c, d\}}$<br/>
                &bull; $\{a, c, d\} \bowtie \{a, c, e\} \implies \mathbf{\{a, c, d, e\}}$<br/>
                Candidate set after join: $C_4 = \{\{a, b, c, d\}, \{a, c, d, e\}\}$.<br/><br/>
                2. Prune Step (Check if all 3-subsets belong to $L_3$):<br/>
                &bull; For $\{a, b, c, d\}$: Subsets are $\{a, b, c\} \in L_3$, $\{a, b, d\} \in L_3$, $\{a, c, d\} \in L_3$, $\{b, c, d\} \in L_3$. All present! &rarr; <strong>KEPT</strong>.<br/>
                &bull; For $\{a, c, d, e\}$: Subsets include $\{a, d, e\}$. Is $\{a, d, e\} \in L_3$? <strong>NO!</strong> &rarr; <strong>PRUNED</strong>.<br/><br/>
                Final Valid Candidate Set: $C_4 = \mathbf{\{\{a, b, c, d\}\}}$.
              </div>
            </div>
          </details>

          <!-- Ex 4.6 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 4.6: FP-Tree Construction & Conditional Pattern Base</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Given 5 transactions: $T_1: \{I1, I2, I5\}$, $T_2: \{I2, I4\}$, $T_3: \{I2, I3\}$, $T_4: \{I1, I2, I4\}$, $T_5: \{I1, I3\}$. Let $\text{min\_sup} = 2$. Find frequent patterns containing $I5$.</p>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                1. Support counts: $I2: 4, I1: 3, I3: 2, I4: 2, I5: 1$.<br/>
                2. Filter frequent items ($\text{min\_sup} \ge 2$): $I2, I1, I3, I4$. ($I5$ has count 1 &lt; 2, so $I5$ is infrequent overall).<br/>
                3. If $\text{min\_sup}=1$, $I5$ appears in $T_1$ with prefix path: <code>(I2:1, I1:1)</code>.<br/>
                4. Conditional pattern base for $I5$: $\{\{I2, I1\}: 1\}$. Conditional FP-tree for $I5$ has no nodes with support &ge; 2.
              </div>
            </div>
          </details>

          <!-- Ex 4.10 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 4.10: Lift vs Kulczynski vs Imbalance Ratio</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> In a database of 10,000 transactions, 1,000 buy Coffee, 2,000 buy Tea, and 800 buy both. Compute Lift, Kulczynski ($Kulc$), and Imbalance Ratio ($IR$).</p>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                &bull; $P(Coffee) = \frac{1000}{10000} = 0.10$<br/>
                &bull; $P(Tea) = \frac{2000}{10000} = 0.20$<br/>
                &bull; $P(Coffee \cap Tea) = \frac{800}{10000} = 0.08$<br/><br/>
                1. Lift:<br/>
                $$\text{Lift}(Coffee \implies Tea) = \frac{P(Coffee \cap Tea)}{P(Coffee)P(Tea)} = \frac{0.08}{0.10 \times 0.20} = \frac{0.08}{0.02} = \mathbf{4.0}$$
                Lift $= 4.0 > 1 \implies$ Coffee and Tea are strongly positively correlated!<br/><br/>
                2. Kulczynski Measure (Null-Invariant):<br/>
                $$P(Tea|Coffee) = \frac{800}{1000} = 0.80, \quad P(Coffee|Tea) = \frac{800}{2000} = 0.40$$
                $$\text{Kulc} = \frac{1}{2}(0.80 + 0.40) = \mathbf{0.60}$$
                3. Imbalance Ratio ($IR$):<br/>
                $$IR = \frac{|P(Coffee) - P(Tea)|}{P(Coffee) + P(Tea) - P(Coffee \cap Tea)} = \frac{|0.10 - 0.20|}{0.10 + 0.20 - 0.08} = \frac{0.10}{0.22} \approx \mathbf{0.4545}$$
              </div>
            </div>
          </details>
        </div>
      </section>
"""
