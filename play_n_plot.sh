#!/bin/sh
#runs an ipd tournament and plots the results in a pdf
python ipd.py
Rscript plot_tournament_results.R
rm Rplots.pdf
