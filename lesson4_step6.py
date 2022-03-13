from selenium import webdriver
from selenium.common import exceptions


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/cats.html")

    button = browser.find_element_by_id("button")

    if button:
        assert "successful"

except exceptions.NoSuchElementException:
    print("This element is not exist.")

except exceptions.StaleElementReferenceException:
    print("The element stale")

except exceptions.ElementNotVisibleException:
    print("The element is not visible.")


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций
    browser.quit()

