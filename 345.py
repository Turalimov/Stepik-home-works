from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
text = browser.find_element(By.ID, 'answer').send_keys(y)
browser.execute_script("window.scrollBy(0, 100);")
check = browser.find_element(By.ID, 'robotCheckbox').click()
radio = browser.find_element(By.ID, 'robotsRule').click()
sbm_btn = browser.find_element(By.XPATH, '/html/body/div/form/button').click()
time.sleep(5)
