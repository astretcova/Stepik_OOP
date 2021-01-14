from .page.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_should_see_login_link(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_should_see_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()