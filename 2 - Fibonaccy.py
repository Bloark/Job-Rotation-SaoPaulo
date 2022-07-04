#Sequencia de Fibonacci

def validadorFibonacci(numeroUsuario):
    numeroInicial = 0
    somaFibonacci = 1
    while numeroInicial <= numeroUsuario:
               
        if numeroUsuario == numeroInicial or somaFibonacci== numeroUsuario:
            return True
        else:
            numeroInicial = numeroInicial + somaFibonacci
            somaFibonacci = numeroInicial + somaFibonacci
           
    if numeroInicial == numeroUsuario or somaFibonacci== numeroUsuario:
        return True
    else:
        return False
print("Fibonacci Verficador");
numeroUsuario=input("Informe o numero: ")
numeroUsuario=int(numeroUsuario)
resultado = validadorFibonacci(numeroUsuario)
if resultado == True:
    print("O número informado pertence a sequência de Fibonacci")
else:
    print("O número informado não pertence a sequência de Fibonacci")