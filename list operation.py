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

#remove
countries.remove("USA")
print(countries)

#update
countries[3]="brazil"
print(countries)

#find index
p=countries.index("brazil")
print(p)
countries[p]="BRAZIL"
print(countries)

#if a item exits or not
print ("JAPAN"in countries)
print ("JAPAN"not in countries)