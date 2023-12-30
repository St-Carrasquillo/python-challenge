#import modules for operating system and CSV Files
import os
import csv

# Specify the file paths
file_path = os.path.join('Resources', 'budget_data.csv')
output_file_path = os.path.join('analysis','analysis_results.txt')

# Initialize variables to store analysis results
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []

# Open the CSV file to read 'r'
with open(file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Skip the header row
    header = next(csv_reader)

    # Iterate through the rows
    for row in csv_reader:
        # Extract values from the current row
        date = row[0]
        profit_loss = int(row[1])

        # Task 1: Calculate the total number of months
        total_months += 1

        # Task 2: Calculate the net total amount of "Profit/Losses"
        net_total += profit_loss

        # Task 3: Calculate the changes in "Profit/Losses"
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Task 4: Calculate the average of changes
average_change = sum(changes) / len(changes)

# Task 5: Find the greatest increase and decrease in profits
max_increase_index = changes.index(max(changes))
max_decrease_index = changes.index(min(changes))

greatest_increase_date = dates[max_increase_index]
greatest_increase_amount = changes[max_increase_index]

greatest_decrease_date = dates[max_decrease_index]
greatest_decrease_amount = changes[max_decrease_index]

# Print the analysis results
print('Financial Analysis')
print(f'Total Months: {total_months}')
print(f'Net Total: ${net_total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})')

# Export the analysis results, writing 'w' to a text file
with open(output_file_path, 'w') as output_file:
    output_file.write('Financial Analysis\n')
    output_file.write(f'Total Months: {total_months}\n')
    output_file.write(f'Net Total: ${net_total}\n')
    output_file.write(f'Average Change: ${average_change:.2f}\n')
    output_file.write(f'Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase_amount}\n')
    output_file.write(f'Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease_amount}\n')

print(f'Analysis results exported to {output_file_path}.')