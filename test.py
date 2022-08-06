def get_integer():
    idiot = True
    while idiot:
        number = input('Input number: ')
        try:
            number = int(number)
        except:
            pass
        else:
            idiot = False
    else:
        print('Thank you!')
    return number


print(type(get_integer()))
