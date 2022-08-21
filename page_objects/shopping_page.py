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

    def click_add_to_basket_button(self):
        self.click(self.__add_to_basket_button)

    def click_your_basket_button(self):
        self.click(self.__your_basket_button)

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