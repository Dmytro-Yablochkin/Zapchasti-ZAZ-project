from GenerateRandomData import random_email
from GenerateRandomData import random_number


class UserData:
    user_name = ''
    user_last_name = ''
    user_middle_name = ''
    user_email = ''
    user_password = ''
    user_phone_number = ''

    random_user_email = random_email
    random_phone_number = random_number

    user_city = ''
    warehouse_num = '№'

    current_num = ''

    # ----------- incorrect data -------------- #
    bad_user_email = ''
    bad_user_password = ''
