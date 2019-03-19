import array
size = int(input("What size of an array do you want? "))

array = [size]

for index in array:
    for index in range(size):
        int(input("What do you want in array %s? " % index))

for index, array in enumerate(array, start =1):
    print(index, array)
