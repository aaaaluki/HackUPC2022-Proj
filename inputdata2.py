from tkinter import messagebox, ttk
import tkinter as tk
def show_selection():
    # Obtener la opción seleccionada.
    selection = combo.get()
    value = entry.get()
    messagebox.showinfo(
        message=f"{selection}: {value}",
        title="Selection"
    )
main_window = tk.Tk()
main_window.config(width=400, height=200)
main_window.title("Pàgina principal")
#where you select the type of parameter
combo = ttk.Combobox(
    state="readonly",
    values=["id", "name", "brand id", "year","fuel", "price"]
    #id, name, brand_id, year, fuel, price
)
combo.place(x=50, y=50)

#Whre you put the value of the parameter
entry = ttk.Entry()
entry.place(x=200, y=50)

label=ttk.Label(text="Hello bb")
label.place(x=50,y=25)

#Button to introduce parameter
button = ttk.Button(text="Introduce Parameter", command=show_selection)
button.place(x=100, y=100)
main_window.mainloop()