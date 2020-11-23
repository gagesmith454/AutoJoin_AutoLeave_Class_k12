# imports and sources

from selenium import webdriver
import os 
import time
import pause

UserName = 'YourUserName'
Password = 'YourPassword'

# auto login    ---- Math ----

driver = webdriver.Chrome()
driver.get('https://login-learn.k12.com/#login')

time.sleep(5)

UN = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[2]/div[2]/input')
UN.send_keys(UserName)

PW = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[3]/div[2]/input')
PW.send_keys(Password)

LB = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[5]/span/button')
LB.click()

# go to calender and join class

time.sleep(7)

Calender = driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[1]/div[1]/ul/li[1]/a')
Calender.click()

time.sleep(7)

Math = driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td/a/span/span[1]')
Math.click()

pause.minutes(45)   #time in class - 45 Minute  

driver.close()      #quit class

pause.minutes(45)   #Switch

###############################################################################
 

# auto login    ---- Science ----

driver = webdriver.Chrome()
driver.get('https://login-learn.k12.com/#login')

time.sleep(5)

UN = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[2]/div[2]/input')
UN.send_keys(UserName)

PW = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[3]/div[2]/input')
PW.send_keys(Password)

LB = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[5]/span/button')
LB.click()

# go to calender and join class

time.sleep(7)

Calender = driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[1]/div[1]/ul/li[1]/a')
Calender.click()

time.sleep(7)

Science = driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[2]/td/a/span/span[1]')
Science.click()

pause.minutes(45)   #time in class - 45 Minute  

driver.close()      #quit class

pause.minutes(45)   #Switch

######################################################################################

# auto login    ---- English ----

driver = webdriver.Chrome()
driver.get('https://login-learn.k12.com/#login')

time.sleep(5)

UN = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[2]/div[2]/input')
UN.send_keys(UserName)

PW = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[3]/div[2]/input')
PW.send_keys(Password)

LB = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[5]/span/button')
LB.click()

# go to calender and join class

time.sleep(7)

Calender = driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[1]/div[1]/ul/li[1]/a')
Calender.click()

time.sleep(7)

English = driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[3]/td/a/span/span[1]')
English.click()

pause.minutes(45)   #time in class - 45 Minute  

driver.close()      #quit class

pause.minutes(45)   #switch

##################################################################################

# auto login    ---- GoogleApps ----

driver = webdriver.Chrome()
driver.get('https://login-learn.k12.com/#login')

time.sleep(5)

UN = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[2]/div[2]/input')
UN.send_keys(UserName)

PW = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[3]/div[2]/input')
PW.send_keys(Password)

LB = driver.find_element_by_xpath('/html/body/div/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div[5]/span/button')
LB.click()

# go to calender and join class

time.sleep(7)

Calender = driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[1]/div[1]/ul/li[1]/a')
Calender.click()

time.sleep(7)

GoogleApps = driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[4]/td/a/span/span[1]')
GoogleApps.click()

time.sleep(2700)   #time in class - 45 Minute  

driver.close()     #quit class

# end

##################################################################
