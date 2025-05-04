import tkinter as tk
from tkinter import messagebox


class Cliente:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"


class GestorClientes:
    def __init__(self):
        self.clientes = []

    def listar_clientes(self):
        if not self.clientes:
            return "No hay clientes registrados."
        return "\n".join(str(cliente) for cliente in self.clientes)

    def consultar_cliente(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                return str(cliente)
        return "Cliente no encontrado."

    def agregar_cliente(self, nombre, apellido, dni):
        if any(cliente.dni == dni for cliente in self.clientes):
            return "Ya existe un cliente con ese DNI."
        else:
            nuevo_cliente = Cliente(nombre, apellido, dni)
            self.clientes.append(nuevo_cliente)
            return "Cliente agregado correctamente."

    def modificar_cliente(self, dni, nuevo_nombre, nuevo_apellido):
        for cliente in self.clientes:
            if cliente.dni == dni:
                cliente.nombre = nuevo_nombre
                cliente.apellido = nuevo_apellido
                return "Cliente modificado correctamente."
        return "Cliente no encontrado."

    def borrar_cliente(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                self.clientes.remove(cliente)
                return "Cliente eliminado correctamente."
        return "Cliente no encontrado."


class App:
    def __init__(self, root):
        self.gestor = GestorClientes()

        # Clientes de prueba iniciales
        self.gestor.agregar_cliente("Juan", "Pérez", "12345678A")
        self.gestor.agregar_cliente("Ana", "García", "87654321B")

        self.root = root
        self.root.title("Gestor de Clientes")

        # Widgets
        self.label = tk.Label(root, text="Gestor de Clientes", font=("Arial", 16))
        self.label.pack(pady=10)

        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.entry_nombre = tk.Entry(self.frame, width=15)
        self.entry_nombre.grid(row=0, column=0, padx=5)
        self.entry_nombre.insert(0, "Nombre")

        self.entry_apellido = tk.Entry(self.frame, width=15)
        self.entry_apellido.grid(row=0, column=1, padx=5)
        self.entry_apellido.insert(0, "Apellido")

        self.entry_dni = tk.Entry(self.frame, width=15)
        self.entry_dni.grid(row=0, column=2, padx=5)
        self.entry_dni.insert(0, "DNI")

        self.add_button = tk.Button(self.frame, text="Agregar Cliente", command=self.agregar_cliente)
        self.add_button.grid(row=1, column=0, columnspan=3, pady=5)

        self.modify_button = tk.Button(root, text="Modificar Cliente", command=self.modificar_cliente)
        self.modify_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Borrar Cliente", command=self.borrar_cliente)
        self.delete_button.pack(pady=5)

        self.list_button = tk.Button(root, text="Listar Clientes", command=self.listar_clientes)
        self.list_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Consultar Cliente", command=self.consultar_cliente)
        self.search_button.pack(pady=5)

    def agregar_cliente(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        dni = self.entry_dni.get()
        mensaje = self.gestor.agregar_cliente(nombre, apellido, dni)
        messagebox.showinfo("Resultado", mensaje)

    def modificar_cliente(self):
        dni = self.entry_dni.get()
        nuevo_nombre = self.entry_nombre.get()
        nuevo_apellido = self.entry_apellido.get()
        mensaje = self.gestor.modificar_cliente(dni, nuevo_nombre, nuevo_apellido)
        messagebox.showinfo("Resultado", mensaje)

    def borrar_cliente(self):
        dni = self.entry_dni.get()
        mensaje = self.gestor.borrar_cliente(dni)
        messagebox.showinfo("Resultado", mensaje)

    def listar_clientes(self):
        clientes = self.gestor.listar_clientes()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, clientes)

    def consultar_cliente(self):
        dni = self.entry_dni.get()
        cliente = self.gestor.consultar_cliente(dni)
        messagebox.showinfo("Resultado", cliente)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()