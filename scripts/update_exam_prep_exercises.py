# -*- coding: utf-8 -*-
import os

EXAM_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Exam_Preparation', 'index.html'))

NEW_EXERCISES_AND_DL_HTML = r"""          <!-- Exercise 2.2 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch2">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 2.2 — Central Tendency, Quartiles &amp; Boxplot (Book p. 80 / PDF p. 111)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 2: Data &amp; Preprocessing</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> Suppose that the data for analysis include the attribute <em>age</em>. The <em>age</em> values for the data tuples are (in ascending order): <code>13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70</code>. (a) What is the <em>mean</em> of the data? What is the <em>median</em>? (b) What is the <em>mode</em> of the data? Comment on the data's modality. (c) What is the <em>midrange</em> of the data? (d) Can you find (roughly) the first quartile ($Q_1$) and third quartile ($Q_3$)? (e) Give the <em>five-number summary</em>. (f) Show a <em>boxplot</em> of the data.
            </div>
            <div class="text-xs text-slate-400 space-y-1.5 border-t border-white/5 pt-3">
              <p><strong>Verified Solution ($N = 27$):</strong></p>
              <ul class="list-disc pl-5 space-y-1">
                <li><strong>(a) Mean &amp; Median:</strong> $\sum x_i = 809 \implies \bar{x} = \frac{809}{27} \approx \mathbf{29.9630}$. Since $N=27$ is odd, median position is $\frac{27+1}{2}=14 \implies \text{Median} = x_{(14)} = \mathbf{25}$.</li>
                <li><strong>(b) Mode &amp; Modality:</strong> Both $25$ and $35$ occur $4$ times (max frequency). Hence the dataset is <strong>bimodal</strong> (modes: $25, 35$).</li>
                <li><strong>(c) Midrange:</strong> $\frac{\min + \max}{2} = \frac{13 + 70}{2} = \mathbf{41.5}$.</li>
                <li><strong>(d) Quartiles ($Q_1, Q_3$):</strong> Splitting at median $x_{(14)}=25$ leaves $13$ items in lower half (middle $7$th item is $Q_1 = \mathbf{20}$) and $13$ items in upper half ($15$th–$27$th; middle $21$st item is $Q_3 = \mathbf{35}$).</li>
                <li><strong>(e) Five-Number Summary:</strong> $[\min, Q_1, \text{median}, Q_3, \max] = \mathbf{[13, 20, 25, 35, 70]}$.</li>
                <li><strong>(f) Boxplot &amp; Fences:</strong> $\text{IQR} = Q_3 - Q_1 = 35 - 20 = 15$. Upper fence $= Q_3 + 1.5\cdot\text{IQR} = 35 + 22.5 = 57.5$; lower fence $= 20 - 22.5 = -2.5$. Since $70 \gt 57.5$, <strong>$70$ is an outlier</strong> (plotted individually); lower whisker $= 13$, box $= [20, 35]$ (median $25$), upper whisker $= \mathbf{52}$.</li>
              </ul>
            </div>
          </div>

          <!-- Exercise 2.7 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch2">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 2.7 — Age &amp; Body Fat: Stats, Boxplots, Scatter &amp; Q-Q Plot (Book p. 81 / PDF p. 112)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 2: Data &amp; Preprocessing</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> Suppose that a hospital tested the <em>age</em> and <em>body fat</em> data for 18 randomly selected adults ($n=18$): (a) Calculate the mean, median, and standard deviation of <em>age</em> and <em>%fat</em>. (b) Draw the boxplots for <em>age</em> and <em>%fat</em>. (c) Draw a <em>scatter plot</em> and a <em>q-q plot</em> based on these two variables.
              <div class="overflow-x-auto my-2">
                <table class="w-full text-[11px] font-mono text-center border border-white/10">
                  <tr class="bg-slate-800 text-indigo-300"><td class="p-1 border border-white/10">age</td><td>23</td><td>23</td><td>27</td><td>27</td><td>39</td><td>41</td><td>47</td><td>49</td><td>50</td></tr>
                  <tr><td class="bg-slate-800 text-sky-300 p-1 border border-white/10">%fat</td><td>9.5</td><td>26.5</td><td>7.8</td><td>17.8</td><td>31.4</td><td>25.9</td><td>27.4</td><td>27.2</td><td>31.2</td></tr>
                  <tr class="bg-slate-800 text-indigo-300"><td class="p-1 border border-white/10">age</td><td>52</td><td>54</td><td>54</td><td>56</td><td>57</td><td>58</td><td>58</td><td>60</td><td>61</td></tr>
                  <tr><td class="bg-slate-800 text-sky-300 p-1 border border-white/10">%fat</td><td>34.6</td><td>42.5</td><td>28.8</td><td>33.4</td><td>30.2</td><td>34.1</td><td>32.9</td><td>41.2</td><td>35.7</td></tr>
                </table>
              </div>
            </div>
            <div class="text-xs text-slate-400 space-y-2 border-t border-white/5 pt-3">
              <div>
                <strong>(a) Summary Statistics (Han Eq. 2.6 population $\sigma$; sample $s$ with $\div 17$ in parentheses):</strong>
                <ul class="list-disc pl-5 mt-1 space-y-1">
                  <li><strong>age:</strong> $\sum x_i = 836 \implies \bar{x} = \frac{836}{18} \approx \mathbf{46.4444}$. Median $= \frac{x_{(9)} + x_{(10)}}{2} = \frac{50+52}{2} = \mathbf{51.0}$. $\sigma_{\text{age}} = \sqrt{\frac{2970.4444}{18}} \approx \mathbf{12.8462}$ ($s = 13.2186$).</li>
                  <li><strong>%fat (sorted):</strong> <code>7.8, 9.5, 17.8, 25.9, 26.5, 27.2, 27.4, 28.8, 30.2, 31.2, 31.4, 32.9, 33.4, 34.1, 34.6, 35.7, 41.2, 42.5</code>. $\sum y_i = 518.1 \implies \bar{y} = \frac{518.1}{18} \approx \mathbf{28.7833}$. Median $= \frac{30.2+31.2}{2} = \mathbf{30.7}$. $\sigma_{\text{\%fat}} = \sqrt{\frac{1455.9450}{18}} \approx \mathbf{8.9937}$ ($s = 9.2544$).</li>
                </ul>
              </div>
              <div>
                <strong>(b) Boxplots ($n=18 \implies$ lower 9 median = 5th sorted, upper 9 median = 14th sorted):</strong>
                <ul class="list-disc pl-5 mt-1 space-y-1">
                  <li><strong>age:</strong> $[\min, Q_1, \text{Med}, Q_3, \max] = [23, 39, 51, 57, 61]$, $\text{IQR} = 18$, fences $[12, 84] \implies$ no outliers; whiskers $23$ and $61$.</li>
                  <li><strong>%fat:</strong> $[7.8, 26.5, 30.7, 34.1, 42.5]$, $\text{IQR} = 7.6$, fences $[15.1, 45.5] \implies \mathbf{7.8, 9.5}$ are outliers ($\lt 15.1$); lower whisker $= 17.8$, upper whisker $= 42.5$.</li>
                </ul>
              </div>
              <div>
                <strong>(c) Scatter Plot &amp; Q-Q Plot:</strong> Scatter plot graphs the 18 raw pairs $(\text{age}_i, \text{\%fat}_i)$, showing a strong upward linear association with two low-fat points around ages 23–27. Because $M=N=18$, the Q-Q plot pairs independently sorted quantiles $(x_{(i)}, y_{(i)})$ at quantile $f_i = \frac{i - 0.5}{18}$: $(23, 7.8), (23, 9.5), (27, 17.8), (27, 25.9), \dots, (60, 41.2), (61, 42.5)$.
              </div>
            </div>
          </div>

          <!-- Exercise 2.18 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch2">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 2.18 — Normalizing Age = 35 Using Ex. 2.14 Data (Book p. 82 / PDF p. 113)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 2: Data &amp; Preprocessing</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> Using the data for <em>age</em> given in Exercise 2.14 (<code>13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70</code>; $N=27, \min=13, \max=70, \bar{x}=\frac{809}{27}\approx 29.9630$), answer: (a) Use min-max normalization to transform $35$ onto $[0.0, 1.0]$. (b) Use z-score normalization to transform $35$, where standard deviation $\sigma = 12.70$ years. (c) Use normalization by decimal scaling to transform $35$. (d) Comment on which method you prefer and why.
            </div>
            <div class="text-xs text-slate-400 space-y-2 border-t border-white/5 pt-3">
              <div>
                <strong>(a) Min-Max Normalization onto $[0.0, 1.0]$:</strong>
                $$v' = \frac{v - \min_A}{\max_A - \min_A}(1.0 - 0.0) + 0.0 = \frac{35 - 13}{70 - 13} = \frac{22}{57} \approx \mathbf{0.3860}$$
              </div>
              <div>
                <strong>(b) Z-Score Normalization ($\sigma = 12.70$ years):</strong>
                $$v' = \frac{v - \bar{A}}{\sigma_A} = \frac{35 - 29.9630}{12.70} = \frac{5.0370}{12.70} \approx \mathbf{0.3966}$$
                <span class="text-[11px] text-slate-500">(Using rounded $\bar{A}=29.96$ gives $\frac{5.04}{12.70}\approx 0.3969$.)</span>
              </div>
              <div>
                <strong>(c) Decimal Scaling Normalization:</strong> $\max(|v_i|) = 70 \implies$ smallest integer $j$ with $\frac{70}{10^j} \lt 1$ is $j = 2$ ($10^2 = 100$):
                $$v' = \frac{35}{10^2} = \mathbf{0.35}$$
              </div>
              <div>
                <strong>(d) Preferred Method:</strong> <strong>Decimal scaling</strong> (or <strong>z-score</strong>) is preferred over min-max here: decimal scaling divides by $100$, preserves exact proportions, requires no statistics, and stays within $[0,1)$ for any human age $\lt 100$. <strong>Z-score</strong> also prevents range compression caused by the extreme outlier $70$ and avoids out-of-bounds failures on future records $\gt 70$.
              </div>
            </div>
          </div>

          <!-- Exercise 2.19 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch2">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 2.19 — Z-Score Normalization, Correlation $r$ &amp; Covariance (Book p. 82 / PDF p. 113)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 2: Data &amp; Preprocessing</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> Using the data for <em>age</em> and <em>body fat</em> given in Exercise 2.7 ($n=18$), answer: (a) Normalize the two attributes based on <em>z-score normalization</em>. (b) Calculate the <em>correlation coefficient</em> (Pearson's product moment coefficient). Are these two attributes positively or negatively correlated? Compute their covariance.
            </div>
            <div class="text-xs text-slate-400 space-y-2 border-t border-white/5 pt-3">
              <div>
                <strong>(a) Z-Score Normalization ($z_i = \frac{v_i - \bar{V}}{\sigma_V}$ using $\bar{A}=46.4444, \sigma_A=12.8462$ and $\bar{B}=28.7833, \sigma_B=8.9937$):</strong>
                <div class="overflow-x-auto my-2">
                  <table class="w-full text-center font-mono text-[11px] border border-white/10">
                    <tr class="bg-slate-800 text-slate-200"><th class="p-1 border border-white/10">#</th><th class="p-1 border border-white/10">age</th><th class="p-1 border border-white/10">$z_{\text{age}}$</th><th class="p-1 border border-white/10">%fat</th><th class="p-1 border border-white/10">$z_{\text{\%fat}}$</th><th class="p-1 border border-white/10">#</th><th class="p-1 border border-white/10">age</th><th class="p-1 border border-white/10">$z_{\text{age}}$</th><th class="p-1 border border-white/10">%fat</th><th class="p-1 border border-white/10">$z_{\text{\%fat}}$</th></tr>
                    <tr><td>1</td><td>23</td><td>-1.8250</td><td>9.5</td><td>-2.1441</td><td>10</td><td>52</td><td>+0.4325</td><td>34.6</td><td>+0.6468</td></tr>
                    <tr><td>2</td><td>23</td><td>-1.8250</td><td>26.5</td><td>-0.2539</td><td>11</td><td>54</td><td>+0.5882</td><td>42.5</td><td>+1.5251</td></tr>
                    <tr><td>3</td><td>27</td><td>-1.5136</td><td>7.8</td><td>-2.3331</td><td>12</td><td>54</td><td>+0.5882</td><td>28.8</td><td>+0.0019</td></tr>
                    <tr><td>4</td><td>27</td><td>-1.5136</td><td>17.8</td><td>-1.2212</td><td>13</td><td>56</td><td>+0.7438</td><td>33.4</td><td>+0.5133</td></tr>
                    <tr><td>5</td><td>39</td><td>-0.5795</td><td>31.4</td><td>+0.2909</td><td>14</td><td>57</td><td>+0.8217</td><td>30.2</td><td>+0.1575</td></tr>
                    <tr><td>6</td><td>41</td><td>-0.4238</td><td>25.9</td><td>-0.3206</td><td>15</td><td>58</td><td>+0.8995</td><td>34.1</td><td>+0.5912</td></tr>
                    <tr><td>7</td><td>47</td><td>+0.0432</td><td>27.4</td><td>-0.1538</td><td>16</td><td>58</td><td>+0.8995</td><td>32.9</td><td>+0.4577</td></tr>
                    <tr><td>8</td><td>49</td><td>+0.1989</td><td>27.2</td><td>-0.1761</td><td>17</td><td>60</td><td>+1.0552</td><td>41.2</td><td>+1.3806</td></tr>
                    <tr><td>9</td><td>50</td><td>+0.2768</td><td>31.2</td><td>+0.2687</td><td>18</td><td>61</td><td>+1.1331</td><td>35.7</td><td>+0.7691</td></tr>
                  </table>
                </div>
              </div>
              <div>
                <strong>(b) Covariance &amp; Pearson Correlation Coefficient ($n = 18$):</strong>
                $$\sum_{i=1}^{18} a_i b_i = 25763.20, \quad \sum_{i=1}^{18}(a_i - \bar{A})(b_i - \bar{B}) = 1700.3333$$
                $$\text{Cov}(\text{age}, \text{\%fat}) = \frac{\sum a_i b_i}{18} - \bar{A}\bar{B} = \frac{25763.20}{18} - (46.4444)(28.7833) = \mathbf{94.4630} \quad (\text{sample } \div 17: 100.0196)$$
                $$r_{\text{age},\text{\%fat}} = \frac{94.4630}{12.8462 \times 8.9937} = \mathbf{+0.8176}$$
                <p><strong>Interpretation:</strong> Since $r = +0.8176 \gt 0$ (and $\text{Cov} \gt 0$), <em>age</em> and <em>%fat</em> are <strong>strongly positively correlated</strong>.</p>
              </div>
            </div>
          </div>

          <!-- Exercise 2.20 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch2">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 2.20 — Binning 12 Sales Price Records (Book p. 82 / PDF p. 113)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 2: Data &amp; Preprocessing</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> Suppose a group of 12 <em>sales price</em> records has been sorted as follows: <code>5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215</code>. Partition them into three bins by: (a) Equal-frequency (equal-depth) partitioning, (b) Equal-width partitioning, (c) Clustering.
            </div>
            <div class="text-xs text-slate-400 space-y-1.5 border-t border-white/5 pt-3">
              <ul class="list-disc pl-5 space-y-1">
                <li><strong>(a) Equal-Frequency ($12 / 3 = 4$ values per bin):</strong> Bin 1: <code>{5, 10, 11, 13}</code>; Bin 2: <code>{15, 35, 50, 55}</code>; Bin 3: <code>{72, 92, 204, 215}</code>.</li>
                <li><strong>(b) Equal-Width ($w = \frac{215 - 5}{3} = 70$, intervals $[5, 75], (75, 145], (145, 215]$):</strong> Bin 1: <code>{5, 10, 11, 13, 15, 35, 50, 55, 72}</code>; Bin 2: <code>{92}</code>; Bin 3: <code>{204, 215}</code>.</li>
                <li><strong>(c) Clustering (1D $k$-means, $k=3$, min $\text{SSE} = 1688.08$):</strong> Cluster 1: <code>{5, 10, 11, 13, 15, 35}</code> (mean $14.83$); Cluster 2: <code>{50, 55, 72, 92}</code> (mean $67.25$); Cluster 3: <code>{204, 215}</code> (mean $209.50$).</li>
              </ul>
            </div>
          </div>

          <!-- Exercise 3.15 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 3.15 — ROLAP, MOLAP &amp; HOLAP Comparison (Book pp. 137–138 / PDF pp. 168–169)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 3: Data Warehousing &amp; OLAP</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> A multidimensional view can be implemented by a relational database technique (<em>ROLAP</em>), a multidimensional database technique (<em>MOLAP</em>), or a hybrid technique (<em>HOLAP</em>). (a) Briefly describe each. (b) For each technique, explain how each implements: (i) generation of a data warehouse (incl. aggregation), (ii) roll-up, (iii) drill-down, (iv) incremental updating. (c) Which implementation techniques do you prefer, and why?
            </div>
            <div class="text-xs text-slate-400 space-y-2 border-t border-white/5 pt-3">
              <p><strong>(a) Overview:</strong> <strong>ROLAP</strong> uses relational tables + OLAP SQL middleware; <strong>MOLAP</strong> uses array-based multidimensional stores; <strong>HOLAP</strong> stores large atomic data in ROLAP and high-level aggregates in MOLAP arrays.</p>
              <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] border border-white/10 my-1">
                  <tr class="bg-slate-800 text-slate-200"><th class="p-1.5 border border-white/10">Function</th><th class="p-1.5 border border-white/10">ROLAP</th><th class="p-1.5 border border-white/10">MOLAP</th><th class="p-1.5 border border-white/10">HOLAP</th></tr>
                  <tr><td class="p-1.5 border border-white/10 font-bold">i. Generation</td><td class="p-1.5 border border-white/10">Load fact/dim tables; compute SQL GROUP BY / CUBE summary tables.</td><td class="p-1.5 border border-white/10">Map dim values to array indices; compute compressed subcube arrays (MultiWay).</td><td class="p-1.5 border border-white/10">Load atomic data into ROLAP tables; materialize upper cuboids in MOLAP arrays.</td></tr>
                  <tr><td class="p-1.5 border border-white/10 font-bold">ii. Roll-up</td><td class="p-1.5 border border-white/10">Join dim hierarchies + SQL GROUP BY or query coarser materialized table.</td><td class="p-1.5 border border-white/10">Direct array lookup on coarser cuboid or sum along array axis.</td><td class="p-1.5 border border-white/10">Read MOLAP summary arrays directly; fall back to ROLAP SQL if unmaterialized.</td></tr>
                  <tr><td class="p-1.5 border border-white/10 font-bold">iii. Drill-down</td><td class="p-1.5 border border-white/10">SQL WHERE on parent + GROUP BY finer dim table attributes.</td><td class="p-1.5 border border-white/10">Index lower-level array chunk along refined dim coordinates.</td><td class="p-1.5 border border-white/10">Traverse MOLAP arrays down; switch to ROLAP SQL for raw drill-through.</td></tr>
                  <tr><td class="p-1.5 border border-white/10 font-bold">iv. Incremental Update</td><td class="p-1.5 border border-white/10">Append delta rows to fact table; SQL MERGE affected summary partitions.</td><td class="p-1.5 border border-white/10">Update chunks, expand/re-chunk arrays for new members, propagate ancestors.</td><td class="p-1.5 border border-white/10">Append deltas cheaply in ROLAP base tables, then propagate delta aggregates to MOLAP.</td></tr>
                </table>
              </div>
              <p><strong>(c) Preference:</strong> <strong>HOLAP</strong> is best for large enterprise warehouses (scalable sparse relational base storage + sub-second MOLAP summary array reads); MOLAP suits small dense data marts, and ROLAP suits extreme relational scale.</p>
            </div>
          </div>

          <!-- Exercise 3.17 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 3.17 — Max &amp; Min Cells in an n-D Data Cube (Book p. 138 / PDF p. 169)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 3: Data Warehousing &amp; OLAP</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> A data cube, $C$, has $n$ dimensions, and each dimension has exactly $p$ distinct values in the base cuboid. Assume that there are no concept hierarchies associated with the dimensions. (a) Max cells in base cuboid? (b) Min cells in base cuboid? (c) Max cells (base + aggregate) in $C$? (d) Min cells in $C$?
            </div>
            <div class="text-xs text-slate-400 space-y-1.5 border-t border-white/5 pt-3">
              <ul class="list-disc pl-5 space-y-1">
                <li><strong>(a) Max Base Cells:</strong> Every combination in Cartesian product is present $\implies \mathbf{p^n}$.</li>
                <li><strong>(b) Min Base Cells:</strong> Since each dimension must contain all $p$ distinct values, placing them diagonally $(v_{1,i}, \dots, v_{n,i})$ achieves the minimum $\mathbf{p}$.</li>
                <li><strong>(c) Max Total Cells in $C$:</strong> Each coordinate has $p$ values plus $*$ (<code>all</code>) $\implies \sum_{k=0}^n \binom{n}{k} p^k = \mathbf{(p + 1)^n}$.</li>
                <li><strong>(d) Min Total Cells in $C$:</strong> Of the $2^n$ cuboids, the $0$-D apex has $1$ cell, and each of the $2^n - 1$ non-apex cuboids retains $\ge 1$ dimension having $p$ distinct values ($\ge p$ cells, attained by $p$ diagonal base cells) $\implies \mathbf{p(2^n - 1) + 1 = p \cdot 2^n - p + 1}$.</li>
              </ul>
            </div>
          </div>

          <!-- Exercise 3.18 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 3.18 — 10-D Base Cuboid (3 Cells): Full, Iceberg &amp; Closed Cube (Book p. 138 / PDF p. 169)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 3: Data Warehousing &amp; OLAP</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> A 10-D base cuboid has 3 base cells: (1) $(a_1, d_2, d_3, d_4, \dots, d_{10})$, (2) $(d_1, b_2, d_3, d_4, \dots, d_{10})$, (3) $(d_1, d_2, c_3, d_4, \dots, d_{10})$, where $a_1 \ne d_1, b_2 \ne d_2, c_3 \ne d_3$ and measure is <code>count()</code>. Find: (a) nonempty cuboids in full cube, (b) nonempty aggregate (nonbase) cells in full cube, (c) nonempty aggregate cells in iceberg cube ($\text{count} \ge 2$), (d) closed cells in full cube.
            </div>
            <div class="text-xs text-slate-400 space-y-1.5 border-t border-white/5 pt-3">
              <p>Dimensions $F = \{4,\dots,10\}$ never differ across the 3 cells, giving $2^7 = 128$ keep/$*$ subsets $S_F$.</p>
              <ul class="list-disc pl-5 space-y-1">
                <li><strong>(a) Nonempty Cuboids:</strong> Every projection of a nonempty base cuboid is nonempty $\implies 2^{10} = \mathbf{1024}$.</li>
                <li><strong>(b) Nonempty Aggregate (Nonbase) Cells:</strong> Over $S_V \subseteq \{1,2,3\}$: $\emptyset \to 1$ cell (count 3); $|S_V|=1$ ($3$ cuboids) $\to 2$ cells each (count 2 and 1); $|S_V|=2$ ($3$ cuboids) $\to 3$ cells each (count 1); $S_V=\{1,2,3\} \to 3$ cells across $127$ nonbase cuboids (excluding the 10-D base cuboid). Sum $= (1 + 6 + 9)\times 128 + 3 \times 127 = \mathbf{2429}$ (total $2432 - 3$ base).</li>
                <li><strong>(c) Iceberg Aggregate Cells ($\text{count} \ge 2$):</strong> Only $S_V=\emptyset$ ($1$ cell, count 3) and $|S_V|=1$ ($3 \times 1$ cells having $d_i$, count 2) pass $\implies (1 + 3)\times 128 = \mathbf{512}$.</li>
                <li><strong>(d) Closed Cells:</strong> Every closed cell fixes $d_4,\dots,d_{10}$ (otherwise specializing $*$ to $d_k$ preserves count): count 3 gives $(*,*,*,d_4\dots)$ ($1$ cell); count 2 gives $(d_1,*,*), (*,d_2,*), (*,*,d_3)$ ($3$ cells); count 1 gives the $3$ base cells $\implies 1 + 3 + 3 = \mathbf{7}$.</li>
              </ul>
            </div>
          </div>

          <!-- Exercise 3.22 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 3.22 — 100-D Curse of Dimensionality, Iceberg &amp; Closed Cells (Book p. 139 / PDF p. 170)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 3: Data Warehousing &amp; OLAP</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> Two 100-D base cells: $(a_1, a_2, a_3, \dots, a_{100})$ and $(a_1, a_2, b_3, \dots, b_{100})$. (a) Compute number of nonempty aggregate cells; comment on space and time. (b) If iceberg $\text{min\_sup} = 2$, how many aggregate cells and show them. (c) Given 20 tuples forming these two base cells with count 10 each and $\text{min\_sup}=10$: (i) how many aggregate cells exist, (ii) ignoring redundant constant-to-$*$ generalizations with the same count, how many distinct cells remain and what are they?
            </div>
            <div class="text-xs text-slate-400 space-y-1.5 border-t border-white/5 pt-3">
              <ul class="list-disc pl-5 space-y-1">
                <li><strong>(a) Nonempty Aggregate Cells:</strong> Each cell yields $2^{100}-1$ aggregate cells, overlapping only when dims $3\dots 100$ are all $*$ ($2^2 = 4$ cells) $\implies 2(2^{100}-1) - 4 = \mathbf{2^{101} - 6} \approx 2.535 \times 10^{30}$ cells. Even 2 base rows explode storage and time exponentially ($O(2^D)$).</li>
                <li><strong>(b) Iceberg ($\text{min\_sup}=2$, count-1 cells):</strong> Only the $\mathbf{4}$ shared cells pass: $(a_1, a_2, *, \dots, *)$, $(a_1, *, *, \dots, *)$, $(*, a_2, *, \dots, *)$, $(*, *, *, \dots, *)$.</li>
                <li><strong>(c)(i) Iceberg ($\text{min\_sup}=10$, count-10 base cells):</strong> All aggregate cells have count $10$ or $20 \ge 10$, so all $\mathbf{2^{101} - 6}$ aggregate cells survive ($2^{101}-10$ with count $10$; $4$ with count $20$).</li>
                <li><strong>(c)(ii) Closed Cells Remaining:</strong> Only $\mathbf{3}$ cells: $(a_1, a_2, a_3, \dots, a_{100}):10$, $(a_1, a_2, b_3, \dots, b_{100}):10$, and $(a_1, a_2, *, \dots, *):20$.</li>
              </ul>
            </div>
          </div>

          <!-- Exercise 4.1 (Bonus Moodle 4.1Chapter 5 safeguard) -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch4">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 4.1 — Querying Frequent Closed Itemsets $\mathcal{C}$ (Book p. 170 / PDF p. 201)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 4: Basic Pattern Mining (Moodle "4.1Chapter 5" Check)</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> Suppose you have the set $\mathcal{C}$ of all frequent closed itemsets on a data set $D$, as well as the support count for each frequent closed itemset. Describe an algorithm to determine whether a given itemset $X$ is frequent or not, and the support of $X$ if it is frequent.
            </div>
            <div class="text-xs text-slate-400 space-y-1.5 border-t border-white/5 pt-3">
              <ol class="list-decimal pl-5 space-y-1">
                <li>Find all frequent closed supersets of $X$: $S = \{Y \in \mathcal{C} \mid X \subseteq Y\}$.</li>
                <li>If $S = \emptyset$, return <strong>not frequent</strong> (because $\text{closure}(X)$ has the same support as $X$, so if $X$ were frequent then $\text{closure}(X) \in \mathcal{C}$ would cover $X$).</li>
                <li>Otherwise ($S \ne \emptyset$), return <strong>frequent</strong> with exact support $\text{support\_count}(X) = \max_{Y \in S} \text{support\_count}(Y)$ (achieved at $Y = \text{closure}(X)$).</li>
              </ol>
            </div>
          </div>

          <!-- Exercise 4.3 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch4">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 4.3 — Apriori Subset Support, Confidence &amp; Partition Proofs (Book p. 170 / PDF p. 201)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 4: Basic Pattern Mining</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> The Apriori algorithm makes use of <em>prior knowledge</em> of subset support properties. (a) Prove all nonempty subsets of a frequent itemset must be frequent. (b) Prove $\text{support}(s') \ge \text{support}(s)$ for any nonempty subset $s'$ of $s$. (c) Given frequent itemset $l$ and $s \subset l, s' \subseteq s$, prove $\text{conf}(s' \Rightarrow (l - s')) \le \text{conf}(s \Rightarrow (l - s))$. (d) If $D$ is subdivided into $n$ nonoverlapping partitions, prove any itemset frequent in $D$ must be frequent in at least one partition.
            </div>
            <div class="text-xs text-slate-400 space-y-1.5 border-t border-white/5 pt-3">
              <ul class="list-disc pl-5 space-y-1">
                <li><strong>(a) &amp; (b):</strong> For any nonempty $s' \subseteq s$, every transaction $T \in D$ containing $s$ must also contain $s'$: $\{T \mid s \subseteq T\} \subseteq \{T \mid s' \subseteq T\} \implies \text{sup\_count}(s') \ge \text{sup\_count}(s) \implies \text{support}(s') \ge \text{support}(s)$. Thus if $s$ is frequent ($\ge \text{min\_sup}$), all nonempty subsets $s'$ are frequent.</li>
                <li><strong>(c):</strong> $\text{conf}(s' \Rightarrow (l-s')) = \frac{\text{sup}(l)}{\text{sup}(s')}$ and $\text{conf}(s \Rightarrow (l-s)) = \frac{\text{sup}(l)}{\text{sup}(s)}$. Since $s' \subseteq s$, by (b) $\text{sup}(s') \ge \text{sup}(s) \ge \text{sup}(l) \gt 0$, so taking reciprocals reverses the inequality: $\text{conf}(s' \Rightarrow (l-s')) \le \text{conf}(s \Rightarrow (l-s))$.</li>
                <li><strong>(d) Partition Proof (by contradiction):</strong> Suppose $X$ is frequent in $D$ ($\text{sup\_count}_D(X) \ge \sigma |D|$) yet infrequent in every partition $D_i$: $\text{sup\_count}_{D_i}(X) \lt \sigma |D_i|$ for $i=1\dots n$. Summing gives $\text{sup\_count}_D(X) = \sum_{i=1}^n \text{sup\_count}_{D_i}(X) \lt \sigma \sum_{i=1}^n |D_i| = \sigma |D|$, a contradiction.</li>
              </ul>
            </div>
          </div>

          <!-- Exercise 4.6 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch4">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 4.6 — MONKEY Database: Apriori vs FP-Growth &amp; Strong Metarules (Book p. 171 / PDF p. 202)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 4: Basic Pattern Mining</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> A database has five transactions ($\text{min\_sup} = 60\% \implies \text{count} \ge 3$, $\text{min\_conf} = 80\%$): <code>T100: {M, O, N, K, E, Y}</code>, <code>T200: {D, O, N, K, E, Y}</code>, <code>T300: {M, A, K, E}</code>, <code>T400: {M, U, C, K, Y}</code>, <code>T500: {C, O, O, K, I, E}</code> (as distinct set of items: <code>{C, O, K, I, E}</code>). (a) Find all frequent itemsets using Apriori and FP-growth, and compare efficiency. (b) List all strong association rules matching $\forall x \in \text{transaction},\; \text{buys}(X, \text{item}_1) \land \text{buys}(X, \text{item}_2) \Rightarrow \text{buys}(X, \text{item}_3)\; [s, c]$.
            </div>
            <div class="text-xs text-slate-400 space-y-2 border-t border-white/5 pt-3">
              <div>
                <strong>(a1) Apriori (3 DB scans, 22 candidates counted + 3 pruned):</strong>
                <ul class="list-disc pl-5 mt-1 space-y-0.5">
                  <li>$L_1$ ($\text{sup} \ge 3$): <code>{E}:4, {K}:5, {M}:3, {O}:3, {Y}:3</code>.</li>
                  <li>$L_2$ (out of $\binom{5}{2}=10$ candidates in $C_2$): <code>{E,K}:4, {E,O}:3, {K,M}:3, {K,O}:3, {K,Y}:3</code>.</li>
                  <li>$C_3 \to L_3$: Raw join produces <code>{E,K,O}</code> (kept), plus <code>{K,M,O}, {K,M,Y}, {K,O,Y}</code> (all 3 pruned since <code>{M,O}, {M,Y}, {O,Y}</code> $\notin L_2$). Hence $L_3 = \{\{E,K,O\}:3\}$. Total = <strong>11 frequent itemsets</strong>.</li>
                </ul>
              </div>
              <div>
                <strong>(a2) FP-Growth (2 DB scans, zero candidate generation):</strong> F-list: <code>K:5, E:4, M:3, O:3, Y:3</code>. Ordered DB: <code>KEMOY, KEOY, KEM, KMY, KEO</code>. Root splits into <code>K:5 &rarr; E:4 &rarr; (M:2 &rarr; O:1 &rarr; Y:1, O:2 &rarr; Y:1)</code> and <code>K:5 &rarr; M:1 &rarr; Y:1</code>. Conditional mining from bottom up yields identical 11 frequent itemsets (faster on dense data; avoids multi-pass DB I/O and combinatorial $C_k$ joins).
              </div>
              <div>
                <strong>(b) Strong Rules Matching $2 \Rightarrow 1$ Metarule (from $L_3 = \{E, K, O\}$, $s = 3/5 = 60\%$):</strong>
                <ul class="list-disc pl-5 mt-1">
                  <li>$E \land K \Rightarrow O$: $\text{conf} = 3/4 = 75\%$ (Reject, $\lt 80\%$).</li>
                  <li>$\mathbf{E \land O \Rightarrow K}$: $s = 60\%, c = 3/3 = \mathbf{100\%}$ (<strong>Strong</strong>).</li>
                  <li>$\mathbf{K \land O \Rightarrow E}$: $s = 60\%, c = 3/3 = \mathbf{100\%}$ (<strong>Strong</strong>).</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Exercise 4.10 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch4">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 4.10 — Incremental Mining on $DB \cup \Delta DB$ (Book p. 172 / PDF p. 203)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 4: Basic Pattern Mining</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> Suppose that frequent itemsets are saved for a large transactional database, $DB$. Discuss how to efficiently mine the (global) association rules under the same minimum support threshold, if a set of new transactions, denoted as $\Delta DB$, is (incrementally) added in?
            </div>
            <div class="text-xs text-slate-400 space-y-1.5 border-t border-white/5 pt-3">
              <p>An itemset $X$ is globally frequent in $DB' = DB \cup \Delta DB$ iff $\text{sup\_count}_{DB}(X) + \text{sup\_count}_{\Delta DB}(X) \ge \sigma(|DB| + |\Delta DB|)$. By Exercise 4.3(d), any globally frequent itemset must be frequent in $DB$ ($L^{DB}$) or $\Delta DB$ ($L^{\Delta DB}$) — the <strong>FUP Incremental Mining Strategy</strong>:</p>
              <ul class="list-disc pl-5 space-y-1">
                <li><strong>Case 1 ($X \in L^{DB}, X \in L^{\Delta DB}$):</strong> Automatically globally frequent; sum counts directly (zero $DB$ scan).</li>
                <li><strong>Case 2 ($X \in L^{DB}, X \notin L^{\Delta DB}$):</strong> Scan small $\Delta DB$ only; if sum $\lt \sigma(|DB|+|\Delta DB|)$, prune loser $X$ and its supersets (zero $DB$ scan).</li>
                <li><strong>Case 3 ($X \notin L^{DB}, X \in L^{\Delta DB}$):</strong> Potential new winner; filter by global $(k-1)$-subset Apriori check, then scan $DB$ <em>only</em> for these surviving candidates.</li>
                <li><strong>Case 4 ($X \notin L^{DB}, X \notin L^{\Delta DB}$):</strong> Guaranteed infrequent in $DB'$; pruned immediately. Strong rules are then extracted in memory from updated $L^{DB'}$.</li>
              </ul>
            </div>
          </div>

          <!-- Exercise 6.7 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch6">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 6.7 — Employee Count Table: Decision Tree &amp; Naive Bayes (Book pp. 299–300 / PDF pp. 330–331)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 6: Classification Basic</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> Generalized employee training data with <code>count</code> tuples (class attribute: <code>status</code> $\in \{\text{senior}, \text{junior}\}$). (a) How would you modify the basic decision tree algorithm (Fig. 6.3) to take into consideration the <code>count</code> of each generalized data tuple? (b) Use your algorithm to construct a decision tree from the given data. (c) Given tuple $X = (\text{department}=\text{systems}, \text{age}=26\dots 30, \text{salary}=46\text{K}\dots 50\text{K})$, what would a naive Bayesian classification of <code>status</code> be?
              <div class="overflow-x-auto my-2">
                <table class="w-full text-[11px] font-mono text-left border border-white/10">
                  <tr class="bg-slate-800 text-amber-300"><th class="p-1 border border-white/10">department</th><th class="p-1 border border-white/10">status</th><th class="p-1 border border-white/10">age</th><th class="p-1 border border-white/10">salary</th><th class="p-1 border border-white/10 text-right">count</th></tr>
                  <tr><td class="p-1 border border-white/10">sales</td><td class="p-1 border border-white/10">senior</td><td class="p-1 border border-white/10">31...35</td><td class="p-1 border border-white/10">46K...50K</td><td class="p-1 border border-white/10 text-right">30</td></tr>
                  <tr><td class="p-1 border border-white/10">sales</td><td class="p-1 border border-white/10">junior</td><td class="p-1 border border-white/10">26...30</td><td class="p-1 border border-white/10">26K...30K</td><td class="p-1 border border-white/10 text-right">40</td></tr>
                  <tr><td class="p-1 border border-white/10">sales</td><td class="p-1 border border-white/10">junior</td><td class="p-1 border border-white/10">31...35</td><td class="p-1 border border-white/10">31K...35K</td><td class="p-1 border border-white/10 text-right">40</td></tr>
                  <tr><td class="p-1 border border-white/10">systems</td><td class="p-1 border border-white/10">junior</td><td class="p-1 border border-white/10">21...25</td><td class="p-1 border border-white/10">46K...50K</td><td class="p-1 border border-white/10 text-right">20</td></tr>
                  <tr><td class="p-1 border border-white/10">systems</td><td class="p-1 border border-white/10">senior</td><td class="p-1 border border-white/10">31...35</td><td class="p-1 border border-white/10">66K...70K</td><td class="p-1 border border-white/10 text-right">5</td></tr>
                  <tr><td class="p-1 border border-white/10">systems</td><td class="p-1 border border-white/10">junior</td><td class="p-1 border border-white/10">26...30</td><td class="p-1 border border-white/10">46K...50K</td><td class="p-1 border border-white/10 text-right">3</td></tr>
                  <tr><td class="p-1 border border-white/10">systems</td><td class="p-1 border border-white/10">senior</td><td class="p-1 border border-white/10">41...45</td><td class="p-1 border border-white/10">66K...70K</td><td class="p-1 border border-white/10 text-right">3</td></tr>
                  <tr><td class="p-1 border border-white/10">marketing</td><td class="p-1 border border-white/10">senior</td><td class="p-1 border border-white/10">36...40</td><td class="p-1 border border-white/10">46K...50K</td><td class="p-1 border border-white/10 text-right">10</td></tr>
                  <tr><td class="p-1 border border-white/10">marketing</td><td class="p-1 border border-white/10">junior</td><td class="p-1 border border-white/10">31...35</td><td class="p-1 border border-white/10">41K...45K</td><td class="p-1 border border-white/10 text-right">4</td></tr>
                  <tr><td class="p-1 border border-white/10">secretary</td><td class="p-1 border border-white/10">senior</td><td class="p-1 border border-white/10">46...50</td><td class="p-1 border border-white/10">36K...40K</td><td class="p-1 border border-white/10 text-right">4</td></tr>
                  <tr><td class="p-1 border border-white/10">secretary</td><td class="p-1 border border-white/10">junior</td><td class="p-1 border border-white/10">26...30</td><td class="p-1 border border-white/10">26K...30K</td><td class="p-1 border border-white/10 text-right">6</td></tr>
                </table>
              </div>
            </div>
            <div class="text-xs text-slate-400 space-y-2 border-t border-white/5 pt-3">
              <div><strong>(a) Algorithm Modification:</strong> Use each generalized row's <code>count</code> as a weight $w_r$: replace tuple counts with $|D| = \sum \text{count}_r$ and $|C_{i,D}| = \sum_{r \in C_i} \text{count}_r$ inside Entropy, Information Gain, majority-class voting, and empty-partition checks.</div>
              <div>
                <strong>(b) Decision Tree Construction ($|D| = 165$: $52$ senior, $113$ junior):</strong>
                $$\text{Info}(D) = -\left(\frac{52}{165}\log_2\frac{52}{165} + \frac{113}{165}\log_2\frac{113}{165}\right) = \mathbf{0.8990\text{ bits}}$$
                <ul class="list-disc pl-5 mt-1 space-y-0.5">
                  <li>$\text{Gain}(\text{department}) = 0.8990 - 0.8504 = \mathbf{0.0486}$; $\text{Gain}(\text{age}) = 0.8990 - \frac{79}{165}(0.9906) = \mathbf{0.4247}$; $\text{Gain}(\text{salary}) = 0.8990 - \frac{63}{165}(0.9468) = \mathbf{0.5375}$ &rarr; <strong>Root = <code>salary</code></strong>.</li>
                  <li>Pure leaves under <code>salary</code>: <code>26K...30K</code> $\to$ junior ($46$); <code>31K...35K</code> $\to$ junior ($40$); <code>36K...40K</code> $\to$ senior ($4$); <code>41K...45K</code> $\to$ junior ($4$); <code>66K...70K</code> $\to$ senior ($8$).</li>
                  <li>Only <code>46K...50K</code> ($40$ senior, $23$ junior) is impure: both <code>department</code> and <code>age</code> achieve pure split ($\text{Gain}=0.9468$; <code>department</code> wins Gain Ratio $0.6477$ vs $0.5684$ with 3 branches: <code>sales</code> $\to$ senior, <code>systems</code> $\to$ junior, <code>marketing</code> $\to$ senior).</li>
                </ul>
              </div>
              <div>
                <strong>(c) Naive Bayesian Classification for $X = (\text{systems}, 26\dots 30, 46\text{K}\dots 50\text{K})$:</strong>
                <p class="mt-0.5">&bull; <em>Raw counts:</em> $P(\text{age}=26\dots 30 \mid \text{senior}) = 0/52 = 0 \implies P(X|\text{senior})P(\text{senior}) = 0$, whereas $P(X|\text{junior})P(\text{junior}) = \left(\frac{23}{113}\cdot\frac{49}{113}\cdot\frac{23}{113}\right)\frac{113}{165} = \mathbf{0.012303}$.</p>
                <p>&bull; <em>With Laplace smoothing ($q_{\text{dept}}=4, q_{\text{age}}=6, q_{\text{sal}}=6$):</em> $P_{\text{Lap}}(X|\text{senior})P(\text{senior}) = \left(\frac{9}{56}\cdot\frac{1}{58}\cdot\frac{41}{58}\right)\frac{52}{165} = \mathbf{0.000617}$ vs $P_{\text{Lap}}(X|\text{junior})P(\text{junior}) = \left(\frac{24}{117}\cdot\frac{50}{119}\cdot\frac{24}{119}\right)\frac{113}{165} = \mathbf{0.011904}$ ($95.07\%$ posterior). Thus <strong>predicts <code>status = junior</code></strong>.</p>
              </div>
            </div>
          </div>

          <!-- Exercise 6.19 -->
          <div class="ex-card p-5 rounded-lg bg-slate-900/70 border border-white/10 space-y-3" data-chapter="ch6">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">Exercise 6.19 — 10-Fold Cross-Validation Paired $t$-Test (Book p. 302 / PDF p. 333)</span>
              <span class="text-xs font-mono text-slate-400">Chapter 6: Classification Basic</span>
            </div>
            <div class="text-xs text-slate-300 font-medium">
              <strong>Verbatim Problem:</strong> Suppose we want to select between two prediction models, $M_1$ and $M_2$, using 10 rounds of 10-fold CV. The error rates for $M_1$ are <code>30.5, 32.2, 20.7, 20.6, 31.0, 41.0, 27.7, 26.0, 21.5, 26.0</code>. The error rates for $M_2$ are <code>22.4, 14.5, 22.4, 19.6, 20.7, 20.4, 22.1, 19.4, 16.2, 35.0</code>. Comment on whether one model is significantly better than the other at significance level $1\%$.
            </div>
            <div class="text-xs text-slate-400 space-y-1.5 border-t border-white/5 pt-3">
              <div>
                <p><strong>Step-by-Step Paired $t$-Test (Han Eq. 6.31–6.32, Book pp. 285–286):</strong></p>
                <p>&bull; Differences $d_i = \text{err}(M_1)_i - \text{err}(M_2)_i$: $[+8.1, +17.7, -1.7, +1.0, +10.3, +20.6, +5.6, +6.6, +5.3, -9.0]$.</p>
                $$\overline{\text{err}}(M_1) = 27.72, \quad \overline{\text{err}}(M_2) = 21.27 \implies \bar{d} = \frac{64.5}{10} = \mathbf{6.45}$$
                $$\text{var}(M_1 - M_2) = \frac{1}{k}\sum_{i=1}^{10}(d_i - \bar{d})^2 = \frac{681.225}{10} = 68.1225 \implies t = \frac{6.45}{\sqrt{68.1225/10}} = \mathbf{2.4712} \quad (\text{or } 2.3444 \text{ with } k-1)$$
                <p>&bull; Critical value at $\alpha = 0.01$ ($\text{sig}/2 = 0.005$, $\text{df} = 9$): $t_{0.005,\,9} = \mathbf{3.250}$. Since $|t| = 2.4712 \lt 3.250$ ($p = 0.0355 \gt 0.01$), we <strong>fail to reject $H_0$</strong>: the difference is <strong>not statistically significant at the $1\%$ level</strong> (though it is significant at $5\%$, $t_{0.025,9}=2.262$).</p>
              </div>
            </div>
          </div>

        </div>
      </div>

          <!-- TOPIC 9 MANDATED WORKED EXAMPLE: Deep Learning Forward & Backprop (Han §10.1) -->
          <div class="p-4 rounded bg-slate-900/80 border border-white/10 space-y-3" data-chapter="6">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300 border border-white/10">Topic 9 Mandated Example: Han Example 10.1 (Book pp. 495–496 / PDF pp. 526–527)</span>
              <span class="text-xs text-slate-400">Deep Learning Backpropagation</span>
            </div>
            <div class="text-xs text-slate-300 leading-relaxed">
              <strong>Verbatim Problem (Fig. 10.7 &amp; Table 10.1):</strong> A 3-layer feed-forward neural network has 3 inputs ($x_1=1, x_2=0, x_3=1$), 2 hidden units (4, 5), and 1 output unit (6), target class $T = 1$, learning rate $\eta = 0.9$. Initial weights &amp; biases: $w_{14}=0.2, w_{15}=-0.3, w_{24}=0.4, w_{25}=0.1, w_{34}=-0.5, w_{35}=0.2, w_{46}=-0.3, w_{56}=-0.2, b_4=-0.4, b_5=0.2, b_6=0.1$. Trace forward pass, error backpropagation, and weight updates.
            </div>
            <div class="text-xs text-slate-400 space-y-2 border-t border-white/5 pt-3">
              <div>
                <strong>1. Forward Propagation (Table 10.2):</strong>
                $$I_4 = 0.2 + 0 - 0.5 - 0.4 = -0.7 \implies O_4 = \frac{1}{1+e^{0.7}} \approx \mathbf{0.332}$$
                $$I_5 = -0.3 + 0 + 0.2 + 0.2 = 0.1 \implies O_5 = \frac{1}{1+e^{-0.1}} \approx \mathbf{0.525}$$
                $$I_6 = (-0.3)(0.332) + (-0.2)(0.525) + 0.1 = -0.105 \implies O_6 = \frac{1}{1+e^{0.105}} \approx \mathbf{0.474}$$
              </div>
              <div>
                <strong>2. Backpropagated Node Errors (Table 10.3 — Exact Textbook Values):</strong>
                $$\delta_6 = (0.474)(1-0.474)(1-0.474) = \mathbf{0.1311}, \quad \delta_5 = (0.525)(1-0.525)(0.1311)(-0.2) = \mathbf{-0.0065}, \quad \delta_4 = (0.332)(1-0.332)(0.1311)(-0.3) = \mathbf{-0.0087}$$
              </div>
              <div>
                <strong>3. Weight &amp; Bias Updates (Table 10.4):</strong>
                $w_{46}^+ = -0.3 - 0.9(0.1311)(0.332) = \mathbf{-0.339}$; $w_{56}^+ = -0.2 - 0.9(0.1311)(0.525) = \mathbf{-0.262}$; $w_{14}^+ = \mathbf{0.208}$; $w_{15}^+ = \mathbf{-0.294}$; $w_{24}^+ = \mathbf{0.4}$; $w_{25}^+ = \mathbf{0.1}$; $w_{34}^+ = \mathbf{-0.492}$; $w_{35}^+ = \mathbf{0.206}$; $b_6^+ = 0.1 - 0.9(0.1311) = -0.0180$ (book prints $-0.180$); $b_5^+ = \mathbf{0.206}$; $b_4^+ = \mathbf{-0.392}$.
                <p class="mt-1 text-amber-300"><em>Errata Note:</em> Han Table 10.3 computes $\delta_6 = +0.1311$ using $(T - O_6)$ while Table 10.4 subtracts $\eta \delta_j O_i$ (using Eq. 10.4 sign $\delta_6 = (O_6 - T)O_6(1-O_6) = -0.1311$ gives $w_{46}^+ = -0.261$, moving $O_6$ toward $T=1$).</p>
              </div>
            </div>
          </div>

          """

