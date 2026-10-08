from array2D import slice_me

print("\033[92m-------------- Test Python for Datascience 1 - ex1 --------------\n\n\033[0m")

print("\033[93m------ Test not a list ------\n\033[0m")

family = 2,
print(slice_me(family, 0, 2))

print("\033[93m------ Test same length in list ------\n\033[0m")

family = [[1.80, 78.4],
        [2.15, 102.7, 12.3],
        [2.10, 98.5],
        [1.88, 75.2]]

print(slice_me(family, 0, 2))

print("\033[93m------ Test start is not a int ------\n\033[0m")

family = [[1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]]

print(slice_me(family, 1.3, 2))
print(slice_me(family, 1, "test"))

print("\033[93m\n------ Test with good arguments ------\n\033[0m")

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

print("\033[93m\n------ Test __doc__ ------\n\033[0m")

print("\033[91m", slice_me.__doc__, "\n")

print("\033[92m\n\n-------------- End of Test --------------\033[0m")
