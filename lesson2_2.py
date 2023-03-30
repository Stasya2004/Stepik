from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Edge()
    browser.get(link)

    button1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)
   
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()

    button2 = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']") #Почему-то не работает последняя кнопка
    button2.click()

finally:
     
    time.sleep(15)
    browser.quit()
