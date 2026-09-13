#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:36:01 2026

@author: paratusalcantara
"""

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import black
from io import BytesIO

input_file = "cornell.pdf"
output_file = "cornell_marked0.pdf"

quote = """Cultivate students’ personal and intellectual growth, fostering the whole student.<br/>On the stage or field, in makerspaces and living communities, MIT is where brilliant, committed, creative people come together to learn, work, live, and play.<br/>Collaborative, hands-on, curiosity-driven ethos."""

reader = PdfReader(input_file)
writer = PdfWriter()

for page in reader.pages:

    width = float(page.mediabox.width)
    height = float(page.mediabox.height)

    packet = BytesIO()

    c = canvas.Canvas(packet, pagesize=(width, height))

    style = ParagraphStyle(
        "quote",
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=black,
        alignment=TA_LEFT,
    )

    # Width available for the quote
    text_width = width - 270

    paragraph = Paragraph(quote, style)

    # Height is calculated automatically
    _, text_height = paragraph.wrap(text_width, height)

    # Position: 40 points from left, 40 points from top
    x = 250
    y = height - 20 - text_height

    paragraph.drawOn(c, x, y)

    c.save()
    packet.seek(0)

    overlay = PdfReader(packet).pages[0]

    page.merge_page(overlay)
    writer.add_page(page)

with open(output_file, "wb") as f:
    writer.write(f)

print("Created:", output_file)