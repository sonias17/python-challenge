# python-challenge
This project includes two Python scripts: one for analyzing financial records (PyBank) and another for counting election votes (PyPoll).

## PyBank

### Objective

In the PyBank script, the goal is to analyze the financial records of a company provided in a dataset called `budget_data.csv`. The script calculates the following values:

- Total number of months included in the dataset
- Net total amount of "Profit/Losses" over the entire period
- Changes in "Profit/Losses" over the entire period, and the average of those changes
- Greatest increase in profits (date and amount) over the entire period
- Greatest decrease in profits (date and amount) over the entire period

### Usage

To run the PyBank script, execute the following command: python main.py (within the PyBank path)

The script will print the analysis to the terminal and as a text file in the analysis folder within the PyBank folder. 

The expected output should match the following: 

Financial Analysis
Total Months: 86
Total: $22,564,198
Average Change: $-8,311.11
Greatest Increase in Profits: Aug-16 ($1,862,002)
Greatest Decrease in Profits: Feb-14 ($-1,825,558)


## PyPoll 

### Objective
In the PyPoll script, the goal is to use data from election_data.csv to analyze and count votes. The script calculates the following values:

Total number of votes cast
A list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote

### Usage
To run the PyPoll script, use the following command: python main.py (within the PyPoll path)

The script will print the election results within the terminal and as a text_file in the analysis folder within the PyPoll 

The expected output should look like the following: 

Election Results

Total Votes: 369,711

Charles Casper Stockham: 23.049% (85,213)
Diana DeGette: 73.812% (272,892)
Raymon Anthony Doane: 3.139% (11,606)

Winner: Diana DeGette

