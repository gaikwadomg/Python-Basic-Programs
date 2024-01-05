#2d list aslo can be called as nested list 

number_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#list inside list is nested iist or 2d list 

print(number_list[3][0])

#printing all numbers of list using loop 

for row in number_list:
    for col in row:
        print(col) 



for i in number_list:
    print(i)
    for j in i:
        print(j)