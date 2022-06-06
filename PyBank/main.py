import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as pybank:
    reader = csv.reader(pybank)
    header = next(reader)

#calculate the total number of months from the dataset and create a list
#calculate the net total amount of "Profit/Losses" over the entire period and create a list
    count = 0
    pybank_PL = []
    Net_PL=0
    date=[]
    for row in reader:
        count = count + 1
        pybank_PL.append(int(row[1]))
        Net_PL += int(row[1])
        date.append(row[0])

#calculate the month-to-month change of profit/losses and create a list
    changePL=[]
    Average_PL=0.00
    for i in range(len(pybank_PL)-1):
        change = pybank_PL[i+1] - pybank_PL[i]
        changePL.append(change)
        Average_PL = round(sum(changePL)/len(changePL),2) 
        greatest_increase_profits = max(changePL)
        greatest_decrease_profits = min(changePL)
        increase_date = date[changePL.index(greatest_increase_profits)+1]
        decrease_date = date[changePL.index(greatest_decrease_profits)+1]

#print output at the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Month: {count}")
    print(f"Total Net Profit/Losses: ${Net_PL}")
    print(f"Average Profit/Losses: ${Average_PL}")
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_profits})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits})")


#write the results to an output file
# Specify the file to write to
output_path = os.path.join("Analysis", "Pybank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    csvfile.write(f"Financial Analysis \n")
    csvfile.write(f"---------------------------- \n")
    csvfile.write(f"Total Month: {count} \n")
    csvfile.write(f"Total Net Profit/Losses: ${Net_PL} \n")
    csvfile.write(f"Average Profit/Losses: ${Average_PL} \n")
    csvfile.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_profits}) \n")
    csvfile.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits}) \n")