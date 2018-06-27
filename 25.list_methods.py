tup="samsung"
print("1.",list(tup))
list1=(3,67,14)
print('2.',sorted(list1))       #to get the list in sorted order
avengers=[]                  #adding elements to the given list
avengers.append("capitan-america")
avengers.append("thor")
print('3.',avengers)

list1=['sas','pas','cas']      #for a list or tuple to get extended
list2=['has','was','oas']
list1.extend(list2)
print('4.',list1)
name="qwrt1"
list1.extend(name)
print('5.',list1)


#append vs extend
a=['we','ty','fg','nm']
b=['sd','xc','gh','jk']
a.extend(b)
print('6.',a)
a.append(b)
print('7.',a)


#to find the occurence of a particular item
a=['a','t','a','u','e','a','u','t','o','n']
print('8.',a.count('a'))
print('9.',a.count('u'))

#for inserting an element
a=['sas','eas','was','qas']
a.insert(3,'das')
print('10.',a)


#for deleting an element
a.remove('das')
print('11.',a)


#sorting list
list1 = [5, 6, 7, 1, 4, 2, 0, 4, 2, 8]
list1.sort()
print('12.',list1)
list1.sort(reverse=True)
print('13.',list1)


#to print elements in reverse order
list1=['qwe','ergh','hjk','yuio']
list1.reverse()
print('14.',list1)

