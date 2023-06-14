#proporciona el esqueleto para definir los métodos. El primer método que todas las clases deben proporcionar es el constructor. El constructor define la forma en que se crean los objetos de datos. Para crear un objeto Fraccion, tendremos que proporcionar dos piezas de datos, el numerador y el denominador. En Python, el método constructor siempre se llama __init__ (dos subrayados antes y después de init)
class Fraccion:
    def __init__(self,arriba,abajo):

        self.num = arriba
        self.den = abajo
    def mostrar(self):
      print(self.num,"/",self.den)
f1 = Fraccion(1,4)
f2 = Fraccion(1,2)
print(f1+f2)
