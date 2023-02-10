with open("../Sources/DeclarationEngl.txt", 'r') as f:
    dec_txt = f.read().lower()


def encrypt_word(file_txt: str, words: list):
    """
    Encrypts a word from a list of words using a txt file data.
    :param file_txt: .read of a txt file.
    :param words: List of words to encrypt.
    :return: A dictionary of words as keys and their location in the txt file as values.
    """
    import re  # regex = regular expressions module
    words_locs = dict()  # define an empty dictionary
    file_txt = re.split(r'[\[\],;\)\)\" ]', file_txt)  # splits the file's text with special chars
    for i in file_txt:
        if i == "" or i == "-":  # removes element if element is a space or stand-alone hyphen.
            file_txt.remove(i)
    # print(file_txt)  # to see how the program splits the text
    for word in words:
        word = word.lower()
        try:
            wrd_loc = file_txt.index(word)+1  # adds 1 so it won't start from 0
        except ValueError:
            continue
        words_locs[word] = f'{wrd_loc:03}'
    return words_locs


str_to_encrypt = ""
print(encrypt_word(dec_txt, str_to_encrypt.split()))
