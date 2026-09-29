import sys
from ft_filter import ft_filter


def if_length_greater(word, length):
    return len(word) >= length


def ispunct(char):
    punctuation_chars = "\'!()-[]{};:'\"\\,<>./?@#$%^&*_~\""
    return char in punctuation_chars


def main():
    try:
        args = sys.argv[1:3]
        assert len(args) == 2, "the arguments are bad"

        S, N = args
        N = int(N)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    if list(ft_filter(ispunct, S)):
        print("AssertionError: the arguments are bad")
        return
    if [x for x in S if x in "\t\n\r"]:
        print("AssertionError: the arguments are bad")
        return
    if N < 0:
        print("AssertionError: the arguments are bad")
        return

    S_list = S.split(" ")

    W_list = list(ft_filter(lambda word: if_length_greater(word, N), S_list))

    print(W_list)


if __name__ == "__main__":
    main()
