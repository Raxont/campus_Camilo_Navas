# campus_Camilo_Navas
Quiz 1
Pregunta 1: Respuesta B
Pregunta 2: Respuesta A
Pregunta 3: Respuesta C
Pregunta 4: Respuesta C
Pregunta 5: Respuesta A

Ejercicio practico
Crea un algoritmo “CalculadoradeEdades”
  1) Se define bandera como logico,edad como real, (i,suma,grande) como entero y op como caracter
  2) En un bucle de repeticion se repite hasta que la edad ingresada sea negativa}
      a) Se guarda la cantidad de veces que se ingreso la edad en la variable i
      b) Se crea un si para guardar en la variable grande la mayor edad ingresada
      c) Se guarda la suma de las edades ingresadas en la variable suma
      d) Se le pide que ingrese la edad al usuario donde se verifica con un mientras que no sea decimal
  3)Se le pide al usuario que digite la opcion a usar
  4)Se usa un segun dependiendo de la respuesta anterior
    a) p: se da el promedio de edades que es suma/i
    b) m: Se indica la edad mayor con la variable grande



Algoritmo CalculadoradeEdades
	Definir bandera como logico
	Definir edad como real
	Definir i,suma,grande como entero
	Definir op como caracter
	edad<-0;
	i<-0;
	suma<-0;
	
	Repetir
		i<-i+1;
		Si grande>edad Entonces
			grande<-grande;
		Fin Si
		si grande<edad Entonces
			grande<-edad;
		Fin Si
		suma<-edad+suma;
		Escribir "Ingrese la edad"
		Leer edad;
		Mientras edad-trunc(edad)<>0 hacer
			Escribir "Error, ingrese numeros no decimales, vuelve a ingresar la edad"
			Leer edad;
		FinMientras
	Hasta Que edad<0
		Escribir "Seleccione operación (P/M):"
		Leer op;
		Repetir
			Segun op Hacer
				"p":
					
					Escribir "El promedio de edades es: ",suma/i;
				"m":
					Escribir "La edad mayor es: ",grande;
				De Otro Modo:
					Escribir "Error, opcion ingresada no valida, vuelva a repetir la opcion"
					Leer op;
			Fin Segun
		Hasta Que op=="m" o op=="p"
FinAlgoritmo
