# Exercise 1
ages = [2, 12, 12, 14, 15, 17, 18, 20, 20]

print('the Maximum age is: ', max(ages))
print(set(ages))



print('-------------------------------')
print('--------------------------------')
# exercise 2

age_1 = [2, 12, 12, 14, 16, 16, 14, 20, 20]
age_2 = [2, 4, 12, 14, 16, 16, 14, 20, 20]
def data_list(age_1, age_2):
    result = False
    for x in age_1:
        for y in age_2:
            if x == y:
                result = True
                return result
print(data_list([2, 12, 12, 14, 16, 16, 14, 20, 20],  [2, 4, 12, 14, 16, 16, 14, 20, 20]))
print(data_list([2, 12, 12, 14, 16, 16, 14, 20, 20],[2, 4, 12, 14, 16, 16, 14, 20, 20]))
