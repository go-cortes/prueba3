import fun 
from os import system
op=0
lista=[]
while op!=4:
    system("cls")
    fun.mostrar_lista()
    op=fun.get_opcion()
    if op==1:
        system("cls")
        lista.append(fun.listar_usuarios())
        elif op==2:
            system("cls")
            fun.listar_notas(notas)
            system("pause")
            elif op==3:
                system("cls")
                fun.buscar_nota_usuario(usuario)
                system("pause")
                fun.crear_archivo(lista)