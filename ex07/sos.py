import sys

def getMorseCode():
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
                    '1': '.----',
                    '2': '..---',
                    '3': '...--',
                    '4': '....-',
                    '5': '.....',
                    '6': '-....',
                    '7': '--...',
                    '8': '---..',
                    '9': '----.',
                    '0': '-----',
                    ' ': '/ '}
    return NESTED_MORSE


def main():
    try:
        args = sys.argv[1:]
        assert len(args) < 2, "More than one argument is provided"
        try:
            assert len(sys.argv[1]) > 0, "the arguments are bad"
            if [char for char in sys.argv[1] if not char.isalnum() and char != ' ']:
                raise AssertionError("the arguments are bad")
        except IndexError:
            raise AssertionError("the arguments are bad")
        res = []
        for char in sys.argv[1]:
        
            if char.upper() not in getMorseCode():
                raise AssertionError("the arguments are bad")
            else:
                res.append(getMorseCode()[char.upper()])
        str = ' '.join(res)
        print(str)
    except AssertionError as e:
        print(f"AssertionError : {e}")
        exit(1)


if __name__ == "__main__":
    main()
