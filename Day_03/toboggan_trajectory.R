library(tidyverse)

N_trees <- function(input, right = 3, down = 1) {
    trajectory <- data.frame(row = seq(1, nrow(input), down)) %>%
        mutate(extended_col = seq(1, n()*right, right),
               col = extended_col %% ncol(input),
               col = ifelse(col == 0, ncol(input), col))
    
    sum(as.matrix(input)[as.matrix(trajectory[, c("row", "col")])] == "#")
}

input <- scan("/Users/kaidolepik/Desktop/Project/Advent_of_code/Day_03/input.txt", what = "character") %>%
    str_split(pattern = "") %>%
    lapply(as.data.frame.list) %>%
    data.table::rbindlist()

# Day 3.1
N_trees(input)

# Day 3.2
prod(c(N_trees(input, 1, 1), N_trees(input, 3, 1), N_trees(input, 5, 1), 
       N_trees(input, 7, 1), N_trees(input, 1, 2)))
