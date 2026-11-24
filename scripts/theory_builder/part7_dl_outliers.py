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
            <h3 class="text-base font-bold text-amber-300">Mandated Textbook Worked Example 10.1 (Han §10.1, Book pp. 495–496 / PDF pp. 526–527)</h3>
            <span class="text-xs font-mono text-amber-400">"Practice the example"</span>
          </div>

          <div class="p-4 rounded bg-slate-900 border border-white/10 space-y-3 text-xs">
            <p class="text-slate-200">
              <strong>Given (Fig. 10.7 &amp; Table 10.1):</strong> 3 input nodes ($x_1=1, x_2=0, x_3=1$), 2 hidden nodes (Units 4, 5), 1 output node (Unit 6), target class label $T=1$, learning rate $\eta=0.9$. Initial weights &amp; biases: $w_{14}=0.2, w_{15}=-0.3, w_{24}=0.4, w_{25}=0.1, w_{34}=-0.5, w_{35}=0.2, w_{46}=-0.3, w_{56}=-0.2, b_4=-0.4, b_5=0.2, b_6=0.1$.
            </p>

            <div class="font-mono text-slate-300 space-y-1.5 bg-slate-950 p-3 rounded">
              <p><strong class="text-indigo-400 block mb-1">Step 1: Forward Propagation (Table 10.2)</strong></p>
              <p>&bull; Unit 4: $I_4 = 0.2(1) + 0.4(0) - 0.5(1) - 0.4 = -0.7 \implies O_4 = \frac{1}{1 + e^{0.7}} \approx \mathbf{0.332}$ (exact $0.3318$)</p>
              <p>&bull; Unit 5: $I_5 = -0.3(1) + 0.1(0) + 0.2(1) + 0.2 = +0.1 \implies O_5 = \frac{1}{1 + e^{-0.1}} \approx \mathbf{0.525}$ (exact $0.5250$)</p>
              <p>&bull; Unit 6: $I_6 = (-0.3)(0.332) + (-0.2)(0.525) + 0.1 = -0.105 \implies O_6 = \frac{1}{1 + e^{0.105}} \approx \mathbf{0.474}$ (exact $0.4739$)</p>

              <p><strong class="text-sky-400 block mt-2 mb-1">Step 2: Error Backpropagation (Table 10.3 — Exact Textbook Values)</strong></p>
              <p>&bull; Unit 6: $\delta_6 = O_6(1 - O_6)(T - O_6) = (0.474)(1 - 0.474)(1 - 0.474) = \mathbf{0.1311}$</p>
              <p>&bull; Unit 5: $\delta_5 = O_5(1 - O_5)\delta_6 w_{56} = (0.525)(1 - 0.525)(0.1311)(-0.2) = \mathbf{-0.0065}$</p>
              <p>&bull; Unit 4: $\delta_4 = O_4(1 - O_4)\delta_6 w_{46} = (0.332)(1 - 0.332)(0.1311)(-0.3) = \mathbf{-0.0087}$</p>

              <p><strong class="text-emerald-400 block mt-2 mb-1">Step 3: Weight &amp; Bias Updates (Table 10.4)</strong></p>
              <p>&bull; $w_{46}^{\text{new}} = -0.3 - (0.9)(0.1311)(0.332) = \mathbf{-0.339}$; &nbsp; $w_{56}^{\text{new}} = -0.2 - (0.9)(0.1311)(0.525) = \mathbf{-0.262}$</p>
              <p>&bull; $w_{14}^{\text{new}} = 0.2 - (0.9)(-0.0087)(1) = \mathbf{0.208}$; &nbsp; $w_{15}^{\text{new}} = -0.3 - (0.9)(-0.0065)(1) = \mathbf{-0.294}$</p>
              <p>&bull; $w_{24}^{\text{new}} = 0.4 - 0 = \mathbf{0.4}$; &nbsp; $w_{25}^{\text{new}} = 0.1 - 0 = \mathbf{0.1}$ (since $x_2 = 0$)</p>
              <p>&bull; $w_{34}^{\text{new}} = -0.5 - (0.9)(-0.0087)(1) = \mathbf{-0.492}$; &nbsp; $w_{35}^{\text{new}} = 0.2 - (0.9)(-0.0065)(1) = \mathbf{0.206}$</p>
              <p>&bull; $b_6^{\text{new}} = 0.1 - (0.9)(0.1311) = -0.0180$ (book misprints $-0.180$); &nbsp; $b_5^{\text{new}} = \mathbf{0.206}$; &nbsp; $b_4^{\text{new}} = \mathbf{-0.392}$.</p>
              <p class="text-amber-300 pt-1"><em>Book Errata Note:</em> Han 4th Ed. Table 10.3 computes $\delta_6 = +0.1311$ using $(T - O_6)$ while Table 10.4 subtracts $\eta \delta_j O_i$ (using Eq. 10.4 sign $\delta_6 = (O_6 - T)O_6(1-O_6) = -0.1311$ gives $w_{46}^{\text{new}} = -0.261$, moving $O_6$ closer to $T=1$).</p>
            </div>
          </div>
        </div>

        <!-- Textbook Ch 10 Summary -->
        <details class="surface-card p-4 text-xs">
          <summary class="font-bold text-indigo-300 flex items-center justify-between cursor-pointer">
            <span>📖 Textbook Chapter 10 Summary (Han §10.6 — Plain-English Walkthrough, §10.1 Focus)</span>
            <span class="toggle-icon text-indigo-400">&rarr;</span>
          </summary>
          <div class="mt-3 space-y-2 text-slate-300 border-t border-white/10 pt-2 leading-relaxed">
            <p class="text-slate-200 font-medium">Chapter 10 covers how neural networks learn layered features with backpropagation and scale to grids, sequences, and graphs. <em>(Endsem syllabus covers §10.1 only.)</em></p>
            <ul class="list-disc pl-5 space-y-1">
              <li><strong>Units, activations &amp; deep networks [Endsem §10.1]:</strong> A unit computes a linear weighted sum of inputs and passes it through a nonlinear activation like sign, sigmoid, or ReLU. Stacking layers creates a deep network that approximates nonlinear functions and learns feature hierarchies.</li>
              <li><strong>Multilayer feed-forward networks (MLPs) [Endsem §10.1]:</strong> An MLP stacks an input layer, one or more hidden layers, and an output layer, written cleanly in matrix form as a chain graph.</li>
              <li><strong>Backpropagation [Endsem §10.1]:</strong> Backpropagation uses gradient descent to adjust weights and biases, minimizing prediction loss by alternating forward propagation (inputs to outputs) and backward error propagation (outputs back to inputs).</li>
              <li><strong>[Beyond §10.1] Optimization &amp; generalization:</strong> Responsive ReLU activations and cross-entropy loss fight vanishing gradients; adaptive learning rates, dropout, and greedy pretraining improve convergence and test generalization.</li>
              <li><strong>[Beyond §10.1] CNNs, RNNs &amp; GNNs:</strong> CNNs model grid/image data via shared convolution kernels and pooling; RNNs/LSTMs model sequences via shared time weights and memory gates; GNNs/GCNs learn node embeddings over graphs.</li>
            </ul>
          </div>
        </details>
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
