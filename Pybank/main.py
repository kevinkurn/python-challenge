# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Pybank', 'Resources', 'budget_data.csv')
output_path= os.path.join('..', 'Pybank', 'Analysis', 'test.txt')

#module to upload output as txt
import sys

#import statistics module
import statistics

#Open the csvfile
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the first header of the file
    csv_header=next(csvreader)
    #create a counter to count the total number of months (this is done by counting number of rows excl. the header in the file)
    total_month=0   
    #create a counter to count total profit/loss with starting value of 0
    total_profit=0
    #create a blank list to input all the profit/loss month to month
    profit_list=[]
    #create a blank list to calculate changes of profit/loss on month to month
    var_list = []
    #create a blank list to store all the months in csv file
    month_list=[]
    #create a counter to allow substraction calculation between profits in the list
    profit_counter = 0

    # Read each row of data after the header
    for row in csvreader:
        #increase total month counter by one
        total_month+=1
        #define total profit of the month
        total_profit=total_profit+float(row[1])   
        #update profit list with profit figure month on month
        profit_list.append(row[1])
        #update month_list
        month_list.append(row[0])

    #create a loop that calculates the change profit/loss from current month to the next month
    for i in range(len(profit_list)-1):
        diff=(float(profit_list[profit_counter+1]))-float(profit_list[profit_counter])
        var_list.append(diff)
        profit_counter=profit_counter+1

    avg_change=float(statistics.mean(var_list))
    greatest_inc = max(var_list)
    greatest_dec = min(var_list)
    highest_month = var_list.index(greatest_inc)+1
    lowest_month = var_list.index(greatest_dec)+1

    #create a variable for analysis outcome
    analysis = ("Financial Analysis"
        "\n----------------------"
        f"\nTotal Months: {total_month}"
        f"\nTotal: {total_profit}"
        f"\nAverage Change: ${round(avg_change,2)}"
        f"\nGreatest Increase in Profits: {month_list[highest_month]} (${int(greatest_inc)})"
        f"\nGreatest Decrease in Profits: {month_list[lowest_month]} (${int(greatest_dec)})")

    #print output in terminal
    print(analysis)

    #print output into txt file
    with open(output_path,'w') as text_file:
        text_file.write(analysis)