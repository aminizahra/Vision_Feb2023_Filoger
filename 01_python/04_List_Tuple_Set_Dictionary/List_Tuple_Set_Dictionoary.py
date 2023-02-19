#Touple
flower = ('Touple', )
print(type(flower))

marks1 = ('A', 'B', 'C', 'D')

marks2 = ('W', 'X', 'Y', 'Z') # You can change all members of the touple

#print(marks)

all_marks = marks1 + marks2

print(all_marks)


#Dict
mt_dict = {}

print(type(mt_dict))

user ={'first_name':'Ali',
       'last_name':'Farajnia',
       'age':25}

#active!
user['active'] = True
print(user)

print(user['first_name'])
print(user['last_name'])

print(user.get('age'))


age = user.get('age')
print(age)


del user['active']
print(user)


#loop dict
for Key in user:
    print (Key)

#Set
mt_set = {}
print(type(mt_set))

mt_set2 = set()
print(type(mt_set2))

#unique member
courses_set = set(['py', 'dip', 'dl', 'py', 'cv'])
print(courses_set)

size_set = len(courses_set)
print(size_set)

for element in courses_set:
    print(element)
    
#remove
#discard
#pop

# courses_set.remove('C++')   #error

courses_set.discard('C++')  #handell error

print(courses_set)
courses_set.pop() #del first element
print(courses_set)











