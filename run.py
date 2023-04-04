# All imported modules that are used in the application.
import sys
from datetime import datetime, timedelta, date
import re
import pandas as pd
import gspread
from google.oauth2.service_account import (
    Credentials,
)

# The OAuth 2.0 scopes for accessing the APIs
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
    # Dictionary storing "username" and "password" as the keys and "Staff" and
    # "Cakes" as their respective values.
    user_creds = {
        "username": "Staff",
        "password": "Cakes123",
    }

    print(
        "Please login. Remember, passwords and usernames are case sensitive"
    )

    # Using the range method, with i as the variable, 1 is added to i eachtime
    # a wrong attmpt is made, until the final 3rd attempt.
    # An f-string is used to display the attempt number against the 3 allowed.
    for i in range(3):
        print(f"Attempt {i+1}/3:")

        # Requests user input which is validated using the "user_creds".
        username = input("Please enter your username:  ")
        password = input("Please enter your password:  ")

        if (
            username == user_creds["username"]
            and password == user_creds["password"]
        ):
            # Granted upon password match and print's welcome screen.
            print("Access granted \n")

            print("                =================================== \n")
            print("                      Welcome to Cakes R Us ")
            print("                         Customer Orders ")
            print("                Happy Cake Customers always return!! \n")
            print("                ==================================== \n")

            # Returns "True" when there's a match and exits the loop.
            return True

        # Executed when user enters incorrect username and passwords.
        print("Access denied ")

        # attempts_left, is the changing value of whatever 3(maximum attempts)
        # minus the changing value of i + 1, depending on howmany times the
        # for loop has been executed.
        attempts_left = 3 - (i + 1)

        # The if statement executes, all the time that the value of
        # "attempts_left" is greater than "0"
        if attempts_left > 0:
            # String literal used to display the remaining number of attempts.
            print(f"You have {attempts_left} attempt(s) remaining.")
    print("Maximum login attempts reached. Access denied")

    # Used to exit after the maximum number of failed attempts is reached.
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
    # The Regex pattern for this code is from the StackOverflow site, here:
    # https://stackoverflow.com/questions/39895282/improving-the-below-regex-
    # for-us-and-uk-names
    # I changed it and tested the change her: https://regexr.com/
    pattern = re.compile(
        r"^[A-Za-z]{1,2}([A-Za-z'-]+[a-z])?(,? [A-Z][A-Za-z'-]+[a-z])*$"
    )

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

    # full_name variable created by concatenation of the first_name and
    # last_name variables, and title method applied to give each name a
    # capital letter, even if hyphenated.
    full_name = first_name.title() + " " + last_name.title()
    print(full_name)

    # Returns the variable "full_name", so it can be used by other functions.
    return full_name


def get_valid_address():
    """
    Request input from user for first of first line of address.
    Use Regex pattern to validate input.  The pattern allows for the option of
    using "flat", flat number and a letter.  For example: Flat 5b.
    Then, house number, street name, and allows for endings such as
    "drive, close, st, rd", with whitespaces where needed most.
    Loop until input is valid.
    Use f-strings to inform user of incorrect input.
    """
    # RegEx pattern created and tested at: https://regexr.com/
    # Pattern optional flat numbers before the actual street address
    pattern = re.compile(
        r"^(?:flat)?\s*\d*[,_]?\s*\d+\s+[A-Za-z]+(?:\s+[A-Za-z]+)*"
    )

    while True:
        address = input("enter first line of address:  ")

        # If there's a pattern match, the code breaks. Otherwise, it
        # uses a string literal to tell the user that their input wasn't
        # valid and request they try again.
        if pattern.match(address):
            break
        print(
            f"{address} is not a valid address.  Please enter a valid"
            "first line of address"
        )
    # If the input is valid, title method is applied, creating the new variable
    # "titled_address"
    titled_address = address.title()
    print(titled_address)

    # Returns the variable "titled_address", so it can then be used by
    # other functions.
    return titled_address


def get_valid_postcode():
    """
    Request user input of valid UK postcode.  Validation by Regex pattern
    Loop request till input is valid.
    Use f-string to inform user of incorrect input
    Apply Uppercase.
    """
    # Pattern for postcode was borrowed from Stack Overflow at this page
    # here: https://stackoverflow.com/questions/164979/regex-for-matching-
    # uk-postcodes , which says that the pattern was originally supplied
    # by the uk government, so probably the most comprehensive, without using
    # a subscription API
    pattern = re.compile(
        r"([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|"
        r"(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|"
        r"([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})"
    )

    while True:
        # Requests user input
        postcode = input("Please enter a valid postcode:  ")
        if pattern.match(postcode):
            break
        print(f"{postcode} is an invalid format.")

    # If the input is valid, title method is applied, creating the new variable
    # "uppered_postcode"
    uppered_postcode = postcode.upper()
    print(uppered_postcode)

    # Returns the variable "uppered_postcode", so it can then be used by
    # other functions.
    return uppered_postcode


