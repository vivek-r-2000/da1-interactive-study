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
            <h3 class="text-base font-bold text-amber-300">Mandated Solved Textbook Exercises (Chapter 6)</h3>
            <span class="text-xs font-mono text-amber-400">Ex 6.7, 6.19</span>
          </div>

          <!-- Ex 6.7 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 6.7: Information Gain vs Gini Index Calculation Walkthrough</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Given a dataset of 14 credit applicants: 9 Approved ($C_1$), 5 Rejected ($C_2$). Attribute <code>Income</code> has 3 values: Low (4 tuples: 1 Approved, 3 Rejected), Medium (6 tuples: 4 Approved, 2 Rejected), High (4 tuples: 4 Approved, 0 Rejected). Compute Information Gain and Gini Index split for Income.</p>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                1. Base Entropy $\text{Info}(D)$:<br/>
                $$\text{Info}(D) = -\left(\frac{9}{14}\log_2\frac{9}{14} + \frac{5}{14}\log_2\frac{5}{14}\right) = -(0.6429 \times (-0.6374) + 0.3571 \times (-1.4854)) = 0.4098 + 0.5305 = \mathbf{0.9403} \text{ bits}$$
                2. Conditional Entropy $\text{Info}_{\text{Income}}(D)$:<br/>
                &bull; Low (1A, 3R): $\text{Info}(D_{\text{Low}}) = -\left(\frac{1}{4}\log_2\frac{1}{4} + \frac{3}{4}\log_2\frac{3}{4}\right) = -(0.25(-2) + 0.75(-0.415)) = 0.5 + 0.3113 = 0.8113$<br/>
                &bull; Medium (4A, 2R): $\text{Info}(D_{\text{Med}}) = -\left(\frac{4}{6}\log_2\frac{4}{6} + \frac{2}{6}\log_2\frac{2}{6}\right) = -(0.667(-0.585) + 0.333(-1.585)) = 0.390 + 0.528 = 0.9183$<br/>
                &bull; High (4A, 0R): Pure node! $\text{Info}(D_{\text{High}}) = 0$<br/>
                $$\text{Info}_{\text{Income}}(D) = \frac{4}{14}(0.8113) + \frac{6}{14}(0.9183) + \frac{4}{14}(0) = 0.2318 + 0.3936 + 0 = \mathbf{0.6254} \text{ bits}$$
                3. Information Gain:<br/>
                $$\text{Gain}(D, \text{Income}) = \text{Info}(D) - \text{Info}_{\text{Income}}(D) = 0.9403 - 0.6254 = \mathbf{0.3149} \text{ bits}$$
                4. Base Gini Index $\text{Gini}(D)$:<br/>
                $$\text{Gini}(D) = 1 - \left[\left(\frac{9}{14}\right)^2 + \left(\frac{5}{14}\right)^2\right] = 1 - [0.4133 + 0.1276] = \mathbf{0.4592}$$
                5. Binary Split Gini on \{Low\} vs \{Med, High\}:<br/>
                &bull; Low (1A, 3R): $\text{Gini}(D_1) = 1 - [(1/4)^2 + (3/4)^2] = 1 - [0.0625 + 0.5625] = 0.375$<br/>
                &bull; Med, High (8A, 2R): $\text{Gini}(D_2) = 1 - [(8/10)^2 + (2/10)^2] = 1 - [0.64 + 0.04] = 0.320$<br/>
                $$\text{Gini}_{\{\text{Low}\}}(D) = \frac{4}{14}(0.375) + \frac{10}{14}(0.320) = 0.1071 + 0.2286 = \mathbf{0.3357}$$
                $$\Delta \text{Gini} = 0.4592 - 0.3357 = \mathbf{0.1235}$$
              </div>
            </div>
          </details>

          <!-- Ex 6.19 -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Exercise 6.19: Naive Bayes Classification & Laplace Correction</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Problem:</strong> Given a training set where attribute $A$ has 3 values $\{a_1, a_2, a_3\}$. In class $C_1$ (70 samples), counts are $a_1=50, a_2=20, a_3=0$. Show how Laplace correction avoids zero probability when classifying a sample with $A=a_3$.</p>
              <div class="font-mono text-slate-200 space-y-1 bg-slate-950 p-2.5 rounded">
                1. Without Laplace correction:<br/>
                $$P(a_3|C_1) = \frac{0}{70} = 0 \implies P(\mathbf{x}|C_1) = 0 \times \prod_{k \ne A} P(x_k|C_1) = 0$$
                A single unseen value destroys all evidence from all other attributes!<br/><br/>
                2. With Laplace correction ($+1$ to numerator, $+q=3$ to denominator):<br/>
                $$P_{\text{Laplace}}(a_1|C_1) = \frac{50 + 1}{70 + 3} = \frac{51}{73} \approx 0.6986$$
                $$P_{\text{Laplace}}(a_2|C_1) = \frac{20 + 1}{70 + 3} = \frac{21}{73} \approx 0.2877$$
                $$P_{\text{Laplace}}(a_3|C_1) = \frac{0 + 1}{70 + 3} = \frac{\mathbf{1}}{\mathbf{73}} \approx \mathbf{0.0137}$$
                Sum check: $\frac{51+21+1}{73} = \frac{73}{73} = 1.0$. The zero trap is completely avoided while preserving valid probability axioms.
              </div>
            </div>
          </details>
        </div>
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
      </section>
"""
