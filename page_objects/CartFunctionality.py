from robot.libraries.BuiltIn import BuiltIn
from CatalogueItems.ListItems import ListItems
from Itemlocators.Items import Items
from OtherFunctionality import Other_Locators

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class Cart_Locators:
    append_btn = 'css = #cart_quantity_up_13467_0_0_0'
    subtract_btn = 'css = #cart_quantity_down_13467_0_0_0'
    remove_btn = 'css = a.cart_quantity_delete'

    quantity_field = 'css = input[name="quantity_13467_0_0_0"]'

    empty_cart_warning = 'css = p.alert-warning'

    product_in_cart = 'css = #product_8127_0_0_0'

    header_cart_droplist = 'css = a.btn.btn-cart'
    droplist_delete_icon = 'css = #blockart_blockcart_lines_wrap > dl > dt > div > div.shopping-cart__item-del > a'
    droplist_block = 'css = #blockart_blockcart_lines_wrap'

class CartFunctionality:
    # 4. Append/subtract item button
    def click_markdown_btn(self):
        bi.run_keyword('element should be visible', ListItems.markdown_item)
        bi.run_keyword('Click link', ListItems.markdown_item)
        # bi.sleep(1)

    def click_rsp96226990_item_link(self):
        bi.run_keyword('Scroll element into view', Items.rsp96226990)
        bi.run_keyword('Click element', Items.rsp96226990)

    def add_current_item_to_cart(self):
        bi.run_keyword('Mouse over', Other_Locators.add_to_cart_btn)
        bi.run_keyword('Click button', Other_Locators.add_to_cart_btn)

    def click_checkout_btn(self):
        bi.run_keyword('Wait until element is visible', Other_Locators.modal_window)
        bi.run_keyword('Click element', Other_Locators.checkout_order_btn)

    def click_append_btn(self):
        bi.run_keyword('Mouse over', Cart_Locators.append_btn)
        bi.run_keyword('Click element', Cart_Locators.append_btn)
        sl.reload_page()

    def check_append_is_success(self):
        bi.run_keyword('Textfield value should be', Cart_Locators.quantity_field, 2)

    def click_subtract_btn(self):
        bi.run_keyword('Mouse over', Cart_Locators.subtract_btn)
        bi.run_keyword('Click element', Cart_Locators.subtract_btn)
        sl.reload_page()

    def check_subtract_is_success(self):
        bi.run_keyword('Textfield value should be', Cart_Locators.quantity_field, 1)

    # 5. Removing an item from the cart
    def execute_testcase_id_4(self):
        bi.run_keywords('click_markdown_btn', 'click_rsp96226990_item_link',
                        'add_current_item_to_cart', 'click_checkout_btn')

    def click_trash_icon(self):
        bi.run_keyword('Mouse over', Cart_Locators.remove_btn)
        bi.run_keyword('Click link', Cart_Locators.remove_btn)
        sl.reload_page()

    def check_remove_is_success(self):
        bi.run_keyword('Wait until page contains element', Cart_Locators.empty_cart_warning)

    # 15. Saving cart information functionality
    def check_saving_info_is_success(self):
        bi.run_keyword('click_accessories_btn')
        bi.run_keyword('click_11022_3901094_item')
        bi.run_keyword('add_current_item_to_cart')
        bi.run_keyword('click_checkout_btn')
        sl.reload_page()
        bi.run_keyword('Wait until page contains element', Cart_Locators.product_in_cart)

    # 17. Delete item from cart droplist
    def add_to_cart(self):
        bi.run_keyword('click_accessories_btn')
        bi.run_keyword('click_11022_3901094_item')
        bi.run_keyword('add_current_item_to_cart')

    def delete_from_cart_droplist(self):
        bi.run_keyword('Click link', Cart_Locators.header_cart_droplist)
        bi.run_keyword('Wait until element is visible', Cart_Locators.droplist_block)
        bi.run_keyword('Click element', Cart_Locators.droplist_delete_icon)

    def check_deleting_is_successfull(self):
        bi.run_keyword('Wait until element is not visible', Items.item_11022_3901094)