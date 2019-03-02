#takes an csv file containing results of an IPD tournament and plots the scores of the submissions.  very early version, just for testing.
library(tidyverse)

ipd = read_csv("overall_results.csv")
match = read_csv("matchup_results.csv")

ggplot(data=ipd) +
  geom_col(mapping = aes(x = name, y = score))
ggsave(filename = "test.pdf")

#ggplot(data=match) + facet_wrap(~ name1 + name2) + geom_col(mapping = aes(x = name1, y = score1)) + geom_col(mapping = aes(x = name2, y = score2))
  