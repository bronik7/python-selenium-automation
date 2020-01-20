from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')
search = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
search.clear();
search.send_keys('Lego')
sleep(2)
search.send_keys(Keys.RETURN)
assert 'Lego' in driver.find_element_by_xpath("//span[@class='a-color-state a-text-bold']").text
driver.close()