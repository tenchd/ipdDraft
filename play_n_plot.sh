#!/bin/sh
python ipd.py
Rscript plot_tournament_results.R
rm Rplots.pdf
