# is_male = False
# is_tall = True

# if is_male and is_tall:
#     print("I am male and i am tall")
# elif is_male and not(is_tall):
#     print("i am a short male")
# elif not(is_male) and not(is_tall):
#     print("i am not male and i am not tall ")
# elif not(is_male) and is_tall:
#     print("i am tall but ot male")


# maximum of three numbers using function 
def maxi(num1 , num2 , num3):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    if num2 >= num3 and num2 >= num1:
        print(num2)
    if num3 >= num1 and num3 >= num2:
        print(num3)

x = input("Enter first number :")
y = input("Enter second number :")
z = input("Enter third number :")

x= float(x)
y = float(y)
z= float(z)

print("Maximum of three numbers using if else is : ")
maxi(x,y,z)


