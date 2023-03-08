#Cristian Uva 3M
#Calcolare l'n-esimo numero della successione di Fibonacci. (Ricorsivo)

#Creo la funzione "recursive_fibonacci", per calcolare il numero di fi
def recursive_fibonacci(n: int) -> int:
    #In caso è 0 o 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    #In caso non è 0 o 1 somma i 2 numeri precedenti.
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

#MAIN
#Inserimento del numero
n = int(input("Inserisci un numero intero positivo: "))
risultato = recursive_fibonacci(n)
print(risultato)
