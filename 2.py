input_string = input("Enter your string: ")

vowels = "AEIOUaeiou"

count = sum(1 for char in input_string if char in vowels)

print("The amount of vowels are:", count)