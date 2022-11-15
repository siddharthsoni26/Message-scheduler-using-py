import time

import requests
import schedule

from credits import mobile_number


def send_message():
    resp = requests.post ('https://textbelt.com/text' , {
        "phone" : mobile_number,
        'message': "Hey, Welcome!",
        'key': 'textbelt'
    })

    print(resp.json())

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)