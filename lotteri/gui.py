import lotteri
from tkinter import *
from tkinter import messagebox


lotter = lotteri.lotteri()

root = Tk()
#titel på fönster
root.title("Lotteri")
root.geometry("300x400")

label_antal = Label(root, text="Antal lotter: ")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)



textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()


def update_list_box(antal_lotter):
    print("hej")
    listbox.delete(0, END)

    listbox.insert(1, "Grattis din lilla råtta.")

    try:

        int_antal_lotter = int(antal_lotter)

        i=0

        if(int_antal_lotter <= 3):


            while i<int_antal_lotter:
                vinst = lotter.get_vinst()
                listbox.insert((i+2), vinst)
                i = i + 1

        else:
            messagebox.showinfo("ÖJ max 3 din lilla nöt")
    
    except:
        messagebox.showinfo("Endast siffror tillåten.")


def clickaSlumpButton():
    antal_lott = textbox_antal.get()

    textbox_antal.delete(0, END)
    update_list_box(antal_lott)

button_slumpa = Button(text="Tur knapp!", command=clickaSlumpButton)
button_slumpa.grid(row=1, column=0, sticky=E, padx=15, pady=13)

listbox = Listbox(root, height=4, width=30, bg="blue", activestyle="dotbox", font="Helvetica", fg="red")
listbox.grid(row=2, column=0, columnspan=2, padx=14, pady=15)


root.mainloop()