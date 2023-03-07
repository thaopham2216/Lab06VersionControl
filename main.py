def menu():
    print(
        '''
Menu
---------------
1. Encode
2. Decode
3. Quit

    ''')

def encoder(password_input):
    encoded_password = ''
    new_i = ''
    for i in password_input:
        if int(i) in range(0,7):
            new_i = int(i) + 3
        elif int(i) == 7:
            new_i = 0
        elif int(i) == 8:
            new_i = 1
        elif int(i) == 9:
            new_i = 2
        encoded_password += str(new_i)
    print(encoded_password)
    return encoded_password


# def decoder(encoded):
#     original_password = ''
#     new_element = ''
#     for element in encoded:
#
#     return original_password


if __name__ == "__main__":
    menu()
    stop_option = 0

    # get user input
    option_input = int(input("Please enter an option: "))
    password_input = input('Please enter your password to encode: ')

    while stop_option != 3:
        if option_input == 1:
            encoded = encoder(password_input)
            print("Your password has been encoded and stored!")
        elif option_input == 2:
            encoded = encoder(password_input)
            # original_pass = decoder(encoded)
            print(f'The encoded password is {encoded}, and the original password is original_pass')
        else:
            stop_option = 3

        menu()

        option_input = int(input("Please enter an option: "))
        stop_option = option_input
