import frappe

class ToWhomItConcerns():
    pass

@frappe.whitelist()
def get_salary_slip(employee):
    mydata = frappe.db.sql(f""" select net_pay, name from `tabSalary Slip` 
    where employee_name = "{employee}" order by name  desc limit 1 """, as_dict=1)
    for d in mydata:
        last_salary = d["net_pay"]
        url = d["name"]
        salary = f"""<a href="/app/salary-slip/{url}">Salary = {last_salary}</a>"""
    return salary


