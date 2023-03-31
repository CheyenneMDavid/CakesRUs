import sys
import gspread
from google.oauth2.service_account import (
    Credentials,
)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]


CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("CakesRUs")


def get_valid_login():
    """
    Requests user to login, in order to use the application.
    The dictionary called "user_creds" stores the username of "Staff" as
    a key and the password of "Cakes123" as it's value.
    Use if and else statements to identify a match.
    Loop request for correct input three times, displaying how many tries
    remain, using the range method. After three failed tries, print to the
    screen that the maximum tries have been reached and program then exits.
    Else, if there is a match, Welcome screen is printed.
    """
    user_creds = {
        "username": "Staff",
        "password": "Cakes123",
    }

    print(
        "Please login. Remember, passwords and usernames are case sensitive"
    )

    for i in range(3):
        print(f"Attempt {i+1}/3:")

        username = input("Please enter your username:  ")
        password = input("Please enter your password:  ")

        if (
            username == user_creds["username"]
            and password == user_creds["password"]
        ):

            print("Access granted \n")

            print("                =================================== \n")
            print("                      Welcome to Cakes R Us ")
            print("                         Customer Orders ")
            print("                Happy Cake Customers always return!! \n")
            print("                ==================================== \n")

            return True
        print("Access denied ")

        attempts_left = 3 - (i + 1)
        if attempts_left > 0:
            print(f"You have {attempts_left} attempt(s) remaining.")
    print("Maximum login attempts reached. Access denied")

    sys.exit()


get_valid_login()
