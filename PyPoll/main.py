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
                total_votes += 1                                #adding 1 for each row that it goes through to the variable total_votes
                
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
        print(f'Total Votes: {total_votes}') #printing the variable total votes
        print("")
        print("============================")
        print("")
        print('Candidates:')
        for candidate, vote_count in candidate_votes.items():                        #for each candidate and vote count in the dictionary candidate votes
                vote_percentage = (vote_count/total_votes)*100                        #calculate vote percentage
                print(f'{candidate}: {vote_percentage:.3f}% ({vote_count} votes)')        #Print the candidate, the vote percentage to a 3rd decimal place, and their vote count
        print("")
        print("============================")
        print("")
        winner = max(candidate_votes, key=candidate_votes.get)                        #winner is the candidate with the maximum candidate votes
        print(f'Winner: {winner}')
       
        print("")
        print("============================")
        print("")

        output_path = 'election_results.txt'                                        #this assumes the path is the same as election_data_csv at the top
        with open(output_path, 'w') as output_file:                                #writing the next file
                output_file.write("Election Results\n")
                output_file.write("============================\n")                        # the \n starts a new line
                output_file.write(f'Total Votes: {total_votes}\n')
                output_file.write("============================\n")
                output_file.write('Candidates: \n')
                for candidate, vote_count in candidate_votes.items():
                        vote_percentage = (vote_count / total_votes) * 100
                        output_file.write (f'{candidate}: {vote_percentage: .3f}% ({vote_count} votes)\n')
                output_file.write("============================\n")
                output_file.write(f'Winner: {winner}\n')
                output_file.write("============================\n")
        print(f'Results exported to {output_path}')
        print("")
      