def get_valid_customer_number():
    """
    Request user input of a valid UK phone number. Validate with RegEx
    pattern.
    Loop request until a valid input it entered.
    Use f-string to inform user of incorrect input.
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
        # Requests user input for email, matches against the regex pattern
        # in order to validate and  returns "email" so it can be used by
        # other functions.
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

    # Prints to the terminal, telling the user which cakes are available cakes
    # that are available to order and their price
    print("Cakes available to order: \n")
    print("New Baby Boy, cost £35.00")
    print("New Baby Girl, cost £35.00")
    print("Wedding, £70")
    print("18th Birthday, cost £35.00 \n")

    # Dictionary to keep the cake types as keys and the prices as the values.
    cakes = {"girl": 35, "boy": 35, "18": 35, "wedding": 70}

    while True:
        # Requests user input for choice of cake.  If the input is valid,
        # the dictionary containing the key and values of cake type and
        # price are used to create the variables of "cost" and "cake_type"
        # and are returned along with the variable "order_date", so they
        # can be used by other functions.
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
        print(
            f" You chose '{cake_choice}', which was NOT a valid choice,"
            f"please choose from the list of available cakes, correctly."
        )


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

    # Used to ensure that the required delivery dates are not earlier
    # than two weeks by using the date.today method and timedelta with
    # a difference of 14days
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

        # Using the not equal to day 6 in the week, to designate a sunday and
        # is greater than or equal to 14, to ensure dates accepted are not a
        # Sunday and more than 2 weeks away.
        if day_of_week != 6 and time_gap.days >= 14:

            # returns "required date so it can be used by other functions"
            return required_date
        print(
            "This date is not valid. "
            "Please ensure the date is at least two "
            "weeks away and not on a Sunday."
        )


def write_to_csv(
    full_name,
    street_address,
    postcode,
    phone_number,
    email,
    required_date,
    cake_type,
    order_date,
    cost,
):
    """
    Uses variables created by the other functions to update the CSV file
    called "cakes.csv" by creating a new dataframe called "new_row" and then
    "new_row" is added to the original "df".
    """

    # Mega thanks to the efforts of Keith Galli and his YouTube channel
    # here: https://www.youtube.com/watch?v=vmEHCJofslg&t=1715s
    # And his resources here: https://github.com/KeithGalli/pandas
    # which helped me really a lot for this project.
    df = pd.read_csv("cakes.csv")

    new_row = pd.DataFrame(
        {
            "Full name": [full_name],
            "First line of address": [street_address.title()],
            "Postcode": [postcode.upper()],
            "Phone number": [phone_number],
            "Email address": [email],
            "Date required": [required_date],
            "Cake type": [cake_type],
            "Cost": [cost],
            "Date ordered": [order_date],
        }
    )

    # The df variable is redefined by concatenating the original df and
    # new_row, whilst ignoring the original indexes from either of them.
    # Once they're concatenated, a new index is created for the new,
    # re-defined df variable
    df = pd.concat([df, new_row], ignore_index=True)

    # The redefined variable "df" is used to write to the "cakes.csv" file.
    df.to_csv("cakes.csv", index=False)

    print("Order details recorded. \n \n")


def update_sheets():
    """
    Uses the previously updated CSV file to update Google Sheets
    """
    worksheets = SHEET.get_worksheet(0)
    df = pd.read_csv("cakes.csv")
    row = df.shape[0]
    column = df.shape[1]

    # Defining a new variable called "cells_list" which represents the list
    # of cells (literaly) on the worksheet that are going to be filled with
    # the data from df, which has been created using cakes.csv.
    # The chr and ord function workout the amount of space needed to house
    # the data from df.  The starting point will be top left of the sheets
    # which is A2 because it's not counting the index or headings.
    cells_list = worksheets.range(f"A2:{chr(ord('A') + column - 1)}{row + 1}")

    # Zip is used to iterate over cell_lists and the data content of df,
    # until all the needed the worksheet cells are populated.
    for cell, value in zip(cells_list, df.values.flatten()):
        cell.value = value
    worksheets.update_cells(cells_list)

    # Confirms that the Google sheets have been successfully updated.
    print("Google Sheets updated")


def main():
    """
    Runs all program functions after the initial "get_valid_login" fu
    """
    full_name = get_valid_customer_name()
    street_address = get_valid_address()
    postcode = get_valid_postcode()
    phone_number = get_valid_customer_number()
    email = get_valid_customer_email()
    cost, cake_type, order_date = choose_cake()
    required_date = date_required()

    # Takes all the variable and their values and uses them as arguments
    # to update the "cakes.csv" file.
    write_to_csv(
        full_name,
        street_address,
        postcode,
        phone_number,
        email,
        required_date,
        cake_type,
        order_date,
        cost,
    )

    # Uses the freshly written to file, "cakes.csv" to update Google Sheets.
    update_sheets()


# This is the first function that is called, which allows the user to log in
# and then use the application to record orders for cakes, from customers.
get_valid_login()

main()
