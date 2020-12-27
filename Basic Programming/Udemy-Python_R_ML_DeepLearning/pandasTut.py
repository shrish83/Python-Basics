##for data manipulation and analysis
import pandas as pd
data = pd.read_csv("C:/Users/Swapnil Kumar Vaish/Documents/Python/Basic Programming/Udemy-Python_R_ML_DeepLearning/1. ST Academy - Crash course and Regression files/Data/Customer.csv")
#removing index/serial no. column
data = pd.read_csv("C:/Users/Swapnil Kumar Vaish/Documents/Python/Basic Programming/Udemy-Python_R_ML_DeepLearning/1. ST Academy - Crash course and Regression files/Data/Customer.csv",index_col=0)


#first 5 rows
print(data.head())
#print 100 rows
print(data.head(10))


#description
print(data.describe())

#indexing in data frame
print(data.iloc[0])    #gives 1st row of data frame
