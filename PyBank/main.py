import os
import csv

Cpath = os.path.join('Resources','budget_data.csv')

with open(Cpath) as Cfile:
    # Set reader and read header
    Creader = csv.reader(Cfile, delimiter=',')
    header = next(Creader)
    
    # Reading the first line independently for the average change in profits
    # Assuming the first line is the very first profit recorded
    init = next(Creader)
    totMonths = 1
    netProf = int(init[1])
    oldMonth = netProf
    totChange = 0
    # extrema and extMonth arrays will hold the greatest changes and their associated months respectively
    extrema= [0,0]
    extMonth = [init[0],init[0]]
    for row in Creader:
        totMonths += 1 # Counts the rows
        newMonth = int(row[1])      
        netProf += newMonth # Net Profit is the total sum of profits/losses
        MonthlyChange = newMonth - oldMonth
        if MonthlyChange < extrema[0]: # Checks for greatest loss
            extrema[0] = MonthlyChange
            extMonth[0] = row[0]
        if MonthlyChange > extrema[1]: # Checks for greatest profit
            extrema[1] = MonthlyChange
            extMonth[1] = row[0]
        totChange += MonthlyChange # Total change is the cummulative difference in changes
        oldMonth = newMonth  # Sets up for next loop

    # Note that one is subtracted from the total months as there is one less change from months than total months
    AvgChange = round(totChange/(totMonths-1),2) 
   
    # Create text file with format as instructed
    text = open("PyBank.txt","w")
    text.write(f"""\
          Financial Analysis
        ----------------------------
        Total Months: {totMonths}
        Total: ${netProf}
        Average Change: ${AvgChange}
        Greatest Increase in Profits: {extMonth[1]} (${extrema[1]})
        Greatest Decrease in Profits: {extMonth[0]} (${extrema[0]})
          """)
    text.close

    # Opens newly created text file and prints to terminal
    text = open("PyBank.txt", "r")
    print(text.read())
    text.close