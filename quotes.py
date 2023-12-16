import requests
from bs4 import BeautifulSoup

try:
    response = requests.get("https://dolarhoy.com/")

    if response.status_code == 200:
        soup=BeautifulSoup(response.text,"html.parser")
        dolar = soup.find('div', class_="tile dolar")
        for i in dolar:
            bloques=i.find_all('div', class_="tile is-child")
            for j in bloques:
                titulo=j.find('a', class_="title")
                compra=j.find('div', class_="compra")
                venta=j.find('div', class_="venta")
                if titulo.text != 'Dólar Tarjeta':
                    print(titulo.text)
                    print(f"Compra {(compra.find('div', class_='val').text)}")
                    print(f"Venta {(venta.find('div', class_='val').text)}")
                else:
                    print(titulo.text)
                    print(f"Venta {(venta.find('div', class_='val').text)}")
                    
                print("******************\n")
            
        print("Solicitud realizada correctamente")
    else:
        print("Algo salió mal")

except requests.exceptions.ConnectionError:
    print("Error de conexión")