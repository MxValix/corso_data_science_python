# Esercizio 1 #######

is_prime <- function(num) {
  if (num == 2) {
    TRUE
  } else if (any(num %% 2:(num-1) == 0)) {
    FALSE
  } else { 
    TRUE
  }
}

x <- readline(prompt="Inserisci un intero x: ")
x <- as.integer(x)

ifelse(x %% 2 == 0,"È pari","È dispari")

if (x%%2 == 0) {
  print("È pari")
} else {
  print("È dispari")
}
if (is_prime(x)){
  print("è primo")
} else {
  print("non è primo")
}
