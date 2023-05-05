from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.689)
    my_label3.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input = Entry(width=5)
input.grid(column=1, row=0)

my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)

my_label1 = Label(text="Miles")
my_label1.grid(column=2, row=0)

my_label2 = Label(text="Km")
my_label2.grid(column=2, row=1)

my_label3 = Label(text="0")
my_label3.grid(column="1", row="1")

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)






window.mainloop()