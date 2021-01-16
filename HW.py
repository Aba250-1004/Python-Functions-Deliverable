def sum_to(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

# print(sum_to(10))

def largest(inputList):
    largest = "empty list"
    if (len(inputList) > 0):
        largest = inputList[0]
        for i in range(len(inputList)):
            if (largest < inputList[i]):
                largest = inputList[i]
    return largest


# print(largest([1,2,3,4,0]))

def occurances(string,substring):
    totalMatches = 0
    subMatches = 0
    for i in range(len(string)):
        if(string[i] == substring[subMatches]):
            subMatches+=1
            if (subMatches == len(substring)):
                totalMatches += 1
                subMatches = 0
        else:
            subMatches = 0
    return totalMatches

# print(occurances('fleep floop', 'e'))
# print(occurances('fleep floop', 'p') )
# print(occurances('fleep floop', 'ee'))
# print(occurances('fleep floop', 'fe'))

def product(*nums):
    product = 1
    for num in nums: 
        product *= num
    return product

# print(product(1,2,3,4,5))
# print(product(4,5))

def getName():
    name = str(input("what is your name?"))
    return "hello, " + name

# print(getName())

def reverseIt(string):
    toReturn = ""
    for character in string:
        toReturn = character + toReturn
    return toReturn

# print(reverseIt("race car"))

def swapEm():
    a = 10
    b = 30

    temp = a
    a = b
    b = temp

    print(a)
    print(b)    

# swapEm()

def muiltplyArray(arr):
    if (len(arr) < 1):
        return 1
    total = 1
    for num in arr:
        total *= num
    return total

# print(muiltplyArray([2,2,4]))

def fizzbuzz(x):
    answer = ""
    if (x % 3 == 0):
        answer += "fizz"
    if (x % 5 == 0):
        answer += "buzz"
    if (x % 3 != 0) and (x % 5 != 0):
        answer += "archer"
    return answer

# print(fizzbuzz(1))

def nthFibonacciNumber(n):
    fibs = [1, 1]
    while(len(fibs) < n):
        fibs.append(fibs[len(fibs) - 2] + fibs[len(fibs) - 1])
    return fibs[len(fibs) -1]

# print(nthFibonacciNumber(7))

def searchArray(arr, value):
    for num in arr:
        if num == value:
            return True
    return False

# print(searchArray([1,2,3],5))

def hasDupes(arr):
    dictionary = {}
    for num in arr:
        if num in dictionary:
            return True
        else:
            dictionary[num] = True
    return False


print(hasDupes([0,1,2,3,3]))