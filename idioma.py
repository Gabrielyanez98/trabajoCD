class Idioma:

    def __init__(self,  idioma):
        self.__idioma = idioma
       
    
    def getIdioma(self):
        return self.__idioma
    

    def setIdioma(self,idioma):
        self.__idioma = idioma
   
    
    def __str__(self):
        return "EL idioma es: " + self.__idioma 