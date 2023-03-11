
import frappe
from frappe.frappe.model import document


def stock_entry(doc, method):
    if doc.material_request_type == "Material Issue":
        new_stock_entry = frappe.new_doc("Stock Entry")
        new_stock_entry.stock_entry_type = doc.material_request_type
        new_stock_entry.from_warehouse = doc.set_warehouse

        for item in doc.items:
            new_stock_entry.append("items", {"item_code": item.item_code, "qty": item.qty})

        new_stock_entry.insert()
        new_stock_entry.submit()


