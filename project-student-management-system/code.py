# --------------
# Code starts here
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
print(new_class)
new_class.append('Peter Warden')
new_class.remove('Carla Gentry')
print(new_class)

# Code ends here


# --------------
# Code starts here
courses={'Math': 65,'English':70,'History':80,'French':70,'Science':60}
b=courses.values()
total=sum(b)
percentage=(total/500)*100
print(percentage)

# Code ends here


# --------------
# Code starts here

mathematics={'Geoffrey Hinton':78,
'Andrew Ng':95,
'Sebastian Raschka':65,
'Yoshua Benjio':50,
'Hilary Mason':70,
'Corinna Cortes':66,
'Peter Warden':75}
topper= max(mathematics,key = mathematics.get)
print (topper)


# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here


# Create variable first_name 
first_name = (topper.split()[0])
print (first_name)

# Create variable Last_name and store last two element in the list
last_name = (topper.split()[1])
print (last_name)

# Concatenate the string
full_name = last_name + ' ' + first_name

# print the full_name
print (full_name)

# print the name in upper case
certificate_name = full_name.upper()

print (certificate_name)

# Code ends here


