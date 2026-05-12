import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Customer_Data,
    Inventory,
    Customer,
    Employee,
    Manager,
    Store,
    Service,
    Product,
    Online_Portal,
    Terminal,
    Order,
    Transactions,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_customer_data_is_not_abstract():
    assert not inspect.isabstract(Customer_Data)


def test_customer_data_constructor_exists():
    assert callable(Customer_Data.__init__)


def test_customer_data_constructor_args():
    sig = inspect.signature(Customer_Data.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Contact" in params, "Missing parameter 'Contact'"

def test_customer_data_has_Name():
    assert hasattr(Customer_Data, "Name")
    descriptor = None
    for klass in Customer_Data.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_customer_data_has_Contact():
    assert hasattr(Customer_Data, "Contact")
    descriptor = None
    for klass in Customer_Data.__mro__:
        if "Contact" in klass.__dict__:
            descriptor = klass.__dict__["Contact"]
            break
    assert isinstance(descriptor, property)



def test_inventory_is_not_abstract():
    assert not inspect.isabstract(Inventory)


def test_inventory_constructor_exists():
    assert callable(Inventory.__init__)


def test_inventory_constructor_args():
    sig = inspect.signature(Inventory.__init__)
    params = list(sig.parameters.keys())
    assert "Services" in params, "Missing parameter 'Services'"
    assert "Products" in params, "Missing parameter 'Products'"

def test_inventory_has_Services():
    assert hasattr(Inventory, "Services")
    descriptor = None
    for klass in Inventory.__mro__:
        if "Services" in klass.__dict__:
            descriptor = klass.__dict__["Services"]
            break
    assert isinstance(descriptor, property)

def test_inventory_has_Products():
    assert hasattr(Inventory, "Products")
    descriptor = None
    for klass in Inventory.__mro__:
        if "Products" in klass.__dict__:
            descriptor = klass.__dict__["Products"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())



def test_store_is_not_abstract():
    assert not inspect.isabstract(Store)


def test_store_constructor_exists():
    assert callable(Store.__init__)


def test_store_constructor_args():
    sig = inspect.signature(Store.__init__)
    params = list(sig.parameters.keys())



def test_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_service_constructor_exists():
    assert callable(Service.__init__)


def test_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())
    assert "Terms" in params, "Missing parameter 'Terms'"
    assert "Info" in params, "Missing parameter 'Info'"

def test_service_has_Terms():
    assert hasattr(Service, "Terms")
    descriptor = None
    for klass in Service.__mro__:
        if "Terms" in klass.__dict__:
            descriptor = klass.__dict__["Terms"]
            break
    assert isinstance(descriptor, property)

