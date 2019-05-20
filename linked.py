import argparse,os,time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from mail_extract import get_linked_in_profiles,is_valid_url

import pandas as pd

user = 'sohel.ahmed2178@gmail.com'
pwd='Sa01835645622!'

path = r"C:\Users\sohel\Desktop\chromedriver.exe"

prof_list=[]


with open('data.txt', 'r') as myfile:



    lines = myfile.readlines()
    profiles = get_linked_in_profiles(lines)

    my_driver = webdriver.Chrome(path)
    my_driver.get("https://www.linkedin.com/uas/login")

    time.sleep(2)

    email_field = my_driver.find_element_by_id("session_key-login")
    email_field.send_keys(user)
    time.sleep(1)

    pass_field = my_driver.find_element_by_id("session_password-login")
    pass_field.send_keys(pwd)
    time.sleep(1)

    my_driver.find_element_by_xpath("""//*[@id="btn-primary"]""").click()

    time.sleep(3)

    test_profiles=profiles[:10]

    for prof in test_profiles:
        print(prof)

        user ={}
        my_driver.get(prof)

        time.sleep(5)

        name=""
        current_position=""
        location=""

        try:
            name = my_driver.find_element_by_xpath("""/html/body/div[5]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/div[1]/h1""").text
        except:
            try:
                name = my_driver.find_element_by_xpath("""/html/body/div[4]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/div[1]/h1""").text
            except:
                pass

        try:
            current_position = my_driver.find_element_by_xpath("""/html/body/div[5]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/h2""").text
        except:
            try:
                current_position = my_driver.find_element_by_xpath("""/html/body/div[4]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/h2""").text
            except:
                pass

        try:
            location = my_driver.find_element_by_xpath("""/html/body/div[5]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/h3""").text
        except:
            try:
                location = my_driver.find_element_by_xpath("""/html/body/div[4]/div[5]/div[2]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/h3""").text
            except:
                pass

        user['name'] = name
        user['current_position'] = current_position
        user['location'] = location

        print(name,location,current_position)

        prof_list.append(user)

        time.sleep(2)

    
    # for x in prof_list:
    #     print(x)

    my_driver.close()

    df = pd.DataFrame(prof_list)

    df.to_csv('output.csv', index=False)








# print(name)
# print(current_position)
# print(location)

