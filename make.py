#!/usr/bin/python3
import subprocess

subprocess.call(['bibtex', 'inflation'])
subprocess.call(['pdflatex', 'inflation.tex'])
# subprocess.call(['pdflatex', 'inflation.tex'])
# subprocess.call(['pdflatex', 'inflation.tex'])
