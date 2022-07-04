# Using List comprehensions
# for constructing output list

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]


list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:",
							list_using_comp)


# Constructing output list using for loop
output_list = []
for var in range(1, 10):
	output_list.append(var ** 2)
	
print("Output List using for loop:", output_list)
