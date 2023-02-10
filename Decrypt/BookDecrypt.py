from Sources import Formats as fr  # Class of colors and bold for strings.

agreed_words = "For example, if the sender and receiver agreed that this sentence were to be the keytext, then every" \
               "word would be numerically labeled, each number providing the basis for encryption."
PAGE_NUMBER = 74  # The page number the words were taken from; used for reference.
BOOK_NAME = "The Code Book by Simon Singh"  # Book name & author words were taken from; used for reference.
book_words_list = agreed_words.split()
# num_of_words = len(book_words_list)  # 30
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_table(words: list):
    """
    Creates a dictionary of numbers as keys and letters as values for every first letter from each word in the list of
    words from the page book; each number represent the location of the word in the words list.
    :param words: List of words from the page book.
    :return: Dictionary with numbers as keys and letters as values.
    """
    encrypt_table = dict()
    num = 1
    for word in words:
        word = word.upper()
        encrypt_table[num] = word[0]  # first letter of word
        num += 1
    return encrypt_table


def get_key(val: str, key_dict: dict):
    """
    Gets the key from a dictionary based on a value.
    :param val: value to search
    :param key_dict: dictionary to search from
    :return: the key associated with the value
    """
    for key, value in key_dict.items():
        if val == value:  # if the requested value equals to the value in the table -
            return key  # - return the associated key.
    return 0


def decrypt_msg(enc_msg: str, key_table: dict):
    """
    Decrypts a message by substituting the letters as numbers from the key table.
    :param enc_msg: Str; the message to be decrypted.
    :param key_table: Table of numbers as keys and letters as values.
    :return: Decoded message from the book.
    """
    import re  # regex - regular expressions.
    plain_txt = ""
    enc_msg = re.split(r'-', enc_msg)  # to put several splits, enter brackets.
    print(enc_msg)
    digit_flag = 0
    for digit in enc_msg:
        flag_space = 0
        this_digit = ""
        if " " in digit:
            for j in digit:
                if j != " ":  # if the digit isn't a space
                    this_digit += j
                elif j == " ":  # when done concatenating the digits
                    plain_txt += key_table.get(int(this_digit), " ")
                    plain_txt += " "
                    flag_space = 1
                    this_digit = ""
                if flag_space == 1 and len(this_digit) > 1:
                    plain_txt += key_table.get(int(this_digit), " ")
        elif digit[0] == '0':  # since encrypted text comes with zero padding, they need to be ignored.
            plain_txt += key_table.get(int(digit[1]), " ")
            # the line above adds the next digit after zero; we know there is no more than one zero padded.
        else:
            plain_txt += key_table.get(int(digit), " ")
        digit_flag += 1
    return plain_txt


def get_cipher_from_file(file_name: str):
    """
    Decodes a coded message from a text file.
    :param file_name: File name to be extracted from
    :return: PRINTS the decoded message, line by line.
    """
    solved_text = list()
    with open(file_name, 'r') as cf:  # cf = cipher file; opened for read only
        for line in cf:
            # print(line)
            solved_text.append(shortcut_decrypt(enc_msg=line))

    print("The decrypted message is: ")
    print("---------------------------------")
    for item in solved_text:
        print("  > " + item)


def shortcut_decrypt(enc_msg: str):
    """
    Fast method to decrypt the message; used for line reading function.
    :param enc_msg: Encrypted message to be deciphered.
    :return: Formatter decoded message.
    """
    key_table = create_table(book_words_list)  # Creates the key table from the book words.
    return fr.Colors.BOLD + fr.Colors.RED + \
        decrypt_msg(enc_msg=enc_msg, key_table=key_table) + fr.Colors.END
    # Result is formatted in bold and red; taken from an outside class.


def main():
    key_table = create_table(book_words_list)  # Creates the key table from the book words.
    print(key_table)
    enc_msg = "14-02-06-22-02 02-21-25 01-04-12 03-16-07"
    print("The decrypted message is:", fr.Colors.BOLD + fr.Colors.RED + \
          decrypt_msg(enc_msg=enc_msg, key_table=key_table) + fr.Colors.END)


if __name__ == '__main__':
    get_cipher_from_file(file_name="../Text Riddles/Riddle 1")
