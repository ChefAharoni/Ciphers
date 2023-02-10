# Explanation in The Code Book by Simon Singh; page ??; chapter - The Beale's Cipher

book_words_str = "Not surprisingly, once the author knew the value of the treasure, he spent increasing amounts of " \
                 "time analyzing the other two cipher sheets, particularly the first Beale cipher, which describes " \
                 "the treasure’s location."
agreed_words = "For example, if the sender and receiver agreed that this sentence were to be the keytext, then every" \
               "word would be numerically labeled, each number providing the basis for encryption."
PAGE_NUMBER = 74  # The page number the words were taken from; used for reference.
BOOK_NAME = "The Code Book by Simon Singh"  # Book name & author words were taken from; used for reference.
book_words_list = agreed_words.split()
num_of_words = len(book_words_list)  # 33
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_table(words: list) -> dict:
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
        # encrypt_table[word[0]] = num
        num += 1
    return encrypt_table


def check_abc(table: dict) -> list:
    """
    Checks which letters from the ABC appear.
    :param table: Dictionary of numbers and values created
    :return: List of sorted unique letters.
    """
    ltrs = list()
    for ltr in table.values():
        if ltr in ABC and ltr not in ltrs:
            ltrs.append(ltr)
    return sorted(set(ltrs))


def not_in_abc(page_ltrs: list) -> list:
    """
    Checks which letters from the ABC doesn't appear.
    :param page_ltrs: List of letters extracted from the book page.
    :return: List of sorted unique letters.
    """
    ltrs = list()  # declare an empty list.
    for ltr in ABC:
        if ltr in page_ltrs:  # to avoid double letters; re-checked when converting to set.
            continue
        ltrs.append(ltr)
    return sorted(set(ltrs))


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


def encrypt_msg(msg: str, key_table: dict) -> str:
    """
    Encrypts a message by substituting the letters as numbers from the key table.
    :param msg: Str; the message to be encrypted.
    :param key_table: Table of numbers as keys and letters as values.
    :return: String of numbers.
    """
    coded_msg = ""  # the message coded
    msg = msg.upper()  # abc table is capitalized, so matching the letter check to be capital.
    flag = 0  # num of non-empty runs; to avoid un-necessary hyphens
    for ltr in msg:  # for every letter in the text to be coded
        if flag == 0:
            # coded_msg += str(get_key(val=ltr, key_dict=key_table))  # find the letter, get its key
            coded_msg += f'{(get_key(val=ltr, key_dict=key_table)):02}'  # find the letter, get its key
            flag += 1
        elif ltr != " ":  # if the letter is not an empty space
            coded_msg += "-"
            # coded_msg += str(get_key(val=ltr, key_dict=key_table))  # find the le®tter, get its key
            coded_msg += f'{(get_key(val=ltr, key_dict=key_table)):02}'  # find the letter, get its key
            flag += 1
        elif ltr == " ":
            coded_msg += " "
            flag = 0  # once a blank is detected, resets the zero.
    return coded_msg


def write_msg_to_file(file_name: str, msg: str) -> None:
    with open(file_name, 'a') as cf:  # cf = cipher file; opened as append so former ciphers won't delete.
        cf.write(msg)
        cf.write("\n")


def main():
    key_table = create_table(book_words_list)
    print(key_table)
    ltrs_in_dict = check_abc(create_table(book_words_list))
    print(ltrs_in_dict)
    ltrs_not_in_dict = not_in_abc(ltrs_in_dict)
    print(ltrs_not_in_dict)
    msg = "beale we are lpr"
    ciphered_message = encrypt_msg(msg, key_table)
    print(ciphered_message)
    file_name = "../Text Riddles/Riddle 1"
    write_msg_to_file(file_name=file_name, msg=ciphered_message)


if __name__ == '__main__':
    main()
