import sys


def main():
    try:
        args = sys.argv[1:]
        assert len(args) < 2, "More than one argument is provided"
        if len(args) == 0:
            exit(0)
        try:
            i = int(args[0])
            if i % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            raise AssertionError("Argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError : {e}")
        exit(1)


if __name__ == "__main__":
    main()
