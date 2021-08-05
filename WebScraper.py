from bs4 import BeautifulSoup
import requests
import time
from datetime import date
import csv

URL = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

WAIT_TIME = 6*1 # 10 minutes

def find_jobs(unfamiliar_skills):
    date_of_search = date.today().strftime("%d/%m/%Y")
    
    print("##########################################")
    print('Initializing search...')
    print(date_of_search)
    print("##########################################")
    
    print(f'\nFiltering out {unfamiliar_skills}...\n')

    html_text = requests.get(URL).text

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:

        published_date = job.find('span', class_='sim-posted').span.text.strip()

        if 'few' in published_date:
        	company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        	skills = job.find('span', class_='srp-skills').text.strip()
        	more_info = job.header.h2.a['href']
        	if unfamiliar_skills not in skills:
        	
        		with open('jobs/jobs.csv', 'a', newline='') as f:
        		
        			writer = csv.writer(f)
        			writer.writerow([company_name, skills, more_info, date_of_search, published_date])
            
if __name__ == "__main__":
	print('Welcome to the Job Hunt Web Scraper.')
	unfamiliar_skills = input('What skill should the search engine filter out? ')
	
	while True:
		find_jobs(unfamiliar_skills)
		time.sleep(WAIT_TIME)
	
	
	
	
	
