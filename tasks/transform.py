from datetime import datetime

def transform(data):
    """
    transformamos la data de randomuser
    """
    transform_data = []
    for pais in data:
        nombre = pais['name']['common']
        capital = pais['capital'][0] if 'capital' in pais else 'Sin capital'
        region = pais.get('region', 'Sin región')
        poblacion = pais.get('population', 0)
        
        transform_data.append({
            "nombre": nombre,
            "capital": capital,
            "region": region,
            "poblacion": poblacion
        })
    return transform_data