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
clothing1077 <- subset(data, Clothing.ID == 1077)
dbWriteTable(connessione, "clothing1077", clothing1077)
clothing1077 <- dbReadTable(connessione, "clothing1077")
View(clothing1077)
distinct_id <- unique(data, Clothing.ID)
d_len <- length(distinct_id)
View(distinct_id)
ratingID <- matrix(0,nrow=d_len,ncol=2)
for (d in distinct_id){
  tmp <- subset(data, Clothing.ID == d)
  media <- mean(tmp$Rating)
  print(paste("ID: ", tmp, " MEDIA: ", media))
}
View(ratingID)
