import json
import inflect  # for converting numerical numbers to 1st, 2nd, 3rd, etc..

"""PTK HIA Cryptogram Riddle, from the Play theme for 2022-2023; p.34 
Solve this cryptogram to help you identify and evaluate potential sources. 
Read “Identifying and Evaluating Sources” (page 29) for valuable hints. 
What characteristics should you look for to determine whether a source is academic?"""

with open('Cryptogram.json', 'r') as cryp_read_f:
    g_cryptogram = json.load(cryp_read_f)
WORDS_CRYPTOGRAM_SUM = [len(word) for word in g_cryptogram[1::2]]  # Sum of the words: [5, 6, 3, 4, 3, 9, 6, 8, 3, 11]


def reset_decoder() -> None:
    """
    Creates or resets a Dictionary with the ABC as keys and None as values.
    Use this function with CAUTION, as it will ERASE your json file.
    # :return: Dict of ABC's as keys and None as values.
    """
    decoder = {chr(ltr): "0" for ltr in range(65, 91)}  # Dict comprehension from ASCII values
    with open('Decoder.json', 'w') as dec_w_f:
        json.dump(decoder, dec_w_f, indent=2)
    # print(decoder)
    # return decoder


def get_decoder() -> dict:
    """
    Reads the recorder data from the json file and returns it as a dict.
    :return: Returns a dictionary with the Decoder information.
    """
    with open('Decoder.json', 'r') as dec_r_f:
        decoder = json.load(dec_r_f)
    return decoder


def update_decoder(ltr: str, val: str) -> None:
    """
    Updates the data of the recorder dictionary for each letter and its numeric value.
    :param ltr: The letter (key) to be updated.
    :param val: The value of the letter to be updated.
    """
    ltr = ltr.upper()
    with open('Decoder.json', 'r') as dec_r_f:
        decoder = json.load(dec_r_f)
    with open('Decoder.json', 'w') as dec_w_f:
        decoder[ltr] = val
        json.dump(decoder, dec_w_f, indent=2)


def get_cryptogram() -> dict:
    with open('Cryptogram.json', 'r') as cryp_r_f:
        cryptogram = json.load(cryp_r_f)
    return cryptogram


def reset_cryptogram() -> None:
    """
    Resets the cryptogram to the default empty slots for each letter position.
    """
    cryptogram = ["First Word", [{16: None}, {26: None}, {21: None}, {13: None}, {8: None}],
                  "Second Word", [{13: None}, {14: None}, {19: None}, {21: None}, {11: None}, {22: None}],
                  "Third Word", [{16: None}, {6: None}, {21: None}],
                  "Fourth Word", [{8: None}, {10: None}, {1: None}, {14: None}],
                  "Fifth Word", [{19: None}, {7: None}, {23: None}],
                  "Sixth Word", [{21: None}, {14: None}, {9: None}, {14: None}, {3: None}, {19: None}, {7: None},
                                 {11: None}, {10: None}],
                  "Seventh Word", [{13: None}, {14: None}, {11: None}, {6: None}, {7: None}, {23: None}],
                  "Eighth Word", [{11: None}, {12: None}, {21: None}, {21: None}, {14: None}, {7: None}, {11: None},
                                  {10: None}],
                  "Ninth Word", [{19: None}, {7: None}, {23: None}],
                  "Tenth Word", [{11: None}, {21: None}, {14: None}, {23: None}, {26: None}, {24: None}, {26: None},
                                 {9: None}, {26: None}, {8: None}, {10: None}]]
    with open('Cryptogram.json', 'w') as cryp_w_f:
        json.dump(cryptogram, cryp_w_f, indent=1)


def update_cryptogram(decoder: dict, mode: str):
    """
    Updates the cryptogram according to the letters' values in the decoder.
    """
    with open('Cryptogram.json', 'r') as cryp_r_f:
        cryptogram = json.load(cryp_r_f)
    for word in cryptogram[1::2]:  # Skips the title in every element (side note: maybe the title is useless?)
        for i in word:  # For every dict with num and its value.
            for k, v in i.items():  # For num and its value in the dict
                for key, val in decoder.items():
                    if k == val:
                        i[k] = key  # Update the cryptogram dict value to the corresponding letter from the Decoder.
                    elif k == 0:  # If value isn't correct, update to None again.
                        i[k] = None
    if mode == "JSON":
        with open('Cryptogram.json', 'w') as cryp_w_f:
            json.dump(cryptogram, cryp_w_f, indent=1)
    elif mode == "Manual":
        return cryptogram


