from tkinter import *

janela = Tk()

# label contendo o nome do app em destaque
calc = Label(janela, text="Calculadora", bg="#C0C0C0", width=30, font="times 16 bold", bd=3, relief="ridge")
calc.pack()

# dimensonamento e configurações da tela principal
janela.title("Single Calc")
janela.geometry("300x400+500+200")
janela["bg"] = "#ADD8E6"
janela.resizable(0, 0)
janela.wm_iconbitmap("calculator.ico")


# função click
def click(evento):
    global ed1, tela
    text = evento.widget.cget("text")
    if text == "=":
        if ed1.get().isdigit():
            value = float(ed1.get())
        else:
            value = eval(ed1.get())

        ed1.set(value)
        tela.update()

    elif text == "C":
        ed1.set("")
        tela.update()
    else:
        ed1.set(ed1.get() + text)
        tela.update()


# tela de entrada dos números e operações
ed1 = StringVar()
ed1.set("")
tela = Entry(janela, textvar=ed1, font="lucida 12 bold")
tela.pack(fill=X, ipadx=10, padx=10, pady=10)

# botões contendo números e operações
frm = Frame(janela, bg="#ADD8E6")
bt1 = Button(frm, width=4, text="1", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="2", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="3", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="+", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
frm.pack()

frm = Frame(janela, bg="#ADD8E6")
bt1 = Button(frm, width=4, text="4", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="5", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="6", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="-", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
frm.pack()

frm = Frame(janela, bg="#ADD8E6")
bt1 = Button(frm, width=4, text="7", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="8", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="9", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="*", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
frm.pack()

frm = Frame(janela, bg="#ADD8E6")
bt1 = Button(frm, width=4, text=".", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="0", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="=", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
bt1 = Button(frm, width=4, text="/", font="lucida 10 bold")
bt1.pack(side=LEFT, padx=10, pady=10)
bt1.bind("<Button-1>", click)
frm.pack()

frm = Frame(janela, bg="#ADD8E6")
bt1 = Button(frm, width=27, text="C", font="lucida 10 bold")
bt1.pack()
frm.pack()



# manter a janela aberta
janela.mainloop()
