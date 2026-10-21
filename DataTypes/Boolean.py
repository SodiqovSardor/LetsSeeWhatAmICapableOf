# Boolean Data Type (bool)

# Basic boolean values
is_logged_in = True # this makes our is logged in's value to be True that means the user is logged in
print(is_logged_in) # and the output shows True meaning its true
is_premium_acc = False # this is the is_premium_acc its value is False so the account is not premium
print(is_premium_acc) # and the output is False meaning it is false
# pretty simple right ?

# Booleans result from comparison operators here are the examples
age = 25
is_adult = age >= 18 # True
is_senior = age >= 65 # False
names_match = "Sarah" == "sarah" # False cuz you see firs letter is asigned with the Big S

print( "are you an adult : " , is_adult , " are you a senior : " , is_senior , ", Your are is : " , age)

# Booleans allow you to combine canditions:
is_logged_in = True # is the user logged in , in this place yes the User is logged in cuz it is written there that its true
has_premium_account = False # does our user have a premium account False lets think so our user does not have premium and just created account today
can_access_premium = is_logged_in and has_premium_account # False , But why we can see the user is logged in Thats literally written there is_logged_in = True right but wrong you see the has_premium_account = False and our operator is "and" operator for "and" operator to work our both sides must be true but our example shows so "True" and "False" but it must be "True" and "True" but in our case both sides do not math so its False
print( "can the user acces premium ? : " ,can_access_premium) # This is just print for yall to test this
can_view_content = is_logged_in or has_premium_account # True , But why this is True you might ask cuz we have True and False but i said if True and False this is False , Wrong you can see we are using the "or" operator insead of "and" operator our "or" operator is not that strict and with the "or" operator it outputs True every time if either of our 2 things is true like in my explanation we have "True" or "False" so this is True it ourputs False only when the both canditions are False like "False" or "False" its output is False
print("can the user view content? : " , can_view_content) # this is just print for testing
is_regular_user = not has_premium_account # True , But why as you see we have "not" operator in programming most known with the "!" this but in python we can write "not" as well pretty complicated right so our has_premium_account = False right our "not" operator works like not_has_premium_account = True it just like switches your "true" with "false" and "false" with "true" when you put not operator
print( "is this a regular user? : " , is_regular_user) # this is just print as well for testing

# Complex candition
is_target_demographic = (age >= 18 and age <= 35) and is_logged_in # True , this is just the thing i explained but its just a compldex candition
print( "is our target demographic ? : " , is_target_demographic) # just print for testing
