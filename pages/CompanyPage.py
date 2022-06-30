from pages.base_page import BasePage
from locators.company_page_locators import CompanyPageLocators


class CompanyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def leadership_section_title(self):
        return self.get_text_element_css(CompanyPageLocators.leadership_section_title, 'leadership_section_title')

    def download_facebook_image(self):
        self.get_facebook_profile_image(CompanyPageLocators.facebook_logo)

    def click_facebook_button(self):
        self.click_element_css(CompanyPageLocators.facebook_anchor, 'facebook_anchor')
