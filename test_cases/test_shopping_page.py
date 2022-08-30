from pythonProject.Final_Project_Juice.utilities.wait import wait_until

def test_addin_random_product_to_basket(open_shopping_page):
    """@test description: check, that user can add random product to basket
    @preconditions:
    1. user navigates to shopping page
    @steps:
    1. choose random product
    2. click 'Add to basket'
    @expected result: 'Your Basket shows 1 added product'
    """
    shopping_page = open_shopping_page
    shopping_page.choose_random_product()
    shopping_page.click_add_to_basket_button()
    number_of_products_added = shopping_page.get_number_of_items_added()
    assert number_of_products_added == '1', "Product was not added to basket"

def test_correct_product_name(open_shopping_page):
    """@test description: check, that name of product, added to the basket is correct
    @preconditions:
    1. user navigates to shopping page
    @steps:
    1. choose random product
    2. click 'Add to basket'
    3. check, that added product name = selected random product name
    @expected result: Products have the same name
    """
    shopping_page = open_shopping_page
    shopping_page.choose_random_product()
    random_product_name = shopping_page.get_random_product_header()
    print(random_product_name)
    shopping_page.click_add_to_basket_button()
    shopping_page.click_your_basket_button()
    added_to_basket_product = shopping_page.get_added_product_header()
    assert random_product_name == added_to_basket_product, "Products are different"
    
def test_adding_shopping_address(open_shopping_page):
    """@test description: check, that name of product, added to the basket is correct
    @preconditions:
    1. user navigates to shopping page
    @steps:
    1. click 'Account' button
    2. select 'Orders & Payment'
    3. select 'My saved addresses'
    4. click '+ Add new address'
    5. insert address details
    6. click 'Submit'
    7. check, than new address was created
    @expected result: name = 'name', address = 'address, city, state, zip', country = 'country'
    """
    shopping_page = open_shopping_page
    shopping_page.click_account_button()
    shopping_page.click_orders_and_payments_button()
    shopping_page.click_my_saved_addresses_button()
    shopping_page.click_add_new_address_button()
    shopping_page.enter_country('Ukraine').enter_name('Olena').enter_phone('123456789').\
        enter_zip('123456').enter_address('Randomna str.').enter_city('Kyiv').enter_state('Kyivska')
    time.sleep(3)
    shopping_page.click_submit_button()
    name = shopping_page.get_name_header()
    full_address = shopping_page.get_full_address_header()
    country = shopping_page.get_country_name()
    time.sleep(3)
    assert name == 'Olena', "Name is different"
    assert full_address == 'Randomna str., Kyiv, Kyivska, 123456', "Address is different"
    assert country == 'Ukraine', "Country is different"
