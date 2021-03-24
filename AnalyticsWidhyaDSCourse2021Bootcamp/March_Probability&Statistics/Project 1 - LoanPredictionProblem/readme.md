This file contains information and explanation regarding the problem statement. I've studied the online course specifically for this course on analytics vidhya as it is my first problem solving towards data science.

Problem Statement:
Dream Housing Finance company deals in all kinds of home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and after that company validates the customer eligibility for loan. Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others. To automate this process, they have provided a dataset to identify the customers segments that are eligible for loan amount so that they can specifically target these customers. 

STEP 1
Inferences from the Problem Statement:
        Our problem is a classification problem wether a loan would be approved or not. Two types of classification:-
             1) Binary Classification: yes/no, 0/1, etc.
             2) Multiclass :  genre of movies:= classic,fantasy, romance, horror, etc



STEP 2
Hypothesis Generstion
    About brianstorming about the problem regarding all the possible fators that impact the outcome
    It is done before looking at the data

    Let's think about the factors that might affect our loan approval:
        salary, loan amount, loan term, emi, loan history


STEP 3
Loading data and analyzing variables, datatypes
  1) object: categorical
       here:= Loan_Id, gender, married, dependents, education self employes, property area, loan_Status
  2) int64: integer variables
       here:= income
  3) float64: decimal vlaues, integers
       here:= loanAMt, loanTerm, credit history


STEP 4
Visualize each variable separately
  1) categorical  2) ordinal   3) numerical
   In Bivariate Analysis, our hypothesis will help us in visualizing those features against each other.
Do missing value and outlier treatment

STEP 5
Model Performance Evaluation. Ways to evaluate performance:=
    1) Accuracy:= usinf confusion matrix
         -> Precision, Recall, Specificity, ROC Curve, AUC(Higher the AUC better the prediction)

STEP 6
Model Building
here, Logistic Regression(to predict binary outcome)
