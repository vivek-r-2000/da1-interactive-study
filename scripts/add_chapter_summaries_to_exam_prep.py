# -*- coding: utf-8 -*-
import os

EXAM_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Exam_Preparation', 'index.html'))

CH1_2_DETAILS = r"""
              <details class="mt-2 pt-2 border-t border-white/5 text-slate-300">
                <summary class="cursor-pointer font-semibold text-indigo-300 hover:text-indigo-200">📖 Textbook Chapter 1 &amp; 2 Summaries (Plain English)</summary>
                <div class="mt-2 space-y-2 text-[11px] leading-relaxed">
                  <div>
                    <strong class="text-white">Chapter 1 (§1.8):</strong> Data mining turns raw data into clear, useful patterns. The KDD process runs through cleaning, integration, selection, transformation, pattern discovery, evaluation, and presentation across structured, unstructured, stored, and stream data—covering characterization, associations, classification/regression, deep learning, clustering, and outlier detection while protecting privacy.
                  </div>
                  <div>
                    <strong class="text-white">Chapter 2 (§2.7):</strong> Good mining starts with attribute types (nominal, binary, ordinal, interval, ratio) and statistics (mean, median, mode, IQR, variance, SD, boxplots, Q-Q plots). Proximity metrics (Jaccard, Euclidean, Manhattan, Minkowski, supremum, cosine, Tanimoto, KL divergence) compare objects; cleaning, integration, normalization, discretization, and dimensionality reduction (PCA, subset selection, kernel PCA, t-SNE) prepare messy data.
                  </div>
                </div>
              </details>
"""

CH3_DETAILS = r"""
              <details class="mt-2 pt-2 border-t border-white/5 text-slate-300">
                <summary class="cursor-pointer font-semibold text-indigo-300 hover:text-indigo-200">📖 Textbook Chapter 3 Summary (Plain English)</summary>
                <div class="mt-2 space-y-1 text-[11px] leading-relaxed">
                  <p><strong class="text-white">Chapter 3 (§3.6):</strong> A data warehouse is subject-oriented, integrated, time-variant, and nonvolatile (separate from operational OLTP DBs), built on a three-tier architecture with ETL tools and metadata. Data lakes store raw and transformed data across layered zones. Multidimensional star, snowflake, and fact constellation schemas form a cuboid lattice explored via roll-up, drill-down, drill-across, drill-through, slice-and-dice, and pivot over ROLAP, MOLAP, or HOLAP servers, accelerated by bitmap/join indexes, columnar storage, and partial materialization (such as BUC).</p>
                </div>
              </details>
"""

CH4_5_DETAILS = r"""
              <details class="mt-2 pt-2 border-t border-white/5 text-slate-300">
                <summary class="cursor-pointer font-semibold text-indigo-300 hover:text-indigo-200">📖 Textbook Chapter 4 &amp; 5 Summaries (Plain English)</summary>
                <div class="mt-2 space-y-2 text-[11px] leading-relaxed">
                  <div>
                    <strong class="text-white">Chapter 4 (§4.4):</strong> Association mining finds frequent itemsets (min support) and strong rules (min confidence) across three algorithm families: Apriori (level-wise downward closure), FP-growth (candidate-free FP-tree), and Eclat (vertical TID_set intersections). Because support/confidence alone can mislead, null-invariant measures—especially Kulczynski paired with Imbalance Ratio—evaluate true correlation.
                  </div>
                  <div>
                    <strong class="text-white">Chapter 5 (§5.7 — Endsem §5.1 Focus):</strong> Expands beyond basic itemsets to multilevel, multidimensional, quantitative, rare, and negative patterns (§5.1), plus constraint-based pruning, high-dimensional row-enumeration/Pattern-Fusion, compressed top-$k$ patterns, sequential mining (GSP, SPADE, PrefixSpan, CloSpan), subgraph mining (AGM, FSG, gSpan, CloseGraph), and text/software tools (ToPMine, SegPhrase, AutoPhrase, CP-Miner).
                  </div>
                </div>
              </details>
"""

