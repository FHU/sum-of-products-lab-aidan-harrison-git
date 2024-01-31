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
    string1 = input("Provide a series of integers with spaces in between each: ")
    string2 = input("Provide another series of the same length and format: ")

    list1str = string1.split()
    list2str = string2.split()
    
    for digit in list1str: 
        list1.append(int(digit))
    for digit in list2str:
        list2.append(int(digit))

    if len(list1) != len(list2):
        raise ValueError('Error - series 1 and 2 must be equal in length')
    else:
        print(sum_of_products(list1, list2))


# read in the strings first
# then split on whitespace .split()




