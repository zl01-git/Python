from flask import Flask, render_template, request


class Order:
    def __init__(self, id, desc, items):
        self.id = id
        self.desc = desc
        self.items = items

    def __repr__(self) -> str:
        return f"<Order {self.id}: {self.desc} - {self.items}>"


orders = {43: Order(43, 'Оплата картой, через почту', ['Кружка', 'Майка', 'Стикеры']), 69: Order(
    69, 'Оплата наличными, через почту', ['Медные диски'])}

# print(42 in orders.keys())


app = Flask(__name__)

@app.route("/", methods=["POST"])
def render_send():
    req = request.form.get("id")
    if req in orders.keys():
        return orders[int(req)]
