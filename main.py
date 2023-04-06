from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox

def accionVideo() :
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

def accionMusica() :
    enlace = videos.get()
    cancion = YouTube(enlace)
    descarga = cancion.streams.get_audio_only()
    descarga.download()

def popup() :
    MessageBox.showinfo("Sobre mi")

root = Tk()
root.config(bd=15)
root.title("Descargar videos de youtube")

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Informacion", menu=helpmenu)
helpmenu.add_command(label="Autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

instrucciones = Label(root, text="Programa creado para descargar videos de youtube")
instrucciones.grid(row=0, column=0)

videos = Entry(root)
videos.grid(row=1, column=0, columnspan=2)

botonVideo = Button(root, text="Descargar Video", command=accionVideo)
botonVideo.grid(row=2, column=0)

botonMusica = Button(root, text="Descargar Musica", command=accionMusica)
botonMusica.grid(row=2, column=1)

root.mainloop()