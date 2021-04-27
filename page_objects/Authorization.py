from robot.libraries.BuiltIn import BuiltIn
from Registration import Create_Locators
from UserData import UserData

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class Auth_Locators:
    email_input = 'css = #email_ajax'
    password_input = 'css = #passwd_ajax'
    submit_auth_btn = 'css = #SubmitLoginAjax'
    auth_user_success = 'css = a[href="https://zapchastizaz.com.ua/my-account"]'


class Authorization(Create_Locators, UserData):
    def user_sign_up(self):
        bi.run_keyword('redirect_to_authorization_form')
        bi.run_keyword('input_user_email')
        bi.run_keyword('input_user_password')
        bi.run_keyword('submit_authorization')
        bi.run_keyword('check_user_is_login')

    # 2. Authorization
    def redirect_to_authorization_form(self):
        sl.maximize_browser_window()
        bi.run_keyword('redirect_to_auth_form')

    def input_user_email(self):
        bi.run_keyword('Input text', Auth_Locators.email_input, UserData.user_email)

    def input_user_password(self):
        bi.run_keyword('Input password', Auth_Locators.password_input, UserData.user_password)

    def submit_authorization(self):
        bi.run_keyword('Click button', Auth_Locators.submit_auth_btn)

    def check_user_is_login(self):
        bi.run_keyword('Wait until page contains element', Auth_Locators.auth_user_success)

    # 2.1 Authorization with incorrect password
    def input_incorrect_password(self):
        bi.run_keyword('Input password', Auth_Locators.password_input, UserData.bad_user_password)

    def check_message_alert(self):
        bi.run_keyword('Wait until page contains element', Create_Locators.message_alert)

