def plain_txt(msg=""):
    if msg == "":  # Checks if function was called with parameters; asks for user input otherwise.
        msg: str = input("Enter the plain text to be converted: ")
    return msg


def shift(c_shift=0):
    if c_shift == 0:  # Checks if function was called with parameters; asks for user input otherwise.
        c_shift: int = int(input("Enter the number of letter shifts: "))
    return c_shift


# A-Z - 65-90; All caps for ease of use and decryption.


def encrypt(msg: str, ltr_shift: int):
    """
    Encrypts a message using Caesar cipher, through ASCII table.
    :param msg: The plain text to be encrypted.
    :param ltr_shift: The number of shifts for the text.
    :return: Ciphered text, letters shifted; string.
    """
    cipher_txt: str = ""
    msg: str = msg.upper()  # All caps for ease of use and decryption.
    special_chars = [",", " ", ";", "?"]
    for ltr in msg:
        ltr_ord: int = ord(ltr)
        ltr_shifted: int = (ltr_ord + ltr_shift)
        if ltr in special_chars:  # If there's a special character, simply add the special character, no substitution.
            cipher_txt += ltr
        elif ltr_shifted > 90:  # If the ASCII value exceeds 'Z' == 90.
            ltr_shifted = ltr_shifted - 26  # Runs back to the start of the ABC ASCII table; the difference of Z & A.
            cipher_txt += chr(ltr_shifted)
        elif ltr != " ":
            cipher_txt += chr(ltr_shifted)
        else:
            print("Error, go check me.")
    return cipher_txt


def main():
    """
    Execution of the encryption.
    :return: Ciphered text printed.
    """
    text = "hello world, chicken invaders"
    letters_shift = 3
    print(encrypt(msg=plain_txt(text), ltr_shift=shift(letters_shift)))


if __name__ == '__main__':
    main()
