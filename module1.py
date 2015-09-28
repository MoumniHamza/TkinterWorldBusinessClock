from geopy import geocoders # $ pip  install geopy
import calendar
from datetime import datetime
import pytz # $ pip install pytz
def hours(x):
        g = geocoders.GoogleV3()
        place, (lat, lng) = g.geocode(x)
        timezone = g.timezone((lat, lng)) # return pytz timezone object
        print(timezone.zone)
        now = datetime.now(timezone) 
        weekday = now.weekday() 
        print(calendar.day_name[weekday])
        print(now)
        return hours
        