numrolls <- function(k, n, s){
  i <- seq.int(from = 0, to = (k-n)%/%s )
  sum((-1)**i * choose(n, i) * choose(k - s*i - 1, k - s*i - n))
}

rolldice_sum_prob <- function(sum_, dice_amount, sides = 6){
  numrolls(sum_, dice_amount, sides)/sides**dice_amount
}
