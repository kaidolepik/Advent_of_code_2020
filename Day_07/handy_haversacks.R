library(tidyverse)
library(igraph)

input <- data.table::fread("Day_07/input.txt", sep = "\n", header = FALSE) %>%
    separate(V1, c("from", "to"), sep = " contain ") %>%
    separate_rows(to, sep = ", ") %>%
    mutate(from = sub(" bag.*", "", from),
           to = sub(" bag.*", "", to))

vertices <- tibble(bag = unique(input$from))
edges <- input %>%
    filter(to != "no other") %>%
    separate(to, into = c("weight", "to"), sep = "(?<=\\d) ", convert = TRUE) %>%
    relocate(weight, .after = to)
g <- graph_from_data_frame(edges, directed = TRUE, vertices)

# Day 7.1
ego_size(g, order = length(V(g)), nodes = "shiny gold", mode = "in", mindist = 1)

# Day 7.2
paths <- all_simple_paths(g, from = "shiny gold")
lapply(paths, function(path) {
    edges_of_path <- get.edge.ids(g, rep(path, times = c(1, rep(2, length(path)-2), 1)))
    prod(E(g)$weight[edges_of_path])
}) %>%
    unlist() %>%
    sum()
    