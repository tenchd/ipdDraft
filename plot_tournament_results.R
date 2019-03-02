#takes an csv file containing results of an IPD tournament and plots the scores of the submissions.  very early version, just for testing.
library(tidyverse)

ipd = read_csv("overall_results.csv")
match = read_csv("matchup_results.csv")

ggplot(data=ipd) +
  geom_col(mapping = aes(x = name, y = score, fill = name)) + theme(legend.position="none")
ggsave(filename = "overall_scores.pdf")

ggplot(data=match) + facet_wrap(~ game_num) + geom_col(mapping = aes(x = player, fill = name, y = score)) + 
  geom_text(aes(x = player, y = 0, label = name, vjust=-0.25)) +
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank(), legend.position = "none")
ggsave(filename = "matchups.pdf")  
  
