import csv
import os


budget_data_csv = os.path.join("/Users/matthewflanagan/Desktop/Data Analytics Work/Module 3/python-challenge/PyBank/Resources/budget_data.csv")


total_months = 0
total = 0
previous_profit_or_losses = 0
total_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        date = row[0]
        profit_or_losses = int(row[1])
        total_months += 1
        total += profit_or_losses
        
        if total_months > 1:
            change = profit_or_losses - previous_profit_or_losses
            total_change += change
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = date
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = date

        
        previous_profit_or_losses = profit_or_losses
        
    average_change = total_change / (total_months-1)
        
        
        
    print("")
    print("Financial Analysis")
    print("------------------------------")
    print("")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average_change:.2f}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
    print("")

    output_path = 'financial_analysis.txt'
    with open(output_path, 'w') as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write("------------------------------\n")
        output_file.write(f'Total Months: {total_months}\n')
        output_file.write(f'Total: ${total}\n')
        output_file.write(f'Average Change: ${average_change:.2f}\n')
        output_file.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
        output_file.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')
        
