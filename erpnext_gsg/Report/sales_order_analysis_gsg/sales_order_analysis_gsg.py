import frappe
from erpnext.erpnext.controllers.trends import validate_filters, get_columns, get_data
from erpnext.erpnext.regional.italy.utils import get_conditions
from erpnext.erpnext.selling.report.sales_order_analysis.sales_order_analysis import get_so_elapsed_time, prepare_data
from frappe.frappe.utils.data import date_diff, time_diff


def execute(filters=None):
	if not filters:
		return [], [], None, []

	validate_filters(filters)

	columns = get_columns(filters)
	conditions = get_conditions(filters)
	data = get_data(conditions, filters)
	so_elapsed_time = get_so_elapsed_time(data)

	if not data:
		return [], [], None, []

	data, chart_data = prepare_data(data, so_elapsed_time, filters)

	return columns, data, None, chart_data


def validate_filters(filters):
	from_date, to_date = filters.get("from_date"), filters.get("to_date")
	from_time, to_time = filters.get("from_time"), filters.get("to_time")

	if not from_date and to_date:
		frappe.throw("From and To Dates are required")
	elif date_diff(to_date, from_date) < 0:
		frappe.throw("To Date cannot be before From Date")

	if not from_time and to_time:
		frappe.throw("From and To Times are required")
	elif time_diff(to_time, from_time) < time_diff("00:00:00","00:00:00"):
		frappe.throw("To Date cannot be before From Date")