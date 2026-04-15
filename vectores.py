
"""
    APA - T3      Nel Penin Yele
    
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    
    def  __mul__(self, other):
        """
        Método para dar un vector formado por la multiplicación elemento a elemento de dos vectores o multiplicar un vector por un número

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])

        >>> v1 * v2
        Vector([4, 10, 18])

   
        >>> v1 * 2
        Vector([2, 4, 6])

        """

        if isinstance(other,(int, float, complex)):
            return Vector(item * other for item in self)
        else: 
            return Vector(num1 * num2 for num1, num2 in zip(self, other))
        
    __rmul__ = __mul__
    # igualamos __rmul__ a __mul__ porque la multiplicación es commutativa. 

    def __matmul__(self, other):

        """
        Método para multiplicar matrices 

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])

        >>> v1 @ v2
        32
        """
        if isinstance(other, Vector):
            return sum(num1 * num2 for num1, num2 in zip(self, other))
        else:
            raise TypeError("No se puede realizar la operación porque no es un vector")
    
    def __rmatmul__(self, other):
        """
        Método para comprovar que en la otra posición, el otro elemento también es un vector, si lo es usará el método __mul__

        """
        if isinstance(other, Vector):
            return other @ self #reutiliza __mul__
        else:
            raise TypeError("No se puede realizar la operación porque no es un vector")
        
    def __floordiv__(self, other):

        """
        Método que devuleve la componente v1 paralela a v2

        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])

        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """

        if isinstance(other, Vector):
            factor = ( self @ other )/(other @ other)
            return Vector(item * factor for item in other)
        else:
            raise TypeError("No se puede realizar la operación porque no es un vector")
        
    def __rfloordiv__(self, other):
        """
        Método para comprovar que el otro componente (v2) es un vector con el reflejado de __floordiv__
        """
        if isinstance(other, Vector):
            return self // other #reutiliza __floordiv__
        else:
            raise TypeError("No se puede realizar la operación porque no es un vector")
    
        
    def __mod__(self, other):
        """
        Método para calcular la componente normal de un vector (v1) respecto a otro vector(v2)

        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])

        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
        """
        if isinstance(other, Vector):
            return Vector([num1 - num2 for num1, num2 in zip(self, self // other)])
        else:
            raise TypeError("No se puede realizar la operación porque no es un vector")
        
    def __rmod__(self, other):
        """
        Método para comprovar que en el reflejado de __mod__ el otro componente es un vector
        """
        if isinstance(other, Vector):
            return self % other #reutiliza __mod__
 
 
if __name__ == "__main__":
      import doctest
      doctest.testmod()
