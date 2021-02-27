# String
name = "Harry"
print(name[0])
print(name[1])

# Lists - mutable - in a particular order - sequence of mutable values
names = ["Harry", "Ron", "Rita", "Ginny"]
print(names)
print(names[0])
#mutable
names.append("Girwar")
names.sort()
print(names)

# Tuples - immutable in a particular order - sequence of immutable values
coordinate = (10.0,20.0)
print(coordinate)

# Set - Collection of unique values
s = set()
#add element to Set
s.add(1)
s.add(2)
s.add(3)
s.add(1)
print(s)
print(f"Length ",{len(s)})
s.remove(2)
print(s)
print(f"Length ",{len(s)})

# Dictionary - Collection of key-value pair
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(thisdict["brand"])
