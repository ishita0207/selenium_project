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
# print(state_name)
for j in state_name:
    print(j)
    v = driver.find_element(By.LINK_TEXT,j)
    url = str(v.get_attribute("href"))
    driver.get(url)
    print(j+"Site Opened")
    detail_info = driver.find_elements(By.CLASS_NAME,"wb-stl-special")
    Type=[]
    Phone_Number=[]
    all_info = []
    for k in detail_info:
        all_info = all_info.append(k.text)

    for i in detail_info:
        i = str(i.text)
        if i == "© 2015 - 2022 Indianhelpline.com":
            break
    print("Main Site Opening")
    driver.get(main_url)
        # try:
        #     print(i.text)
        # except NoSuchElementException as exception:
        #     exit
# writer.writerow(value)
# print("came out of loop")
# data = pd.read_csv("prog2.csv")
# data = pd.DataFrame(data)
# for i in range(1):
#         i = str(data.loc[i,'StateName'])
#         v = driver.find_element(By.LINK_TEXT,i)
#         url = str(v.get_attribute("href"))
#         optn = webdriver.ChromeOptions()
#         optn.add_argument('headless')
#         driver = webdriver.Chrome("C:/Users/Ashish Goyal/Downloads/chromedriver_win32/chromedriver.exe",options=optn)
#         driver.get(url)
#         detail_info = driver.find_element(By.CLASS_NAME,"wb-stl-special")
#         print(detail_info.size)