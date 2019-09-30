print('='*50)


frase = input('{0}Digite uma frase: '.format(' '*5))
letra = input('{0}DIga uma letra: '.format(' '*5))


print('{0}A letra foi encontrada {1} vezes'.format( ' '*5 ,frase.count(letra)))
print('{0}A letra foi encontradana na posicao {1} pela primeira vez'.format( ' '*5 ,frase.index(letra)))
print('{0}A letra foi encontrada na posicao {1} pela ultima vez'.format( ' '*5 ,frase.rindex(letra)))

print('='*50)