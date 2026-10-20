# Float Data Type and Integer Data types work the same so i dont have to explain many things like in the first explanation of Integer
# Float data type exmaples
example_one = 1.123
example_two = 22.34
example_three = 334.5

# Float TypeConversion from String and Number to float examples

# First Example from String to a Float Data Type
price_string = "1.99" # we all see that price is written as a string as a word now we are going to convert this to a Float data type we know its string because of these "" , ''
print("im just showcasing that this is string : " , price_string , "this one is string")
price_string_to_float = float(price_string) # now we switched the sting to a float now instead of the "1.99" we are going to get 1.99 notice the difference , right this one is 1.99 different data type
print("We switched the from the string to a float : " , price_string_to_float , "this one is float")

# Second Example from Integer to a Float Data Type
price_number = 2 # this one is a number why do we know this one is a number and not a float cuz we do not have 2.0 2.00 like this you know we do not have a dot and the extra things after it and python is smart and automatically detects that and flags our data as a number
print("im showcasing number : " , price_number , "this one is a number")
price_number_to_float = float(price_number) # so i switched from number to a float right now and the expected answer would be : 2.0 cuz we switched to float and our answer would have . and 0 after it cuz we are writing a basic number that is just 2
print("we switched from the number to a float : " , price_number_to_float , "this one is float")
