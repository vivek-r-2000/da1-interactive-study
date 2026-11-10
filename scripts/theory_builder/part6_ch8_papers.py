# -*- coding: utf-8 -*-

part6_html = r"""
      <!-- ==========================================
           TOPIC 8: CHAPTER 8 CLUSTER ANALYSIS & 4 PAPERS
      ========================================== -->
      <section id="topic-8" class="theory-section space-y-6 scroll-mt-24">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div>
            <span class="text-xs font-mono text-amber-400 uppercase tracking-wider font-semibold">Topic 8 &bull; Han Chapter 8 + 4 Research Papers</span>
            <h2 class="text-xl sm:text-2xl font-bold text-white">Chapter 8: Cluster Analysis & 4 Mandated Papers</h2>
          </div>
          <span class="text-xs font-mono px-2 py-1 rounded bg-slate-800 text-slate-300 border border-white/10">~22 min read</span>
        </div>

        <div class="tldr-box text-xs">
          <strong class="text-indigo-300 block mb-1">📌 TL;DR:</strong>
          Clustering partitions unlabeled data into natural groups maximizing intra-cluster similarity and minimizing inter-cluster similarity. Covers Partitioning (K-Means/PAM), Hierarchical (AGNES/DIANA/Linkages), Density-based (DBSCAN), Grid-based (STING/CLIQUE), Silhouette validation, and 4 mandated papers: CLARANS, BIRCH, DBSCAN, and CHAMELEON.
        </div>

        <!-- 8.1 Partitioning Methods -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">8.1 Partitioning Algorithms: K-Means vs PAM (K-Medoids)</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-indigo-400 block mb-1">K-Means (MacQueen 1967):</strong>
              <p>&bull; <strong>Objective:</strong> Minimize Within-Cluster Sum of Squares (SSE):</p>
              $$\text{SSE} = \sum_{k=1}^K \sum_{\mathbf{x} \in C_k} \|\mathbf{x} - \mathbf{m}_k\|^2$$
              <p>&bull; <strong>Algorithm:</strong> 1. Pick $k$ random centroids $\mathbf{m}_k$; 2. Assign each point to closest centroid; 3. Recompute centroid as mean of points; 4. Repeat until convergence.</p>
              <p class="text-rose-400 mt-1 font-semibold">⚠️ Exam Weaknesses: Sensitive to outliers (a single extreme point pulls the mean away); cannot discover non-spherical clusters; requires pre-specifying $k$.</p>
            </div>

            <div class="p-3 rounded bg-slate-900 border border-white/5 space-y-1">
              <strong class="text-sky-400 block mb-1">PAM (Partitioning Around Medoids - Kaufman & Rousseeuw):</strong>
              <p>&bull; <strong>Objective:</strong> Uses <em>actual representative objects</em> (medoids) instead of artificial centroids.</p>
              <p>&bull; <strong>Algorithm:</strong> Iteratively swaps a medoid $o_i$ with a non-medoid $o_h$ if the total swapping cost $TC_{ih} < 0$.</p>
              <p>&bull; <strong>Advantage:</strong> Extremely robust to noise and outliers!</p>
              <p>&bull; <strong>Complexity:</strong> $O(k(n-k)^2)$ per iteration. Infeasible for large datasets ($n > 1000$) $\implies$ solved by CLARA (sampling) and CLARANS (randomized graph search).</p>
            </div>
          </div>
        </div>

        <!-- 8.2 Hierarchical Linkages -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">8.2 Hierarchical Linkage Criteria (AGNES)</h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <strong class="text-emerald-400 block mb-0.5">1. Single Link (MIN):</strong>
              $$d(A, B) = \min_{\mathbf{p} \in A, \mathbf{q} \in B} d(\mathbf{p}, \mathbf{q})$$
              <p class="text-slate-300">Can handle non-elliptical shapes. <em>Fatal weakness:</em> <strong>Chaining effect</strong> (noisy noise points act as bridges merging separate clusters!).</p>
            </div>

            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <strong class="text-pink-400 block mb-0.5">2. Complete Link (MAX):</strong>
              $$d(A, B) = \max_{\mathbf{p} \in A, \mathbf{q} \in B} d(\mathbf{p}, \mathbf{q})$$
              <p class="text-slate-300">Produces tight, compact spherical clusters; avoids chaining. <em>Weakness:</em> Highly sensitive to outliers.</p>
            </div>

            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <strong class="text-amber-400 block mb-0.5">3. Average Link (Mean):</strong>
              $$d(A, B) = \frac{1}{|A||B|} \sum_{\mathbf{p} \in A} \sum_{\mathbf{q} \in B} d(\mathbf{p}, \mathbf{q})$$
              <p class="text-slate-300">Robust compromise between single and complete link; less sensitive to noise.</p>
            </div>

            <div class="p-2.5 rounded bg-slate-900 border border-white/5">
              <strong class="text-purple-400 block mb-0.5">4. Ward's Method:</strong>
              $$\Delta ESS(A, B) = \frac{|A||B|}{|A| + |B|} \|\mathbf{m}_A - \mathbf{m}_B\|^2$$
              <p class="text-slate-300">Merges clusters minimizing the increase in total within-cluster variance.</p>
            </div>
          </div>
        </div>

        <!-- 8.3 Silhouette Validation -->
        <div class="surface-card p-5 space-y-3">
          <h3 class="text-base font-bold text-slate-100">8.3 Cluster Validation: The Silhouette Coefficient</h3>
          <div class="formula-box text-xs space-y-1.5">
            <p class="text-slate-300">For each object $i$, define:</p>
            <p>&bull; $a(i)$: Average dissimilarity of $i$ to all other objects in its <strong>own cluster</strong> (cohesion).</p>
            <p>&bull; $b(i)$: Minimum average dissimilarity of $i$ to all objects in any <strong>other cluster</strong> (separation).</p>
            $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad -1 \le s(i) \le +1$$
            <div class="pt-2 border-t border-white/10 text-slate-400 space-y-0.5">
              <p>&bull; $s(i) \approx +1$: Point is tightly clustered with its peers and far from other clusters (&check; Excellent!).</p>
              <p>&bull; $s(i) \approx 0$: Point lies on the border between two clusters.</p>
              <p>&bull; $s(i) \approx -1$: Point has been misclassified into the wrong cluster!</p>
            </div>
          </div>
        </div>

        <!-- 8.4 THE 4 MANDATED CLUSTERING RESEARCH PAPERS -->
        <div class="surface-elevated p-5 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-amber-300">The 4 Mandated Clustering Research Papers</h3>
            <span class="text-xs font-mono text-amber-400">CLARANS, BIRCH, DBSCAN, CHAMELEON</span>
          </div>

          <!-- Paper 4: CLARANS -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Paper 4: CLARANS: A Method for Clustering Objects for Spatial Data Mining (Ng & Han 1994)</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Core Innovation:</strong> Views the medoid clustering search space as an abstract graph $G_n^k$, where each vertex is a set of $k$ medoids, and two vertices are connected if they differ by exactly 1 medoid.</p>
              <ul class="list-disc ml-5 space-y-1">
                <li><strong>PAM</strong> checks all $k(n-k)$ neighbors (exhaustive local search &rarr; slow).</li>
                <li><strong>CLARA</strong> draws multiple small samples of size $40 + 2k$ and runs PAM (biased toward sample).</li>
                <li><strong>CLARANS (Randomized Search):</strong> Explores the full graph dynamically by inspecting at most <code>maxneighbor</code> randomly chosen neighbors. If an improvement is found, move to that vertex. If no improvement is found in <code>maxneighbor</code> checks, record local minimum and restart with a fresh random vertex up to <code>numlocal</code> times!</li>
                <li><strong>Result:</strong> Superior quality over CLARA with significantly faster runtime than PAM.</li>
              </ul>
            </div>
          </details>

          <!-- Paper 5: BIRCH -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Paper 5: BIRCH: An Efficient Data Clustering Method for Very Large Databases (Zhang et al. 1996)</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Core Innovation:</strong> Overcomes I/O bottlenecks by summarizing dense clusters into in-memory <strong>Clustering Feature (CF) vectors</strong> stored in a height-balanced <strong>CF-Tree</strong>.</p>
              <div class="font-mono bg-slate-950 p-2.5 rounded my-1">
                $$CF = (N, \vec{LS}, SS)$$
                &bull; $N$: Number of data points.<br/>
                &bull; $\vec{LS} = \sum_{i=1}^N \mathbf{x}_i$: Linear sum of $N$ points.<br/>
                &bull; $SS = \sum_{i=1}^N \mathbf{x}_i^2$: Square sum of $N$ points.<br/>
                &bull; <strong>CF Additivity Property:</strong> If cluster $C_1$ has $CF_1$ and $C_2$ has $CF_2$, the merged cluster $C_1 \cup C_2$ has $CF = CF_1 + CF_2 = (N_1 + N_2, \vec{LS}_1 + \vec{LS}_2, SS_1 + SS_2)$ without needing raw points!
              </div>
              <p><strong>4-Phase Architecture:</strong> Phase 1: Build in-memory CF-tree; Phase 2: Condense tree; Phase 3: Run global clustering (e.g. agglomerative) on leaf entries; Phase 4: Reassign raw data tuples.</p>
            </div>
          </details>

          <!-- Paper 6: DBSCAN -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Paper 6: DBSCAN: A Density-Based Algorithm for Discovering Clusters (Ester et al. 1996)</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Core Innovation:</strong> Discovers clusters of arbitrary non-spherical shapes (e.g. rings, S-shapes) and isolates noise points without requiring $k$ in advance.</p>
              <div class="space-y-1.5 font-mono text-slate-200 bg-slate-950 p-2.5 rounded">
                &bull; <strong>$\epsilon$-Neighborhood:</strong> $N_\epsilon(p) = \{q \in D \mid \text{dist}(p, q) \le \epsilon\}$.<br/>
                &bull; <strong>Core Point:</strong> Point $p$ having $|N_\epsilon(p)| \ge MinPts$.<br/>
                &bull; <strong>Border Point:</strong> Not a core point, but falls inside the $\epsilon$-neighborhood of a core point.<br/>
                &bull; <strong>Noise Point:</strong> Neither a core nor a border point.<br/>
                &bull; <strong>Directly Density-Reachable:</strong> Point $q$ is directly density-reachable from $p$ if $p$ is a core point and $q \in N_\epsilon(p)$.<br/>
                &bull; <strong>Density-Reachable:</strong> Chain of directly reachable core points $p_1 \to p_2 \to \dots \to q$. (Transitive, but asymmetric!).<br/>
                &bull; <strong>Density-Connected:</strong> Both $p$ and $q$ are density-reachable from a common core point $o$. (Symmetric and reflexive).
              </div>
            </div>
          </details>

          <!-- Paper 7: CHAMELEON -->
          <details class="p-3 rounded bg-slate-900 border border-white/5 text-xs">
            <summary class="font-bold text-slate-200 flex items-center justify-between">
              <span>Paper 7: CHAMELEON: A Hierarchical Clustering Algorithm Using Dynamic Modeling (Karypis et al. 1999)</span>
              <span class="toggle-icon text-indigo-400">&rarr;</span>
            </summary>
            <div class="mt-3 space-y-2 text-slate-300 border-t border-white/5 pt-2">
              <p><strong>Core Innovation:</strong> Dynamic modeling of cluster similarity that adapts to the internal characteristics of the clusters being merged (unlike CURE or ROCK which use static models).</p>
              <div class="space-y-1 font-mono text-slate-200 bg-slate-950 p-2.5 rounded">
                &bull; <strong>Phase 1:</strong> Construct a $k$-NN graph from data points and partition it into thousands of small, highly cohesive subclusters using a multilevel graph partitioning algorithm (hMETIS).<br/>
                &bull; <strong>Phase 2:</strong> Agglomerative merging of subclusters based on two dynamic metrics:<br/>
                &nbsp;&nbsp;1. <strong>Relative Interconnectivity ($RI$):</strong> Ratio of edge-cut between clusters $C_i, C_j$ to internal edge-cuts within $C_i$ and $C_j$:
                $$RI(C_i, C_j) = \frac{2 |EC_{\{C_i, C_j\}}|}{|EC_{C_i}| + |EC_{C_j}|}$$
                &nbsp;&nbsp;2. <strong>Relative Closeness ($RC$):</strong> Ratio of average weight of crossing edges to internal average edge weights:
                $$RC(C_i, C_j) = \frac{\bar{S}_{EC_{\{C_i, C_j\}}}}{\frac{|C_i|}{|C_i|+|C_j|}\bar{S}_{EC_{C_i}} + \frac{|C_j|}{|C_i|+|C_j|}\bar{S}_{EC_{C_j}}}$$
                &bull; <strong>Decision Rule:</strong> Merge subclusters only if <em>both</em> $RI$ and $RC$ are high ($RI \times RC^\alpha \ge \text{threshold}$).
              </div>
            </div>
          </details>
        </div>
      </section>
"""
