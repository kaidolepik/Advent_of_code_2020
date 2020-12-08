library(tidyverse)

input <- read.table(text = gsub("(-|: )", " ", readLines("Day_02/input.txt")),
                    col.names=c("min", "max", "letter", "password"), stringsAsFactors = FALSE)

# Day 1
input %>%
    mutate(count = str_count(password, letter)) %>%
    filter(count >= min & count <= max) %>%
    nrow()

# Day 2
input %>%
    mutate(count = (substr(password, min, min) == letter) + (substr(password, max, max) == letter)) %>%
    filter(count == 1) %>%
    nrow()
