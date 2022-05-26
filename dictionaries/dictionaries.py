mydict = {
    "book":"Dynamics",
    "Publisher":"longhorn",
    "year":2001,
    "Authors": ['Elon musk','Paul levesque'],
    "Good": True,
    
}
print(mydict.keys())
print(mydict.values())
print(mydict.get('book'))
print(mydict.items())

if 'Publisher' in mydict:
    print("Publisher is a key")

