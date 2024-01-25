import pytest
from repo.orange_hrm.fixture.application import Application

app = Application(10)


@pytest.fixture()
def logout(request):
    fixture = Application(10)
    request.addfinalizer(app.logout_from_app)
    return fixture


@pytest.fixture()
def cleanup(request):
    fixture = Application(10)
    request.addfinalizer(app.custom_field_cleanup)
    return fixture


@pytest.fixture()
def cleanup_edited(request):
    fixture = Application(10)
    request.addfinalizer(app.edited_name_custom_field_cleanup)
    return fixture


@pytest.fixture()
def quit_session(request):
    fixture = Application(10)
    request.addfinalizer(app.quit_session)
    return fixture


def test_adding_text_type_custom_field_successfully(cleanup):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.custom_fields_page.page_url)  # Precondition 2
    app.click_button('xpath', app.custom_fields_page.buttons['add'])  # Step 1
    app.fill_input('xpath', app.add_custom_field_page.inputs['field_name'],
                   app.add_custom_field_data.inputs['field_name'])  # Step 2
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['screen'],
                                    app.add_custom_field_page.screen_options['personal_details'])  # Step 3
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['type'],
                                    app.add_custom_field_page.types['text'])  # Step 4
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 5
    app.wait_for_element_to_be_visible('xpath', '//div[text()="{}"]'.format(
        app.add_custom_field_data.inputs['field_name']))  # Assertion 1
    assert app.wd.current_url == app.custom_fields_page.page_url  # Assertion 2


def test_adding_drop_down_type_custom_field_successfully(cleanup):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.custom_fields_page.page_url)  # Precondition 2
    app.click_button('xpath', app.custom_fields_page.buttons['add'])  # Step 1
    app.fill_input('xpath', app.add_custom_field_page.inputs['field_name'],
                   app.add_custom_field_data.inputs['field_name'])  # Step 2
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['screen'],
                                    app.add_custom_field_page.screen_options['personal_details'])  # Step 3
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['type'],
                                    app.add_custom_field_page.types['dropdown'])  # Step 4
    app.fill_input('xpath', app.add_custom_field_page.inputs['select_options'],
                   app.add_custom_field_data.inputs['select_options'])  # Step 5
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 6
    app.wait_for_element_to_be_visible('xpath', '//div[text()="Test Custom Field"]')  # Assertion 1
    assert app.wd.current_url == app.custom_fields_page.page_url  # Assertion 2


def test_adding_custom_field_cancelled_with_data_entered(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.custom_fields_page.page_url)  # Precondition 2
    app.click_button('xpath', app.custom_fields_page.buttons['add'])  # Step 1
    app.fill_input('xpath', app.add_custom_field_page.inputs['field_name'],
                   app.add_custom_field_data.inputs['field_name'])  # Step 2
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['screen'],
                                    app.add_custom_field_page.screen_options['personal_details'])  # Step 3
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['type'],
                                    app.add_custom_field_page.types['text'])  # Step 4
    app.click_button('xpath', app.add_custom_field_page.buttons['cancel'])  # Step 5
    assert app.wd.current_url == app.custom_fields_page.page_url  # Assertion 1


def test_adding_custom_field_cancelled_without_data_entered(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.custom_fields_page.page_url)  # Precondition 2
    app.click_button('xpath', app.custom_fields_page.buttons['add'])  # Step 1
    app.click_button('xpath', app.add_custom_field_page.buttons['cancel'])  # Step 2
    assert app.wd.current_url == app.custom_fields_page.page_url  # Assertion 1


def test_adding_not_declared_type_custom_field_without_any_data(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.custom_fields_page.page_url)  # Precondition 2
    app.click_button('xpath', app.custom_fields_page.buttons['add'])  # Step 1
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 2
    assert app.wd.current_url == app.add_custom_field_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.add_custom_field_page.error_messages['missing_field_name'])
    assert app.wd.find_element(app.types['xpath'],
                               app.add_custom_field_page.error_messages['missing_field_name']).get_attribute(
        'textContent') == app.add_custom_field_data.error_messages['missing_field_name']
    app.wait_for_element_to_be_visible('xpath', app.add_custom_field_page.error_messages['missing_screen'])
    assert app.wd.find_element(app.types['xpath'],
                               app.add_custom_field_page.error_messages['missing_screen']).get_attribute(
        'textContent') == app.add_custom_field_data.error_messages['missing_screen']
    app.wait_for_element_to_be_visible('xpath', app.add_custom_field_page.error_messages['missing_type'])
    assert app.wd.find_element(app.types['xpath'],
                               app.add_custom_field_page.error_messages['missing_type']).get_attribute(
        'textContent') == app.add_custom_field_data.error_messages['missing_type']  # Assertion 2


