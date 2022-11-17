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

#How to update value on a particular key

