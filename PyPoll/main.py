import csv
import os

election_data_csv = os.path.join("/Users/matthewflanagan/Desktop/Data Analytics Work/Module 3/python-challenge/PyPoll/Resources/election_data.csv")

total_votes = 0
candidate_names = set()
candidate_votes = {}
candidates = dict()



with open(election_data_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)

        
        for row in csvreader:
                candidate_name = row[2]
                total_votes += 1
                
                if candidate_name in candidate_votes:
                        #if the candidate is already in the dictionary, it will add 1 to the vote count
                        candidate_votes[candidate_name] += 1
                else:
                        #if the candidate is not in the dictionary it will start them off with a vote count of 1
                        candidate_votes[candidate_name] = 1

        

        print("")
        print("Election Results")
        print("")
        print("============================")
        print("")
        print(f'Total Votes: {total_votes}')
        print("")
        print("============================")
        print("")
        print('Candidates:')
        for candidate, vote_count in candidate_votes.items():
                vote_percentage = (vote_count/total_votes)*100
                print(f'{candidate}: {vote_percentage:.3f}% ({vote_count} votes)')
        print("")
        print("============================")
        print("")
        winner = max(candidate_votes, key=candidate_votes.get)
        print(f'Winner: {winner}')
       
        print("")
        print("============================")
        print("")