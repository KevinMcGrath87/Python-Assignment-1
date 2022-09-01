#countdown
def countdown(number):
    list1=[]
    for x in range (number,-1 ,-1):
        list1.append(x)
    return(list1)
    print(countdown(45))

#print and return
def printReturn(listarg=[0,0]):
    print(listarg[0])
    return(listarg[1])
print(printReturn([3,5]))
print(printReturn())

#first plus length
def firstPlus(list1=[0,0]):
    length1 = len(list1)
    num1=list1[0]
    sum = num1 + length1
    return(sum)
print(firstPlus([1,2,3,4,5]))

#values greater than second
def values(list1):
    newList=[]
    if len(list1)<2 or not isinstance(list1, list):
        return(False)
    for x in list1:
        if x > list1[1]:
            newList.append(x)
    print(len(newList))
    return(newList)
print(values([34,54,22,678,876,654,23,545346,6565,333,5,7,4,900]))

#this length that value
def lengthVal(size, value):
    list1 = []
    for x in range(size):
        list1.append(value)
    return(list1)
print(lengthVal(9,10))


