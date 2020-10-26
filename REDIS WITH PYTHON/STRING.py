# importing redis module

import redis

# calling redis with its port number on the local machine with an object instance
r = redis.Redis(host='localhost', port=6379, db=0)

# printing empty line
print()

# setting the key and value
print("Did the value is set for the specified key ? :",r.set('Name', 'Ajay')) # prints ture if value is set to the key

# printing empty line
print()

# getting the value from the specified key
print("The Value of the Specified key 'Name' is :",r.get('Name')) # print the value of the key specified

