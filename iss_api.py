import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -22.932924
MY_LONG = -47.073845
my_email = "piemegumi@yahoo.com"
password = "fdzjwlmzzyzibylc"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_longitude in range(MY_LONG - 5, MY_LONG + 5 + 1) and iss_latitude in range(MY_LAT - 5, MY_LAT + 5 + 1):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="piemegumi@gmail.com",
                msg="Subject:Look Up\n\nThe ISS is over your head."
            )


