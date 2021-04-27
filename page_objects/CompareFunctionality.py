from robot.libraries.BuiltIn import BuiltIn
from CatalogueItems.ListItems import ListItems
from Itemlocators.Items import Items

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class Compare_Locators:
    add_to_compare_btn = 'css = div.g-cart.row > div > div > div:nth-child(1)' \
                         ' > div > div > div.b-goods__compare-wrap > a'
    submit_compare_btn = 'css = button.btn.bt_compare_header.btn-compare.bt_compare'
    delete_from_compare_btn1 = 'css = div.remove a[data-id-product="8833"]'
    delete_from_compare_btn2 = 'css = div.remove a[data-id-product="9999"]'
    close_btn = 'css = .fancybox-overlay-fixed > div > div > a'

    compare_info_pop_up = 'css = p.fancybox-error'
    add_to_compare_msg = 'Товар добавлен к сравнению'
    delete_from_compare_msg = 'Товар удален из сравнения'

    item_553339_compare_icon = 'css = div:nth-child(4) > div > div.b-goods__footer > ' \
                               'div.b-goods__compare-wrap > a '
    item_pjc_051_compare_icon = 'css = div:nth-child(6) > div > div.b-goods__footer > div.b-goods__compare-wrap > a'
    # -------------------------- compare result locators ---------------------- #
    compare_is_success = 'css = #center_column > div > div.products_block.table-responsive'


class CompareFunctionality:
    # 6. Compare adding items pop-up
    def hover_takuma_list_item(self):
        bi.run_keyword('Mouse over', ListItems.takuma_item)

    def click_takuma_chassis_item(self):
        bi.run_keyword('Wait until element is visible', ListItems.takuma_chassis_sub_item)
        bi.run_keyword('Click link', ListItems.takuma_chassis_sub_item)

    def click_553339_item(self):
        bi.run_keyword('Scroll element into view', Items.item_553339)
        bi.run_keyword('Click element', Items.item_553339)

    def click_add_to_compare_btn(self):
        bi.run_keyword('Mouse over', Compare_Locators.add_to_compare_btn)
        bi.run_keyword('Click link', Compare_Locators.add_to_compare_btn)

    def check_add_to_compare_is_success(self):
        bi.run_keyword('Wait until page contains element', Compare_Locators.compare_info_pop_up)
        bi.run_keyword('Wait until element contains', Compare_Locators.compare_info_pop_up,
                       Compare_Locators.add_to_compare_msg)

    def close_compare_pop_up(self):
        bi.run_keyword('Wait until element is visible', Compare_Locators.close_btn)
        bi.run_keyword('Click link', Compare_Locators.close_btn)

    def check_delete_from_compare_is_success(self):
        bi.run_keyword('Wait until page contains element', Compare_Locators.compare_info_pop_up)
        bi.run_keyword('Wait until element contains', Compare_Locators.compare_info_pop_up,
                       Compare_Locators.delete_from_compare_msg)

    # 8. Compare adding items pop-up
    def click_lt_555_item(self):
        bi.run_keyword('Scroll element into view', Items.item_LT555)
        bi.run_keyword('Click element', Items.item_LT555)

    # 9. Compare different categories
    def add_to_compare_553339_item(self):
        bi.run_keyword('Mouse over', Items.item_553339)
        bi.run_keyword('Wait until element is visible', Compare_Locators.item_553339_compare_icon)
        bi.run_keyword('Click link', Compare_Locators.item_553339_compare_icon)

    def add_to_compare_PJC_051(self):
        bi.run_keyword('Scroll element into view', Items.item_PJC_051)
        bi.run_keyword('Wait until element is visible', Compare_Locators.item_pjc_051_compare_icon)
        bi.run_keyword('Click link', Compare_Locators.item_pjc_051_compare_icon)

    def submit_compare(self):
        bi.run_keyword('Mouse over', Compare_Locators.submit_compare_btn)
        bi.run_keyword('Click button', Compare_Locators.submit_compare_btn)

    def check_compare_is_success(self):
        bi.run_keyword('Wait until page contains element', Compare_Locators.compare_is_success)

    # 11. Compare items delete
    def execute_testcase_id_9(self):
        bi.run_keyword('hover_takuma_list_item')
        bi.run_keyword('click_takuma_chassis_item')
        bi.run_keyword('add_to_compare_553339_item')
        bi.run_keyword('check_add_to_compare_is_success')
        bi.run_keyword('close_compare_pop_up')
        bi.run_keyword('add_to_compare_PJC_051')
        bi.run_keyword('check_add_to_compare_is_success')
        bi.run_keyword('close_compare_pop_up')
        bi.run_keyword('submit_compare')
        bi.run_keyword('check_compare_is_success')

    def delete_item_from_compare(self):
        bi.run_keyword('Mouse over', Compare_Locators.delete_from_compare_btn1)
        bi.run_keyword('Click link', Compare_Locators.delete_from_compare_btn1)
        bi.run_keyword('Mouse over', Compare_Locators.delete_from_compare_btn2)
        bi.run_keyword('Click link', Compare_Locators.delete_from_compare_btn2)

    def check_deleting_is_success(self):
        bi.run_keyword('Wait until element is not visible', Items.item_553339)
        bi.run_keyword('Wait until element is not visible', Items.item_PJC_051)
