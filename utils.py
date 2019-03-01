#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:47:37 2019

@author: devd
"""

def write_overall(filename, strategies):
    """Writes results of IPD tournament (participants and total scores to file."""
    f = open(filename, 'w')
    f.write("name,author,score\n")
    for strat in strategies:
        f.write("{},{},{}\n".format(strat.name, strat.author, strat.score))
    f.close()