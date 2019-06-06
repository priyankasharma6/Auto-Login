from selenium import webdriver
import unittest
import time

#input username and password

usernameStr = 'username'
passwordStr = 'password'

#reaching the website

driver = webdriver.Chrome(executable_path = r'C:\Users\pooja\AppData\Local\Programs\Python\Python37\Scripts\chromedriver.exe');
driver.get(('https://my.fullerton.edu/'))

# fill in username element and hit the next button

username = driver.find_element_by_id('username')
username.send_keys(usernameStr)


#entering the password

password = driver.find_element_by_id('password')
password.send_keys(passwordStr)
submit = driver.find_element_by_class_name("LoginButton").click()






