class HomePageLocators:
    logo = "#navbar  a.brand"
    contact_us_modal_initiator = '[href="#contact_form_pop"]'
    contact_us_form_name_input = '#fancybox-content [name="your-name"]'
    contact_us_form_email_input = '#fancybox-content [name="your-email"]'
    contact_us_form_mobile_number_input = '#fancybox-content [name="mobile-number"]'
    contact_us_form_subject_input = '#fancybox-content [name="your-subject"]'
    contact_us_form_message_input = '#fancybox-content [name="your-message"]'
    contact_us_form_submit_button = '#fancybox-content [value="Send"]'
    contact_us_form_overall_validation_error = '#fancybox-content div.wpcf7-response-output'
    contact_us_form_email_validation_error = '#fancybox-content span.your-email span'
    contact_us_form_name_validation_error = '#fancybox-content span.your-name span'
    contact_us_form_mobile_validation_error = '#fancybox-content span.mobile-number span'
    contact_us_form_message_validation_error = '#fancybox-content span.your-message span'
    company_link_in_menu_script = "document.querySelector('#menu-main-nav-1 > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-887 > a').click()"
    careers_link_in_menu_script = "document.querySelector('#menu-main-nav-1 > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-478 > a').click()"
    join_us_button = 'button.join-us-white'
