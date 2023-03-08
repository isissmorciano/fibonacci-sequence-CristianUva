#Cristian Uva 3M
#Calcolare l'n-esimo numero della successione di Fibonacci. (Iterativo)

def iterative_fibonacci(n: int) -> int:
    #Inizializziamo i primi 2 numeri della successione di Fibonacci
    primo_numero, secondo_numero = 0, 1
    #Se n è 0 o 1, restituisce il valore corrispondente
    if n == 0:
        return primo_numero
    if n == 1:
        return secondo_numero
    #Calcoliamo i successivi numeri della successione di Fibonacci in modo iterativo
    for i in range(2, n+1):
        terzo_numero = primo_numero + secondo_numero
        #Aggiorniamo i valori di primo_numero e secondo_numero
        primo_numero, secondo_numero = secondo_numero, terzo_numero
    return terzo_numero

#MAIN
#Inserimento del numero
n = int(input("Inserisci un numero intero positivo: "))
risultato = iterative_fibonacci(n)
print(risultato)