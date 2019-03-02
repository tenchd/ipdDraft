library(tidyverse)

hist = read_csv("game_history.csv")

ggplot(data=hist) + geom_text(mapping = aes(y = round, x = player, color = move, label = move, size = 10)) + scale_y_reverse() + 
  theme(legend.position = "none", axis.text.x = element_text(size=12))

ggsave(filename="sample_game.pdf")