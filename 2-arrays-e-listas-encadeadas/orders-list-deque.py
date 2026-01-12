from collections import deque

class OrdersQueue:
    def __init__(self):
        # deque é otimizado para inserções e remoções rápidas nas duas pontas
        self.queue = deque()

    def order(self, item):
        # Adiciona ao final (equivalente ao tail.next)
        self.queue.append(item)

    def cook(self):
        # Verifica se está vazio
        if not self.queue:
            print("No orders to cook")
            return

        # popleft() remove do início (equivalente ao head = head.next)
        # Operação O(1)
        item = self.queue.popleft()
        print(f"Cooking: {item}")

# Execução (mesma lógica do exemplo anterior)
orders = OrdersQueue()

orders.order("meat")
orders.cook()

orders.order("salad")
orders.order("juice")

orders.cook()
orders.cook()
orders.cook()
