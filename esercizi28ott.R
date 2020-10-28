# Esercizio 1 #######

x <- readline(prompt="Inserisci un intero x: ")
x <- as.integer(x)

ifelse(x %% 2 == 0,"È pari","È dispari")

if (x%%2 == 0) {
  print("È pari")
} else {
  print("È dispari")
}