import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D list (family) from the specified start index to the end index."""
    try:
        assert isinstance(family, list), "Family must be a list"
        lenght = len(family[0])
        assert all(len(value) == lenght for value in family), \
            "Each element of family must contain 2 value"
        
        assert isinstance(start, int), "start must be a int"
        assert isinstance(end, int), "end must be a int"

    except AssertionError as error:
        print(error)
        return []    

    print("My shape is : ", np.array(family).shape)

    sliced_family = family[start:end]

    print("My new shape is : ", np.array(sliced_family).shape)

    return sliced_family