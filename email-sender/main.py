import smtplib
import datetime as dt
import random
my_email = "myemail@gmail.com"
password = "password"

now = dt.datetime.now()
weekday = now.weekday()

if weekday ==1:
    with open('quotes.txt') as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
    print(quote)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{quote}")




#you should allow less secure app access on

