from collections import Counter

def numero_mais_frequente(lista):
    contagem = Counter(lista)
    
    max_freq = max(contagem.values())
    
    mais_frequentes = [num for num, freq in contagem.items() if freq == max_freq]
    
    return mais_frequentes

numeros = [1,3,5,4,3,5,7,5,3,2,4,8,0,5,3,2,2,5,7,6,3,2,3,6,8]
print(numero_mais_frequente(numeros))