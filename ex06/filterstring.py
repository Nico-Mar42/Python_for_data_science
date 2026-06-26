import sys
from ft_filter import ft_filter


def if_length_greater(word, length):
    return len(word) >= length


def ispunct(char):
    punctuation_chars = "\'!()-[]{};:'\"\\,<>./?@#$%^&*_~\""
    return char in punctuation_chars


def main():
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad1")
        return

    if not sys.argv[2].isdigit():
        print("AssertionError: the arguments are bad2")
        return

    N = int(sys.argv[2])
    S = sys.argv[1]
    if list(ft_filter(ispunct, S)):
        print("AssertionError: the arguments are bad3")
        return
    if [x for x in S if x in "\t\n\r"]:
        print("AssertionError: the arguments are bad4")
        return
    if N < 0:
        print("AssertionError: the arguments are bad5")
        return

    S_list = S.split(" ")

    print("S_list:", S_list)

    W_list = list(ft_filter(lambda word: if_length_greater(word, N), S_list))

    print("W_list:", W_list)


if __name__ == "__main__":
    main()
