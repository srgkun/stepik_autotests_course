from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:

    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button2 = browser.find_element_by_id("solve")
    button2.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()