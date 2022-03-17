import pytest
from selenium import webdriver
import math
import time


def answer():
    return math.log(int(time.time()))


links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1", ]


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestStepikPage:

    def test_answer(self, browser):
        for link in links:
            browser.get(link)
            textarea = browser.find_element_by_css_selector("textarea")
            textarea.send_keys(str(answer()))
            button = browser.find_element_by_css_selector(".submit-submission")
            button.click()
            message = browser.find_element_by_css_selector(".smart-hints__hint").text
            if "Correct!" not in message:
                print(message)