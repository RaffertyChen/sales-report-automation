#part 3 breaking and fixing a file
import pandas as pd
from pathlib import Path

folder = Path(__file__).parent
messy = pd.read_csv(folder / "orders_messy.csv", skiprows=1)#to skip the title row
print(messy.head())

messy["unit_price"] = messy["unit_price"].str.replace("$","") #so if we add $ sign the data can stil be sorted
messy["unit_price"] = pd.to_numeric(messy["unit_price"])

messy["date"] = pd.to_datetime(messy["date"] , format="mixed")

messy["customer_id"] = messy["customer_id"].str.strip()#so the data even with a space can still be read

messy["total"] = messy["quantity"] * messy["unit_price"]# to take out data and count the unit price and quanitity and then group them up by customer id 
per_customer = messy.groupby("customer_id")["total"].sum()
print(per_customer)

messy["month"] = messy["date"].dt.to_period("M") # to take out data and sort out by month
per_month = messy.groupby("month")["total"].sum()
print(per_month)