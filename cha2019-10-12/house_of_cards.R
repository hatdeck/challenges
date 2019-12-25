house_of_cards <- function(floors){
  if (floors < 1) stop("input must be greater than 0")
  (floors + 1)*(3*(floors + 1) + 1)/2
}
