#dictionaries in python 

dic ={
    322:"rutik",
    56:"shubham",
    546:"sgfh"

}
print(dic[546])

info ={'name':'karna','age':20,'eligible':True}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
    print(f'the values corresponding to the key {key}is {info[key]}')
