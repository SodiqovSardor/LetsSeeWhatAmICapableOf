# Lists are similar to arrays , They can contain any type of variable , and they can contain as much of variables as you want

# Examples on creating Lists :
mylist = [] # this is the list that we created
mylist.append(1) # append is used to add things for now we are using it to add numbers to our list
mylist.append(2) # same here
mylist.append(3) # same here

# Printing out to see that it works
print(mylist[0]) # we are tyring to get the first index of this List indexes start at zero so we are getting the mylist[0] first it will output 1 cuz [0] is the index that we start with it goes like [0 , 1 ,2]
print(mylist[1]) # same as well but we are getting the second room
print(mylist[2]) # same as well but we are getting the third room
# as you might've saw it ouputted 1 , 2 ,3 it means our code worked
# if you want for them all to appear we have to write a simple for loop
# prints out 1 , 2 , 3 as well 
for x in mylist : 
    print(x)

# We can try to access the index which does not exist and it will give us an error
list = [1 , 2 , 3]
print(list[3]) # it gives us an error list error is our of range that means we do not have the thing we are searching for

