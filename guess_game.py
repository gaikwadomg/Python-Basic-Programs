to_guess = "elephant"
guess = ""
print("---------------start-guess-Game--------------")
print("An animal which has trunk ! you only got 3 chances  \n \n")
count = 0 

while guess != to_guess and count < 3:
    guess = input("Enter guess : ")
    count += 1

if guess == to_guess:
    print("\nYou win the game")
else:
    print("\nYou lose the game")

print("----------------Thank You--------------")
