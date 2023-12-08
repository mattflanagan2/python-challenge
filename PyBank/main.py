import csv
import os


budget_data_csv = os.path.join("/Users/matthewflanagan/Desktop/Data Analytics Work/Module 3/python-challenge/PyBank/Resources/budget_data.csv")


total_months = 0
total = 0
previous_profit_or_losses = 0
total_change = 0
greatest_increase = 0
greatest_increase_month = ""            #defined as an empty string
greatest_decrease = 0
greatest_decrease_month = ""

with open(budget_data_csv, 'r') as csvfile:            #opening the csv file 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:                #for each row in the csv reader
        date = row[0]                    #assign the date variable to the first row
        profit_or_losses = int(row[1])    #assign profit or loss variable as an integer (if you don't do this it won't recognize the negative values) and to the second row
        total_months += 1                #count the total months (aka each row)
        total += profit_or_losses        #add to the total for each profit or loss row 
        
        if total_months > 1:            #for each month after the first month
            change = profit_or_losses - previous_profit_or_losses    #calculate the change
            total_change += change                                    #add the change to the total change 
            if change > greatest_increase:                            #if the change is greater than 0 or the previous number thereafter that becomes the new greatest change
                greatest_increase = change
                greatest_increase_month = date                        #get the date for that greatest increase
            if change < greatest_decrease:                            #same principal for the greatest decrease
                greatest_decrease = change
                greatest_decrease_month = date

        
        previous_profit_or_losses = profit_or_losses                #store previous row profit/loss value
        
    average_change = total_change / (total_months-1)                #calculate average change
        
        
        
    print("")                                                    #printing the results 
    print("Financial Analysis")
    print("------------------------------")
    print("")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average_change:.2f}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
    print("")

    output_path = 'financial_analysis.txt'                    #output path assumes the budget_data_csv path from top
    with open(output_path, 'w') as output_file:                #writing the text file to that path
        output_file.write("Financial Analysis\n")
        output_file.write("------------------------------\n")
        output_file.write(f'Total Months: {total_months}\n')
        output_file.write(f'Total: ${total}\n')
        output_file.write(f'Average Change: ${average_change:.2f}\n')
        output_file.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
        output_file.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')
        
