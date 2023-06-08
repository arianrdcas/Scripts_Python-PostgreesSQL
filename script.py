import pandas as pd
import psycopg2
import csv 


# Conectar a PostgreSQL
conn = psycopg2.connect(host='localhost', dbname='Prueba2Codigo', user='postgres', password='arian')

# Crear un cursor
cursor = conn.cursor()

# Nombre del archivo CSV y tabla en PostgreSQL
csv_file = 'C:/Users/yni6c/Downloads/Ventas.csv'
table_name = 'ventas2'

# Abrir el archivo CSV y leer los datos
with open(csv_file, 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Omitir la primera línea si contiene encabezados


# Iterar sobre las filas del archivo CSV e insertar en la tabla de PostgreSQL
    for row in csv_data:
        query = f"INSERT INTO {table_name} (Fecha, Provincia, Vendedor, Forma_de_pago, Producto, Categoria, Precio, Cantidad, Ventas) VALUES (%s, %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s)"
        cursor.execute(query, row)

# Confirmar los cambios y cerrar la conexión
conn.commit()
cursor.close()
conn.close()

