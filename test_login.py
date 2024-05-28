import pytest
from selenium import webdriver
from login_page import LoginPage
from main_menu_page import MainMenuPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login('Admin', 'admin123')

def test_verify_main_menu(driver):
    main_menu_page = MainMenuPage(driver)
    main_menu_page.verify_menu_options()
