#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:29:10 2019

@author: devd
"""

import deciders as d

#This is an example file a participant would submit for the tournament.
#The participant defines a decider function and instantiates a submission
#object with it.  That's pretty much it.  You can rename this file, replacing
#the decider and names with your own, and email it to me.

#encode "Cooperate" actions as C and "Defect" actions as D.  This convention
#holds for the actions that deciders return, as well as history entries.
C = 0
D = 1

def davidsDecider(history):
    """An example decider that cooperates until the opponent defects, and then
    defects forever."""
    #return C on first round
    if not history:
        return C
    else:
        #if either player defected last round, return D.
        if history[-1][0] or history [-1][1]:
            return D
        else:
            #else no one has ever defected.  return C.
            return C

davidsSubmission = d.Submission(davidsDecider, "revengebot", "david")