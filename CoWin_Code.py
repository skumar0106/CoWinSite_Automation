###################################################
# Code For Cowin Slot Scheduling
# Parameters :: 
# 1) Name of the Registered Candiate as displayed in the COwin Site
# 2) Phone Number 
# 3) Centers : List all the Desirable Centers
###################################################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Parameters
import json
givenJSONObject = "parameters.json"

with open(givenJSONObject) as jsonFile:
    jobParameters = json.load(jsonFile)
jsonObjects = [key for key in jobParameters]

jsonObjects
for i in jsonObjects:
    jobProperties = jobParameters.get(i)
    Mob_no = jobProperties.get("MobileNumber")
    NameOFRegisteredCandidate = jobProperties.get("NameOfCandidate")
    stateName = jobProperties.get("StateName")
    districtName = jobProperties.get("DistrictName")
    centers = jobProperties.get("Centers")

# Code

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver_path = './chromedriver_linux64 _89/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://selfregistration.cowin.gov.in/")
enterMobNo = driver.find_element_by_xpath('//input[@formcontrolname="mobile_number"]')
enterMobNo.clear()
enterMobNo.send_keys(Mob_no)
time.sleep(2)
enterMobNo.submit()

getOTP_btn = driver.find_element_by_xpath("//ion-button[@type='button']")
getOTP_btn.click()

print("Enter The OTP recieved in 25 seconds")
time.sleep(20)

verifyAndProceed_btn = driver.find_element_by_xpath("//ion-button[@type='button']")
verifyAndProceed_btn.click()
print("OTP Entered and button Clicked")
time.sleep(4)

scheduleApt_loc = "//h3[contains(text(),'{}')]/ancestor::ion-grid[@class='cardblockcls md hydrated']//span[contains(text(),'Schedule')]".format(
    NameOFRegisteredCandidate)
driver.execute_script("arguments[0].click();",
                      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, scheduleApt_loc))))

sch_now_loc = "//ion-button[contains(text(),'Schedule Now')]"
driver.execute_script("arguments[0].click();",
                      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, sch_now_loc))))

# Toggle Btn
searchByDistrict = driver.find_element_by_xpath("//div[@data-checked='Search By District']")
searchByDistrict.click()

# State
drp_state = "//div[@class='mat-select-arrow-wrapper ng-tns-c84-4']"
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, drp_state))).click()

state_loc = "//span[contains(text(),'{}')]".format(stateName)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, state_loc))).click()

# District
time.sleep(2)
drp_dist = "//div[@class='mat-select-arrow-wrapper ng-tns-c84-6']"
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, drp_dist))).click()

dist_loc = "//span[contains(text(),'{}')]".format(districtName)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, dist_loc))).click()

# print("Click on Search")
search_button = driver.find_element_by_xpath("//ion-col[@class='ion-text-start col-space-mobile md hydrated']")
search_button.click()
driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()

# print("Click on Search")
search_button = driver.find_element_by_xpath("//ion-col[@class='ion-text-start col-space-mobile md hydrated']")
search_button.click()

T = 1
while T == 1:
    for i in centers:
        print("Searching for ::::: ", i)
        start = time.time()
        slot_var = "//h5[contains(text(),'{}')]/ancestor::div[@class='mat-list-text']//a".format(i)
        event = driver.find_elements_by_xpath(slot_var)
        if len(event) == 0:
            print("Specified Center : {} not available on the page ".format(i))
            end = time.time()
            timeTaken = end - start
            print("Not available Center {0} Loop completed in {1}".format(i, timeTaken))
        else:
            values = []
            for items in event: values.append(items.text)
            num_val = [s for s in values if s.isdigit()]
            if len(num_val) == 0:
                print("No Slots Available for center {} ::".format(i))
                print("Clicking on Search Button Again")
                time.sleep(1)
                search_button = driver.find_element_by_xpath(
                    "//ion-col[@class='ion-text-start col-space-mobile md hydrated']")
                search_button.click()
                driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()
                time.sleep(1)
                end = time.time()
                timeTaken = end - start
                print("Loop completed for {0} in {1}".format(i, timeTaken))
            else:
                for j in num_val:
                    available_slot = slot_var + "[contains(text(),'{}')]".format(j)
                    print(available_slot)
                    driver.find_element_by_xpath(available_slot).click()
                    time_loc = "//ion-button[contains(text(),'03:00PM-06:00PM')]"
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, time_loc))).click()
                    time.sleep(8)
                    driver.find_element_by_xpath("//ion-button[@type='submit']").click()
        print('---------------------------------------')
