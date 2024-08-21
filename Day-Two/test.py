name = "Beau"
print(name)
print(name.lower())
print(name.upper())
print(name.isalpha())

num = 24.5
print(abs(num))
print(round(num))

optionlist = ["apple", "banana", "cat"]
if "apple" in optionlist:
  print("yes")

optionlist[0:2]

optiontuple = ("apple", "banana", "cat")
optiondict = {"fruit": "apple", "fruit2": "banana", "animal": "cat"}
optionset = {"apple", "banana", "cat"}
optionset2 = {"apple", "bat", "coconut"}

select = optionset & optionset2
combine = optionset | optionset2
subtract = optionset - optionset2
subtract2 = optionset2 - optionset
print(select)
print(combine)
print(subtract)
print(subtract2)
