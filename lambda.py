#dictionary inside lists
people=[
{"name": "Rita", "city":"Bhopal" },
{"name": "Girwar", "city": "Jodhpur"},
{"name": "Priyanshi", "city": "Bareily"}
]

#def f(person):
    #return person["name"]

#people.sort(key= f)

people.sort(key = lambda person: person["name"])
print(people)
