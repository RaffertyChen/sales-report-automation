# b1 load csv
from pathlib import Path

from openpyxl import load_workbook
import pandas as pd
from openpyxl.styles import Font

folder = Path(__file__).parent
orders = pd.read_csv(folder / "orders.csv")

# b2 total sales
orders["total"] = orders["quantity"] * orders["unit_price"]
per_customer = orders.groupby("customer_id")["total"].sum()
print(per_customer)

orders["month"] = orders["date"].str[:7]
per_month = orders.groupby("month")["total"].sum()
print(per_month)

# b3 merge two files
customers = pd.read_csv(folder / "customers.csv")
print(customers)

merged = pd.merge(
    orders, customers, on="customer_id", how="left"
)  # need to put how"left" so pandas doenst skip any files
print(merged.head())

print(len(orders))
print(len(merged))

# b5 export to excel
with pd.ExcelWriter(folder / "sales_report.xlsx") as writer:
    merged.to_excel(writer, sheet_name="Orders", index=False)
    per_customer.to_excel(writer, sheet_name="By customer")
    per_month.to_excel(writer, sheet_name="by month")
print("saved sales_report.xlsx")

#b5 format the orders sheet
wb = load_workbook(folder / "sales_report.xlsx")
ws = wb["Orders"]

for cell in ws[1]:
    cell.font = Font(bold=True)

for letter in["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
    ws.column_dimensions[letter].width = 18

money = "$#,##0.00"

for cell in ws["F"]:
    cell.number_format = money

for cell in ws["G"]:
    cell.number_format = money

ws = wb["By customer"]

for cell in ws[1]:
    cell.font = Font(bold=True)

for cell in ws["B"]:
    cell.number_format = money

ws.column_dimensions["A"].width = 15
ws.column_dimensions["B"].width = 15

ws = wb["by month"]

for cell in ws[1]:
    cell.font = Font(bold=True)

for cell in ws["B"]:
    cell.number_format = money

ws.column_dimensions["A"].width = 15
ws.column_dimensions["B"].width = 15

wb.save(folder / "sales_report.xlsx")
print("formated sales_report.xlsx")
