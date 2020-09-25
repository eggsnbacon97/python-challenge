# Import modules--------------------------------------------------------------------------------

import os
import csv
import numpy as np

# Define path to file---------------------------------------------------------------------------

csvpath = os.path.join("..", "PyPoll", "Resources",
                       "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

# Define variables as floats--------------------------------------------------------------------

total_vote = float()
khan = float()
correy = float()
li = float()
otooley = float()

# Open file and skip header----------------------------------------------------------------------

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headerskip = next(csvfile)

# For each row, add 1 to "total_vote"--------------------------------------------------------------

    for row in csvreader:
        total_vote += 1

# If "name", add it to their specific vote count---------------------------------------------------

        if (row[2]) == "Khan":
            khan += 1
        if (row[2]) == "Correy":
            correy += 1
        if (row[2]) == "Li":
            li += 1
        if (row[2]) == "O'Tooley":
            otooley += 1

# Divide individual vote over total vote to get percentages------------------------------------------

    kahn_percent = np.divide(khan, total_vote)
    correy_percent = np.divide(correy, total_vote)
    li_percent = np.divide(li, total_vote)
    ot_percent = np.divide(otooley, total_vote)

# Winner is determined by taking max of all candidates------------------------------------------------

winner = max(khan, correy, li, otooley)

# If the winner is "name", their name becomes "can_name"-----------------------------------------------

if winner == khan:
    can_name = ("Khan")

if winner == correy:
    can_name = ("Correy")

if winner == li:
    can_name = ("Li")

if winner == otooley:
    can_name = ("O'Tooley")

# Print it all out-------------------------------------------------------------------------------------

print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_vote:.0f}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%} ({khan:.0f})")
print(f"Correy: {correy_percent:.3%} ({correy:.0f})")
print(f"Li: {li_percent:.3%} ({li:.0f})")
print(f"O'Tooley: {ot_percent:.3%} ({otooley:.0f})")
print(f"---------------------------")
print(f"Winner: {can_name}")
print(f"---------------------------")

# Define path to output file----------------------------------------------------------------------------

election_results = os.path.join(
    "..", "PyPoll", "Analysis", "Election_Results.txt")

# Print it all out---------------------------------------------------------------------------------------

with open(election_results, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_vote:.0f}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%} ({khan:.0f})\n")
    txtfile.write(f"Correy: {correy_percent:.3%} ({correy:.0f})\n")
    txtfile.write(f"Li: {li_percent:.3%} ({li:.0f})\n")
    txtfile.write(f"O'Tooley: {ot_percent:.3%} ({otooley:.0f})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {can_name}\n")
    txtfile.write(f"---------------------------")
