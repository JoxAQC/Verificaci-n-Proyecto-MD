# Violación:
    
    def calcularVentaComidas():
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

    def calcularBebidaPotencial():
        arregloTotal=[]
        with open(file_path4, "r") as f:
            pagos = json.load(f)
        for element in pagos:
            arregloTotal.append(element["ID"])
        tipo = "bebida"
        listaBebidas = Preferencia.clasificarProductos(arregloTotal,tipo)
        lista = pd.Series(listaBebidas) 
        resultados = pd.Series(lista.value_counts())
        arreglo = numpy.array(resultados)
        cantPotencial = arreglo[0]
        for element in listaBebidas:
            if listaBebidas.count(element) == cantPotencial:
                bebidaPotencial = element
        with open(file_path2, "r") as f:
            productos = json.load(f)
        for element in productos:
            if element["ID"]==bebidaPotencial:
                bebida = element["Nombre"]
                precio = element["Precio"]
        print("--> La bebida más vendida fue: "+str(bebida))
        return precio*cantPotencial

    def calcularComidaPotencial():
        arregloTotal=[]
        with open(file_path4, "r") as f:
            pagos = json.load(f)
        for element in pagos:
            arregloTotal.append(element["ID"])
        tipo = "comida"
        listaComidas = Preferencia.clasificarProductos(arregloTotal,tipo)
        lista = pd.Series(listaComidas) 
        resultados = pd.Series(lista.value_counts())
        arreglo = numpy.array(resultados)
        cantPotencial = arreglo[0]
        for element in listaComidas:
            if listaComidas.count(element) == cantPotencial:
                comidaPotencial = element
        with open(file_path2, "r") as f:
            productos = json.load(f)
        for element in productos:
            if element["ID"]==comidaPotencial:
                comida = element["Nombre"]
                precio = element["Precio"]
        print("--> La comida más vendida fue: "+str(comida))
        return precio*cantPotencial


# Correción:

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
                bebida_potencial = element
        with open(file_path2, "r") as f:
            productos = json.load(f)
        for element in productos:
            if element["ID"]==bebida_potencial:
                bebida = element["Nombre"]
                precio = element["Precio"]
        print("--> La bebida más vendida fue: "+str(bebida))
        return precio*cant_potencial

    def calcular_comida_potencial(self):
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


# Descripción de cambios: 
## 1. Añadido self en las funciones de instancia:
 - Problema original: Las funciones calcularVentaComidas, calcularBebidaPotencial y calcularComidaPotencial no tenían el parámetro self y no estaban definidas como métodos de instancia.
 - Corrección: Se agregó self como primer parámetro en todas las funciones. Esto indica que las funciones pertenecen a una instancia específica de la clase Administrador y pueden acceder a los atributos y otros métodos de la instancia.
 - Impacto: Esto permite usar estos métodos como parte de un objeto instanciado de la clase, lo que es el comportamiento esperado para métodos que operan en la instancia.
## 2. Convenciones de nombres en variables:
 - Problema original: Algunos nombres de variables no seguían las convenciones de estilo de Python (PEP 8), como arregloTotal, listaBebidas, cantPotencial, etc.
 - Corrección: Se cambiaron los nombres de variables a un formato más acorde a PEP 8, es decir, en snake_case. Por ejemplo:
    - arregloTotal → arreglo_total
    - listaBebidas → lista_bebidas
    - cantPotencial → cant_potencial
 - Impacto: Este cambio mejora la legibilidad y coherencia del código con las convenciones estándar de Python, haciéndolo más claro y mantenible para otros desarrolladores.
## 3. Renombre de función para seguir convención:
 - Problema original: La función calcularComidaPotencial no seguía las convenciones de nomenclatura de funciones en Python (debería estar en snake_case).
 - Corrección: Se renombró la función de calcularComidaPotencial a calcular_comida_potencial.
 - Impacto: Esto mejora la consistencia del código con la convención de nombres en Python (usar minúsculas y guiones bajos para los nombres de funciones), haciéndolo más legible y profesional.