#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:13:59 2019

@author: David Tench
"""

import deciders as d
from classes import Strategy, Game
from utils import write_results


def tournament(submissions, num_rounds):
    """Given a list of strategies, plays a round-robin tournament between all pairs of strategies
    and reports the overall scores of each strategy as well as the result of each game."""
    strategies = [Strategy(submission) for submission in submissions]
    game_num = 1
    games = []
    for i in range(len(strategies)):
        for j in range(i+1, len(strategies)):
            #print(strategies[i].name, strategies[j].name)
            g = Game(strategies[i], strategies[j], num_rounds, game_num)
            score1, score2 = g.play()
            strategies[i].update_score(score1)
            strategies[j].update_score(score2)
            game_num += 1
            games.append(g)
    
    for strat in strategies:
        print("Final score for {} submitted by {} is {}".format(strat.name, strat.author, strat.score))
    write_results(strategies, games)
            
        
if __name__ == '__main__': 
    
#    test_game = Game(Strategy(d.randomSubmission), Strategy(d.tftSubmission), 10, display=True)
#    test_game.play()
#                
#    test_game2 = Game(Strategy(d.randomSubmission), Strategy(d.alternatorSubmission), 10, display = True)
#    test_game2.play()
    
    submissions = [d.randomSubmission, d.tftSubmission, d.alternatorSubmission,
                   d.acSubmission, d.adSubmission]
           
    tournament(submissions, 20)