def sum_of_products(list1, list2):
    counter = 0
    total = 0
    for number in list1:
        
        total += (number*list2[counter])
        counter += 1
    return total
if __name__ == '__main__':
    list1 = [] 
    list2 = []  

    # list1 = [int(digit) for digit in input("Provide a series of integers with no spaces in between each: ")]
    # list2 = [int(digit) for digit in input("Provide another series of the same length and format: ")]

    for digit in input("Provide a series of integers with no spaces in between each: "):
        list1.append(int(digit))
    for digit in input("Provide another series of the same length and format: "):
        list2.append(int(digit))

    if len(list1) != len(list2):
        print('Error: each series must be the same length')
    else:
        print(sum_of_products(list1, list2))




