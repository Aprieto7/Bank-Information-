# Start the project by importing os module and reading CSV files
import os 
import csv

# Define Variables
months = [] 
profit_loss_changes = []

months_count = 0 
net_profitloss = 0 
prev_month_profitloss = 0 
current_month_profitloss = 0 
profit_loss_change = 0

os.chdir(os.path.dirname(__file__))

budgetdata_csvpath = os.path.join("Resources", "budget_data.csv")

with open(budgetdata_csvpath, newline="") as csvfile:
    
    #Split data by commas
    Bank_data = csv.reader(csvfile, delimiter = ',')
    headers = next(csvfile)

    # Run loop through data
    for row in Bank_data: 
        months_count += 1 

        current_month_profitloss = int(row[1])
        net_profitloss += current_month_profitloss

        if (months_count == 1):
            prev_month_profitloss = current_month_profitloss
        else:
            profit_loss_change = current_month_profitloss - prev_month_profitloss
            months.append(row[0])
            profit_loss_changes.append(profit_loss_change)
            prev_month_profitloss = current_month_profitloss
    
    # Sum and average of Profit/Losses over the period
    sum_profitloss = sum(profit_loss_changes)
    average_profitloss = round(sum_profitloss/(months_count - 1),2)

    # Show the highest/lowest months 
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    highest_month = profit_loss_changes.index(highest_change)
    lowest_month = profit_loss_changes.index(lowest_change)

    best_month = months[highest_month]
    worse_month = months[lowest_month]

    # Show best month 

    # Print Output
    print("Financial Analysis")
    print("--------------------------------")
    print(f'Total Months: {months_count}')
    print(f'Total: ${net_profitloss}')
    print(f'Average Change: ${average_profitloss}')
    print(f'Greatest Increase in Profits: {best_month} (${highest_change})')
    print(f'Greatest Decrease in Losses: {worse_month} (${lowest_change})')

PyBank_Analysis = os.path.join("Analysis", "PyBank_Analysis.txt")
with open(PyBank_Analysis, "w") as txt:
    txt.write("Financial Analysis" + "\n")
    txt.write("-------------------------------" + "\n") 
    txt.write("Total Months  : " + str(months_count) + "\n")
    txt.write("Total         : " + "$" + str(net_profitloss) + "\n")
    txt.write("Average Change: " + "$" + str(int(average_profitloss)) + "\n")
    txt.write("Greatest Increase in Profits: " + str(best_month) + " ($" + str(highest_change) + ")\n")
    txt.write("Greatest Decrease in Losses : " + str(worse_month) + " ($" + str(lowest_change) + ")\n") 