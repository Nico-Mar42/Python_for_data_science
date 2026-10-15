from load_csv import load

print("\033[92m-------------- Test Python for Datascience 2 - ex0 --------------\n\n\033[0m")

print("\033[93m------ Test not a String ------\n\033[0m")

print(load(2))

print("\033[93m\n------ Test path does not exist ------\n\033[0m")

print(load("non_existent_file.csv"))

print("\033[93m\n------ Test path is not a CSV ------\n\033[0m")

print(load("test.txt"))

print("\033[93m\n------ Test with good path ------\n\033[0m")

print(load("life_expectancy_years.csv"))

print("\033[91m", load.__doc__,)

print("\033[92m\n\n-------------- End of Test --------------\033[0m")