CH6_7_DETAILS = r"""
              <details class="mt-2 pt-2 border-t border-white/5 text-slate-300">
                <summary class="cursor-pointer font-semibold text-indigo-300 hover:text-indigo-200">📖 Textbook Chapter 6 &amp; 7 Summaries (Plain English)</summary>
                <div class="mt-2 space-y-2 text-[11px] leading-relaxed">
                  <div>
                    <strong class="text-white">Chapter 6 (§6.8):</strong> Classification predicts categorical labels (vs continuous regression). Eager learners (ID3/C4.5/CART decision trees, Naive Bayes, Perceptron, logistic regression) build global models before testing, while lazy learners (k-NN, CBR) generalize at query time. Confusion matrices (accuracy, sensitivity, specificity, precision, $F_\beta$), cross-validation, $t$-tests, ROC curves, ensembles (bagging, boosting, random forests), and imbalance handling evaluate and improve models.
                  </div>
                  <div>
                    <strong class="text-white">Chapter 7 (§7.8 — Endsem §7.1, 7.2.1, 7.3, 7.5, 7.6, 7.7.1, 7.7.3):</strong> Adds Bayesian belief networks (BBNs) for subset conditional independencies, SVMs (higher-dimensional hyperplanes + support vectors) extended to multiclass ensembles/error-correcting codes, and scarce-label learning (semisupervised self-training/cotraining, active learning, distant supervision, transfer learning TrAdaBoost, zero-shot learning)—alongside rule-based/genetic/pattern classifiers, metric learning, LIME, streams, and RL.
                  </div>
                </div>
              </details>
"""

CH8_DETAILS = r"""
              <details class="mt-2 pt-2 border-t border-white/5 text-slate-300">
                <summary class="cursor-pointer font-semibold text-indigo-300 hover:text-indigo-200">📖 Textbook Chapter 8 Summary (Plain English)</summary>
                <div class="mt-2 space-y-1 text-[11px] leading-relaxed">
                  <p><strong class="text-white">Chapter 8 (§8.6):</strong> Clustering groups similar objects without labels across partitioning, hierarchical, density-based, and grid-based families. Partitioning covers k-means (minimizing SSE), outlier-resistant k-medoids, nominal k-modes, and nonlinear kernel k-means. Hierarchical clustering builds dendrograms bottom-up (single, complete, mean, average linkage) or top-down (MST), alongside BIRCH (CF-tree), probabilistic hierarchical clustering, and density-based clustering (DBSCAN).</p>
                </div>
              </details>
"""

CH10_DETAILS = r"""
              <details class="mt-2 pt-2 border-t border-white/5 text-slate-300">
                <summary class="cursor-pointer font-semibold text-indigo-300 hover:text-indigo-200">📖 Textbook Chapter 10 Summary (Plain English — §10.1 Focus)</summary>
                <div class="mt-2 space-y-1 text-[11px] leading-relaxed">
                  <p><strong class="text-white">Chapter 10 (§10.6):</strong> <em>[Endsem §10.1]</em> Neural units compute a weighted sum plus nonlinear activation (sign, sigmoid, ReLU); stacking layers forms MLPs (chain graphs) trained via backpropagation gradient descent alternating forward and backward passes. <em>[Beyond §10.1]</em> ReLU, cross-entropy, adaptive learning rates, dropout, and pretraining speed training, while CNNs, RNNs/LSTMs, and GNNs/GCNs handle grids, sequences, and graphs.</p>
                </div>
              </details>
"""

def inject_after(content, anchor, addition):
    if addition.strip()[:40] in content:
        return content
    idx = content.index(anchor) + len(anchor)
    return content[:idx] + addition + content[idx:]

def main():
    with open(EXAM_PATH, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    content = inject_after(
        content,
        "data normalization (Min-max, z-score, decimal scaling), and discretization.\n\n              </p>",
        CH1_2_DETAILS
    )
    content = inject_after(
        content,
        "cardinality sorting heuristic.\n\n              </p>",
        CH3_DETAILS
    )
    content = inject_after(
        content,
        "Two-Phase High Utility Itemsets (Liu et al. '05).\n\n              </p>",
        CH4_5_DETAILS
    )
    content = inject_after(
        content,
        "k-NN lazy learner, Weak & Semi-supervised learning.\n\n              </p>",
        CH6_7_DETAILS
    )
    content = inject_after(
        content,
        "CHAMELEON dynamic modeling (Karypis et al. '99).\n\n              </p>",
        CH8_DETAILS
    )
    content = inject_after(
        content,
        "and Trends in Data Mining.\n\n              </p>",
        CH10_DETAILS
    )

    with open(EXAM_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added all 9 chapter summaries to Exam_Preparation/index.html #tab-syllabus.")

if __name__ == '__main__':
    main()
