#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    # this function should do the math
    counter = 0
    total = 0
    for number in list1:
        
        total += (number*list2[counter])
        counter += 1
    return total
# list1 = [1, 2, 3]
# list2 = [3, 2, 1]


# if __name__ == '__main__':
#    #REMOVE PASS AND YOUR CODE GOES HERE
#    # read in the integers
#    # call sum of products (return a value)
#    # print the result
#     pass

list1 = [] 
list2 = []  

list1 = [int(digit) for digit in input("Provide a series of integers with no spaces in between each: ")]
list2 = [int(digit) for digit in input("Provide another series of the same length and format: ")]

# print(list1)
# print(list2)

# length = int(input("I need two lists of integers, which should be equal in length. Choose your length: "))

# list1input = str(input("Provide a series of integers with no spaces in between each: "))
# list2input = str(input("Provide another series of the same length and format: "))

# for position in len(list1input): 
#     list1.append(list1input[position])
# for position in len(list2input):
#     list2.append(list2input[position])

if len(list1) != len(list2):
    print('Error: each series must be the same length')
else:
    print(sum_of_products(list1, list2))




