from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_locator = (By.NAME, 'username')
        self.password_locator = (By.NAME, 'password')
        self.submit_button_locator = (By.XPATH, '//button[@type="submit"]')

    def login(self, username, password):
        self.find_element(*self.username_locator).send_keys(username)
        self.find_element(*self.password_locator).send_keys(password)
        self.find_element(*self.submit_button_locator).click()
