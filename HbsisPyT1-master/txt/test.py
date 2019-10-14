
with open ('nomes.txt','a') as arquivo:
    arquivo.write('O aleki vai pagar meu almoço' + '\n')

with open ('nomes.txt','r') as arquivo:

    for l in arquivo:
        nomes = l.strip().split(' ')
        for it in nomes:
            print(it, end=' ')

        print('')
    print(nomes) 