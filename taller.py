clientes = [
    {"nombre": "juan", "edad":90,"correo":"cristian@gmail.com"},
    {"nombre": "pedro", "edad":78,"correo":"camilo@gmail.com"}
]

def agregar_cliente():
    nombre=input("Ingrese el nombre del Cliente ")
    try:
        edad = float(input(f"Ingrese la edad de: {nombre}"))
        correo=str(input("Ingrese el correo del Cliente "))
        if edad <0:
            print("edad invalida. Debe ser mayor a 0")
            return
        if not "@" in  clientes:
            print("correo invalido. Debe ingresar el @ en su correo")
            return
        clientes.append({"nombre":nombre,"Edad":edad,"Correo":correo})
        print("Cliente agregado correctamente")
    except ValueError:
        print("Entrada invalida. Debe de ingresar un cliente valido")
        
        
def eliminar_clientes():
    nombre = input("Ingrese el nombre del cliente a eliminar: ")
    global clientes
    clientes = [ cliente for cliente in clientes if cliente["nombre"].lower() != nombre.lower()]
    print("Cliente eliminado correctamente")
    
def mostrar_clientes():
    if not clientes:
        print("No hay clientes registrados")
        return
    print("Lista de Clientes: ")
    for cliente in clientes:
        print(f"-{cliente["nombre"]}: {cliente["edad"]}:{cliente["correo"]}")
        
def buscar_clientes():
    
    global clientes
    print("nombre" in clientes)
    

def clientes_ordenados():
    global clientes
    clientes.sort()
    
    print(clientes)
        
def calcular_promedio_clientes():
    if not clientes:
        print("No hay clientes registrados")
        return
    promedio = sum(cliente["edad"] for cliente in clientes) / len(clientes)
    print(f"Promedio de edad: {promedio:.2f}")