def main():
    with open(EXAM_PATH, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    start_marker = '          <!-- Exercise 2.2 -->'
    end_marker = '<!-- TOPIC 10 MANDATED WORKED EXAMPLE: Local Outlier Factor (LOF) Calculation -->'

    assert start_marker in content, "Could not find Exercise 2.2 marker"
    assert end_marker in content, "Could not find Topic 10 marker"

    s_idx = content.index(start_marker)
    e_idx = content.index(end_marker)

    updated = content[:s_idx] + NEW_EXERCISES_AND_DL_HTML + content[e_idx:]

    # Fix Ch4 filter dropdown label and BUC cardinality sort order across Exam_Preparation/index.html
    updated = updated.replace(
        '<option value="ch4">Chapter 4 (4.3, 4.6, 4.10)</option>',
        '<option value="ch4">Chapter 4 (4.3, 4.6, 4.10, +4.1)</option>'
    )
    updated = updated.replace(
        '<span class="px-1.5 py-0.2 rounded-full bg-brand-500/20 text-brand-300 font-mono text-[10px]">14 Solved</span>',
        '<span class="px-1.5 py-0.2 rounded-full bg-brand-500/20 text-brand-300 font-mono text-[10px]">15 Solved</span>'
    )
    updated = updated.replace(
        '<p class="text-slate-400 mt-1">Ascending cardinality order $(A \\to B \\to C)$ ensures maximum early subtree pruning.</p>',
        '<p class="text-slate-400 mt-1">Decreasing cardinality order (highest cardinality first) splits into smaller partitions earlier for maximal iceberg pruning (Han §3.5.2).</p>'
    )
    updated = updated.replace(
        'Why does the BUC (Bottom-Up Computation) iceberg algorithm sort dimensions in ascending order of cardinality?',
        'Why does the BUC (Bottom-Up Computation) iceberg algorithm sort dimensions in decreasing order of cardinality?'
    )
    updated = updated.replace(
        "<span>B) To maximize iceberg pruning early at shallow recursion levels.</span>",
        "<span>B) Higher-cardinality dimensions produce smaller partitions early, maximizing iceberg pruning at shallow recursion levels.</span>"
    )
    updated = updated.replace(
        "'mock-ans-2': { ans: 'B', expl: 'BUC sorts dimensions in increasing cardinality order so low-cardinality partitions group large slices first and deep high-cardinality dimensions prune early.' }",
        "'mock-ans-2': { ans: 'B', expl: 'Han §3.5.2 (Book p. 129): BUC sorts dimensions in decreasing order of cardinality. Higher cardinality yields smaller partitions early, giving more opportunity to prune sparse subtrees.' }"
    )

    with open(EXAM_PATH, 'w', encoding='utf-8') as f:
        f.write(updated)
    print(f"Updated {EXAM_PATH} cleanly.")

if __name__ == '__main__':
    main()
