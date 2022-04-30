from tkinter import messagebox, ttk
import tkinter as tk
def show_selection():
    # Obtener la opción seleccionada.
    selection = combo.get()
    value = entry.get()
    id = id_entry.get()
    messagebox.showinfo(
        message=f"you id is {id} selected by {selection} and value {value}",
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
combo.place(x=100, y=100)

#where you put the id
id_entry=ttk.Entry()
id_entry.place(x=200, y=25)

#Whre you put the value of the parameter
entry = ttk.Entry()
entry.place(x=250, y=100)

label=ttk.Label(text="Enter your id:")
label.place(x=100,y=25)

#Button to introduce parameter
button = ttk.Button(text="Introduce Parameter", command=show_selection)
button.place(x=150, y=125)
main_window.mainloop()