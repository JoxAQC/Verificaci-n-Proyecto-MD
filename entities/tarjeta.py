from entities.metodos import Metodo
import datetime
import json
from werkzeug.security import check_password_hash

file_path = "files/tarjetas.json"


class Tarjeta(Metodo):
    def __init__(self, num_tarjeta, fech_caducidad, cod_seguridad, nom_tarjeta, apell_tarjeta, emisor_tarjeta):
        self.__emisor = emisor_tarjeta
        self._numTarjeta = num_tarjeta
        self.__fechCaducidad = fech_caducidad
        self.__codSeguridad = cod_seguridad
        self.__nombTarjeta = nom_tarjeta
        self.__apellTarjeta = apell_tarjeta

    def verificar(self):
        passed = False
        with open(file_path, "r") as f:
            tarjetas = json.load(f)

        for element in tarjetas:
            p = True if element["emisor"] == self.__emisor else False
            q = check_password_hash(element["numTarjeta"], str(self._numTarjeta))
            r = check_password_hash(element["fechCaducidad"], self.__fechCaducidad)
            s = check_password_hash(element["codSeguridad"], str(self.__codSeguridad))
            t = True if element["nombTarjeta"] == self.__nombTarjeta else False
            u = True if element["apellTarjeta"] == self.__apellTarjeta else False
            if p and q and r and s and t and u:
                passed = True
        return passed

    def verificarCaducidad(self):
        passed = False
        fecha_actual = datetime.datetime.now()
        fecha_v = datetime.datetime.strptime(self.__fechCaducidad, "%m/%Y")
        if fecha_v > fecha_actual:
            passed = True
        return passed

    def verificarBloqueo(self):
        passed = False
        with open("files/numeroBloqueado.json", "r") as f:
            numeros_bloqueados = json.load(f)

        for element in numeros_bloqueados:
            if element["numero"] == self._numTarjeta:
                passed = True
        return passed
