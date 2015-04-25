class prime_class:
  x=int(input("Ingrese un Numero: "))
  def is_prime():
    if x<2:
      return False
      for i in range(2,x):
        if x%i == 0:
          return False
          else:
            return True
                
