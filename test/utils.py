from datetime import datetime
import inspect
import logging
from pathlib import Path
from faker.proxy import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver



class Utils:
    ROOT_DIR = Path(__file__).parent.parent

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)



    def element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def presence_of_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def visibility_of_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def switch_to_window(self, window_index: int):
        windows = self.driver.window_handles
        if window_index < len(windows):
            self.driver.switch_to.window(windows[window_index])

    def is_element_displayed(self, locator) -> bool:
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.is_displayed()

    def is_element_enabled(self, locator) -> bool:
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.is_enabled()

    def validate_page_title(self):
        actual_title = self.driver.title
        return self.wait.until(EC.title_is(actual_title))

    def validate_text(self, locator) -> str:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @staticmethod
    def generate_fake_candidate_data():
        faker = Faker()
        candidate_data = {
            "firstname": faker.first_name(),
            "middlename": faker.first_name(),
            "lastname": faker.last_name(),
            "email": faker.email(),
            "contact": faker.basic_phone_number()
        }
        return candidate_data

    @staticmethod
    def get_logger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(Utils.ROOT_DIR / 'log' / 'logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.addHandler(fileHandler)
        return logger