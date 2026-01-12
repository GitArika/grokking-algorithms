class OrderNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class OrdersList:
    def __init__(self):
        self.head = None  # primeiro pedido
        self.tail = None  # último pedido

    def order(self, item):
        new_order = OrderNode(item)

        if self.head is None:
            self.head = new_order
            self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order
 
    def cook(self):
        if self.head is None:
            print("No orders to cook")
            return

        print("Cooking:", self.head.item)

        self.head = self.head.next

        if self.head is None:
            self.tail = None

orders = OrdersList()

orders.order("meat")
orders.cook()

orders.order("salad")
orders.order("juice")

orders.cook()
orders.cook()
orders.cook()
