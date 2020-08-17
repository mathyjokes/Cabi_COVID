import requests
from bs4 import BeautifulSoup
import boto3

s3=boto3.client('s3')
list=s3.list_objects(Bucket='capitalbikeshare-data')['Contents']
    
title = []
link = []
full_text = []

url = "https://s3.amazonaws.com/capitalbikeshare-data/index.html"
response = requests.get(url)
if response.status_code == 200:
    page = response.content
    sopa = BeautifulSoup(page, 'html.parser')
    for green in sopa.find_all('span', {'class', 'green-title'}):
        episode_name = green.find('a').text
        episode_page = green.find('a').get('href')
        response = requests.get(episode_page)
        if response.status_code == 200:
            page = response.content
            sopa = BeautifulSoup(page, 'html.parser')
            episode_text = sopa.find('div', {'class', 'podcast_intro'}).text
            title.append(episode_name)
            link.append(episode_page)
            full_text.append(episode_text)
            print(episode_name)


alls = [title, link, full_text]
filename = "FREAKONOMICS_EPISODES.csv"
field_names = ['Title', 'Link', 'Text']
with codecs.open(filename, "w", encoding = 'utf-8-sig') as logfile:
    logger = csv.DictWriter(logfile, fieldnames = field_names)
    logger.writeheader()
    for line in zip(*alls):
        result = {}
        result['Title'] = line[0]
        result['Link'] = line[1]
        result['Text'] = line[2]
        logger.writerow(result)

print 'Congratulations! Look in your current folder for "%s" for the results of your search' %filename        