from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=35,pady=30)

def convert_mile_to_km():
    mile = miles_input.get()
    mile_km = round(float(mile)*1.60934)
    km_label_result.config(text=mile_km)

miles_input = Entry(width=10)
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)


km_text = Label(text="is equal to ")
km_text.grid(column=0, row=1)
km_label_result = Label(text=0)
km_label_result.grid(column=1, row=1)
km_writen = Label(text="Km")
km_writen.grid(column=2, row=1)

convert_button = Button(text="Convert", command=convert_mile_to_km)
convert_button.grid(column=1,row=2)

window.mainloop()