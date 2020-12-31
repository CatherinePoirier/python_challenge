# read csv file three columns voter Id, County and Candidate
#Calculate 1. The total number of votes cast - count rows in file minus the header
    #2.  a Complete list of Candidate who received votes - From Candidate column - Create a list with Candidate info. Then create a dictionary with the candidates
    
    #4 The Total number of votes each candidate won - need this for #3 - created a counter for each candiate from Dictionary and loop through candiate list and count each time their name shows up
    #Does this happen within the Dictionary?

    #3. The percentage of Votes each candidate won - need to count and divide - divide each candidates total by the total number of votes cast from #1.
          
    #5 The winner of the election based on popular vote. 
import os
import csv

csvpath=os.path.join('Resources', 'election_data.csv')
output_path = os.path.join("analysis", "poll_data.txt")

csvfile=open(csvpath)
csvreader=csv.reader(csvfile)

 # Read the header row first
csv_header = next(csvreader) #removed header from csvreader object but saved it in CSV_header if needed
#print(f"CSV Header: {csv_header}")
#row_1 = next(csvreader) #removes first row of data and stores it in row_1
#print(row_1)
candidate_list=[]  #A list of votes cast for the candidates
candidate_info={}   #A dictionary to determine unique value - Determine who the candiates are
vote_count=0
name=[]
unique_candidate=[]
highest_count=0

for each_name in csvreader:      #reades each_row from cvsreader column c into candiate_info
    candidate_list.append(each_name[2])

for each_row in candidate_list:  #calculates the votecount
     vote_count=vote_count+1
#print(f'Vote Count: {vote_count}')

for x in candidate_list:            #gets a unique list of candidates 
    if x not in unique_candidate:
            unique_candidate.append(x)

for name in unique_candidate:       #assigns key(candidate name) to dictionary and assigns 0 to value
       candidate_info[name]=0       #0 value will be changed to votes cast below

for y in candidate_list:
    for z in unique_candidate:
        if z == y:
            candidate_info[z]=candidate_info[z]+1


#prints Results
print(' ')
print('Election Results')
print('-----------------------------')
print(f'Total Votes: {vote_count}')
for a in candidate_info:
    print(f'{a}: {((candidate_info[a]/vote_count)*100):.3f}%  ({candidate_info[a]})')
for b in candidate_info:
    if candidate_info[b] > highest_count:
        highest_count=candidate_info[b]
        winner=b
print('-----------------------------')
print(f'Winner: {winner}')
print('-----------------------------')

with open(output_path, 'w', newline='') as csvfile:
    #csvwriter= csv.writer(csvfile, delimiter=',')
    csvwriter= csv.writer(csvfile)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow([f'Total Votes: {vote_count}'])

    for a in candidate_info:
        csvwriter.writerow([f'{a}: {((candidate_info[a]/vote_count)*100):.3f}%  ({candidate_info[a]})'])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow(['-----------------------------'])



