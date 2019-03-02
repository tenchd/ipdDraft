#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:47:37 2019

@author: devd
"""

import time as t
import os
from shutil import copyfile

def generate_dirname():
    timestamp = t.asctime(t.gmtime())
    return "records/" + timestamp.replace(' ', '_')

def write_overall(strategies, filepath):
    """Writes results of IPD tournament (participants and total scores to file
    in two locations: one in the working directory for temporary use by the R
    script, and one in the records directory for long-term storage."""
    #filename = generate_filename(filename_keyword)
    f = open("overall_results.csv", 'w')
    f.write("name,author,score\n")
    for strat in strategies:
        f.write("{},{},{}\n".format(strat.name, strat.author, strat.score))
    f.close()
   
    copyfile("overall_results.csv", filepath + "/overall_results.csv")
    

def write_matchups(games, filepath):
    f = open("matchup_results.csv", 'w')
    f.write("name1, name2, score1, score2\n")
    for game in games:        
        f.write("{},{},{},{}\n".format(game.name1, game.name2, game.score1, game.score2))
    f.close()
    
    copyfile("matchup_results.csv", filepath + "/matchup_results.csv")
    
def write_results(strategies, games):
    filepath = generate_dirname()
    os.mkdir(filepath)
    write_overall(strategies, filepath)
    write_matchups(games, filepath)