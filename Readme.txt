Python Challenge

Pybank - 

The Pybank chanllenge required python code to read a csv file. 
The data include monthly total of profit associated with a date.
Code was written to loop through the data to determine the following:
	The total number of months included in the dataset
	The net total amount of "Profit/Losses" over the entire period
	Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
	The greatest increase in profits (date and amount) over the entire period
	The greatest decrease in losses (date and amount) over the entire period
The results of the above information was then printed to the screen and to a .txt file.

Once I realized the Profit and Loss needed to be changed to an integer it was easier to get started.
The other challenge I ran into was figuring out how to get the first calculation for the change in profit in loss.
I decided to remove the first row of data and hold it as a value then after each calculation
save the current value to use in the next calculation.
The other calculations were not difficult to do.

Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)

PyPoll

The PyPoll challenge required code to read a csv file.
The data included three columns of data however all 
of the information needed for the assignement could be done using the Candidate
information 