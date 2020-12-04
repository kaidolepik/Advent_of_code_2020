library(tidyverse)

input <- read_file("/Users/kaidolepik/Desktop/Project/Advent_of_code/Day_04/input.txt") %>%
    str_replace_all(c("(?<!\n)\n(?!(\n|$))" = " ", "\n\n" = "\n")) %>%
    data.table::fread(fill = TRUE, na.strings = "", header = FALSE) %>%
    rownames_to_column("id") %>%
    pivot_longer(cols = V1:V8, names_to = "col", values_to = "key_value_pair", values_drop_na = TRUE) %>%
    separate(key_value_pair, c("key", "value"), sep = ":") %>%
    pivot_wider(id_cols = id, names_from = key, values_from = value) %>%
    select(-id)

# Day 4.1
sum(rowSums(is.na(input)) == 0 | (rowSums(is.na(input)) == 1 & is.na(input$cid)))

# Day 4.2
input %>%
    filter(between(byr, 1920, 2002),
           between(iyr, 2010, 2020),
           between(eyr, 2020, 2030),
           grepl("^\\d+cm$", hgt) & between(substr(hgt, 1, nchar(hgt)-2), 150, 193) | grepl("^\\d+in$", hgt) & between(substr(hgt, 1, nchar(hgt)-2), 59, 76),
           grepl("^#[0-9a-f]{6}$", hcl),
           grepl("^(amb|blu|brn|gry|grn|hzl|oth)$", ecl),
           grepl("^\\d{9}$", pid)) %>%
    nrow()
