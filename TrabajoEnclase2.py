import os

class OperasBas():
    # declaración de constructor
    def _init_(self):
        pass
    # declaración de métodos

    def suma(self, num1, num2):
        res = num1 + num2
        return res

    def resta(self, num1, num2):
        res = num1 - num2
        return res

    def multi(self, num1, num2):
        res = num1 * num2
        return res

    def div(self, num1, num2):
        res = num1 / num2
        return res


def main():
    ob = OperasBas()
    opt = -1
    res = 0
    print("Bienvenido a operaciones basicas seleccione la operacion a realizar!")
    while (opt != 0):
        opt = int(
            input('1.- Suma\n 2.- Resta\n 3.- Multiplicación\n 4.- División\n 5.- Salir\n'))
        if (opt == 5):
            break
        os.system('clear')
        num1 = int(input('Ingresa el primer número:'))
        num2 = int(input('Ingresa el segundo número:'))
        if (opt == 1):
            res = ob.suma(num1, num2)
        elif (opt == 2):
            res = ob.resta(num1, num2)
        elif (opt == 3):
            res = ob.multi(num1, num2)
        elif (opt == 4):
            res = ob.div(num1, num2)
        print('El resultado es: {}'.format(res))
        
if __name__ == "__main__":
    main()               
          