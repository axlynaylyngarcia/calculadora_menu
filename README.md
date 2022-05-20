# calculadora básica con menu

calculadora básica se puede realizar con condiciones. Se desea realizar operaciones básicas con dos número `x,y`. Además se desea calcular la potencia y el logaritmo. Se debe considerar los casos donde
`y = 0` donde la división `x/y` NO se puede realizar `x <=0` donde NO se puede calcular el `log(x)`. Se desea generar un menú para que el usuario pueda seleccionar la operación a realizar. Una manera de hacerlo es la siguiente:

1. Se reciben los dos números `x,y` para realizar la operación.
2. Se recibe la operación a realizae mediante la variable `opción` la que seleciiona en el menú que operación ejecuta el algoritmo.
3. Se inicializa la variable lógica `bandera = false`. Si la división o el logaritmo no se pueden calcular se hace `bandera = true`.
4. Mediante condidciones se realiza la operación deseada.
   * En el caso de la división , si `y = 0`, NO se puede realizar la división, se muestra un mensaje y se hace `bandera = True`
   * En el caso del logaritmo, si `x<=0`, NO se puede calcular el logaritmo, se muestra un mensaje y se hace `bandera = True`.
5. Se muestra el resultado en el caso en que `bandera = False`. 

*Tomado de: Python con aplicaciones a las matemáticas, ingenieria y finanzas. Cervantes 0, Baez D.*