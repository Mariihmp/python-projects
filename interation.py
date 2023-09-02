from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

elemnt = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
#how to interact with elements

all_portals = driver.find_element(By.LINK_TEXT, 'Community portal')
# all_portals.click()


sending_inp =driver.find_element(By.NAME, "search").send_keys('python')
# sending_inp.send_keys(Keys.ENTER)

driver.get('https://www.google.com')
input = driver.find_element(By.NAME,'q')
                                 

input.send_keys('hello world')
google_srch = driver.find_element(By.NAME,'btnK')
google_srch.click()






