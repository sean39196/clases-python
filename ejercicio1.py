class Animal:
    def __init__(self,nombre,num_patas,):
        self.nombre = nombre
        self.num_patas = num_patas
class Perro(Animal):
    def __init__(self, nombre, num_patas,raza):
        super().__init__(nombre, num_patas)
        self.raza = raza
    def hacer_ruido(self):
        print("guau guau")
    def correr(self):
        print(" esta corriendo")
class Ave(Animal):
    def __init__(self, nombre, num_patas):
        super().__init__(nombre, num_patas)
    def hacer_ruido(self):
        print("twittear, twittear")
    def volar(self):
        print(" esta volando")

if __name__ == "__main__":
    luka = Perro("luka","cuatro","buldog")
    luka.correr()
    ave = Ave("pio","dos")
    ave.volar()