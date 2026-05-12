import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Menu,
    MenuItem,
    FoodItem,
    DrinksItem,
    Customer,
    Order,
    Report,
    Kasir,
    Karyawan,
    Bartender,
    Chef,
    Manager_Owner,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_menu_is_not_abstract():
    assert not inspect.isabstract(Menu)


def test_menu_constructor_exists():
    assert callable(Menu.__init__)


def test_menu_constructor_args():
    sig = inspect.signature(Menu.__init__)
    params = list(sig.parameters.keys())
    assert "drinksItem" in params, "Missing parameter 'drinksItem'"
    assert "category" in params, "Missing parameter 'category'"
    assert "foodItem" in params, "Missing parameter 'foodItem'"

def test_menu_has_drinksItem():
    assert hasattr(Menu, "drinksItem")
    descriptor = None
    for klass in Menu.__mro__:
        if "drinksItem" in klass.__dict__:
            descriptor = klass.__dict__["drinksItem"]
            break
    assert isinstance(descriptor, property)

def test_menu_has_category():
    assert hasattr(Menu, "category")
    descriptor = None
    for klass in Menu.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_menu_has_foodItem():
    assert hasattr(Menu, "foodItem")
    descriptor = None
    for klass in Menu.__mro__:
        if "foodItem" in klass.__dict__:
            descriptor = klass.__dict__["foodItem"]
            break
    assert isinstance(descriptor, property)



def test_menuitem_is_not_abstract():
    assert not inspect.isabstract(MenuItem)


def test_menuitem_constructor_exists():
    assert callable(MenuItem.__init__)


def test_menuitem_constructor_args():
    sig = inspect.signature(MenuItem.__init__)
    params = list(sig.parameters.keys())
    assert "item_Id" in params, "Missing parameter 'item_Id'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "available" in params, "Missing parameter 'available'"
    assert "item_description" in params, "Missing parameter 'item_description'"
    assert "item_price" in params, "Missing parameter 'item_price'"

def test_menuitem_has_item_Id():
    assert hasattr(MenuItem, "item_Id")
    descriptor = None
    for klass in MenuItem.__mro__:
        if "item_Id" in klass.__dict__:
            descriptor = klass.__dict__["item_Id"]
            break
    assert isinstance(descriptor, property)

def test_menuitem_has_quantity():
    assert hasattr(MenuItem, "quantity")
    descriptor = None
    for klass in MenuItem.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_menuitem_has_available():
    assert hasattr(MenuItem, "available")
    descriptor = None
    for klass in MenuItem.__mro__:
        if "available" in klass.__dict__:
            descriptor = klass.__dict__["available"]
            break
    assert isinstance(descriptor, property)

def test_menuitem_has_item_description():
    assert hasattr(MenuItem, "item_description")
    descriptor = None
    for klass in MenuItem.__mro__:
        if "item_description" in klass.__dict__:
            descriptor = klass.__dict__["item_description"]
            break
    assert isinstance(descriptor, property)

def test_menuitem_has_item_price():
    assert hasattr(MenuItem, "item_price")
    descriptor = None
    for klass in MenuItem.__mro__:
        if "item_price" in klass.__dict__:
            descriptor = klass.__dict__["item_price"]
            break
    assert isinstance(descriptor, property)



def test_fooditem_is_not_abstract():
    assert not inspect.isabstract(FoodItem)


def test_fooditem_constructor_exists():
    assert callable(FoodItem.__init__)


def test_fooditem_constructor_args():
    sig = inspect.signature(FoodItem.__init__)
    params = list(sig.parameters.keys())
    assert "drinkType" in params, "Missing parameter 'drinkType'"

def test_fooditem_has_drinkType():
    assert hasattr(FoodItem, "drinkType")
    descriptor = None
    for klass in FoodItem.__mro__:
        if "drinkType" in klass.__dict__:
            descriptor = klass.__dict__["drinkType"]
            break
    assert isinstance(descriptor, property)



def test_drinksitem_is_not_abstract():
    assert not inspect.isabstract(DrinksItem)


