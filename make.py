#!/usr/bin/python3
import subprocess

latex = ['inflation']

for l in latex:
  subprocess.call(['pdflatex', l])
  subprocess.call(['bibtex', l])
  subprocess.call(['pdflatex', l])
  subprocess.call(['pdflatex', l])
