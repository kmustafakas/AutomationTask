import pytest
from pages.HomePage import HomePage
from pages.CompanyPage import CompanyPage


@pytest.mark.usefixtures("setup", "website_setup")
class TestCompanySection:

    def test_company_section(self, config):
        # vars for the test
        expected_facebook_link = 'https://www.facebook.com/MusalaSoft?fref=ts'
        expected_company_section_link = 'https://www.musala.com/company/'
        expected_facebook_photo = 'logo.png'
        expected_leadership_title = 'Leadership'

        home_page = HomePage(self.driver)
        company_page = CompanyPage(self.driver)

        print("step1: go to company page")
        home_page.click_on_company_main_nav()

        print("step2: verify company link")
        current_url = company_page.get_current_url()
        if current_url not in expected_company_section_link:
            print("company url is not as expected")
            assert False

        print("step3: verify leadership section exists")
        leadership_title = company_page.leadership_section_title()
        if leadership_title not in expected_leadership_title:
            print("leadership title is not as expected ")
            assert False

        print("step4: click on facebook button")
        company_page.click_facebook_button()

        print("step5: switch the tab")
        company_page.switch_tab_focus()

        print("step6: download facebook image")
        company_page.download_facebook_image()

        print("step7: verify facebook page link")
        current_url = company_page.get_current_url()
        if current_url not in expected_facebook_link:
            print("leadership title is not as expected ")
            assert False

        print("step8: verify logo screenshot with the original one")
        status = company_page.make_sure_two_images_the_same(company_page.facebook_logo_file_name,
                                                            expected_facebook_photo)
        if not status:
            print("facebook profile not as expected")
            assert False

        print("logo verified with the original one")
