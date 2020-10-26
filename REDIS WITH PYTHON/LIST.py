# importing redis module

import redis

# calling redis with its port number on the local machine with an object instance
r = redis.Redis(host='localhost', port=6379, db=0)

# printing empty line
print()

name = 'Names'

# seting the key and value for list
print("\nHow many value is pushed to for the specified key in a list ? :",r.lpush(name, 'Ajay', 'Aj', 'Maayon')) # prints ture if value is set to the key

# printing empty line
print()

# geting the value from the specified key
print("\nThe Value of the Specified key 'Names' is :\n") 

for i in range(0, r.llen(name)):
    print(r.lindex(name,i)) # print the value of the key specified

# deleting values present inside the list for specified key
for i in range(0, r.llen(name)):
    r.lpop(name)


# geting the value from the specified key after deleting
print("\nThe Value of the Specified key 'Names' after deleting :\n") 

for i in range(0, r.llen(name)):
    print(r.lindex(name,i)) # print the value of the key specified




