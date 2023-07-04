from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_find_btn_add_to_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        button_on_page = True
    except NoSuchElementException:
        button_on_page = False
    assert button_on_page, "No add_to_basket button on page"

