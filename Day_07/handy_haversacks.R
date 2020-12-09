library(tidyverse)
library(igraph)

input_graph <- read_delim("Day_07/input.txt", delim = "\n", col_names = "bag") %>%
    separate(bag, c("from", "to"), sep = " contain ") %>%
    separate_rows(to, sep = ", ") %>%
    mutate(from = sub(" bag.*", "", from),
           to = sub(" bag.*", "", to)) %>%
    filter(to != "no other") %>%
    separate(to, into = c("weight", "to"), sep = "(?<=\\d) ", convert = TRUE) %>%
    relocate(weight, .after = to) %>%
    graph_from_data_frame()

# Day 7.1
ego_size(input_graph, order = length(V(input_graph)), nodes = "shiny gold", mode = "in", mindist = 1)

# Day 7.2
paths <- all_simple_paths(input_graph, from = "shiny gold")
lapply(paths, function(path) {
    edges_of_path <- get.edge.ids(input_graph, rep(path, times = c(1, rep(2, length(path)-2), 1)))
    prod(E(input_graph)$weight[edges_of_path])
}) %>%
    unlist() %>%
    sum()
    