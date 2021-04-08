import pandas as pd
columns = ['Año', 'Clave_Ent', 'Entidad', 'Cve. Municipio', 'Municipio',
        'Tipo de delito',  'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

delitos = pd.read_csv("Municipal-Delitos-2015-2021_feb2021.csv", encoding= "Latin-1", 
                      usecols= columns)


delitos[delitos["Tipo de delito"]== "Abuso sexual"].to_csv("Abusosexual2015_2021.csv", header=True)

print('Realizado filtro de Abuso sexual ')
