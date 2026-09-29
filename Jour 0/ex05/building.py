import sys


def ispunct(char):
    punctuation_chars = "''!()-[]{};:'\"\\,<>./?@#$%^&*_~''"
    return char in punctuation_chars


def main():
    try:
        args = sys.argv[1:]
        assert len(args) < 2, "More than one argument is provided"
        if len(args) == 0:
            print("What is the text to count?")
            str = sys.stdin.readline()
        else:
            str = args[0]
        uppercase_count = 0
        lowercase_count = 0
        punctuation_count = 0
        space_count = 0
        digit_count = 0

        for i in range(len(str)):
            if str[i].isupper():
                uppercase_count += 1
            elif str[i].islower():
                lowercase_count += 1
            elif str[i].isdigit():
                digit_count += 1
            elif str[i].isspace():
                space_count += 1
            elif ispunct(str[i]):
                punctuation_count += 1
            else:
                print("Error: Invalid character found.")
                return

        print("The text contains", len(str), "characters:")
        print(uppercase_count, "upper letters")
        print(lowercase_count, "lower letters")
        print(punctuation_count, "punctuation marks")
        print(space_count, "spaces")
        print(digit_count, "digits")

    except AssertionError as e:
        print(f"AssertionError : {e}")
        exit(1)


if __name__ == "__main__":
    main()
