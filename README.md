# Sales Report Automation

Turns raw order data into a clean, formatted Excel report in a few seconds.

## The problem

Every month, someone has to work out each order's total by hand, add up the sales for every customer and every month, look up each customer's company name, and make the spreadsheet readable. It's slow and boring, and one missed row makes the totals wrong.

## What it does

- Reads an orders file and a customer list
- Works out the total for every order, then the totals per customer and per month
- Adds each customer's company name and country, without losing orders from customers missing from the list
- Saves everything as a formatted Excel report with three tabs: Orders, By customer and By month

## The result

The finished report is ready in a few seconds instead of about an hour of manual work, and no orders go missing, even from customers who aren't in the customer list.

## Handles messy files

Real exports are rarely clean. `messy.py` shows the script coping with:

- a title row above the column names
- stray spaces after customer IDs
- prices typed with a $ sign
- dates written in different formats

## How to run it

1. Install Python from python.org.
2. Open a terminal in this folder and run: `python -m pip install -r requirements.txt`
3. Run: `python sales_summary.py`
4. Open `sales_report.xlsx`.

## Files

- `sales_summary.py`: builds the report
- `messy.py`: cleans a messy version of the orders file
- `orders.csv`, `customers.csv`, `orders_messy.csv`: sample data (made up)
- `sales_report.xlsx`: an example of the finished report