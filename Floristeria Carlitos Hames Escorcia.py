import tkinter as tk
from tkinter import ttk, messagebox
import random

def crearInventario():
    flores = ["tulipán", "lirio", "rosa", "dahlia",
              "margarita", "girasol", "clavel", "geranio"]
    seleccion = random.sample(flores, 3)
    inventario = {
        flor: {
            "precio": random.randint(2000, 6000),
            "cantidad": random.randint(10, 50),
            "vendidas": 0
        } for flor in seleccion
    }
    return inventario

class FloristeriaGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title(" Floristería Carlitos ")
        self.ventana.geometry("650x500")
        self.ventana.configure(bg="#f0f0f0")
        
    
        self.inventario = crearInventario()
        self.inventario_inicial = {f: d.copy() for f, d in self.inventario.items()}
        self.total_ganado = 0
        
      
        self.crear_widgets()
        
    def crear_widgets(self):
        
        titulo = tk.Label(
            self.ventana,
            text=" Floristería Carlitos ",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            pady=10
        )
        titulo.pack()
        
      
        marco_tabla = tk.Frame(self.ventana, bg="#f0f0f0")
        marco_tabla.pack(pady=10)
        
        columnas = ("Flor", "Precio", "Cantidad")
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas, show="headings", height=8)
        
     
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=150, anchor="center")
        
        scrollbar = ttk.Scrollbar(marco_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        
        self.tabla.pack(side="left")
        scrollbar.pack(side="right", fill="y")
        
        
        marco_entradas = tk.Frame(self.ventana, bg="#f0f0f0")
        marco_entradas.pack(pady=10)
        
       
        tk.Label(marco_entradas, text="Nombre de la flor:", bg="#f0f0f0").grid(row=0, column=0, padx=5)
        self.entrada_flor = tk.Entry(marco_entradas)
        self.entrada_flor.grid(row=0, column=1, padx=5)
        
        tk.Label(marco_entradas, text="Cantidad:", bg="#f0f0f0").grid(row=0, column=2, padx=5)
        self.entrada_cantidad = tk.Entry(marco_entradas, width=10)
        self.entrada_cantidad.grid(row=0, column=3, padx=5)
        
      
        marco_botones = tk.Frame(self.ventana, bg="#f0f0f0")
        marco_botones.pack(pady=10)
        
        
        estilos = {'font': ('Arial', 10), 'width': 15, 'height': 2}
        
        tk.Button(marco_botones, text="Vender ", command=self.vender, bg="#90EE90", **estilos).pack(side="left", padx=5)
        tk.Button(marco_botones, text="Agregar Flor ", command=self.agregar_flor, bg="#FFB6C1", **estilos).pack(side="left", padx=5)
        tk.Button(marco_botones, text="Cerrar Tienda ", command=self.cerrar_tienda, bg="#87CEEB", **estilos).pack(side="left", padx=5)
        
        self.lbl_total = tk.Label(
            self.ventana,
            text=f"Total Ganado: ${self.total_ganado:,}",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        )
        self.lbl_total.pack(pady=10)
        
       
        self.actualizar_tabla()
    
    def actualizar_tabla(self):
        
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        
        for flor, datos in self.inventario.items():
            self.tabla.insert("", "end", values=(
                flor,
                f"${datos['precio']:,}",
                datos['cantidad']
            ))
    
    def vender(self):
        flor = self.entrada_flor.get().strip().lower()
        
        try:
            cantidad = int(self.entrada_cantidad.get())
            if cantidad <= 0:
                messagebox.showwarning("Error", "La cantidad debe ser mayor a 0")
                return
        except ValueError:
            messagebox.showwarning("Error", "Ingrese una cantidad válida")
            return
        
        if flor not in self.inventario:
            messagebox.showinfo("No disponible", f"{flor} no se encuentra a la venta 🤷‍♀️")
            return
        
        datos = self.inventario[flor]
        if cantidad > datos["cantidad"]:
            messagebox.showwarning("Sin stock", f"No hay suficientes {flor}. Solo hay {datos['cantidad']} disponibles")
            return
        
      
        datos["cantidad"] -= cantidad
        datos["vendidas"] += cantidad
        venta = datos["precio"] * cantidad
        self.total_ganado += venta
        
        
        if datos["cantidad"] == 0:
            messagebox.showinfo("Agotado", f"{flor} ha sido eliminada del inventario 🥀")
            del self.inventario[flor]
        
        self.actualizar_tabla()
        self.lbl_total.config(text=f"Total Ganado: ${self.total_ganado:,}")
        messagebox.showinfo("Venta Exitosa", f"Vendidas {cantidad} de {flor} por un total de ${venta:,}")
        
        
        self.entrada_flor.delete(0, tk.END)
        self.entrada_cantidad.delete(0, tk.END)
    
    def agregar_flor(self):
        flor = self.entrada_flor.get().strip().lower()
        if not flor:
            messagebox.showwarning("Error", "Ingrese el nombre de la flor")
            return
            
        try:
            cantidad = int(self.entrada_cantidad.get())
            if cantidad <= 0:
                messagebox.showwarning("Error", "La cantidad debe ser mayor a 0")
                return
        except ValueError:
            messagebox.showwarning("Error", "Ingrese una cantidad válida")
            return
        
        if flor in self.inventario:
            self.inventario[flor]["cantidad"] += cantidad
            messagebox.showinfo("Actualizado", f"Se agregaron {cantidad} unidades de {flor}")
        else:
            precio = random.randint(2000, 6000)
            self.inventario[flor] = {
                "precio": precio,
                "cantidad": cantidad,
                "vendidas": 0
            }
            messagebox.showinfo("Nueva Flor", f"Se agregó {flor} con precio de ${precio:,}")
        
        self.actualizar_tabla()
        self.entrada_flor.delete(0, tk.END)
        self.entrada_cantidad.delete(0, tk.END)
    
    def cerrar_tienda(self):
        resumen = "===  Resumen del Día  ===\n\n"
        resumen += "Flor\t\tVendidas\tGanancia\n"
        resumen += "=" * 40 + "\n"
        
        flores_vendidas = {}
        for flor, datos_iniciales in self.inventario_inicial.items():
            datos_finales = self.inventario.get(flor, {"cantidad": 0, "vendidas": 0})
            vendidas = datos_iniciales["cantidad"] - datos_finales["cantidad"]
            ganancia = vendidas * datos_iniciales["precio"]
            flores_vendidas[flor] = vendidas
            resumen += f"{flor}\t\t{vendidas}\t\t${ganancia:,}\n"
        
        if flores_vendidas:
            mas_vendida = max(flores_vendidas.items(), key=lambda x: x[1])
            menos_vendida = min(flores_vendidas.items(), key=lambda x: x[1])
            
            resumen += "\n" + "=" * 40 + "\n"
            resumen += f"Flor más vendida: {mas_vendida[0]} ({mas_vendida[1]} unidades)\n"
            resumen += f"Flor menos vendida: {menos_vendida[0]} ({menos_vendida[1]} unidades)\n"
            resumen += f"Total ganado: ${self.total_ganado:,}"
        else:
            resumen += "\nNo se realizaron ventas hoy"
        
        messagebox.showinfo("Cierre de Tienda", resumen)

def main():
    ventana = tk.Tk()
    app = FloristeriaGUI(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()