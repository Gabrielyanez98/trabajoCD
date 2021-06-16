import mysql.connector



class AdminEntidades():
    def __init__(self):
        pass

    def insert(idioma):
        
        
        cnx = mysql.connector.connect( user='root', password='root', host='localhost', database='trabajocd')
        cursor = cnx.cursor()
        insert = "INSERT INTO idioma (nombre) VALUES ('%s')" % (idioma)
        cursor.execute(insert)
        cnx.commit()
        cursor.close()
        cnx.close()


    def delete(self):

        cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='trabajocd')
        cursor = cnx.cursor()
        delete = "DELETE FROM idioma WHERE idIdioma = %i" % ()
        cursor.execute(delete)
        cnx.commit()                 
        cursor.close()
        cnx.close() 


    def update(self):

        cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='trabajocd')
        cursor = cnx.cursor()
        update = "UPDATE idiomas SET idioma = '%s' WHERE idIdioma = %i" % ('Catalán', 1)
        cursor.execute(update)
        cnx.commit()                           
        cursor.close()
        cnx.close() 


    def getAll():

        cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='trabajocd')
        cursor = cnx.cursor()
        update = "SELECT * FROM idiomas"
        cursor.execute(update)
        cnx.commit()                           
        cursor.close()
        cnx.close()

    def getById():

        cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='trabajocd')
        cursor = cnx.cursor()
        update = "SELECT idIdiomas FROM idIdiomas"
        cursor.execute(update)
        cnx.commit()                           
        cursor.close()
        cnx.close()
    

   