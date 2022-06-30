from pages.base_page import BasePage
from locators.careers_page_locators import CareersPageLocators
import os


class CareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_check_positions_button(self):
        try:
            self.click_element_css(CareersPageLocators.check_our_position_hero_button, 'check_our_position_hero_button')
        except:
            # will do nothing , next step will verify link and make sure it goes to the right link
            print("it failing even after click success")

    def select_location(self, location):
        self.select_from_select(CareersPageLocators.careers_locations_select, location, 'careers_locations_select')

    def click_on_a_job_card(self, job_name):
        locator = CareersPageLocators.job_card_general_script.replace('job_name', job_name)
        self.script_execute(locator, 'job_name')

    def get_job_sections_titles(self):
        job_description_elements = self.get_multiple_elements(
            CareersPageLocators.job_description_sections_titels_general, 'job_description_sections_titels_general')
        titles = []
        for element in job_description_elements:
            titles.append(element.text)

        return titles

    def get_file_path(self, file_name):
        return os.path.abspath(file_name)

    def upload_cv(self, file_name):
        cv_abs_path = self.get_file_path(file_name)
        self.click_element_css(CareersPageLocators.cv_upload_input, 'cv_upload_input')
        self.upload_file(cv_abs_path)

    def upload_cv_by_injection(self, file_name):
        cv_abs_path = self.get_file_path(file_name)
        script = CareersPageLocators.cv_upload_to_inject_file_script.replace("file", cv_abs_path)
        self.script_execute(script, 'cv_upload_input')

    def click_apply_button(self):
        self.click_element_css(CareersPageLocators.apply_button, 'apply_button')

    def click_close_ack_modal_button(self):
        self.click_element_css(CareersPageLocators.close_message_modal_in_apply_form_button,
                               'close_message_modal_in_apply_form_button')

    def click_agree_check_box(self):
        self.click_element_css(CareersPageLocators.agree_checkbox_apply_form, 'agree_checkbox_apply_form')

    def get_presented_jobs_names_and_links(self):
        names = []
        links = []
        jobs_names = self.get_multiple_elements(
            CareersPageLocators.job_card_name_general, 'job_card_name_general')
        for element in jobs_names:
            names.append(element.text)

        jobs_links = self.get_multiple_elements(
            CareersPageLocators.job_card_link_general, 'job_card_link_general')
        for element in jobs_links:
            links.append(element.get_attribute('href'))

        return names, links
