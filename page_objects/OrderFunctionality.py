from robot.libraries.BuiltIn import BuiltIn
from Itemlocators.Items import Items
from UserData import UserData
from CatalogueItems.ListItems import ListItems

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class OrderForm_Locators:
    header_logo = 'css = .header__logo > a:last-child'
    order_form = 'css = #collapseOne > div'

    name_field = 'css = #firstname'
    last_name_field = 'css = #lastname'
    middle_name_field = 'css = #middlename'
    phone_number_field = 'css = #phone'
    email_field = 'css = #email'

    another_man_checkbox = 'css = label[for="customerAnotherAddress"]'

    continue_btn = 'css = #orderContinue'
    submit_account_btn = 'css = #submitAccount'
    submit_order_form = 'css = #submitOrderForm'
    submit_order_btn = 'css = #submitOrderForm button.btn.btn__form-next'

    delivery_method_form = 'css = #collapseTwo'
    delivery_method_droplist = 'css = #opc_delivery_methods > div.carrier_block' \
                               ' > div.fline > span > span.selection > span'

    # ----------------- delivery form items ---------------------------- #
    user_city_droplist = 'css = #select2-address_city-container > span'
    user_city_droplist_item = 'css = ul.select2-results__options :nth-child(1)'
    user_city_field = 'css = span.select2-search.select2-search--dropdown > input'
    # ------------------ delivery droplist items ----------------------- #
    nova_poshta = 'css = ul.select2-results__options :nth-child(1)'
    nova_poshta_delivery = 'css = ul.select2-results__options :nth-child(2)'
    justin = 'css = ul.select2-results__options :nth-child(3)'
    delivery_group = 'css = ul.select2-results__options :nth-child(4)'
    self_delivery = 'css = ul.select2-results__options :nth-child(5)'

    # ---------------- delivery warehouse droplist items ------------------ #
    delivery_warehouse_droplist = 'css = #warehouse_div > span > span.selection > span'
    delivery_warehouse_droplist_item = 'css = ul.select2-results__options :nth-child(1)'
    warehouse_field = 'css = span.select2-search.select2-search--dropdown > input'


