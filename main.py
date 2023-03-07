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
    # print(encoded_password)
    return encoded_password


def decoder(encode):
    # Creates an empty decoded password string.
    decoded_password = ''
    for char in encode:
        # Converts character to an integer.
        char = int(char)
        # Shifts integer back by three.
        char -= 3
        # Accounts for circumstances when decoding produces a negative number.
        if char == -1:
            char = 9
        elif char == -2:
            char = 8
        elif char == -3:
            char = 7
        # Converts the character back into a string
        char = str(char)
        # Adds each character to decoded password.
        decoded_password += char
    return decoded_password



if __name__ == '__main__':

    # Loop to run options
    stop = 0
    while stop != 3:
        # print menu
        menu()

        # get input
        option_input = int(input('Please enter an option: '))
        if option_input == 3:
            break

        # if loop for option_input
        encode = ''
        original_password = ''
        if option_input == 1:
            password_input = input('Please enter your password to encode: ')
            encode = encoder(password_input)
            print('Your password has been encoded and stored')
        elif option_input == 2:
            encode = encoder(password_input)
            original_password = decoder(encode)
            print(f"The encoded password is {encode}, and the original password is {original_password}.")
        else:
            stop = option_input

