#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:47:37 2019

@author: David Tench
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
    f.write("game_num, name, score, player\n")
    for game in games:        
        f.write("{},{},{}, 1\n".format(game.game_num, game.name1, game.score1))
        f.write("{},{},{}, 2\n".format(game.game_num, game.name2, game.score2))
    f.close()
    
    copyfile("matchup_results.csv", filepath + "/matchup_results.csv")

def write_history(games, filepath):
    game = games[4]
    f = open("game_history.csv", 'w')
    f.write("round, player, move\n")
    for i in range(len(game.history)):
        moves = game.history[i][0]
        f.write("{},{},{}\n".format(i+1, game.name1, game.move_namer(moves[0])))
        f.write("{},{},{}\n".format(i+1, game.name2, game.move_namer(moves[1])))
    f.close()
    
    copyfile("game_history.csv", filepath + "/game_history.csv")
        

    
def write_results(strategies, games):
    filepath = generate_dirname()
    os.mkdir(filepath)
    write_overall(strategies, filepath)
    write_matchups(games, filepath)
    write_history(games, filepath)