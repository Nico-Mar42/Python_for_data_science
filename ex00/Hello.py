ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Change the second element of the list to "World!"
ft_list[1] = "World!" 

# Change the second element of the tuple to "France"
ft_tuple = ("Hello", "France") 


ft_set.discard("tutu!")
ft_set.add("LeHavre")
ft_dict["Hello"] = "42LeHavre" 


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)