def crypt_print(mode: str, crypt_dict: dict) -> None:  # Check later with internet if I can make a variable optional.
    """
    Prints the Cryptogram in a clean way with underscores for missing letters (None).
    """
    flag = 0  # For special characters used specifically in this riddle
    if mode == "JSON":
        with open('Cryptogram.json', 'r') as cryp_r_f:
            cryptogram = json.load(cryp_r_f)
    elif mode == "Manual":
        cryptogram = crypt_dict
    print("\n-------------------------------------------------------------------\n")
    for word in cryptogram[1::2]:
        for i in word:
            for k, v in i.items():
                if v is None:
                    print("_", end="")
                else:
                    print(v, end="")
        if flag == 0:
            print(", ", end="")
        elif flag == 5:
            print("; ", end="")
        elif flag == 6:
            print(", ", end="")
        else:
            print(" ", end="")
        flag += 1
    print("\n-------------------------------------------------------------------")


def word_ltrs_sum(final_pos: str) -> int:
    """
    Sums the amount of letters in a corresponding word.
    """
    word_pos, corresponding_elem = check_word_pos(final_pos)
    ltrs_count = len(corresponding_elem)
    print(f'The sum of the {word_pos} is {ltrs_count} letters.')
    # print(corresponding_elem)  # delete me, used for testing
    return ltrs_count


def check_word_pos(final_pos: str):
    """
    Checks the location of a word from the corresponding location given.
    """
    word_pos = None
    corresponding_elem = None
    with open('Cryptogram.json', 'r') as cryp_r_f:
        cryptogram = json.load(cryp_r_f)
    for i in range(len(cryptogram)):
        if final_pos in cryptogram[i]:
            word_pos = cryptogram[i]  # First/Second/Third/etc.. word
            corresponding_elem = cryptogram[i + 1]
    if word_pos is None or corresponding_elem is None:  # If no such position exists.
        raise ValueError
    return word_pos, corresponding_elem


def guess_word(final_pos: str, ltrs_count: int, mode: str, word_guess=""):
    """
    Using a guessed input for a certain word, replaces the empty letters with guessed letters.
    Takes the guessed letter in place of the value, and checks its value across all other letters; meaning that if
    the first word has five spaces with the following values: 15, 23, 25, 16, 15, and the guessed input is A, B, C, D, E
    then it will assign 15 to A, 23 to B, etc.. and will place them for each time they occur over the words.
    :param final_pos: The position of the word in the Cryptogram; first/second/third...
    :param ltrs_count: The amount of letters in the checked word. i.e. first word has five letters, then 5 is the num.
    :param mode: Auto = no user input; Manual = user enters word guess.
    :param word_guess: If Auto mode, enter the word to be checked; otherwise user will be prompted.
    """
    mode = mode.title()
    word_pos, corresponding_elem = check_word_pos(final_pos)
    if mode == "Manual":
        word_guess = input("Enter a guess for the word: ")
    if len(word_guess) != ltrs_count and mode == "Manual":
        print("Sorry, there are different number of letters for the word you've chosen.")
        print(f'You have ')
    else:
        with open('Decoder.json', 'r') as dec_r_f:  # Won't update the file, but will manipulate the dict temporarily.
            temp_decoder = json.load(dec_r_f)
        j = 0  # represents the letters in user_guess
        guessed_word_w_nums = {}
        for i in corresponding_elem:
            for k, v in i.items():
                # k = corresponding ltr number of cryptogram
                guessed_word_w_nums[k] = word_guess[j].upper()  # This dict is a guesses Cryptogram
            j += 1
        for val, ltr in guessed_word_w_nums.items():
            temp_decoder[ltr] = val

        if mode == "Manual":
            print(guessed_word_w_nums)
            print(temp_decoder)

        if mode == "Manual":
            new_cryptogram = update_cryptogram(decoder=temp_decoder, mode="Manual")
            crypt_print(mode="Manual", crypt_dict=new_cryptogram)
        elif mode == "Auto":
            new_cryptogram = update_cryptogram(decoder=temp_decoder, mode="Manual")
            # print(new_cryptogram)  # Count only lists with 50% (maybe more)
            result = count_results(new_cryptogram)  # Should it be printed or not?
            if result:  # If result == True
                crypt_print(mode="Manual", crypt_dict=new_cryptogram)


