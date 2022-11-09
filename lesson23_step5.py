from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    number = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = number.text
    y = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, " #answer")
    input_answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()