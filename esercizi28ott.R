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

#ifelse(x %% 2 == 0,"È pari","È dispari")

if (x%%2 == 0) {
  print("È pari")
} else {
  print("È dispari")
}
if (is_prime(x)){
  print("è primo")
  for (i in c(2:x-1)){
    if (is_prime(i)){
      print(i)
    }
  }
} else {
  print("non è primo")
}

# Esercizio 2

cnt <- 1

while (cnt < 10) {
  outputMsg = paste("This is loop number: ", cnt)
  print(outputMsg)
  cnt = cnt + 1
}


# Esercizio 3

v <- seq(1,20,by=2)
print(v)
for (x in v){
  pow = x*x
  outputMsg = paste("The square of X is: ", pow)
  print(outputMsg)
}
