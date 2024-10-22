#Task-1
languages = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']
print("Original list:", languages)
print("Sorted list:", sorted(languages))
languages.reverse()
print("Reversed list:", languages)
languages.sort()
print("Sorted in place:", languages)

#Task-2
numbers = input("Enter a string of numbers separated by spaces: ")
numbers_list = [int(x) for x in numbers.split()]
total_sum = sum(numbers_list)
print(f"The sum is: {total_sum}")

#Task-3
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
message = ', '.join(cities[:-1]) + ' and ' + cities[-1]
print(message)

#Task-4
numbers = input("Enter 3 digits separated by spaces: ")
digits_list = [x for x in numbers.split()]
reversed_digits_list = digits_list[::-1]
reversed_number = ''.join(reversed_digits_list)
print(f"Reversed number: {reversed_number}")

#Task-5
professions = ['Doctor', 'Engineer', 'Teacher', 'Artist', 'Pilot']
print("Original list:", professions)
print("Sorted list:", sorted(professions))
professions.reverse()
print("Reversed list:", professions)
professions.sort()
print("Sorted in place:", professions)

#Task-6
keywords = ('for', 'if', 'else', 'in', ':')
print(f"{keywords[0]} each token in the postfix expression :")
print("    if the token is a number :")
print("        print('Convert it to an integer and add it to the end of values')")
print("    else :")
print("        print('Append the result to the end of values')")




