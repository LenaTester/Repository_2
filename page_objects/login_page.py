from selenium.webdriver.common.by import By

from pythonProject.Final_Project_Juice.utilities.web_ua.base_page import BasePage
from pythonProject.Final_Project_Juice.page_objects.shopping_page import ShoppingPage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    __login_form = (By.XPATH, '//div[@id = "login-form"]')
    __email_input = (By.XPATH, '//input[@id = "email"]')
    __password_input = (By.XPATH, '//input[@id = "password"]')
    __login_button = (By.XPATH, '//button[@id = "loginButton"]')
    __invalid_creds_error = (By.CSS_SELECTOR, '.error')
    __your_basket_button = (By.XPATH, '//button[@aria-label = "Show the shopping cart"]')

    def is_login_form_present(self):
        return self.is_element_present(self.__login_form)

    def enter_email(self, email):
        self.send_keys(self.__email_input, email)
        return self

    def enter_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def click_login_button(self):
        self.click(self.__login_button)
        return self

    def get_error_message(self):
        return self.get_text(self.__invalid_creds_error)

    def is_login_button_active(self):
        return self.is_element_active(self.__login_button)

    def is_your_basket_present(self):
        return self.is_element_present(self.__your_basket_button)

    def open_shopping_page(self):
        self.enter_email('lena03103@gmail.com').enter_password('Juice1@')
        self.click(self.__login_button)
        return ShoppingPage(self.driver)


