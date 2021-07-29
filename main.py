import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

loan_data = pd.read_csv("lending_club_loan_two.csv")  #importing libraries and CSV


#This is all Pie chart Code following
sum_of_credit_grade = np.unique(loan_data['grade'])#Getting unique Credit Grade Values from CSV. Using this to loop through all loans with a specific credit grade
credit_grade = np.unique(loan_data['grade']) #Getting unique Credit Grade Values - this variable will be used in the pie chart. Needed two of the same variables are the above variable gets overwritten.
loan_ave = round(loan_data ['grade'].value_counts()/loan_data['grade'].count()*100, 2) # gives me the % of what grades the loans are in and sorts largest to smallest


with np.nditer(sum_of_credit_grade, op_flags=["readwrite"], flags=["refs_ok"]) as it: # Setup a loop to allow array values to be overwritten
   for x in it: # Loop cycle
            x[...] = loan_data.loc[loan_data['grade'] == x[...],'loan_amnt'].sum() # Takes the value  for each loan grade and gets the Sum value of each credit Grade


# For loop replaces all the below code.
#test = loan_data.loc[loan_data['grade'] == 'A','loan_amnt'].sum()
##test1 = loan_data.loc[loan_data['grade'] == 'B','loan_amnt'].sum()
#test2 = loan_data.loc[loan_data['grade'] == 'C','loan_amnt'].sum()
#test3 = loan_data.loc[loan_data['grade'] == 'D','loan_amnt'].sum()
#test4 = loan_data.loc[loan_data['grade'] == 'E','loan_amnt'].sum()
#test5 = loan_data.loc[loan_data['grade'] == 'F','loan_amnt'].sum()
#test6 = loan_data.loc[loan_data['grade'] == 'G','loan_amnt'].sum()
#print(test)
#print(test1)
#print(test2)
#print(test3)
#print(test4)
#print(test5)
#print(test6)


credit_check = np.sum(loan_data['loan_amnt'])
print(credit_check)
print (loan_ave)



fig, (ax,ax1) = plt.subplots(1,2,figsize=(15,15))
ax.pie(loan_ave, labels=credit_grade, autopct='%1.1f%%')
ax.set_title('% Exposure by Credit Rating', bbox={'facecolor':'0.8', 'pad':5})

ax1.pie(loan_ave, labels=sum_of_credit_grade, autopct='%1.1f%%')
ax1.set_title('Value per rating', bbox={'facecolor':'0.8', 'pad':5})
plt.show()



#This code is testing code.
#print(loan_data)
#print(loan_data.head())
#print(loan_data.shape)

#missing_values_count = loan_data.isnull().sum()
#print(missing_values_count)


#x = loan_data['term'].head(15)
#y1 = loan_data['loan_amnt'].head(15)
#y2 = loan_data[''].head(15)

#ax.plot(x,y1)
#ax.bar(x,y2)
#ax.scatter(x,y1)