from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_contact_us_page(self):
        self.click_element_css(HomePageLocators.contact_us_modal_initiator, 'contact_us_modal_initiator')

    def contact_us_fill_name(self, name):
        self.insert_text_to_element_css(HomePageLocators.contact_us_form_name_input, name, 'contact_us_form_name_input')

    def contact_us_fill_email(self, email):
        self.insert_text_to_element_css(HomePageLocators.contact_us_form_email_input, email,
                                        'contact_us_form_email_input')

    def contact_us_fill_mobile_number(self, mobile_number):
        self.insert_text_to_element_css(HomePageLocators.contact_us_form_mobile_number_input, mobile_number,
                                        'contact_us_form_mobile_number_input')

    def contact_us_fill_subject(self, subject):
        self.insert_text_to_element_css(HomePageLocators.contact_us_form_subject_input, subject,
                                        'contact_us_form_subject_input')

    def contact_us_fill_message(self, message):
        self.insert_text_to_element_css(HomePageLocators.contact_us_form_message_input, message,
                                        'contact_us_form_message_input')

    def submit_contact_us_form(self):
        self.click_element_css(HomePageLocators.contact_us_form_submit_button, 'contact_us_form_submit_button')

    def get_email_validation_error_text(self):
        return self.get_text_element_css(HomePageLocators.contact_us_form_email_validation_error,
                                         'contact_us_form_email_validation_error')

    def get_name_validation_error_text(self):
        return self.get_text_element_css(HomePageLocators.contact_us_form_name_validation_error,
                                         'contact_us_form_name_validation_error')

    def get_mobile_validation_error_text(self):
        return self.get_text_element_css(HomePageLocators.contact_us_form_mobile_validation_error,
                                         'contact_us_form_mobile_validation_error')

    def get_message_validation_error_text(self):
        return self.get_text_element_css(HomePageLocators.contact_us_form_message_validation_error,
                                         'contact_us_form_message_validation_error')

    def get_overall_validation_error_text(self):
        return self.get_text_element_css(HomePageLocators.contact_us_form_overall_validation_error,
                                         'contact_us_form_overall_validation_error')

    def fill_all_inputs_except_email(self, name, mobile_number, subject, message):
        self.contact_us_fill_name(name)
        self.contact_us_fill_mobile_number(mobile_number)
        self.contact_us_fill_subject(subject)
        self.contact_us_fill_message(message)

    def click_on_company_main_nav(self):
        self.script_execute(HomePageLocators.company_link_in_menu_script, 'company_link_in_menu_script')

    def click_on_careers_main_nav(self):
        self.script_execute(HomePageLocators.careers_link_in_menu_script, 'careers_link_in_menu_script')

    def click_join_us_button(self):
        self.click_element_css(HomePageLocators.join_us_button, 'join_us_button')
