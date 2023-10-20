from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
btn = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
text = browser.find_element(By.ID, 'answer').send_keys(y)
sbm_btn = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
time.sleep(5)
