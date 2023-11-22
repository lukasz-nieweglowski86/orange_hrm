from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import repo.orange_hrm.data.login_page as login_data
import repo.orange_hrm.pages.login_page as login_page
import repo.orange_hrm.pages.dashboard_page as dashboard_page
from repo.orange_hrm.fixture.page_base import PageBase
from repo.orange_hrm.fixture.application import Application
from repo.orange_hrm.fixture.session import SessionHelper

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

wd = webdriver.Chrome(service=service, options=options)
wd.maximize_window()

page_base = PageBase(wd, 10)
app = Application(wd, 10)
session = SessionHelper()

"""
Test: test_login_successful

PRECONDITIONS:
1. User exists and is logged out.

STEPS:
1. Navigate to login page. -> Login page is displayed.
2. Fill the 'username' field. -> Username is entered.
3. Fill the 'password' field. -> Password is entered.
4. Click the 'Login' button. -> Button is clicked, dashboard page is displayed.

ASSERTIONS:
1. Check if current URL matches dashboard page URL.
"""


def test_login_successful():
    page_base.navigate_to_page(login_page.page_url)  # Step 1
    page_base.fill_input('xpath', login_page.inputs['login'], login_data.logins['correct_value'])  # Step 2
    page_base.fill_input('xpath', login_page.inputs['password'], login_data.passwords['correct_value'])  # Step 3
    page_base.click_button('xpath', login_page.buttons['login'])  # Step 4
    assert wd.current_url == dashboard_page.page_url  # Assertion 1
    app.logout_from_app()
    session.quit_session()


"""
Test: test_login_incorrect_username

PRECONDITIONS:
1. User exists and is logged out.

STEPS:
1. Navigate to login page. -> Login page is displayed.
2. Fill the 'username' field. -> Username is entered.
3. Fill the 'password' field. -> Password is entered.
4. Click the 'Login' button. -> Button is clicked, error message is displayed.

ASSERTIONS:
1. Check if current URL matches login page URL.
2. Check if displayed error message text is what it should be.
"""


def test_login_incorrect_username():
    page_base.navigate_to_page(login_page.page_url)  # Step 1
    page_base.fill_input('xpath', login_page.inputs['login'], login_data.logins['incorrect_value'])  # Step 2
    page_base.fill_input('xpath', login_page.inputs['password'], login_data.passwords['correct_value'])  # Step 3
    page_base.click_button('xpath', login_page.buttons['login'])  # Step 4
    assert wd.current_url == login_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', login_page.error_messages['invalid_credentials'])
    assert wd.find_element(page_base.types['xpath'], login_page.error_messages['invalid_credentials']).text == \
           login_data.error_message_value['invalid_credentials']  # Assertion 2
    session.quit_session()


"""
Test: test_login_incorrect_password

PRECONDITIONS:
1. User exists and is logged out.

STEPS:
1. Navigate to login page. -> Login page is displayed.
2. Fill the 'username' field. -> Username is entered.
3. Fill the 'password' field. -> Password is entered.
4. Click the 'Login' button. -> Button is clicked, error message is displayed.

ASSERTIONS:
1. Check if current URL matches login page URL.
2. Check if displayed error message text is what it should be.
"""


def test_login_incorrect_password():
    page_base.navigate_to_page(login_page.page_url)  # Step 1
    page_base.fill_input('xpath', login_page.inputs['login'], login_data.logins['correct_value'])  # Step 2
    page_base.fill_input('xpath', login_page.inputs['password'], login_data.passwords['incorrect_value'])  # Step 3
    page_base.click_button('xpath', login_page.buttons['login'])  # Step 4
    assert wd.current_url == login_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', login_page.error_messages['invalid_credentials'])
    assert wd.find_element(page_base.types['xpath'], login_page.error_messages['invalid_credentials']).text == \
           login_data.error_message_value['invalid_credentials']  # Assertion 2
    session.quit_session()


"""
Test: test_login_no_username

PRECONDITIONS:
1. User exists and is logged out.

STEPS:
1. Navigate to login page. -> Login page is displayed.
2. Fill the 'password' field. -> Password is entered.
3. Click the 'Login' button. -> Button is clicked, error message under username input is displayed.

ASSERTIONS:
1. Check if current URL matches login page URL.
2. Check if displayed error message text is what it should be.
"""


def test_login_no_username():
    page_base.navigate_to_page(login_page.page_url)  # Step 1
    page_base.fill_input('xpath', login_page.inputs['password'], login_data.passwords['correct_value'])  # Step 2
    page_base.click_button('xpath', login_page.buttons['login'])  # Step 3
    assert wd.current_url == login_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', login_page.error_messages['missing_username'])
    assert wd.find_element(page_base.types['xpath'], login_page.error_messages['missing_username']).text == \
           login_data.error_message_value['missing_username']  # Assertion 2
    session.quit_session()


"""
Test: test_login_no_password

PRECONDITIONS:
1. User exists and is logged out.

STEPS:
1. Navigate to login page. -> Login page is displayed.
2. Fill the 'username' field. -> Username is entered.
3. Click the 'Login' button. -> Button is clicked, error message under password input is displayed.

ASSERTIONS:
1. Check if current URL matches login page URL.
2. Check if displayed error message text is what it should be.
"""


def test_login_no_password():
    page_base.navigate_to_page(login_page.page_url)  # Step 1
    page_base.fill_input('xpath', login_page.inputs['login'], login_data.logins['correct_value'])  # Step 2
    page_base.click_button('xpath', login_page.buttons['login'])  # Step 3
    assert wd.current_url == login_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', login_page.error_messages['missing_password'])
    assert wd.find_element(page_base.types['xpath'], login_page.error_messages['missing_password']).text == \
           login_data.error_message_value['missing_password']  # Assertion 2
    session.quit_session()


"""
Test: test_login_no_username_and_password

PRECONDITIONS:
1. User exists and is logged out.

STEPS:
1. Navigate to login page. -> Login page is displayed.
2. Click the 'Login' button. -> Button is clicked, error messages under username and password inputs are displayed.

ASSERTIONS:
1. Check if current URL matches login page URL.
2. Check if displayed error messages texts are what they should be.
"""


def test_login_no_username_and_password():
    page_base.navigate_to_page(login_page.page_url)  # Step 1
    page_base.click_button('xpath', login_page.buttons['login'])  # Step 2
    assert wd.current_url == login_page.page_url  # Assertion 1
    page_base.wait_for_element_to_be_visible('xpath', login_page.error_messages['missing_username'])
    page_base.wait_for_element_to_be_visible('xpath', login_page.error_messages['missing_password'])
    assert wd.find_element(page_base.types['xpath'], login_page.error_messages['missing_username']).text == \
           login_data.error_message_value['missing_username']  # Assertion 2
    assert wd.find_element(page_base.types['xpath'], login_page.error_messages['missing_password']).text == \
           login_data.error_message_value['missing_password']  # Assertion 2
    session.quit_session()
