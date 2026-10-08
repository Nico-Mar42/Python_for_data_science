import numpy as np
import load_image
import matplotlib
import matplotlib.pyplot as plt


def main():
    ''' Main function to test the zoom functionality. '''
    matplotlib.use("TkAgg")

    img_nparray = load_image.ft_load("animal.jpeg")

    try:
        assert isinstance(img_nparray, np.ndarray), \
            "Image must be a numpy array"
        assert img_nparray.size > 0, "Image array is empty"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return []

    print(img_nparray)
    sliced_array = img_nparray[100:500, 450:850, 0:1]
    plt.imshow(sliced_array, cmap="gray")
    plt.xlabel("X")
    plt.ylabel("Y")
    print("New shape after slicing:", sliced_array.shape, "or (400, 400)")
    print(sliced_array)
    plt.show()


if __name__ == "__main__":
    main()
