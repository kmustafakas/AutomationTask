import pytest
from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup", "website_setup")
class TestContactUsEmailInput:

    def test_contact_us_email_input(self, config):
        # vars for the test
        expected_email_validation_message = 'The e-mail address entered is invalid.'
        expected_overall_validation_message = 'One or more fields have an error. Please check and try again.'
        emails_file_name = 'wrong_formatted_emails.txt'
        name = "Automation Test name"
        mobile_number = "05912312345"
        subject = "Automation Test Subject"
        message = "Automation Test Message"
        home_page = HomePage(self.driver)

        print("step1 : to open contact form")
        home_page.open_contact_us_page()

        print("step2 :fill all inputs except email")
        home_page.fill_all_inputs_except_email(name, mobile_number, subject, message)

        print("step3: open wrong formatted emails file")
        file1 = open(emails_file_name, 'r')
        lines = file1.readlines()

        count = 0
        print("step4: test five wrong formatted emails from file and get validation messages")
        for line in lines:
            count += 1
            email = line.strip()
            home_page.contact_us_fill_email(email)
            home_page.submit_contact_us_form()
            error_message = ''
            error_message = home_page.get_email_validation_error_text()
            if error_message not in expected_email_validation_message:
                print("validation message for email is not as expected")
                assert False
            error_message = ''
            error_message = home_page.get_overall_validation_error_text()
            if error_message not in expected_overall_validation_message:
                print("validation message for overall is not as expected")
                assert False
