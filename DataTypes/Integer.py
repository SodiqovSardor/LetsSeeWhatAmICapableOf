# Numeric / Integers 
number = 5
print("This is just a number : ",number) # outputs 5

# Converting into int with int()
word = "250" # we can see it is number but it is always a string if written with "" or '' or `` im not sure about ``
print("im showcasing the word : " , word , "this is string")
notaregularnumber = 0.213 # we are calling this one a float type number from now on
trueandfalse = True # in python we call these `true and false` Booleans
print("this is a number but written in string so techincally it is a word : ",word) # ofc it outputs the 250 but in string the next data type i will teach

# Type Conversion Start
stringtonumber = int(word) # now we are techincally converting number inside that string "250" to a number that is 250 without these ""
print( "this is converted from string to nubmer : ", stringtonumber , "this is number") # the output in both `word` and `stringtonumber` are 250 but 1st one is string second one is number in short integer we are calling number data types integers from now on 

floattonumber = int(notaregularnumber) # as you can see we are converting number in different structure just to a basic number that does not look like this : 0.2131 our number wuld look like 0
print( "this is converted from float to number" , floattonumber) # the output shows that is successfully converted and the answer is 0 just know this the number didnt get rounded we just removed the part after `.` dot

booleantonumber = int(trueandfalse) # now we are converting boolean to a number sounds dumb right like we are Converting the word to a number lol . So lets stop here for a second you know Computer does not know what we are writing into it , it only knows 0 and 1 active and inactive states so we have boolean that has only 2 states as well `True and False` true that means active and active in compuler language is 1 and as you might've thought already False is inactive and it is 0 let me demonstrate it to you via just converting it from boolean to int
print(" this is conveted from Boolean to number integer techincally : " , booleantonumber) # as we saw output is 1 we converted the Boolean to a number "Integer" impressive isnt it 