def test_drinksitem_constructor_exists():
    assert callable(DrinksItem.__init__)


def test_drinksitem_constructor_args():
    sig = inspect.signature(DrinksItem.__init__)
    params = list(sig.parameters.keys())
    assert "drinkType" in params, "Missing parameter 'drinkType'"

def test_drinksitem_has_drinkType():
    assert hasattr(DrinksItem, "drinkType")
    descriptor = None
    for klass in DrinksItem.__mro__:
        if "drinkType" in klass.__dict__:
            descriptor = klass.__dict__["drinkType"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "cust_Id" in params, "Missing parameter 'cust_Id'"
    assert "cust_name" in params, "Missing parameter 'cust_name'"

def test_customer_has_cust_Id():
    assert hasattr(Customer, "cust_Id")
    descriptor = None
    for klass in Customer.__mro__:
        if "cust_Id" in klass.__dict__:
            descriptor = klass.__dict__["cust_Id"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_cust_name():
    assert hasattr(Customer, "cust_name")
    descriptor = None
    for klass in Customer.__mro__:
        if "cust_name" in klass.__dict__:
            descriptor = klass.__dict__["cust_name"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "numTable" in params, "Missing parameter 'numTable'"
    assert "cust_id" in params, "Missing parameter 'cust_id'"
    assert "foodItem" in params, "Missing parameter 'foodItem'"
    assert "drinksItem" in params, "Missing parameter 'drinksItem'"
    assert "cust_name" in params, "Missing parameter 'cust_name'"
    assert "order_Id" in params, "Missing parameter 'order_Id'"

def test_order_has_numTable():
    assert hasattr(Order, "numTable")
    descriptor = None
    for klass in Order.__mro__:
        if "numTable" in klass.__dict__:
            descriptor = klass.__dict__["numTable"]
            break
    assert isinstance(descriptor, property)

def test_order_has_cust_id():
    assert hasattr(Order, "cust_id")
    descriptor = None
    for klass in Order.__mro__:
        if "cust_id" in klass.__dict__:
            descriptor = klass.__dict__["cust_id"]
            break
    assert isinstance(descriptor, property)

def test_order_has_foodItem():
    assert hasattr(Order, "foodItem")
    descriptor = None
    for klass in Order.__mro__:
        if "foodItem" in klass.__dict__:
            descriptor = klass.__dict__["foodItem"]
            break
    assert isinstance(descriptor, property)

def test_order_has_drinksItem():
    assert hasattr(Order, "drinksItem")
    descriptor = None
    for klass in Order.__mro__:
        if "drinksItem" in klass.__dict__:
            descriptor = klass.__dict__["drinksItem"]
            break
    assert isinstance(descriptor, property)

def test_order_has_cust_name():
    assert hasattr(Order, "cust_name")
    descriptor = None
    for klass in Order.__mro__:
        if "cust_name" in klass.__dict__:
            descriptor = klass.__dict__["cust_name"]
            break
    assert isinstance(descriptor, property)

def test_order_has_order_Id():
    assert hasattr(Order, "order_Id")
    descriptor = None
    for klass in Order.__mro__:
        if "order_Id" in klass.__dict__:
            descriptor = klass.__dict__["order_Id"]
            break
    assert isinstance(descriptor, property)



def test_report_is_not_abstract():
    assert not inspect.isabstract(Report)


def test_report_constructor_exists():
    assert callable(Report.__init__)


def test_report_constructor_args():
    sig = inspect.signature(Report.__init__)
    params = list(sig.parameters.keys())
    assert "orders" in params, "Missing parameter 'orders'"
    assert "profit" in params, "Missing parameter 'profit'"
    assert "totalSales" in params, "Missing parameter 'totalSales'"

def test_report_has_orders():
    assert hasattr(Report, "orders")
    descriptor = None
    for klass in Report.__mro__:
        if "orders" in klass.__dict__:
            descriptor = klass.__dict__["orders"]
            break
    assert isinstance(descriptor, property)

def test_report_has_profit():
    assert hasattr(Report, "profit")
    descriptor = None
    for klass in Report.__mro__:
        if "profit" in klass.__dict__:
            descriptor = klass.__dict__["profit"]
            break
    assert isinstance(descriptor, property)

def test_report_has_totalSales():
    assert hasattr(Report, "totalSales")
    descriptor = None
    for klass in Report.__mro__:
        if "totalSales" in klass.__dict__:
            descriptor = klass.__dict__["totalSales"]
            break
    assert isinstance(descriptor, property)



def test_kasir_is_not_abstract():
    assert not inspect.isabstract(Kasir)


def test_kasir_constructor_exists():
    assert callable(Kasir.__init__)


def test_kasir_constructor_args():
    sig = inspect.signature(Kasir.__init__)
    params = list(sig.parameters.keys())
    assert "cust_id" in params, "Missing parameter 'cust_id'"
    assert "order_id" in params, "Missing parameter 'order_id'"

def test_kasir_has_cust_id():
    assert hasattr(Kasir, "cust_id")
    descriptor = None
    for klass in Kasir.__mro__:
        if "cust_id" in klass.__dict__:
            descriptor = klass.__dict__["cust_id"]
            break
    assert isinstance(descriptor, property)

def test_kasir_has_order_id():
    assert hasattr(Kasir, "order_id")
    descriptor = None
    for klass in Kasir.__mro__:
        if "order_id" in klass.__dict__:
            descriptor = klass.__dict__["order_id"]
            break
    assert isinstance(descriptor, property)



def test_karyawan_is_not_abstract():
    assert not inspect.isabstract(Karyawan)


def test_karyawan_constructor_exists():
    assert callable(Karyawan.__init__)


def test_karyawan_constructor_args():
    sig = inspect.signature(Karyawan.__init__)
    params = list(sig.parameters.keys())
    assert "staff_Id" in params, "Missing parameter 'staff_Id'"
    assert "contact" in params, "Missing parameter 'contact'"
    assert "name" in params, "Missing parameter 'name'"

def test_karyawan_has_staff_Id():
    assert hasattr(Karyawan, "staff_Id")
    descriptor = None
    for klass in Karyawan.__mro__:
        if "staff_Id" in klass.__dict__:
            descriptor = klass.__dict__["staff_Id"]
            break
    assert isinstance(descriptor, property)

def test_karyawan_has_contact():
    assert hasattr(Karyawan, "contact")
    descriptor = None
    for klass in Karyawan.__mro__:
        if "contact" in klass.__dict__:
            descriptor = klass.__dict__["contact"]
            break
    assert isinstance(descriptor, property)

def test_karyawan_has_name():
    assert hasattr(Karyawan, "name")
    descriptor = None
    for klass in Karyawan.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bartender_is_not_abstract():
    assert not inspect.isabstract(Bartender)


def test_bartender_constructor_exists():
    assert callable(Bartender.__init__)


def test_bartender_constructor_args():
    sig = inspect.signature(Bartender.__init__)
    params = list(sig.parameters.keys())
    assert "staff_Id" in params, "Missing parameter 'staff_Id'"
    assert "name" in params, "Missing parameter 'name'"

def test_bartender_has_staff_Id():
    assert hasattr(Bartender, "staff_Id")
    descriptor = None
    for klass in Bartender.__mro__:
        if "staff_Id" in klass.__dict__:
            descriptor = klass.__dict__["staff_Id"]
            break
    assert isinstance(descriptor, property)

def test_bartender_has_name():
    assert hasattr(Bartender, "name")
    descriptor = None
    for klass in Bartender.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_chef_is_not_abstract():
    assert not inspect.isabstract(Chef)


def test_chef_constructor_exists():
    assert callable(Chef.__init__)


def test_chef_constructor_args():
    sig = inspect.signature(Chef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "staff_Id" in params, "Missing parameter 'staff_Id'"

def test_chef_has_name():
    assert hasattr(Chef, "name")
    descriptor = None
    for klass in Chef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_chef_has_staff_Id():
    assert hasattr(Chef, "staff_Id")
    descriptor = None
    for klass in Chef.__mro__:
        if "staff_Id" in klass.__dict__:
            descriptor = klass.__dict__["staff_Id"]
            break
    assert isinstance(descriptor, property)



def test_manager_owner_is_not_abstract():
    assert not inspect.isabstract(Manager_Owner)


def test_manager_owner_constructor_exists():
    assert callable(Manager_Owner.__init__)


def test_manager_owner_constructor_args():
    sig = inspect.signature(Manager_Owner.__init__)
    params = list(sig.parameters.keys())


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
Menu_strategy = st.builds(
    Menu,
    drinksItem=
        st.none(),
    category=
        safe_text,
    foodItem=
        st.none()
)
MenuItem_strategy = st.builds(
    MenuItem,
    item_Id=
        st.integers(),
    quantity=
        st.integers(),
    available=
        st.booleans(),
    item_description=
        safe_text,
    item_price=
        st.integers()
)
FoodItem_strategy = st.builds(
    FoodItem,
    drinkType=
        safe_text
)
DrinksItem_strategy = st.builds(
    DrinksItem,
    drinkType=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    cust_Id=
        safe_text,
    cust_name=
        safe_text
)
Order_strategy = st.builds(
    Order,
    numTable=
        st.integers(),
    cust_id=
        safe_text,
    foodItem=
        st.none(),
    drinksItem=
        st.none(),
    cust_name=
        safe_text,
    order_Id=
        safe_text
)
Report_strategy = st.builds(
    Report,
    orders=
        safe_text,
    profit=
        safe_text,
    totalSales=
        safe_text
)
Kasir_strategy = st.builds(
    Kasir,
    cust_id=
        safe_text,
    order_id=
        safe_text
)
Karyawan_strategy = st.builds(
    Karyawan,
    staff_Id=
        safe_text,
    contact=
        safe_text,
    name=
        safe_text
)
Bartender_strategy = st.builds(
    Bartender,
    staff_Id=
        safe_text,
    name=
        safe_text
)
Chef_strategy = st.builds(
    Chef,
    name=
        safe_text,
    staff_Id=
        safe_text
)
Manager_Owner_strategy = st.builds(
    Manager_Owner,
)

@given(instance=Menu_strategy)
@settings(max_examples=50)
def test_menu_instantiation(instance):
    assert isinstance(instance, Menu)



@given(instance=Menu_strategy)
def test_menu_drinksItem_setter(instance):
    original = instance.drinksItem
    instance.drinksItem = original
    assert instance.drinksItem == original



@given(instance=Menu_strategy)
def test_menu_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=Menu_strategy)
def test_menu_foodItem_setter(instance):
    original = instance.foodItem
    instance.foodItem = original
    assert instance.foodItem == original

@given(instance=MenuItem_strategy)
@settings(max_examples=50)
def test_menuitem_instantiation(instance):
    assert isinstance(instance, MenuItem)



@given(instance=MenuItem_strategy)
def test_menuitem_item_Id_setter(instance):
    original = instance.item_Id
    instance.item_Id = original
    assert instance.item_Id == original



@given(instance=MenuItem_strategy)
def test_menuitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=MenuItem_strategy)
def test_menuitem_available_setter(instance):
    original = instance.available
    instance.available = original
    assert instance.available == original



@given(instance=MenuItem_strategy)
def test_menuitem_item_description_setter(instance):
    original = instance.item_description
    instance.item_description = original
    assert instance.item_description == original



@given(instance=MenuItem_strategy)
def test_menuitem_item_price_setter(instance):
    original = instance.item_price
    instance.item_price = original
    assert instance.item_price == original

@given(instance=FoodItem_strategy)
@settings(max_examples=50)
def test_fooditem_instantiation(instance):
    assert isinstance(instance, FoodItem)



@given(instance=FoodItem_strategy)
def test_fooditem_drinkType_setter(instance):
    original = instance.drinkType
    instance.drinkType = original
    assert instance.drinkType == original

@given(instance=DrinksItem_strategy)
@settings(max_examples=50)
def test_drinksitem_instantiation(instance):
    assert isinstance(instance, DrinksItem)



@given(instance=DrinksItem_strategy)
def test_drinksitem_drinkType_setter(instance):
    original = instance.drinkType
    instance.drinkType = original
    assert instance.drinkType == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_cust_Id_setter(instance):
    original = instance.cust_Id
    instance.cust_Id = original
    assert instance.cust_Id == original



@given(instance=Customer_strategy)
def test_customer_cust_name_setter(instance):
    original = instance.cust_name
    instance.cust_name = original
    assert instance.cust_name == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_numTable_setter(instance):
    original = instance.numTable
    instance.numTable = original
    assert instance.numTable == original



@given(instance=Order_strategy)
def test_order_cust_id_setter(instance):
    original = instance.cust_id
    instance.cust_id = original
    assert instance.cust_id == original



@given(instance=Order_strategy)
def test_order_foodItem_setter(instance):
    original = instance.foodItem
    instance.foodItem = original
    assert instance.foodItem == original



@given(instance=Order_strategy)
def test_order_drinksItem_setter(instance):
    original = instance.drinksItem
    instance.drinksItem = original
    assert instance.drinksItem == original



@given(instance=Order_strategy)
def test_order_cust_name_setter(instance):
    original = instance.cust_name
    instance.cust_name = original
    assert instance.cust_name == original



@given(instance=Order_strategy)
def test_order_order_Id_setter(instance):
    original = instance.order_Id
    instance.order_Id = original
    assert instance.order_Id == original

@given(instance=Report_strategy)
@settings(max_examples=50)
def test_report_instantiation(instance):
    assert isinstance(instance, Report)



@given(instance=Report_strategy)
def test_report_orders_setter(instance):
    original = instance.orders
    instance.orders = original
    assert instance.orders == original



@given(instance=Report_strategy)
def test_report_profit_setter(instance):
    original = instance.profit
    instance.profit = original
    assert instance.profit == original



@given(instance=Report_strategy)
def test_report_totalSales_setter(instance):
    original = instance.totalSales
    instance.totalSales = original
    assert instance.totalSales == original

@given(instance=Kasir_strategy)
@settings(max_examples=50)
def test_kasir_instantiation(instance):
    assert isinstance(instance, Kasir)



@given(instance=Kasir_strategy)
def test_kasir_cust_id_setter(instance):
    original = instance.cust_id
    instance.cust_id = original
    assert instance.cust_id == original



@given(instance=Kasir_strategy)
def test_kasir_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original

@given(instance=Karyawan_strategy)
@settings(max_examples=50)
def test_karyawan_instantiation(instance):
    assert isinstance(instance, Karyawan)



@given(instance=Karyawan_strategy)
def test_karyawan_staff_Id_setter(instance):
    original = instance.staff_Id
    instance.staff_Id = original
    assert instance.staff_Id == original



@given(instance=Karyawan_strategy)
def test_karyawan_contact_setter(instance):
    original = instance.contact
    instance.contact = original
    assert instance.contact == original



@given(instance=Karyawan_strategy)
def test_karyawan_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Bartender_strategy)
@settings(max_examples=50)
def test_bartender_instantiation(instance):
    assert isinstance(instance, Bartender)



@given(instance=Bartender_strategy)
def test_bartender_staff_Id_setter(instance):
    original = instance.staff_Id
    instance.staff_Id = original
    assert instance.staff_Id == original



@given(instance=Bartender_strategy)
def test_bartender_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Chef_strategy)
@settings(max_examples=50)
def test_chef_instantiation(instance):
    assert isinstance(instance, Chef)



@given(instance=Chef_strategy)
def test_chef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Chef_strategy)
def test_chef_staff_Id_setter(instance):
    original = instance.staff_Id
    instance.staff_Id = original
    assert instance.staff_Id == original

@given(instance=Manager_Owner_strategy)
@settings(max_examples=50)
def test_manager_owner_instantiation(instance):
    assert isinstance(instance, Manager_Owner)
