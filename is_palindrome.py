from typing import Tuple


def is_palindrome(text: str) -> Tuple[bool, str]:
    """
    EX:
        is_palindrome('Francesco') returns False
        is_palindrome('ANNNA') returns True
    """

    if not text.isalpha():
        raise TypeError("you did not insert a valid string format")
    reversed_string = text[::-1]
    return reversed_string == text, reversed_string


def check_palindrome(text: str) -> None:
    aux_, reversed_text = is_palindrome(text)
    if aux_:
        try:
            assert reversed_text == text
        except AssertionError:
            raise InvalidPalindrome("there is something wrong with the palindrome algorithm")


class InvalidPalindrome(Exception):
    pass


if __name__ == '__main__':
    while True:
        text = input("Which string you want to check??")
        # non ho usato argparse perchè argparse permetterebbe di settare il valore di text da riga di comando soltanto una volta (la seconda e la terza iterazione varrebbe sempre lo stesso valore)
        aux_, reversed_string = is_palindrome(text)
        if aux_:
            check_palindrome(text)
            print(f"Yes, the word {text} is a palindrome")
        else:
            print(f" Sorry, {text} is not a palindrome")
        playing_again = input("if you want to press another word just type y otherwise type n")
        if playing_again == 'n':
            print("thank you, see you next time!!")
            break
