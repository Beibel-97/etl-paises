import requests

def extract():
    """
    Extraer data de randomuser
    """
    URL = "https://restcountries.com/v3.1/region/America"
    response = requests.get(URL)
    
    try:                                                
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"ERROR AL CONECTAR CON LA API: {response.status_code}")
            return []
    except Exception as e:
        print(f"ERROR DE CONEXIÓN: {e}")
        return []  