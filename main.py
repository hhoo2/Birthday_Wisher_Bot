# Import necessary libraries
import pandas  # For data handling
import smtplib  # For sending email
import datetime as dt  # For working with dates
import random  # For randomness

# Your email and password for sending the email
MY_EMAIL = "annaanderson0702@gmail.com"
MY_PASSWORD = "mrbo tjme wxgx cfsf"

# Load birthday data from 'birthdays.csv' using pandas
birthdays_dict = pandas.read_csv("birthdays.csv").to_dict(orient="records")

# List of letter templates
letter_templates = ["letter_template/letter_1.txt", "letter_template/letter_2.txt", "letter_template/letter_3.txt"]

# Check if today is someone's birthday and send a personalized email
for birthday in birthdays_dict:
    name, email, year, month, day = birthday["name"], birthday["email"], birthday["year"], birthday["month"], birthday["day"]

    if dt.date.today().month == month and dt.date.today().day == day:
        # Choose a random letter template and personalize it
        with open(random.choice(letter_templates)) as letter_file:
            content = letter_file.read()
        content = content.replace("[NAME]", name)

        # Establish an SMTP connection and send a birthday email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject: Happy Birthday\n\n{content}"
            )
