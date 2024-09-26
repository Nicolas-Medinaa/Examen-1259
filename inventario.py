class inventario:
    def __init__(self,ID,marcas, modelos,proveedor,cantidad,años,sucursal):
        self.años=años
        self.sucursal=sucursal
        self.ID=ID
        self.marcas=marcas
        self.modelos=modelos
        self.proveedor=proveedor
        self.cantidad=cantidad

    def mostrar1259(self):
        print("sucursal", self.sucursal)
        print("año del telefono", self.años)
        print("Datos del Proveedor", self.proveedor)
        print("modelos de celular", self.marcas)
        print("marcas", self.modelos)
        print("años", self.proveedor)
        print("cantidad", self.cantidad)

    def listas_id1259(self):
        id1259=["124587","457411","454545","21141"]
        print(id1259)
        for di in id1259:
            print(di)  

    def tupla_Marcas1259(self):
        marca1259=("Iphone","Samsung","Xiaomi","Hoppo","Motorola","Mac","Honor")
        print(marca1259)
        for mar in marca1259:
            print(mar)

    def dicc_Provedor1259(self):
        proveedor1259 = {
            "Id Proveedor 1": 22308051281259,
            "Nombre":"Nicolas Medina Zubia",
            "Telefono": 6571014236,
            "Correo electronico": "a.22308051281259@cbtis.edu.mx",
            "Id proveedor 2" : 1259,
            "Nombre": "Nicolas",
            "Telefono": 1014236,
        }
        print(proveedor1259)
        for prov,edor in proveedor1259.items():
            print(f"1:{prov} 2{edor}")

    def listas_mod1259(self):
        id1259=["Plus","Max","Galaxy","G60","Pro Max"]
        print(id1259)
        for di in id1259:
            print(di)  

# Zona de ejecucion

info = inventario()

info.mostrar1259()
print("")
print("id")
print("")

info.listas_id1259()
print("")
print("Marcas")
print("")

info.tupla_Marcas1259()
print("")
print("Proveedores")
print("")
