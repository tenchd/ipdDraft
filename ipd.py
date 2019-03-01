#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:13:59 2019

@author: devd
"""

import deciders as d
from classes import Player, Strategy, Game
import utils as u

C = 0
D = 1

#class Player:
#    """Encapsulates the info about prisoner's dilemma players needed to 
#    simulate games.  All that's required is a decider function, which must
#    rely only on history (and later, once I implement it, the payoffs."""
#    
#    def __init__(self, decider):
#        self.decider = decider
#        self.history = []
#    
#    def decision(self):
#        """This is called by Game each round to determine the player's choice 
#        (Cooperate or Defect) for that round.  Return 0 for Cooperate and 
#        1 for Defect."""
#        return self.decider(self.history)
#    
#    def update_history(self, result):
#        """After a round, this is called by Game to update the player's history
#        of the game so far.  result is a 2-ple containing the player's move 
#        last round, and the opponent's move last round respectively."""
#        self.history.append(result)
#        
#    def see_history(self):
#        """For debugging"""
#        output = [["COOPERATE" if move==C else "DEFECT" for move in round] for round in self.history]
#        print(output)
#
#
#class Strategy:
#    """Keeps track of the performance of a strategy over multiple games.  Is
#    used in each game to instantiate Player objects."""
#    
#    def __init__(self, submission):
#        self.decider = submission.decider
#        self.name = submission.name
#        self.author = submission.author
#        self.score = 0
#    
#    def update_score(self, update):
#        self.score += update        
#        
#
#class Game:
#    """Simulates a Iterated Prisoner's Dilemma game between 2 agents, specified
#    via functions that decide what actions they take given game history."""
#    
#    def __init__(self, strategy1, strategy2, num_rounds, game_num=1, display=False): 
#         self.player1 = Player(strategy1.decider)
#         self.name1 = strategy1.name
#         self.player2 = Player(strategy2.decider)
#         self.name2 = strategy2.name
#         self.num_rounds = num_rounds
#         self.history = []
#         self.score1 = 0
#         self.score2 = 0
#         self.display = display
#         self.game_num = game_num
#    
#    def scores(self, move1, move2):
#        """Assigns scores to the players based on which move they chose.
#        Since Cooperate is encoded as 0 and Defect is coded as 1, we can use
#        player moves as indices for the payoff matrix."""
#        payoffs = [[(3,3),(0,5)],
#                   [(5,0),(1,1)]]
#        return payoffs[move1][move2]
#    
#    def move_namer(self, move):
#        """Converts a move into human-readable form for display."""
#        if move:
#            return "DEFECT"
#        return "COOPERATE"
#    
#    def play_round(self):
#        """Performs a single PD round.  Asks players for their moves, then
#        tells them the results of the move and updates their scores."""
#        move1 = self.player1.decision()
#        m1 = self.move_namer(move1)
#        move2 = self.player2.decision()
#        m2 = self.move_namer(move2)
#        s1, s2 = self.scores(move1, move2)
#        self.score1 += s1
#        self.score2 += s2
#        if self.display:
#            print("{} played {} for {} points and {} played {} for {} points".format(self.name1, m1, s1, self.name2, m2, s2))
#        self.history.append(((move1, move2), (self.score1, self.score2)))
#        self.player1.update_history((move1, move2))
#        #player 2 needs the moves reversed for their history
#        self.player2.update_history((move2, move1))
#    
#    def play(self):
#        """Plays the entire set of rounds between the two players, then returns
#        the final scores to their Strategy objects."""
#        for i in range(self.num_rounds):
#            if self.display:
#                print("playing round {}".format(i+1))
#            self.play_round()
#        print("Game {}: {} got {} points and {} got {} points.".format(self.game_num, self.name1, self.score1, self.name2, self.score2))
#        return(self.score1, self.score2)


def tournament(submissions, num_rounds):
    """Given a list of strategies, plays a round-robin tournament between all pairs of strategies
    and reports the overall scores of each strategy as well as the result of each game."""
    strategies = [Strategy(submission) for submission in submissions]
    game_num = 1
    for i in range(len(strategies)):
        for j in range(i+1, len(strategies)):
            #print(strategies[i].name, strategies[j].name)
            g = Game(strategies[i], strategies[j], num_rounds, game_num)
            score1, score2 = g.play()
            strategies[i].update_score(score1)
            strategies[j].update_score(score2)
            game_num += 1
    
    for strat in strategies:
        print("Final score for {} submitted by {} is {}".format(strat.name, strat.author, strat.score))
    u.write_overall("test.csv", strategies)
            
        
if __name__ == '__main__': 
    
#    test_game = Game(Strategy(d.randomSubmission), Strategy(d.tftSubmission), 10, display=True)
#    test_game.play()
#                
#    test_game2 = Game(Strategy(d.randomSubmission), Strategy(d.alternatorSubmission), 10, display = True)
#    test_game2.play()
    
    submissions = [d.randomSubmission, d.tftSubmission, d.alternatorSubmission,
                   d.acSubmission, d.adSubmission]
           
    tournament(submissions, 10)