find_short <- function(s){
  min(nchar(unlist(strsplit(s, " "))))
}
