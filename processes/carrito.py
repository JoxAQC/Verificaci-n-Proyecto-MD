import datetime
import json

file_path = "files/productos.json"
file_path2 = "files/pedidos.json"

class Carrito:
    def __init__(self, id, cantidad_seleccionada, cantidad, productos_seleccionados):
        self._id = id
        self._cantidad_seleccionada = cantidad_seleccionada
        self._cantidad = cantidad
        self._productos_seleccionados = productos_seleccionados


    def pedir_productos(self, cantidad_seleccionada):
        productos_seleccionados = []
        for i in range(cantidad_seleccionada):
            pedir1 = int(input("Ingrese el id del "+ str(i + 1)+ " producto a pedir:"))
            while (pedir1<1) or (pedir1>23):
                pedir1 = int(input("Ingrese el id del "+ str(i + 1)+ " producto a pedir:"))
            productos_seleccionados.append(pedir1)
        return productos_seleccionados

    def calcular_monto(self, productos_seleccionados):
        monto_c = 0
        for element in productos_seleccionados:
            with open(file_path, "r") as f: #abrie el json productos
                data = json.load(f)
            for productos_seleccionados in data: #matriz en el archivo
                if productos_seleccionados["ID"] == element:
                    monto_c = monto_c + productos_seleccionados["Precio"]
        return monto_c

    def nombrepd(self, productos_seleccionados):
        nombre = []
        for element in productos_seleccionados:
            with open(file_path, "r") as f: #abrie el json productos
                data = json.load(f)
            for productos_seleccionados in data: #matriz en el archivo
                if productos_seleccionados["ID"] == element:
                    nombre.append(productos_seleccionados["Nombre"])
        return nombre

    def nombre_producto(self, producto):
        with open(file_path, "r") as f: #abrie el json productos
            data = json.load(f)
        for productos_seleccionados in data: #matriz en el archivo
            if productos_seleccionados["ID"] == producto:
                nombre=productos_seleccionados["Nombre"]
        return nombre
    
    
    def preciopd(self, productos_seleccionados):
        precio = []
        for element in productos_seleccionados:
            with open(file_path, "r") as f: #abrie el json productos
                data = json.load(f)
            for productos_seleccionados in data: #matriz en el archivo
                if productos_seleccionados["ID"] == element:
                    precio.append(productos_seleccionados["Precio"])
        return precio
    
    def idpd(self, productos_seleccionados):
        id = []
        for element in productos_seleccionados:
            with open(file_path, "r") as f: #abrie el json productos
                data = json.load(f)
            for productos_seleccionados in data: #matriz en el archivo
                if productos_seleccionados["ID"] == element:
                    id.append(productos_seleccionados["ID"])
        return id


