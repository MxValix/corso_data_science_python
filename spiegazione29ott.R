# DATAFRAME ####

v1 <- c(1,2,3)
v2 <- c("a")
v3 <- c(T,F,T)
v4 <- c(4,5,6)
v5 <- c("d","e","f")

DS <- data.frame(v1,v2,v3,v4,v5)
View(DS)
str(DS)
dim(DS)
nrow(DS)
ncol(DS)

rownames(DS) <- c("rowA", "rowB", "rowC")
names(DS) <- c("colA", "colB", "colC", "colD", "colE")

DS[c("rowA"),c("colC")]

# LIST ####

o1 <- c(1,2,3)
o2 <- c("a","b","c","d")
o3 <- c(T,F,T,T,F)

list1 <- list(o1,o2,o3) 
View(list1)

list2 <- list(o1,o2,o2,list1)
View(list2)

list1[1]
list2[4]

names(list1) <- c("first","second","third")
list1

View(list1)

list1[c("second")]
list1$second
str(list1)
typeof(list1$third)

movies <- c("SPIDERMAN", "BATMAN", "VERTIGO", "CHINATOWN")
movies_lower <- lapply(movies,tolower)
str(movies_lower)
View(movies_lower)

# SAPPLY ####
data(movies)
View (movies)

dt <- movies
sum_movies <- sapply(dt,min)
sum_movies
sum_movies <- sapply(dt,max)
sum_movies

lmn_movies <- lapply(dt,min)
lmn_movies

lmx_movies <- lapply(dt,max)
lmx_movies
