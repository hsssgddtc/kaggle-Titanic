setwd("G:\\Project\\GitHub\\kaggle-Titanic")

readData <- function(path.name, file.name, column.types, missing.types){
  read.csv(paste(path.name, file.name, sep=""), 
           colClasses = column.types,na.strings=c("NA",""))  
}

titanic.path <- "./data/"
train.data.file <- "train.csv"
test.data.file <- "test.csv"
missing.types <- c("NA", "")
train.column.types <- c('integer',   # PassengerId
                        'factor',    # Survived 
                        'factor',    # Pclass
                        'character', # Name
                        'factor',    # Sex
                        'numeric',   # Age
                        'integer',   # SibSp
                        'integer',   # Parch
                        'character', # Ticket
                        'numeric',   # Fare
                        'character', # Cabin
                        'factor'     # Embarked
)
test.column.types <- train.column.types[-2]

typeof(train.raw["Ticket"])
train.raw <- readData(titanic.path, train.data.file, 
                      train.column.types, missing.types)
df.train <- train.raw
test.raw <- readData(titanic.path, test.data.file, 
                     test.column.types, missing.types)
df.infer <- test.raw

library(Amelia)
missmap(df.train,main="Titanic Training Data - Missings Map", col=c("red","black"), legend=FALSE)
head(df.train)
