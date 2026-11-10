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
            <h3 class="text-base font-bold text-amber-300">Mandated Solved Textbook Exercises (Chapter 2)</h3>
            <span class="text-xs font-mono text-amber-400">Ex 2.2, 2.7, 2.18, 2.19, 2.20</span>
          </div>

          <!-- Ex 2.2 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 2.2: Data Cleaning & Handling Missing Values</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Suppose a retail sales dataset has 10% missing income values. What are the 5 standard methods to handle them, and which is best for machine learning?</p>
              <ol class="list-decimal ml-5 space-y-1">
                <li><strong>Ignore the tuple:</strong> Drop row. Only viable if missingness is completely random and dataset is enormous. Otherwise biases sample.</li>
                <li><strong>Fill manually:</strong> Time-consuming and infeasible for millions of rows.</li>
                <li><strong>Use global constant (e.g. "Unknown" or -1):</strong> Algorithmic hazard: clustering or decision trees might treat "Unknown" as an interesting distinct group!</li>
                <li><strong>Use attribute central tendency (Mean / Median):</strong> Fast and standard. For skewed salary distributions, use <em>median</em> over mean.</li>
                <li><strong>Most probable value (Inference via Decision Tree / Regression):</strong> Best approach. Predict missing income from Age, Education, and Job using a regression model.</li>
              </ol>
            </div>
          </details>

          <!-- Ex 2.7 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 2.7: Five-Number Summary, IQR & Boxplot Outlier Fences</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Given sorted age values: <code>13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 36, 40, 45, 46, 52, 70</code> ($n=26$). Compute Five-number summary, $IQR$, and test if $70$ is an outlier.</p>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                &bull; Min = 13, Max = 70<br/>
                &bull; Median ($Q_2$): Average of 13th (25) and 14th (25) = 25<br/>
                &bull; First Quartile ($Q_1$): Median of lower 13 values = 7th value = 20<br/>
                &bull; Third Quartile ($Q_3$): Median of upper 13 values = 20th value = 35<br/>
                &bull; Five-number summary: [13, 20, 25, 35, 70]<br/>
                &bull; $IQR = Q_3 - Q_1 = 35 - 20 = 15$<br/>
                &bull; Upper Outlier Fence: $Q_3 + 1.5 \cdot IQR = 35 + 1.5(15) = 35 + 22.5 = \mathbf{57.5}$<br/>
                &bull; Conclusion: Since $70 > 57.5$, <strong>70 is formally flagged as an outlier</strong>.
              </div>
            </div>
          </details>

          <!-- Ex 2.18 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 2.18: Cosine Similarity vs Euclidean Distance on Document Vectors</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Given document term vectors $\vec{x} = (5, 0, 3, 0, 2, 0, 0, 2, 0, 0)$ and $\vec{y} = (3, 0, 2, 0, 1, 1, 0, 1, 0, 1)$. Compute Cosine Similarity and Euclidean Distance.</p>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                &bull; Dot product: $\vec{x} \cdot \vec{y} = (5)(3) + (0)(0) + (3)(2) + (0)(0) + (2)(1) + (0)(1) + (0)(0) + (2)(1) + 0 + 0 = 15 + 6 + 2 + 2 = \mathbf{25}$<br/>
                &bull; $\|\vec{x}\| = \sqrt{5^2 + 0 + 3^2 + 0 + 2^2 + 0 + 0 + 2^2 + 0 + 0} = \sqrt{25 + 9 + 4 + 4} = \sqrt{42} \approx 6.48074$<br/>
                &bull; $\|\vec{y}\| = \sqrt{3^2 + 0 + 2^2 + 0 + 1^2 + 1^2 + 0 + 1^2 + 0 + 1^2} = \sqrt{9 + 4 + 1 + 1 + 1 + 1} = \sqrt{17} \approx 4.12311$<br/>
                &bull; $\cos(\vec{x}, \vec{y}) = \frac{25}{\sqrt{42}\sqrt{17}} = \frac{25}{\sqrt{714}} = \frac{25}{26.72078} \approx \mathbf{0.9356}$ (Highly similar documents!)<br/>
                &bull; Euclidean distance: $d(\vec{x}, \vec{y}) = \sqrt{(5-3)^2 + 0 + (3-2)^2 + 0 + (2-1)^2 + (0-1)^2 + 0 + (2-1)^2 + 0 + (0-1)^2} = \sqrt{4 + 0 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1} = \sqrt{9} = \mathbf{3.0}$.
              </div>
            </div>
          </details>

          <!-- Ex 2.19 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 2.19: Min-Max vs Z-Score Normalization Step-by-Step</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> An attribute has $\min = 200$, $\max = 1000$, $\bar{A} = 500$, and standard deviation $s = 100$. Normalize value $v = 400$ using (a) Min-Max onto $[0, 1]$ and (b) Z-score normalization.</p>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                (a) Min-Max Normalization:<br/>
                $$v' = \frac{v - \min}{\max - \min}(1 - 0) + 0 = \frac{400 - 200}{1000 - 200} = \frac{200}{800} = \mathbf{0.25}$$
                (b) Z-Score Normalization:<br/>
                $$v' = \frac{v - \bar{A}}{s} = \frac{400 - 500}{100} = \frac{-100}{100} = \mathbf{-1.0}$$
                Interpretation: 400 is located exactly 1 standard deviation below the population mean.
              </div>
            </div>
          </details>

          <!-- Ex 2.20 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 2.20: Chi-Square ($\chi^2$) Independence Test Calculation</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Given a contingency table of 1500 people classified by Gender and Fiction/Non-fiction preference:</p>
              <table class="w-full border border-white/10 text-center my-1">
                <tr class="bg-slate-950 font-bold"><td></td><td>Fiction</td><td>Non-fiction</td><td>Total</td></tr>
                <tr><td class="font-bold">Male</td><td>250 (observed)</td><td>200 (observed)</td><td>450</td></tr>
                <tr><td class="font-bold">Female</td><td>200 (observed)</td><td>850 (observed)</td><td>1050</td></tr>
                <tr class="font-bold bg-slate-950"><td>Total</td><td>450</td><td>1050</td><td>1500</td></tr>
              </table>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                1. Expected Frequencies $E_{ij} = \frac{RowTotal \times ColTotal}{N}$:<br/>
                &bull; $E_{Male, Fic} = \frac{450 \times 450}{1500} = 135$<br/>
                &bull; $E_{Male, Non} = \frac{450 \times 1050}{1500} = 315$<br/>
                &bull; $E_{Fem, Fic} = \frac{1050 \times 450}{1500} = 315$<br/>
                &bull; $E_{Fem, Non} = \frac{1050 \times 1050}{1500} = 735$<br/><br/>
                2. $\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$:<br/>
                $$\chi^2 = \frac{(250-135)^2}{135} + \frac{(200-315)^2}{315} + \frac{(200-315)^2}{315} + \frac{(850-735)^2}{735}$$
                $$\chi^2 = \frac{115^2}{135} + \frac{(-115)^2}{315} + \frac{(-115)^2}{315} + \frac{115^2}{735} = \frac{13225}{135} + \frac{13225}{315} + \frac{13225}{315} + \frac{13225}{735}$$
                $$\chi^2 = 97.96 + 41.98 + 41.98 + 17.99 = \mathbf{199.91}$$
                3. Degrees of freedom $= (r-1)(c-1) = (2-1)(2-1) = 1$.<br/>
                Critical value at $\alpha=0.001$ is $10.83$. Since $199.91 \gg 10.83$, we decisively reject the null hypothesis: <strong>Gender and Reading Preference are strongly dependent!</strong>
              </div>
            </div>
          </details>
        </div>
      </section>
"""
