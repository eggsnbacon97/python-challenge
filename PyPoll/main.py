import os
import csv
import numpy as np

csvpath = os.path.join("..", "PyPoll", "Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

total_vote=float()
khan=float()
correy=float()
li=float()
otooley=float()

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    headerskip=next(csvfile)

    for row in csvreader:
        total_vote +=1

        if (row[2]) == "Khan":
            khan +=1
        if (row[2]) == "Correy":
            correy +=1
        if (row[2]) == "Li":
            li +=1
        if (row[2]) == "O'Tooley":  
            otooley +=1

             
