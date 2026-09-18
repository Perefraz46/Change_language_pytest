from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_auth_button_is_displayed(browser):
    browser.get(link)
    auth_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "btn-add-to-basket")))


    assert auth_button.is_displayed(), "Onboarding action button isn't displayed"
