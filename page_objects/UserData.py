from GenerateRandomData import random_email
from GenerateRandomData import random_number


class UserData:
    user_name = 'Дмитрий'
    user_last_name = 'Яблочкин'
    user_middle_name = 'Валентинович'
    user_email = 'Ramennewlife1994@gmail.com'
    user_password = '1605f1994'
    user_phone_number = '0632083449'

    random_user_email = random_email
    random_phone_number = random_number

    user_city = 'Льв'
    warehouse_num = '№67'

    current_num = '+38 (063) 208-34-49'

    # ----------- incorrect data -------------- #
    bad_user_email = '12345678910'
    bad_user_password = '11111111'
