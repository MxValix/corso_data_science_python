library(DBI)
library(RPostgreSQL)
library(odbc)
db_password <- "admin"
drv <- dbDriver("PostgreSQL")
connessione <- dbConnect( drv, 
                          dbname='textmining', 
                          host='localhost', 
                          port=5432, 
                          user = 'postgres',
                          password=  db_password )
dbWriteTable(connessione, "WomenClothing", textmining)
data <- dbReadTable(connessione, "WomenClothing")
View(data)
#boh <- subset(data, Rating < 3)
#View(boh)
distinct_id <- unique(data$Clothing.ID)
d_len <- length(distinct_id)
View(distinct_id)
tmp <- data.frame(Clothing.ID = numeric())
distinct <- data.frame(Clothing.ID = numeric(), Rating = numeric(), Eta = numeric())

for (d in distinct_id){
  tmp <- subset(data, Clothing.ID == d)
  mediaRating <- mean(tmp$Rating)
  mediaAge <- mean(tmp$Age)
  distinct <- rbind(distinct,data.frame(tmp$Clothing.ID,mediaRating,mediaAge))
}
distinct <- unique(distinct)
names(distinct)[1] <- "Clothing.ID"
names(distinct)[2] <- "Rating"
names(distinct)[3] <- "Age"
distinct <- distinct[order(distinct[2]),]
dbWriteTable(connessione,"distinct", distinct)
distinct <- dbReadTable(connessione,"distinct")
View(distinct)
