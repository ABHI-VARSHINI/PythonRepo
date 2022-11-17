#Work with tuple

t1=() #empty tuple
#failed assignment and append
#print(t1.append(5)) #AttributeError: 'tuple' object has no attribute 'append' because tuples are immutable
#t1[0] = 3

t2 = (20, 30, 40, 50)
print(len(t2))

#Indexing also works for tuple, print 3rd element from the tuple
print(t2[2])

#In tuples indexing, slicing and iteration also works

