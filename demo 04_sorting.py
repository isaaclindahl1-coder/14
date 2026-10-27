names = ["Evan", "Jace", "Zach", "Mykyta", "Isaac", "Allyn"]
# . sort method
print(names)
names.sort() # defults to all cappitalz first
print(names)

#sort in reverse order
names.sort(reverse=True)
print(names)

# other_names = ("blake", "michael", "")
# but we can sort a tuple IF we use sorted:
sorted_other_names = sorted()


#sort by length of string
len_of_name_sorted = sorted(other_names, key)


lambda s: len(list(filter(lambda c: c.lower() in 'aeiou', s)))
 