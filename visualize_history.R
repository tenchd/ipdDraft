#author: David Tench
#creates a visual representation of the moves chosen by both players in an IPD game.  early version, for testing

library(tidyverse)

#load game history
hist = read_csv("game_history.csv")

#plot history
ggplot(data=hist) + geom_text(mapping = aes(y = round, x = player, color = move, label = move, size = 10)) + scale_y_reverse() + 
  theme(legend.position = "none", axis.text.x = element_text(size=12))

ggsave(filename="sample_game.pdf")