print("-----------------------------------------------------------------")
students = ["om" ,"kunal","Ayaj","Lokesh" , "Anand"]
print(students)  #original list
print(students[1]) #particular element of list 
print(students[2:])  # all elements of list after  a specific index
print(students[2:4]) # some selected part of lisrt index

print("-----------------------------------------------------------------")


numbers = [343,44,4,33,45,46,33]

#concating two lists  using extend function 
print("Adding concatinating 2 strings -->")
students.extend(numbers)
print(students)
print("-----------------------------------------------------------------")

#adding item to end of list using append() function 
students.append("omkar")
print("\nAdded item at last -->")
print(students)
print("-----------------------------------------------------------------")

#removing item from end using pop()
students.pop()
print( "\nRemoved from end -->")
print(students)
print("-----------------------------------------------------------------")

#insert item in between using insert() function 
print("\nInserted item in between at fourth place -->")
students.insert(3 , "kk")
print(students)
print("-----------------------------------------------------------------")

#remove certain item from the list 
print("\nRemoved item from list in between removing  \" kk \" frm list -->")
students.remove("kk")
print(students)
print("-----------------------------------------------------------------")

#removing each element from list for getting empty list --->
print("\n Removing each element from list -->")
students.clear()
print(students)
print("-----------------------------------------------------------------")

#check weather certain item is in list or not
print("\nCheck if 33 is in list numbers or not  --->")
no = numbers.index(33)
print(no)

students = ["om" ,"kunal","Ayaj","Lokesh" , "Anand"]
no = [2,3,4,22,12,44,55,22,9]
print("-----------------------------------------------------------------")

# Try out sorting list 
students.sort()
print("\nI can sort list using .sort() function -->")
print(students)

no.sort()
print(no)
print("-----------------------------------------------------------------")


#We can revverse a string in python ising .reverse() function
print("\n I can reverse a string using .reverse() function")
students.reverse()
print(students)
no.reverse()
print(no)
print("-----------------------------------------------------------------")

#i can copy list in python using .copy() function

copystd = students.copy()
print("Original list student -->")
print(students)
print("Copied list named copystd -->")
print(copystd)

print("-----------------------------------------------------------------")
print("-----------------------------END-----------------------------------")
print("-----------------------------------------------------------------")

      

