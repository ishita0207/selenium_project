from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

optn = webdriver.ChromeOptions()
optn.add_argument('headless')
driver = webdriver.Chrome("C:/Users/Ashish Goyal/Downloads/chromedriver_win32/chromedriver.exe",options=optn)
main_url = "https://indianhelpline.com/"
driver.get(main_url)
v = driver.find_elements(By.ID,'wb_element_instance1163')
for i in v:
    state_name = str(i.text)
state_name = state_name.split('\n')
header = ['StateName', 'Type', 'Phone Number']
f = open('C:/Users/Ashish Goyal/Desktop/devOps_challenges/prog2.csv', 'w')
writer = csv.writer(f)
writer.writerow(header)
for j in state_name:
    v = driver.find_element(By.LINK_TEXT,j)
    url = str(v.get_attribute("href"))
    driver.get(url)
    detail_info = driver.find_elements(By.CLASS_NAME,"wb-stl-special")
    Name_Type=[]
    Phone_Number=[]
    all_info = []
    count = 0
    for k in detail_info:
        k = str(k.text)
        all_info.insert(count,k)
        count = count +1
    first_it = 0
    second_it = 1
    print(all_info)
    for m in range(len(all_info)-1):
        if(first_it <= len(all_info)-1 and second_it <= len(all_info)-1):
            Name_Type.append(all_info[first_it])
            Phone_Number.append(all_info[second_it])
            first_it+=2
            second_it+=2
        else:
            exit
    print(Name_Type)
    print(Phone_Number)
    for l in range(len(Name_Type)):
        if(Name_Type[l] == "© 2015 - 2022 Indianhelpline.com"):
            exit
        else:
            writer.writerow([j,Name_Type[l],Phone_Number[l]])
    driver.get(main_url)
    print("************************NEW--WEBISTE--STARTED*************************")
# req = requests.get("C:/Users/Ashish Goyal/Desktop/devOps_challenges/prog2.csv")
# url_content = req.content
# csv_file = open('download.csv','wb')
# csv_file.write(url_content)
# csv_file.close()