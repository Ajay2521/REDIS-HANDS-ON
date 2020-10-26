# importing redis module

import redis

# calling redis with its port number on the local machine with an object instance
r = redis.Redis(host='localhost', port=6379, db=0)

nameAge = "NameAge" 

# seting the key and value
print("\nDid the value is set for the specified key in hash ?:",r.hset(nameAge, 'Ajay',19)) # prints ture if value is set to the key
print("\nDid the value is set for the specified key in hash ?:",r.hset(nameAge, 'Aj',18)) # prints ture if value is set to the key
print("\nDid the value is set for the specified key in hash ?:",r.hset(nameAge, 'Maayon',2)) # prints ture if value is set to the key

# getting the keys present in the hash
print("\nThe keys present in the given hash is :",r.hkeys(nameAge))

# getting the values present in the hash
print("\nThe values present in the given hash is :",r.hvals(nameAge))

# getting the keys and values present in the hash
print("\nThe values present in the given hash is :",r.hgetall(nameAge))
