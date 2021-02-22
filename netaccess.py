#!/usr/bin/env python3

import selenium
import selenium.webdriver
from selenium.webdriver.firefox.options import Options
import time

#--------------------------------firefox---------------------------------
firefox_options = Options()
firefox_options.add_argument("--headless") #Comment this to see the process
browser = selenium.webdriver.Firefox(options=firefox_options)
#browser = selenium.webdriver.Firefox()

#--------------------------------chrome---------------------------------
#(Uncomment below lines and comment above lines if you want to use chrome)
 
#chrome_options = Options()
#chrome_options.add_argument("--headless") #Remove this to see the process
#browser = selenium.webdriver.Chrome(options=chrome_options)
#browser = selenium.webdriver.Chrome()


website = "https://netaccess.iitm.ac.in"
user = "Roll Number" #Replace with your roll number
pwd = "Password" #Replace with your password

htmlElementUser = "userLogin"
htmlElementPwd = "userPassword"
htmlElementSubmit = "submit"
htmlIdDuration = "radios-1"
htmlElementApprove = "approveBtn"	

try:
	browser.get((website))
	userElement = browser.find_element_by_name(htmlElementUser)
	userElement.send_keys(user)		
	pwdElement  = browser.find_element_by_name(htmlElementPwd)
	pwdElement.send_keys(pwd)
	signin  = browser.find_element_by_name(htmlElementSubmit)
	signin.click()
 
	browser.get((website + "/account/approve"))
	durationElement = browser.find_element_by_id(htmlIdDuration)
	durationElement.click()
	approve  = browser.find_element_by_name(htmlElementApprove)
	approve.click()
	
	print("Netaccess Successful!")
	
	print("Closing program...")
 
	#time.sleep(1)
	browser.quit()

 
except Exception:
	print("Error!!!")
	browser.quit()




