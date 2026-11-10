# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.dirname(__file__))

from part1_head_nav import part1_html
from part2_ch1_ch2 import part2_html
from part3_ch3_ch4 import part3_html
from part4_ch5_papers import part4_html
from part5_ch6_ch7 import part5_html
from part6_ch8_papers import part6_html
from part7_dl_outliers import part7_html
from part8_calc_synthesis import part8_html

full_html = (
    part1_html +
    part2_html +
    part3_html +
    part4_html +
    part5_html +
    part6_html +
    part7_html +
    part8_html
)

out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Study_Material', 'endsem_master_theory.html'))
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

size = os.path.getsize(out_path)
print(f"Generated {out_path} successfully. Total size: {size} bytes ({size/1024:.1f} KB).")
