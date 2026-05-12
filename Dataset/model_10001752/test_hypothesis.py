import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Daily_production,
    ETF_EPF,
    Bonus,
    Salary,
    Order_Sent,
    Administrator,
    Worker,
    Staff,
    Leave,
    Attendance,
    Employee,
    Section,
    Interface_Interface,
    Items,
    Stock,
    Orders,
    Supplier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_daily_production_is_not_abstract():
    assert not inspect.isabstract(Daily_production)


def test_daily_production_constructor_exists():
    assert callable(Daily_production.__init__)


def test_daily_production_constructor_args():
    sig = inspect.signature(Daily_production.__init__)
    params = list(sig.parameters.keys())
    assert "item_code" in params, "Missing parameter 'item_code'"
    assert "future_Qty" in params, "Missing parameter 'future_Qty'"
    assert "date" in params, "Missing parameter 'date'"
    assert "pro_number" in params, "Missing parameter 'pro_number'"
    assert "curr_qty" in params, "Missing parameter 'curr_qty'"
    assert "item_name" in params, "Missing parameter 'item_name'"
    assert "section" in params, "Missing parameter 'section'"

def test_daily_production_has_item_code():
    assert hasattr(Daily_production, "item_code")
    descriptor = None
    for klass in Daily_production.__mro__:
        if "item_code" in klass.__dict__:
            descriptor = klass.__dict__["item_code"]
            break
    assert isinstance(descriptor, property)

def test_daily_production_has_future_Qty():
    assert hasattr(Daily_production, "future_Qty")
    descriptor = None
    for klass in Daily_production.__mro__:
        if "future_Qty" in klass.__dict__:
            descriptor = klass.__dict__["future_Qty"]
            break
    assert isinstance(descriptor, property)

def test_daily_production_has_date():
    assert hasattr(Daily_production, "date")
    descriptor = None
    for klass in Daily_production.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_daily_production_has_pro_number():
    assert hasattr(Daily_production, "pro_number")
    descriptor = None
    for klass in Daily_production.__mro__:
        if "pro_number" in klass.__dict__:
            descriptor = klass.__dict__["pro_number"]
            break
    assert isinstance(descriptor, property)

def test_daily_production_has_curr_qty():
    assert hasattr(Daily_production, "curr_qty")
    descriptor = None
    for klass in Daily_production.__mro__:
        if "curr_qty" in klass.__dict__:
            descriptor = klass.__dict__["curr_qty"]
            break
    assert isinstance(descriptor, property)

def test_daily_production_has_item_name():
    assert hasattr(Daily_production, "item_name")
    descriptor = None
    for klass in Daily_production.__mro__:
        if "item_name" in klass.__dict__:
            descriptor = klass.__dict__["item_name"]
            break
    assert isinstance(descriptor, property)

def test_daily_production_has_section():
    assert hasattr(Daily_production, "section")
    descriptor = None
    for klass in Daily_production.__mro__:
        if "section" in klass.__dict__:
            descriptor = klass.__dict__["section"]
            break
    assert isinstance(descriptor, property)



def test_etf_epf_is_not_abstract():
    assert not inspect.isabstract(ETF_EPF)


def test_etf_epf_constructor_exists():
    assert callable(ETF_EPF.__init__)


def test_etf_epf_constructor_args():
    sig = inspect.signature(ETF_EPF.__init__)
    params = list(sig.parameters.keys())
    assert "no" in params, "Missing parameter 'no'"
    assert "rate" in params, "Missing parameter 'rate'"
    assert "type" in params, "Missing parameter 'type'"

def test_etf_epf_has_no():
    assert hasattr(ETF_EPF, "no")
    descriptor = None
    for klass in ETF_EPF.__mro__:
        if "no" in klass.__dict__:
            descriptor = klass.__dict__["no"]
            break
    assert isinstance(descriptor, property)

def test_etf_epf_has_rate():
    assert hasattr(ETF_EPF, "rate")
    descriptor = None
    for klass in ETF_EPF.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)

def test_etf_epf_has_type():
    assert hasattr(ETF_EPF, "type")
    descriptor = None
    for klass in ETF_EPF.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_bonus_is_not_abstract():
    assert not inspect.isabstract(Bonus)


def test_bonus_constructor_exists():
    assert callable(Bonus.__init__)


