#importing modules
import os
import csv

csvpath = os.path.join('/Users/soniasingh/Desktop/Bootcamp_work/python-challenge/PyPoll/Resources/election_data.csv')

#identifying the variables
total_votes = 0
candidates = {}
winner = ""


#reading the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
#recognize the header
    csv_header = next(csvreader)
#print the rows 
    for row in csvreader:
        candidate = row[2]
#counting  total votes
        total_votes += 1
#adding candidates to dict and counting votes
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] +=1
#finding the winner 
max_votes = max(candidates.values())
for candidate, votes in candidates.items():
    if votes == max_votes:
        winner = candidate 

#printing the results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f'{candidate}: {percentage: .3f}% ({votes})')

print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

#printing the results as a text file
output_path = os.path.join('analysis', 'election_results.txt')

with open(output_path, 'w') as text_file:
    text_file.write('Election Results\n')
    text_file.write('-------------------------\n')
    text_file.write(f'Total Votes: {total_votes}\n')
    text_file.write('-------------------------\n')

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        text_file.write(f'{candidate}: {percentage: .3f}% ({votes})')

    text_file.write('-------------------------\n')
    text_file.write(f'Winner: {winner}\n')
    text_file.write('-------------------------\n')
