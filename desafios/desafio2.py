print('='*60)


salario = float(input('{0}Digite o salario liquido: '.format(' '*5)))


print('{}O salario liquido é: R${:7.2f}'.format( ' '*5 ,salario))
print('{}Gastos E: R${:7.2f}'.format( ' '*5 ,salario*0.5))
print('{}Investimentos LP: R${:7.2f}'.format( ' '*5 ,salario*0.2))
print('{}Inverstimentos CP: R${:7.2f}'.format( ' '*5 ,salario*0.1))
print('{}Livre: R${:7.2f}\n'.format( ' '*5 ,salario*0.2))



print('='*60)