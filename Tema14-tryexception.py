
num1=10
num2=0


'''cuando intentas dividir un numero entre 0 o hace referencia'''
try:
    res=num1/num2
except ZeroDivisionError:   
    print('Error en el programa')
finally:
    pass

    
 
print('Fin del programa')   
