##########################################################
#     An automated Facebook message sender in Python     #
#    that send messages to people from a csv database    #
#                  Author : JustOssa :)                  #
##########################################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import csv
import configparser
import time
import os

## Get user data ##
configParser = configparser.RawConfigParser()                   ## ConfigParser for reading Config File
configFilePath = r'fb.conf'                                     ## Source config file
configParser.read(configFilePath)                               ## Read Config file
usr = configParser.get('Creds', 'username')                     ## Read Username
pwd = configParser.get('Creds', 'password')                     ## Read Password
a = s = 0                                                       ## All/Sent counter
cooldown = 10                                                   ## cooldown
ids = os.getcwd()+'/ids.csv'                                    ## ids csv file
message = '''Test message'''                                    ## the message to send
image = 'MyPhoto.jpg'                                           ## the image to send

while True:
   cool = int(input('Number of messages to cool down ('+str(cooldown)+'s) after : '))
   if cool==0:
      print("It can't be 0 ¯\\_(ツ)_/¯")
      continue
   else: break


## Login ##

chrome_options = Options()
chrome_options.add_argument("--app=https://mbasic.facebook.com")                      ## Load chrome without toolbar
chrome_options.add_argument("--window-size=600,618")                                  ## Set Browser window size

driver = webdriver.Chrome(options=chrome_options)                                     ## Initializing Browser
driver.find_element_by_id('m_login_email').send_keys(usr)                             ## Fill Username
password_box = driver.find_element_by_name('pass').send_keys(pwd)                     ## Fill Password
login_btn = driver.find_element_by_name('login').submit()                             ## Click Login
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "root")))      ## Wait main page to load

## Handling wrong credentials
if "mbasic.facebook.com/login" in driver.current_url and "save-device" not in driver.current_url:
   print("incorrect password")
   exit()

with open(ids, encoding="utf-8", newline='') as csvfile:                                           ## Read the CSV

   reader = csv.DictReader(csvfile)    
   for row in reader:
      a+=1
      name = row['Name']                                                                           ## Get Name column from csv
      id = row['Uid']                                                                              ## Get Uid column from csv
      profileurl = "https://mbasic.facebook.com/messages/compose/?ids={0}/".format(id)             ## Set profile message URL

      # Sending message
      driver.get(profileurl)                                                                       ## Calling Profile message URL
      WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "root")))             ## Wait messaging page to load (slowing a bit)
      driver.find_element_by_name('body').send_keys(message)                                       ## Load message
      send_btn = driver.find_element_by_name("Send").submit()                                      ## Send message

      """
      # Sending image "MyPhoto.jpg"
      driver.get(profileurl)                                                                       ## Calling Profile message URL
      WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "root")))             ## Wait messaging page to load (slowing a bit)
      driver.find_element_by_name('file1').send_keys(os.getcwd()+"/"+image)                        ## Load image
      driver.find_element_by_xpath("//input[@value='Send Photos']").submit()                       ## Send image
      """

      try:
         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "messageGroup")))  ## Wait messages page to load (slowing a bit)
      except:   
         print("Failed to message : ", name)  ## Print fail msg if not loaded
      else:
         print("Message sent to : ", name)    ## Print success msg if loaded
         s+=1
      
      ## Cooling down ##
      if a % cool == 0:
         print("Cooling down for 10s ..")
         time.sleep(10)                      ## Time to wait (in seconds)

print("\nTotal:",s,"/", a, "Sent.")
input("\nPress Enter to exit...")
driver.quit()