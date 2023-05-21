name = "Iván"
last_name = "Alarcón Vallejos"
age = 31
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "Soy Iván"
print (quote)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print (template)

template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print (template2)

template3 = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template3)

template4 = f"Hola mi nomvre completo es {name} {last_name} y tengo {age} años"
print (template4)