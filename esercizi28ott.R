# Esercizio 1 ####

x <- readline(prompt="Inserisci un intero x: ")
x <- as.integer(x)

is_prime <- function(num) {
  if (num == 2) {
    TRUE
  } else if (any(num %% 2:(num-1) == 0)) {
    FALSE
  } else { 
    TRUE
  }
}
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


# Esercizio 2 ####

cnt <- 1

while (cnt < 10) {
  outputMsg <- paste("This is loop number: ", cnt)
  print(outputMsg)
  cnt <- cnt + 1
}


# Esercizio 3 ####

v <- seq(1,20,by=2)
print(v)
for (x in v){
  pow <- x*x
  outputMsg <- paste("The square of X is: ", pow)
  print(outputMsg)
}


# Esercizio 4 ####

x <- 0
while (x<=5) {
  x <- as.integer(readline(prompt="Inserisci un numero maggiore di 5: "))
}
matrice <- matrix(0, nrow = x, ncol = x)
for (i in 1:x){
  for (j in 1:x){
    prod <- i*j
    matrice[i, j] <- prod
  }
}
View(matrice)


# Esercizio 5 ####

sottomatrice <- matrice[0:5,0:5]
View (sottomatrice)


# Esercizio Data Structure 1 ####

# genero i numeri random e matrice 15x7
righe <- 15
colonne <- 7
rand <- sample(1:1000, righe*colonne)
matriceRandom <- matrix(rand, nrow = righe, ncol = colonne)
View(matriceRandom)
# estrapolo la colonna 1 e 3 insieme
df_matriceRandom <- matriceRandom[,c(1,3)]
View(df_matriceRandom)
# seleziono tutti gli elementi < 20 dalla colonna 1
df_sottomatrice <- df_matriceRandom[which(df_matriceRandom[,1]<20), select=1]
View(df_sottomatrice)
# eseguo la somma delle colonne e le inserisco in un vettore
sommaColonne <- colSums(matriceRandom)
sommaColonne
length(sommaColonne)
# sottomatrice con valori < 100
sottomatrice100 = matriceRandom[which(matriceRandom>100)]
View(sottomatrice100)
# sottomatrice con 100<=valori<=200
sottomatrice200 = matriceRandom[which(matriceRandom>=100 & matriceRandom<=200)]
View(sottomatrice200)
# diagonale sottomatrice 7x7
sottomatrice7x7 <- diag(matriceRandom[0:7,0:7])
View(sottomatrice7x7)
