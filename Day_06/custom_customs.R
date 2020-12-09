library(tidyverse)

input <- read_file("Day_06/input.txt") %>%
    str_replace_all(c("(?<!\n)\n(?!(\n|$))" = " ", "\n\n" = "\n")) %>%
    read_table(col_names = "form") %>%
    rownames_to_column("id") %>%
    mutate(N_group = str_count(form, " ") + 1) %>%
    separate_rows(form, sep = "") %>%
    filter(!form %in% c(" ", ""))

# Day 6.1
input %>%
    unique() %>%
    nrow()

# Day 6.2
input %>%
    group_by(id, form, N_group) %>%
    summarize(N_form = n()) %>%
    filter(N_form == N_group) %>%
    nrow()
