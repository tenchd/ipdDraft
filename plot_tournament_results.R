library(tidyverse)

ipd = read_csv("test.csv")

ggplot(data=ipd) +
  geom_col(mapping = aes(x = name, y = score))
ggsave(filename = "test.pdf")
