from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://vaisible.monday.com/users/sign_in")
driver.find_element_by_id("user_email").send_keys("timofii.sorokin@vaisible.com")
driver.find_element_by_id("user_password").send_keys("XXXXXXXXXXXXXX")
driver.find_element_by_class_name("ladda-label").click()
driver.get("https://vaisible.monday.com/admin/my-team/my-team")
for users in driver.find_elements_by_id("users"):
    print(users.text)
driver.close()
