from bs4 import BeautifulSoup
import requests

def getYOE(input_string):
  for index, char in enumerate(input_string):
    if char.isdigit():
      return input_string[index:]
  return ""


html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for index, job in enumerate(jobs):
  header = job.find('header', class_ = 'clearfix')
  company_name = header.find('h3').text
  job_title = header.find('h2').strong.text
  years_experience = getYOE(job.find('ul', class_ = 'top-jd-dtl clearfix').li.text)
  location = job.find('span').text
  skills = job.find('ul', class_ = 'list-job-dtl clearfix').find('span', class_ = 'srp-skills').text
  link = header.a['href']

  with open(f'posts/{index}.txt', 'w') as f:
    f.write(f"Job Title: {job_title.strip()} \n")
    f.write(f"Company Name: {company_name.strip()} \n")
    f.write(f"Years of experience: {years_experience} \n")
    f.write(f"Location: {location} \n")
    f.write(f"Skills: {skills.strip()} \n")
    f.write(f"Link: {link}")
  print(f'File saved: {index}')
