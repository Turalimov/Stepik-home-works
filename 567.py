from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
sbm_btn = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
confirm = browser.switch_to.alert
confirm.accept()
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
text = browser.find_element(By.ID, 'answer').send_keys(y)
sbm_btn = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
time.sleep(5)
