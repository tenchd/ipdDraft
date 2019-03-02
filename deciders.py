#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:06:53 2019

@author: David Tench
"""

import random as rand

#encode "Cooperate" actions as C and "Defect" actions as D.  This convention
#holds for the actions that deciders return, as well as history entries.
C = 0
D = 1


class Submission:
    """Use this class to create submissions for IPD tournaments.
    Implement a decider function, and add a display name for the decider as
    well as your name as author.  These will be displayed in tournament results.
    """
    
    def __init__(self, decider, name, author):
        self.decider = decider
        self.name = name
        self.author = author

#See below for examples of submissions based on different decider functions.

#deciders must rely only on history, a list containing the moves played by each player in prior rounds.
#history[i] contains a 2ple (m1, m2) where m1 is the action the decider took in round
# i+1 and m2 is the action the opponent took in round i+1.

def randomDecider(history):
    """This decider ignores all past history and chooses from Cooperate or
    Defect uniformly at random."""
    return rand.getrandbits(1)

randomSubmission = Submission(randomDecider, "randy", "library")


def titForTat(history):
    """This decider Cooperates on round 1 and otherwise does whatever the
    opponent did last round."""
    if not history:
        return C
    else:
        return history[-1][1]

tftSubmission = Submission(titForTat, "taft", "library")


def alwaysCooperate(history):
    """Always returns cooperate."""
    return C

acSubmission = Submission(alwaysCooperate, "cooper", "library")


def alwaysDefect(history):
    """Always defects."""
    return D

adSubmission = Submission(alwaysDefect, "detlef", "library")


def alternator(history):
    """Alternates between cooperating and defecting."""
    if not history:
        return C
    else:
        if history[-1][0]:
            return C
        return D
    
alternatorSubmission = Submission(alternator, "nate", "library")