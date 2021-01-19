from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #error handling
from selenium.common.exceptions import TimeoutException #timeout if not found
import os
import re
import time
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
dates = []
sdate = date(2020, 1, 1)   # start date
edate = date(2020, 1, 31)   # end date

delta = edate - sdate       # as timedelta

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)

    date_time = day.strftime("%d/%m/%Y")
    dates.append(date_time)
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = r"C:\chromedriver.exe"

y='https://app.cpcbccr.com/AQI_India/'
driver = webdriver.Chrome('C:\\Users\\Saurav Telge\\chromedriver.exe')
driver.get(y)
driver.set_window_size(1920, 1080)

for i in dates:

    wait = WebDriverWait(driver, 200)
    datee= driver.find_element_by_xpath("//*[@id='date']/input")
    driver.execute_script("arguments[0].value = ''", datee)
    datee.send_keys(f"{i}");
    datee.send_keys(Keys.RETURN)
    WebDriverWait(driver, 200)
    driver.find_element_by_id('downloadExcel').click()
