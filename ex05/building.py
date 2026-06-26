import sys


def ispunct(char):
    punctuation_chars = "''!()-[]{};:'\"\\,<>./?@#$%^&*_~''"
    return char in punctuation_chars


def main():
    if len(sys.argv) > 2:
        print("Usage: python building.py <object>")
        return
    if len(sys.argv) == 1:
        print("What is the text to count?")
        str = sys.stdin.readline()
    else:
        str = sys.argv[1]
    if len(str) == 0:
        print("Error: Empty string provided.")
        return
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


if __name__ == "__main__":
    main()
