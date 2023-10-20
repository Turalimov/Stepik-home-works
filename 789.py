from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),("100")))
browser.find_element(By.ID, "book").click()
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
text = browser.find_element(By.ID, 'answer').send_keys(y)
sbm_btn = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
time.sleep(5)

