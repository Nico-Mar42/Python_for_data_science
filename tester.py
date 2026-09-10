import sys
from ex02.find_ft_type import all_thing_is_obj
from ex03.NULL_not_found import NULL_not_found
from time import sleep
from tqdm import tqdm
from ex08.Loading import ft_tqdm
from ex09.src.ft_package import count_in_list


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        args = sys.argv[1]

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    if args == "2":
        ft_list  = ["Hello", "tata!"]
        ft_tuple = ("Hello", "toto!")
        ft_set   = {"Hello", "tutu!"}
        ft_dict  = {"Hello" : "titi!"}
        all_thing_is_obj(ft_list)
        all_thing_is_obj(ft_tuple)
        all_thing_is_obj(ft_set)
        all_thing_is_obj(ft_dict)
        all_thing_is_obj("Brian")
        all_thing_is_obj("Toto")
        print(all_thing_is_obj(10))

    if args == "3":
        Nothing = None
        Garlic = float("NaN")
        Zero = 0
        Empty = ''
        Fake = False
        NULL_not_found(Nothing)
        NULL_not_found(Garlic)
        NULL_not_found(Zero)
        NULL_not_found(Empty)
        NULL_not_found(Fake)
        print(NULL_not_found("Brian"))

    if args == "8":
        for elem in ft_tqdm(range(333)):
            sleep(0.005)
        print()
        for elem in tqdm(range(333)):
            sleep(0.005)
        print()

    if args == "9":
        print(count_in_list(["toto", "tata", "toto"], "toto")) # Doit afficher 2
        print(count_in_list(["toto", "tata", "toto"], "tutu")) # Doit afficher 0


if __name__ == "__main__":
    main()