def test_adding_drop_down_type_custom_field_without_any_data(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.custom_fields_page.page_url)  # Precondition 2
    app.click_button('xpath', app.custom_fields_page.buttons['add'])  # Step 1
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['type'],
                                    app.add_custom_field_page.types['dropdown'])  # Step 2
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 3
    assert app.wd.current_url == app.add_custom_field_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.add_custom_field_page.error_messages['missing_field_name'])
    assert app.wd.find_element(app.types['xpath'],
                               app.add_custom_field_page.error_messages['missing_field_name']).get_attribute(
        'textContent') == app.add_custom_field_data.error_messages['missing_field_name']
    app.wait_for_element_to_be_visible('xpath', app.add_custom_field_page.error_messages['missing_screen'])
    assert app.wd.find_element(app.types['xpath'],
                               app.add_custom_field_page.error_messages['missing_screen']).get_attribute(
        'textContent') == app.add_custom_field_data.error_messages['missing_screen']
    app.wait_for_element_to_be_visible('xpath', app.add_custom_field_page.error_messages['missing_options'])
    assert app.wd.find_element(app.types['xpath'],
                               app.add_custom_field_page.error_messages['missing_options']).get_attribute(
        'textContent') == app.add_custom_field_data.error_messages['missing_options']  # Assertion 2


def test_adding_custom_field_without_field_name(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.custom_fields_page.page_url)  # Precondition 2
    app.click_button('xpath', app.custom_fields_page.buttons['add'])  # Step 1
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['screen'],
                                    app.add_custom_field_page.screen_options['personal_details'])  # Step 2
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['type'],
                                    app.add_custom_field_page.types['text'])  # Step 3
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 4
    assert app.wd.current_url == app.add_custom_field_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.add_custom_field_page.error_messages['missing_field_name'])
    assert app.wd.find_element(app.types['xpath'],
                               app.add_custom_field_page.error_messages['missing_field_name']).get_attribute(
        'textContent') == app.add_custom_field_data.error_messages['missing_field_name']  # Assertion 2


def test_adding_custom_field_without_screen(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.custom_fields_page.page_url)  # Precondition 2
    app.click_button('xpath', app.custom_fields_page.buttons['add'])  # Step 1
    app.fill_input('xpath', app.add_custom_field_page.inputs['field_name'],
                   app.add_custom_field_data.inputs['field_name'])  # Step 2
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['type'],
                                    app.add_custom_field_page.types['text'])  # Step 3
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 4
    assert app.wd.current_url == app.add_custom_field_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.add_custom_field_page.error_messages['missing_screen'])
    assert app.wd.find_element(app.types['xpath'],
                               app.add_custom_field_page.error_messages['missing_screen']).get_attribute(
        'textContent') == app.add_custom_field_data.error_messages['missing_screen']  # Assertion 2


def test_adding_custom_field_without_type(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.navigate_to_page(app.custom_fields_page.page_url)  # Precondition 2
    app.click_button('xpath', app.custom_fields_page.buttons['add'])  # Step 1
    app.fill_input('xpath', app.add_custom_field_page.inputs['field_name'],
                   app.add_custom_field_data.inputs['field_name'])  # Step 2
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['screen'],
                                    app.add_custom_field_page.screen_options['personal_details'])  # Step 3
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 4
    assert app.wd.current_url == app.add_custom_field_page.page_url  # Assertion 1
    app.wait_for_element_to_be_visible('xpath', app.add_custom_field_page.error_messages['missing_type'])
    assert app.wd.find_element(app.types['xpath'],
                               app.add_custom_field_page.error_messages['missing_type']).get_attribute(
        'textContent') == app.add_custom_field_data.error_messages['missing_type']  # Assertion 2


def test_custom_field_deletion_successful(logout):
    app.login_to_app_as_admin()  # Precondition 1
    app.add_custom_field(app.add_custom_field_data.inputs['field_name'],
                         app.add_custom_field_page.screen_options['personal_details'], 'text')  # Precondition 2, 3
    app.click_button('xpath', app.custom_fields_page.icons['delete'])  # Step 1
    app.click_button('xpath', app.custom_fields_page.buttons['removal_confirmation'])  # Step 2
    assert app.wd.current_url == app.custom_fields_page.page_url  # Assertion 1
    app.wait_for_text_to_be_present('xpath', '//div[text()="Blood Type"]', 'Blood Type')
    assert len(app.wd.find_elements(app.types['xpath'], '//div[text()="{}"]'.format(
        app.add_custom_field_data.inputs['field_name']))) == 0  # Assertion 2


def test_custom_field_deletion_cancelled(cleanup):
    app.login_to_app_as_admin()  # Precondition 1
    app.add_custom_field(app.add_custom_field_data.inputs['field_name'],
                         app.add_custom_field_page.screen_options['personal_details'], 'text')  # Precondition 2, 3
    app.click_button('xpath', app.custom_fields_page.icons['delete'])  # Step 1
    app.click_button('xpath', app.custom_fields_page.buttons['removal_cancellation'])  # Step 2
    assert app.wd.current_url == app.custom_fields_page.page_url  # Assertion 1
    app.wait_for_text_to_be_present('xpath', '//div[text()="Blood Type"]', 'Blood Type')
    assert len(app.wd.find_elements(app.types['xpath'], '//div[text()="{}"]'.format(
        app.add_custom_field_data.inputs['field_name']))) == 1  # Assertion 2


