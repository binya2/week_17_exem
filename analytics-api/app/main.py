from fastapi import FastAPI
import uvicorn
from dal import get_top_customers, get_customers_without_orders, get_zero_credit_active_customers
from congif import settings

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "Analytics Server is Running"}


@app.get("/analytics/top-customers")
def route_top_customers():
    return get_top_customers()


@app.get("/analytics/customers-without-orders")
def route_customers_no_orders():
    return get_customers_without_orders()


@app.get("/analytics/zero-credit-active-customers")
def route_zero_credit():
    return get_zero_credit_active_customers()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=settings.debug,
    )
