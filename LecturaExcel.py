#Importar pandas
import pandas as pd
#Crea un Data Frame y asignamos la lectura del archivo excel
df=pd.read_excel()
#Reescribimos el Data Frame, quitando las filas que tienen el valor de la 
#columna email duplicado
df=df.drop_duplicates(columna="email")
#Imprimimos la columna email
for i in df.index:
  print(df["Email][i])
