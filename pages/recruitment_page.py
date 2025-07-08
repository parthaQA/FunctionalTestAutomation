import time

from selenium.webdriver.common.by import By
from test.utils import Utils


class RecruitmentPage:
    validate_recruitement_page = (By.XPATH, "//h6[text()='Recruitment']")
    add_recruitment_button = (By.XPATH, "//button[normalize-space()='Add']")
    add_candidate_label = (By.XPATH,"//h6[text()='Add Candidate']")
    first_name = (By.NAME, "firstName")
    middle_name = (By.NAME, "middleName")
    last_name = (By.NAME, "lastName")
    email_id = (By.XPATH, "//*[text()='Email']")
    contact_number = (By.XPATH, "(//*[text()='Contact Number']/following::input[@placeholder='Type here'])")
    select_dropdown = (By.XPATH, "//div[text()='-- Select --']")
    application_date = (By.XPATH, "//input[@placeholder='yyyy-dd-mm']")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")
    verify_tooltip = (By.XPATH, "//*[text()='Successfully Saved']")
    save_tooltip = (By.XPATH, "//*[text()='Successfully Updated']")
    shortlist_button = (By.XPATH, "//button[normalize-space()='Shortlist']")

    def __init__(self, driver):
        self.driver = driver
        self.utils = Utils(self.driver)


    def validate_recruitment_page(self):
        try:
            return self.utils.is_element_displayed(self.validate_recruitement_page)
        except Exception as e:
            Utils.get_logger().info(f"An error occurred while validating recruitment page: {e}")
            return False

    def click_add_recruitment_button(self):
        self.utils.element_clickable(self.add_recruitment_button).click()
        return self.utils.is_element_displayed(self.add_candidate_label)


    def select_dropdown_option(self, option_text):
        dropdown = self.utils.visibility_of_element(self.select_dropdown)
        dropdown.click()
        try:
            select_option = self.utils.presence_of_element((By.XPATH, f"//*[text()='{option_text}']"))
            select_option.click()
        except Exception as e:
            Utils.get_logger().info(f"An error occurred while selecting dropdown option: {e}")


    def select_email_id(self, email):
        el = self.utils.visibility_of_element(self.email_id)
        select_email = el.find_element(By.XPATH, "//input[@placeholder='Type here']")
        select_email.send_keys(email)

    def select_contact_number(self, contact_number):
        el = self.utils.visibility_of_element(self.contact_number)
        # select_contact = el.find_element(By.XPATH, "//input[@placeholder='Type here']")
        el.send_keys(contact_number)


    def add_new_candidate(self, first_name, middle_name, last_name):
        self.utils.visibility_of_element(self.first_name).send_keys(first_name)
        self.utils.visibility_of_element(self.middle_name).send_keys(middle_name)
        self.utils.visibility_of_element(self.last_name).send_keys(last_name)
        self.utils.element_clickable(self.save_button).click()

    def verify_tooltip_message(self):
        try:
            return self.utils.is_element_displayed(self.verify_tooltip)
        except Exception as e:
            Utils.get_logger().info(f"An error occurred while verifying tooltip message: {e}")
            return False

    def verify_save_tooltip_message(self):
        try:
            return self.utils.is_element_displayed(self.save_tooltip)
        except Exception as e:
            Utils.get_logger().info(f"An error occurred while verifying save tooltip message: {e}")
            return None

    def verify_application_status(self):
        try:
            application_status = self.utils.presence_of_element((By.CSS_SELECTOR, ".orangehrm-recruitment-status p"))
            return application_status.text if application_status else None
        except Exception as e:
            Utils.get_logger().info(f"An error occurred while verifying application status: {e}")
            return None

    def click_shortlist_button(self):
        try:
            self.utils.is_element_displayed(self.shortlist_button)
            self.utils.element_clickable(self.shortlist_button).click()
            return True
        except Exception as e:
            Utils.get_logger().info(f"An error occurred while clicking the shortlist button: {e}")
            return False


    def save_shortlisted_candidate(self):
        try:
            time.sleep(5)
            self.utils.element_clickable(self.save_button).click()
            return self.verify_save_tooltip_message()
        except Exception as e:
            Utils.get_logger().info(f"An error occurred while saving the shortlisted candidate: {e}")
            return False


