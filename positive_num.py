def print_positive_numbers(input_list):
    positive_numbers = []

    for num in input_list:
        if num > 0:
            positive_numbers.append(num)

    if len(positive_numbers) > 0:
        print("Output:", positive_numbers)
    else:
        print("No positive numbers found in the list.")

user_input = input("Enter a list of numbers separated by spaces: ")
user_input = user_input.split()  
input_list = []

for num_str in user_input:
    try:
        num = int(num_str)
        input_list.append(num)
    except ValueError:
        pass

if input_list:
    print("Input:", input_list)
    print_positive_numbers(input_list)
else:
    print("Invalid input. Please enter a list of numbers.")
