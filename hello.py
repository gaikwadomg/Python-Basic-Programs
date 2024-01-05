print("Hello ths is my first python program actually seecond!\n")

print("Now i can draw triangle and various shapes in python : See by yourself : --- >>> ")

print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____| \n")


print("Lets play with variables thy are name given to a memory location \n we can say that variables are containers that stores value and make it easy to access stored values :: -- > \n")

name = "Kunal Khopade"
age = "19"

print("hello there my name is  " + name + ", \n and my age is " + age +",\n")
print( name + "ia a very inobedient untrustworthy and untrustworthy person  of age " + age +"\n")
print("In above paragraph we can change everytime name and age appear in paragraph by just one time changing in variables name and age ! \n\n")

print("Now lets tru to play with strings :: -- > \n")

text = "I love India !"
print("original string: " + text)
print("\nlets print string in Uppercase using upper() function : " + text.upper())
print("\nlets print string in Lowercase using lower() function : " + text.lower())
print("lets find length of string using len() function length is  : --> " + str(len(text)))  # len() gives integer value to concat integer with string convert  integer to string using str() function .
print("\nlets check if string is uppercase or not : " +  str(text.lower().islower())) 
print("\nlets check if string is uppercase or not : " +  str(text.islower())) 

print("\n lets try to get element in string by its index   :")
print("element at 11th position is :")
print(text[10])

print("\n \n now lets try finding index of certain element in the string : ")
print("Index of India is similarly we can finde index for any single element " + str(text.index("India")))

print("\n lets try to replace elements form string with newer one : \n")
print(" Replcing India with US hence resultant string --- > " + text.replace("India" , "US"))










