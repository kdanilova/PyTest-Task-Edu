import time

from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_presented_on_page(browser):
    browser.get(link)
    try:
        browser.find_element_by_css_selector(".btn.btn-lg.btn-primary")
    except NoSuchElementException:
        assert False, "Button not found"
    finally:
        time.sleep(3)
