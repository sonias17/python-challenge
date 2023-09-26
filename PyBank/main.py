import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#setting the variables for what I am looking for 
total_months = 0
net_amount = 0
previous_profit_loss = 0
changes = [] #List to store changes in profit/loss
dates = [] #list to store dates

#Reading the CSV
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
# make sure to read the header of the table first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
#print the following rows as data below a header 
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        total_months += 1
        net_amount += profit_loss

        #calculating the changes in profit/loss 
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date) 

        previous_profit_loss = profit_loss

#calculating average change   
average_change = sum(changes) / len(changes)

#calculating the greatest increase in profit
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
#calculating the greatest decrease in profit 
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

#printing the results 
print('Financial Analysis')
print('------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

#outputting as a text file
output_path = os.path.join('analysis','finanical_analysis.txt')

with open(output_path, 'w') as text_file:
    text_file.write('Financial Analysis\n')
    text_file.write('------------------\n')
    #f strings needed for the following
    text_file.write(f'Total Months: {total_months}\n')
    text_file.write(f'Total: ${net_amount}\n')
    text_file.write(f'Average Change: ${average_change}\n')
    text_file.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
    text_file.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')

