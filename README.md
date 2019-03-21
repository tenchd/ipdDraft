# ipdTournament

For an overview of this project and the tournament, read the [wiki](https://github.com/tenchd/ipdTournament/wiki/Iterated-Prisoner's-Dilemma-Tournament:--Motivation-&-Details).

## How to Write a Submission

Make a copy of example_submission.py and use it as a template to create your own decider.  example_submission.py has detailed instructions in its comments.  You can email your modified copy of this template to me to enter it in the tournament (please rename the file!).

If you want to test your creation against some simple strategies, import your submission in ipd.py and add your submission object to the list of submissions in the main function of ipd.py.  Then run ipd.py.

## Visualization

Users who have access to a bash terminal and have R installed can run play_n_plot.sh to run a dummy tournament and generate charts summarizing the results as seen in the sample_charts directory.  Requires installation of tidyverse package for R.
