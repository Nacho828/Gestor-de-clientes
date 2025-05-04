import tkinter as tk
from tkinter import messagebox
from Cliente import Cliente


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

