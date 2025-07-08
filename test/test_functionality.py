

import pytest
from test.utils import Utils



@pytest.mark.usefixtures("setup")
class TestFunctionality:


    @pytest.mark.add_candidate
    @pytest.mark.parametrize("candidate", [Utils.generate_fake_candidate_data()])
    def test_add_new_candidate(self, candidate):
        recruitment_page = self.login_page.navigate_to_recruitment_page()
        assert recruitment_page.validate_recruitment_page(), "Recruitment page validation failed."
        assert recruitment_page.click_add_recruitment_button(), "Add Recruitment button click failed."
        recruitment_page.select_dropdown_option("Senior QA Lead")
        recruitment_page.select_email_id(candidate['email'])
        recruitment_page.select_contact_number(candidate['contact'])
        recruitment_page.add_new_candidate(
            first_name=candidate['firstname'],
            middle_name=candidate['middlename'],
            last_name= candidate['lastname'])
        assert recruitment_page.verify_tooltip_message()
        Utils.get_logger().info("New candidate added successfully.")

    @pytest.mark.parametrize("candidate", [Utils.generate_fake_candidate_data()])
    def test_shortlist_candidate(self, candidate):
        recruitment_page = self.login_page.navigate_to_recruitment_page()
        assert recruitment_page.validate_recruitment_page(), "Recruitment page validation failed."
        self.test_add_new_candidate(candidate)
        assert recruitment_page.verify_application_status()== "Status: Application Initiated"
        assert recruitment_page.click_shortlist_button(), "Shortlist button click failed."
        assert recruitment_page.save_shortlisted_candidate()
        Utils.get_logger().info("Shortlisted candidate successfully.")
