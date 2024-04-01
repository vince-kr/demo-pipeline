from collections import Counter
from dataclasses import dataclass
import datetime
from flask import Flask


@dataclass
class EggSale:
    """Record a single sale of a number of eggs"""
    quantity: int
    sale_price: int  # represent money as an integer number of cents
    buyer: str = "Unnamed"
    sale_date: datetime.date = datetime.date.today()
    currency: str = "EUR"

    def per_egg(self) -> float:
        return self.sale_price / 100 / self.quantity


class Reporting:
    @staticmethod
    def orders_per_buyer(all_orders: tuple[EggSale]) -> dict:
        """List number of orders placed by each unique buyer"""
        count_orders_per_buyer = Counter(order.buyer for order in all_orders)
        return dict(count_orders_per_buyer)


es_tuple = (
        EggSale(12, 600, "Alice"),
        EggSale(10, 800),
        EggSale(30, 900, "Bob"),
        EggSale(6, 200),
        EggSale(12, 600, "Alice"),
        EggSale(6, 320),
        )

app = Flask(__name__)


@app.route("/")
def index():
    response = "<h2>Main page</h2>"
    response += "<a href=\"report\">Order report</a>"
    return response


@app.route("/report")
def order_report():
    summary_buyers = sorted(Reporting.orders_per_buyer(es_tuple).items(),
                            key=lambda x: x[1],
                            reverse=True)
    response = "<h2>Order report</h2>"
    response += "<table><tr><th>Buyer</th><th>Number of orders</th></tr>"
    for buyer, qty in summary_buyers:
        response += "<tr><td>" + buyer + "</td>"
        response += "<td>" + str(qty) + "</td></tr>"
    return response
