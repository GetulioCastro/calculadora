from tkinter import *

janela = Tk()

Label(janela, text="Calculadora", bg="#C0C0C0").pack(fill=X)
janela.title("Calc")
janela.geometry("300x400+300+150")
janela["bg"] = "#FFFFE0"

ed1 = Entry(janela)
ed1.place(x=80, y=100)

janela.mainloop()
