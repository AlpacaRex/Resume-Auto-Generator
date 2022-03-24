import tkinter as tk
from tkinter import ttk
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import toLength, cm
import math


def figure_font(eduExpList1, eduExpList2, workExpList1, workExpList2, tech, eva):
    a = float(len(tech)+len(eva))/527.0*1.5
    b = 1.5*(eduExpList1.size() + workExpList1.size()+4+3*5)
    c = -780
    font = ((-b+math.sqrt(b**2-4*a*c))/(2*a))
    if font > 20:
        return 20

    return font


def makepdf(name, edu, age, tel, sex, email, eduExpList1, eduExpList2, workExpList1, workExpList2, tech, eva):
    pdfmetrics.registerFont(TTFont('fzlt', '字体/FZLTHJW.TTF'))
    font = figure_font(eduExpList1, eduExpList2, workExpList1, workExpList2, tech, eva)
    print(font)
    print(eduExpList1.size())
    print(eduExpList1.size())
    print(float(len(tech)*font/527))
    print(float(len(eva)*font/527))
    print(" ")
    story = []

    doc = SimpleDocTemplate("简历.pdf", leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm)

    styles = getSampleStyleSheet()  # 获得reportlab预先设定的文本模板
    styles.add(ParagraphStyle(name='title1', alignment=TA_JUSTIFY, fontName="fzlt", fontSize=2*font, wordWrap="CJK"))
    styles.add(ParagraphStyle(name="title2", alignment=TA_JUSTIFY, fontName="fzlt", fontSize=1.5*font, wordWrap="CJK"))
    styles.add(ParagraphStyle(name="para", alignment=TA_JUSTIFY, fontName="fzlt", fontSize=font, wordWrap="CJK", leading=1.5*font))

    text = '''<para><br/>个人简历</para>'''
    story.append(Paragraph(text, styles["title1"]))
    story.append(Spacer(100, 2*font))
    text = '''<para><br/>基本信息</para>'''
    story.append(Paragraph(text, styles["title2"]))
    story.append(Spacer(100, 1.5*font))


    table_style = [
        ('FONTNAME', (0, 0), (-1, -1), 'fzlt'),
        ('FONTSIZE', (0, 0), (-1, -1), font),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

    ]
    table_data = [['姓名：', name, '学历：', edu],
                  ['年龄：', age, '电话：', tel],
                  ['性别：', sex, '邮箱：', email],
                  ]
    # 生成表格
    table_table = Table(table_data, colWidths=font*5, rowHeights=font*1.5, style=table_style, hAlign='LEFT')
    story.append(table_table)

    text = '''<para><br/>教育背景</para>'''
    story.append(Paragraph(text, styles["title2"]))
    story.append(Spacer(100, 1.5*font))

    for index in range(eduExpList1.size()):
        text = eduExpList1.get(index) + "  " + eduExpList2.get(index)
        story.append(Paragraph(text, styles["para"]))

    text = '''<para><br/>工作经历</para>'''
    story.append(Paragraph(text, styles["title2"]))
    story.append(Spacer(100, 1.5*font))

    for index in range(workExpList1.size()):
        text = workExpList1.get(index) + " " + workExpList2.get(index)
        story.append(Paragraph(text, styles["para"]))

    text = '''<para><br/>技能特长</para>'''
    story.append(Paragraph(text, styles["title2"]))
    story.append(Spacer(100, 1.5*font))

    story.append(Paragraph(tech, styles["para"]))

    text = '''<para><br/>自我评价</para>'''
    story.append(Paragraph(text, styles["title2"]))
    story.append(Spacer(100, 1.5*font))

    story.append(Paragraph(eva, styles["para"]))
    doc.build(story)
