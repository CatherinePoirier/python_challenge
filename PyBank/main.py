# read csv file two columns date and Profit/Losses
#Calculate 1. The total number of months included in the dataset
    #2. The net total amount of "Profit/Losses" over the entire period
#WORKING
import os
import csv

csvpath=os.path.join('Resources', 'Homework_03-Python_PyBank_Resources_budget_data.csv')

csvfile=open(csvpath)
csvreader=csv.reader(csvfile)
line_count=0

#csv_header=next(csvreader)
#print(csv_header)

#Net_total_dict={} #creating a dictionaly of p&l values
 # Read the header row first (skip this step if there is now header)
csv_header = next(csvreader) #removed header from csvreader object
print(f"CSV Header: {csv_header}")
row_1 = next(csvreader) #removes first row of data and stores it in row_1
print(row_1)

    # Read each row of data after the header
net_total=0
hold_row=int(row_1[1]) #row one value for calculation
pl_list=[hold_row] #row one value for list
change_pl=[]
total_change=0


for each_row in csvreader:
          pl_list.append(int(each_row[1]))
          change_pl_row=(int(each_row[1])-hold_row)
          change_pl.append(change_pl_row)

          #assign current row so can use in next calc as row above it
          hold_row=int(each_row[1])
                    #print(each_row)
#print(change_pl)

for change_row in change_pl:
    #print(each_row)
    total_change=total_change+change_row

average_change=total_change/len(change_pl)

print(total_change)
print(f'average change is {average_change}')

for each_row in pl_list:
    #print(each_row)
    net_total=net_total+each_row

print(f'Net Total is {net_total}')


#print(f'Processed {line_count} lines.')
#print(f'Net Total is {net_total}')
    
#move down a row and subtract the value above it to get the change in p&l
#append the change in p&L to a new list called change_pl 


# for each_pl in pl_list:
#     #print(each_pl)
#     change_pl= 2ndrow - 1strow

# csv_header = next(csvreader)
# print(f"CSV Header: {csv_header}")


# add all of the change_pl values togeter to get Total_Change_pl
# count the number of Change_pl values to get Change_pl_count
#calculate Average_chang_pl = Total_Change_pl/Change_pl_count






  