def mostrar_menu():
    menu"""[1]resgistrar alumno
    [2]listar todos los alumnos
    [3]buscar alumnos por nivel
    [4]calcular la nota promedio de los alumnos
    [5]salir del programa y guardar
    --->"""
    print(menu,end="")
    def get_opcion():
        while True:
            try:
                op=int(input())
                if op>=1 and op<=4:
                    return op
                    else:
                        raise ValueError
                        except:
                            print("ingrese una opcion valida-->",end="")

                            def agregar_alumno():
                                lista=input("ingrese el listado de alumnos: ")
                                nota=input("ingrese las notas de los alumnos:")
                                resgistro=("ingrese el registro de alumno: ")
                                alumno=input("ingrese la clase del alumno: ")
                                nombre=input("ingrese el nombre del alumno: ")
                                nivel=input("ingrese el nivel del alumno:")
                                res={"lista":lista,"nota":nota,"registro":registro,"alumno":alumno,"nombre":nombre,"nivel":nivel}
                                return res

                                def buscar_alumnos(lista):
                                  for i in range(len(lista))
                                  print(f"lista{i+1}:")
                                  print(f"nota:{lista[i]["nota"]}")
                                  print(f"registro:{lista[i]["registro"]}")
                                  print(f"alumno:{lista[i]["alumno"]}")
                                  print(f"nombre:{lista[i]["nombre"]}")
                                  print(f"nivel:{lista[i]["lista"]}")
                                  print(f"*************************")

                                  def buscar_calculo_nota(lista):
                                    nota_alumno=input("ingrese la nota del alumo: ")
                                    encontrado = False
                                    for i in range (len(lista)):
                                        if nota_alumno==lista[i]["lista"]:
                                            res=lista[i]
                                            encontrado = new_func():
                                            if encontrado:
                                                print(f"lista:{res["lista"]}")
                                                print(f"nota:{res["nota"]}")
                                                print(f"registro:{res["registro"]}")
                                                print(f"alumno:{res["alumno"]}")
                                                print(f"nombre:{res["nombre"]}")
                                                print(f"nivel:{res["nivel"]}")
                                                else:
                                                    def new_func():
                                                        encontrado = True
                                                        return encontrado

                                                        def crear_archivo(lista):
                                                            with open("lista_alumnos.txt","w")as archivo:
                                                                for i in lista:
                                                                    res= i["nota"]+","+i["registro"]+","+i["alumno"]+","+i["nombre"]+","+["nombre"]+","+i[nivel]+"\n"
                                                                    archivo.write(res)

