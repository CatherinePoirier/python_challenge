# read csv file two columns date and Profit/Losses
#Calculate 1. The total number of months included in the dataset
    #2. The net total amount of "Profit/Losses" over the entire period
#WORKING
import os
import csv

csvpath=os.path.join('Resources', 'Homework_03-Python_PyBank_Resources_budget_data.csv')
output_path = os.path.join("analysis", "bank_data.txt")

csvfile=open(csvpath)
csvreader=csv.reader(csvfile)


csv_header = next(csvreader) #removed header from csvreader object but saved it in CSV_header if needed
#print(f"CSV Header: {csv_header}")
row_1 = next(csvreader) #removes first row of data and stores it in row_1
#print(row_1)
total_months=1   #total months starts at 1 because removed first month and added it to row_1 varialbe, needed to get total month counts
   
net_total=0  #defines net_total as integer and starts at 0
hold_row=int(row_1[1]) #assigns the integer value of row one Profit & Loss column [1] value for calculation
hold_date=(row_1[0])
pl_list=[hold_row] #creating a new list for P& L values only - assigning row one value to begin list
date_list=[hold_date]
change_pl=[]
total_change=0

print(hold_date)
#when find row of calculation find index and add 1 because moved first row to get date index

for each_row in csvreader:      #for loop takes a row value and subtracts the value above it to get the change in P & L and appendeds the change_pl value to a list
          pl_list.append(int(each_row[1]))  #changes the P&L column to an integer value and adds it to pl_list 
          date_list.append(each_row[0])  #adds the date value to a new list called date_list**********************************
          change_pl_row=(int(each_row[1])-hold_row)  # subtract a p&l value from the row above its value to get the change_pl_row value
          change_pl.append(change_pl_row)  #appends the change_pl_row value to list change_pl
          hold_row=int(each_row[1])   #assign current row to hold_row so can use in next calc as row above it
          total_months=total_months+1
                    
#print(change_pl)

for change_row in change_pl:  #adds each row in change_pl to get the total_change value
    #print(each_row)
    total_change=total_change+change_row
average_change=total_change/len(change_pl)  #calculate the average of Change_pl by the number of values in the list 

great_decrease=0  
great_increase=0 

for small_num in change_pl:
        if great_decrease >= small_num:
            great_decrease=small_num 
            decrease_index=change_pl.index(small_num)

for big_num in change_pl:
        if great_increase < big_num:
            great_increase=big_num 
            increase_index=change_pl.index(big_num)


#print(date_list)
#need to add 1 to indexs to account for header row
decrease_index=decrease_index+1
increase_index=increase_index+1

#grabbing date of greatest decrease from csvreader
decrease_date=(date_list[decrease_index])
print(f'decrease date:  {decrease_date}')
increase_date=(date_list[increase_index])
print(f'increase date:  {increase_date}')

for each_row in pl_list:
    #print(each_row)
    net_total=net_total+each_row

print("Financial Analysis")
print('--------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
#print(total_change)
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: (${great_increase})')
print(f'Greatest Decrease in Profits: (${great_decrease})')

with open(output_path, 'w', newline='') as csvfile:
    csvwriter= csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Anallysis'])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow([f'Total Months: {total_months}'])
    csvwriter.writerow([f'Total: ${net_total}'])
#print(total_change)
    csvwriter.writerow([f'Average Change: ${average_change:.2f}'])
    csvwriter.writerow([f'Greatest Increase in Profits: (${great_increase})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: (${great_decrease})'])


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






  