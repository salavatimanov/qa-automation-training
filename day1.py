from operator import truediv

print('hello world')

num = 7
fl = 7.77
name = 'Salavat'
users = ['Salavat', 'Daniil', 'Artem']
auth = {'salavat' : '1234'}
num_set = {1,2,3}

result = num + fl
print(result)


fstring = f'Hello, {name} '
print(fstring)


check = 7 > 5
print(check)


print(users[0])

users.append('Misha')
print(users)

users.insert(0, 'Egor')
print(users)

print(auth['salavat'])
auth['daniil'] = '4321'

print(auth)

nums = [1,2,2,6,6,6,6,77,77,7,8,8,8,8]
unique = set(nums)
print(unique)
unique.add(29)
print(unique)
