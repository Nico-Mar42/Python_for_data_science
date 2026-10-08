import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image from a file and return it as a numpy array."""
    try:
        assert isinstance(path, str), "Path must be a String"
        assert path.lower().endswith((".jpg", ".jpeg")), \
            "image must be in .jpg or .jpeg format"

        image = Image.open(path)

        assert image.format == "JPEG", \
            "Image must be a JPEG or JPG file"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return []

    image_rgb = image.convert("RGB")
    array_rgb = np.array(image_rgb)
    print("The shape of image is:", array_rgb.shape)
    print(array_rgb)

    return array_rgb
