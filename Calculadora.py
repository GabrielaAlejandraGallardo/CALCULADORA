import os
#funciones

def sumar(n1,n2):
    return n1+n2
def restar(n1,n2):
    return n1-n2   
def multiplicar(n1,n2):
    return n1*n2  
def dividir(n1,n2):
    return n1/n2       
#funcion para el menu
def menu():
   # os.system("cls")
    print("+ para Sumar")
    print("- para Restar")
    print("* para Multiplicar") 
    print("/ para Dividir")
    print("s para Salir")
#funcion principal
def main():
    while True:
       
       menu()    
       n1=float(input("Ingrese el primer número: "))
       n2=float(input("Introduce el segundo número: "))
       op=input("Ingrese una opción ")
       if op=="+":
         print("El  resultado de la suma es : ",sumar(n1,n2))
       elif op=="-":
         print("El restultado de la resta es: ", restar(n1,n2))   
       elif op=="*":
          print("El resultado de la Multiplicación es :",multiplicar(n1,n2))  
       elif op=="/":
          print("El resultado de la división es :",dividir(n1,n2))
       elif op=="s":   
            break
    #   os.system("cls")  
     

#Aca empieza el programa....
main()