train <- read.csv("./data/train.csv", stringsAsFactors=FALSE)
test <- read.csv("./data/test.csv", stringsAsFactors=FALSE)

##[Part 1: Booting Up R](http://trevorstephens.com/post/72918760617/titanic-getting-started-with-r-part-1-booting)
str(train)
prop.table(table(train$Survived))
test$Survived <- rep(0, 418)
submit <- data.frame(PassengerId = test$PassengerId, Survived = test$Survived)
write.csv(submit, file = "./data/theyallperish.csv", row.names = FALSE)

## [Part 2: The Gender-Class Model](http://trevorstephens.com/post/72920580937/titanic-getting-started-with-r-part-2-the)
# Dealing with sex
summary(train$Sex)
prop.table(table(train$Sex, train$Survived))
prop.table(table(train$Sex, train$Survived),1)
prop.table(table(train$Sex, train$Survived),2)
test$Survived <- 0
test$Survived[test$Sex == 'female'] <- 1
View(test)

# Dealing with Age
summary(train$Age)
train$Child <- 0
train$Child[train$Age < 18] <- 1

aggregate(Survived ~ Child + Sex, data=train, FUN=sum)
aggregate(Survived ~ Child + Sex, data=train, FUN=length)
aggregate(Survived ~ Child + Sex, data=train, FUN=function(x) {sum(x)/length(x)})

# Holy! This is what i want!
# Get rid of if-elses!
train$Fare2 <- '30+'
train$Fare2[train$Fare < 30 & train$Fare >= 20] <- '20-30'
train$Fare2[train$Fare < 20 & train$Fare >= 10] <- '10-20'
train$Fare2[train$Fare < 10] <- '<10'
aggregate(Survived ~ Fare2 + Pclass + Sex, data=train, FUN=function(x) {sum(x)/length(x)})

test$Survived <- 0
test$Survived[test$Sex == 'female'] <- 1
test$Survived[test$Sex == 'female' & test$Pclass == 3 & test$Fare >= 20] <- 0

## [Part 3: Decision Trees](http://trevorstephens.com/post/72923766261/titanic-getting-started-with-r-part-3-decision)
########################################################################################################################
## Decision trees have a number of advantages. They are what’s known as a glass-box model, after the model has found the 
## patterns in the data you can see exactly what decisions will be made for unseen data that you want to predict. 
## They are also intuitive and can be read by people with little experience in machine learning after a brief explanation. 
## Finally, they are the basis for some of the most powerful and popular machine learning algorithms.
########################################################################################################################

library(rpart)
fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, data=train, method="class")
plot(fit)
text(fit)
## install RGtk2 failed thousand times. 
# install.packages("RGtk2", depen=T, type="source")
# install.packages('RGtk2')
# install.packages('rattle')
# install.packages('rpart.plot')
# install.packages('RColorBrewer')
library(rattle)
library(rpart.plot)
library(RColorBrewer)
# doesn't work without RGtk2 installed properly.
fancyRpartPlot(fit)

# Here we have called rpart’s predict function. Here we point the function to the model’s fit object, which contains 
# all of the decisions we see above, and tell it to work its magic on the test dataframe. No need to tell it which 
# variables we originally used in the model-building phase, it automatically looks for them and will certainly let you 
# know if something is wrong. Finally we tell it to again use the class method (for ones and zeros output) and 
# as before write the output to a dataframe and submission file.
Prediction <- predict(fit, test, type = "class")
submit <- data.frame(PassengerId = test$PassengerId, Survived = Prediction)
write.csv(submit, file = "./data/myfirstdtree.csv", row.names = FALSE)

## TRY TO INSTALL RGtk2
# install gWidgets FAILED!!!!
# install.packages("gWidgets", depen=T)
# install.packages("gWidgetsRGtk2", depen=T, type="source")
