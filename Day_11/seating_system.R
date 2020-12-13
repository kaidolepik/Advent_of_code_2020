library(tidyverse)

find_left <- function(mat, row, col) {
    ifelse(col == 1, NA, mat[row, rev(which(!is.na(mat[row, 1:(col-1)])))[1]])
}

find_right <- function(mat, row, col) {
    ifelse(col == ncol(mat), NA, mat[row, col + which(!is.na(mat[row, (col+1):ncol(mat)]))[1]])
}

find_top <- function(mat, row, col) {
    find_left(t(mat), col, row)
}

find_bottom <- function(mat, row, col) {
    find_right(t(mat), col, row)
}

find_top_left <- function(mat, row, col) {
    start_row <- 1 + (row - col)*(row > col)
    start_col <- 1 + (col - row)*(col > row)
    pos <- ifelse(row == 1 || col == 1, NA, rev(which(!is.na(diag(mat[start_row:(row-1), start_col:(col-1), drop = FALSE]))))[1])
    
    mat[start_row + pos - 1, start_col + pos - 1]
}

find_bottom_right <- function(mat, row, col) {
    pos <- ifelse(row == nrow(mat) || col == ncol(mat), NA, which(!is.na(diag(mat[(row+1):nrow(mat), (col+1):ncol(mat), drop = FALSE])))[1])
    
    mat[row + pos, col + pos]
}

find_top_right <- function(mat, row, col) {
    find_bottom_right(mat[nrow(mat):1, ], nrow(mat) - row + 1, col)
}

find_bottom_left <- function(mat, row, col) {
    find_bottom_right(mat[, ncol(mat):1], row, ncol(mat) - col + 1)
}

adjacent_seats_day1 <- function(mat) {
    left <- cbind(NA, mat[, -ncol(mat)])
    right <- cbind(mat[, -1], NA)
    top <- rbind(NA, mat[-nrow(mat), ])
    bottom <- rbind(mat[-1, ], NA)
    top_left <- rbind(NA, cbind(NA, mat[-nrow(mat), -ncol(mat)]))
    bottom_left <- rbind(cbind(NA, mat[-1, -ncol(mat)]), NA)
    top_right <- rbind(NA, cbind(mat[-nrow(mat), -1], NA))
    bottom_right <- rbind(cbind(mat[-1, -1], NA), NA)
    
    list(left, right, top, bottom, top_left, bottom_left, top_right, bottom_right)
}

adjacent_seats_day2 <- function(mat) {
    left <- right <- top <- bottom <- top_left <- bottom_right <- top_right <- bottom_left <- matrix(NA, nrow = nrow(mat), ncol = ncol(mat))
    for (row in 1:nrow(mat)) {
        for (col in 1:ncol(mat)) {
            if (is.na(mat[row, col]))
                next
            left[row, col] <- find_left(mat, row, col)
            right[row, col] <- find_right(mat, row, col)
            top[row, col] <- find_top(mat, row, col)
            bottom[row, col] <- find_bottom(mat, row, col)
            top_left[row, col] <- find_top_left(mat, row, col)
            bottom_right[row, col] <- find_bottom_right(mat, row, col)
            top_right[row, col] <- find_top_right(mat, row, col)
            bottom_left[row, col] <- find_bottom_left(mat, row, col)
            # Could also just change row/col order and use only find_right/find_bottom_right
        }
    }
    
    list(left, right, top, bottom, top_left, top_right, bottom_left, bottom_right)
}

seat_sim <- function(mat, adjacent_func, criteria) {
    adjacent_sum <- Reduce("+", lapply(adjacent_func(mat), function(x) replace(x, is.na(x), 0)))
    
    new_mat <- mat
    new_mat[!is.na(mat) & mat == 0 & adjacent_sum == 0] <- 1
    new_mat[!is.na(mat) & mat == 1 & adjacent_sum >= criteria] <- 0
    
    if (all(mat == new_mat, na.rm = TRUE))
        return(mat)
    else
        return(seat_sim(new_mat, adjacent_func, criteria))
}

mat <- read_file("/Users/kaidolepik/Desktop/Project/Advent_of_code/Day_11/input.txt") %>%
    str_replace_all(c("L" = " FALSE ", "\\." = " NA ")) %>%
    data.table::fread() %>%
    as.matrix()

sum(seat_sim(mat, adjacent_seats_day1, criteria = 4), na.rm = TRUE) # Day 11.1
sum(seat_sim(mat, adjacent_seats_day2, criteria = 5), na.rm = TRUE) # Day 11.2
