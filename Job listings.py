from selenium import webdriver
from bs4 import BeautifulSoup

chrome_path = r"D:\WebDrivers\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)  
driver.get(r"https://www.indeed.co.in/jobs?q=python,data+science,machine+learning&jt=new_grad")

res = driver.execute_script("return document.documentElement.outerHTML")
#driver.quit()

soup = BeautifulSoup(res,"html.parser")

results = soup.find(id="resultsCol")
jobs = results.find_all("div", class_="jobsearch-SerpJobCard")

#print(len(jobs))

for job in jobs:
    title = job.find("h2", class_="title")
    company = job.find("span", class_="company")
    location = job.find("div", class_="location")
    if location == None:
        location=job.find("span", class_="location")
    
    if None in (title, company, location):
        continue

    link = job.find("a")["href"]
    


    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())

    salary = job.find("span", class_="salaryText")
    if salary != None:
        print(salary.text.strip())

    summary = job.find("div", class_="summary")
    if summary != None:
        print("\n"+summary.text.strip())


    print(f"\nApply here: indeed.com{link}\n\n")
    


driver.quit()
    

