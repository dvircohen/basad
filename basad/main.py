import requests
import sys
import json
import datetime

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

class ShabbatCheker():
    def __init__(self):
        pass

    def check(self):
        """
        Use hebcal RESP API to check if the code is running on Shabbat
        :return:
        """
        req = requests.get('https://www.hebcal.com/shabbat/?cfg=json&geonameid=3448439&m=50')
        j = json.loads(req.text)

        for item in j['items']:
            if item['category'] == 'candles':
                candles = item['date']
                candles = datetime.datetime.strptime(candles[:-6], '%Y-%m-%dT%H:%M:%S')

            if item['category'] == 'havdalah':
                havdalah = item['date']
                havdalah = datetime.datetime.strptime(havdalah[:-6], '%Y-%m-%dT%H:%M:%S')

        if time_in_range(candles, havdalah, datetime.datetime.now()):
            print("Your code ran on Shabbat and therefor not kosher. Exiting.")
            sys.exit(0)
        else:
            print(f"It is not Shabbat yet. You still have {( candles- datetime.datetime.now()).days} days")

