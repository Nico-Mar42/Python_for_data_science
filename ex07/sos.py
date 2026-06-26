import sys
NESTED_MORSE = {'A': '.-',
                'B': '-...',
                'C': '-.-.',
                'D': '-..',
                'E': '.',
                'F': '..-.',
                'G': '--.',
                'H': '....',
                'I': '..',
                'J': '.---',
                'K': '-.-',
                'L': '.-..',
                'M': '--',
                'N': '-.',
                'O': '---',
                'P': '.--.',
                'Q': '--.-',
                'R': '.-.',
                'S': '...',
                'T': '-',
                'U': '..-',
                'V': '...-',
                'W': '.--',
                'X': '-..-',
                'Y': '-.--',
                'Z': '--..',
                ' ': '/ '}


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return
    if [char for char in sys.argv[1] if not char.isalpha() and char != ' ']:
        print("AssertionError: the arguments are bad")
        return

    for char in sys.argv[1]:
        if char.upper() not in NESTED_MORSE:
            print("AssertionError: the arguments are bad")
            return
        if char == ' ':
            print(NESTED_MORSE[char], end='')
        else:
            print(NESTED_MORSE[char.upper()], end=' ')


if __name__ == "__main__":
    main()
