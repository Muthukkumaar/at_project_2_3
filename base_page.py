from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            return element
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
