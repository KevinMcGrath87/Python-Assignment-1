print("first")
#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#prints the number 5

# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
print("second")

#prints error because it calls an undefined function
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#prints the number 5 because that is the first return statement and nothing else in the code block is executed after the return

print("third")

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#prints the number 5 since the print that occurs after the return statement isnt executed
print("fourth")


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#prints the name of the function since no value is returned//actually prints none the value of the funciton
print("fifth")


#6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
#add does not return a value it prints when it is called. it is called inside of a print statement. the concatenation/+ has nothing to act on I dont think it will print anything it actually errors ...trys to add two none type things... operation error
print("sixth")


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#converts the number 2 and 5 to strings and concatenates them. i.e. prints 25
print("seventh")


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#when the funciton is called it prings 100. then checks if 100 is less than 10 which is false so it returns 10 it should print 10 

print("eigth")

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#first iteration of print since condition is met for the first condition prints 7, second iteration prints 14 3rd iteration prints  prints 21

print("ninth")

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#prints the number 8
print("tenth")


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#prints first the number 500 then prints 500 again then calls foobar which has a local variable called b the equals 30 and prints the value of 300, then prints 500 the global variable of b 
print("eleventh")

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# prints 500., prints 500 again, executed fubar and prints 300, prints 300 again
print("twelfth")


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#prints 500, prints 500, sets b to foobar, prins 300 the return of foobar
print("thirteenth")


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# bar is not defined in the foo call but is executed as part of its subroutine I thin this will erroer despite bar being defined later in the codeblock. Otherwise it will print1 call bar which prints 3 and then prints 2
print("fourteenth")


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#prints 1 assigns local x to bar function calls x in print which is the value 5  prints 10
print("fifteenth")