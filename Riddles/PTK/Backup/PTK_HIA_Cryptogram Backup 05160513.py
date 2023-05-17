import json


def reset_decoder() -> None:
    """
    Creates or resets a Dictionary with the ABC as keys and None as values.
    Use this function with CAUTION, as it will ERASE your json file.
    # :return: Dict of ABC's as keys and None as values.
    """
    decoder = {chr(ltr): "0" for ltr in range(65, 91)}  # Dict comprehension from ASCII values
    with open('../Decoder.json', 'w') as dec_w_f:
        json.dump(decoder, dec_w_f, indent=2)
    # print(decoder)
    # return decoder


def get_decoder() -> dict:
    """
    Reads the recorder data from the json file and returns it as a dict.
    :return: Returns a dictionary with the Decoder information.
    """
    with open('../Decoder.json', 'r') as dec_r_f:
        decoder = json.load(dec_r_f)
    return decoder


def update_decoder(ltr: str, val: str) -> None:
    """
    Updates the data of the recorder dictionary for each letter and its numeric value.
    :param ltr: The letter (key) to be updated.
    :param val: The value of the letter to be updated.
    """
    ltr = ltr.upper()
    # val = int(val)
    with open('../Decoder.json', 'r') as dec_r_f:
        decoder = json.load(dec_r_f)
    with open('../Decoder.json', 'w') as dec_w_f:
        decoder[ltr] = val
        json.dump(decoder, dec_w_f, indent=2)


def get_cryptogram() -> dict:
    with open('../Cryptogram.json', 'r') as cryp_r_f:
        cryptogram = json.load(cryp_r_f)
    return cryptogram


def reset_cryptogram() -> None:
    cryptogram = {"First word: ": {16: None, 26: None, 21: None, 13: None, 8: None},
                  "Second word: ": {13: None, 14: None, 19: None, 21: None, 11: None, 22: None},
                  "Third word: ": {16: None, 6: None, 21: None},
                  "Fourth word: ": {8: None, 10: None, 1: None, 14: None},
                  "Fifth word: ": {19: None, 7: None, 23: None},
                  "Sixth word: ": {21: None, 14: None, 9: None, 14: None, 3: None, 19: None, 7: None, 11: None, 10: None},
                  "Seventh word: ": {13: None, 14: None, 11: None, 6: None, 7: None, 23: None}}
    with open('../Cryptogram.json', 'w') as cryp_w_f:
        json.dump(cryptogram, cryp_w_f, indent=1)


def update_cryptogram(decoder: dict):
    with open('../Cryptogram.json', 'r') as cryp_r_f:
        cryptogram = json.load(cryp_r_f)
    # ltrs_vals = (sorted(decoder.items(), key=lambda item: item[1], reverse=True))
    # print(ltrs_vals)
    for word in cryptogram.values():
        for k, v in word.items():
            for key, val in decoder.items():
                if k == val:  # If the key of the word in the cryptogram equals
                    # the value of the corresponding letter in the decoder
                    word[k] = key
    with open('../Cryptogram.json', 'w') as cryp_w_f:
        json.dump(cryptogram, cryp_w_f, indent=1)


def crypt_print() -> None:
    with open('../Cryptogram.json', 'r') as cryp_r_f:
        cryptogram = json.load(cryp_r_f)
    for word in cryptogram.values():
        for v in word.values():
            if v is None:
                print("_", end="")
            else:
                print(v, end="")
        print(" ", end="")


def main():
    # reset_cryptogram()
    update_decoder("B", "0")
    update_decoder("A", "16")  # Calc guess
    update_decoder("N", "6")  # Calc guess
    update_decoder("D", "21")  # Calc guess
    update_decoder("C", "14")
    decoder = get_decoder()
    update_cryptogram(decoder)
    # print(get_cryptogram())
    crypt_print()


if __name__ == "__main__":
    main()
