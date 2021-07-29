import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

request=requests.get('http://api.open-notify.org/astros.json')
print(request.status_code)
print(request.text)



loan_data = pd.read_csv("lending_club_loan_two.csv")  #importing libraries and CSV#
credit_grade = np.unique(loan_data['grade'])
sum_of_credit_grade = np.unique(loan_data['grade'])
grade_loan_array = []
sum_loan_array = []
multiply_array = []


def Print_Grade_Balances( Grade_balances ):#function created to print out grade balances.
    for element in Grade_balances:
        balance = loan_data.groupby('grade')['loan_amnt'].sum()[element] #grouping the data frame for grade and summing the balance as long as its equal to the current element,
        print("Loans in Credit Grade", element, "have a raw exposure of", balance)


for element in credit_grade:#loop to calculate the average Interest per Credit Grade
    interest_Calc = round(loan_data.groupby('grade')['int_rate'].mean()[element], 2)
    print("The Average Credit Grade", element, "interest rate is", interest_Calc)
    grade_loan_array.append(interest_Calc)

for element in credit_grade:
    balance = loan_data.groupby('grade')['loan_amnt'].sum()[element] #grouping the data frame for grade and summing the balance as long as its equal to the current element,
    sum_loan_array.append(balance)

sum_loan_array = np.divide(sum_loan_array, 10000)# Figure here divided by 10000 to quantify data in the millions (data set values were in the billions.
multiply_array = np.multiply(grade_loan_array, sum_loan_array) #multiply the loan grade interest rate by the sum of loans per grade
multiply_array = np.divide(multiply_array, 100)#divide by 100 to get the correct average interest paid.


print(multiply_array)
print(grade_loan_array)
print(sum_loan_array)


Print_Grade_Balances( credit_grade) #function call

barWidth = 0.25
fig = plt.subplots(figsize=(20, 20))

# Set position of bar on X axis
br1 = np.arange(len(multiply_array))
br2 = [x + barWidth for x in br1]

# Make the plot
plt.bar(br1, multiply_array, color='r', width=barWidth,
        edgecolor='grey', label='Interest Paid')
plt.bar(br2, sum_loan_array, color='g', width=barWidth,
        edgecolor='grey', label='Loan Amount')


plt.xlabel('Credit Grade', fontweight='bold', fontsize=15)
plt.ylabel('€ in Thousands', fontweight='bold', fontsize=15)
plt.legend()
plt.show()



