# -*- coding: utf-8 -*-

part2_html = r"""
      <!-- ==========================================
           TOPIC 1: CHAPTER 1 INTRODUCTION
      ========================================== -->
      <section id="topic-1" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-indigo-400 uppercase tracking-wider font-semibold">Topic 1 &bull; Han Chapter 1</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Chapter 1: Introduction to Data Analytics & KDD</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~8 min read</span>
        </div>

        <!-- TLDR Box -->
        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 TL;DR (1-Minute Summary):</strong>
          Data Analytics transforms raw, unorganized numbers into high-value strategic wisdom through the 9-step KDD pipeline. Data mining is the automated discovery of non-trivial, hidden, previously unknown, and actionable patterns across 6 core tasks (characterization, discrimination, association, classification, clustering, outlier analysis).
        </div>

        <!-- 1. DIKW Hierarchy -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">1.1 The DIKW Pyramid (Data &rarr; Information &rarr; Knowledge &rarr; Wisdom)</h3>
          <div class="analogy-box text-xs">
            <strong class="text-sky-300 block mb-0.5">💡 Real-World Analogy:</strong>
            Think of a patient monitoring device in an ICU:
            <ul class="mt-1 space-y-1 text-slate-300">
              <li>• <strong>Data (Raw facts):</strong> Stream of raw integers: <code>140, 95, 142, 98</code>.</li>
              <li>• <strong>Information (Contextualized):</strong> Adding units and metadata: <em>"Patient systolic/diastolic blood pressure is 140/95 mmHg at 10:00 AM."</em></li>
              <li>• <strong>Knowledge (Pattern recognition):</strong> Connecting with medical rules: <em>"Blood pressure above 140/90 mmHg consistently across 3 readings indicates Stage-2 Hypertension."</em></li>
              <li>• <strong>Wisdom (Actionable decision):</strong> Clinical intervention: <em>"Administer 5mg Amlodipine immediately to prevent cardiovascular crisis."</em></li>
            </ul>
          </div>
        </div>

        <!-- 1.2 The 9-Step KDD Process -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">1.2 The 9-Step KDD Process (Knowledge Discovery in Databases)</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            Data mining is not an isolated trick; it is the <strong>central algorithmic core</strong> of the broader 9-stage engineering process:
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="font-bold text-indigo-400">1. Domain Understanding:</span> Define user goals and prior knowledge.
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="font-bold text-indigo-400">2. Target Data Selection:</span> Query relevant subsets from data warehouses.
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="font-bold text-indigo-400">3. Cleaning & Preprocessing:</span> Remove noise, handle missing fields.
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="font-bold text-indigo-400">4. Data Reduction:</span> Dimensionality reduction (PCA), feature selection.
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="font-bold text-sky-400">5. Matching DM Goals:</span> Decide task: classification, clustering, or rules.
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="font-bold text-sky-400">6. Algorithm Choice:</span> Select specific technique (e.g., C4.5, DBSCAN, Apriori).
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="font-bold text-emerald-400">7. Data Mining:</span> Execute algorithms to uncover patterns.
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="font-bold text-amber-400">8. Pattern Evaluation:</span> Filter redundant rules using Lift/Kulczynski.
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="font-bold text-emerald-400">9. Knowledge Presentation:</span> Visual dashboards and decision deployment.
            </div>
          </div>
        </div>

        <!-- 1.3 The 6 Data Mining Functionalities -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">1.3 The 6 Primary Data Mining Tasks</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-indigo-400 block mb-1">1. Characterization & Discrimination:</strong>
              Summarizing characteristics of a target class (e.g., software engineers who buy Macs) vs comparing against contrasting classes (e.g., non-buyers).
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-sky-400 block mb-1">2. Association & Frequent Patterns:</strong>
              Finding items frequently bought together: $Beer \implies Diapers$ [Support 2%, Confidence 80%].
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-emerald-400 block mb-1">3. Classification (Supervised):</strong>
              Building a model on labeled training data to predict discrete categorical class labels for future items.
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-amber-400 block mb-1">4. Cluster Analysis (Unsupervised):</strong>
              Grouping unlabeled objects based on maximizing intra-cluster similarity and minimizing inter-cluster similarity.
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-rose-400 block mb-1">5. Outlier & Anomaly Analysis:</strong>
              Detecting observations that deviate so substantially from expected patterns as to indicate fraud, fault, or intrusion.
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-purple-400 block mb-1">6. Trend & Evolution Analysis:</strong>
              Modeling time-series, spatio-temporal trajectories, and changing behavior across sequential periods.
            </div>
          </div>
        </div>

        <!-- Trap Box -->
        <div class="trap-box text-xs">
          <strong class="text-rose-300 block mb-1">⚠️ Professor's Exam Trap: Classification vs Clustering</strong>
          Never mix up Classification and Clustering! <strong>Classification is Supervised</strong> (target class labels exist in training data, e.g., Fraud = Yes/No). <strong>Clustering is Unsupervised</strong> (no target labels exist; the algorithm discovers clusters purely from pairwise distance metrics).
        </div>

        <!-- Textbook Ch 1 Summary -->
        <details class="surface-card p-4 text-xs">
          <summary class="font-bold text-indigo-300 flex items-center justify-between cursor-pointer">
            <span>📖 Textbook Chapter 1 Summary (Han §1.8 — Plain-English Walkthrough)</span>
            <span class="toggle-icon text-indigo-400">&rarr;</span>
          </summary>
          <div class="mt-3 space-y-2 text-slate-300 border-t border-white/10 pt-2 leading-relaxed">
            <p class="text-slate-200 font-medium">Data mining turns massive piles of raw data into clear, useful patterns and real-world knowledge.</p>
            <ul class="list-disc pl-5 space-y-1">
              <li><strong>Why data mining exists:</strong> Rapid data growth demands effective, scalable, and flexible analysis. Data mining grew naturally from information technology and brings several fields together.</li>
              <li><strong>Knowledge discovery steps:</strong> The KDD process finds interesting patterns through data cleaning, data integration, data selection, data transformation, pattern and model discovery, pattern or model evaluation, and knowledge presentation.</li>
              <li><strong>What makes a pattern interesting:</strong> A pattern or model counts as knowledge when it holds on test data with some certainty, looks novel, helps users act or check a hunch, and stays easy to understand. Objective or subjective interestingness measures guide discovery.</li>
              <li><strong>Supported data types:</strong> You can mine structured data (relational databases, transaction data) and unstructured data (text, multimedia). Data also splits into stored data and stream data, which needs special stream mining algorithms.</li>
              <li><strong>Data mining functionalities:</strong> Tasks specify what patterns or knowledge to find: characterization and discrimination; mining frequent patterns, associations, and correlations; classification and regression; deep learning; cluster analysis; and outlier detection.</li>
              <li><strong>Related fields &amp; society:</strong> Data mining blends statistics, machine learning, and database technology, powering business intelligence, Web search, bioinformatics, health informatics, and finance while balancing data privacy and security.</li>
            </ul>
          </div>
        </details>
      </section>

      <!-- ==========================================
           TOPIC 2: CHAPTER 2 PREPROCESSING & STATS
      ========================================== -->
      <section id="topic-2" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-semibold">Topic 2 &bull; Han Chapter 2</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Chapter 2: Data Preprocessing, Measurements & Statistics</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~18 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 TL;DR:</strong>
          Data preprocessing handles missing values, smooths noise, normalizes ranges, and reduces dimensions so distance-based classifiers can operate. The official Endsem syllabus explicitly requires solving Exercises 2.2, 2.7, 2.18, 2.19, and 2.20!
        </div>

        <!-- 2.1 Attribute Types -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">2.1 Attribute Measurement Hierarchy</h3>
          <div class="overflow-x-auto">
            <table class="w-full text-xs text-left border border-white/10">
              <thead class="bg-slate-900 text-slate-200">
                <tr>
                  <th class="p-2 border-b border-white/10">Type</th>
                  <th class="p-2 border-b border-white/10">Description</th>
                  <th class="p-2 border-b border-white/10">Mathematical Operations</th>
                  <th class="p-2 border-b border-white/10">Example</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-white/5 text-slate-300">
                <tr>
                  <td class="p-2 font-bold text-indigo-400">Nominal</td>
                  <td class="p-2">Categories, names, codes with no intrinsic order.</td>
                  <td class="p-2 font-mono">=, &ne; (Mode only)</td>
                  <td class="p-2">Eye color, Marital status, Pin code</td>
                </tr>
                <tr>
                  <td class="p-2 font-bold text-sky-400">Ordinal</td>
                  <td class="p-2">Ranked sequence where relative order is meaningful, but distance between ranks is unknown.</td>
                  <td class="p-2 font-mono">&gt;, &lt;, =, &ne; (Median, Percentiles)</td>
                  <td class="p-2">Grade (A, B, C), Shirt size (S, M, L), Customer satisfaction</td>
                </tr>
                <tr>
                  <td class="p-2 font-bold text-emerald-400">Interval</td>
                  <td class="p-2">Equal scale intervals, but <strong>arbitrary zero point</strong> (0 does not mean absence!).</td>
                  <td class="p-2 font-mono">+, &minus; (Mean, StDev)</td>
                  <td class="p-2">Temperature in &deg;C/&deg;F, Calendar years (2026 AD)</td>
                </tr>
                <tr>
                  <td class="p-2 font-bold text-amber-400">Ratio</td>
                  <td class="p-2">Numeric scale with an <strong>inherent absolute zero point</strong> (0 means true absence). Ratios are valid!</td>
                  <td class="p-2 font-mono">+, &minus;, &times;, &divide; (Geometric mean)</td>
                  <td class="p-2">Salary, Age, Weight, Temperature in Kelvin ($200K$ is twice $100K$)</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- 2.2 Distances & Similarities -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">2.2 Mathematical Distance & Similarity Metrics</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="formula-box">
              <strong class="text-indigo-400 block mb-1">Minkowski Distance ($L_p$ Norm):</strong>
              $$d(\vec{x}, \vec{y}) = \left(\sum_{i=1}^d |x_i - y_i|^p\right)^{1/p}$$
              <p class="text-slate-400 mt-1">
                &bull; $p=1$: <strong>Manhattan ($L_1$)</strong>: City-block distance along grid lines.<br/>
                &bull; $p=2$: <strong>Euclidean ($L_2$)</strong>: Straight-line ruler distance.<br/>
                &bull; $p=\infty$: <strong>Supremum ($L_\infty$)</strong>: $\max_{i=1\dots d} |x_i - y_i|$.
              </p>
            </div>

            <div class="formula-box">
              <strong class="text-sky-400 block mb-1">Cosine Similarity (Document Vectors):</strong>
              $$\cos(\vec{x}, \vec{y}) = \frac{\vec{x} \cdot \vec{y}}{\|\vec{x}\| \|\vec{y}\|} = \frac{\sum x_i y_i}{\sqrt{\sum x_i^2}\sqrt{\sum y_i^2}}$$
              <p class="text-slate-400 mt-1">
                Measures angle, not magnitude! If two documents discuss identical topics but one is 10&times; longer, their Euclidean distance is huge, but Cosine similarity is exactly 1.0!
              </p>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs mt-2">
            <div class="formula-box">
              <strong class="text-emerald-400 block mb-1">Jaccard Coefficient (Binary Sets):</strong>
              $$J(A, B) = \frac{|A \cap B|}{|A \cup B|} = \frac{q}{q + r + s}$$
              <p class="text-slate-400 mt-1">
                $q$: attributes 1 in both; $r$: 1 in A, 0 in B; $s$: 0 in A, 1 in B. Ignores $t$ (0 in both) for asymmetric binary data!
              </p>
            </div>

            <div class="formula-box">
              <strong class="text-amber-400 block mb-1">Pearson Correlation Coefficient ($r_{A,B}$):</strong>
              $$r_{A,B} = \frac{\sum_{i=1}^n (a_i - \bar{A})(b_i - \bar{B})}{(n-1) s_A s_B} = \frac{\sum a_i b_i - n \bar{A}\bar{B}}{(n-1) s_A s_B}$$
              <p class="text-slate-400 mt-1">
                Range $[-1, +1]$. $+1$: perfect positive linear correlation; $-1$: perfect negative; $0$: linearly uncorrelated.
              </p>
            </div>
          </div>
        </div>

        <!-- 2.3 Normalization Methods -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">2.3 Normalization Techniques</h3>
          <div class="space-y-2 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-indigo-400">1. Min-Max Normalization:</strong> Maps to range $[\text{new\_min}, \text{new\_max}]$ (typically $[0, 1]$):
              $$v' = \frac{v - \min_A}{\max_A - \min_A} (\text{new\_max}_A - \text{new\_min}_A) + \text{new\_min}_A$$
              <span class="text-slate-400"><em>Weakness:</em> Extremely sensitive to future out-of-bounds outliers!</span>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-sky-400">2. Z-Score Normalization (Zero-Mean):</strong>
              $$v' = \frac{v - \bar{A}}{\sigma_A} \quad \text{or with Mean Absolute Deviation: } v' = \frac{v - \bar{A}}{s_A}$$
              <span class="text-slate-400">Useful when actual min and max are unknown or outliers distort min-max bounds.</span>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-emerald-400">3. Decimal Scaling:</strong> $v' = \frac{v}{10^j}$, where $j$ is the smallest integer such that $\max(|v'|) < 1$.
            </div>
          </div>
        </div>

        <!-- 2.4 MANDATED TEXTBOOK EXERCISES CHAPTER 2 -->
        <div class="surface-elevated p-5 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-amber-300">Mandated Solved Textbook Exercises (Han 4th Ed. Chapter 2)</h3>
            <span class="text-xs font-mono text-amber-400">Ex 2.2, 2.7, 2.18 (+2.14), 2.19, 2.20</span>
          </div>

          <!-- Ex 2.2 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 2.2 (Book p. 80 / PDF p. 111): Central Tendency, Five-Number Summary &amp; Boxplot of Age</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> Suppose that the data for analysis include the attribute <em>age</em>. The <em>age</em> values for the data tuples are (in ascending order): <code>13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70</code> ($N = 27$). (a) What is the <em>mean</em> of the data? What is the <em>median</em>? (b) What is the <em>mode</em> and modality? (c) What is the <em>midrange</em>? (d) Find (roughly) $Q_1$ and $Q_3$. (e) Give the <em>five-number summary</em>. (f) Show a <em>boxplot</em> of the data.</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a) Mean &amp; Median ($N = 27$):</strong></p>
                <p>&bull; $\sum x_i = 809 \implies \text{Mean } \bar{x} = \frac{809}{27} \approx \mathbf{29.9630}$ years.</p>
                <p>&bull; $N = 27$ is odd $\implies$ Median is at position $\frac{27+1}{2} = 14 \implies \text{Median } (Q_2) = x_{(14)} = \mathbf{25}$.</p>
                <p><strong>(b) Mode &amp; Modality:</strong> Both $25$ and $35$ occur $4$ times (highest frequency) $\implies$ <strong>Bimodal</strong> (modes: $25, 35$).</p>
                <p><strong>(c) Midrange:</strong> $\frac{\min + \max}{2} = \frac{13 + 70}{2} = \mathbf{41.5}$.</p>
                <p><strong>(d) Quartiles ($Q_1, Q_3$):</strong> Splitting at $x_{(14)} = 25$ (excluding median): lower half has $13$ items &rarr; middle ($7$th) is $Q_1 = \mathbf{20}$; upper half has $13$ items ($15$th–$27$th) &rarr; middle ($21$st) is $Q_3 = \mathbf{35}$.</p>
                <p><strong>(e) Five-Number Summary:</strong> $[\text{Min}, Q_1, Q_2, Q_3, \text{Max}] = \mathbf{[13, 20, 25, 35, 70]}$.</p>
                <p><strong>(f) Boxplot &amp; Fences:</strong> $\text{IQR} = Q_3 - Q_1 = 35 - 20 = 15$. Lower fence $= 20 - 1.5(15) = -2.5$ (lower whisker $= 13$). Upper fence $= 35 + 1.5(15) = 57.5 \implies \mathbf{70}$ is an <strong>outlier</strong> (plotted individually); upper whisker stops at $\mathbf{52}$.</p>
              </div>
            </div>
          </details>

          <!-- Ex 2.7 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 2.7 (Book p. 81 / PDF p. 112): Hospital Age &amp; %Fat — Stats, Boxplots, Scatter &amp; Q-Q Plot</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> Suppose that a hospital tested the <em>age</em> and <em>body fat</em> data for 18 randomly selected adults ($n=18$): (a) Calculate the mean, median, and standard deviation of <em>age</em> and <em>%fat</em>. (b) Draw the boxplots for <em>age</em> and <em>%fat</em>. (c) Draw a <em>scatter plot</em> and a <em>q-q plot</em> based on these two variables.</p>
              <div class="overflow-x-auto my-1">
                <table class="w-full text-[11px] font-mono text-center border border-white/10">
                  <tr class="bg-slate-950 text-indigo-300"><td>age</td><td>23</td><td>23</td><td>27</td><td>27</td><td>39</td><td>41</td><td>47</td><td>49</td><td>50</td></tr>
                  <tr><td class="bg-slate-950 text-sky-300">%fat</td><td>9.5</td><td>26.5</td><td>7.8</td><td>17.8</td><td>31.4</td><td>25.9</td><td>27.4</td><td>27.2</td><td>31.2</td></tr>
                  <tr class="bg-slate-950 text-indigo-300"><td>age</td><td>52</td><td>54</td><td>54</td><td>56</td><td>57</td><td>58</td><td>58</td><td>60</td><td>61</td></tr>
                  <tr><td class="bg-slate-950 text-sky-300">%fat</td><td>34.6</td><td>42.5</td><td>28.8</td><td>33.4</td><td>30.2</td><td>34.1</td><td>32.9</td><td>41.2</td><td>35.7</td></tr>
                </table>
              </div>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a) Summary Statistics (Han Eq. 2.6 population $\sigma$; sample $s$ shown in parentheses):</strong></p>
                <p>&bull; <strong>age:</strong> $\sum x_i = 836 \implies \bar{x} = \frac{836}{18} \approx \mathbf{46.4444}$. Median $= \frac{50+52}{2} = \mathbf{51.0}$. $\sigma = \sqrt{\frac{2970.4444}{18}} \approx \mathbf{12.8462}$ (sample $s \approx 13.2186$).</p>
                <p>&bull; <strong>%fat (sorted):</strong> <code>7.8, 9.5, 17.8, 25.9, 26.5, 27.2, 27.4, 28.8, 30.2, 31.2, 31.4, 32.9, 33.4, 34.1, 34.6, 35.7, 41.2, 42.5</code>.</p>
                <p>&bull; $\sum y_i = 518.1 \implies \bar{y} = \frac{518.1}{18} \approx \mathbf{28.7833}$. Median $= \frac{30.2+31.2}{2} = \mathbf{30.7}$. $\sigma = \sqrt{\frac{1455.9450}{18}} \approx \mathbf{8.9937}$ (sample $s \approx 9.2544$).</p>
                <p><strong>(b) Boxplots ($n=18 \implies$ lower 9 median = 5th, upper 9 median = 14th):</strong></p>
                <p>&bull; <strong>age:</strong> $[23, 39, 51, 57, 61]$, $\text{IQR}=18$, fences $[12, 84] \implies$ no outliers; whiskers $23$ and $61$.</p>
                <p>&bull; <strong>%fat:</strong> $[7.8, 26.5, 30.7, 34.1, 42.5]$, $\text{IQR}=7.6$, fences $[15.1, 45.5] \implies \mathbf{7.8, 9.5}$ are outliers (&lt; $15.1$); lower whisker $= 17.8$, upper whisker $= 42.5$.</p>
                <p><strong>(c) Scatter &amp; Q-Q Plot:</strong> Scatter plots observed pairs $(\text{age}_i, \text{\%fat}_i)$ showing an upward linear trend. Q-Q plot pairs independently sorted quantiles $(x_{(i)}, y_{(i)})$ at $f_i = \frac{i-0.5}{18}$ (e.g., $(23, 7.8), (23, 9.5), \dots, (61, 42.5)$), revealing an S-like shift at lower ages because low-fat points skew the left tail.</p>
              </div>
            </div>
          </details>

          <!-- Ex 2.18 (+2.14) -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 2.18 (Book p. 82 / PDF p. 113): Normalization of Age = 35 (using Ex. 2.14 Data)</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> Using the data for <em>age</em> given in Exercise 2.14 (<code>13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70</code>; $N=27, \min=13, \max=70, \bar{x}=\frac{809}{27}\approx 29.9630$), answer: (a) Use min-max normalization to transform $v=35$ onto $[0.0, 1.0]$. (b) Use z-score normalization to transform $v=35$, where standard deviation $\sigma = 12.70$ years. (c) Use decimal scaling for $v=35$. (d) Comment on which method you prefer and why.</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a) Min-Max onto $[0.0, 1.0]$:</strong> $v' = \frac{35 - 13}{70 - 13}(1.0 - 0.0) + 0.0 = \frac{22}{57} \approx \mathbf{0.3860}$.</p>
                <p><strong>(b) Z-Score ($\sigma = 12.70$):</strong> $v' = \frac{35 - 29.9630}{12.70} = \frac{5.0370}{12.70} \approx \mathbf{0.3966}$ (with rounded $\bar{A}=29.96$: $0.3969$).</p>
                <p><strong>(c) Decimal Scaling:</strong> $\max(|v_i|) = 70 \implies$ smallest $j$ with $70 / 10^j \lt 1$ is $j = 2 \implies v' = \frac{35}{10^2} = \mathbf{0.35}$.</p>
                <p><strong>(d) Preference:</strong> <strong>Decimal scaling</strong> (simple division by $100$, preserves exact proportions, never goes out-of-bounds for human ages $&lt; 100$) or <strong>Z-score normalization</strong> (resists range compression from the outlier $70$ and handles future records $&gt; 70$ without breaking $[0,1]$ bounds, unlike Min-Max).</p>
              </div>
            </div>
          </details>

          <!-- Ex 2.19 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 2.19 (Book p. 82 / PDF p. 113): Z-Score Table, Pearson Correlation &amp; Covariance (Ex. 2.7 Data)</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> Using the data for <em>age</em> and <em>body fat</em> given in Exercise 2.7, answer: (a) Normalize the two attributes based on <em>z-score normalization</em>. (b) Calculate the <em>correlation coefficient</em> (Pearson's product moment coefficient). Are they positively or negatively correlated? Compute their covariance.</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a) Z-Score Normalization ($z_i = \frac{v_i - \bar{V}}{\sigma_V}$ using $\bar{A}=46.4444, \sigma_A=12.8462$ and $\bar{B}=28.7833, \sigma_B=8.9937$):</strong></p>
                <p>Sample values: Tuple 1 $(23, 9.5) \to (-1.8250, -2.1441)$; Tuple 5 $(39, 31.4) \to (-0.5795, +0.2909)$; Tuple 9 $(50, 31.2) \to (+0.2768, +0.2687)$; Tuple 18 $(61, 35.7) \to (+1.1331, +0.7691)$.</p>
                <div class="overflow-x-auto my-1">
                  <table class="w-full text-[10px] text-center border border-white/10">
                    <tr class="bg-slate-900 text-indigo-300"><th>#</th><th>age</th><th>$z_{\text{age}}$</th><th>%fat</th><th>$z_{\text{\%fat}}$</th><th>#</th><th>age</th><th>$z_{\text{age}}$</th><th>%fat</th><th>$z_{\text{\%fat}}$</th></tr>
                    <tr><td>1</td><td>23</td><td>-1.825</td><td>9.5</td><td>-2.144</td><td>10</td><td>52</td><td>+0.433</td><td>34.6</td><td>+0.647</td></tr>
                    <tr><td>2</td><td>23</td><td>-1.825</td><td>26.5</td><td>-0.254</td><td>11</td><td>54</td><td>+0.588</td><td>42.5</td><td>+1.525</td></tr>
                    <tr><td>3</td><td>27</td><td>-1.514</td><td>7.8</td><td>-2.333</td><td>12</td><td>54</td><td>+0.588</td><td>28.8</td><td>+0.002</td></tr>
                    <tr><td>4</td><td>27</td><td>-1.514</td><td>17.8</td><td>-1.221</td><td>13</td><td>56</td><td>+0.744</td><td>33.4</td><td>+0.513</td></tr>
                    <tr><td>5</td><td>39</td><td>-0.580</td><td>31.4</td><td>+0.291</td><td>14</td><td>57</td><td>+0.822</td><td>30.2</td><td>+0.158</td></tr>
                    <tr><td>6</td><td>41</td><td>-0.424</td><td>25.9</td><td>-0.321</td><td>15</td><td>58</td><td>+0.900</td><td>34.1</td><td>+0.591</td></tr>
                    <tr><td>7</td><td>47</td><td>+0.043</td><td>27.4</td><td>-0.154</td><td>16</td><td>58</td><td>+0.900</td><td>32.9</td><td>+0.458</td></tr>
                    <tr><td>8</td><td>49</td><td>+0.199</td><td>27.2</td><td>-0.176</td><td>17</td><td>60</td><td>+1.055</td><td>41.2</td><td>+1.381</td></tr>
                    <tr><td>9</td><td>50</td><td>+0.277</td><td>31.2</td><td>+0.269</td><td>18</td><td>61</td><td>+1.133</td><td>35.7</td><td>+0.769</td></tr>
                  </table>
                </div>
                <p><strong>(b) Covariance &amp; Pearson Correlation ($n = 18$):</strong></p>
                <p>&bull; $\sum_{i=1}^{18} a_i b_i = 25763.20$, $\sum (a_i - \bar{A})(b_i - \bar{B}) = 1700.3333$.</p>
                <p>&bull; $\text{Cov}(A, B) = \frac{25763.20}{18} - (46.4444)(28.7833) = \mathbf{94.4630}$ (sample cov $\div 17 = 100.0196$).</p>
                <p>&bull; $r_{A,B} = \frac{94.4630}{(12.8462)(8.9937)} = \mathbf{+0.8176}$ (exact same value for sample vs population).</p>
                <p>&bull; <strong>Conclusion:</strong> Strong <strong>positive correlation</strong> ($r = +0.8176 \gt 0$): body fat percentage generally rises with age.</p>
              </div>
            </div>
          </details>

          <!-- Ex 2.20 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 2.20 (Book p. 82 / PDF p. 113): Partitioning 12 Sales Price Records into 3 Bins</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> Suppose a group of 12 <em>sales price</em> records has been sorted as follows: <code>5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215</code>. Partition them into three bins by: (a) Equal-frequency (equal-depth) partitioning, (b) Equal-width partitioning, (c) Clustering.</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a) Equal-Frequency ($12 / 3 = 4$ items per bin):</strong></p>
                <p>&bull; Bin 1: <code>{5, 10, 11, 13}</code> &bull; Bin 2: <code>{15, 35, 50, 55}</code> &bull; Bin 3: <code>{72, 92, 204, 215}</code></p>
                <p><strong>(b) Equal-Width:</strong> Width $w = \frac{215 - 5}{3} = 70 \implies$ bins $[5, 75], (75, 145], (145, 215]$:</p>
                <p>&bull; Bin 1: <code>{5, 10, 11, 13, 15, 35, 50, 55, 72}</code> &bull; Bin 2: <code>{92}</code> &bull; Bin 3: <code>{204, 215}</code></p>
                <p><strong>(c) Clustering ($k = 3$ 1D $k$-means minimizing SSE):</strong></p>
                <p>&bull; Cluster 1: <code>{5, 10, 11, 13, 15, 35}</code> (mean $= 14.83$) &bull; Cluster 2: <code>{50, 55, 72, 92}</code> (mean $= 67.25$) &bull; Cluster 3: <code>{204, 215}</code> (mean $= 209.50$). (Check: $|35 - 14.83| = 20.17 \lt |35 - 67.25| = 32.25$.)</p>
              </div>
            </div>
          </details>
        </div>

        <!-- Textbook Ch 2 Summary -->
        <details class="surface-card p-4 text-xs">
          <summary class="font-bold text-emerald-300 flex items-center justify-between cursor-pointer">
            <span>📖 Textbook Chapter 2 Summary (Han §2.7 — Plain-English Walkthrough)</span>
            <span class="toggle-icon text-emerald-400">&rarr;</span>
          </summary>
          <div class="mt-3 space-y-2 text-slate-300 border-t border-white/10 pt-2 leading-relaxed">
            <p class="text-slate-200 font-medium">Good data mining starts with knowing your attribute types, measuring how objects compare, and cleaning messy inputs.</p>
            <ul class="list-disc pl-5 space-y-1">
              <li><strong>Data objects &amp; attribute types:</strong> Datasets contain objects described by nominal (categorical names), binary (two states, symmetric or asymmetric), ordinal (ranked without known step sizes), or numeric attributes.</li>
              <li><strong>Numeric scales:</strong> Interval-scaled attributes use fixed equal units (no true zero), while ratio-scaled attributes have an inherent zero-point so ratios make sense.</li>
              <li><strong>Basic statistics &amp; plots:</strong> Mean, weighted mean, median, and mode track central tendency; range, quantiles, quartiles, IQR, variance, and standard deviation track spread. Boxplots, quantile plots, Q-Q plots, histograms, and scatter plots let you inspect distributions visually.</li>
              <li><strong>Similarity &amp; dissimilarity:</strong> Common proximity metrics include Jaccard coefficient (asymmetric binary), Euclidean, Manhattan, Minkowski, and supremum distances (numeric), cosine measure and Tanimoto coefficient (sparse term-frequency vectors), and Kullback-Leibler (KL) divergence $D_{KL}(p(x) \| q(x))$.</li>
              <li><strong>Data quality &amp; cleaning:</strong> Quality spans accuracy, completeness, consistency, timeliness, believability, and interpretability. Data cleaning fills missing values, smooths noise, spots outliers, and fixes inconsistencies via discrepancy detection and transformation.</li>
              <li><strong>Integration, transformation &amp; reduction:</strong> Data integration resolves semantic heterogeneity, correlation, and tuple duplication. Data transformation uses normalization, discretization, compression, and sampling; dimensionality reduction uses PCA, attribute subset selection, kernel PCA, and t-SNE.</li>
            </ul>
          </div>
        </details>
      </section>
"""
