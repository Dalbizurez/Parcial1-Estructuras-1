from list import LinkedList

class Polinomio(LinkedList):

    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        ecuacion = ""
        node = self.head
        for x in range(self.length, 0, -1):
            coeficiente = node.data
            ecuacion += f" {'-' if coeficiente < 0 else '+'} {coeficiente} x^{x}"
            node =  node.next
        ecuacion += f"{node.data}"

