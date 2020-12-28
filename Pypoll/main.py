# read csv file three columns voter Id, County and Candidate
#Calculate 1. The total number of votes cast
    #2.  a Complete list of Candidate who received votes - From Candidate column
    #3. The percentage of Votes each candidate won - need to count and divide
    #4 The Total number of votes each candidate won - need this for #3
    #5 The winner of the election based on popular vote. 
import os
import csv

csvpath=os.path.join('Resources', 'election_data.csv')
output_path = os.path.join("analysis", "poll_data.txt")


csvfile=open(csvpath)
csvreader=csv.reader(csvfile)
vote_count=0

#Net_total_dict={} #creating a dictionaly of p&l values
 # Read the header row first
csv_header = next(csvreader) #removed header from csvreader object but saved it in CSV_header if needed
print(f"CSV Header: {csv_header}")
#row_1 = next(csvreader) #removes first row of data and stores it in row_1
#print(row_1)

   
#net_total=0
#hold_row=int(row_1[1]) #row one value for calculation
#pl_list=[hold_row] #row one value for list
#change_pl=[]
#total_change=0

#Calculates the Total number of votes by counting each row after header was removed
for each_row in csvreader:
   vote_count=vote_count+1


#prints Results
print('Election Results')
print('-----------------------------')
print(f'Total Votes: {vote_count}')
print('-----------------------------')

with open(output_path, 'w', newline='') as csvfile:
    csvwriter= csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow([f'Total Votes: {vote_count}'])
    csvwriter.writerow(['-----------------------------'])

#when find row of calculation find index and add 1 because moved first row to get date index

# for each_row in csvreader:      #for loop takes a row value and subtracts the value above it to get the change in P & L and appendeds the change_pl value to a list
#           pl_list.append(int(each_row[1]))  #changes the P&L column to an integer value and adds it to pl_list 
#           change_pl_row=(int(each_row[1])-hold_row)  # subtract a p&l value from the row above its value to get the change_pl_row value
#           change_pl.append(change_pl_row)  #appends the change_pl_row value to list change_pl
#           hold_row=int(each_row[1])   #assign current row to hold_row so can use in next calc as row above it
#           total_months=total_months+1
#                     #print(each_row)
# #print(change_pl)

# for change_row in change_pl:  #adds each row in change_pl to get the total_change value
#     #print(each_row)
#     total_change=total_change+change_row
# average_change=total_change/len(change_pl)  #calculate the average of Change_pl by the number of values in the list 

# great_decrease=0  #not sure if this should be something else
# great_increase=0 

# for small_num in change_pl:
#         if great_decrease >= small_num:
#             great_decrease=small_num 
#             decrease_index=change_pl.index(small_num)

# for big_num in change_pl:
#         if great_increase < big_num:
#             great_increase=big_num 
#             increase_index=change_pl.index(big_num)


# #
# #print(f'inc index {csvreader[increase_index]}')
# dec_date=0

# print(f'deccrease index {decrease_index}')
# print(f'increase index {increase_index}')
# #dec_date==csvreader[0, decrease_index]
# #print(f' decrease date is {dec_date}')
# dec_date=csvreader.index(decrease_index)
# print(f'decrease date is {dec_date}')


# print("Financial Analysis")
# print('--------------------------------')
# print(f'Total Months: {total_months}')
# print(f'Total: ${net_total}')
# #print(total_change)
# print(f'Average Change: ${average_change:.2f}')
# print(f'Greatest Increase in Profits: (${great_increase})')
# print(f'Greatest Decrease in Profits: (${great_decrease})')


# #print(f'Processed {line_count} lines.')
# #print(f'Net Total is {net_total}')
    
# #move down a row and subtract the value above it to get the change in p&l
# #append the change in p&L to a new list called change_pl 


# # for each_pl in pl_list:
# #     #print(each_pl)
# #     change_pl= 2ndrow - 1strow

# # csv_header = next(csvreader)
# # print(f"CSV Header: {csv_header}")


# # add all of the change_pl values togeter to get Total_Change_pl
# # count the number of Change_pl values to get Change_pl_count
# #calculate Average_chang_pl = Total_Change_pl/Change_pl_count






  