'''
Created on 23-Aug-2019

@author: racha
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver=webdriver.Chrome(executable_path="C:\Program Files\Chrome driver\chromedriver.exe")

driver.get("https://www.happyeasygo.com/flight/")

print(driver.title)

print(driver.current_url)

driver.maximize_window()

driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click()

time.sleep(5)

PNo_ele=driver.find_element_by_name("phoneNo")

print(PNo_ele.is_displayed()) # Return the True or False element or field 

PNo_ele.send_keys("7353249488")

time.sleep(5)

Pwd_ele=driver.find_element_by_name("password")

print(Pwd_ele.is_enabled())

Pwd_ele.send_keys("rachu@22")

driver.find_element_by_id("login-btn").click()

time.sleep(5)

Roundtrip_radio = driver.find_element_by_id("Roundtrip")

print(Roundtrip_radio.is_selected())

time.sleep(5)

Oneway_radio=driver.find_element_by_id("oneway")
print(Oneway_radio.is_selected())

time.sleep(5)

driver.get("https://www.cricbuzz.com/")
print(driver.title)
print(driver.current_url)

time.sleep(5)

driver.back()

print(driver.title)
print(driver.current_url)

time.sleep(5)

driver.forward()

time.sleep(5)

driver.back()

time.sleep(5)

driver.close()