# CakesRUs

CakesRUs is an application that records the ordering and delivery of cake
orders.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Dependencies and Required Packages](#dependencies-and-required-packages)
- [Installation](#installation)
- [Use](#use)
- [Testing of Functions](#testing-of-functions)
- [Further Development](#further-development)
- [Copy / Improve / Constribute](#copy--improve--constribute)
- [Credits, Acknowledgments and Appreciation-to](#credits-acknowledgments-and-appreciation-to)

___

## Features

This application runs in a Python terminal and uses a pandas dataframe.
It then updates updates Google sheets.
___

## Prerequisites

- Python 3.*
- A Google account in order to access Google Sheets and Google Drive.

___

## Dependencies and Required Packages

The following Python modules

- gspread
- google-auth2
- regex
- pandas
- sys
- datetime, timedelta, and date.

___

## Installation

If you don't have python installed on your machine, you can download it and
install it from the [official website](https://www.python.org/downloads/)

To add the Google Sheets and Drive, goto the
[Google Developers Console](https://console.cloud.google.com/),
where you can create projects.  Enable the APIs for Google Sheets and
Google Drive.  And then create a service account and download the json file.

You can find more detailed instructions in how to use the APIs in the
official documanteation within the [Google Sheets quickstart guide](<https://developers.google.com/sheets/api/quickstart/python>) and the
[Google Drive quickstart guide](https://developers.google.com/drive/api/quickstart/python)

___

## Use

### User sign-in

When the application is run, the user is asked to log in using a username
and password, which are case sensitive and must match the ones stored
within the application.  The username is "Staff" and the password is "Cakes123"
The application allows for 3 attempts to sign in and informs the user
howmany attempts remain out of three that are allowed, eachtime a sign in fails
When there's three failed attempts, the application exits.

### Entering details for the order

When the login in successful, thje "Welcom" screen displays and the user is
asked to enter the following customer details:

- First name
- Last name
- First line of the street address
- Postcode
- Customer's telephone number
- Customer's email

All the requested input are validated within the functions, which continue to
loop the requests until the input is invalid.

Cakes that are available to order and their accompanying price are printed to
the screen and the user is asked to enter the customers choice.
The cakes are: "New Baby Boy", "New Baby Girl", "Wedding", and
"18th Birthday".  But to ensure simplicity of entry, the cake names are kept
to simple one word entry of "Boy", "Girl", "Wedding" and "18".

When the cake is selected, an order date is created using the current date
and then constraints of delivery are printed to the screen.  The contraints
are that orders muct be made 14 days in advance of the required date and that
cakes can't be delivered on a Sunday.
The user is requested to enter a date for when the cake is required.  If the
input date is less than 14 days away or if it falls on a Sunday, the user is
told that the date is invalid and to enter a valid date.  The request for a
valid date to be entered loops until a valid date is entered.

Once a valid required date is accepted, all the details that have been provided
update the csv file called cakes.csv and then the csv file is used to update
the Google Sheets.

Validation for the street addresses, postcodes, telephone numbers and emails
is done using regex pattern matching.
___
___

## Testing of functions

### get_valid_login()

Purpose is to provide secure access to the application, using a predefined
username and password, with limited attempts.

When purposely inputting incorrectly, the function denies me access and
informs me of howmany attempts I have remaining and requests I enter my
details again. After I purposely entered incorrect details, the application
gave one final display of "Access Denied" and then exited.
When I entered correct details, the welcome screen was displayed and then the
application moved to the next function.

### get_valid_customer_name()

Purpose is to request, accept and validate first names and last names, which
may be hyphenated and contain apostrophes, and the create a new variable called
full name by joinging them together and ensure that each segment of the name
started with a capital letter. For both first name and last name requests,
when I input a name that had spaces or any characters other that letters,
hyphen and apostrophes, the input was considered invalid and correct input
was requested again.
When I provided correct input, the first name and last name were returned as
full name with each part of the full name starting with a capital letter.

### get_valid_address()

Purpose is to request, accept and validate the first line of an address, accounting
for the possibility of it being a flat number, before the house number in a
street.

I've input a variety of adresses, including variations using flat numbers and
letters such as flat 2b, followed house numbers, street names and endings such
as "Drive", "Road", "Way", "Street", etc...  Also abreviations such as "Dr",
"Rd", "St" which all passed.  When I've input a street/road name without a
house number first, the function has returned a response of invalid. Whilst
the regex pattern matching does validate valid address, there's shortfalls.
An address could be entered and misspelled, but still accepted.
See: [Regex Pattern Limitations](#regex-pattern-limitations)

### get_valid_postcode()

Purpose is to request, accept and validate UK postcodes. I've purposely entered
gibberish as postcodes, which have proved to be invalid. I've also entered
various postcodes which I know to be correct, and they've all been validated
by the function.
See: [Regex Pattern Limitations](#regex-pattern-limitations)

### get_valid_customer_number()

Purpose is to request, accept and validate a UK telephone number. I've
purposely entered incorrect format numbers which can not be valid and the
has found them to be invalid.
I've input both landline numbers which I know to be correct and also
mobile numbers which I know to be correct. Both have been validated by the
function.
See: [Regex Pattern Limitations](#regex-pattern-limitations)

### get_valid_customer_email()

Purpose is to request, accept and validate email addresses.  Email addresses
that I know to be correct have been confirmed, whilst entries which I know
couldn't possibly be correct have been found as invalid by the function.
See: [Regex Pattern Limitations](#regex-pattern-limitations)

### choose_cake()

Purpose of the function is to present the user with the cakes that are
available and request they input their choice.  The input for each cake was
simplified to minimise user error for input.  But still requires the correct
response. When I input incorrectly, the function looped at is was expected to
and when correct input was entered, the function then displayed the price that
was associated with that cake, as it should.

### date_required()

Purpose it to accept a date for delivery of the cake, with the limitations
that the delivery date can't be on a Sunday or within 14 days of the cake being
ordered. When the function runs, it tells the user the current date and the
earliest date that a cake can be ordered for. It then request the user enter
a desired delivery date, using the format of dd/mm/yyy.

When I entered anything other than a date further than 14 days away, in a
format of dd/mm/yyy, the function said the date was invalid and looped the
request again. When I entered a date in the format of dd/mm/yyy, which was
more than 14 days away, but I knew to fall on a Sunday, the function said the
date was invalid and looped the request again.
When I entered a date in the format of dd/mm/yyyy which was more than 14 days
away and did not fall on a Sunday, the function accepted the date and moved
to the next function.

### write_to_csv()

Purpose of this function is to use the values of the variable created by all
the previous functions and use them to update the csv file. This function does
not require any user input, and is auomatically executed after a date is
accepted for when the cake is required.

This function acted as it was expected.

___

## Regex Pattern Limitations

With all the functions that rely on a regex pattern, regardless of how
it's been formulated, there is a risk of false validation,
purely because the input meets the "required pattern".  An example of this is
a mobile number which may meet all the criteria, but hasn't been issued to
anyone yet.

___

## Conclusion

Using regex is useful and unlike APIs, regex is free.  But it can validate something incorrectly because it only searches to see if something meets the criteria of what it would look like, if it were to exist. But this is not proof of that thing existing. So although APIs may cost, they would be of greater benefit.

___

## Further Development

The planned future changes in this application are: Increase the range of cakes
available to order.  Not so much in the number of types, but instead, where the
person ordering is able to design the cake they want. A "Build-a-Cake" option,
which would also tally up a cost, so the customer is in control of what they're
ordering and also how much they want to spend on it. Whilst this application
runs in a terminal, it would be well suited to being incorporated into an
application which had a front.

I believe that such further functionality would be well suited to a full
website application that incorporated this application into it, because it
could then make use of an interface where the user could create their cake and
have a visual representation of what it could look like.

___

## Deployment

These are the steps I followed, in order to deploy my project on the [Heroku](https://dashboard.heroku.com/apps) platform:

- Sign into [Heroku](https://dashboard.heroku.com/apps) and click on "New" to create a new application.

- Choose a name for the application, select your region and then click on "Create App"

The application needs to access the contents of the creds.json file.

- Goto the "Settings" tab and scroll down to "Config Vars".

- In the field that says "KEY", enter "CREDS".  In the field for "VALUE", cut & paste the contents of the creds.json file into it and then click on "Add"

- below this, again in the field that says "KEY", enter "PORT" and in the field that says "Value" enter "8000" and then click "Add"

- Scroll down and click on "Add Buildpacks".

- Select "Python" and click "Save changes".

- Click on "Add Buildpacks" again and select "node.js" and click "Save changes".

- Select the "Deploy" tab and scroll to "Dployment method" and click on "Connect to GitHub".

- Enter the GitHub repo name and click search.

- Click connect to link up the Heroku app and the GitHub repository code.

- Scroll down to "Manual deploy", ensure "master" is selected and then click "Deploy Branch".

- The deployed application can be found here.

___

## Copy / Improve / Constribute

If anyone wishes to copy and improve this software by contributing changes,
please do.  You will find instructions from
[GitHub on how to do this.](https://docs.github.com/en/get-started/quickstart/contributing-to-projects#forking-a-repository)
___

## Credits, Acknowledgments and Appreciation to

[Stack Overflow](https://stackoverflow.com/) for regex patterns
used in this application.

[Regexr.com](https://regexr.com/) for the facility to
create and test patterns.

[Corey Schafer](https://www.youtube.com/@coreyms) for his Python tutorial on the [Datetime Module](https://www.youtube.com/watch?v=eirjjyP2qcQ)

[Keith Galli](https://www.youtube.com/@KeithGalli) and his Python tutorial on [Pandas](https://www.youtube.com/watch?v=vmEHCJofslg&t=1715s)
