import csv
import os

election_data_csv = os.path.join("/Users/matthewflanagan/Desktop/Data Analytics Work/Module 3/python-challenge/PyPoll/Resources/election_data.csv")

total_votes = []
winner = []
candidates = {}
candidates = dict()




with open(election_data_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)

        print(csvreader)
        print(f"CSV Header: {header}")
        for row in csvreader:
                candidates = {"name": "Diana DeGette","Charles Casper Stockham","Raymon Anthony Doane"}
                print(f'{candidates["name"]}')
                