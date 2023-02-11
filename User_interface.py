def get_info():
    info = []
    last_name = input('Фамилия: ')
    info.append(last_name)
    first_name = input('Имя: ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр. Вводи номер начиная с 7.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр и начинаться с 7.')
    info.append(phone_number)
    description = input('Описание: ')
    info.append(description)
    return