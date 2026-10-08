import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy import ndarray as array


def ft_invert(array) -> array:
    """Invert the colors of an RGB image represented as a numpy array."""

    matplotlib.use("TkAgg")

    try:
        assert isinstance(array, np.ndarray), "Input must be a numpy array"
        assert array.ndim == 3 and array.shape[2] == 3, \
            "Input array must be an RGB image"
        assert array.size > 0, "Input array is empty"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return []

    inverted_array = 255 - array

    plt.imshow(inverted_array)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return inverted_array


def ft_red(array) -> array:
    """Extract the red channel from an RGB
        image represented as a numpy array."""

    matplotlib.use("TkAgg")

    try:
        assert isinstance(array, np.ndarray), "Input must be a numpy array"
        assert array.ndim == 3 and array.shape[2] == 3, \
            "Input array must be 3-dimensional with 3 channels (RGB image)"
        assert array.size > 0, "Input array is empty"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return []

    red_channel = array * np.array([1, 0, 0])

    plt.imshow(red_channel)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return red_channel


def ft_green(array) -> array:
    """Extract the green channel from an
        RGB image represented as a numpy array."""

    matplotlib.use("TkAgg")

    try:
        assert isinstance(array, np.ndarray), "Input must be a numpy array"
        assert array.ndim == 3 and array.shape[2] == 3, \
            "Input array must be 3-dimensional with 3 channels (RGB image)"
        assert array.size > 0, "Input array is empty"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return []

    green_channel = array.copy()

    green_channel[:, :, 0] = 0
    green_channel[:, :, 2] = 0

    plt.imshow(green_channel)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return green_channel


def ft_blue(array) -> array:
    """Extract the blue channel from an
        RGB image represented as a numpy array."""

    matplotlib.use("TkAgg")

    try:
        assert isinstance(array, np.ndarray), "Input must be a numpy array"
        assert array.ndim == 3 and array.shape[2] == 3, \
            "Input array must be 3-dimensional with 3 channels (RGB image)"
        assert array.size > 0, "Input array is empty"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return []

    blue_channel = array.copy()

    blue_channel[:, :, 0] = 0
    blue_channel[:, :, 1] = 0

    plt.imshow(blue_channel)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return blue_channel


def ft_grey(array) -> array:
    """Convert an RGB image represented
        as a numpy array to grayscale."""

    matplotlib.use("TkAgg")

    try:
        assert isinstance(array, np.ndarray), "Input must be a numpy array"
        assert array.ndim == 3 and array.shape[2] == 3, \
            "Input array must be 3-dimensional with 3 channels (RGB image)"
        assert array.size > 0, "Input array is empty"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return []

    grey_array = np.mean(array, axis=2)

    plt.imshow(grey_array / 255, cmap="gray")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return grey_array
