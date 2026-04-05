"""
APA T - 3
Diego Fabelo Marrero

vectores.py (Gestión de vectores)

Tests unitarios:
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])

>>> v1 * v2
Vector([4, 10, 18])

>>> v1 @ v2
32

>>> v3 = Vector([2, 1, 2])
>>> v4 = Vector([0.5, 1, 0.5])
>>> v3 // v4
Vector([1.0, 2.0, 1.0])

>>> v3 % v4
Vector([1.0, -1.0, 1.0])

"""

class Vector:
    vector = []
    def __init__(self, iterable):
        """
        Constructor de la clase vector.
        El argumento es un iterable para recorrer
        
        """
        self.vector = [elemento for elemento in iterable]

    def __repr__(self):
        """
        Representación del vector
        El argumeto es el propio vector
        
        """
        return "Vector(" + repr(self.vector) + ")"

    def __str__(self):
        """
        Representación del vector como string 
        El argumento es el propio vector
        Su salida será la representacion del mismo
            
        """
        return str(self.vector)

    def __len__(self):  
        """
        Devuelve la longitud del vector
        El argumento es el propio vector
        Su salida será la longitud del vector
        
        """
        return len(self.vector)

    def __sub__(self, otro):
        """
        Resta dos vectores componente a componente.
        Los argumentos son los vectores a restar
        Devolverá la diferencia entre ambos
            
        """
        return Vector([a - b for a, b in zip(self.vector, otro.vector)])

    def __mul__ (self, otro):
        """
        Multiplicacion de vector * vector o vector * numero
        Sus argumentos son o bien dos vectores o un vector y escalar
        Devuelve el resultado de la operación
        
        """
        if isinstance(otro, (int, float)):
            return Vector([c * otro for c in self.vector])
            
        if isinstance(otro, Vector):
            return Vector([a * b for a, b in zip(self.vector, otro.vector)])

    def __rmul__(self, otro):
        """
        Multiplicación de un vector por un número
        Sus argumentos son el vector y el número
        La salida el resultado
        
        """
        return self.__mul__(otro)

    def __matmul__(self, otro):
        """
        Producto escalar de dos vectores
        Los argumentos serán dos vectores
        La salida el resultado
        
        """
        return sum(a * b for a, b in zip(self.vector, otro.vector))

    def __floordiv__(self, otro):
        """
        Calcula la componente paralela de un vector respecto a otro
        El argumento será el vector de referencia
        Su salida la componente paralela
        
        """
        numerador = self @ otro
        denominador = otro @ otro
        return ((numerador/denominador)*otro)

    def __mod__(self, otro):
        """
        Calcula la componente perpendicular de un vector respecto a otro.
        El argumento será el vector de referencia
        Su salida la componente perpendicular
        
        """
        return self - (self // otro)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)