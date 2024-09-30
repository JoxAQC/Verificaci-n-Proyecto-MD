from entities.user import Usuario
import json
from werkzeug.security import check_password_hash
import pandas as pd 
from processes.preferencia import Preferencia              
import numpy

file_path = "files/adminDatos.json"
file_path1 = "files/pedidos.json"
file_path2 = "files/productos.json"
file_path3 = "files/bebidas.json"
file_path5 = "files/comidas.json"
file_path4 = "files/pagos.json"

class Administrador(Usuario):
    def __init__(self, usuario, contrasenia, nombre, apellido, correo, llave_maestra):
        super().__init__(usuario, contrasenia, nombre, apellido, correo)
        self._llaveMaestra = llave_maestra

    def verify_session(self, given_user, given_password):
        with open(file_path, "r") as f:
            usuario = json.load(f)

        for element in usuario:
            if element["usuario"] == given_user and check_password_hash(
                element["contrasenia"], given_password
            ):
                print("Bienvenido, " + element["nombre"])
                llave = input("Ingrese su llame maestra para continuar: ")
                while check_password_hash(element["llave_maestra"], llave) == False:
                    print("Llave maestra incorrecta, intentelo nuevamente, por favor")
                    llave = input("Ingrese su llame maestra para continuar: ")
                return Administrador(
                    element["usuario"],
                    element["contrasenia"],
                    element["nombre"],
                    element["apellido"],
                    element["correo"],
                    element["llave_maestra"]
                )

    def calcularVentaTotal(self):
        venta = 0
        with open(file_path4, "r") as f:
            pagos = json.load(f)
        for element in pagos:
            with open(file_path2, "r") as f:
                productos = json.load(f)
            for producto in productos:
                if element["ID"]==producto["ID"]:
                    venta = venta + producto["Precio"]    
        return venta

    def calcularVentaBebidas(self):
        venta = 0
        with open(file_path3, "r") as f:
            bebidas = json.load(f)
        for bebida in bebidas:   
            with open(file_path4, "r") as f:
                pagos = json.load(f)
            for element in pagos:
                    if element["ID"] == bebida:
                        with open(file_path2, "r") as f:
                            productos = json.load(f)
                        for producto in productos:
                            if producto["ID"] == element["ID"]:
                                venta += producto["Precio"]
        return venta

    def calcularVentaComidas(self):
        venta = 0
        with open(file_path5, "r") as f:
            comidas = json.load(f)
        for comida in comidas:   
            with open(file_path4, "r") as f:
                pagos = json.load(f)
            for element in pagos:
                    if element["ID"] == comida:
                        with open(file_path2, "r") as f:
                            productos = json.load(f)
                        for producto in productos:
                            if producto["ID"] == element["ID"]:
                                venta += producto["Precio"]
        return venta

    def calcularPorcentaje(self, total,subtotal):
        porcentaje = float(subtotal/total*100.00)
        return porcentaje

    def calcularBebidaPotencial(self):
        arreglo_total=[]
        with open(file_path4, "r") as f:
            pagos = json.load(f)
        for element in pagos:
            arreglo_total.append(element["ID"])
        tipo = "bebida"
        lista_bebidas = Preferencia.clasificarProductos(arreglo_total,tipo)
        lista = pd.Series(lista_bebidas) 
        resultados = pd.Series(lista.value_counts())
        arreglo = numpy.array(resultados)
        cant_potencial = arreglo[0]
        for element in lista_bebidas:
            if lista_bebidas.count(element) == cant_potencial:
                bebida_botencial = element
        with open(file_path2, "r") as f:
            productos = json.load(f)
        for element in productos:
            if element["ID"]==bebida_botencial:
                bebida = element["Nombre"]
                precio = element["Precio"]
        print("--> La bebida más vendida fue: "+str(bebida))
        return precio*cant_potencial

    def calcularComidaPotencial(self):
        arreglo_total=[]
        with open(file_path4, "r") as f:
            pagos = json.load(f)
        for element in pagos:
            arreglo_total.append(element["ID"])
        tipo = "comida"
        lista_comidas = Preferencia.clasificarProductos(arreglo_total,tipo)
        lista = pd.Series(lista_comidas) 
        resultados = pd.Series(lista.value_counts())
        arreglo = numpy.array(resultados)
        cant_potencial = arreglo[0]
        for element in lista_comidas:
            if lista_comidas.count(element) == cant_potencial:
                comida_potencial = element
        with open(file_path2, "r") as f:
            productos = json.load(f)
        for element in productos:
            if element["ID"]==comida_potencial:
                comida = element["Nombre"]
                precio = element["Precio"]
        print("--> La comida más vendida fue: "+str(comida))
        return precio*cant_potencial