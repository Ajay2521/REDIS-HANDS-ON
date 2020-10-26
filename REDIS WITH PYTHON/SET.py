# importing redis module

import redis

# calling redis with its port number on the local machine with an object instance
r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.sadd("Name1", "Ajay",  "Aj", "Maayon", "Aju")                               

r.sadd("Name2", "Smily", "Aj", "Vijay", "Varun")                               

r.sadd("Name3", "Ajith", "Smily", "Aj", "Vijay")

# printing the union of all the sets
print("\nUnion of Name1, Name2 ,Name3 is :\n")
print(r.sunion("Name1","Name2","Name3"))

# printing the intersection of all the sets
print("\nIntersection of Name1, Name2 ,Name3 is :\n")
print(r.sinter("Name1","Name2","Name3"))

# printing the difference of all the sets
print("\nDifference of Name1, Name2 ,Name3 is :\n")
print(r.sdiff("Name1","Name2","Name3"))