import pandas
import datetime as dt
from random import randint
import smtplib
import os

SENDER_EMAIL = "ezratawachiapps@gmail.com"
MY_PASS = "bvjq fijs oouk sltr"


now = dt.datetime.now()
now_month = now.month
now_day = now.day
df = pandas.read_csv("birthdays.csv")
today_bd_list = df[(df['month'] == now_month) & (df['day'] == now_day)].to_dict(orient="records")
if len(today_bd_list) > 0:
    random_index_l = randint(1,3)
    with open(f"letter_templates/letter_{random_index_l}.txt") as letter:
        content = letter.read()
    for birthday in today_bd_list:
        birthday_name = birthday["name"]
        birthday_email = birthday["email"]
        letter = content.replace("[NAME]",birthday_name).replace("Angela","Wisher")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(SENDER_EMAIL,MY_PASS)
            connection.sendmail(from_addr=SENDER_EMAIL,to_addrs=birthday_email,msg=f"Subject:Happy Birthday {birthday_name}!: \n\n{letter}")



else:
    print("No bd today")





