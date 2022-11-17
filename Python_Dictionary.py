#Dictionary in Python
dict1 = {}
print(type(dict1))

#How to insert values in dictionary
dict2 = {}
dict2['name'] = 'Varshi'
dict2['age'] = 23
dict2['Hobby'] = 'Dancing'
dict2['skills'] = ['Python', 'Java']
dict2['States visited'] = ('AP', 'TS', 'KN')
dict2[564]='Random key'
print(dict2)

dict3 = {'color':'White', 'Curry':'Potato','Nationality':'Indian'}
#print(dict3)

dict2['Other details']=dict3
print(dict2)

#Check the length of dictionary
print("Length of the dictionary is: ",len(dict2)) #Number of key value pairs

#How to access value of a particular key(print value of the variable name)
print(dict2['name'])
print(dict2['skills'][0])
#temp=dict2['skills']
#print(temp[1])

print(dict2['Other details']['Nationality'])

#How to update value on a particular key(change age frm 23 to 33)
dict2['age'] = 33
print(dict2)

#How to get the keys from a dictionary
keys_total = list(dict2.keys())
print("Total keys in dict are: ", keys_total)

#How to get the values from a dictionary
values_total = list(dict2.values())
print("Total values in dict are: ", values_total)

#How to iterate on dictionary?
for k,v in dict2.items(): #dict.items() is a pre-defined method to get keys and values seperately
    print("Key is: ",k, "and value is: ",v)

#Compare dictionary 
dict3={'a':1, 'b':2, 'c':3}
dict4={'b':2, 'a':1, 'c':3}
print(dict3==dict4) #Results true because dictionaries doesn't follow sequential flow

dict3={'a':1, 'b':2, 'c':3}
dict4={'b':2, 'a':1, 'c':2}
print(dict3==dict4)

#How to delete specific key-value pair from dictionary
print(dict2)
del dict2[564]
del dict2['Hobby']

print(dict2)

#How to check if key exists in dictionary or not
print(dict2.get('age'))
print(dict2.get('skills'))
keys_in_dict = list(dict2.keys())
if 'skills' in keys_in_dict:
    print(True)
else:
    print(False)

