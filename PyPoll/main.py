import os
import csv
import numpy as np

csvpath = os.path.join("..", "PyPoll", "Resources",
                       "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

total_vote = float()
khan = float()
correy = float()
li = float()
otooley = float()

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headerskip = next(csvfile)

    for row in csvreader:
        total_vote += 1

        if (row[2]) == "Khan":
            khan += 1
        if (row[2]) == "Correy":
            correy += 1
        if (row[2]) == "Li":
            li += 1
        if (row[2]) == "O'Tooley":
            otooley += 1

    kahn_percent = np.divide(khan, total_vote)
    correy_percent = np.divide(correy, total_vote)
    li_percent = np.divide(li, total_vote)
    ot_percent = np.divide(otooley, total_vote)

winner = max(khan, correy, li, otooley)

if winner == khan:
    can_name=("Khan")

if winner == correy:
    can_name = ("Correy")

if winner == li:
    can_name = ("Li")

if winner == otooley:
    can_name = ("O'Tooley")

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

