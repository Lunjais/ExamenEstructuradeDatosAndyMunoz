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

        self.average_btn = tk.Button(self.window, text="Promedio del arreglo", command=self.promedio_arreglo)
        self.average_btn.pack()

        self.sum_btn = tk.Button(self.window, text="Suma de elementos", command=self.suma_elementos)
        self.sum_btn.pack()

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
            max_idx = i
            for j in range(i+1, n):
                if self.array[j] > self.array[max_idx]:
                    max_idx = j
            self.array[i], self.array[max_idx] = self.array[max_idx], self.array[i]
        messagebox.showinfo("Arreglo ordenado", "El arreglo se ha ordenado de mayor a menor.")

    def tamano_arreglo(self):
        tamano = len(self.array)
        messagebox.showinfo("Tamaño del arreglo", f"El tamaño del arreglo es: {tamano}")

    def promedio_arreglo(self):
        if self.array:
            promedio = sum(self.array) / len(self.array)
            messagebox.showinfo("Promedio del arreglo", f"El promedio del arreglo es: {promedio}")
        else:
            messagebox.showwarning("Arreglo vacío", "El arreglo está vacío.")

    def suma_elementos(self):
        if self.array:
            suma = sum(self.array)
            messagebox.showinfo("Suma de elementos", f"La suma de los elementos del arreglo es: {suma}")
        else:
            messagebox.showwarning("Arreglo vacío", "El arreglo está vacío.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ArrayApp()
    app.run()
