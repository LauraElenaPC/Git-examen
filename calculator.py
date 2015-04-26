class calculator_class: """clase que llama al metodo"""
    """declaracion de variables"""
    x=[5,3,7,8,2] 
    n=0
    def sum(x): """metodo que contiene las instrucciones que ejecutara el codigo"""
        for i in range[0,5]: """ciclo for para el rango del contador"""
            n=n+1 """incremento en 1 de la variable que almacena la posicion del contador"""
            t=x+x[n+1]  """suma de los valores de la lista almacenada en x"""
        print t
