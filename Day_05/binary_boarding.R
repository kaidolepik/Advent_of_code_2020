library(tidyverse)

input <- read_table("/Users/kaidolepik/Desktop/Project/Advent_of_code/Day_05/input.txt", col_names = "seat") %>%
    separate(seat, c("row", "col"), sep = 7) %>%
    mutate(row = strtoi(str_replace_all(row, c("F" = "0", "B" = "1")), base = 2),
           col = strtoi(str_replace_all(col, c("L" = "0", "R" = "1")), base = 2),
           seat_id = 8*row + col) %>%
    arrange(seat_id)

max(input$seat_id) # Day 5.1
input$seat_id[diff(input$seat_id) != 1] + 1 # Day 5.2
