# importing relevant libraries to be able to print date/time
import os
from datetime import datetime, date

# defining a function which prints out the current date and time

def print_current_date_and_time():
    print (f"Today's date and time is:  {datetime.today()}")

# first requesting the user to provide an input as per requirements of Practical Task 2 

msg = input ("Please provide a message to print: ")

# printing the message as per Practical Task 2 initial instructions
print (f"User has inputted the message : {msg}")

# call function to print date and time
print_current_date_and_time()

