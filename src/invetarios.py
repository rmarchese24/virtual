productos = {}

def agregar_producto(nombre, cantidad, precio):
    if nombre in productos:
        raise ValueError("El producto ya existe en el inventario.")
    productos[nombre] = {
        "cantidad": cantidad,
        "precio": precio
    }

def actualizar_stock(nombre, nueva_cantidad):
    if nombre not in productos:
        raise KeyError("El producto no existe en el inventario.")
    productos[nombre]["cantidad"] = nueva_cantidad

def eliminar_producto(nombre):
    if nombre not in productos:
        raise KeyError("El producto no existe en el inventario.")
    del productos[nombre]

def buscar_producto(nombre):
    return productos.get(nombre, None)
