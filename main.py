from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load
from tabulate import tabulate

def main():
    data = extract()
    print(data[0])
    data_transform = transform(data)
    resultado = load(data_transform)
    print(f' se insertaron {resultado} registros en la base de datos')
    
if __name__ == "__main__":
    main()