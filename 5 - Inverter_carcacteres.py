palavraInvertida = input("Digite uma palavra para ser invertida: ")
tamanhoPalavra = len(palavraInvertida)
i=0

while i < tamanhoPalavra:
    print(palavraInvertida[tamanhoPalavra-i-1],end="")    
    i=i+1