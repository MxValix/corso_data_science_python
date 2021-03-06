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
dbWriteTable(connessione, "mtcars", mtcars)
data <- dbReadTable(connessione, "mtcars")
View(data)
dbListTables(connessione)
