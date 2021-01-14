from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):
    q = 1

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def click_bucket(self):
        bucket = self.browser.find_element(By.XPATH, "//*[@id='add_to_basket_form']/button")
        bucket.click()

    def text_bucket(self):
        bucket = self.browser.find_element(By.XPATH, "//h1")
        return bucket.text

    def check_bucket(self):
        bucket = self.browser.find_element(By.XPATH, "//h1")
        assert bucket.text == self.text_bucket()




