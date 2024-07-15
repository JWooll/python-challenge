import os
import csv

Cpath = os.path.join('Resources','election_data.csv')

with open(Cpath) as Cfile:
    # Set reader and read header
    Creader = csv.reader(Cfile, delimiter=',')
    header = next(Creader)
    totVoter = 0 # Initiates total voter count
    candList = {} # Candidate list is a dictionary that will hold candidate names as keys
                  # and will hold the number of votes they receive as the values
    for row in Creader:
        totVoter += 1 # Counts the number of rows
        if row[2] in candList:
            candList[row[2]] += 1 # Adds vote to respective candidate if already in candidate list
        else:
            candList[row[2]] = 1 # Adds new candidate as key and sets value to one
    text = open("PyPoll.txt","w") # Write results into file as instructed
    text.write(f"""\
Election Results
-------------------------
Total Votes: {totVoter}
-------------------------
""")
    wincount = 0
    for cand in candList:
        # Percentage is candidate votes/total votes
        text.write(f"{cand}: {round(candList[cand]/totVoter * 100,3)}% ({candList[cand]})\n")
        #Checks if candidate had the most votes, assigns that candidate as winner
        if candList[cand] > wincount:
            wincount = candList[cand]
            winner = cand
    text.write(f"""
-------------------------
Winner: {winner}
-------------------------          
          """)
    text.close
    
    # Opens newly created text file and prints to terminal
    text = open("PyPoll.txt", "r")
    print(text.read())
    text.close
