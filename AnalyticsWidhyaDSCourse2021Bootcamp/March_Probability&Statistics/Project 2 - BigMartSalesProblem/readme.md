Problem Statement:
The data scientists at BigMart have collected 2013 sales data for 1559 products across 10 stores in different cities. Also, certain attributes of each product and store have been defined. The aim is to build a predictive model and predict the sales of each product at a particular outlet.
Using this model, BigMart will try to understand the properties of products and outlets which play a key role in increasing sales.
Please note that the data may have missing values as some stores might not report all the data due to technical glitches. Hence, it will be required to treat them accordingly. 


STEP 1
Inferences from Problem Statement
   Our problem is a regression problem to predict the continuous values of the sales variable.

STEP 2
Hypothesis Generation
   About brianstorming about the problem regarding all the possible fators that impact the outcome
    It is done before looking at the data
    1) storelocation, storeType, storeSize will affect sales
    2) ItemVisibility, itemType, itemMRP will affet sales

STEP 3
Loading data and analyzing variables, datatypes
1) object: categorical
  2) int64: integer variables
  3) float64: decimal vlaues, integers

STEP 4
Visualize each variable separately
  1) categorical 
     here:= ItemType, outletIdentifier, outletType
  2) ordinal
     here:= outletSize, outletLocationType, 
  3) numerical
     here:= itemWeight, ItemVisibility, itemMRP, year, Sales
   In Bivariate Analysis, our hypothesis will help us in visualizing those features against each other.
Do missing value and outlier treatment

STEP 5
Model Performance Evaluation. Ways to evaluate performance:=
    1) Accuracy:= usinf confusion matrix
         -> Precision, Recall, Specificity, ROC Curve, AUC(Higher the AUC better the prediction)

STEP 6
Model Building
here, Logistic Regression(to predict binary outcome)


