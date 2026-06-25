import math
def NULL_not_found(object: any) -> int:


    if str(type(object)) == "<class 'NoneType'>":
        print("Nothing: None ", str(type(object)))
        return 0
    elif str(type(object)) == "<class 'float'>":
        if object != object:
            print("Cheese: nan ", str(type(object)))
            return 0
    elif str(type(object)) == "<class 'int'>":
        if int(object) == 0:
            print("Zero: 0 ", str(type(object)))
            return 0
    elif str(type(object)) == "<class 'str'>":
        if str(object) == "":
            print("Empty: ", str(type(object)))
            return 0
    elif str(type(object)) == "<class 'bool'>":
        if bool(object) == False:
            print("Fake: False ", str(type(object)))
            return 0

    print("Type not found")
    return 1
