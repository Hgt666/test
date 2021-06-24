'''#coding=utf-8
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://user.tungee.com/users/sign-in")
driver.find_element_by_xpath("//*[@id='user-login-wrapper']/div/div/div/section[2]/form/div[1]/div/div/span/span/span/span[2]/input").send_keys("17802198459")
driver.find_element_by_xpath("//*[@id='user-login-wrapper']/div/div/div/section[2]/form/div[2]/div/div/span/span/input").send_keys("Hgt_17802198459")
driver.find_element_by_xpath("//button[@class='ant-btn _2jejW ant-btn-primary']").click()
# time.sleep(1)
# url=driver.current_url
# title=driver.title
time.sleep(2)
driver.find_element_by_xpath("//*[@id='app-content']/div[1]/div[2]/div/div/div[2]/div/a[1]/div/span").click()
url=driver.current_url
title=driver.title
print(url)
print(title)

# driver.quit()'''


