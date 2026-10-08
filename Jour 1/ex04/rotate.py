import numpy as np
import load_image
import matplotlib
import matplotlib.pyplot as plt


def main():
    ''' Main function to test the rotate functionality. '''
    matplotlib.use("TkAgg")

    img_nparray = load_image.ft_load("animal.jpeg")

    try:
        assert isinstance(img_nparray, np.ndarray), \
            "Image must be a numpy array"
        assert img_nparray.size > 0, "Image array is empty"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return []

    sliced_array = img_nparray[100:500, 450:850, 0:1]
    print("The shape of image is:", sliced_array.shape)
    print(sliced_array)

    gray_array = sliced_array.squeeze()

    transposed_array = np.zeros_like(gray_array)

    for row in range(gray_array.shape[0]):
        for column in range(gray_array.shape[1]):
            transposed_array[column, row] = gray_array[row, column]

    plt.imshow(transposed_array, cmap="gray")
    plt.xlabel("X")
    plt.ylabel("Y")
    print("New shape after slicing:", transposed_array.shape)
    print(transposed_array)
    plt.show()


if __name__ == "__main__":
    main()
