class prime_class: """clase"""
  x=raw_input("Ingrese un Numero: ") 
  def is_prime(int(x)): """metodo"""
  x=int(x)    """convierte el dato ingresado en un entero"""
    if x<2:     """si el numero es menor que 2 no es primo, devuelve un False"""
      return False
      for i in range(2,x): """toma los numeros de un rango iniciando en 2 hasta el numero que ingresamos"""
        if x%i == 0:       """si el residuo es cero, no es primo por lo que devuelve un False"""
          return False 
          else:           """si el residuo es distinto a cero, entonces es primo, devuelve True"""
            return True
                