def test_bonus_constructor_args():
    sig = inspect.signature(Bonus.__init__)
    params = list(sig.parameters.keys())
    assert "IDnum" in params, "Missing parameter 'IDnum'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_bonus_has_IDnum():
    assert hasattr(Bonus, "IDnum")
    descriptor = None
    for klass in Bonus.__mro__:
        if "IDnum" in klass.__dict__:
            descriptor = klass.__dict__["IDnum"]
            break
    assert isinstance(descriptor, property)

def test_bonus_has_id():
    assert hasattr(Bonus, "id")
    descriptor = None
    for klass in Bonus.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bonus_has_type():
    assert hasattr(Bonus, "type")
    descriptor = None
    for klass in Bonus.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bonus_has_amount():
    assert hasattr(Bonus, "amount")
    descriptor = None
    for klass in Bonus.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "position" in params, "Missing parameter 'position'"
    assert "Salary" in params, "Missing parameter 'Salary'"

def test_salary_has_id():
    assert hasattr(Salary, "id")
    descriptor = None
    for klass in Salary.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_position():
    assert hasattr(Salary, "position")
    descriptor = None
    for klass in Salary.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_Salary():
    assert hasattr(Salary, "Salary")
    descriptor = None
    for klass in Salary.__mro__:
        if "Salary" in klass.__dict__:
            descriptor = klass.__dict__["Salary"]
            break
    assert isinstance(descriptor, property)



def test_order_sent_is_not_abstract():
    assert not inspect.isabstract(Order_Sent)


def test_order_sent_constructor_exists():
    assert callable(Order_Sent.__init__)


def test_order_sent_constructor_args():
    sig = inspect.signature(Order_Sent.__init__)
    params = list(sig.parameters.keys())
    assert "sentOrder_id" in params, "Missing parameter 'sentOrder_id'"
    assert "order_status" in params, "Missing parameter 'order_status'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "Item_id" in params, "Missing parameter 'Item_id'"

def test_order_sent_has_sentOrder_id():
    assert hasattr(Order_Sent, "sentOrder_id")
    descriptor = None
    for klass in Order_Sent.__mro__:
        if "sentOrder_id" in klass.__dict__:
            descriptor = klass.__dict__["sentOrder_id"]
            break
    assert isinstance(descriptor, property)

def test_order_sent_has_order_status():
    assert hasattr(Order_Sent, "order_status")
    descriptor = None
    for klass in Order_Sent.__mro__:
        if "order_status" in klass.__dict__:
            descriptor = klass.__dict__["order_status"]
            break
    assert isinstance(descriptor, property)

