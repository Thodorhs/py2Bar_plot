#!/bin/bash
python3 plot.py
epstopdf plot.eps --outfile=plot.pdf 
pdfcrop plot.pdf
