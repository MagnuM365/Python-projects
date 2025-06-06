import smtplib
import random
import datetime as dt
import pandas

MY_EMAIL = "sthavicky555@gmail.com"
MY_PASSWORD = "jaqcxonwqsdchzzf"

now = dt.datetime.now()
today = (now.month, now.day)

# Use pandas to read the birthdays.csv

data = pandas.read_csv("birthdays.csv")
2
# Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# Use the replace() method to replace [NAME] with the actual name. 

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        updated_contents = contents.replace("[NAME]", birthday_person["name"])
    
    with(smtplib.SMTP("smtp.gmail.com")) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday\n\n{updated_contents}")





