#importing  modules
import requests
from bs4 import BeautifulSoup
import csv
import pandas as p

#scraping the data

url = "https://www.flipkart.com/search?q=mobiles"
r = requests.get(url)

soup=BeautifulSoup(r.content,"html.parser")

titles = soup.find_all('div',class_='_4rR01T')
rattings = soup.find_all('div',class_='_3LWZlK')
reviews = soup.find_all('span',class_='_2_R_DZ')

mt=[]
mr=[]
mre=[]

for titles,rattings,reviews in zip(titles,rattings,reviews):
    mt.append(titles.text)
    mr.append(rattings.text)
    mre.append(reviews.text)


#saving data in CSV

d={'mt':mt,'mr':mr,'mre':mre}

model = p.DataFrame(data=d)

model.to_csv("mobilesdata.csv")