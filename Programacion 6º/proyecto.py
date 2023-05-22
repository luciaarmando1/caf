import tkinter as tk

#inicio de ventana
ventana= tk.Tk()
ventana.title("Login")
ventana.geometry("300x150")
#label
etiqueta_usuario = tk.Label(ventana, text="Usuario:", font=("Arial",35), fg="blue" )
etiqueta_usuario.pack()
cuadro_usuario = tk.Entry(ventana)
cuadro_usuario.pack()

etiqueta_contra = tk.Label(ventana, text="Contraseña:", fg="red")
etiqueta_contra.pack()
cuadro_contra = tk.Entry(ventana, show="*")
cuadro_contra.pack()

def imprimir():
    texto= "hola "
    etiqueta_contra = tk.Label(ventana, text=texto, fg="red")
    etiqueta_contra.pack()
    print(f"{texto}")
    
boton = tk.Button(ventana, text="Presioname", command=imprimir)
boton.pack()

   
   
   #-----------------------------------------------------------
   

ventana.mainloop() #fin de ventana


