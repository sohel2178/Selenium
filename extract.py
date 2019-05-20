from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from mail_extract import get_url_list
import time
import os
from random import randrange as r


# WebDriver Setting
user_name = 'sohel.ahmed2178@gmail.com'
pwd='Sa01835645622!'
path = r"C:\Users\sohel\Desktop\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(path,chrome_options=chrome_options)

def login(filename):
    driver.get("https://www.linkedin.com/uas/login")

    time.sleep(2)

    email_field = driver.find_element_by_id("session_key-login")
    email_field.send_keys(user_name)
    time.sleep(1)

    pass_field = driver.find_element_by_id("session_password-login")
    pass_field.send_keys(pwd)
    time.sleep(1)

    driver.find_element_by_xpath("""//*[@id="btn-primary"]""").click()
    time.sleep(3)

    start_data_crawl(filename)



def crawl_data(url):
    user={}
    driver.get(url)
    time.sleep(r(5,16))
    user['url']=url
    name=""
    current_position=""
    location=""

    try:
        name = driver.find_element_by_xpath("""/html/body/div[5]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/div[1]/h1""").text.encode("ascii","ignore").decode('utf-8')
    except:
        try:
            name = driver.find_element_by_xpath("""/html/body/div[4]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/div[1]/h1""").text.encode("ascii","ignore").decode('utf-8')
        except:
            pass

    try:
        current_position = driver.find_element_by_xpath("""/html/body/div[5]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/h2""").text.encode("ascii","ignore").decode('utf-8')
    except:
        try:
            current_position = driver.find_element_by_xpath("""/html/body/div[4]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/h2""").text.encode("ascii","ignore").decode('utf-8')
        except:
            pass

    try:
        location = driver.find_element_by_xpath("""/html/body/div[5]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/h3""").text.encode("ascii","ignore").decode('utf-8')
    except:
        try:
            location = driver.find_element_by_xpath("""/html/body/div[4]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/h3""").text.encode("ascii","ignore").decode('utf-8')
        except:
            pass

    user['name'] = name
    user['current_position'] = current_position
    user['location'] = location

    return user





def start_data_crawl(filename):
    data_list=[]
    url_list = get_url_list(filename)

    new_list = url_list[:3]

    for url in new_list:
        # print(url)
        data = crawl_data(url)
        data_list.append(data)
        print(data)

    name = os.path.splitext(filename)[0]

    df = pd.DataFrame(data_list)

    df.to_csv(name+'-info.csv',index=False)

        








if __name__ == "__main__":
    
    login('./output/data1.csv')
    






