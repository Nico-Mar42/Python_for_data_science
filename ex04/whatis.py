import sys


def main():
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            return 0
        elif len(sys.argv) > 2:
            return print(AssertionError("AssertionError : "
                         "More than one argument is provided"))

    if not sys.argv[1].isdigit():
        return print(AssertionError("AssertionError : "
                     "Argument is not an integer"))
    i = int(sys.argv[1])

    if type(i) is int:
        if i % 2 == 0:
            return print("I'm Even.")
        else:
            return print("I'm Odd.")
    else:
        return print(AssertionError("AssertionError : "
                     "Argument is not an integer"))


if __name__ == "__main__":
    main()
