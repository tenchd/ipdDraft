# ipdTournament

## Introduction

The Prisoner's Dilemma is a famous game studied in game theory where rational players are incentivized against cooperation, even though mutual cooperation could lead to greater rewards.  This raises questions about human behavior - if defection is rational, why do humans so often cooperate in similar situations?  Are we irrational, or does the thought experiment fail to capture important factors guiding human behavior?

[Wikipedia](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma) suggests an answer:

>It is implied that the prisoners will have no opportunity to reward or punish their partner other than the prison sentences they get and that their decision will not affect their reputation in the future. Because betraying a partner offers a greater reward than cooperating with them, all purely rational self-interested prisoners will betray the other, meaning the only possible outcome for two purely rational prisoners is for them to betray each other.[2] The interesting part of this result is that pursuing individual reward logically leads both of the prisoners to betray when they would get a better reward if they both kept silent. In reality, humans display a systemic bias towards cooperative behavior in this and similar games despite what is predicted by simple models of "rational" self-interested action.[3][4][5][6]

>An extended "iterated" version of the game also exists. In this version, the classic game is played repeatedly between the same prisoners, who continuously have the opportunity to penalize the other for previous decisions. If the number of times the game will be played is known to the players, then (by backward induction) two classically rational players will betray each other repeatedly, for the same reasons as the single-shot variant. In an infinite or unknown length game there is no fixed optimum strategy, and prisoner's dilemma tournaments have been held to compete and test algorithms for such cases.[7] 

This repo is the framework for an iterated Prisoner's Dilemma (hereafter IPD) tournament.  You can write + submit a strategy and have it compete!

## How the Tournament Will Work

### Structure

Each pair of user submissions will compete in an IPD game with standard payoffs, lasting for an unspecified number of rounds (think double digits).  At the end of the game the "points" each player has earned from their payoffs are added to a running total for their strategy.  The strategy with the highest average point total after all pairs of strategies have competed is the winner.

### Rules

1. Don't be a jerk.  This competition is entirely for fun and there is no prize for winning other than bragging rights.  I'm an amateur and these rules won't cover every possible misdeed.  Use your best judgment, ask for clarification if necessary, etc.

2. Submissions, which amount to implementations of a decider function, should rely only on the game history to choose actions.  They should NOT use other meta-information about the tournament: the identity of their opponent, their opponent's source code, other player's overall scores, etc.

3. There is currently no limit on the number of entries any person can submit.  This rule may be subject to change based on how many submissions I get (I may impose a limit on submissions/person, or prevent a submitter's multiple strategies from playing against each other).

4. If you want to use packages/libraries that don't come standard with Python 3.7, let me know so I can makes sure to have them set up before the tournament.

5. Please don't share your submissions with other participants before the competition if you can avoid it.  It'll be more interesting if everyone is coming in blind.

### Submitting

At the moment I'm just planning to have people email me submissions at dtench@protonmail.ch.  Put "IPDSUBMISSION" in the subject line please.  Format for submissions TBD.

In the meantime, email me to be added to an email list for announcements.

Deadline for submissions (and therefore the tournament date itself) TBD.

### Future Directions

If people enjoy this tournament, I may do it again with more complicated rules in the future.  Possible modifications include:
* varying payoffs 
* allowing some sort of communication between players during a game
* an evolutionary modeling scenario where strategies reproduce by getting points and attempt to outnumber other strategies

If you have ideas be sure to let me know!

## How to Write a Submission

If you want to test out a strategy, add it as a Submission object in the deciders.py file (which also contains examples you can start from), then add that submission object to the list of submissions in the main function of ipd.py.  Then run ipd.py.

## Visualization

Users who have access to a bash terminal and have R installed can run play_n_plot.sh to run a dummy tournament and generate charts summarizing the results.  Requires installation of tidyverse package for R.
