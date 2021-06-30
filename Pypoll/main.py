# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Pypoll', 'Resources', 'election_data.csv')
output_path= os.path.join('..', 'Pypoll', 'Analysis', 'election_result.txt')

#module to upload output as txt
import sys

#Open the csvfile
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the first header of the file
    csv_header=next(csvreader)
    #create a counter to count the total number of months (this is done by counting number of rows excl. the header in the file)
    total_votes=0
    #create a list of candidates
    candidate_list=[]
    #create a list to account vote counter for each candidate. 
    #In this case, vote list is like a ballot box, whilst vote counter is reserved for each candidate based on the order generated in candidate_list
    vote_list=[]
    vote_counter=[0,0,0,0]
    
    #create a loop in the csv file
    for row in csvreader:
        #count total votes cast
        total_votes+=1
        #update vote_list with names of each candidate (i.e ballot box)
        vote_list.append(row[2])
        #update candidate list with unique names of candidate
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    #create a loop to start counting the votes each candidate gets. 
    #In this case, for each candidate name that appears in vote_list (ballot box), increase the voting counter of each candidate by 1
    for i in vote_list:
        if i ==candidate_list[0]:
            vote_counter[0]+=1
        elif i ==candidate_list[1]:
            vote_counter[1]+=1
        elif i ==candidate_list[2]:
            vote_counter[2]+=1
        elif i ==candidate_list[3]:
            vote_counter[3]+=1

    #set up variables to determine the winner
    highest_vote = max(vote_counter)
    winner_index = vote_counter.index(int(highest_vote))
    winner=candidate_list[winner_index]

    #print the results in the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for j in range(len(candidate_list)):
        print(f"{str(candidate_list[j])}: {round(vote_counter[j]/total_votes*100,3)}% ({vote_counter[j]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    #print output into txt file
    sys.stdout=open(output_path,"w")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for j in range(len(candidate_list)):
        print(f"{str(candidate_list[j])}: {round(vote_counter[j]/total_votes*100,3)}% ({vote_counter[j]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")  
    sys.stdout.close()