class OrderFunctionality(Items, UserData):
    # 7. Check user can create an order
    def click_11022_3901094_item(self):
        bi.run_keyword('Scroll element into view', Items.item_11022_3901094)
        bi.run_keyword('Click element', Items.item_11022_3901094)

    def check_user_info_is_correct(self):
        bi.run_keyword('Textfield value should be', OrderForm_Locators.last_name_field, UserData.user_last_name)
        bi.run_keyword('Textfield value should be', OrderForm_Locators.name_field, UserData.user_name)
        bi.run_keyword('Textfield value should be', OrderForm_Locators.middle_name_field, UserData.user_middle_name)
        bi.run_keyword('Textfield value should be', OrderForm_Locators.phone_number_field, UserData.current_num)
        bi.run_keyword('Textfield value should be', OrderForm_Locators.email_field, UserData.user_email)

    def click_continue_btn(self):
        bi.run_keyword('Mouse over', OrderForm_Locators.continue_btn)
        bi.run_keyword('Click button', OrderForm_Locators.continue_btn)

    def choose_delivery_method(self):
        bi.run_keyword('check_preloader')
        bi.run_keyword('Click element', OrderForm_Locators.delivery_method_droplist)
        bi.run_keyword('Mouse over', OrderForm_Locators.self_delivery)
        bi.run_keyword('Click element', OrderForm_Locators.self_delivery)

    # 13. Creating order via Nova Poshta
    def add_item_to_cart(self):
        bi.run_keyword('click_accessories_btn')
        bi.run_keyword('click_11022_3901094_item')
        bi.run_keyword('add_current_item_to_cart')
        bi.run_keyword('click_checkout_btn')

    def input_user_data_in_order_form(self):
        bi.run_keyword('Wait until page contains element', OrderForm_Locators.last_name_field)
        bi.run_keyword('Mouse over', OrderForm_Locators.last_name_field)
        bi.run_keyword('Click element', OrderForm_Locators.last_name_field)
        bi.run_keyword('Input text', OrderForm_Locators.last_name_field, UserData.user_last_name)
        bi.run_keyword('Click element', OrderForm_Locators.name_field)
        bi.run_keyword('Input text', OrderForm_Locators.name_field, UserData.user_name)
        bi.run_keyword('Input text', OrderForm_Locators.middle_name_field, UserData.user_middle_name)
        bi.run_keyword('Input text', OrderForm_Locators.phone_number_field, UserData.random_phone_number)
        bi.run_keyword('Input text', OrderForm_Locators.email_field, UserData.random_user_email)

    def submit_user_data(self):
        bi.run_keyword('Mouse over', OrderForm_Locators.submit_account_btn)
        bi.run_keyword('Click button', OrderForm_Locators.submit_account_btn)

    def choose_nova_poshta_delivery_method(self):
        bi.run_keyword('check_preloader')
        bi.run_keyword('Click element', OrderForm_Locators.delivery_method_droplist)
        bi.run_keyword('Mouse over', OrderForm_Locators.nova_poshta)
        bi.run_keyword('Click element', OrderForm_Locators.nova_poshta)

    def choose_city_to_delivery(self):
        bi.run_keyword('Click element', OrderForm_Locators.user_city_droplist)
        bi.run_keyword('Wait until element is visible', OrderForm_Locators.user_city_field)
        bi.run_keyword('Click element', OrderForm_Locators.user_city_field)
        bi.run_keyword('Input text', OrderForm_Locators.user_city_field, UserData.user_city)
        bi.run_keyword('Wait until element contains', OrderForm_Locators.user_city_droplist_item, 'Львов')
        bi.run_keyword('Mouse over', OrderForm_Locators.user_city_droplist_item)
        bi.run_keyword('Click element', OrderForm_Locators.user_city_droplist_item)

    def choose_delivery_warehouse(self):
        bi.run_keyword('Wait until element is visible', OrderForm_Locators.delivery_warehouse_droplist)
        bi.run_keyword('Click element', OrderForm_Locators.delivery_warehouse_droplist)
        bi.run_keyword('Wait until element is visible', OrderForm_Locators.warehouse_field)
        bi.run_keyword('Click element', OrderForm_Locators.warehouse_field)
        bi.run_keyword('Input text', OrderForm_Locators.warehouse_field, UserData.warehouse_num)
        bi.run_keyword('Wait until element contains', OrderForm_Locators.delivery_warehouse_droplist_item,
                       'Отделение №67 (до 30 кг): ул. Стрыйская, 45а')
        bi.run_keyword('Mouse over', OrderForm_Locators.delivery_warehouse_droplist_item)
        bi.run_keyword('Click element', OrderForm_Locators.delivery_warehouse_droplist_item)

    # 14. Creating multi order via Justin
    def add_items_to_cart(self):
        bi.run_keyword('add_item_to_cart')
        bi.run_keyword('Mouse over', OrderForm_Locators.header_logo)
        bi.run_keyword('Click link', OrderForm_Locators.header_logo)
        bi.run_keyword('Wait until page contains element', ListItems.accessories_item)
        bi.run_keyword('click_accessories_btn')
        bi.run_keyword('click_iz04_item')
        bi.run_keyword('add_iz04_in_cart')
        bi.run_keyword('click_checkout_btn')

    def input_user_data_in_order_form_2(self):
        bi.run_keyword('Wait until page contains element', OrderForm_Locators.last_name_field)
        bi.run_keyword('Mouse over', OrderForm_Locators.last_name_field)
        bi.run_keyword('Click element', OrderForm_Locators.last_name_field)
        bi.run_keyword('Input text', OrderForm_Locators.last_name_field, UserData.user_last_name)
        bi.run_keyword('Click element', OrderForm_Locators.name_field)
        bi.run_keyword('Input text', OrderForm_Locators.name_field, UserData.user_name)
        bi.run_keyword('Input text', OrderForm_Locators.middle_name_field, UserData.user_middle_name)
        bi.run_keyword('Input text', OrderForm_Locators.phone_number_field, UserData.random_phone_number)
        bi.run_keyword('Input text', OrderForm_Locators.email_field, UserData.random_user_email)

    def choose_justin_delivery(self):
        bi.run_keyword('check_preloader')
        bi.run_keyword('Click element', OrderForm_Locators.delivery_method_droplist)
        bi.run_keyword('Mouse over', OrderForm_Locators.justin)
        bi.run_keyword('Click element', OrderForm_Locators.justin)

    def choose_justin_city_address(self):
        bi.run_keyword('check_preloader')
        bi.run_keyword('Click element', OrderForm_Locators.user_city_droplist)
        bi.run_keyword('Wait until element is visible', OrderForm_Locators.user_city_field)
        bi.run_keyword('Click element', OrderForm_Locators.user_city_field)
        bi.run_keyword('Input text', OrderForm_Locators.user_city_field, UserData.user_city)
        bi.run_keyword('Wait until element contains', OrderForm_Locators.user_city_droplist_item,
                       'Львов (Львовская обл.)')
        bi.run_keyword('Mouse over', OrderForm_Locators.user_city_droplist_item)
        bi.run_keyword('Click element', OrderForm_Locators.user_city_droplist_item)

    def check_delivery_address_is_correct(self):
        bi.run_keyword('check_preloader')
        bi.run_keyword('Textfield value should be', OrderForm_Locators.delivery_warehouse_droplist,
                       'Отделение №5 (Гетьмана Мазепы ул., 11 )')
