

from fastapi import FastAPI

from models import OrderItem

app = FastAPI(title="Store Order API")

orders: list[OrderItem] = []


@app.post("/orders", status_code=201)
def create_order(item:OrderItem):
    # Raw JSON is passed straight into the dataclass
    orders.append(item)
    return {**item.model_dump(), "total": item.total}


@app.get("/orders/summary")
def order_summary():
    return {
        "count": len(orders),
        "revenue": sum(item.total for item in orders),
    }


@app.delete("/orders")
def clear_orders():
    orders.clear()
    return {"cleared": True}
