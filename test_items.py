import pytest
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    # Uncomment next line to check the page language
    #time.sleep(30)
    items = browser.find_elements_by_css_selector("form#add_to_basket_form>button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(items) > 0 , "'Add to basket' button wasn't found"
