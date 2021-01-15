from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    #def go_to_login_page(self):
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

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_login(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)