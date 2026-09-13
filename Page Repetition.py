#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:30:56 2026

@author: paratusalcantara
"""

# import sys
# !{sys.executable} -m pip install pypdf
from pypdf import PdfReader, PdfWriter

n = 64
src = "cornell_marked0.pdf"# https://printsheet.io/cornell
out = "cornell_"+str(n)+"pages_m.pdf"

reader = PdfReader(src)
writer = PdfWriter()

for _ in range(n):
    for page in reader.pages:
        writer.add_page(page)

with open(out, "wb") as f:
    writer.write(f)