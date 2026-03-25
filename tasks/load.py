import mysql.connector


def load(data):
    resultado = 0
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root2025',
            database='db_g7'
        )
        cursor = conn.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pais(
                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        nombre VARCHAR(255) NOT NULL,
                        capital VARCHAR(255) NOT NULL,
                        region VARCHAR(255),
                        poblacion BIGINT);
                    """)
        conn.commit()
        
        insert_query = """
                    INSERT INTO pais(nombre, capital, region, poblacion)
                    VALUES(%(nombre)s, %(capital)s, %(region)s, %(poblacion)s)
                    """
            
        cursor.executemany(insert_query,data)
        conn.commit()
        resultado = cursor.rowcount
        cursor.close()
        conn.close()
    
    except Exception as e:
        print(f"ERROR AL CARGAR DATOS: {e}")
    
    return resultado