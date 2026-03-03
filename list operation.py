#create a list
countries=["UAE","IRAN","USA","JAPAN","MORROCO",]
print(countries)

#lenght/amount of words in a list
print(len(countries))

#fetching/indexing a item

print(countries[2])
print(countries[len(countries)-1])

#retive all items
for i in range(len(countries)):
    print(countries[i])
for i in countries:
    print(i)

# add item
countries.append("india")
print(countries)