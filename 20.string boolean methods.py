a="life should be great rather than long"
print(a.endswith('g'))
print(a.endswith('fe',0,4))
print(a.endswith('fe',2,6))
print(a.startswith('li'))
print(a.startswith('s',5,15))

#__gives true when string contains only letters__
a="asdf"
print(a.isalpha())
b="qwer34"
print(b.isalpha())



#__gives true when string contains only characters__
a="hello123"
print(a.isalnum())
b="hello123#"
print(b.isalnum())


#__gives true when string contains only digits__
a="123456"
print(a.isdigit())
b="1234ghj"
print(b.isdigit())


#__deals with only white spaces__
a="  "
print(a.isspace())
b="hello "
print(b.isspace())


#__gives true when the string is title__
a="Samsung Galaxy"
print(a.istitle())
b="samsung Galaxy"
print(b.istitle())


#__to check for lower case__
a="samsung"
print(a.islower())
b="samsung136%"
print(b.islower())
c="SAmSUng"
print(c.islower())


#__to check for uper case__
a="SAMSUNG$@#78"
print(a.isupper())
b="wefo"
print(b.isupper())

