from list import LinkedList

class Polinomio(LinkedList):

    def __init__(self) -> None:
        super().__init__()
    
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

