from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"]="none"
browser = webdriver.Chrome(desired_capabilities=caps,executable_path='/home/pavanar/chromedriver76-0-3809-126',chrome_options=chrome_options)
f = open("/home/pavanar/Desktop/stocks","r")
i = 0
for line in f:
    browser.get(line)
    browser.execute_script('''window.open("http://bing.com", "_blank");''')
    browser.switch_to_window(browser.window_handles[i+1])
    i += 1
time.sleep(120)
mainurl = 'https://www.finance.yahoo.com'
browser.get(mainurl)
print ('its open')