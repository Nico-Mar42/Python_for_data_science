from load_image import ft_load

print("\033[92m-------------- Test Python for Datascience 1 - ex2 --------------\n\n\033[0m")

print("\033[93m------ Test not a String ------\n\033[0m")

print("\033[91m", ft_load(42))

print("\033[93m\n------ Test not a jpg ------\n\033[0m")

print("\033[91m", ft_load("logo.webp"))

print("\033[93m\n------ Test is a webp rename on jpg ------\n\033[0m")

print("\033[91m", ft_load("logo.jpg"))

print("\033[93m\n------ Test with good arguments ------\n\033[0m")

print("\033[94m", ft_load("landscape.jpg"))

print("\033[93m\n------ Test __doc__ ------\n\033[0m")

print("\033[91m", ft_load.__doc__, "\n")

print("\033[92m\n\n-------------- End of Test --------------\033[0m")
