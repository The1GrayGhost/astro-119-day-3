#string

s="I am a string"
print(type(s))       #will say str

yes=True
print(type(yes))

no=False
print(type(no))

#lists

alpha_list=["a", "b", "c"]
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

#tuple

alpha_tuple=("a", "b", "c")
print(type(alpha_tuple))

try: 
	alpha_tuple[2]="d"
except TypeError:
	print("We can't add elements to tuples!")
print(alpha_tuple)		