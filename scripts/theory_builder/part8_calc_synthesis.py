# -*- coding: utf-8 -*-

part8_html = r"""
      <!-- ==========================================
           TOPIC 11: SCIENTIFIC CALCULATOR GUIDE
      ========================================== -->
      <section id="topic-11" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-semibold">Topic 11 &bull; Operational Tooling</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Scientific Calculator Master Operational Guide</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~6 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 Official Notice:</strong>
          Scientific calculators are <strong>explicitly allowed</strong> in the Endsem examination. Below are the exact keystroke combinations for Casio fx-991ES / fx-991EX calculators to compute logarithms, exponentials, statistics, and combinations in seconds.
        </div>

        <div class="surface-card p-5 space-y-3">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-2">
              <strong class="text-indigo-400 block font-bold">1. Logarithm Base 2 ($\log_2(x)$ for Entropy/Gini):</strong>
              <p class="text-slate-300 font-mono">&bull; Method A (Direct): Press <code>[log_&#9633;(&#9633;)]</code> &rarr; Base <code>2</code> &rarr; Value <code>x</code>.</p>
              <p class="text-slate-300 font-mono">&bull; Method B (Change of base): <code>[log] (x) &divide; [log] (2)</code> or <code>[ln] (x) &divide; [ln] (2)</code>.</p>
              <p class="text-slate-400"><em>Shortcut:</em> Precompute $\ln(2) \approx 0.693147$. Divide $\ln(x)$ by $0.693147$.</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-2">
              <strong class="text-sky-400 block font-bold">2. Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$ (Deep Learning):</strong>
              <p class="text-slate-300 font-mono">&bull; Keystrokes: <code>1 &divide; ( 1 + [SHIFT] [ln] ( - z ) )</code></p>
              <p class="text-slate-400"><em>Example:</em> For $z=0.3775$: <code>1 &divide; (1 + e^(-0.3775)) = 0.59327</code>.</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-2">
              <strong class="text-emerald-400 block font-bold">3. Sample Mean ($\bar{x}$) and Standard Deviation ($s$):</strong>
              <p class="text-slate-300 font-mono">&bull; Setup: <code>[MODE] &rarr; 3 (STAT) &rarr; 1 (1-VAR)</code>.</p>
              <p class="text-slate-300 font-mono">&bull; Enter all numbers pressing <code>[=]</code> after each value &rarr; Press <code>[AC]</code>.</p>
              <p class="text-slate-300 font-mono">&bull; Extract: <code>[SHIFT] &rarr; 1 (STAT) &rarr; 4 (Var) &rarr; 2 (x&#772;)</code> for mean; <code>4 (s_x)</code> for sample std dev!</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-2">
              <strong class="text-amber-400 block font-bold">4. Combinations ($_nC_r$ for Candidate Tuples & Itemsets):</strong>
              <p class="text-slate-300 font-mono">&bull; Keystrokes: <code>n [SHIFT] [&divide;] r [=]</code>.</p>
              <p class="text-slate-400"><em>Example:</em> Finding 2-itemsets from 10 items: <code>10 [SHIFT] [&divide;] 2 = 45</code>.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- ==========================================
           TOPIC 12: CROSS-CHAPTER SYNTHESIS
      ========================================== -->
      <section id="topic-12" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-purple-400 uppercase tracking-wider font-semibold">Topic 12 &bull; Synthesis</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Cross-Chapter Integration & Synthesis Questions</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~12 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 Prof. Reddy's Crucial Warning:</strong>
          <em>"Questions may be given by connecting the topics discussed in several chapters."</em> Below are the 4 primary cross-chapter synthesis paradigms that connect patterns, classification, clustering, warehousing, and outlier analysis.
        </div>

        <div class="space-y-4 text-xs">
          <!-- Synthesis 1 -->
          <div class="surface-card p-4 space-y-2">
            <h3 class="font-bold text-indigo-300 text-sm">Synthesis 1: Pruning Principles Across the Course (Apriori vs BUC vs CLIQUE)</h3>
            <p class="text-slate-300 leading-relaxed">
              Notice how the exact same anti-monotonicity mathematical principle governs three different chapters:
            </p>
            <ul class="list-disc ml-5 space-y-1 text-slate-300">
              <li><strong>Pattern Mining (Apriori):</strong> If an itemset is infrequent, all its supersets are guaranteed infrequent. Prunes candidate itemsets.</li>
              <li><strong>Data Warehousing (BUC):</strong> If an aggregate cell count falls below <code>min_sup</code>, none of its descendant cuboid cells can meet <code>min_sup</code>. Prunes recursive lattice branches.</li>
              <li><strong>Clustering (CLIQUE):</strong> If a $k$-dimensional subspace unit is not dense, no $(k+1)$-dimensional projection can be dense. Prunes high-dimensional candidate clusters.</li>
            </ul>
          </div>

          <!-- Synthesis 2 -->
          <div class="surface-card p-4 space-y-2">
            <h3 class="font-bold text-sky-300 text-sm">Synthesis 2: Comparative Analysis of All 4 Linear Classifiers</h3>
            <div class="overflow-x-auto">
              <table class="w-full border border-white/10 text-left">
                <thead class="bg-slate-900 text-slate-200">
                  <tr>
                    <th class="p-2 border-b border-white/10">Classifier</th>
                    <th class="p-2 border-b border-white/10">Decision Boundary</th>
                    <th class="p-2 border-b border-white/10">Loss Function</th>
                    <th class="p-2 border-b border-white/10">Optimization & Uniqueness</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-white/5 text-slate-300 font-mono">
                  <tr>
                    <td class="p-2 font-bold text-indigo-400">Single Perceptron</td>
                    <td class="p-2">Linear Hyperplane</td>
                    <td class="p-2">Perceptron Loss</td>
                    <td class="p-2">Non-unique; order dependent.</td>
                  </tr>
                  <tr>
                    <td class="p-2 font-bold text-sky-400">Logistic Regression</td>
                    <td class="p-2">Linear Hyperplane</td>
                    <td class="p-2">Cross-Entropy (Log Loss)</td>
                    <td class="p-2">Unique globally optimal MLE solution.</td>
                  </tr>
                  <tr>
                    <td class="p-2 font-bold text-emerald-400">Linear SVM</td>
                    <td class="p-2">Maximum Margin (MMH)</td>
                    <td class="p-2">Hinge Loss</td>
                    <td class="p-2">Unique quadratic program; depends only on Support Vectors.</td>
                  </tr>
                  <tr>
                    <td class="p-2 font-bold text-purple-400">Multi-Layer Perceptron</td>
                    <td class="p-2">Non-Linear Manifold</td>
                    <td class="p-2">Cross-Entropy or MSE</td>
                    <td class="p-2">Non-convex gradient descent via Backprop.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Synthesis 3 -->
          <div class="surface-card p-4 space-y-2">
            <h3 class="font-bold text-emerald-300 text-sm">Synthesis 3: How Clustering Algorithms Act as Outlier Detectors</h3>
            <ul class="list-disc ml-5 space-y-1 text-slate-300">
              <li><strong>K-Means Centroid Distance:</strong> An object whose Euclidean distance to its closest centroid $\|\mathbf{x} - \mathbf{m}_k\|$ exceeds a statistical threshold (e.g. $3\sigma$) is flagged as a cluster outlier.</li>
              <li><strong>DBSCAN Noise Cluster:</strong> All points that fail to meet $MinPts$ density reachability are assigned directly to noise cluster $-1$.</li>
              <li><strong>LOF (Density Ratio):</strong> Compares local reachability density against neighbors to identify local anomalies without distorting multi-density structures.</li>
            </ul>
          </div>

          <!-- Synthesis 4 -->
          <div class="surface-card p-4 space-y-2">
            <h3 class="font-bold text-amber-300 text-sm">Synthesis 4: Associative Classification (Mining Rules for Classification)</h3>
            <p class="text-slate-300 leading-relaxed">
              In traditional classification, decision trees greedily split one attribute at a time. In <strong>Associative Classification</strong> (e.g. CBA - Classification Based on Associations), we run Apriori to discover high-confidence association rules where the rule consequent is strictly a class label:
              $$A_1 \land A_2 \land \dots \land A_k \implies Class = C_i$$
              Then we sort rules by confidence and support to build a rule-based classifier that considers multi-attribute correlations simultaneously!
            </p>
          </div>
        </div>
      </section>

    </main>
  </div>

  <!-- FOOTER -->
  <footer class="border-t border-white/10 mt-16 py-8 text-center text-xs text-slate-500">
    <p>CS4.405 Data Analytics I &bull; Prof. P. Krishna Reddy &bull; IIIT Hyderabad</p>
    <p class="mt-1">Endsem Master Theory Blueprint &bull; Unified Single-Destination Study Compendium</p>
  </footer>

  <!-- CLIENT-SIDE SCRIPT: PROGRESS, SEARCH, AND INTERSECTION OBSERVER -->
  <script>
    // Reading Progress Bar
    window.addEventListener('scroll', () => {
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrolled = (window.scrollY / docHeight) * 100;
      const bar = document.getElementById('read-progress-bar');
      if (bar) bar.style.width = scrolled + '%';
    });

    // Active TOC Highlight via Intersection Observer
    const sections = document.querySelectorAll('.theory-section');
    const navItems = document.querySelectorAll('.sticky-nav-item');

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navItems.forEach(item => {
            if (item.getAttribute('href') === '#' + id) {
              item.classList.add('active');
            } else {
              item.classList.remove('active');
            }
          });
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px' });

    sections.forEach(s => observer.observe(s));

    // Live Filter & Search
    function filterTheoryTopics() {
      const query = document.getElementById('theory-search-input').value.trim().toLowerCase();
      if (!query) {
        sections.forEach(s => s.style.display = 'block');
        return;
      }
      sections.forEach(s => {
        const text = s.innerText.toLowerCase();
        if (text.includes(query)) {
          s.style.display = 'block';
        } else {
          s.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
"""
