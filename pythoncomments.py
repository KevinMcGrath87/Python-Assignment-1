num1 = 42 #variable declaration,numbner data type,
num2 = 2.3 #variable declaration, float data type
boolean = True #variable declaration "boolean" wtih boolean data type
string = 'Hello World'#variable declaration with string data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration list data type
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary dtat type variable declaration
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration tuple data type
print(type(fruit))#log statement of a type checkshould print data type of the fruit tuple
print(pizza_toppings[1])# log statement should print the second item in the list "pizza_toppings"
pizza_toppings.append('Mushrooms')#adds the value Like "push" in js to the list pizza_toppings
print(pizza_toppings)
print(person['name'])#log statement of the value in the dictionary associated with key item "name"
person['name'] = 'George'#changes value of item associated with key :name in the dicitonary of person
person['eye_color'] = 'blue'#essentially the same as above
print(fruit[2])#log statemt prints value at 3rd item in fruit tuple... i.e prints banana

if num1 > 45: #conditional statement
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:#conditional with condition of length check on the value assigned to the variable string
    print("It's a short word!")
elif len(string) > 15:#else if
    print("It's a long word!")
else:#else
    print("Just right!")

for x in range(5):#for loop using x as indexing variable ...less than 5 increments ...
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):#for loop starting at 2 for values less than 10 incrementing by 3
    print(x)
x = 0
while(x < 5):#while loop with x starting at 0 for as long as x is less than 5 prints x each time and increments by 1
    print(x)
    x += 1

pizza_toppings.pop()#function removes last itme in list pizza_toppings
pizza_toppings.pop(1)
#function removes item at index 1 in pizza_toppings
print(person)#prints the dictionary person
person.pop('eye_color')#removes the eye color property and value
print(person)#prints person without the eye color property

for topping in pizza_toppings: #for loop using topping as variable for indexing...i.e. for each item in the list
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives': # for loop stops when it reaches the last item "olives in the list"
        break

def print_hello_ten_times():#function definition with no parameters
    for num in range(10):#performs the function for all numbers 0-9; i.e prints hello 10 times
        print('Hello')

print_hello_ten_times()#function call

def print_hello_x_times(x):#function definition with x as a parameter x sets the amount of times the function is performed x is defined earlier as 0 but not perhaps in this codeblock
    for num in range(x):
        print('Hello')

print_hello_x_times(4)#sets parameter x to 4 in function and calls funciton prints hello 4 times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) # name <variablename> not defined
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)