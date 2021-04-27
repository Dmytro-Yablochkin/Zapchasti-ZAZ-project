from robot.libraries.BuiltIn import BuiltIn

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class SearchField_Locators:
    search_field = 'css = #search_query_top'
    search_submit_btn = 'css = button.btn-search'

    search_categories = 'css = #filtrMenu'
    search_categories_form = 'css = div.form__category-item.active'
    # --------------- categories form items ---------------- #
    tavria_slavuta = 'css = div.form__category-item.active :nth-child(1) label'
    lanos_sens = 'css = div.form__category-item.active :nth-child(2) label'
    aveo = 'css = div.form__category-item.active :nth-child(3) label'
    lacetti = 'css = div.form__category-item.active :nth-child(4) label'
    oil_chemicals = 'css = div.form__category-item.active :nth-child(5) label'
    forza = 'css = div.form__category-item.active :nth-child(6) label'
    accessories = 'css = div.form__category-item.active :nth-child(7) label'
    nexia = 'css = div.form__category-item.active :nth-child(8) label'
    nubira = 'css = div.form__category-item.active :nth-child(9) label'
    matiz = 'css = div.form__category-item.active :nth-child(10) label'
    leganza = 'css = div.form__category-item.active :nth-child(11) label'
    epica = 'css = div.form__category-item.active :nth-child(12) label'
    takuma = 'css = div.form__category-item.active :nth-child(13) label'
    crous = 'css = div.form__category-item.active :nth-child(14) label'
    kaptiva = 'css = div.form__category-item.active :nth-child(15) label'
    evanda = 'css = div.form__category-item.active :nth-child(16) label'
    aveo_t_300 = 'css = div.form__category-item.active :nth-child(17) label'
    markdown = 'css = div.form__category-item.active :nth-child(18) label'


class SearchFieldFunctionality:
    # 10. Check check-box functionality
    def click_search_categories(self):
        bi.run_keyword('Wait until page contains element', SearchField_Locators.search_field)
        bi.run_keyword('Click element', SearchField_Locators.search_categories)

    def click_categories_check_boxes(self):
        bi.run_keyword('Click element', SearchField_Locators.lacetti)
        bi.run_keyword('Click element', SearchField_Locators.nubira)
        bi.run_keyword('Click element', SearchField_Locators.epica)

    def submit_search(self):
        bi.run_keyword('Click button', SearchField_Locators.search_submit_btn)

    def check_search_result_is_success(self):
        bi.run_keyword('Wait until page contains', ' 0 результатов было найдено. ')

    # 18. Check user can take search result using incorrect search data
    def input_incorrect_search_data(self):
        bi.run_keyword('Input text', SearchField_Locators.search_field, 'Рыжий пес Доберман')
