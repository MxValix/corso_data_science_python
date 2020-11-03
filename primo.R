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
distinct_id <- unique(data$Clothing.ID)
d_len <- length(distinct_id)
View(distinct_id)
tmp <- data.frame(Clothing.ID = numeric())
distinct <- data.frame(Clothing.ID = numeric(), Rating = numeric())

for (d in distinct_id){
  tmp <- subset(data, Clothing.ID == d)
  media <- mean(tmp$Rating)
  distinct <- rbind(distinct,data.frame(tmp$Clothing.ID,media))
}
distinct <- unique(distinct)
names(distinct)[1] <- "Clothing.ID"
names(distinct)[2] <- "Rating"
dbWriteTable(connessione,"distinct", distinct)
distinct <- dbReadTable(connessione,"distinct")
View(distinct)
