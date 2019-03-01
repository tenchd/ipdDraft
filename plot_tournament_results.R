#takes an csv file containing results of an IPD tournament and plots the scores of the submissions.  very early version, just for testing.
library(tidyverse)

ipd = read_csv("test.csv")

ggplot(data=ipd) +
  geom_col(mapping = aes(x = name, y = score))
ggsave(filename = "test.pdf")
