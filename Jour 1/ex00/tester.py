from give_bmi import give_bmi, apply_limit

print("\033[92m-------------- Test Python for Datascience 1 - ex0 --------------\n\n\033[0m")

print("\033[93m------ Test not a list ------\n\033[0m")

height1 = "test"
weight1 = [165.3, 38.4]

bmi = give_bmi(height1, weight1)

print("\033[93m\n------ Test not a int | float ------\n\033[0m")

height2 = [2.71, "test"]
weight2 = [165.3, 38.4]

bmi = give_bmi(height2, weight2)

print("\033[93m\n------ Test not same lenght ------\n\033[0m")

height3 = [2.71, 1.15, 2]
weight3 = [165.3, 38.4]

bmi = give_bmi(height3, weight3)

print("\033[93m\n------ Test good arguments ------\n\033[0m")

height4 = [2.71, 1.15]
weight4 = [165.3, 38.4]

bmi = give_bmi(height4, weight4)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("\033[93m\n------ Test __doc__ ------\n\033[0m")

print("\033[91m", give_bmi.__doc__, "\n")
print("\033[91m", apply_limit.__doc__,)

print("\033[92m\n\n-------------- End of Test --------------\033[0m")

