from robot.libraries.BuiltIn import BuiltIn
from CatalogueItems.ListItems import ListItems
from Itemlocators.Items import Items
from HeaderNavigation import HeaderNavigation

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class Other_Locators:
    add_to_cart_btn = 'css = #add_to_cart_submit'
    checkout_order_btn = 'css = div.layer-cart a.btn--order'

    close_sign = 'css = #layer_cart span.cross'

    modal_window = 'css = #layer_cart'

    contact_page = 'Контакты - телефоны, график работы, карта проезда'

    preloader = 'css = .blockloadicon'


class OtherFunctionality(ListItems, Items):
    # 3. Add items modal window
    def click_accessories_btn(self):
        bi.run_keyword('Click link', ListItems.accessories_item)

    def click_iz04_item(self):
        bi.run_keyword('Scroll element into view', Items.iz_04)
        bi.run_keyword('Click element', Items.iz_04)

    def add_iz04_in_cart(self):
        bi.run_keyword('Mouse over', Other_Locators.add_to_cart_btn)
        bi.run_keyword('Click button', Other_Locators.add_to_cart_btn)

    def close_modal_window(self):
        bi.run_keyword('Wait until element is visible', Other_Locators.modal_window)
        bi.run_keyword('Wait until element is visible', Other_Locators.close_sign)
        bi.run_keyword('Click element', Other_Locators.close_sign)

    # 12. Catalogue subcategories
    def check_redirect_is_success(self):
        bi.run_keyword('Wait until page contains', 'Ходовая на Chevrolet Tacuma (Шевроле Такума)')

    # 16. Check user can navigate to Contacts page
    def click_header_contacts(self):
        bi.run_keyword('Click element', HeaderNavigation.contacts)

    def check_contact_page_redirecting_is_success(self):
        bi.run_keyword('Wait until page contains', Other_Locators.contact_page)

    def check_preloader(self):
        bi.run_keyword('Wait until element is visible', Other_Locators.preloader)
        bi.run_keyword('Wait until element is not visible', Other_Locators.preloader)
