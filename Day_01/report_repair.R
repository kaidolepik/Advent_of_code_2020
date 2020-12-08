product_of_N_expenses_with_sum <- function(expenses, N = 2, expense_sum = 2020) {
    expense_pairs <- combn(expenses, N)
    
    prod(expense_pairs[, colSums(expense_pairs) == expense_sum])
}

expenses <- scan("Day_01/input.txt")
product_of_N_expenses_with_sum(expenses, 2) # Day 1.1
product_of_N_expenses_with_sum(expenses, 3) # Day 1.2
