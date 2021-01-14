"""
file: covid_automation.py
author: Zeb Hollinger | zah1276@rit.edu

description: Python script that automates the covid daily
             check-ins for ATS

"""

from selenium import webdriver
import yaml
import time

# open the hidden file with the goods
conf = yaml.full_load(open("hidden.yml"))
#  vars for the ATS daily check-in
atsID = conf["rit_ats"]["id"]
atsPassword = conf["rit_ats"]["password"]

#these vars and hidden files could be duplicated to login multiple people
#for example:
#conf_dan = yaml.full_load(open("hidden_dan.yml"))
#atsID_dan = conf_dan["rit_ats"]["id"]
#atsPassword_dan = conf_dan["rit_ats"]["password"]


#consider adding these lines
chromeOptions = webdriver.ChromeOptions()
prefs = {'safebrowsing.enabled': 'false'}
chromeOptions.add_experimental_option("prefs", prefs)
#driver = webdriver.Chrome(chrome_options=chromeOptions)

#  initialize ChromeDriver
#driver = webdriver.Chrome()
# i use this because my path is fucked
driver = webdriver.Chrome(chrome_options=chromeOptions,
                          executable_path=r"C:\Windows\1- PROJECT RESOURCES (in path)\chromedriver.exe")


#  radio button strings
button1 = "MainContent_RptrAthleteForms_rblYesCHecked_1_1_1"
button2 = "MainContent_RptrAthleteForms_rblYesCHecked_2_1_2"
button3 = "MainContent_RptrAthleteForms_rblYesCHecked_3_1_3"
button4 = "MainContent_RptrAthleteForms_rblYesCHecked_4_1_4"
button5 = "MainContent_RptrAthleteForms_rblYesCHecked_5_1_5"
button6 = "MainContent_RptrAthleteForms_rblYesCHecked_6_1_6"
button7 = "MainContent_RptrAthleteForms_rblYesCHecked_7_1_7"
button8 = "MainContent_RptrAthleteForms_rblYesCHecked_8_1_8"
button9 = "MainContent_RptrAthleteForms_rblYesCHecked_9_1_9"
button10 = "MainContent_RptrAthleteForms_rblYesCHecked_10_1_10"

# bot was missing some buttons, these are the ones i added
button0 ="MainContent_RptrAthleteForms_rblYesCHecked_0_1_0"
button11 = "MainContent_RptrAthleteForms_rblYesCHecked_11_1_11"
button12 = "MainContent_RptrAthleteForms_rblYesCHecked_12_1_12"
button13 = "MainContent_RptrAthleteForms_rblYesCHecked_13_1_13"
textbox1 = "MainContent_RptrAthleteForms_txtAnswer_0"


def login_ats(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_id(submit_buttonId).click()
    try:
        driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_1_1_1")
    except:
        driver.find_element_by_id("cmdScreening").click()
        
    driver.find_element_by_id(button0).click()
    driver.find_element_by_id(textbox1).send_keys("98.6")
    driver.find_element_by_id(button1).click()
    driver.find_element_by_id(button2).click()
    driver.find_element_by_id(button3).click()
    driver.find_element_by_id(button4).click()
    driver.find_element_by_id(button5).click()
    driver.find_element_by_id(button6).click()
    driver.find_element_by_id(button7).click()
    driver.find_element_by_id(button8).click()
    driver.find_element_by_id(button9).click()
    driver.find_element_by_id("MainContent_btnNextFormPage").click()
    driver.find_element_by_id(button10).click()
    driver.find_element_by_id(button11).click()
    driver.find_element_by_id(button12).click()
    driver.find_element_by_id(button13).click()
    driver.find_element_by_id("MainContent_cmdSaveForms2").click()
    driver.get("https://www.atsusers.com/ATSAthletePhone/Default.aspx?action=logout")
    driver.close()


login_ats("https://www.atsusers.com/ATSAthletePhone/login.aspx?db=atsclarku", 
          "emailForSignIn", CheggID, "passwordForSignIn", CheggPassword, "cmdLogin")

# expand this for all users
#login_ats("https://www.atsusers.com/ATSAthletePhone/login.aspx?db=atsclarku", "txtUserName", atsID_dan, "txtPassword",
#          atsPassword_dan, "cmdLogin")
