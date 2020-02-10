line_1 = "Kaneki and Rize are OP "
#SLICING
print(len(line_1))
print(line_1[::100])
a = (line_1[-8:-1])
b = (line_1[15:22])
print(a)
print(b)
if a==b:
      print(1)
else:
      print(0)
print(line_1[::-6])



#SOME FUNCTIONS 
print(type(line_1))
print(line_1.isalnum())
print(line_1.istitle())
print(line_1.endswith(" "))
print(line_1.count("k"))
print(line_1.isupper())
print(line_1.capitalize())
print(line_1.isalpha())
