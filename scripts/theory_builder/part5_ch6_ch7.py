# -*- coding: utf-8 -*-

part5_html = r"""
      <!-- ==========================================
           TOPIC 6: CHAPTER 6 CLASSIFICATION BASIC
      ========================================== -->
      <section id="topic-6" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-semibold">Topic 6 &bull; Han Chapter 6</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Chapter 6: Classification Basic Concepts & Methods</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~20 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 TL;DR:</strong>
          Classification builds a mapping function from input features to discrete class labels. Decision trees split nodes using Information Gain or Gini Index; Naive Bayes multiplies conditional probabilities using Bayes' rule and patches zeros with Laplace smoothing. Mandated exercises: 6.7, 6.19.
        </div>

        <!-- 6.1 Decision Tree Splitting Criteria -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">6.1 Decision Tree Attribute Selection Measures</h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
            <div class="formula-box">
              <strong class="text-indigo-400 block mb-1">1. Information Gain (ID3):</strong>
              $$\text{Info}(D) = -\sum_{i=1}^m p_i \log_2(p_i)$$
              $$\text{Info}_A(D) = \sum_{j=1}^v \frac{|D_j|}{|D|} \text{Info}(D_j)$$
              $$\text{Gain}(D, A) = \text{Info}(D) - \text{Info}_A(D)$$
              <p class="text-rose-400 mt-1 font-semibold">⚠️ Exam Trap: Biased toward attributes with many distinct values (e.g. Transaction_ID gives Gain = 1.0 but is useless)!</p>
            </div>

            <div class="formula-box">
              <strong class="text-sky-400 block mb-1">2. Gain Ratio (C4.5):</strong>
              $$\text{SplitInfo}_A(D) = -\sum_{j=1}^v \frac{|D_j|}{|D|} \log_2 \frac{|D_j|}{|D|}$$
              $$\text{GainRatio}(D, A) = \frac{\text{Gain}(D, A)}{\text{SplitInfo}_A(D)}$$
              <p class="text-slate-400 mt-1">Normalizes Information Gain by split entropy to penalize broad multi-valued attributes.</p>
            </div>

            <div class="formula-box">
              <strong class="text-emerald-400 block mb-1">3. Gini Index (CART):</strong>
              $$\text{Gini}(D) = 1 - \sum_{i=1}^m p_i^2$$
              $$\text{Gini}_A(D) = \frac{|D_1|}{|D|} \text{Gini}(D_1) + \frac{|D_2|}{|D|} \text{Gini}(D_2)$$
              $$\Delta \text{Gini}(A) = \text{Gini}(D) - \text{Gini}_A(D)$$
              <p class="text-slate-400 mt-1">Computes node impurity for binary splits. Minimizes misclassification impurity.</p>
            </div>
          </div>
        </div>

        <!-- 6.2 Naive Bayes & Laplace -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">6.2 Naive Bayesian Classification & Laplace Smoothing</h3>
          <div class="formula-box text-xs space-y-2">
            <div>
              <strong class="text-indigo-400">Bayes' Theorem:</strong>
              $$P(C_i|\mathbf{x}) = \frac{P(\mathbf{x}|C_i) P(C_i)}{P(\mathbf{x})}$$
            </div>
            <div>
              <strong class="text-sky-400">Class-Conditional Independence Assumption:</strong>
              $$P(\mathbf{x}|C_i) = \prod_{k=1}^d P(x_k|C_i) = P(x_1|C_i) \times P(x_2|C_i) \times \dots \times P(x_d|C_i)$$
            </div>
            <div class="border-t border-white/10 pt-2">
              <strong class="text-emerald-400">The Zero-Probability Problem & Laplace Correction:</strong>
              <p class="text-slate-300">
                If an attribute value $x_k$ never appeared with class $C_i$ in training data, $P(x_k|C_i) = 0$, which zeros out the <strong>entire product</strong> $P(\mathbf{x}|C_i) = 0$!
              </p>
              $$P_{\text{Laplace}}(x_k = v | C_i) = \frac{\text{count}(x_k=v, C_i) + 1}{\text{count}(C_i) + q}$$
              <p class="text-slate-400 mt-1">Where $q$ is the total number of distinct possible values for attribute $x_k$.</p>
            </div>
          </div>
        </div>

        <!-- 6.3 Evaluation Metrics -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">6.3 Model Evaluation Metrics (Confusion Matrix)</h3>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-mono text-center">
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="text-slate-400 block text-[10px]">ACCURACY</span>
              <span class="text-white font-bold">$\frac{TP + TN}{Total}$</span>
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="text-slate-400 block text-[10px]">PRECISION</span>
              <span class="text-indigo-400 font-bold">$\frac{TP}{TP + FP}$</span>
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="text-slate-400 block text-[10px]">RECALL (SENSITIVITY)</span>
              <span class="text-sky-400 font-bold">$\frac{TP}{TP + FN}$</span>
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <span class="text-slate-400 block text-[10px]">F1-SCORE</span>
              <span class="text-emerald-400 font-bold">$\frac{2 \cdot P \cdot R}{P + R}$</span>
            </div>
          </div>
        </div>

        <!-- 6.4 MANDATED TEXTBOOK EXERCISES CHAPTER 6 -->
        <div class="surface-elevated p-5 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-amber-300">Mandated Solved Textbook Exercises (Han 4th Ed. Chapter 6)</h3>
            <span class="text-xs font-mono text-amber-400">Ex 6.7, 6.19</span>
          </div>

          <!-- Ex 6.7 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 6.7 (Book pp. 299–300 / PDF pp. 330–331): Count-Weighted Decision Tree &amp; Naive Bayes</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> Generalized employee training data with <code>count</code> tuples (class label: <code>status</code> $\in \{\text{senior}, \text{junior}\}$). (a) Explain how to modify basic decision tree induction (Fig. 6.3) to handle <code>count</code>. (b) Construct a decision tree using that algorithm. (c) Classify unseen tuple $X = (\text{department}=\text{systems}, \text{age}=26\dots 30, \text{salary}=46\text{K}\dots 50\text{K})$ via naive Bayes.</p>
              <div class="overflow-x-auto my-1">
                <table class="w-full text-[11px] font-mono text-left border border-white/10">
                  <tr class="bg-slate-950 text-amber-300"><th class="p-1.5">department</th><th class="p-1.5">status</th><th class="p-1.5">age</th><th class="p-1.5">salary</th><th class="p-1.5 text-right">count</th></tr>
                  <tr><td class="p-1.5">sales</td><td>senior</td><td>31...35</td><td>46K...50K</td><td class="text-right pr-2">30</td></tr>
                  <tr><td class="p-1.5">sales</td><td>junior</td><td>26...30</td><td>26K...30K</td><td class="text-right pr-2">40</td></tr>
                  <tr><td class="p-1.5">sales</td><td>junior</td><td>31...35</td><td>31K...35K</td><td class="text-right pr-2">40</td></tr>
                  <tr><td class="p-1.5">systems</td><td>junior</td><td>21...25</td><td>46K...50K</td><td class="text-right pr-2">20</td></tr>
                  <tr><td class="p-1.5">systems</td><td>senior</td><td>31...35</td><td>66K...70K</td><td class="text-right pr-2">5</td></tr>
                  <tr><td class="p-1.5">systems</td><td>junior</td><td>26...30</td><td>46K...50K</td><td class="text-right pr-2">3</td></tr>
                  <tr><td class="p-1.5">systems</td><td>senior</td><td>41...45</td><td>66K...70K</td><td class="text-right pr-2">3</td></tr>
                  <tr><td class="p-1.5">marketing</td><td>senior</td><td>36...40</td><td>46K...50K</td><td class="text-right pr-2">10</td></tr>
                  <tr><td class="p-1.5">marketing</td><td>junior</td><td>31...35</td><td>41K...45K</td><td class="text-right pr-2">4</td></tr>
                  <tr><td class="p-1.5">secretary</td><td>senior</td><td>46...50</td><td>36K...40K</td><td class="text-right pr-2">4</td></tr>
                  <tr><td class="p-1.5">secretary</td><td>junior</td><td>26...30</td><td>26K...30K</td><td class="text-right pr-2">6</td></tr>
                </table>
              </div>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p><strong>(a) Algorithm Modification:</strong> Use <code>count</code> as row weight: $|D| = \sum \text{count}_r$, $|C_{i,D}| = \sum_{r \in C_i} \text{count}_r$, weighted entropy/gain fractions $|D_j|/|D|$, and majority voting by highest summed <code>count</code>.</p>
                <p><strong>(b) Decision Tree ($|D| = 165$: $52$ senior, $113$ junior):</strong></p>
                <p>&bull; Root $\text{Info}(D) = -\frac{52}{165}\log_2\frac{52}{165} - \frac{113}{165}\log_2\frac{113}{165} = \mathbf{0.8990}$ bits.</p>
                <p>&bull; $\text{Gain}(\text{department}) = 0.8990 - 0.8504 = \mathbf{0.0486}$; $\text{Gain}(\text{age}) = 0.8990 - \frac{79}{165}(0.9906) = \mathbf{0.4247}$; $\text{Gain}(\text{salary}) = 0.8990 - \frac{63}{165}(0.9468) = \mathbf{0.5375}$ &rarr; <strong>Split root on <code>salary</code></strong>.</p>
                <p>&bull; Pure leaves under <code>salary</code>: <code>26K...30K</code> (46 junior), <code>31K...35K</code> (40 junior), <code>36K...40K</code> (4 senior), <code>41K...45K</code> (4 junior), <code>66K...70K</code> (8 senior).</p>
                <p>&bull; Impure branch <code>46K...50K</code> ($40$ senior, $23$ junior): both <code>department</code> and <code>age</code> achieve pure split ($\text{Gain}=0.9468$; <code>department</code> wins GainRatio tie-break: <code>sales</code> &rarr; senior, <code>systems</code> &rarr; junior, <code>marketing</code> &rarr; senior).</p>
                <p><strong>(c) Naive Bayes for $X = (\text{systems}, 26\dots 30, 46\text{K}\dots 50\text{K})$:</strong></p>
                <p>&bull; Raw counts: $P(\text{age}=26\dots 30 \mid \text{senior}) = 0/52 = 0 \implies P(X|\text{senior})P(\text{senior}) = 0$; $P(X|\text{junior})P(\text{junior}) = \left(\frac{23}{113}\cdot\frac{49}{113}\cdot\frac{23}{113}\right)\frac{113}{165} = \mathbf{0.012303}$.</p>
                <p>&bull; With Laplace correction ($q_{\text{dept}}=4, q_{\text{age}}=6, q_{\text{sal}}=6$): $P_{\text{Lap}}(X|\text{senior})P(\text{senior}) = \left(\frac{9}{56}\cdot\frac{1}{58}\cdot\frac{41}{58}\right)\frac{52}{165} = \mathbf{0.000617}$ vs $P_{\text{Lap}}(X|\text{junior})P(\text{junior}) = \left(\frac{24}{117}\cdot\frac{50}{119}\cdot\frac{24}{119}\right)\frac{113}{165} = \mathbf{0.011904}$ &rarr; <strong>Predict <code>status = junior</code></strong> ($95.07\%$ posterior).</p>
              </div>
            </div>
          </details>

          <!-- Ex 6.19 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 6.19 (Book p. 302 / PDF p. 333): 10-Fold Cross-Validation Paired t-Test (M1 vs M2)</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Verbatim Question:</strong> Comparing prediction models $M_1$ and $M_2$ over 10 rounds of 10-fold CV: $M_1$ error rates = <code>30.5, 32.2, 20.7, 20.6, 31.0, 41.0, 27.7, 26.0, 21.5, 26.0</code>; $M_2$ error rates = <code>22.4, 14.5, 22.4, 19.6, 20.7, 20.4, 22.1, 19.4, 16.2, 35.0</code>. Is one model significantly better at significance level $1\%$ ($\alpha = 0.01$)?</p>
              <div class="font-mono text-slate-200 space-y-1.5 bg-slate-950 p-2.5 rounded">
                <p>1. Paired differences $d_i = \text{err}(M_1)_i - \text{err}(M_2)_i$: $[+8.1, +17.7, -1.7, +1.0, +10.3, +20.6, +5.6, +6.6, +5.3, -9.0]$.</p>
                <p>2. Means: $\overline{\text{err}}(M_1) = 27.72$, $\overline{\text{err}}(M_2) = 21.27 \implies \bar{d} = \frac{64.5}{10} = \mathbf{6.45}$.</p>
                <p>3. Variance (Han Eq. 6.32 uses $\div k$): $\sum (d_i - \bar{d})^2 = 681.225 \implies \text{var}(M_1 - M_2) = \frac{681.225}{10} = 68.1225$.</p>
                <p>4. $t$-statistic (Han Eq. 6.31): $t = \frac{6.45}{\sqrt{68.1225 / 10}} = \frac{6.45}{2.6100} \approx \mathbf{2.4712}$ ($p = 0.0355$; standard $\div (k-1)$ sample variance gives $t \approx 2.3444$).</p>
                <p>5. Decision ($\text{df} = 9$, two-tailed $\alpha = 0.01 \implies t_{0.005,\,9} = \mathbf{3.250}$): Since $|t| = 2.4712 \lt 3.250$, <strong>fail to reject $H_0$</strong>. Not statistically significant at $1\%$ (though significant at $5\%$ where $t_{0.025,9} = 2.262$).</p>
              </div>
            </div>
          </details>
        </div>

        <!-- Textbook Ch 6 Summary -->
        <details class="surface-card p-4 text-xs">
          <summary class="font-bold text-indigo-300 flex items-center justify-between cursor-pointer">
            <span>📖 Textbook Chapter 6 Summary (Han §6.8 — Plain-English Walkthrough)</span>
            <span class="toggle-icon text-indigo-400">&rarr;</span>
          </summary>
          <div class="mt-3 space-y-2 text-slate-300 border-t border-white/10 pt-2 leading-relaxed">
            <p class="text-slate-200 font-medium">This chapter covers how to build models that predict data labels, evaluate their accuracy reliably, and handle imbalanced datasets.</p>
            <ul class="list-disc pl-5 space-y-1">
              <li><strong>Classification vs. numeric prediction:</strong> Classification extracts models predicting categorical labels, while numeric prediction models continuous-valued functions.</li>
              <li><strong>Decision tree induction:</strong> Trees grow top-down recursively using attribute selection measures (ID3, C4.5, CART), and tree pruning removes noise-driven branches to boost test accuracy.</li>
              <li><strong>Naive Bayesian &amp; linear classifiers:</strong> Naive Bayes applies Bayes' theorem assuming class-conditional independence; linear classifiers (Perceptron, logistic regression) combine weighted inputs linearly.</li>
              <li><strong>Eager vs. lazy learners:</strong> Decision trees, Bayesian, and linear models are eager learners (build a global model before testing); lazy learners (nearest-neighbor, case-based reasoning) store training tuples and generalize at query time.</li>
              <li><strong>Confusion matrices &amp; metrics:</strong> Two-class confusion matrices track TP, TN, FP, FN to compute accuracy, sensitivity (recall), specificity, precision, $F$, and $F_\beta$ (accuracy alone misleads on minority classes).</li>
              <li><strong>Partitioning, model selection &amp; ensembles:</strong> Data splits via holdout, random sampling, cross-validation, or bootstrapping; significance tests ($t$-test) and ROC curves compare models. Ensembles (bagging, boosting, random forests) combine base models, while class imbalance uses oversampling, undersampling, or threshold moving.</li>
            </ul>
          </div>
        </details>
      </section>

      <!-- ==========================================
           TOPIC 7: CHAPTER 7 CLASSIFICATION ADVANCED
      ========================================== -->
      <section id="topic-7" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-indigo-400 uppercase tracking-wider font-semibold">Topic 7 &bull; Han Chapter 7</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Chapter 7: Advanced Classification Methods</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~20 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 TL;DR:</strong>
          Advanced classification addresses non-linear boundaries (SVM with Kernel trick), probabilistic dependency graphs (BBN), lazy case retrieval (CBR), ensemble variance/bias reduction (Bagging & AdaBoost Boosting), and imbalanced class sampling (SMOTE).
        </div>

        <!-- 7.1 Bayesian Belief Networks -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">7.1 Bayesian Belief Networks (BBN - Han §7.1)</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            While Naive Bayes assumes <em>all</em> attributes are mutually conditionally independent given the class, BBN allows specifying <strong>which subsets of attributes depend on each other</strong>.
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-indigo-400 block mb-1">Component 1: Directed Acyclic Graph (DAG)</strong>
              Nodes represent random variables; directed arcs represent probabilistic causal dependency. If there is no directed arc between $X$ and $Y$, they are conditionally independent given their parents!
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-sky-400 block mb-1">Component 2: Conditional Probability Tables (CPT)</strong>
              For every node $X$, a table records the conditional distribution given all combinations of parent values: $P(X | \text{Parents}(X))$.
            </div>
          </div>
          <div class="formula-box text-xs">
            <strong class="text-emerald-400">Joint Probability Factorization:</strong>
            $$P(x_1, x_2, \dots, x_n) = \prod_{i=1}^n P(x_i | \text{Parents}(X_i))$$
          </div>
        </div>

        <!-- 7.3 Support Vector Machines -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">7.3 Support Vector Machines (SVM - Han §7.3)</h3>
          <div class="analogy-box text-xs">
            <strong class="text-sky-300 block mb-0.5">💡 Real-World Analogy:</strong>
            Imagine building a straight highway dividing two enemy army camps. An amateur draws any line that doesn't hit a tent. An expert civil engineer builds the highway right down the middle with the <strong>widest possible cleared sidewalk (margin)</strong> on both sides. The tents right on the edge of the sidewalk are the <strong>Support Vectors</strong>.
          </div>

          <div class="formula-box text-xs space-y-2">
            <div>
              <strong class="text-indigo-400">1. Maximum Margin Hyperplane (MMH):</strong>
              Decision line: $\mathbf{w}^T \mathbf{x} + b = 0$. Margin width: $\gamma = \frac{2}{\|\mathbf{w}\|}$.
              To maximize margin width, we minimize $\|\mathbf{w}\| \implies \min \frac{1}{2}\|\mathbf{w}\|^2$ subject to $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1$.
            </div>
            <div class="border-t border-white/10 pt-2">
              <strong class="text-sky-400">2. The Kernel Trick for Non-Linear Boundaries:</strong>
              <p class="text-slate-300">
                If data is non-linearly separable in $\mathbb{R}^d$, map it via $\Phi(\mathbf{x})$ into a higher-dimensional Hilbert space $\mathcal{H}$ where a linear hyperplane exists. The Kernel Trick computes dot products directly in input space without ever calculating $\Phi(\mathbf{x})$ explicitly:
              </p>
              $$K(\mathbf{x}_i, \mathbf{x}_j) = \Phi(\mathbf{x}_i) \cdot \Phi(\mathbf{x}_j)$$
              &bull; <strong>Polynomial Kernel:</strong> $K(\mathbf{x}, \mathbf{z}) = (\mathbf{x}^T \mathbf{z} + 1)^d$<br/>
              &bull; <strong>Gaussian Radial Basis Function (RBF):</strong> $K(\mathbf{x}, \mathbf{z}) = \exp\left(-\gamma \|\mathbf{x} - \mathbf{z}\|^2\right)$ (Infinite dimensional mapping!)
            </div>
          </div>
        </div>

        <!-- 7.6 Ensemble Methods -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">7.6 Ensemble Methods: Bagging, Boosting & Random Forests</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-indigo-400 block mb-1">Bagging (Bootstrap Aggregating) & Random Forests:</strong>
              <p>&bull; <strong>Mechanism:</strong> Generate $B$ bootstrap samples (sampling with replacement, ~63.2% unique tuples). Train an independent base tree on each sample. Aggregate predictions via majority vote.</p>
              <p>&bull; <strong>Random Forest:</strong> Bagging + randomly select $k = \sqrt{d}$ candidate features at each node split to decorrelate trees.</p>
              <p>&bull; <strong>Goal:</strong> Drastically <strong>reduces variance</strong> without increasing bias!</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-rose-400 block mb-1">Boosting (AdaBoost - Adaptive Boosting):</strong>
              <p>&bull; <strong>Mechanism:</strong> Sequential training. In each round $t$, misclassified samples get increased weights $w_i \leftarrow w_i \exp(\alpha_t)$, while correct samples get decreased weights.</p>
              <p>&bull; <strong>Classifier Weight:</strong> $\alpha_t = \frac{1}{2} \ln\left(\frac{1 - \epsilon_t}{\epsilon_t}\right)$, where $\epsilon_t$ is weighted error.</p>
              <p>&bull; <strong>Goal:</strong> Converts weak learners into a strong learner; drastically <strong>reduces bias</strong>!</p>
            </div>
          </div>
        </div>

        <!-- Textbook Ch 7 Summary -->
        <details class="surface-card p-4 text-xs">
          <summary class="font-bold text-indigo-300 flex items-center justify-between cursor-pointer">
            <span>📖 Textbook Chapter 7 Summary (Han §7.8 — Plain-English Walkthrough)</span>
            <span class="toggle-icon text-indigo-400">&rarr;</span>
          </summary>
          <div class="mt-3 space-y-2 text-slate-300 border-t border-white/10 pt-2 leading-relaxed">
            <p class="text-slate-200 font-medium">Chapter 7 expands classification beyond basic trees into probabilistic graphs, margin-based boundaries, scarce-label learning, and complex data types. <em>(Endsem syllabus covers §7.1, 7.2.1, 7.3, 7.5, 7.6, 7.7.1, 7.7.3.)</em></p>
            <ul class="list-disc pl-5 space-y-1">
              <li><strong>Bayesian belief networks [Endsem §7.1]:</strong> Unlike Naive Bayes, BBNs let you specify conditional independencies between subsets of variables in a graphical causal model (DAG + CPTs).</li>
              <li><strong>Support vector machines &amp; multiclass [Endsem §7.3, §7.6, §7.7.3]:</strong> SVMs map tuples into higher dimensions to find a maximum-margin hyperplane via support vectors; ensembles of binary classifiers and error-correcting codes extend binary models like SVMs to multiclass tasks.</li>
              <li><strong>Scarce-label &amp; transfer learning [Endsem §7.5]:</strong> Semisupervised classification uses labeled + unlabeled data (self-training, cotraining); active learning queries a human oracle; distant supervision, transfer learning (TrAdaBoost), and zero-shot learning handle scarce labels.</li>
              <li><strong>[Beyond Endsem Core]</strong> Rule-based classifiers (sequential covering), genetic algorithms, associative &amp; discriminative frequent-pattern classification, feature selection/engineering, metric learning, and LIME local explanations.</li>
              <li><strong>[Beyond Endsem Core]</strong> Stream classification (one-pass, concept drift), sequence/graph classification, and reinforcement learning (evaluative feedback balancing exploration vs exploitation).</li>
              <li><em>Syllabus reminder:</em> Also review <strong>§7.2.1 (Lazy Learners / Case-Based Reasoning)</strong>, standalone <strong>§7.6 (Ensembles)</strong>, and <strong>§7.7.1 (Class Imbalance / SMOTE)</strong> above, which are in the Endsem syllabus even though omitted from the textbook's §7.8 summary.</li>
            </ul>
          </div>
        </details>
      </section>
"""
