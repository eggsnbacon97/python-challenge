# Import modules------------------------------------------------------------------------------

import os
import csv
import numpy as np

# Define path to file--------------------------------------------------------------------------

csvpath = os.path.join("..", "PyBank", "Resources",
                       "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

# Define floats/lists--------------------------------------------------------------------------

month_total = float()
pl_total = float()
greatest_increase = float()
greatest_decrease = float()
change_month = []

# Open file and skip header----------------------------------------------------------------------

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headerskip = next(csvreader)
    row = next(csvreader)
    previous_row = float(row[1])
    month_total += 1
    pl_total += float(row[1])

# For each row, add up months, and do some other nifty math---------------------------------------

    for row in csvreader:
        month_total += 1
        pl_total += float(row[1])
        month_diff = float(row[1]) - previous_row
        change_month.append(month_diff)
        previous_row = float(row[1])
        changeavg = np.sum(change_month)/len(change_month)

# If the float value is the greatest, grab the month name-----------------------------------------

        if float(row[1]) > greatest_increase:
            greatest_increase_month = row[0]

        if float(row[1]) < greatest_decrease:
            greatest_decrease_month = row[0]

# Calculate min/max for greatest increase/decrease--------------------------------------------------

    max = np.max(change_month)
    min = np.min(change_month)

# Print it all out----------------------------------------------------------------------------------

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {month_total:.0f}")
print(f"Total: ${pl_total:.2f}")
print(f"Average Change: ${changeavg:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${max:.0f})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${min:.0f})")

# Define path to output file--------------------------------------------------------------------------

analysis_file = os.path.join(
    "..", "PyBank", "Analysis", "Analysis_Outputs.txt")

# Print it all out-------------------------------------------------------------------------------------

with open(analysis_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months: {month_total:.0f}\n")
    txtfile.write(f"Total: ${pl_total:.2f}\n")
    txtfile.write(f"Average Change: ${changeavg:.2f}\n")
    txtfile.write(
        f"Greatest Increase in Profits: {greatest_increase_month} (${max:.0f})\n")
    txtfile.write(
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${min:.0f})")
