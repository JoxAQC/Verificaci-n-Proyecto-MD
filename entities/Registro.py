import datetime
import json

file_path = "files/pedidos.json"
file_path2 = "files/productos.json"

class Registro:
    def __init__(self, num_pedidos,monto):
        self._num_pedidos = num_pedidos
        self._monto = monto
        self._fecha = str(
            datetime.datetime.strftime(datetime.datetime.now(), "%d/%m/%Y %H:%M:%S")
        )

    def registrar(self):
        registran = dict(fecha=self._fecha,num_pedidos=self._num_pedidos,monto=self._monto)
        with open(file_path, "r") as f:
            data = json.load(f)
            
        data.append(registran)

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

