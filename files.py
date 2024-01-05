emp_file = open("employs.txt","r")
word = emp_file.read()
print(word)
emp_file.close()

newf = open("insed.html","w") # w and a will overerite and append file at end
newf.write(word)
newf.close()
