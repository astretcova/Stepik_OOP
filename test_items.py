import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_can_add_to_basket(browser):
    browser.get(link)
    time.sleep(3)
    buttons = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(buttons) == 1
