# ejercicio 7 y 8
class cuenta():
    def __init__(self, titular:str, edad:int,cantidad:float = 0.0 ):
        self.titular = titular
        self.cantidad = cantidad
        self.edad = edad
    def get_titular(self):
        return self.titular

    def set_titular(self, nuevo_titular:str):
        self.titular = nuevo_titular
        
    def get_edad(self):
        return self.edad
    
    def get_cantidad(self, cantidad):
        if cantidad >= 0.0: 
            self.cantidad = cantidad

    
    def mostrar(self):
        print(f"Titular: {self.titular}\nCantidad: {self.cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.cantidad += cantidad
    def retirar(self, cantidad):
        self.cantidad -= cantidad
        
ale = cuenta(titular="ale",cantidad=10,edad=19)
ale.mostrar()
ale.set_titular(nuevo_titular="carlos")
ale.mostrar()


class CuentaJoven(cuenta):
    def __init__(self, titular,edad,cantidad,bonificacion:float):
        super().__init__(titular,edad,cantidad)
        self.bonificacion = bonificacion

    def es_titular_valido(self):
        if self.get_edad() >= 18 and self.get_edad() < 25:
            return True
    else return False
    def get_bonificacion(self):
        return self.bonificacion
    
    def set_bonificacion(self,nueva_bonificacion):
        self.bonificacion = nueva_bonificacion
    def mostrar(self):
        print(f"Titular: {self.titular}\nCantidad: {self.cantidad}\nbonificacion:{self.bonificacion}\ntipo de cuenta: cuentaJoven")
      
alejoven = CuentaJoven("ale",19,100,25)
alejoven.mostrar()