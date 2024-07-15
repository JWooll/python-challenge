import os
import csv

Cpath = os.path.join('Resources','election_data.csv')

with open(Cpath) as Cfile:
    # Set reader and read header
    Creader = csv.reader(Cfile, delimiter=',')
    header = next(Creader)
    totVoter = 0
    candList = {}

    for row in Creader:
        totVoter += 1
        if row[2] in candList:
            candList[row[2]] += 1
        else:
            candList[row[2]] = 1
    text = open("PyPoll.txt","w")
    text.write(f"""\
Election Results
-------------------------
Total Votes: {totVoter}
-------------------------
""")
    wincount = 0
    for cand in candList:
        text.write(f"{cand}: {round(candList[cand]/totVoter * 100,3)}% ({candList[cand]})\n")
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