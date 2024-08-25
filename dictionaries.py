#creando un diccionario person
person = {
    'first_name':'Odette',
    'last_name':'Salazar',
    'age':1,
    'country':'Mexico',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

#Largo del diccionario
print(len(person))

#Accediendo a elemetos del diccionario
print(person['address'])
print(person['country'])

#utilizando get
print(person.get('first_name')) 
print(person.get('country'))

#Agregando elementos a un diccionario
person['job_title'] = 'Developer'
person['skills'].append('React')
print(person)

#modificando elementos en diccionario
person['first_name'] = 'Veronica'
person['age'] = 9
print(person)

#Checando keys en un diccionario
print('first_name' in person)
print('cellphone' in person)

#eliminando keys y value pairs de un diccionario
person.pop('first_name')        # elimina el elemento de first_name
person.popitem()                # elimina el elemento address 
del person['is_marred']        # elimina el elemento is_married 

#copiando un
dct_copy = person.copy()

#Obtener claves de diccionario como una lista
keys = person.keys()
print(keys)

#Obtener valores de diccionario como una lista
values = person.values()
print(values) 

#cambiando diccionario a lista de elementos
print(person.items())

#limpiando un diccionario
print(person.clear())

#eliminando diccionario
del person

#ejercicios
dog = {
    'name':'canela',
    'color':'brown',
    'breed':'Meztiza',
    'gender':'female',
    'age': 69
}

student = {
    'first_name':'Abel',
    'last_name':'Salazar',
    'gender':'Male',
    'age': 36,
    'marital_status': 'Married',
    'skills':['developer','JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 
    'country':'Mexico', 
    'city':'Puebla',
    'address':{
        'street':'via de roma',
        'zipcode':'32575'
        }
}

print('Datos en diccionario de estudiante:',len(student))
print(student.get('skills'))
student['job_title'] = 'Developer in Python'
student['skills'].append('HTML')
print(student)
print(student.keys())#claves del diccionario
print(student.values())#valores del diccionario 
print(student.items())#tuplas
del student['skills']
print('Eliminando skills:',student)
del student #eliminando dictionary student