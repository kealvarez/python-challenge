# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
 

# Module for reading CSV files
import csv

csvpath = os.path.join('./Resources/budget_data.csv')

months = 0
profit = 0
max = 0
min = 0
change = 0
previous = 0
delta = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        months += 1
        profit += int(row[1])

        change = int(row[1]) - previous
        previous = int(row[1])

        if months > 1:
            delta = delta + change

        if change > max:
            max = change
            max_month = row[0]

        if change < min:
            min = change
            min_month = row[0] 

avg = round(delta/(months - 1),2)


print("Financial Analysis")
print("-------------------------")
print("Total Months:" + str(months))
print("Total: $" + str(profit))
print("Average Change: $" + str(avg))
print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max) + ")")
print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min) + ")")


with open("pybank_analysis.txt", "w") as results:
    results.write("Financial Analysis\n")
    results.write("-------------------------\n")
    results.write("Total Months: " + str(months) + "\n")
    results.write("Total: $" + str(profit) + "\n")
    results.write("Average Change: $" + str(avg) + "\n")
    results.write("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max) + ")\n")
    results.write("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min) + ")")