'''
    Operaciones:
        1. sumar
        2. restar
        3. multiplicar
        4. dividir

'''

dictionary = {
    'suma' : (lambda x,y : x + y ),
    'resta' : (lambda x,y : x - y ),
    'multiplicacion' : (lambda x,y : x * y),
    'division' : (lambda x,y : x / y)
}


def collect(dictionary):
    # we convert dictionary into a list so it can be accessed by "key index"
    dicList =  list(enumerate(dictionary, start=1))
    for index, value in dicList:
        print(" Opcion #{} : {} ".format(index,value))
    option = int(input("Seleccione una opcion: "))
    # if the option is not in the dictionary's lenght ERROR
    if option not in range(len(dicList)+1):
        print(" Opcion no valida.")
    else:
        print("la opcion seleccionada es:", dicList[option-1][1])
        print(dictionary.get(dicList[option-1][1]))

    



collect(dictionary)
