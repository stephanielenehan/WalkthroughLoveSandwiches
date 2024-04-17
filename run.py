import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

#sales = SHEET.worksheet('sales')
#data = sales.get_all_values()
#print(data)
#above was used to check our API was working. 

# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# function to collect sales data from the user 
# (you add the doc string between the triple quotes to describe what the function is going to do)
def get_sales_data():
    """
    Get sales figures from the user 
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60/n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is: {data_str}")

# Since our code is inside the get_sales_data function, 
# we need to remember to call it so that when we run
# our file the code inside the function will also run
get_sales_data()

# check that by running our code with python3 run.py


