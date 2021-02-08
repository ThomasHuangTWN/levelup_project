import csv
import requests
from bs4 import BeautifulSoup

#url='https://monitoringapi.solaredge.com/site/1458335/power?startTime=2020-07-22%2000:00:00&endTime=2020-07-22%2023:59:00&api_key=6YAMVRNNHPEE6IR3Y4KHCJA9NX0JBVQA'
url='https://google.com'
r=requests.get(url)

soup=BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())

dates = soup.find_all('div')

print(dates)


with open('mycsv.csv', 'w', newline='') as mycsv:
	mycsv_writer=csv.writer(mycsv, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	mycsv_writer.writerow([1,2,3])
	mycsv_writer.writerow([2,3,4])