def count_results(modified_cryptogram: list):
    """
    Counts the amount of None in result: if less than 50% --> returns True, suggesting to print it.
    :param modified_cryptogram: Cryptogram NOT from the json file.
    """
    reg_ltrs = 0
    none_ltrs = 0
    for word in modified_cryptogram[1::2]:
        for i in word:
            for v in i.values():
                if v is None:
                    none_ltrs += 1
                else:
                    reg_ltrs += 1
    total_ltrs = reg_ltrs + none_ltrs
    percent_none = none_ltrs/total_ltrs
    if percent_none < .5:
        return True


def select_pos() -> str:
    """
    Prompts the user to check for which word he would like to guess a word.
    """
    print("There are a total of x words in the cryptogram. ")  # replace x with num of words;
    # print here options for words based on numerical numbering: 1st, second, etc..
    print("Which word would you like to guess? \nEnter the number or the wording (1 / first)")
    pos = input(">>> ")
    return pos.title()


def determine_pos(pos: str):
    """
    Is there a way to make this less personal? Because if we had a different problem with different number of words,
    we would have to change this function, which seems not very computer-science efficient.
    """
    match pos:
        case "1" | "1st" | "first":
            return "First"
        case "2" | "2nd" | "second":
            return "Second"
        case "3" | "3rd" | "third":
            return "Third"
        case "4" | "4th" | "fourth":
            return "Fourth"
        case "5" | "5th" | "fifth":
            return "Fifth"
        case "6" | "6th" | "sixth":
            return "Sixth"
        case "7" | "7th" | "seventh":
            return "Seventh"
        case "8" | "8th" | "eighth":
            return "Eighth"
        case "9" | "9th" | "ninth":
            return "Ninth"
        case "10" | "10th" | "tenth":
            return "Tenth"

        case default:
            return pos


def choose_mode():
    """
    For later - choose the mode for the update Cryptogram (and maybe Decoder?) - either JSON file or manual dict.
    """
    pass


def search_text(f_name: str, req_length: int) -> list:
    with open(f_name, 'r') as par_f:
        paragraph = par_f.read()
    par_words = paragraph.split(' ')
    possible_words = []
    for word in par_words:
        if len(word) == req_length:
            possible_words.append(word)
    return possible_words


def auto_checker(possible_words: list):
    """
    Runs the checking automatically for every word in the paragraph and in the Cryptogram.
    """
    nums = [str(i) for i in range(1, 11)]  # List of nums from 1 to 10 (incl), representing the words in the Cryptogram.
    for i in range(len(possible_words)):  # for each word in the possible words list
        for j in nums:  # representing each word position, so it can run them all.
            fixed_pos = determine_pos(j)  # Converts number to verbal (1 -> First)
            for wrd_length in WORDS_CRYPTOGRAM_SUM:  # For each word length possible
                guess_word(final_pos=fixed_pos, ltrs_count=wrd_length, mode="Auto", word_guess=possible_words[i])


def main():
    print("")
    reset_cryptogram()
    # update_decoder("B", "0")
    # decoder = get_decoder()
    # update_cryptogram(decoder=decoder, mode="JSON")

    paragraph = search_text('Page29.txt', 11)
    # auto_checker(paragraph)
    word_pos = select_pos()  # switch to select pos later
    # determine_pos ???
    guess_word(word_pos, word_ltrs_sum(word_pos), mode="Manual")

    # word_ltrs_sum(word_pos)
    # print(get_cryptogram())
    # crypt_print(mode="JSON", crypt_dict={})

    # UN_IEISITY


if __name__ == "__main__":
    main()
