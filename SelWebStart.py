from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"]="none"
browser = webdriver.Chrome(desired_capabilities=caps,executable_path='/home/pavanar/chromedriver76-0-3809-126',chrome_options=chrome_options)
browser.get('https://www.gmail.com/')
main_window = browser.current_window_handle
browser.maximize_window()
time.sleep(5)
inEle = browser.find_element_by_id("identifierId")
inEle.send_keys("pavanarora7590")
inEle = browser.find_element_by_id("identifierNext").click()
time.sleep(2)
inEle = browser.find_element_by_name("password")
inEle.send_keys("@PeterPabl0")
inEle = browser.find_element_by_id("passwordNext").click()
time.sleep(20)
inEle = browser.find_element_by_
inEle = browser.find_element_by_id("gb_71").click()
