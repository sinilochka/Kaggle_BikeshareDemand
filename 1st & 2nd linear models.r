rm(list = ls())
# load the data
train = read.table("train.txt", header=TRUE)
names(train) <- c("datetime", "hour", "season", "holiday", "workingday","weather","temp","atemp","humidity","windspeed","casual","registered","count")
# look at the data
par(mfrow=c(3,3), mar=c(2.6,2.6,2.6,2.6))
plot(train$hour, train$count, xlab = "Hours", ylab = "Number of Bikes", main = "Hours against Bikes", pch=18)
plot(train$season, train$count, xlab = "Season", ylab = "Number of Bikes", main = "Season against Bikes", pch=18)
plot(train$holiday, train$count, xlab = "Holiday", ylab = "Number of Bikes", main = "Holiday against Bikes", pch=18)
plot(train$workingday, train$count, xlab = "Working Day", ylab = "Number of Bikes", main = "Working Day against Bikes", pch=18)
plot(train$temp, train$count, xlab = "Temperature", ylab = "Number of Bikes", main = "Temperature against Bikes", pch=18)
plot(train$atemp, train$count, xlab = "Atemp", ylab = "Number of Bikes", main = "Atemp against Bikes", pch=18)
plot(train$weather, train$count, xlab = "Weather", ylab = "Number of Bikes", main = "Weather against Bikes", pch=18)
plot(train$humidity, train$count, xlab = "Humidity", ylab = "Number of Bikes", main = "Humidity against Bikes", pch=18)
plot(train$windspeed, train$count, xlab = "Windspeed", ylab = "Number of Bikes", main = "Windspeed against Bikes", pch=18)
# 1st model
fit <- lm(count ~ temp + atemp + humidity + windspeed, data = train)
summary(fit)
anova(fit)
t=rstudent(fit)
qqnorm(rstudent(fit), pch=19)
abline(0,1)
plot(fitted.values(fit), rstudent(fit), xlab = "predicted values", ylab = "residuals", main = " Externally Studentized Residuals",pch=19)
abline(0,0)
library(MASS)
# transformation options
boxcox(fit)
BC <- boxcox(fit)
BC
BC$x[BC$y==max(BC$y)]
# confidence interval
S <- max(BC$y) - 0.5*qchisq(0.95,1)
S
BC$x[BC$y>S]
# square root model
fit2 <- lm(I(sqrt(count))~ temp + atemp + humidity + windspeed, data = train)
summary(fit2)
anova(fit2)
t=rstudent(fit2)
qqnorm(rstudent(fit2), pch=19)
abline(0,1)
plot(fitted.values(fit2), rstudent(fit2), xlab = "predicted values", ylab = "residuals", main = " Externally Studentized Residuals",pch=18)
abline(0,0)
# exhaustive search
library(leaps)
# all subsets from cont-s variables
all <- regsubsets(count ~ temp + atemp + humidity + windspeed, nbest = 6, train)
summary(all)
Cp <- summary(all)$cp
AdjR2 <- summary(all)$adjr2
SSRes <- summary(all)$rss
R2 <- summary(all)$rsq
Matrix <- summary(all)$which
p <- apply(Matrix,1, sum)
MSE <- SSRes/(8600-p)
output <- cbind(p, Matrix, SSRes, R2, AdjR2, MSE, Cp)
colnames(output)[3:6] <- c("temp", "atemp", "humidity", "windspeed") 
output
# square root model (atemp + humidity + windspeed)
fit3 <- lm(I(sqrt(count)) ~ atemp + humidity + windspeed, data = train)
summary(fit3)
anova(fit3)
t=rstudent(fit3)
qqnorm(rstudent(fit3), pch=19)
abline(0,1)
plot(fitted.values(fit3), rstudent(fit3), xlab = "predicted values", ylab = "residuals", main = " Externally Studentized Residuals",pch=18)
abline(0,0)