def test_order_sent_has_quantity():
    assert hasattr(Order_Sent, "quantity")
    descriptor = None
    for klass in Order_Sent.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_order_sent_has_Item_id():
    assert hasattr(Order_Sent, "Item_id")
    descriptor = None
    for klass in Order_Sent.__mro__:
        if "Item_id" in klass.__dict__:
            descriptor = klass.__dict__["Item_id"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"

def test_administrator_has_password():
    assert hasattr(Administrator, "password")
    descriptor = None
    for klass in Administrator.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_username():
    assert hasattr(Administrator, "username")
    descriptor = None
    for klass in Administrator.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_worker_is_not_abstract():
    assert not inspect.isabstract(Worker)


def test_worker_constructor_exists():
    assert callable(Worker.__init__)


def test_worker_constructor_args():
    sig = inspect.signature(Worker.__init__)
    params = list(sig.parameters.keys())
    assert "team" in params, "Missing parameter 'team'"
    assert "section" in params, "Missing parameter 'section'"

def test_worker_has_team():
    assert hasattr(Worker, "team")
    descriptor = None
    for klass in Worker.__mro__:
        if "team" in klass.__dict__:
            descriptor = klass.__dict__["team"]
            break
    assert isinstance(descriptor, property)

def test_worker_has_section():
    assert hasattr(Worker, "section")
    descriptor = None
    for klass in Worker.__mro__:
        if "section" in klass.__dict__:
            descriptor = klass.__dict__["section"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Position" in params, "Missing parameter 'Position'"

def test_staff_has_Position():
    assert hasattr(Staff, "Position")
    descriptor = None
    for klass in Staff.__mro__:
        if "Position" in klass.__dict__:
            descriptor = klass.__dict__["Position"]
            break
    assert isinstance(descriptor, property)



def test_leave_is_not_abstract():
    assert not inspect.isabstract(Leave)


def test_leave_constructor_exists():
    assert callable(Leave.__init__)


def test_leave_constructor_args():
    sig = inspect.signature(Leave.__init__)
    params = list(sig.parameters.keys())
    assert "leave_type" in params, "Missing parameter 'leave_type'"
    assert "from" in params, "Missing parameter 'from'"
    assert "leave_id" in params, "Missing parameter 'leave_id'"
    assert "date" in params, "Missing parameter 'date'"
    assert "to" in params, "Missing parameter 'to'"

def test_leave_has_leave_type():
    assert hasattr(Leave, "leave_type")
    descriptor = None
    for klass in Leave.__mro__:
        if "leave_type" in klass.__dict__:
            descriptor = klass.__dict__["leave_type"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_from():
    assert hasattr(Leave, "from")
    descriptor = None
    for klass in Leave.__mro__:
        if "from" in klass.__dict__:
            descriptor = klass.__dict__["from"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_leave_id():
    assert hasattr(Leave, "leave_id")
    descriptor = None
    for klass in Leave.__mro__:
        if "leave_id" in klass.__dict__:
            descriptor = klass.__dict__["leave_id"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_date():
    assert hasattr(Leave, "date")
    descriptor = None
    for klass in Leave.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_to():
    assert hasattr(Leave, "to")
    descriptor = None
    for klass in Leave.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_attendance_is_not_abstract():
    assert not inspect.isabstract(Attendance)


def test_attendance_constructor_exists():
    assert callable(Attendance.__init__)


def test_attendance_constructor_args():
    sig = inspect.signature(Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "att_id" in params, "Missing parameter 'att_id'"
    assert "date" in params, "Missing parameter 'date'"
    assert "work_hours" in params, "Missing parameter 'work_hours'"
    assert "in_time" in params, "Missing parameter 'in_time'"
    assert "out_time" in params, "Missing parameter 'out_time'"
    assert "OT_hours" in params, "Missing parameter 'OT_hours'"

def test_attendance_has_att_id():
    assert hasattr(Attendance, "att_id")
    descriptor = None
    for klass in Attendance.__mro__:
        if "att_id" in klass.__dict__:
            descriptor = klass.__dict__["att_id"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_date():
    assert hasattr(Attendance, "date")
    descriptor = None
    for klass in Attendance.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_work_hours():
    assert hasattr(Attendance, "work_hours")
    descriptor = None
    for klass in Attendance.__mro__:
        if "work_hours" in klass.__dict__:
            descriptor = klass.__dict__["work_hours"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_in_time():
    assert hasattr(Attendance, "in_time")
    descriptor = None
    for klass in Attendance.__mro__:
        if "in_time" in klass.__dict__:
            descriptor = klass.__dict__["in_time"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_out_time():
    assert hasattr(Attendance, "out_time")
    descriptor = None
    for klass in Attendance.__mro__:
        if "out_time" in klass.__dict__:
            descriptor = klass.__dict__["out_time"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_OT_hours():
    assert hasattr(Attendance, "OT_hours")
    descriptor = None
    for klass in Attendance.__mro__:
        if "OT_hours" in klass.__dict__:
            descriptor = klass.__dict__["OT_hours"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "lname" in params, "Missing parameter 'lname'"
    assert "emp_id" in params, "Missing parameter 'emp_id'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "DOB" in params, "Missing parameter 'DOB'"
    assert "email" in params, "Missing parameter 'email'"
    assert "attendance_count" in params, "Missing parameter 'attendance_count'"

def test_employee_has_address():
    assert hasattr(Employee, "address")
    descriptor = None
    for klass in Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_lname():
    assert hasattr(Employee, "lname")
    descriptor = None
    for klass in Employee.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_emp_id():
    assert hasattr(Employee, "emp_id")
    descriptor = None
    for klass in Employee.__mro__:
        if "emp_id" in klass.__dict__:
            descriptor = klass.__dict__["emp_id"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_fname():
    assert hasattr(Employee, "fname")
    descriptor = None
    for klass in Employee.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_phone():
    assert hasattr(Employee, "phone")
    descriptor = None
    for klass in Employee.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_DOB():
    assert hasattr(Employee, "DOB")
    descriptor = None
    for klass in Employee.__mro__:
        if "DOB" in klass.__dict__:
            descriptor = klass.__dict__["DOB"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_email():
    assert hasattr(Employee, "email")
    descriptor = None
    for klass in Employee.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_attendance_count():
    assert hasattr(Employee, "attendance_count")
    descriptor = None
    for klass in Employee.__mro__:
        if "attendance_count" in klass.__dict__:
            descriptor = klass.__dict__["attendance_count"]
            break
    assert isinstance(descriptor, property)



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "section_id" in params, "Missing parameter 'section_id'"

def test_section_has_name():
    assert hasattr(Section, "name")
    descriptor = None
    for klass in Section.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_section_has_description():
    assert hasattr(Section, "description")
    descriptor = None
    for klass in Section.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_section_has_section_id():
    assert hasattr(Section, "section_id")
    descriptor = None
    for klass in Section.__mro__:
        if "section_id" in klass.__dict__:
            descriptor = klass.__dict__["section_id"]
            break
    assert isinstance(descriptor, property)



def test_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_items_is_not_abstract():
    assert not inspect.isabstract(Items)


def test_items_constructor_exists():
    assert callable(Items.__init__)


def test_items_constructor_args():
    sig = inspect.signature(Items.__init__)
    params = list(sig.parameters.keys())
    assert "price_per_unit" in params, "Missing parameter 'price_per_unit'"
    assert "description" in params, "Missing parameter 'description'"
    assert "unit_of_measure" in params, "Missing parameter 'unit_of_measure'"
    assert "re_order_qty" in params, "Missing parameter 're_order_qty'"
    assert "item_id" in params, "Missing parameter 'item_id'"
    assert "item_code" in params, "Missing parameter 'item_code'"

def test_items_has_price_per_unit():
    assert hasattr(Items, "price_per_unit")
    descriptor = None
    for klass in Items.__mro__:
        if "price_per_unit" in klass.__dict__:
            descriptor = klass.__dict__["price_per_unit"]
            break
    assert isinstance(descriptor, property)

def test_items_has_description():
    assert hasattr(Items, "description")
    descriptor = None
    for klass in Items.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_items_has_unit_of_measure():
    assert hasattr(Items, "unit_of_measure")
    descriptor = None
    for klass in Items.__mro__:
        if "unit_of_measure" in klass.__dict__:
            descriptor = klass.__dict__["unit_of_measure"]
            break
    assert isinstance(descriptor, property)

def test_items_has_re_order_qty():
    assert hasattr(Items, "re_order_qty")
    descriptor = None
    for klass in Items.__mro__:
        if "re_order_qty" in klass.__dict__:
            descriptor = klass.__dict__["re_order_qty"]
            break
    assert isinstance(descriptor, property)

def test_items_has_item_id():
    assert hasattr(Items, "item_id")
    descriptor = None
    for klass in Items.__mro__:
        if "item_id" in klass.__dict__:
            descriptor = klass.__dict__["item_id"]
            break
    assert isinstance(descriptor, property)

def test_items_has_item_code():
    assert hasattr(Items, "item_code")
    descriptor = None
    for klass in Items.__mro__:
        if "item_code" in klass.__dict__:
            descriptor = klass.__dict__["item_code"]
            break
    assert isinstance(descriptor, property)



def test_stock_is_not_abstract():
    assert not inspect.isabstract(Stock)


def test_stock_constructor_exists():
    assert callable(Stock.__init__)


def test_stock_constructor_args():
    sig = inspect.signature(Stock.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "item_id" in params, "Missing parameter 'item_id'"
    assert "stock_id" in params, "Missing parameter 'stock_id'"
    assert "exp_date" in params, "Missing parameter 'exp_date'"

def test_stock_has_quantity():
    assert hasattr(Stock, "quantity")
    descriptor = None
    for klass in Stock.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_stock_has_item_id():
    assert hasattr(Stock, "item_id")
    descriptor = None
    for klass in Stock.__mro__:
        if "item_id" in klass.__dict__:
            descriptor = klass.__dict__["item_id"]
            break
    assert isinstance(descriptor, property)

def test_stock_has_stock_id():
    assert hasattr(Stock, "stock_id")
    descriptor = None
    for klass in Stock.__mro__:
        if "stock_id" in klass.__dict__:
            descriptor = klass.__dict__["stock_id"]
            break
    assert isinstance(descriptor, property)

def test_stock_has_exp_date():
    assert hasattr(Stock, "exp_date")
    descriptor = None
    for klass in Stock.__mro__:
        if "exp_date" in klass.__dict__:
            descriptor = klass.__dict__["exp_date"]
            break
    assert isinstance(descriptor, property)



def test_orders_is_not_abstract():
    assert not inspect.isabstract(Orders)


def test_orders_constructor_exists():
    assert callable(Orders.__init__)


def test_orders_constructor_args():
    sig = inspect.signature(Orders.__init__)
    params = list(sig.parameters.keys())
    assert "total_amount" in params, "Missing parameter 'total_amount'"
    assert "price_per_unit" in params, "Missing parameter 'price_per_unit'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "order_date" in params, "Missing parameter 'order_date'"
    assert "status" in params, "Missing parameter 'status'"
    assert "item_id" in params, "Missing parameter 'item_id'"
    assert "order_id" in params, "Missing parameter 'order_id'"
    assert "recieved_date" in params, "Missing parameter 'recieved_date'"

def test_orders_has_total_amount():
    assert hasattr(Orders, "total_amount")
    descriptor = None
    for klass in Orders.__mro__:
        if "total_amount" in klass.__dict__:
            descriptor = klass.__dict__["total_amount"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_price_per_unit():
    assert hasattr(Orders, "price_per_unit")
    descriptor = None
    for klass in Orders.__mro__:
        if "price_per_unit" in klass.__dict__:
            descriptor = klass.__dict__["price_per_unit"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_Quantity():
    assert hasattr(Orders, "Quantity")
    descriptor = None
    for klass in Orders.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_order_date():
    assert hasattr(Orders, "order_date")
    descriptor = None
    for klass in Orders.__mro__:
        if "order_date" in klass.__dict__:
            descriptor = klass.__dict__["order_date"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_status():
    assert hasattr(Orders, "status")
    descriptor = None
    for klass in Orders.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_item_id():
    assert hasattr(Orders, "item_id")
    descriptor = None
    for klass in Orders.__mro__:
        if "item_id" in klass.__dict__:
            descriptor = klass.__dict__["item_id"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_order_id():
    assert hasattr(Orders, "order_id")
    descriptor = None
    for klass in Orders.__mro__:
        if "order_id" in klass.__dict__:
            descriptor = klass.__dict__["order_id"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_recieved_date():
    assert hasattr(Orders, "recieved_date")
    descriptor = None
    for klass in Orders.__mro__:
        if "recieved_date" in klass.__dict__:
            descriptor = klass.__dict__["recieved_date"]
            break
    assert isinstance(descriptor, property)



def test_supplier_is_not_abstract():
    assert not inspect.isabstract(Supplier)


def test_supplier_constructor_exists():
    assert callable(Supplier.__init__)


def test_supplier_constructor_args():
    sig = inspect.signature(Supplier.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "contact_no" in params, "Missing parameter 'contact_no'"
    assert "email" in params, "Missing parameter 'email'"
    assert "Supplier_id" in params, "Missing parameter 'Supplier_id'"

def test_supplier_has_address():
    assert hasattr(Supplier, "address")
    descriptor = None
    for klass in Supplier.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_name():
    assert hasattr(Supplier, "name")
    descriptor = None
    for klass in Supplier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_contact_no():
    assert hasattr(Supplier, "contact_no")
    descriptor = None
    for klass in Supplier.__mro__:
        if "contact_no" in klass.__dict__:
            descriptor = klass.__dict__["contact_no"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_email():
    assert hasattr(Supplier, "email")
    descriptor = None
    for klass in Supplier.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_Supplier_id():
    assert hasattr(Supplier, "Supplier_id")
    descriptor = None
    for klass in Supplier.__mro__:
        if "Supplier_id" in klass.__dict__:
            descriptor = klass.__dict__["Supplier_id"]
            break
    assert isinstance(descriptor, property)


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Daily_production_strategy = st.builds(
    Daily_production,
    item_code=
        safe_text,
    future_Qty=
        st.integers(),
    date=
        safe_text,
    pro_number=
        safe_text,
    curr_qty=
        st.integers(),
    item_name=
        safe_text,
    section=
        st.integers()
)
ETF_EPF_strategy = st.builds(
    ETF_EPF,
    no=
        st.integers(),
    rate=
        safe_text,
    type=
        safe_text
)
Bonus_strategy = st.builds(
    Bonus,
    IDnum=
        st.integers(),
    id=
        st.integers(),
    type=
        safe_text,
    amount=
        safe_text
)
Salary_strategy = st.builds(
    Salary,
    id=
        st.integers(),
    position=
        safe_text,
    Salary=
        safe_text
)
Order_Sent_strategy = st.builds(
    Order_Sent,
    sentOrder_id=
        safe_text,
    order_status=
        safe_text,
    quantity=
        safe_text,
    Item_id=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    password=
        safe_text,
    username=
        safe_text
)
Worker_strategy = st.builds(
    Worker,
    team=
        st.integers(),
    section=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    Position=
        safe_text
)
Leave_strategy = st.builds(
    Leave,
    leave_type=
        safe_text,
    from=
        safe_text,
    leave_id=
        safe_text,
    date=
        safe_text,
    to=
        safe_text
)
Attendance_strategy = st.builds(
    Attendance,
    att_id=
        safe_text,
    date=
        safe_text,
    work_hours=
        safe_text,
    in_time=
        safe_text,
    out_time=
        safe_text,
    OT_hours=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    address=
        safe_text,
    lname=
        safe_text,
    emp_id=
        safe_text,
    fname=
        safe_text,
    phone=
        st.integers(),
    DOB=
        safe_text,
    email=
        safe_text,
    attendance_count=
        st.integers()
)
Section_strategy = st.builds(
    Section,
    name=
        safe_text,
    description=
        safe_text,
    section_id=
        safe_text
)
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
Items_strategy = st.builds(
    Items,
    price_per_unit=
        safe_text,
    description=
        safe_text,
    unit_of_measure=
        safe_text,
    re_order_qty=
        safe_text,
    item_id=
        safe_text,
    item_code=
        safe_text
)
Stock_strategy = st.builds(
    Stock,
    quantity=
        safe_text,
    item_id=
        safe_text,
    stock_id=
        safe_text,
    exp_date=
        safe_text
)
Orders_strategy = st.builds(
    Orders,
    total_amount=
        safe_text,
    price_per_unit=
        safe_text,
    Quantity=
        safe_text,
    order_date=
        safe_text,
    status=
        safe_text,
    item_id=
        safe_text,
    order_id=
        safe_text,
    recieved_date=
        safe_text
)
Supplier_strategy = st.builds(
    Supplier,
    address=
        safe_text,
    name=
        safe_text,
    contact_no=
        st.integers(),
    email=
        safe_text,
    Supplier_id=
        safe_text
)

@given(instance=Daily_production_strategy)
@settings(max_examples=50)
def test_daily_production_instantiation(instance):
    assert isinstance(instance, Daily_production)



@given(instance=Daily_production_strategy)
def test_daily_production_item_code_setter(instance):
    original = instance.item_code
    instance.item_code = original
    assert instance.item_code == original



@given(instance=Daily_production_strategy)
def test_daily_production_future_Qty_setter(instance):
    original = instance.future_Qty
    instance.future_Qty = original
    assert instance.future_Qty == original



@given(instance=Daily_production_strategy)
def test_daily_production_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Daily_production_strategy)
def test_daily_production_pro_number_setter(instance):
    original = instance.pro_number
    instance.pro_number = original
    assert instance.pro_number == original



@given(instance=Daily_production_strategy)
def test_daily_production_curr_qty_setter(instance):
    original = instance.curr_qty
    instance.curr_qty = original
    assert instance.curr_qty == original



@given(instance=Daily_production_strategy)
def test_daily_production_item_name_setter(instance):
    original = instance.item_name
    instance.item_name = original
    assert instance.item_name == original



@given(instance=Daily_production_strategy)
def test_daily_production_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original

@given(instance=ETF_EPF_strategy)
@settings(max_examples=50)
def test_etf_epf_instantiation(instance):
    assert isinstance(instance, ETF_EPF)



@given(instance=ETF_EPF_strategy)
def test_etf_epf_no_setter(instance):
    original = instance.no
    instance.no = original
    assert instance.no == original



@given(instance=ETF_EPF_strategy)
def test_etf_epf_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original



@given(instance=ETF_EPF_strategy)
def test_etf_epf_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Bonus_strategy)
@settings(max_examples=50)
def test_bonus_instantiation(instance):
    assert isinstance(instance, Bonus)



@given(instance=Bonus_strategy)
def test_bonus_IDnum_setter(instance):
    original = instance.IDnum
    instance.IDnum = original
    assert instance.IDnum == original



@given(instance=Bonus_strategy)
def test_bonus_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Bonus_strategy)
def test_bonus_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Bonus_strategy)
def test_bonus_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Salary_strategy)
@settings(max_examples=50)
def test_salary_instantiation(instance):
    assert isinstance(instance, Salary)



@given(instance=Salary_strategy)
def test_salary_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Salary_strategy)
def test_salary_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=Salary_strategy)
def test_salary_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original

@given(instance=Order_Sent_strategy)
@settings(max_examples=50)
def test_order_sent_instantiation(instance):
    assert isinstance(instance, Order_Sent)



@given(instance=Order_Sent_strategy)
def test_order_sent_sentOrder_id_setter(instance):
    original = instance.sentOrder_id
    instance.sentOrder_id = original
    assert instance.sentOrder_id == original



@given(instance=Order_Sent_strategy)
def test_order_sent_order_status_setter(instance):
    original = instance.order_status
    instance.order_status = original
    assert instance.order_status == original



@given(instance=Order_Sent_strategy)
def test_order_sent_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Order_Sent_strategy)
def test_order_sent_Item_id_setter(instance):
    original = instance.Item_id
    instance.Item_id = original
    assert instance.Item_id == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Administrator_strategy)
def test_administrator_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Worker_strategy)
@settings(max_examples=50)
def test_worker_instantiation(instance):
    assert isinstance(instance, Worker)



@given(instance=Worker_strategy)
def test_worker_team_setter(instance):
    original = instance.team
    instance.team = original
    assert instance.team == original



@given(instance=Worker_strategy)
def test_worker_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_Position_setter(instance):
    original = instance.Position
    instance.Position = original
    assert instance.Position == original

@given(instance=Leave_strategy)
@settings(max_examples=50)
def test_leave_instantiation(instance):
    assert isinstance(instance, Leave)



@given(instance=Leave_strategy)
def test_leave_leave_type_setter(instance):
    original = instance.leave_type
    instance.leave_type = original
    assert instance.leave_type == original



@given(instance=Leave_strategy)
def test_leave_from_setter(instance):
    original = instance.from
    instance.from = original
    assert instance.from == original



@given(instance=Leave_strategy)
def test_leave_leave_id_setter(instance):
    original = instance.leave_id
    instance.leave_id = original
    assert instance.leave_id == original



@given(instance=Leave_strategy)
def test_leave_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Leave_strategy)
def test_leave_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=Attendance_strategy)
@settings(max_examples=50)
def test_attendance_instantiation(instance):
    assert isinstance(instance, Attendance)



@given(instance=Attendance_strategy)
def test_attendance_att_id_setter(instance):
    original = instance.att_id
    instance.att_id = original
    assert instance.att_id == original



@given(instance=Attendance_strategy)
def test_attendance_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Attendance_strategy)
def test_attendance_work_hours_setter(instance):
    original = instance.work_hours
    instance.work_hours = original
    assert instance.work_hours == original



@given(instance=Attendance_strategy)
def test_attendance_in_time_setter(instance):
    original = instance.in_time
    instance.in_time = original
    assert instance.in_time == original



@given(instance=Attendance_strategy)
def test_attendance_out_time_setter(instance):
    original = instance.out_time
    instance.out_time = original
    assert instance.out_time == original



@given(instance=Attendance_strategy)
def test_attendance_OT_hours_setter(instance):
    original = instance.OT_hours
    instance.OT_hours = original
    assert instance.OT_hours == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Employee_strategy)
def test_employee_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Employee_strategy)
def test_employee_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original



@given(instance=Employee_strategy)
def test_employee_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Employee_strategy)
def test_employee_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Employee_strategy)
def test_employee_DOB_setter(instance):
    original = instance.DOB
    instance.DOB = original
    assert instance.DOB == original



@given(instance=Employee_strategy)
def test_employee_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Employee_strategy)
def test_employee_attendance_count_setter(instance):
    original = instance.attendance_count
    instance.attendance_count = original
    assert instance.attendance_count == original

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)



@given(instance=Section_strategy)
def test_section_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Section_strategy)
def test_section_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Section_strategy)
def test_section_section_id_setter(instance):
    original = instance.section_id
    instance.section_id = original
    assert instance.section_id == original

