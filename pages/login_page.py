from functools import wraps

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

import time

from pages.recruitment_page import RecruitmentPage
from test.utils import Utils


class LoginPage:
    user_name = (By.NAME, "username")
    pass_word = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    validate_success_login = (By.XPATH, "//h6[text()='Dashboard']")
    recruitment_page = (By.XPATH, "//span[text()='Recruitment']")
    leave_page = (By.XPATH, "//span[text()='Leave']")



    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.utils = Utils(self.driver)


    def login(self, username: str, password: str):
        self.utils.visibility_of_element(self.user_name).send_keys(username)
        self.utils.visibility_of_element(self.pass_word).send_keys(password)
        self.utils.element_clickable(self.login_button).click()

    def validate_successful_login(self):
        try:
            return self.utils.is_element_displayed(self.validate_success_login)
        except StaleElementReferenceException:
            return False
        except Exception as e:
            print(f"An error occurred while validating successful login: {e}")
            return False

    def navigate_to_recruitment_page(self):
        self.utils.element_clickable(self.recruitment_page).click()
        return RecruitmentPage(self.driver)







