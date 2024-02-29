from list import LinkedList

class Polinomio(LinkedList):

    def __init__(self) -> None:
        super().__init__()
    
    def evaluar(self, valor):
        if not self.head:
            return "0"
        ecuacion = ""
        resultado = 0
        node = self.head
        for x in range(self.length, 1, -1):
            coeficiente = node.data

            ecuacion += f"{'-' if coeficiente < 0 else ''}{coeficiente}*({valor})^{x-1} + "
            
            resultado += coeficiente * pow(valor,x-1)

            node =  node.next
        
        resultado += node.data 
        ecuacion += f"{node.data}"

        ecuacion += f" = {resultado}"

        return ecuacion

    def __str__(self) -> str:
        if not self.head:
            return "0"
        ecuacion = ""
        node = self.head
        for x in range(self.length, 1, -1):
            coeficiente = node.data
            ecuacion += f"{'-' if coeficiente < 0 else ''}{coeficiente}x^{x-1} + "
            node =  node.next
        ecuacion += f"{node.data}"
        return ecuacion