@given(instance=Interface_Interface_strategy)
@settings(max_examples=50)
def test_interface_interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)

@given(instance=Items_strategy)
@settings(max_examples=50)
def test_items_instantiation(instance):
    assert isinstance(instance, Items)



@given(instance=Items_strategy)
def test_items_price_per_unit_setter(instance):
    original = instance.price_per_unit
    instance.price_per_unit = original
    assert instance.price_per_unit == original



@given(instance=Items_strategy)
def test_items_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Items_strategy)
def test_items_unit_of_measure_setter(instance):
    original = instance.unit_of_measure
    instance.unit_of_measure = original
    assert instance.unit_of_measure == original



@given(instance=Items_strategy)
def test_items_re_order_qty_setter(instance):
    original = instance.re_order_qty
    instance.re_order_qty = original
    assert instance.re_order_qty == original



@given(instance=Items_strategy)
def test_items_item_id_setter(instance):
    original = instance.item_id
    instance.item_id = original
    assert instance.item_id == original



@given(instance=Items_strategy)
def test_items_item_code_setter(instance):
    original = instance.item_code
    instance.item_code = original
    assert instance.item_code == original

@given(instance=Stock_strategy)
@settings(max_examples=50)
def test_stock_instantiation(instance):
    assert isinstance(instance, Stock)



