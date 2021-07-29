import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

loan_data = pd.read_csv("lending_club_loan_two.csv")  #importing libraries and CSV#
#print(loan_data.iloc[:3])

initial_value = np.sum(loan_data['loan_amnt'])
balance = np.array(loan_data['loan_amnt'])

print (initial_value)

def Print_Grade_Balances( Grade_balances ):#function created to print out grade balances.
    for element in Grade_balances:
        balance = loan_data.groupby('grade')['loan_amnt'].sum()[element] #grouping the data frame for grade and summing the balance as long as its equal to the current element,
        print("Credit Grade ", element, "has an exposure of", balance)





credit_grade = np.unique(loan_data['grade'])
Print_Grade_Balances( credit_grade)

#def dosomething( thelist ):
 #   for element in thelist:
  #      print element



#sum_of_credit_grade = np.unique(loan_data['grade'])#Getting unique Credit Grade Values from CSV. Using this to loop through all loans with a specific credit grade
#credit_grade = np.unique(loan_data['grade']) #Getting unique Credit Grade Values - this variable will be used in the pie chart. Needed two of the same variables are the above variable gets overwritten.
#loan_ave = round(loan_data ['grade'].value_counts()/loan_data['grade'].count()*100, 2) # gives me the % of what grades the loans are in and sorts largest to smallest
