from requests_html import HTMLSession
import datetime
import pandas as pd
import time 

h = HTMLSession()

location = 'Worcester'

url = f'https://www.google.com/search?q=weather+{location}'

r = h.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"})

numerical = r.html.find('span#wob_tm', first = True).text
#print(numerical)

units = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text
#print(units)

description = r.html.find('div.VQF4g', first = True).find('span#wob_dc', first = True).text
#print(description)

#print(location, numerical, units, description)


#with this we would like to create a csv to input the data
import csv

#lets add the date and time to this
today = datetime.date.today()

time_now = time.localtime()
current_time = time.strftime("%H:%M", time_now )

#Now the format of the table
header = ['Location', 'Date', 'Time' 'Numerical', 'Units', 'Description']
data = [location, today, current_time, numerical, units, description ]

#print(type(data)) 

#Creating CSV file with data in
with open('WeatherWebScraper.csv', 'w', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)  #insert headings
    writer.writerow(data)    #insert data



#to append data to csv(a+)
with open('WeatherWebScraper.csv', 'a+', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)    #insert data


#To automate the program:
def check_weather():
    location = 'Worcester'

    url = f'https://www.google.com/search?q=weather+{location}'

    r = s.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"})

    numerical = r.html.find('span#wob_tm', first = True).text
    #print(numerical)

    units = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text
    #print(units)

    description = r.html.find('div.VQF4g', first = True).find('span#wob_dc', first = True).text
    #print(description)

    today = datetime.date.today()
    time_now = time.localtime()
    current_time = time.strftime("%H:%M", time_now )

    import csv
    header = ['Location', 'Date', 'Time' 'Numerical', 'Units', 'Description']
    data = [location, today, current_time, numerical, units, description ]

    with open('WeatherWebScraper.csv', 'a+', newline = '', encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)    #insert data


while(True):
    check_weather()
    time.sleep(3600)  #weather is checked after every hour