@given(instance=Stock_strategy)
def test_stock_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Stock_strategy)
def test_stock_item_id_setter(instance):
    original = instance.item_id
    instance.item_id = original
    assert instance.item_id == original



@given(instance=Stock_strategy)
def test_stock_stock_id_setter(instance):
    original = instance.stock_id
    instance.stock_id = original
    assert instance.stock_id == original



@given(instance=Stock_strategy)
def test_stock_exp_date_setter(instance):
    original = instance.exp_date
    instance.exp_date = original
    assert instance.exp_date == original

@given(instance=Orders_strategy)
@settings(max_examples=50)
def test_orders_instantiation(instance):
    assert isinstance(instance, Orders)



@given(instance=Orders_strategy)
def test_orders_total_amount_setter(instance):
    original = instance.total_amount
    instance.total_amount = original
    assert instance.total_amount == original



@given(instance=Orders_strategy)
def test_orders_price_per_unit_setter(instance):
    original = instance.price_per_unit
    instance.price_per_unit = original
    assert instance.price_per_unit == original



@given(instance=Orders_strategy)
def test_orders_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Orders_strategy)
def test_orders_order_date_setter(instance):
    original = instance.order_date
    instance.order_date = original
    assert instance.order_date == original



@given(instance=Orders_strategy)
def test_orders_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Orders_strategy)
def test_orders_item_id_setter(instance):
    original = instance.item_id
    instance.item_id = original
    assert instance.item_id == original



@given(instance=Orders_strategy)
def test_orders_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original



@given(instance=Orders_strategy)
def test_orders_recieved_date_setter(instance):
    original = instance.recieved_date
    instance.recieved_date = original
    assert instance.recieved_date == original

@given(instance=Supplier_strategy)
@settings(max_examples=50)
def test_supplier_instantiation(instance):
    assert isinstance(instance, Supplier)



@given(instance=Supplier_strategy)
def test_supplier_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Supplier_strategy)
def test_supplier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Supplier_strategy)
def test_supplier_contact_no_setter(instance):
    original = instance.contact_no
    instance.contact_no = original
    assert instance.contact_no == original



@given(instance=Supplier_strategy)
def test_supplier_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Supplier_strategy)
def test_supplier_Supplier_id_setter(instance):
    original = instance.Supplier_id
    instance.Supplier_id = original
    assert instance.Supplier_id == original
