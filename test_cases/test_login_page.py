import pytest

from pythonProject.Final_Project_Juice.utilities.data_generator import random_string


def test_wrong_creds_check(open_login_page):
    """@test description: check, that user can't login with wrong creds
    @preconditions:
    1. user navigates to login page
    @steps:
    1. enter wrong email and wrong password
    2. click Log in button
    @expected result: user receives message 'Invalid email or password.'
    """
    login_page = open_login_page
    validation_message = login_page.enter_email(random_string()).enter_password(
        random_string()).click_login_button().get_error_message()
    assert validation_message == 'Invalid email or password.'


@pytest.mark.parametrize('creds', [[random_string(), ''], ['', random_string()]])
def test_login_button_state(creds, open_login_page):
    login_page = open_login_page
    login_page.enter_email(random_string()).enter_password(random_string())
    actual_result = login_page.is_login_button_active()
    assert actual_result is False, 'Login button is active'

def test_correct_creds_check(open_login_page):
    """@test description: check, that user can login with correct creds
    @preconditions:
    1. user navigates to login page
    @steps:
    1. enter correct email and correct password
    2. click Log in button
    @expected result: 'Your Basket button is present'
    """
    login_page = open_login_page
    redirection_to_shopping_page = login_page.enter_email('lena03103@gmail.com').enter_password(
        'Juice1@').click_login_button().is_your_basket_present()
    assert redirection_to_shopping_page is True, "Shopping page is not opened"
