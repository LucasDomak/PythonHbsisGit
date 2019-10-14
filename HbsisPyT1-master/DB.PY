import MySQLdb

conexao_mysql = MySQLdb(host ='localhost', database='zuplae01', user='root',passwd='luquinhas19')


cursor = conexao_mysql.cursor()

cursor.execute('SELECT * FROM TIPO')

