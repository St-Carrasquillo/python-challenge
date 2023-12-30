#import modules for operating system and CSV Files
import os
import csv

# Specify the file paths
file_path = os.path.join('Resources', 'election_data.csv')
output_file_path = os.path.join('analysis','analysis_results.txt')


# Initialize variables to store analysis results
total_votes = 0
candidate_votes = {}
candidates = []

# Open the CSV file to read 'r'
with open(file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Skip the header row
    header = next(csv_reader)

    # Iterate through the rows
    for row in csv_reader:
        # Extract values from the current row
        voter_id, county, candidate = row

        # Task 1: Calculate the total number of votes
        total_votes += 1

        # Task 2: Build a list of unique candidates
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0

        # Task 3: Count the votes for each candidate
        candidate_votes[candidate] += 1

# Task 4: Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Task 5: Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results to the terminal
print("Election Results")
print(f"Total Votes: {total_votes}")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.2f}% ({candidate_votes[candidate]})")
print(f"Winner: {winner}")



# Export the analysis results to a text file inside the 'Analysis' folder
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    for candidate in candidates:
        output_file.write(f"{candidate}: {percentages[candidate]:.2f}% {candidate_votes[candidate]}\n")
    output_file.write(f"Winner: {winner}\n")
    

print(f'Analysis results exported to {output_file_path}.')
