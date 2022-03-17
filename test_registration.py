import unittest
from selenium import webdriver


class TestReg(unittest.TestCase):

    def test_reg1(self) -> None:
        self.link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)

        self.input1 = self.browser.find_element_by_css_selector('.first_block>.form-group>.form-control.first')
        self.input1.send_keys("First Name")

        self.input2 = self.browser.find_element_by_css_selector('.first_block>.form-group>.form-control.second')
        self.input2.send_keys("Last Name")

        self.input3 = self.browser.find_element_by_css_selector('.first_block>.form-group>.form-control.third')
        self.input3.send_keys("email@example.com")

        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()

        self.message = self.browser.find_element_by_tag_name("h1").text

        self.assertEqual(self.message, "Congratulations! You have successfully registered!")

        self.browser.quit()


    def test_reg2(self) -> None:
        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)

        self.input1 = self.browser.find_element_by_css_selector('.first_block>.form-group>.form-control.first')
        self.input1.send_keys("First Name")

        self.input2 = self.browser.find_element_by_css_selector('.first_block>.form-group>.form-control.second')
        self.input2.send_keys("Last Name")

        self.input3 = self.browser.find_element_by_css_selector('.first_block>.form-group>.form-control.third')
        self.input3.send_keys("email@example.com")

        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()

        self.message = self.browser.find_element_by_tag_name("h1").text

        self.assertEqual(self.message, "Congratulations! You have successfully registered!")

        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
