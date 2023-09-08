from tkinter import*
fontchanger=Tk()


titre = Label(fontchanger, text = "Choose your font here!").pack()
fontchanger.title("Font")
fontchanger.minsize(750,450)


expression = StringVar()
expression.set("Write Here")    
entree = Entry(fontchanger, textvariable = expression, width=70, bg='ivory').pack()

def newfont():
   resultat.set(eval(expression.get()))

resultat = StringVar()

Label(fontchanger, text = "Onyx:").pack()
Entry(fontchanger, textvariable = expression, font=('Onyx', 12), state="readonly").pack()
Label(fontchanger, text = "Rockwell:").pack()
Entry(fontchanger, textvariable = expression, font=('Rockwell', 12), state="readonly").pack()
Label(fontchanger, text = "Modern:").pack()
Entry(fontchanger, textvariable = expression, font=('Modern', 12), state="readonly").pack()
Label(fontchanger, text = "Fixedsys:").pack()
Entry(fontchanger, textvariable = expression, font=('Fixedsys', 12), state="readonly").pack()
Label(fontchanger, text = "Roman:").pack()
Entry(fontchanger, textvariable = expression, font=('Roman', 12), state="readonly").pack()





fontchanger.mainloop()