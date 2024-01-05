try:
    num = int(input("Enter a number :"))
    print( num)
    o = 9/0

# except:
#     print("You entered a non integer value. ") # except has wide range range you can specify except instead.

except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("invalid input ")

