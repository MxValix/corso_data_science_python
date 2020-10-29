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
