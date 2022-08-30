from selenium.webdriver.common.by import By
import random

from pythonProject.Final_Project_Juice.utilities.web_ua.base_page import BasePage

class ShoppingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    __add_to_basket_button = (By.XPATH, '//button[@aria-label = "Add to Basket"]')
    __added_to_basket_product = (By.XPATH, '//span[@class = "fa-layers-counter fa-layers-top-right fa-3x warn-notification"]')
    __your_basket_button = (By.XPATH, '//button[@aria-label = "Show the shopping cart"]')
    __product_name = (By.XPATH, '//button[@aria-label = "Add to Basket"]/ancestor::mat-card[1]/descendant::div[@class = "item-name"]')
    __added_product_name = (By.XPATH, '//mat-cell[@class = "mat-cell cdk-cell cdk-column-product mat-column-product ng-star-inserted"]')
    __account_button = (By.XPATH, '//button[@aria-label = "Show/hide account menu"]')
    __orders_and_payments_button = (By.XPATH, '//button[@aria-label = "Show Orders and Payment Menu"]')
    __my_saved_addresses_button = (By.XPATH, '//button[@aria-label = "Go to saved address page"]')
    __add_new_address_button = (By.XPATH, '//button[@aria-label = "Add a new address"]')
    __input_country = (By.XPATH, '//input[@placeholder = "Please provide a country."]')
    __input_name = (By.XPATH, '//input[@placeholder = "Please provide a name."]')
    __input_phone = (By.XPATH, '//input[@placeholder = "Please provide a mobile number."]')
    __input_zip = (By.XPATH, '//input[@placeholder = "Please provide a ZIP code."]')
    __input_address = (By.XPATH, '//textarea[@placeholder = "Please provide an address."]')
    __input_city = (By.XPATH, '//input[@placeholder = "Please provide a city."]')
    __input_state = (By.XPATH, '//input[@placeholder = "Please provide a state."]')
    __submit_button = (By.XPATH, '//button[@id = "submitButton"]')
    __name_info = (By.XPATH, '//mat-cell[@class = "mat-cell cdk-cell cdk-column-Name mat-column-Name ng-star-inserted"]')
    __full_address = (By.XPATH, '//mat-cell[@class = "mat-cell cdk-cell cdk-column-Address mat-column-Address ng-star-inserted"]')
    __country_name = (By.XPATH, '//mat-cell[@class = "mat-cell cdk-cell cdk-column-Country mat-column-Country ng-star-inserted"]')

    def click_add_to_basket_button(self):
        self.click(self.__add_to_basket_button)

    def click_your_basket_button(self):
        self.click(self.__your_basket_button)

    def click_account_button(self):
        self.click(self.__account_button)

    def click_orders_and_payments_button(self):
        self.click(self.__orders_and_payments_button)

    def click_my_saved_addresses_button(self):
        self.click(self.__my_saved_addresses_button)

    def click_add_new_address_button(self):
        self.click(self.__add_new_address_button)

    def click_submit_button(self):
        self.click(self.__submit_button)

    def get_number_of_items_added(self):
        return self.get_text(self.__added_to_basket_product)

    def choose_random_product(self):
        products = self.wait_for_elements_located(self.__add_to_basket_button)
        random_product = random.choice(products)
        return random_product

    def get_random_product_header(self):
        return self.get_text(self.__product_name)

    def get_added_product_header(self):
        return self.get_text(self.__added_product_name)

    def enter_country(self, country):
        self.send_keys(self.__input_country, country)
        return self

    def enter_name(self, name):
        self.send_keys(self.__input_name, name)
        return self

    def enter_phone(self, phone):
        self.send_keys(self.__input_phone, phone)
        return self

    def enter_zip(self, zip):
        self.send_keys(self.__input_zip, zip)
        return self

    def enter_address(self, address):
        self.send_keys(self.__input_address, address)
        return self

    def enter_city(self, city):
        self.send_keys(self.__input_city, city)
        return self

    def enter_state(self, state):
        self.send_keys(self.__input_state, state)
        return self

    def get_name_header(self):
        return self.get_text(self.__name_info)

    def get_full_address_header(self):
        return self.get_text(self.__full_address)

    def get_country_name(self):
        return self.get_text(self.__country_name)
