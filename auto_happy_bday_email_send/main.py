##################### Extra Hard Starting Project ######################
import random
import smtplib
import pandas
import datetime as dt


bday_data = pandas.read_csv("birthdays.csv")
bday_dict = bday_data.to_dict(orient="records")
print(bday_dict)

today = dt.datetime.today()
today_tuple = (today.month, today.day)
birthdays_dict = {(row.month, row.day) : row for(index, row) in bday_data.iterrows()}
if today_tuple in birthdays_dict:
    random_num = random.randint(1,3)
    file_path = f"letter_templates/letter_{random_num}.txt"
    name = birthdays_dict[today_tuple]["name"]
    email = birthdays_dict[today_tuple]["email"]

    with open(file_path) as letter_file:
        letter_content = letter_file.read()
        x = letter_content.replace("[NAME]", name.title())

    my_email = "piemegumi@yahoo.com"
    password = "fdzjwlmzzyzibylc"
    with smtplib.SMTP("smtp.mail.yahoo.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday {name.title()}!\n\n{x}."
        )






