first = input("Enter first number : ");
operator = input("Enter your operator ( + , - , * , / , %)  :");
second = input("Enter second number :");

first=int(first);
second = int(second);


if operator == "+":
	res=first+second;
elif operator == "-":
	res=first-second;
elif operator == "*":
	res = first*second;
elif operator == "/":
	res=first/second;
else:
	res=first%second;

print("Result : " + str(res));
	