def test_service_has_Info():
    assert hasattr(Service, "Info")
    descriptor = None
    for klass in Service.__mro__:
        if "Info" in klass.__dict__:
            descriptor = klass.__dict__["Info"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "Company" in params, "Missing parameter 'Company'"

def test_product_has_Company():
    assert hasattr(Product, "Company")
    descriptor = None
    for klass in Product.__mro__:
        if "Company" in klass.__dict__:
            descriptor = klass.__dict__["Company"]
            break
    assert isinstance(descriptor, property)



def test_online_portal_is_not_abstract():
    assert not inspect.isabstract(Online_Portal)


def test_online_portal_constructor_exists():
    assert callable(Online_Portal.__init__)


def test_online_portal_constructor_args():
    sig = inspect.signature(Online_Portal.__init__)
    params = list(sig.parameters.keys())
    assert "StoreLocation" in params, "Missing parameter 'StoreLocation'"

def test_online_portal_has_StoreLocation():
    assert hasattr(Online_Portal, "StoreLocation")
    descriptor = None
    for klass in Online_Portal.__mro__:
        if "StoreLocation" in klass.__dict__:
            descriptor = klass.__dict__["StoreLocation"]
            break
    assert isinstance(descriptor, property)



def test_terminal_is_not_abstract():
    assert not inspect.isabstract(Terminal)


def test_terminal_constructor_exists():
    assert callable(Terminal.__init__)


def test_terminal_constructor_args():
    sig = inspect.signature(Terminal.__init__)
    params = list(sig.parameters.keys())
    assert "Current_Employee" in params, "Missing parameter 'Current_Employee'"

def test_terminal_has_Current_Employee():
    assert hasattr(Terminal, "Current_Employee")
    descriptor = None
    for klass in Terminal.__mro__:
        if "Current_Employee" in klass.__dict__:
            descriptor = klass.__dict__["Current_Employee"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Service" in params, "Missing parameter 'Service'"
    assert "Product" in params, "Missing parameter 'Product'"

def test_order_has_Service():
    assert hasattr(Order, "Service")
    descriptor = None
    for klass in Order.__mro__:
        if "Service" in klass.__dict__:
            descriptor = klass.__dict__["Service"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Product():
    assert hasattr(Order, "Product")
    descriptor = None
    for klass in Order.__mro__:
        if "Product" in klass.__dict__:
            descriptor = klass.__dict__["Product"]
            break
    assert isinstance(descriptor, property)



def test_transactions_is_not_abstract():
    assert not inspect.isabstract(Transactions)


def test_transactions_constructor_exists():
    assert callable(Transactions.__init__)


def test_transactions_constructor_args():
    sig = inspect.signature(Transactions.__init__)
    params = list(sig.parameters.keys())
    assert "Order" in params, "Missing parameter 'Order'"
    assert "Customer" in params, "Missing parameter 'Customer'"

def test_transactions_has_Order():
    assert hasattr(Transactions, "Order")
    descriptor = None
    for klass in Transactions.__mro__:
        if "Order" in klass.__dict__:
            descriptor = klass.__dict__["Order"]
            break
    assert isinstance(descriptor, property)

def test_transactions_has_Customer():
    assert hasattr(Transactions, "Customer")
    descriptor = None
    for klass in Transactions.__mro__:
        if "Customer" in klass.__dict__:
            descriptor = klass.__dict__["Customer"]
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
Customer_Data_strategy = st.builds(
    Customer_Data,
    Name=
        safe_text,
    Contact=
        safe_text
)
Inventory_strategy = st.builds(
    Inventory,
    Services=
        safe_text,
    Products=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
)
Employee_strategy = st.builds(
    Employee,
)
Manager_strategy = st.builds(
    Manager,
)
Store_strategy = st.builds(
    Store,
)
Service_strategy = st.builds(
    Service,
    Terms=
        safe_text,
    Info=
        safe_text
)
Product_strategy = st.builds(
    Product,
    Company=
        safe_text
)
Online_Portal_strategy = st.builds(
    Online_Portal,
    StoreLocation=
        safe_text
)
Terminal_strategy = st.builds(
    Terminal,
    Current_Employee=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Service=
        safe_text,
    Product=
        safe_text
)
Transactions_strategy = st.builds(
    Transactions,
    Order=
        safe_text,
    Customer=
        safe_text
)

@given(instance=Customer_Data_strategy)
@settings(max_examples=50)
def test_customer_data_instantiation(instance):
    assert isinstance(instance, Customer_Data)



@given(instance=Customer_Data_strategy)
def test_customer_data_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Customer_Data_strategy)
def test_customer_data_Contact_setter(instance):
    original = instance.Contact
    instance.Contact = original
    assert instance.Contact == original

@given(instance=Inventory_strategy)
@settings(max_examples=50)
def test_inventory_instantiation(instance):
    assert isinstance(instance, Inventory)



@given(instance=Inventory_strategy)
def test_inventory_Services_setter(instance):
    original = instance.Services
    instance.Services = original
    assert instance.Services == original



@given(instance=Inventory_strategy)
def test_inventory_Products_setter(instance):
    original = instance.Products
    instance.Products = original
    assert instance.Products == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)

@given(instance=Store_strategy)
@settings(max_examples=50)
def test_store_instantiation(instance):
    assert isinstance(instance, Store)

@given(instance=Service_strategy)
@settings(max_examples=50)
def test_service_instantiation(instance):
    assert isinstance(instance, Service)



@given(instance=Service_strategy)
def test_service_Terms_setter(instance):
    original = instance.Terms
    instance.Terms = original
    assert instance.Terms == original



@given(instance=Service_strategy)
def test_service_Info_setter(instance):
    original = instance.Info
    instance.Info = original
    assert instance.Info == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_Company_setter(instance):
    original = instance.Company
    instance.Company = original
    assert instance.Company == original

@given(instance=Online_Portal_strategy)
@settings(max_examples=50)
def test_online_portal_instantiation(instance):
    assert isinstance(instance, Online_Portal)



@given(instance=Online_Portal_strategy)
def test_online_portal_StoreLocation_setter(instance):
    original = instance.StoreLocation
    instance.StoreLocation = original
    assert instance.StoreLocation == original

@given(instance=Terminal_strategy)
@settings(max_examples=50)
def test_terminal_instantiation(instance):
    assert isinstance(instance, Terminal)



@given(instance=Terminal_strategy)
def test_terminal_Current_Employee_setter(instance):
    original = instance.Current_Employee
    instance.Current_Employee = original
    assert instance.Current_Employee == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Service_setter(instance):
    original = instance.Service
    instance.Service = original
    assert instance.Service == original



@given(instance=Order_strategy)
def test_order_Product_setter(instance):
    original = instance.Product
    instance.Product = original
    assert instance.Product == original

@given(instance=Transactions_strategy)
@settings(max_examples=50)
def test_transactions_instantiation(instance):
    assert isinstance(instance, Transactions)



@given(instance=Transactions_strategy)
def test_transactions_Order_setter(instance):
    original = instance.Order
    instance.Order = original
    assert instance.Order == original



@given(instance=Transactions_strategy)
def test_transactions_Customer_setter(instance):
    original = instance.Customer
    instance.Customer = original
    assert instance.Customer == original
