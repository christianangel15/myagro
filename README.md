# myagro
Consider a farmer with an account having 3 loans L1, L2 and L3 as shown bellow:
Loan L1 has a daily rate of R1 and starts in D1 days
Loan L2 has a daily rate of R2 and starts in D2 days
Loan L3 has a daily rate of R3 and starts in D3 days

Each farmer has a device that lights up their home that they can use as collateral for several loans. When a farmer takes out a loan, this device is locked
and payment of the amount equivalent to the daily rate unlocks the device for 1 day of lighting. 
The daily rate that a farmer has to pay to get a day of lighting (the account daily rate)is the sum of the daily rates of all the active loans that the 
farmer has for that particular day. The account daily rate on a particular day is determined by the summation of daily rates of all loans that have started by that day.
whenever a farmer makes a payment K:
	1. if K > account daily rate on that day, the account daily rate is deducted from the paid amount k, the farmer gets a day of lighting and the balance
	is transfered to the next day. On the next day, if the amount transfered is greater than the daily rate on that day, the farmer gets a day of power and the 
	daily rate that day is deducted from the amount and the balance transfered to the 3rd day. This goes on until the amount left is less than the account daily rate that day 
	in which case the farmer does not get any days of lighting and nothing is transfered.

farmers can not get fractions of days of power. e.g. of a farmer with an account daily rate of 3 pays 5 shillings, the farmer gets only 1 day of lighting
if a farmer pays in excess of the daily rate, the balance is carried over to the following day and evaluated for days of lighting based on that day. e.g. if a 
farmer with a daily rate of 1/= today and a daily rate of 2/= tomorrow pays 3/=, he gets 1 day of lighting at 1/= and 1 day of lighting the following day at 2/= so, total
days of lighting will be 2.

if none of the loans has started, all the paid amount is move forward to the next day and the farmer does not get any days of lighting for that day

1.(a): write a function that takes the 6 augments above (R1, D1, R2, D2, R3, D3 as well as the paid amount K and determines the total days of lighting the farmer can get.

e.g. consider : get_days_of_power(R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=21000)

Loan L1 has a daily rate of R1 = 1000 and starts in D1 = 3 days
Loan L2 has a daily rate of R2 = 500 and starts in D2 = 10 days
Loan L3 has a daily rate of R3 = 1500 and starts in D3= 7 days
and farmer pays k = 21,000

first 2 days  account daily rate = 0 days of power = 0
day 3 to day 6 account daily rate = 1000, days of power = 4 days of power at 4000
day 7 to 9 account daily rate = 2500, days of power = 3 days at 7500
day 10 to 12 account daily rate = 3000, days of power = 3 days at 9000 
balance 500 less than daily rate of 3000 so its written off.
total days of power = 10
