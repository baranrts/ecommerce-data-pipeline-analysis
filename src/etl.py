import os
import sys
import pandas as pd

# src klasörünün içindeki db.py'ı hatasız bulması için
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from db import get_engine

def run_etl():
    engine = get_engine()
    
    print("1/5: Musteriler yukleniyor...")
    df_customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
    df_customers.to_sql("customers", engine, if_exists="append", index=False)

    print("2/5: Urunler yukleniyor...")
    df_products = pd.read_csv("data/raw/olist_products_dataset.csv")
    df_products.to_sql("products", engine, if_exists="append", index=False)

    print("3/5: Siparisler yukleniyor...")
    df_orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
    date_cols = [
        "order_purchase_timestamp", 
        "order_approved_at", 
        "order_delivered_carrier_date", 
        "order_delivered_customer_date", 
        "order_estimated_delivery_date"
    ]
    for col in date_cols:
        df_orders[col] = pd.to_datetime(df_orders[col])
    df_orders.to_sql("orders", engine, if_exists="append", index=False)

    print("4/5: Kalemler yukleniyor...")
    df_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
    df_items["shipping_limit_date"] = pd.to_datetime(df_items["shipping_limit_date"])
    df_items.to_sql("order_items", engine, if_exists="append", index=False)

    print("5/5: Odemeler yukleniyor...")
    df_payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")
    df_payments.to_sql("order_payments", engine, if_exists="append", index=False)

    print("\nVERILER BASARIYLA YUKLENDI!")

if __name__ == "__main__":
    run_etl()