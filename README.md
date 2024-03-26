## PyBank Instructions
  
In this Challenge, I was tasked with creating a Python script to analyze the financial records of a company. I was given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

The task is to create a Python script that analyzes the records to calculate each of the following values:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period


## Process
I began with setting the initial values.


<img width="659" alt="Screenshot 2024-03-26 at 1 30 56 PM" src="https://github.com/mattflanagan2/python-challenge/assets/146908072/cb4a48cc-63af-47da-aad3-a8b573b13630">

Next I opened and read the CSV file, then created a for loop to go through each row of the CSV file to find the tate and to find the profit or loss of each row. I then created an a simple if statement where if the value of the current row is either greater than the current greatest increase, make the current row the new greatest increase, and to do the same for the greatest decrease. Finally I used the collected data to calculate the average change.

<img width="810" alt="Screenshot 2024-03-26 at 1 31 56 PM" src="https://github.com/mattflanagan2/python-challenge/assets/146908072/e5cf7d05-27bc-495f-b741-063030dff028">

I then printed the results to the terminal, I also printed the results and saved them to a .txt file as well so that the shareholders only need to open the .txt file to see the results instead of running the code. 

<img width="1028" alt="Screenshot 2024-03-26 at 1 39 24 PM" src="https://github.com/mattflanagan2/python-challenge/assets/146908072/cdb8ad5d-45a8-4081-a25e-7f7b6cf7b588">



The results printed as followed:

<img width="643" alt="Screenshot 2024-03-26 at 1 41 27 PM" src="https://github.com/mattflanagan2/python-challenge/assets/146908072/ec53cd82-24a3-4915-ad8c-64a282399f76">




## My PyPoll Instructions

In this challenge, I was tasked with helping a small, rural town modernize its vote-counting process.

I was given a set of poll data named election_data.csv. This dataset comprised three columns: "Voter ID", "County", and "Candidate". My task was to create a Python script that analyzed the votes and calculated the following values:

 * The total number of votes cast.
 * A complete list of candidates who received votes.
 * The percentage of votes each candidate won.
 * The total number of votes each candidate won.
 * The winner of the election based on popular vote.


## Process

I began with setting the setting the CSV path and initial values.

<img width="1234" alt="Screenshot 2024-03-26 at 1 45 13 PM" src="https://github.com/mattflanagan2/python-challenge/assets/146908072/9bfd353d-ac9d-480e-93cd-6e6aecf82945">

Next I opened the CSV file. I then created a for loop to go through each row and record the candidate name and at one vote to their total vote tally. I created an if statement as well so that if the candidate name is not already in the candidate vote column, it will add their name and add their first vote, however if their name is already in the names column, it will simply add one to their vote total. 

<img width="1234" alt="Screenshot 2024-03-26 at 1 48 16 PM" src="https://github.com/mattflanagan2/python-challenge/assets/146908072/87d513bc-2ab5-4ef6-956e-865e9db938da">

After that I printed the results to the terminal. I also wrote the results to a .txt file so that the results of the data could be easily shared. 

<img width="1234" alt="Screenshot 2024-03-26 at 1 49 54 PM" src="https://github.com/mattflanagan2/python-challenge/assets/146908072/b6e64157-b130-45df-b1db-da75b757ff4c">
<img width="1234" alt="Screenshot 2024-03-26 at 1 50 03 PM" src="https://github.com/mattflanagan2/python-challenge/assets/146908072/9599cc1a-8c7e-4acd-9254-c6d0ddc598b4">



