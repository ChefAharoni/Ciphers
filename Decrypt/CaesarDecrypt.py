def cipher_txt(msg=""):
    if msg == "":  # Checks if function was called with parameters; asks for user input otherwise.
        msg: str = input("Enter the plain text to be converted: ")
    return msg


def shift(c_shift=0):
    if c_shift == 0:  # Checks if function was called with parameters; asks for user input otherwise.
        c_shift: int = int(input("Enter the number of letter shifts: "))
    return c_shift


# A-Z - 65-90; All caps for ease of use and decryption.


def decrypt(enc_msg: str, ltr_shift: int):
    """
    Decrypts a message using Caesar cipher, through ASCII table.
    :param enc_msg: The cipher text to be decrypted.
    :param ltr_shift: The number of shifts for the text.
    :return: plain text, letters shifted; string.
    """
    plain_txt: str = ""
    enc_msg: str = enc_msg.upper()  # All caps for ease of use and decryption.
    for ltr in enc_msg:
        special_chars = [",", " ", ";", "?"]
        ltr_ord: int = ord(ltr)
        ltr_shifted: int = (ltr_ord - ltr_shift)
        if ltr in special_chars:  # If there's a special character, simply add the special character, no substitution.
            plain_txt += ltr
        elif ltr_shifted < 65:  # If the ASCII value exceeds 'A' == 65.
            ltr_shifted = ltr_shifted + 26  # Runs back to the start of the ABC ASCII table; the difference of Z & A.
            plain_txt += chr(ltr_shifted)
        elif ltr != " ":
            plain_txt += chr(ltr_shifted)
    return plain_txt


def main():
    """
    Execution of the encryption.
    :return: Ciphered text printed.
    """
    text = "KHOOR ZRUOG, FKLFNHQ LQYDGHUV"
    letters_shift = 3
    print(decrypt(enc_msg=cipher_txt(text), ltr_shift=shift(letters_shift)))


if __name__ == '__main__':
    main()
