from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("http://suninjuly.github.io/get_attribute.html")
value1 = browser.find_element(By.ID, "treasure")
x = value1.get_attribute('valuex')
y = calc(x)
text = browser.find_element(By.ID, 'answer').send_keys(y)
check = browser.find_element(By.ID, 'robotCheckbox').click()
radio = browser.find_element(By.ID, 'robotsRule').click()
sbm_btn = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button').click()
time.sleep(10)
