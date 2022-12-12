#gets the list of numbers
for i in range(1,101):
#replaces multipules of both 3 and 5 with "fizzbuzz"
    if i % 5 == 0 and i % 3 == 0:
        print("fizzbuzz")
        continue
    #replaces multipules of 5 with "buzz"
    elif i % 5 == 0:
        print("buzz")
    #replaces multipules of 3 with "fizz"
    elif i % 3 == 0:
        print("fizz")
    #prints the list with added fizzes and buzzes
    else:
        print(i)
    
