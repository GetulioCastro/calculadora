from tkinter import *

janela = Tk()

Label(janela, text="Calculadora", bg="#C0C0C0").pack()

# dimensonamento e configurações da tela principal
janela.title("Calc")
janela.geometry("300x400+300+150")
janela["bg"] = "#ADD8E6"
janela.resizable(0, 0)
janela.iconbitmap("calculator.ico")

# tela de entrada dos números e operações
ed1 = Entry(janela)
ed1.place(x=80, y=100)

# botões de números e operações
bt1 = Button(janela, width=4, text="1")
bt1.place(x=80, y=130)
bt2 = Button(janela, width=4, text="2")
bt2.place(x=120, y=130)
bt3 = Button(janela, width=4, text="3")
bt3.place(x=160, y=130)
bt4 = Button(janela, width=4, text="+")
bt4.place(x=200, y=130)
bt5 = Button(janela, width=4, text="4")
bt5.place(x=80, y=158)
bt6 = Button(janela, width=4, text="5")
bt6.place(x=120, y=158)
bt7 = Button(janela, width=4, text="6")
bt7.place(x=160, y=158)
bt8 = Button(janela, width=4, text="-")
bt8.place(x=200, y=158)
bt9 = Button(janela, width=4, text="7")
bt9.place(x=80, y=186)
bt10 = Button(janela, width=4, text="8")
bt10.place(x=120, y=186)
bt11 = Button(janela, width=4, text="9")
bt11.place(x=160, y=186)
bt12 = Button(janela, width=4, text="*")
bt12.place(x=200, y=186)
bt13 = Button(janela, width=4, text=".")
bt13.place(x=80, y=214)
bt14 = Button(janela, width=4, text="0")
bt14.place(x=120, y=214)
bt15 = Button(janela, width=4, text="=")
bt15.place(x=160, y=214)
bt16 = Button(janela, width=4, text="/")
bt16.place(x=200, y=214)


janela.mainloop()
