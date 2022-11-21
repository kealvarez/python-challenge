# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
 
# Module for reading CSV files
import csv

csvpath = os.path.join('./Resources/election_data.csv')

total_votes = 0
vote_candidates = {}
list_candidates = []
winning_count = 0
winning_candidates = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader: 

        total_votes = total_votes + 1
        name_candidates = row[2]

        if name_candidates not in list_candidates:

            list_candidates.append(name_candidates)
            vote_candidates[name_candidates] = 0

        vote_candidates[name_candidates] = vote_candidates[name_candidates] + 1

with open("pypoll_analysis.txt", "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-----------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------------------------\n")
    print(election_results, end="")

    for candidate in vote_candidates:
        votes = vote_candidates.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
    
            
winning_candidate_summary = (
       f"-----------------------------------------\n"
       f"Winner: {winning_candidate}\n"
       f"-----------------------------------------\n")

print(winning_candidate_summary, end="")