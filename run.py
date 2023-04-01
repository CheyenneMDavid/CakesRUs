import sys
from datetime import datetime, timedelta, date
import re
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


def get_valid_customer_name():
    """
    Request user input for first name. Validate using regex pattern.
    Request user input for second name. Validate using regex pattern.
    Regex pattern allows for uppercase, lowercase, hyphens and apostrophes.
    Use f-strings to inform user of incorrect input.
    Both requests will individually loop until valid input is submitted,
    before continuing.
    Create new variable of "customer_full_name" by joining first name
    and last name together.
    Apply "title()" method to change first letter of name or parts of a
    name that may be seperated by a hyphen or apostrophe.
    Result is "betty-boo" would become "Betty-Boo" and "o'brien" would
    would become "O'Brien".
    """
    pattern = re.compile(
        r"^[A-Za-z]{1,2}([A-Za-z'-]+[a-z])?(,? [A-Z][A-Za-z'-]+[a-z])*$"
    )
    # The Regex pattern for this code is from the StackOverflow site, here:
    # https://stackoverflow.com/questions/39895282/improving-the-below-regex-
    # for-us-and-uk-names
    # I changed it and tested the change her: https://regexr.com/
    while True:
        first_name = input(
            "Please enter customer's first name."
            "Hyphens and apostorophes are allowed: \n"
        )
        if pattern.match(first_name):
            break
        print(f"{first_name} is NOT a valid first name")

    while True:
        last_name = input("Please enter customer's last name:  ")
        if pattern.match(last_name):
            break
        print(f"{last_name} is NOT a valid last name")

    customer_full_name = first_name.title() + " " + last_name.title()
    print(customer_full_name)
    return customer_full_name


def get_valid_address():
    """
    Request input from user for first of first line of address.
    Use Regex pattern to validate input.  The pattern allows a match using
    "flat", flat number and a letter.  For example: Flat 5b.
    Then, house number, street name, and allows for endings such as
    "drive, close, st, rd", with whitespaces where needed most.
    Loop until input is valid.
    Use f-strings to inform user of incorrect input.
    """
    # RegEx pattern created and tested at: https://regexr.com/

    pattern = re.compile(
        r"^(?:flat)?\s*\d*[,_]?\s*\d+\s+[A-Za-z]+(?:\s+[A-Za-z]+)*"
    )
    while True:
        address = input("enter first line of address:  ")
        if pattern.match(address):
            break
        print(
            f"{address} is not a valid address.  Please enter a valid"
            "first line of address"
        )
    titled_address = address.title()
    print(titled_address)
    return titled_address


def get_valid_postcode():

    """
    Request user input of valid UK postcode.  Validation by Regex pattern
    Loop request till input is valid.
    Use f-string to inform user of incorrect input
    Apply Uppercase.
    """
    pattern = re.compile(r"^[A-Za-z]{1,2}\d{1,2}[A-Za-z]?\s?\d[A-Za-z]{2}$")

    while True:
        postcode = input("Please enter a valid postcode:  ")
        if pattern.match(postcode):
            break
        print(f"{postcode} is an invalid format.")
    uppered_postcode = postcode.upper()
    print(uppered_postcode)
    return uppered_postcode


def get_valid_customer_number():
    """
    Request user input of a valid UK phone number. Validate with RegEx
    pattern.
    Loop request until a valid input it entered.
    Use f-string to inform user of incorrect input
    """
    # The Regex pattern for this code is from the StackOverflow site, here:
    # https://stackoverflow.com/questions/11518035/regular-expression-for-
    # gb-based-and-only-numeric-phone-number
    pattern = re.compile(
        r"^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|"
        r"((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|"
        r"((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$"
    )

    while True:
        phone_number = input("Please enter a valid UK phone number: \n")
        if pattern.match(phone_number):
            print("Thank you \n")
            return phone_number
        print(
            f"You entered '{phone_number}'. This an invalid phone number \n"
        )


def get_valid_customer_email():
    """
    Request user input of valid email address. Validate with regex pattern.
    """
    # Regex pattern for email validation borrowed from StackOverflow, from
    # this page, here: https://stackoverflow.com/questions/201323/how-can-i
    # -validate-an-email-address-using-a-regular-expression
    pattern = re.compile(
        r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"
        r"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|"
        r"\\[\x01-\x09\x0b\x0c\x0e-\x7f])*"
        r")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*"
        r"[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|"
        r"[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|"
        r"[1-9]?[0-9])|[a-z0-9-]*"
        r"[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|"
        r"\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    )
    while True:
        email = input("Please enter a valid email address:  ")
        if pattern.match(email):
            print("thank you")
            return email
        print(f"{email} is not a valid email")


def choose_cake():
    """
    Print cakes available for order to screen.
    Use dictionary with keys and values for the cakes and cake prices
    Request input from user, for cake customer wishes to order.
    Keeping the input short and to the point, with 'girl', 'boy', '18'and
    'wedding'
    Using a standard if and else to handle the input with "Invalid input"
    printed to the screen.
    Return value of "order_date" for when the cake was ordered using
    the datetime module.
    """
    print("Cakes available to order: \n")
    print("New Baby Boy, cost £35.00")
    print("New Baby Girl, cost £35.00")
    print("Wedding, £70")
    print("18th Birthday, cost £35.00 \n")

    cakes = {"girl": 35, "boy": 35, "18": 35, "wedding": 70}

    while True:
        cake_choice = input(
            "Enter Cake type as: 'Boy', 'Girl', 'Wedding' or '18'  "
        )
        if cake_choice in cakes:
            cost = f"£{cakes[cake_choice]}"
            cake_type = cake_choice.capitalize()
            order_date = datetime.now().strftime("%d-%m-%Y")
            print(f"Cake type: {cake_type} cake  -  Cost: {cost}")
            print(f"Ordered on:  {order_date}")
            return cost, cake_type, order_date
        print("Invalid input, please choose a valid cake.")


def date_required():
    """
    Informs user of todays date and the earliest available date for cakes
    to be delivered.
    Requests user input of the date that the customer wants the cake
    delivered.
    If the requested date falls on a Sunday or is within 14 days, the user
    is requested to enter a different date.
    Dates are displayed in dd/mm/yyy format for ease of reading by user.
    """

    print("Cakes cannot be ordered for Sunday deliveries")
    print("Cakes must be ordered two weeks in advance of required date.")

    today = date.today()
    next_delivery_date = today + timedelta(days=14)

    print(
        f"Today's date is '{today.strftime('%d/%m/%Y')}', so the delivery "
        "date must be a minimum of 14 days from now."
        f"{next_delivery_date.strftime('%d/%m/%Y')} is the earliest date "
        "available"
    )

    while True:
        required_date = input(
            "Please enter date the customer requires the cake (DD/MM/YYYY): "
        )
        required_date = datetime.strptime(required_date, "%d/%m/%Y").date()

        day_of_week = required_date.weekday()

        order_date = date.today()
        time_gap = required_date - order_date

        if day_of_week != 6 and time_gap.days >= 14:
            return required_date
        else:
            print(
                "This date is not valid. "
                "Please ensure the date is at least two "
                "weeks away and not on a Sunday."
            )


# get_valid_login()
# get_valid_customer_name()
# get_valid_address()
# get_valid_postcode()
# get_valid_customer_number()
# get_valid_customer_email()
# choose_cake()
date()
