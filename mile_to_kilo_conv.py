from tkinter import *
KM_CONVERT = 1.609

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * KM_CONVERT, 4)
    kilo_result_label.config(text=f"{km}")

window = Tk()
title = Label(text = "Miles to Kilometer Converter")
title.grid()
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

kilo_result_label = Label(text="0")
kilo_result_label.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
