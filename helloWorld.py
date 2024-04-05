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

# work out the time of the day and establish a greeting accordigly

# Get the current time
current_time = datetime.now().time()

# Extract the hour from the current time
current_hour = current_time.hour

# Greet the user based on the current hour
if 5 <= current_hour < 12:
    greeting = "Good morning"
elif 12 <= current_hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

# Print the greeting
print(f"\n{greeting} User, Program will exit now - Goodbye")

# 
