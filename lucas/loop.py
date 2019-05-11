# empty list
list = []

# number of elements as input
size = int(input("Enter number of elements: \n"))

for i in range(0, size):
    print("enter value",i+1,": ")
    ele = int(input())
    list.append(ele)

print("contents of your list: {}".format(list))
#print(*list)
