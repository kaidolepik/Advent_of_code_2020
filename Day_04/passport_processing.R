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
    mutate(valid_byr = byr >= 1920 & byr <= 2002,
           valid_iyr = iyr >= 2010 & iyr <= 2020,
           valid_eyr = eyr >= 2020 & eyr <= 2030,
           valid_hgt = ifelse(grepl("cm", hgt), substr(hgt, 1, nchar(hgt)-2) >= 150 & substr(hgt, 1, nchar(hgt)-2) <= 193,
                              ifelse(grepl("in", hgt), substr(hgt, 1, nchar(hgt)-2) >= 59 & substr(hgt, 1, nchar(hgt)-2) <= 76, NA)),
           valid_hcl = grepl("#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$", hcl),
           valid_ecl = grepl("^(amb|blu|brn|gry|grn|hzl|oth)$", ecl),
           valid_pid = grepl("^\\d\\d\\d\\d\\d\\d\\d\\d\\d$", pid),
           valid_cid = TRUE) %>%
    filter(valid_byr, valid_iyr, valid_eyr, valid_hgt, valid_hcl, valid_ecl, valid_pid, valid_cid) %>%
    nrow()
