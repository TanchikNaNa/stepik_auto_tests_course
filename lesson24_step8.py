from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math
import time 
from selenium.webdriver.support import expected_conditions as EC




def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '$100'))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    number = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = number.text
    y = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, " #answer")
    input_answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()




