from Sources import Formats as fr


def shift_table(ab: str):  # Language option? need to get ASCII values changes as well.
    ab_size: int = len(ab)  # numbers of letters in the given alphabet.
    ab_shifted = dict()
    for i in range(ab_size+1):  # zero represent the complete ABC, with no shifts.
        shifted_seq = ""
        for ltr in ab:
            ltr_ord: int= ord(ltr)
            ltr_shifted: int = (ltr_ord + i)
            if ltr_shifted > 90:  # If the ASCII value exceeds 'Z' == 90.
                ltr_shifted = ltr_shifted - 26  # Runs back to the start of the ABC ASCII table; the difference of Z&A.
                shifted_seq += chr(ltr_shifted)  # seq = sequence
            else:
                shifted_seq += chr(ltr_shifted)  # seq = sequence
        ab_shifted[i] = shifted_seq
    return ab_shifted


ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SHIFTED_TABLE = shift_table(ab=ABC)  # Used many times in various functions, table doesn't change in the program.


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


def get_rows(keyword: str):
    """
    Finds the row of each word in the keyword.
    :param keyword: Keyword to be searched
    :return: A dictionary of letter of keyword letter as a key and its row number as value.
    """
    keyword = keyword.upper()
    keyword_row = dict()
    for ltr in keyword:
        for shift, val in SHIFTED_TABLE.items():
            # print(val[0])
            if ltr == val[0]:
                row = get_key(val=val, key_dict=SHIFTED_TABLE)
                keyword_row[ltr] = row
    return keyword_row


def get_columns(plain_txt: str):
    """
    Finds the column of each word in the plain text
    :param plain_txt: Plain txt to be searched
    :return: A dictionary of letter of plain text letter as a key and its column number as value.
    """
    plain_txt = plain_txt.upper()
    plain_txt_ltrs = [val for val in SHIFTED_TABLE[0]]  # splits the val into a list so the location can be found.
    keywrd_loc = dict()
    for ltr in plain_txt:
        for val in plain_txt_ltrs:
            if ltr == val:  # matches the letter of the keyword with the location of the letter using .index
                keywrd_loc[ltr] = plain_txt_ltrs.index(ltr)+1  # +1 so first ltr would be 1 and not 0.
    return keywrd_loc


def clean_message(msg: str):
    clean_msg = ""  # message without spaces so keyword length will match
    for ltr in msg:
        if ltr == " ":
            continue
        else:
            clean_msg += ltr
    return clean_msg


def duplicate_keyword(keyword: str, msg: str):
    dup_keyword = ""  # duplicated keyword; copies the keyword the same size as the msg.
    clean_msg = clean_message(msg)
    while len(dup_keyword) != len(clean_msg):  # the duplication process
        for i in range(len(keyword)):
            if len(clean_msg) == len(dup_keyword):
                break
            else:
                dup_keyword += keyword[i]
    return dup_keyword


def encrypt(msg: str, keyword: str):
    """
    Encrypts a plain message using the Vigenére message.
    :param msg: Plain message to be encrypted
    :param keyword: Keyword to be encrypted from.
    :return:
    """
    keyword = keyword.upper()
    coded_msg = ""
    msg = msg.upper()
    # clean_msg = clean_message(msg)
    dup_keyword = duplicate_keyword(keyword=keyword, msg=msg)
    ltrs_columns = get_columns(msg)
    keyword_rows = get_rows(keyword)
    special_chars = [",", " ", ";", "?"]  # to be ignored during encryption
    ltr_iter = 0
    for ltr in msg:
        if ltr in special_chars:  # If there's a special character, simply add the special character, no substitution.
            coded_msg += ltr
        else:  # if the ltr is a regular letter == anything but a special character
            ltr_column = ltrs_columns.get(ltr)  # get the column of the plain text letter
            keyword_row = keyword_rows.get(dup_keyword[ltr_iter])  # get the row of keyword letter
            coded_msg += SHIFTED_TABLE[keyword_row][ltr_column-1]  # add to coded msg the letter matching both above
            # why is ltr_column -1 though? I need to figure out.
            ltr_iter += 1  # each time ltr is not a zero - the iteration is increased by 1; counting only the ltrs.
    return coded_msg


def letters_columns(msg: str):
    """
    Gets the columns of message letters.
    :param msg: Message to be encrypted
    :return: List of letters and its columns.
    """
    clean_msg = clean_message(msg)  # deletes spaces in message
    ltrs_columns = get_columns(clean_msg)
    return ltrs_columns


# def keyword_rows(keyword: str):
#     keyword_rows = get_rows(keyword)


def print_table(msg: str, keyword: str):
    ltrs_columns = letters_columns(msg)  # dict
    keyword_rows = get_rows(keyword)  # dict
    print(fr.Colors.BOLD + "Plain  |  " + fr.Colors.END, end="")
    for ltr in SHIFTED_TABLE[0]:  # Prints in bold the plain text == first letters before shifting.
        print(fr.Colors.BOLD + ltr + fr.Colors.END, end=" ")
    print()  # Prints newline for format wise.
    for shift, shifted_ab in SHIFTED_TABLE.items():
        if shift == 0:
            continue
        if shift in keyword_rows.values():
            print("  " + fr.Colors.GREEN + f'{shift:02}' + "   | " + fr.Colors.END, end=" ")
        else:
            print("  " + f'{shift:02}' + "   | ", end=" ")  # I need to center the shift, but can't format two vars.
        ltr_pos = 0
        for ltr in shifted_ab:
            if shift in keyword_rows.values():
                if ltr_pos == 0:
                    print(fr.Colors.YELLOW + fr.Colors.BOLD + ltr[0] + fr.Colors.END, end=" ")
                # write an if statement so it won't print the first letter twice.
                print(fr.Colors.YELLOW + ltr + fr.Colors.END, end=" ")
                ltr_pos += 1
            else:
                print(ltr, end=" ")
        print()  # Prints newline for format wise.


def test():
    vig_keyword = "King"
    plain_text = "The Sun and the Man in the Moon"
    print_table(msg=plain_text, keyword=vig_keyword)
    print(get_rows(keyword=vig_keyword))
    print(get_columns(plain_txt=plain_text))
    print(encrypt(msg=plain_text, keyword=vig_keyword))


if __name__ == '__main__':
    test()
