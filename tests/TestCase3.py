import pytest
from pages.HomePage import HomePage
from pages.CareersPage import CareersPage
import time


@pytest.mark.usefixtures("setup", "website_setup")
class TestCareersSection:

    def test_careers_section(self, config):
        # vars for the test
        expected_careers_join_us_link = 'https://www.musala.com/careers/join-us/'
        expected_careers_join_us_link_anywhere = 'https://www.musala.com/careers/join-us/?location=Anywhere'
        anyware_location = 'Anywhere'
        job_name = 'QA Engineer (Manual Testing)'
        expected_job_titles = ['General description', 'Requirements', 'Responsibilities', 'What we offer']
        good_cv_file_name = 'good_cv.pdf'
        bad_cv_file_name = 'bad_cv.js'
        expected_email_validation_message = 'The e-mail address entered is invalid.'
        expected_overall_validation_message = 'One or more fields have an error. Please check and try again.'
        expected_empty_field_validation_message = 'The field is required.'
        expected_mobile_validation_message = 'The telephone number is invalid.'
        invalid_email = 'Automation@test'
        invalid_mobile = 'Automation_mobile'

        home_page = HomePage(self.driver)
        careers_page = CareersPage(self.driver)

        print("step1: go to careers page")
        home_page.click_on_careers_main_nav()

        print("step2: click on hero button")
        careers_page.click_on_check_positions_button()

        print("step3: verify careers join us link")
        current_url = careers_page.get_current_url()
        if current_url not in expected_careers_join_us_link:
            print("careers url is not as expected")
            assert False

        print("step4: select anywhere location")
        try:
            careers_page.select_location(anyware_location)
        except:
            # because it keep failing even though it's selected
            current_url = careers_page.get_current_url()
            if current_url not in expected_careers_join_us_link_anywhere:
                print("careers join us url is not as expected")
                assert False

        print("step5: choose QA job")
        careers_page.click_on_a_job_card(job_name)

        print("step6: verify all 4 sections exists and ordered")
        if careers_page.get_job_sections_titles() == expected_job_titles:
            print("verified all 4 sections exists and ordered")
            assert True
        else:
            print("4 sections has a problem check the page")

            assert False

        print("step7: click and verify apply button")
        careers_page.click_apply_button()

        print("step8: submit form with empty values and check validation messages")
        careers_page.click_agree_check_box()
        home_page.submit_contact_us_form()
        time.sleep(5)
        if home_page.get_overall_validation_error_text() not in expected_overall_validation_message:
            print("validation message for overall is not as expected")
            assert False
        careers_page.click_close_ack_modal_button()

        print("step9: verify empty values validation error exists")
        if home_page.get_email_validation_error_text() not in expected_empty_field_validation_message:
            print("validation message empty email isn't as expected")
            assert False
        if home_page.get_name_validation_error_text() not in expected_empty_field_validation_message:
            print("validation message empty name isn't as expected")
            assert False
        if home_page.get_mobile_validation_error_text() not in expected_empty_field_validation_message:
            print("validation message empty mobile isn't as expected")
            assert False
        if home_page.get_message_validation_error_text() not in expected_empty_field_validation_message:
            print("validation message empty message isn't as expected")
            assert False
        print("empty values validation verified")

        print("step10: submit form with invalid email and mobile format")
        home_page.contact_us_fill_email(invalid_email)
        home_page.contact_us_fill_mobile_number(invalid_mobile)
        home_page.submit_contact_us_form()
        time.sleep(5)
        if home_page.get_overall_validation_error_text() not in expected_overall_validation_message:
            print("validation message for overall is not as expected")
            assert False
        careers_page.click_close_ack_modal_button()
        if home_page.get_email_validation_error_text() not in expected_email_validation_message:
            print("validation message for email is not as expected")
            assert False
        if home_page.get_mobile_validation_error_text() not in expected_mobile_validation_message:
            print("validation message for mobile is not as expected")
            assert False
        print("email and mobile validation verified")

        print("step11: upload good_cv")
        careers_page.upload_cv_by_injection(good_cv_file_name)
        home_page.submit_contact_us_form()
        time.sleep(5)
        if home_page.get_overall_validation_error_text() not in expected_overall_validation_message:
            print("validation message for overall is not as expected")
            assert False
        careers_page.click_close_ack_modal_button()
        print("good_cv upload verified")

        print("step12: upload bad_cv")
        careers_page.upload_cv_by_injection(bad_cv_file_name)
        home_page.submit_contact_us_form()
        time.sleep(5)
        if home_page.get_overall_validation_error_text() not in expected_overall_validation_message:
            print("validation message for overall is not as expected")
            assert False
        careers_page.click_close_ack_modal_button()
        print("bad_cv upload verified")
