
def all_thing_is_obj(object: any) -> int:

    if object is None:
        print("")
        return 0

    Stype = str(type(object))
    if Stype == "<class 'str'>":
        print(object, " is in the kitchen : ", Stype)
    elif Stype == "<class 'list'>":
        print("List : ", Stype)
    elif Stype == "<class 'tuple'>":
        print("Tuple : ", Stype)
    elif Stype == "<class 'set'>":
        print("Set : ", Stype)
    elif Stype == "<class 'dict'>":
        print("Dict : ", Stype)
    else:
        print("Type not found")
    return 42
