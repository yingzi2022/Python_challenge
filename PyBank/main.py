import os

import csv

#csvpath = '..\Resources\budget_data.csv'
csvpath = os.path.join("Resources","budget_data.csv")

count = 0
with open(csvpath,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
 #   print(f"CSV Header: {csv_header}")

#The total number of months included in the dataset
    for row in csvreader:
        print(row)
        count = count + 1

print(f"The total number of months included in the dataset is : {count}")

#The total number of months included in the dataset


#The net total amount of "Profit/Losses" over the entire period


#The changes in "Profit/Losses" over the entire period, and then the average of those changes


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in profits (date and amount) over the entire period