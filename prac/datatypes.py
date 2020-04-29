#integer
i = 28 
print(i)
#float
f = 20.4
print(f)
#boolean
b = True
print(b)
#None
n = None
print(n)

#formatted string --> not working!??!

name2 = "kazi"
print("hello, {}!".format(name2))

#string, character list, --> Sequence
name = "Shishir"
print(name)
print( name[3] )

coordinates = (10.0, 20.0)
print( coordinates[1] )

#list
names = ["Kazi","Musharrof", "Shishir"]
print(name)
print(name[2])

# --> Set

setOfNumber = set()
setOfNumber.add(1)
setOfNumber.add(3)
setOfNumber.add(5)
print( setOfNumber )

#dictionary

ages = { "Kazi": 20, "Musharrof": 24 }
ages["Kazi"] += 2
ages["Shishir"] = 23

print( ages )
