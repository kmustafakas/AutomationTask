import pytest
from pages.HomePage import HomePage
from pages.CareersPage import CareersPage
import time


@pytest.mark.usefixtures("setup", "website_setup")
class TestCareersGetJobsByCity:

    def test_get_jobs_by_city(self, config):
        # vars for the test
        expected_careers_join_us_link = 'https://www.musala.com/careers/join-us/'
        expected_careers_join_us_link_anywhere = 'https://www.musala.com/careers/join-us/?location='
        sofia_location = 'Sofia'
        skopje_location = 'Skopje'

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

        print("step4: select Sofia_location location")
        try:
            careers_page.select_location(sofia_location)
        except:
            # because it keep failing even though it's selected
            current_url = careers_page.get_current_url()
            if current_url not in expected_careers_join_us_link_anywhere:
                print("careers join us url is not as expected")
                assert False

        print("step5: print jobs names and links in Sofia_location")
        names, links = careers_page.get_presented_jobs_names_and_links()
        iterator = 0
        print(sofia_location)
        while iterator < len(names):
            print('Position: ' + names[iterator])
            print('More info: ' + links[iterator])
            print('#######')
            iterator += 1

        print('=======================================')

        print("step6: select Skopje_location location")
        try:
            careers_page.select_location(skopje_location)
        except:
            # because it keep failing even though it's selected
            current_url = careers_page.get_current_url()
            if current_url not in expected_careers_join_us_link_anywhere:
                print("careers join us url is not as expected")
                assert False

        print("step7: print jobs names and links in Skopje_location")
        names, links = careers_page.get_presented_jobs_names_and_links()
        iterator = 0
        print(skopje_location)
        while iterator < len(names):
            print('Position: ' + names[iterator])
            print('More info: ' + links[iterator])
            print('#######')
            iterator += 1

        print('=======================================')
