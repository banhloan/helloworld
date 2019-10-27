import random 
'''
Cookie shop scenario
You own a cookie shop. There is a constant stream of customers that vary in number that goes to your shop in
each hour.  
Everytime a batch of customer comes into your shop, they buy all your cookies and split it amongst them 
evenly. You then have to bake a new batch of 100 cookies to sell to the next batch.
For auditing purposes, your task is to print out the average number of cookies bought per customer
from 9am - 9pm.

NOTE: Customers can buy 0 cookies as they are only "window shopping"
NOTE: You are expected to write code that will ask you "How many cookies do you want to bake today?" in the command line, and accepts and input for an answer
This will also instantiate the variable numberOfCookies to your answer.
'''
numberOfCustomers = random.randint(0,10) # first hour
print("How many cookies do you want to bake today?")
numberOfCookies = input()

time = ["9am","10am","11am","12pm","1pm","2pm","3pm","4pm","5pm","6pm","7pm","8pm","9pm"]
for i in range(len(time)):
    numberOfCustomers = random.randint(0,10)
    try:
        numberOfCookiesPerCustomer = int(numberOfCookies)/numberOfCustomers
    except ZeroDivisionError:
        numberOfCookiesPerCustomer = 0
    print("The number of cookies sold per customer is " + str(numberOfCookiesPerCustomer) + " at " + time[i])



