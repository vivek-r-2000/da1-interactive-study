# -*- coding: utf-8 -*-

part7_html = r"""
      <!-- ==========================================
           TOPIC 9: OVERVIEW OF DEEP LEARNING (HAN §10.1)
      ========================================== -->
      <section id="topic-9" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-indigo-400 uppercase tracking-wider font-semibold">Topic 9 &bull; Han Chapter 10, Section 10.1</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Topic 9: Overview of Deep Learning & Backpropagation</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~18 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 TL;DR:</strong>
          Deep Learning replaces manual feature extraction with hierarchical representation learning. A single perceptron is limited by linear separability (cannot learn XOR); Multi-Layer Perceptrons (MLPs) overcome this using non-linear activations (Sigmoid, ReLU) and learn optimal weights using the Backpropagation chain rule. Prof. Reddy specifically noted: <em>"Practice the example"</em>!
        </div>

        <!-- 9.1 Perceptron & XOR -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">9.1 The Perceptron Model & The XOR Barrier</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-indigo-400 block mb-1">The Perceptron (Rosenblatt 1958):</strong>
              <p>&bull; <strong>Net Input:</strong> $z = \mathbf{w}^T \mathbf{x} + b = \sum_{i=1}^d w_i x_i + b$.</p>
              <p>&bull; <strong>Step Activation:</strong> $y = +1$ if $z \ge 0$, else $-1$ (or 0).</p>
              <p>&bull; <strong>Learning Rule:</strong> $\mathbf{w} \leftarrow \mathbf{w} + \eta (t - y) \mathbf{x}$, where $\eta \in (0, 1]$ is learning rate.</p>
              <p>&bull; <strong>Convergence Theorem (Novikoff 1962):</strong> Converges in finite steps <em>if and only if</em> data is linearly separable.</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-rose-400 block mb-1">The XOR Barrier (Minsky & Papert 1969):</strong>
              <p>&bull; In XOR: $(0, 0) \to 0, (1, 1) \to 0$, but $(0, 1) \to 1, (1, 0) \to 1$.</p>
              <p>&bull; Points with label 1 lie on the opposite diagonal of points with label 0. <strong>No single straight line can separate them!</strong></p>
              <p>&bull; <strong>Solution (MLP):</strong> Adding a hidden layer with 2 neurons (one computing OR, one computing NAND) transforms the space so the output neuron (computing AND) linearly separates them!</p>
            </div>
          </div>
        </div>

        <!-- 9.2 Activation Functions -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">9.2 Activation Functions & Derivatives</h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
            <div class="formula-box">
              <strong class="text-indigo-400 block mb-1">1. Logistic Sigmoid $\sigma(z)$:</strong>
              $$\sigma(z) = \frac{1}{1 + e^{-z}}, \quad \sigma'(z) = \sigma(z)(1 - \sigma(z))$$
              <p class="text-slate-400 mt-1">Range $(0, 1)$. Max derivative is $0.25$ at $z=0$. Causes severe <strong>vanishing gradient</strong> in deep layers!</p>
            </div>

            <div class="formula-box">
              <strong class="text-sky-400 block mb-1">2. Hyperbolic Tangent $\tanh(z)$:</strong>
              $$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}, \quad \tanh'(z) = 1 - \tanh^2(z)$$
              <p class="text-slate-400 mt-1">Range $(-1, +1)$. Zero-centered, speeding up convergence over sigmoid.</p>
            </div>

            <div class="formula-box">
              <strong class="text-emerald-400 block mb-1">3. Rectified Linear Unit (ReLU):</strong>
              $$f(z) = \max(0, z), \quad f'(z) = \begin{cases} 1 & z > 0 \\ 0 & z < 0 \end{cases}$$
              <p class="text-slate-400 mt-1">Modern standard. Constant derivative of 1 stops gradient vanishing completely!</p>
            </div>
          </div>
        </div>

        <!-- 9.3 Backpropagation Derivation -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">9.3 The Backpropagation Chain Rule Formulation</h3>
          <div class="formula-box text-xs space-y-2">
            <div>
              <strong class="text-indigo-400">1. Output Layer Weight Gradient ($w_{jk}$ connecting hidden node $j$ to output $k$):</strong>
              $$\frac{\partial E}{\partial w_{jk}} = \frac{\partial E}{\partial z_k} \frac{\partial z_k}{\partial w_{jk}} = \delta_k \cdot a_j, \quad \text{where } \delta_k \equiv (a_k - t_k) \sigma'(z_k)$$
            </div>
            <div class="border-t border-white/10 pt-2">
              <strong class="text-sky-400">2. Hidden Layer Weight Gradient ($w_{ij}$ connecting input $i$ to hidden node $j$):</strong>
              $$\frac{\partial E}{\partial w_{ij}} = \frac{\partial E}{\partial z_j} \frac{\partial z_j}{\partial w_{ij}} = \delta_j \cdot x_i, \quad \text{where } \delta_j \equiv \left(\sum_k \delta_k w_{jk}\right) \sigma'(z_j)$$
            </div>
            <div class="border-t border-white/10 pt-2">
              <strong class="text-emerald-400">3. Parameter Updates:</strong>
              $$w \leftarrow w - \eta \frac{\partial E}{\partial w}, \quad b \leftarrow b - \eta \delta$$
            </div>
          </div>
        </div>

        <!-- 9.4 TEXTBOOK WORKED EXAMPLE §10.1 -->
        <div class="surface-elevated p-5 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-amber-300">Mandated Textbook Worked Numerical Walkthrough (Han §10.1)</h3>
            <span class="text-xs font-mono text-amber-400">"Practice the example"</span>
          </div>

          <div class="p-4 rounded bg-slate-900 border border-white/10 space-y-3 text-xs">
            <p class="text-slate-200">
              <strong>Given:</strong> 2 inputs ($x_1=0.05, x_2=0.10$), biases $b_1=0.35, b_2=0.60$. Target outputs $t_1=0.01, t_2=0.99$. Learning rate $\eta=0.5$. Initial weights: $w_1=0.15, w_2=0.20, w_3=0.25, w_4=0.30, w_5=0.40, w_6=0.45, w_7=0.50, w_8=0.55$.
            </p>

            <div class="font-mono text-slate-300 space-y-1.5 bg-slate-950 p-3 rounded">
              <strong class="text-indigo-400 block mb-1">Step 1: Forward Propagation</strong>
              &bull; $z_{h1} = 0.15(0.05) + 0.20(0.10) + 0.35 = 0.3775 \implies a_{h1} = \frac{1}{1 + e^{-0.3775}} \approx \mathbf{0.59327}$<br/>
              &bull; $z_{h2} = 0.25(0.05) + 0.30(0.10) + 0.35 = 0.3925 \implies a_{h2} = \frac{1}{1 + e^{-0.3925}} \approx \mathbf{0.59688}$<br/>
              &bull; $z_{o1} = 0.40(0.59327) + 0.45(0.59688) + 0.60 = 1.1059 \implies a_{o1} = \frac{1}{1 + e^{-1.1059}} \approx \mathbf{0.75137}$<br/>
              &bull; $z_{o2} = 0.50(0.59327) + 0.55(0.59688) + 0.60 = 1.2249 \implies a_{o2} = \frac{1}{1 + e^{-1.2249}} \approx \mathbf{0.77293}$<br/>
              &bull; Total Squared Error: $E = \frac{1}{2}(0.01 - 0.75137)^2 + \frac{1}{2}(0.99 - 0.77293)^2 = 0.27481 + 0.02356 = \mathbf{0.29837}$<br/><br/>

              <strong class="text-sky-400 block mb-1">Step 2: Backward Pass for Output Weight $w_5$</strong>
              &bull; $\delta_{o1} = (a_{o1} - t_1) \cdot a_{o1}(1 - a_{o1}) = (0.75137 - 0.01) \cdot 0.75137(0.24863) \approx \mathbf{0.13850}$<br/>
              &bull; $\frac{\partial E}{\partial w_5} = \delta_{o1} \cdot a_{h1} = 0.13850 \times 0.59327 \approx \mathbf{0.08217}$<br/>
              &bull; Updated $w_5^+ = w_5 - \eta \frac{\partial E}{\partial w_5} = 0.40 - 0.5(0.08217) = \mathbf{0.35892}$<br/><br/>

              <strong class="text-emerald-400 block mb-1">Step 3: Backward Pass for Hidden Weight $w_1$</strong>
              &bull; $\delta_{o2} = (a_{o2} - t_2) \cdot a_{o2}(1 - a_{o2}) = (0.77293 - 0.99) \cdot 0.77293(0.22707) \approx \mathbf{-0.03810}$<br/>
              &bull; $\delta_{h1} = (\delta_{o1} w_5 + \delta_{o2} w_7) \cdot a_{h1}(1 - a_{h1}) = (0.13850(0.40) + (-0.03810)(0.50)) \cdot 0.59327(0.40673) \approx \mathbf{0.00877}$<br/>
              &bull; $\frac{\partial E}{\partial w_1} = \delta_{h1} \cdot x_1 = 0.00877 \times 0.05 \approx \mathbf{0.000439}$<br/>
              &bull; Updated $w_1^+ = w_1 - \eta \frac{\partial E}{\partial w_1} = 0.15 - 0.5(0.000439) = \mathbf{0.14978}$
            </div>
          </div>
        </div>
      </section>

      <!-- ==========================================
           TOPIC 10: ADVANCES, OUTLIERS & TRENDS (PPTS)
      ========================================== -->
      <section id="topic-10" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-sky-400 uppercase tracking-wider font-semibold">Topic 10 &bull; Lecture PPTs Only</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Topic 10: Advances in Clustering, Outlier Analysis & Trends in Data Mining</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~18 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 TL;DR:</strong>
          Covers advanced grid/subspace clustering (STING, CLIQUE, DENCLUE), semi-supervised constraint clustering (COP-KMeans), statistical and density-based anomaly detection (Local Outlier Factor - LOF), and emerging trends (spatio-temporal trajectories, graph community mining, high-D curse).
        </div>

        <!-- 10.1 Advances in Clustering -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">10.1 Advanced Clustering Paradigms</h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-sky-400 block mb-1">1. STING (Grid-Based):</strong>
              <p>Hierarchical quad-tree cells storing precomputed statistics ($n, m, s, \min, \max, \text{dist}$). Query processing traverses cells top-down in <strong class="text-white">$O(K)$</strong> time, <strong>completely independent of the number of raw data tuples $N$</strong>!</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-indigo-400 block mb-1">2. CLIQUE (Subspace):</strong>
              <p>Finds clusters in arbitrary subspaces of high-dimensional data. Uses the <strong>Apriori Subspace Principle</strong>: A $k$-dimensional cell is dense ONLY IF all its $(k-1)$-dimensional projections are dense.</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-emerald-400 block mb-1">3. DENCLUE (Kernel Density):</strong>
              <p>Models data using non-parametric Gaussian influence kernels. Finds local density peaks (density attractors) using gradient hill climbing. Highly resilient to noise.</p>
            </div>
          </div>
        </div>

        <!-- 10.2 Outlier Analysis Foundations -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">10.2 Outlier Analysis: Hawkins Definition & The 3 Classes</h3>
          <div class="analogy-box text-xs">
            <strong class="text-sky-300 block mb-0.5">💡 Hawkins (1980) Definition:</strong>
            <em>"An outlier is an observation which deviates so much from other observations as to arouse suspicions that it was generated by a different mechanism."</em>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-indigo-400 block mb-0.5">1. Global Outlier:</strong>
              Deviates significantly relative to the entire dataset (e.g. Bill Gates' net worth in an ordinary neighborhood income survey).
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-sky-400 block mb-0.5">2. Contextual Outlier:</strong>
              Deviates with respect to a context (e.g. 35&deg;C in Hyderabad in May is normal, but 35&deg;C in late December is a contextual anomaly).
            </div>
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-pink-400 block mb-0.5">3. Collective Outlier:</strong>
              A sequence of points that collectively deviate (e.g. flatline cardiac ECG for 3 seconds, where voltage values are normal individually).
            </div>
          </div>
        </div>

        <!-- 10.3 LOF Step-by-Step & Worked Example -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">10.3 Local Outlier Factor (LOF - Breunig et al. SIGMOD 2000)</h3>
          <div class="trap-box text-xs">
            <strong class="text-rose-300 block mb-1">⚠️ Why Distance-Based Detection ($k$-NN Distance) Fails:</strong>
            In datasets with <strong>clusters of different densities</strong>, legitimate inliers in a sparse cluster have larger Euclidean distance to their $k$-NN than genuine outliers floating outside a dense cluster! LOF fixes this by comparing <strong>relative local density ratios</strong>.
          </div>

          <div class="formula-box text-xs space-y-2">
            <div>
              <strong class="text-indigo-400">1. Reachability Distance:</strong>
              $$\text{reach-dist}_k(p, o) = \max\{d_k(o), d(p, o)\}$$
            </div>
            <div>
              <strong class="text-sky-400">2. Local Reachability Density ($\text{lrd}_k(p)$):</strong>
              $$\text{lrd}_k(p) = \frac{|N_k(p)|}{\sum_{o \in N_k(p)} \text{reach-dist}_k(p, o)}$$
            </div>
            <div>
              <strong class="text-emerald-400">3. Local Outlier Factor ($\text{LOF}_k(p)$):</strong>
              $$\text{LOF}_k(p) = \frac{\sum_{o \in N_k(p)} \frac{\text{lrd}_k(o)}{\text{lrd}_k(p)}}{|N_k(p)|}$$
              <p class="text-slate-400 mt-1">&bull; $\text{LOF} \approx 1.0$: Inlier (density matches neighbors). &bull; $\text{LOF} \gg 1.0$: Outlier (density is much lower than neighbors!).</p>
            </div>
          </div>

          <div class="example-box text-xs font-mono space-y-1">
            <strong class="text-emerald-300 block font-sans font-bold">Worked Numerical Example: 1D LOF Calculation ($k=2$)</strong>
            <p class="text-slate-200 font-sans">Points on 1D line: $A=0, B=1, C=2, P=6$. Compute $\text{LOF}_2(P)$.</p>
            &bull; $d_2(A)=2, N_2(A)=\{B,C\}$; $d_2(B)=1, N_2(B)=\{A,C\}$; $d_2(C)=2, N_2(C)=\{B,A\}$; $d_2(P)=5, N_2(P)=\{C,B\}$.<br/>
            &bull; $\text{reach-dist}_2(P, C) = \max\{d_2(C), d(P,C)\} = \max\{2, 4\} = 4$.<br/>
            &bull; $\text{reach-dist}_2(P, B) = \max\{d_2(B), d(P,B)\} = \max\{1, 5\} = 5$.<br/>
            &bull; $\text{lrd}_2(B) = \frac{2}{1+1} = 1.0$; $\text{lrd}_2(C) = \frac{2}{2+2} = 0.5$; $\text{lrd}_2(P) = \frac{2}{4+5} = \frac{2}{9} \approx 0.2222$.<br/>
            $$\text{LOF}_2(P) = \frac{\frac{\text{lrd}_2(C)}{\text{lrd}_2(P)} + \frac{\text{lrd}_2(B)}{\text{lrd}_2(P)}}{2} = \frac{\frac{0.5}{2/9} + \frac{1.0}{2/9}}{2} = \frac{2.25 + 4.5}{2} = \mathbf{3.375}$$
            Since $\text{LOF}_2(P) = 3.375 \gg 1.0$, $P$ is decisively identified as an outlier!
          </div>
        </div>

        <!-- 10.4 Trends in Data Mining -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">10.4 Emerging Trends in Data Mining</h3>
          <div class="space-y-2 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-indigo-400 block mb-0.5">1. Spatio-Temporal Trajectory Mining:</strong>
              <p class="text-slate-300">&bull; <strong>Tobler's First Law:</strong> "Near things are more related than distant things" (spatial autocorrelation breaks i.i.d. assumption!).</p>
              <p class="text-slate-300">&bull; <strong>Convoy vs Swarm:</strong> A <em>Convoy</em> requires $m$ objects to travel together for $k$ <strong>consecutive</strong> timestamps; a <em>Swarm</em> relaxes this to $k$ <strong>non-consecutive</strong> timestamps.</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5">
              <strong class="text-sky-400 block mb-0.5">2. High-Dimensional Empty Space Phenomenon:</strong>
              <p class="text-slate-300">&bull; <strong>Distance Concentration (Beyer et al. 1999):</strong> $\lim_{d\to\infty} \frac{d_{\max} - d_{\min}}{d_{\min}} = 0$. In high dimensions, every point becomes virtually equidistant from every other point!</p>
              <p class="text-slate-300">&bull; <strong>Empty Space:</strong> The volume of a hypersphere of radius $r$ inside a hypercube approaches 0 as $d \to \infty$. All mass concentrates in outer corners.</p>
            </div>
          </div>
        </div>
      </section>
"""
