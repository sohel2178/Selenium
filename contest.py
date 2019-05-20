from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import signal
import time

# WebDriver Setting
user_name = 'sohel.ahmed2178@gmail.com'
pwd='Sa01835645622!'
path = r"C:\Users\sohel\Desktop\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(path)


url = 'http://www.cmfchile.cl/portal/principal/605/w3-propertyvalue-18490.html'

driver.get(url)
time.sleep(1)



def hover(browser, xpath):
    element_to_hover_over = browser.find_element_by_xpath(xpath)
    hover = ActionChains(browser).move_to_element(element_to_hover_over)
    hover.perform()

xpath = '//*[@id="nav"]/div/ul/li[3]/a'

hover(driver,xpath)

xpath = '//*[@id="nav"]/div/ul/li[3]/ul/li/div[1]/ul/li[1]/a'

time.sleep(1)

driver.find_element_by_xpath(xpath).click()


if __name__ == "__main__":
    print("Hello")