import re

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')
    
    target1 = '''      <div class="flex items-center gap-2">
        <a href="Exam_Preparation/index.html" class="text-xs bg-indigo-600 hover:bg-indigo-500 text-white font-medium px-3 py-1.5 rounded transition-all">'''
    replace1 = '''      <div class="flex items-center gap-2">
        <a href="Study_Material/endsem_master_theory.html" class="text-xs bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-200 font-medium px-3 py-1.5 rounded border border-emerald-500/30 transition-all">
          📖 Master Theory Guide
        </a>
        <a href="Exam_Preparation/index.html" class="text-xs bg-indigo-600 hover:bg-indigo-500 text-white font-medium px-3 py-1.5 rounded transition-all">'''

    target2 = '''      <div class="flex-shrink-0">
        <a href="Exam_Preparation/index.html" class="inline-flex items-center px-5 py-2.5 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-xs transition-colors shadow-sm">
          Open Exam Preparation Suite &rarr;
        </a>
      </div>'''
    replace2 = '''      <div class="flex-shrink-0 flex flex-col sm:flex-row gap-2">
        <a href="Study_Material/endsem_master_theory.html" class="inline-flex items-center justify-center px-5 py-2.5 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-medium text-xs transition-colors shadow-sm">
          📖 Master Theory Guide &rarr;
        </a>
        <a href="Exam_Preparation/index.html" class="inline-flex items-center justify-center px-5 py-2.5 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-xs transition-colors shadow-sm">
          Open Exam Preparation Suite &rarr;
        </a>
      </div>'''

    if target1 in content and target2 in content:
        content = content.replace(target1, replace1).replace(target2, replace2)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated index.html")
    else:
        print("Failed to match targets in index.html")

def update_home():
    with open('Study_Material/00_home.html', 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')
    
    target1 = '''  <div style="display:flex; gap:.75rem; align-items:center;">
    <a href="../Exam_Preparation/index.html" style="text-decoration:none; padding: .3rem .85rem; border-radius: 6px; font-size: .78rem; font-weight:600; background: #4f46e5; color: #fff;">Exam Prep Suite &rarr;</a>'''
    replace1 = '''  <div style="display:flex; gap:.75rem; align-items:center;">
    <a href="endsem_master_theory.html" style="text-decoration:none; padding: .3rem .85rem; border-radius: 6px; font-size: .78rem; font-weight:600; background: #059669; color: #fff;">📖 Master Theory &rarr;</a>
    <a href="../Exam_Preparation/index.html" style="text-decoration:none; padding: .3rem .85rem; border-radius: 6px; font-size: .78rem; font-weight:600; background: #4f46e5; color: #fff;">Exam Prep Suite &rarr;</a>'''

    target2 = '''      <a href="../Exam_Preparation/index.html" style="background:#4f46e5; color:#ffffff; font-size:0.85rem; font-weight:700; padding:0.65rem 1.25rem; border-radius:8px; text-decoration:none; display:inline-flex; align-items:center; gap:0.5rem; border:1px solid rgba(255,255,255,0.15);">
        Open Endsem Exam Portal &rarr;
      </a>
    </div>

    <!-- Quick Links Grid -->'''
    replace2 = '''      <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
        <a href="endsem_master_theory.html" style="background:#059669; color:#ffffff; font-size:0.85rem; font-weight:700; padding:0.65rem 1.25rem; border-radius:8px; text-decoration:none; display:inline-flex; align-items:center; gap:0.5rem; border:1px solid rgba(255,255,255,0.15);">
          📖 Master Theory Guide &rarr;
        </a>
        <a href="../Exam_Preparation/index.html" style="background:#4f46e5; color:#ffffff; font-size:0.85rem; font-weight:700; padding:0.65rem 1.25rem; border-radius:8px; text-decoration:none; display:inline-flex; align-items:center; gap:0.5rem; border:1px solid rgba(255,255,255,0.15);">
          Open Endsem Exam Portal &rarr;
        </a>
      </div>
    </div>

    <!-- Quick Links Grid -->'''

    if target1 in content and target2 in content:
        content = content.replace(target1, replace1).replace(target2, replace2)
        with open('Study_Material/00_home.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated Study_Material/00_home.html")
    else:
        print("Failed to match targets in Study_Material/00_home.html")

def update_exam_prep():
    with open('Exam_Preparation/index.html', 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')
    
    target1 = '''      <nav class="hidden md:flex items-center space-x-2">

        <a href="../Study_Material/00_home.html" class="px-3 py-1.5 text-xs font-medium text-slate-400 hover:text-slate-200 transition-colors">Study Modules</a>'''
    replace1 = '''      <nav class="hidden md:flex items-center space-x-2">

        <a href="../Study_Material/endsem_master_theory.html" class="px-3 py-1.5 text-xs font-semibold bg-emerald-600/30 text-emerald-200 border border-emerald-500/40 rounded hover:bg-emerald-600/50 transition-colors">📖 Master Theory Guide</a>

        <a href="../Study_Material/00_home.html" class="px-3 py-1.5 text-xs font-medium text-slate-400 hover:text-slate-200 transition-colors">Study Modules</a>'''

    target2 = '''      <!-- Mode Selector -->

      <div class="flex flex-col sm:flex-row items-start sm:items-center gap-2">'''
    replace2 = '''      <!-- Master Theory CTA & Mode Selector -->

      <div class="flex flex-col sm:flex-row items-start sm:items-center gap-3">
        <a href="../Study_Material/endsem_master_theory.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold transition-all">
          📖 Complete Theory Compendium &rarr;
        </a>'''

    if target1 in content and target2 in content:
        content = content.replace(target1, replace1).replace(target2, replace2)
        with open('Exam_Preparation/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated Exam_Preparation/index.html")
    else:
        print("Failed to match targets in Exam_Preparation/index.html")

if __name__ == '__main__':
    update_index()
    update_home()
    update_exam_prep()
