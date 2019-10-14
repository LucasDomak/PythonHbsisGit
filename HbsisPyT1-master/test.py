class Bier:

    @property
    def teor(self):
        return self.__teor    

    @property
    def ibu(self):
        return self.__ibu

    @property
    def tipo(self):
        return self.__tipo


    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo
    
    @teor.setter
    def teor(self,teor):
        self.__teor = teor
    
    @ibu.setter
    def ibu(self,ibu):
        self.__ibu = ibu

bier1 = Bier()

bier1.tipo = 'coe'
bier1.teor = 561561
bier1.ibu = 123123


print('='*50)
print('\n'*2)

print(bier1.teor,bier1.ibu,bier1.tipo)

print('\n'*2)
print('='*50)