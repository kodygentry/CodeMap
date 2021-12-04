import requests
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

def extract(loc, job, page):
    
    time.sleep(20)
    url = 'https://www.ziprecruiter.com/candidate/search?radius=25&search='
    url2 = '&location='
    url3 = '&page='
    
    if loc == 1:
        location = 'Austin%2C+TX'
    elif loc == 2:
        location = 'Dallas%2C+TX'
    elif loc == 3:
        location = 'Raleigh%2C+NC'
    elif loc == 4:
        location = 'San+Jose%2C+CA'
    elif loc == 5:
        location = 'Charlotte%2C+NC'

    if job == 1:
        dicipline = 'machine+learning'
    elif job == 2:
        dicipline = 'full+stack'
    elif job == 3:
        dicipline = 'data+scientist'
    elif job == 4:
        dicipline = 'software+engineer'
    elif job == 5:
        dicipline = 'data+mining'

    driver.get(url + dicipline + url2 + location + url3 + str(page))
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'job_content')
    for item in divs:
        company = item.find('a', class_ = 't_org_link name').text
        title = item.find('span', class_ = 'just_job_title').text
        try:
            location = item.find('a', class_ = 't_location_link location').text
        except:
            location = ''
        summary = item.find('p', class_ = 'job_snippet').text.strip()
        link = item.find('a', class_ = 'job_link t_job_link')#find href
        link = link.attrs['href']#extract href data from link

        job = {
            'company': company,
            'title' : title,
            'location' : location,
            'summary' : summary,
            'link' : link
        }
        joblist.append(job)
    return
        
joblist = []

for x in range(1, 6):#loops through 5 different cities
    for y in range(1, 6):#loops through 5 different jobs
        for z in range(1, 3):#Loops through 3 pages      
            c = extract(x,y,z)
            transform(c)
#jsonStr = json.dumps(joblist)
#print(jsonStr)
with open('all_locations_all_jobtypes.json', 'w') as json_file:
    json.dump(joblist, json_file)
print('Number of results: ', len(joblist))
