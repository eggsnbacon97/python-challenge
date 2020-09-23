import os
import csv
import numpy as np

csvpath = os.path.join("..", "PyBank", "Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

month_total = float(0)
pl_total = float(0)
greatest_increase = float(0)
greatest_decrease = float(0)
change_month = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headerskip = next(csvreader)
    row = next(csvreader)
    previous_row = float(row[1])
    month_total += 1
    pl_total += float(row[1])
    
    for row in csvreader:      
        month_total += 1
        pl_total += float(row[1])
        month_diff = float(row[1]) - previous_row
        change_month.append(month_diff)
        previous_row = float(row[1])
        changeavg = np.sum(change_month)/len(change_month)   

        if float(row[1]) > greatest_increase:
            greatest_increase = float(row[1])
            greatest_increase_month = row[0]
            
        if float(row[1]) < greatest_decrease:
            greatest_decrease = float(row[1])
            greatest_decrease_month = row[0]  
        
    
    max = np.max(change_month)
    min = np.min(change_month)

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {month_total:.0f}")
print(f"Total: ${pl_total:.2f}")
print(f"Average Change: ${changeavg:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${max:.0f})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${min:.0f})")