from robot.libraries.BuiltIn import BuiltIn
from UserData import UserData

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class Create_Locators:
    login_link = 'css = span.link-login'

    registration_form = 'css = #ajaxFormLogin'
    email_create_input = 'css = #email_create_ajax'

    submit_create_btn = 'css = #SubmitCreateAjax'

    message_alert = 'css = span.error'


# 1. Customer registration
class Registration:
    def redirect_to_auth_form(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click element', Create_Locators.login_link)
        bi.run_keyword('Wait until element is visible', Create_Locators.registration_form)

    def create_account(self):
        bi.run_keyword('redirect_to_auth_form')
        bi.run_keyword('Input text', Create_Locators.email_create_input, UserData.user_email)
        bi.run_keyword('Click button', Create_Locators.submit_create_btn)
        bi.run_keyword('Wait until page contains element', Create_Locators.message_alert)

    def bad_create_account(self):
        bi.run_keyword('redirect_to_auth_form')
        bi.run_keyword('Input text', Create_Locators.email_create_input, UserData.bad_user_email)
        bi.run_keyword('Click button', Create_Locators.submit_create_btn)
        bi.run_keyword('Wait until page contains element', Create_Locators.message_alert)
