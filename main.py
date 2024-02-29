from polinomio import Polinomio

def ingresar(polinomio :Polinomio):
    while True:
        coeficiente = "a"
        while not coeficiente.removeprefix("-").isnumeric():
            print("# Para salir")
            coeficiente = input("Coeficiente: ")
            if coeficiente.strip() == "#":
                return
        polinomio.insert_head(int(coeficiente))

def evaluar(polinomio:Polinomio):
    valor = "a"
    while not valor.replace(".","").isnumeric():
        print("Ingrese un valor de numerico")
        valor = input()
    return polinomio.evaluar(float(valor))

def operar(a:Polinomio, b:Polinomio, operacion):
    c = Polinomio()
    nodea = a.head
    nodeb = b.head
    if a.length != b.length:
        return "Operacion no compatible, diferente grado de polinomios"

    for x in range(0, a.length):
        valor = nodea.data
        if x <= b.length:
            if b.head:
                valor += operacion * nodeb.data
        c.add(valor)

        nodea = nodea.next
        if b.head:
            nodeb = nodeb.next
    return c

if __name__ == "__main__":
    a = Polinomio()
    b = Polinomio()

    while True:
        print(f"a = {a}")
        print(f"b = {b}")
        print(
            # Opciones
            "1. Ingresar componente\n" +
            "2. Operar polinomios\n" +
            "3. Evaluar polinomio\n" +
            "s. Salir"
        )
        opcion = input("Ingrese la opcion a realizar: ")
        match opcion:
            # Opciones
            case "1":
                print(
                    "Seleccione el polinomio\n"+
                    f"A. {a}\n"+
                    f"B. {b}"
                )
                poli = input().upper()
                if poli == "A":
                    ingresar(a)
                elif poli == "B":
                    ingresar(b)
                else:
                    print("Polinomio desconocido, vuevla a intentar")
            case "2":
                print(
                    "Adicion o sustraccion\n"+
                    "1. +\n"+
                    "2. -"
                )
                operacion = input()
                match operacion:
                    case "1":
                        operacion = 1
                    case "2":
                        operacion = -1
                    case _:
                        print("Operacion no reconocida")
                        continue

                print(f"c = {operar(a, b, operacion)}")
            case "3":
                print(
                    "Seleccione el polinomio\n"+
                    f"A. {a}\n"+
                    f"B. {b}"
                )
                poli = input().upper()
                if poli == "A":
                    print(evaluar(a))
                elif poli == "B":
                    print(evaluar(b))
                else:
                    print("Polinomio desconocido, vuevla a intentar")
            case "s":
                break
            case _:
                print("Opcion no reconocida")
        input()