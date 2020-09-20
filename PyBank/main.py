import os
import csv

#from os.path import expanduser
#home = expanduser("~")
#budgetdata = os.path.join(home,'C:/Users/Dan/BDAB/python-challenge/PyBank/Resources/' )

path= 'C:/Users/Dan/BDAB/python-challenge/PyBank/Resources/'
budgetdata=os.path.join(path, '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

monthtotal=0
pltotal=0


with open(budgetdata, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    row=next(csvreader)
    monthtotal += 1

    for row in csvreader:
        monthtotal += 1 
        pltotal += int(row[1])

print(f"Total Months: {monthtotal}")
print(f"Total: ${pltotal}")