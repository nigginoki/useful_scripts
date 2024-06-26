#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:18:29 2021

@author: nicholas
"""
import tkinter 
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(result_name):
    pdf_writer = PdfFileWriter()
    root = tkinter.Tk()
    files = filedialog.askopenfilenames(parent=root,title='Choose PDFs !')
    for file in root.tk.splitlist(files):
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(result_name, 'wb') as out:
        pdf_writer.write(out)
        print("PDF-Datei created sucessfully.")
merge_pdfs('merged.pdf')
