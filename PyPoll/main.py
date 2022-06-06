import os
import csv
from tarfile import ReadError

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath,'r', encoding ='utf-8-sig') as pypoll:
    reader = csv.reader(pypoll)
    header = next(reader)

#define a list used for candidates 
    count = 0
    total = 0
    candidatelist=[]

#count the total number of records in the data file
#create a list of voted candidate 
    for row in reader:
        count += 1
        candidatelist.append(row[2])
 
#define a list used to capture candidates with unique value
    uniquecandidate=[]
    vote_percentage=[]
    vote_number=[]
    
#calculate the total number of votes by candidate, vote percentage,
# and the winner candidate with the largest number of votes    
    for i in set(candidatelist):
        uniquecandidate.append(i)
        x = candidatelist.count(i)
        vote_number.append(x)
        y = round((x/count)*100,2)
        vote_percentage.append(y)
        largest_vote = max(vote_number)
        winner_name = uniquecandidate[vote_number.index(largest_vote)]

#write the results to an output file
# Specify the file to write to
output_path = os.path.join("Analysis", "PyPoll.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    csvfile.write(f"Election Results \n")
    csvfile.write(f"---------------------------- \n")
    csvfile.write(f"Total Votes: {count} \n")
    csvfile.write(f"---------------------------- \n")
    for j in range(len(uniquecandidate)):
        csvfile.write(f"{uniquecandidate[j]} : {vote_percentage[j]} % ({vote_number[j]}) \n")
    csvfile.write(f"---------------------------- \n")
    csvfile.write(f"The winner is: {winner_name} \n")
    csvfile.write(f"---------------------------- \n")