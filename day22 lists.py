marks= [3,4,5 ,"harry",True]
print (marks)
print(type(marks))
#(marks[0])

#print(marks[0])
#print(marks[1])
#print(marks[2])
#print(marks[3])

print(marks[-3])  #negative index 
print(marks[len(marks)-3]) #positive index 
print(marks[5-3])  #positive index 
print(marks[2]) #positive index 
print(marks[4]) #positive index 

if 5 in marks:
    print("yes")
else:
    print("no")

print(marks)
print(marks[1:3 ])


lst = [i*i for i in range(4)]
print(lst)
lst = [i*i for i in range(10)if i%2==0]
print(lst)
