# Basic Operators

# Arithmetic Operators
# Just as any other programming languages , addition , subtraction , multiplication , division operators can be used with numbers.

addition = 1 + 2 + 3 + 4 # this is addition we write it with "+"
print( "showcasing the addition : " , addition) # just for printing out the answer

subtraction = 10 - 9 - 8 - 7 # this is subtraction we write it with "-"
print("showcasing subtraction : " , subtraction) # just for priting out the answer

multiplication = 2 * 1 # we use "*" this for multiplication basic multiplication
print("showcasing multiplication : " , multiplication) # just for printing out the answer

division = 4 / 2 # we use "/" this for division between numbers this will output 2.0 if you dont want to have anything after . just write division like this " 4 // 2" this will output just 2
print("showcasing division : " , division) # just for printing out the answer

remainder = 11 % 3 # "%" this is a remainder operator in uzbek "Qoldiq" this operator shows us remainder after division works like division but just outputs a remainder
print( "showcasing remainder `Qoldiq` : " , remainder) # just for printing out the answer

squared = 7 ** 2 # we use "**" double multiplication symbols for power relationship "darajalar uchun tipo bu yerda 7 ni 2 chi darajasi"
cubed = 7 ** 3 # same here but 7 to a power of 3 "7 ni 3 chi darajasi"
print("showcasing the squared : ",squared) # printing out the answer
print("showcasing the cubed : ",cubed) # printing out the answer


# And who said we can only use operators with numbers ? 
# We can use operators with Strings as well

helloworld = "hello" + " " + "world" # as you can see i wrote the "+" operator here cuz here i want to combine the worlds "hello" and "world" to be in 1 like "hello world" and i've added " " free space as well so the words do not collapse into each other like this "helloworld" ! While using "+" operator with strings they will at the 1 word to another
print(helloworld) # printing out the answer ! Answer is "hello world" everything works as expected

lots_of_hellos = "hello " * 5 # Yea we can multiply the words as well with the "*" operators it works as expected it will output "hello" 5 times i added a free space after "hello " cuz i dont want words colliding with eachother
print(lots_of_hellos) # printing out the answer


# We can use Operators with Lists as well

odd_numbers = [1 , 3 , 5 , 7] # i created a list of odd numbers
even_numbers = [2 , 4 , 6 , 8] # i created a list of even numbers
both_of_them = odd_numbers + even_numbers # then i used the "+" operator to combine odd numbers with even numbers our expected output wold be [ 1 , 3 , 5 , 7 , 2 , 4 , 6 ,8 ]
print(both_of_them) # priting out the answer ! as expected the answer is [ 1 , 3 , 5 , 7 , 2 , 4 , 6 ,8 ]

print([1,2,3] * 3) # yea we can use multiplication on lists as well using multiplication on lists will result of having the inside of list 3 times written inside it cuz in my exmaple we are multiplying it to 3 expected answer would be like [ 1 , 3 , 5 , 7 , 2 , 4 , 6 ,8 ]