def test_editing_custom_field_name(cleanup_edited):
    app.login_to_app_as_admin()  # Precondition 1
    app.add_custom_field(app.add_custom_field_data.inputs['field_name'],
                         app.add_custom_field_page.screen_options['personal_details'], 'text')  # Precondition 2, 3
    app.click_button('xpath', app.custom_fields_page.icons['edit'])  # Step 1
    app.clear_custom_field_inputs('field_name')
    app.fill_input('xpath', app.add_custom_field_page.inputs['field_name'],
                   app.add_custom_field_data.inputs['edited_field_name'])  # Step 2
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 3
    app.wait_for_element_to_be_visible('xpath', '//div[text()="{}"]'.format(app.add_custom_field_data.inputs[
                                                                                'edited_field_name']))  # Assertion 1
    assert app.wd.current_url == app.custom_fields_page.page_url  # Assertion 2


def test_editing_custom_field_screen(cleanup):
    app.login_to_app_as_admin()  # Precondition 1
    app.add_custom_field(app.add_custom_field_data.inputs['field_name'],
                         app.add_custom_field_page.screen_options['personal_details'], 'text')  # Precondition 2, 3
    app.click_button('xpath', app.custom_fields_page.icons['edit'])  # Step 1
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['screen'],
                                    app.add_custom_field_page.screen_options['contact_details'])  # Step 2
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 3
    app.wait_for_text_to_be_present('xpath', '//div[text()="{}"]/following::div[1]'.format(
        app.add_custom_field_data.inputs['field_name']), 'Contact Details')  # Assertion 1
    assert app.wd.current_url == app.custom_fields_page.page_url  # Assertion 2


def test_changing_text_type_to_drop_down_type(cleanup):
    app.login_to_app_as_admin()  # Precondition 1
    app.add_custom_field(app.add_custom_field_data.inputs['field_name'],
                         app.add_custom_field_page.screen_options['personal_details'], 'text')  # Precondition 2, 3
    app.click_button('xpath', app.custom_fields_page.icons['edit'])  # Step 1
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['type'],
                                    app.add_custom_field_page.types['dropdown'])  # Step 2
    app.fill_input('xpath', app.add_custom_field_page.inputs['select_options'],
                   app.add_custom_field_data.inputs['select_options'])  # Step 3
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 4
    app.wait_for_text_to_be_present('xpath', '//div[text()="{}"]/following::div[3]'.format(
        app.add_custom_field_data.inputs['field_name']), 'Drop Down')  # Assertion 1
    assert app.wd.current_url == app.custom_fields_page.page_url  # Assertion 2


def test_changing_drop_down_type_to_text_type(cleanup):
    app.login_to_app_as_admin()  # Precondition 1
    app.add_custom_field(app.add_custom_field_data.inputs['field_name'],
                         app.add_custom_field_page.screen_options['personal_details'], 'dropdown',
                         app.add_custom_field_data.inputs['select_options'])  # Precondition 2, 3
    app.click_button('xpath', app.custom_fields_page.icons['edit'])  # Step 1
    app.select_option_from_dropdown('xpath', app.add_custom_field_page.dropdowns['type'],
                                    app.add_custom_field_page.types['text'])  # Step 2
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 3
    app.wait_for_text_to_be_present('xpath', '//div[text()="{}"]/following::div[3]'.format(
        app.add_custom_field_data.inputs['field_name']), 'Text or Number')  # Assertion 1
    assert app.wd.current_url == app.custom_fields_page.page_url  # Assertion 2


def test_editing_select_options(quit_session):
    app.login_to_app_as_admin()  # Precondition 1
    app.add_custom_field(app.add_custom_field_data.inputs['field_name'],
                         app.add_custom_field_page.screen_options['personal_details'], 'dropdown',
                         app.add_custom_field_data.inputs['select_options'])  # Precondition 2, 3
    app.click_button('xpath', app.custom_fields_page.icons['edit'])  # Step 1
    app.clear_custom_field_inputs('select_options')
    app.fill_input('xpath', app.add_custom_field_page.inputs['select_options'],
                   app.add_custom_field_data.inputs['edited_select_options'])  # Step 2
    app.click_button('xpath', app.add_custom_field_page.buttons['save'])  # Step 3
    app.wait_for_element_to_be_visible('xpath', '//div[text()="{}"]'.format(
        app.add_custom_field_data.inputs['field_name']))
    app.click_button('xpath', app.custom_fields_page.icons['edit'])
    app.wait_for_element_to_be_visible('xpath', app.add_custom_field_page.inputs['select_options'])
    assert app.wd.find_element(app.types['xpath'], app.add_custom_field_page.inputs['select_options']).get_attribute(
        'value') == app.add_custom_field_data.inputs['edited_select_options']  # Assertion 1
    app.delete_custom_field(app.add_custom_field_data.inputs['field_name'])
    app.logout_from_app()
