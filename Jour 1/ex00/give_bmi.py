import numpy as np

__doc__ 

def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Caculate BMI values with Numpy"""
    try:
        assert isinstance(height, list), "Height must be a list."
        assert all(isinstance(value, (int, float)) for value in height), \
            "height must contain only number"

        assert isinstance(weight, list), "weight must be a list."
        assert all(isinstance(value, (int, float)) for value in weight), \
            "weight must contain only number"

        assert len(height) == len(weight), \
            "height and weight must have the same length."

    except AssertionError as error:
        print(error)
        return []

    height_array = np.array(height)
    weight_array = np.array(weight)

    bmi_array = weight_array / (height_array ** 2)

    bmi = bmi_array.tolist()

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Checks whether each BMI is above the specified limit."""
    try:
        assert isinstance(bmi, list), "Height must be a list."
        assert all(isinstance(value, (int, float)) for value in bmi), \
            "bmi must contain only number"

        assert isinstance(limit, int), "Limit must be a int"

    except AssertionError as error:
        print(error)
        return []

    bmi_array = np.array(bmi)

    limit_boolean = bmi_array > limit

    return limit_boolean.tolist()
