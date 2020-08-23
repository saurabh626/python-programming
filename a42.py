print("Enter the name of your 5 friends : ")
list=[]
for i in range(0,5):
 e=input()
 list.insert(i,e)
list.sort()
print("Name ofyour friends in alphabetical order : ",list)