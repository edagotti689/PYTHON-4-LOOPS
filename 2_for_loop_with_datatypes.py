'''
1. We can use all data types in for loop except number.
'''

# for loop with string
s = 'sriram'
for c in s:
    print(c)

# for loop with list
names = ['sri','ram','kumar','nagesh', 'balu']
for name in names:
    print(name)

for name in names[2:]:
    print(name)

# For loop with dictionary
emp_det = {'name':'sri', 'eid':35, 'dname':'IT', 'name':'ram'}
for k in emp_det:
    print(k , emp_det[k])



