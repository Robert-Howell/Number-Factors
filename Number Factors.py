
# This function will find all factor pairs for any positive, non-zero whole integer

def number_factors(big_number):
    factor_list1 = []
    factor_list2 = []
    for x in range(0, big_number + 1):
        for y in range(0, big_number + 1):
            if (x * y) == big_number:
                factor_list1.append(x)
                factor_list2.append(y)

    factor_list = zip(factor_list1, factor_list2)
    return list(factor_list)


big_number = int(input("What number do you have in mind?"))

print(number_factors(big_number))
print("You have " + str(len(number_factors(big_number))) + " pairs of factors in " + str(big_number))
