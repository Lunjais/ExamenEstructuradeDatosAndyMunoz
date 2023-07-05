import tkinter as tk
from tkinter import messagebox

class ArrayApp:
    def __init__(self):
        self.array = []

        self.window = tk.Tk()
        self.window.title("Programa de Arreglo")

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.window, textvariable=self.entry_var)
        self.entry.pack()

        self.add_btn = tk.Button(self.window, text="Agregar elemento", command=self.agregar_elemento)
        self.add_btn.pack()

        self.sort_btn = tk.Button(self.window, text="Ordenar arreglo", command=self.ordenar_arreglo)
        self.sort_btn.pack()

        self.size_btn = tk.Button(self.window, text="Tamaño del arreglo", command=self.tamano_arreglo)
        self.size_btn.pack()

        self.max_btn = tk.Button(self.window, text="Elemento de mayor valor", command=self.elemento_mayor)
        self.max_btn.pack()

        self.min_btn = tk.Button(self.window, text="Elemento de menor valor", command=self.elemento_menor)
        self.min_btn.pack()

    def agregar_elemento(self):
        try:
            elemento = int(self.entry_var.get())
            self.array.append(elemento)
            messagebox.showinfo("Éxito", "Elemento agregado correctamente.")
            self.entry_var.set('')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico entero.")

    def ordenar_arreglo(self):
        n = len(self.array)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        messagebox.showinfo("Arreglo ordenado", "El arreglo se ha ordenado de menor a mayor.")

    def tamano_arreglo(self):
        tamano = len(self.array)
        messagebox.showinfo("Tamaño del arreglo", f"El tamaño del arreglo es: {tamano}")

    def elemento_mayor(self):
        if self.array:
            max_elemento = max(self.array)
            messagebox.showinfo("Elemento de mayor valor", f"El elemento de mayor valor es: {max_elemento}")
        else:
            messagebox.showwarning("Arreglo vacío", "El arreglo está vacío.")

    def elemento_menor(self):
        if self.array:
            min_elemento = min(self.array)
            messagebox.showinfo("Elemento de menor valor", f"El elemento de menor valor es: {min_elemento}")
        else:
            messagebox.showwarning("Arreglo vacío", "El arreglo está vacío.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ArrayApp()
    app.run()
