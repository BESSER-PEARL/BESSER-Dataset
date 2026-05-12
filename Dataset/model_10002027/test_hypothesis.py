import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Customer,
    Appliance,
    OrderList,
    BackOrder,
    ClothesWasher,
    Fridge,
    ClothesDryer,
    KitchenRange,
    Dishwasher,
    Furnace,
    Store,
    Order,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "customerID" in params, "Missing parameter 'customerID'"
    assert "name" in params, "Missing parameter 'name'"

def test_customer_has_phoneNumber():
    assert hasattr(Customer, "phoneNumber")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_customerID():
    assert hasattr(Customer, "customerID")
    descriptor = None
    for klass in Customer.__mro__:
        if "customerID" in klass.__dict__:
            descriptor = klass.__dict__["customerID"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_appliance_is_not_abstract():
    assert not inspect.isabstract(Appliance)


def test_appliance_constructor_exists():
    assert callable(Appliance.__init__)


def test_appliance_constructor_args():
    sig = inspect.signature(Appliance.__init__)
    params = list(sig.parameters.keys())
    assert "Model" in params, "Missing parameter 'Model'"
    assert "Brand" in params, "Missing parameter 'Brand'"
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Stock" in params, "Missing parameter 'Stock'"

def test_appliance_has_Model():
    assert hasattr(Appliance, "Model")
    descriptor = None
    for klass in Appliance.__mro__:
        if "Model" in klass.__dict__:
            descriptor = klass.__dict__["Model"]
            break
    assert isinstance(descriptor, property)

def test_appliance_has_Brand():
    assert hasattr(Appliance, "Brand")
    descriptor = None
    for klass in Appliance.__mro__:
        if "Brand" in klass.__dict__:
            descriptor = klass.__dict__["Brand"]
            break
    assert isinstance(descriptor, property)

def test_appliance_has_Price():
    assert hasattr(Appliance, "Price")
    descriptor = None
    for klass in Appliance.__mro__:
        if "Price" in klass.__dict__:
            descriptor = klass.__dict__["Price"]
            break
    assert isinstance(descriptor, property)

def test_appliance_has_Stock():
    assert hasattr(Appliance, "Stock")
    descriptor = None
    for klass in Appliance.__mro__:
        if "Stock" in klass.__dict__:
            descriptor = klass.__dict__["Stock"]
            break
    assert isinstance(descriptor, property)



def test_orderlist_is_not_abstract():
    assert not inspect.isabstract(OrderList)


def test_orderlist_constructor_exists():
    assert callable(OrderList.__init__)


def test_orderlist_constructor_args():
    sig = inspect.signature(OrderList.__init__)
    params = list(sig.parameters.keys())
    assert "orderList" in params, "Missing parameter 'orderList'"

def test_orderlist_has_orderList():
    assert hasattr(OrderList, "orderList")
    descriptor = None
    for klass in OrderList.__mro__:
        if "orderList" in klass.__dict__:
            descriptor = klass.__dict__["orderList"]
            break
    assert isinstance(descriptor, property)



def test_backorder_is_not_abstract():
    assert not inspect.isabstract(BackOrder)


def test_backorder_constructor_exists():
    assert callable(BackOrder.__init__)


def test_backorder_constructor_args():
    sig = inspect.signature(BackOrder.__init__)
    params = list(sig.parameters.keys())
    assert "backOrderList" in params, "Missing parameter 'backOrderList'"

def test_backorder_has_backOrderList():
    assert hasattr(BackOrder, "backOrderList")
    descriptor = None
    for klass in BackOrder.__mro__:
        if "backOrderList" in klass.__dict__:
            descriptor = klass.__dict__["backOrderList"]
            break
    assert isinstance(descriptor, property)



def test_clotheswasher_is_not_abstract():
    assert not inspect.isabstract(ClothesWasher)


def test_clotheswasher_constructor_exists():
    assert callable(ClothesWasher.__init__)


def test_clotheswasher_constructor_args():
    sig = inspect.signature(ClothesWasher.__init__)
    params = list(sig.parameters.keys())
    assert "repairPlan" in params, "Missing parameter 'repairPlan'"

def test_clotheswasher_has_repairPlan():
    assert hasattr(ClothesWasher, "repairPlan")
    descriptor = None
    for klass in ClothesWasher.__mro__:
        if "repairPlan" in klass.__dict__:
            descriptor = klass.__dict__["repairPlan"]
            break
    assert isinstance(descriptor, property)



def test_fridge_is_not_abstract():
    assert not inspect.isabstract(Fridge)


def test_fridge_constructor_exists():
    assert callable(Fridge.__init__)


def test_fridge_constructor_args():
    sig = inspect.signature(Fridge.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_fridge_has_capacity():
    assert hasattr(Fridge, "capacity")
    descriptor = None
    for klass in Fridge.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_clothesdryer_is_not_abstract():
    assert not inspect.isabstract(ClothesDryer)


def test_clothesdryer_constructor_exists():
    assert callable(ClothesDryer.__init__)


def test_clothesdryer_constructor_args():
    sig = inspect.signature(ClothesDryer.__init__)
    params = list(sig.parameters.keys())
    assert "repairPlan" in params, "Missing parameter 'repairPlan'"

def test_clothesdryer_has_repairPlan():
    assert hasattr(ClothesDryer, "repairPlan")
    descriptor = None
    for klass in ClothesDryer.__mro__:
        if "repairPlan" in klass.__dict__:
            descriptor = klass.__dict__["repairPlan"]
            break
    assert isinstance(descriptor, property)



def test_kitchenrange_is_not_abstract():
    assert not inspect.isabstract(KitchenRange)


def test_kitchenrange_constructor_exists():
    assert callable(KitchenRange.__init__)


def test_kitchenrange_constructor_args():
    sig = inspect.signature(KitchenRange.__init__)
    params = list(sig.parameters.keys())



def test_dishwasher_is_not_abstract():
    assert not inspect.isabstract(Dishwasher)


def test_dishwasher_constructor_exists():
    assert callable(Dishwasher.__init__)


def test_dishwasher_constructor_args():
    sig = inspect.signature(Dishwasher.__init__)
    params = list(sig.parameters.keys())



def test_furnace_is_not_abstract():
    assert not inspect.isabstract(Furnace)


def test_furnace_constructor_exists():
    assert callable(Furnace.__init__)


def test_furnace_constructor_args():
    sig = inspect.signature(Furnace.__init__)
    params = list(sig.parameters.keys())
    assert "maximumHeatOutput" in params, "Missing parameter 'maximumHeatOutput'"

def test_furnace_has_maximumHeatOutput():
    assert hasattr(Furnace, "maximumHeatOutput")
    descriptor = None
    for klass in Furnace.__mro__:
        if "maximumHeatOutput" in klass.__dict__:
            descriptor = klass.__dict__["maximumHeatOutput"]
            break
    assert isinstance(descriptor, property)



def test_store_is_not_abstract():
    assert not inspect.isabstract(Store)


def test_store_constructor_exists():
    assert callable(Store.__init__)


def test_store_constructor_args():
    sig = inspect.signature(Store.__init__)
    params = list(sig.parameters.keys())
    assert "customers" in params, "Missing parameter 'customers'"
    assert "sales" in params, "Missing parameter 'sales'"
    assert "inventory" in params, "Missing parameter 'inventory'"
    assert "orders" in params, "Missing parameter 'orders'"

def test_store_has_customers():
    assert hasattr(Store, "customers")
    descriptor = None
    for klass in Store.__mro__:
        if "customers" in klass.__dict__:
            descriptor = klass.__dict__["customers"]
            break
    assert isinstance(descriptor, property)

def test_store_has_sales():
    assert hasattr(Store, "sales")
    descriptor = None
    for klass in Store.__mro__:
        if "sales" in klass.__dict__:
            descriptor = klass.__dict__["sales"]
            break
    assert isinstance(descriptor, property)

def test_store_has_inventory():
    assert hasattr(Store, "inventory")
    descriptor = None
    for klass in Store.__mro__:
        if "inventory" in klass.__dict__:
            descriptor = klass.__dict__["inventory"]
            break
    assert isinstance(descriptor, property)

def test_store_has_orders():
    assert hasattr(Store, "orders")
    descriptor = None
    for klass in Store.__mro__:
        if "orders" in klass.__dict__:
            descriptor = klass.__dict__["orders"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "customer" in params, "Missing parameter 'customer'"
    assert "appliance" in params, "Missing parameter 'appliance'"

def test_order_has_customer():
    assert hasattr(Order, "customer")
    descriptor = None
    for klass in Order.__mro__:
        if "customer" in klass.__dict__:
            descriptor = klass.__dict__["customer"]
            break
    assert isinstance(descriptor, property)

def test_order_has_appliance():
    assert hasattr(Order, "appliance")
    descriptor = None
    for klass in Order.__mro__:
        if "appliance" in klass.__dict__:
            descriptor = klass.__dict__["appliance"]
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
Customer_strategy = st.builds(
    Customer,
    phoneNumber=
        st.integers(),
    customerID=
        st.integers(),
    name=
        safe_text
)
Appliance_strategy = st.builds(
    Appliance,
    Model=
        safe_text,
    Brand=
        safe_text,
    Price=
        safe_text,
    Stock=
        st.integers()
)
OrderList_strategy = st.builds(
    OrderList,
    orderList=
        st.none()
)
BackOrder_strategy = st.builds(
    BackOrder,
    backOrderList=
        st.none()
)
ClothesWasher_strategy = st.builds(
    ClothesWasher,
    repairPlan=
        safe_text
)
Fridge_strategy = st.builds(
    Fridge,
    capacity=
        safe_text
)
ClothesDryer_strategy = st.builds(
    ClothesDryer,
    repairPlan=
        safe_text
)
KitchenRange_strategy = st.builds(
    KitchenRange,
)
Dishwasher_strategy = st.builds(
    Dishwasher,
)
Furnace_strategy = st.builds(
    Furnace,
    maximumHeatOutput=
        safe_text
)
Store_strategy = st.builds(
    Store,
    customers=
        safe_text,
    sales=
        safe_text,
    inventory=
        safe_text,
    orders=
        safe_text
)
Order_strategy = st.builds(
    Order,
    customer=
        st.none(),
    appliance=
        st.none()
)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Customer_strategy)
def test_customer_customerID_setter(instance):
    original = instance.customerID
    instance.customerID = original
    assert instance.customerID == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Appliance_strategy)
@settings(max_examples=50)
def test_appliance_instantiation(instance):
    assert isinstance(instance, Appliance)



@given(instance=Appliance_strategy)
def test_appliance_Model_setter(instance):
    original = instance.Model
    instance.Model = original
    assert instance.Model == original



@given(instance=Appliance_strategy)
def test_appliance_Brand_setter(instance):
    original = instance.Brand
    instance.Brand = original
    assert instance.Brand == original



@given(instance=Appliance_strategy)
def test_appliance_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=Appliance_strategy)
def test_appliance_Stock_setter(instance):
    original = instance.Stock
    instance.Stock = original
    assert instance.Stock == original

@given(instance=OrderList_strategy)
@settings(max_examples=50)
def test_orderlist_instantiation(instance):
    assert isinstance(instance, OrderList)



@given(instance=OrderList_strategy)
def test_orderlist_orderList_setter(instance):
    original = instance.orderList
    instance.orderList = original
    assert instance.orderList == original

@given(instance=BackOrder_strategy)
@settings(max_examples=50)
def test_backorder_instantiation(instance):
    assert isinstance(instance, BackOrder)



@given(instance=BackOrder_strategy)
def test_backorder_backOrderList_setter(instance):
    original = instance.backOrderList
    instance.backOrderList = original
    assert instance.backOrderList == original

@given(instance=ClothesWasher_strategy)
@settings(max_examples=50)
def test_clotheswasher_instantiation(instance):
    assert isinstance(instance, ClothesWasher)



@given(instance=ClothesWasher_strategy)
def test_clotheswasher_repairPlan_setter(instance):
    original = instance.repairPlan
    instance.repairPlan = original
    assert instance.repairPlan == original

@given(instance=Fridge_strategy)
@settings(max_examples=50)
def test_fridge_instantiation(instance):
    assert isinstance(instance, Fridge)



@given(instance=Fridge_strategy)
def test_fridge_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=ClothesDryer_strategy)
@settings(max_examples=50)
def test_clothesdryer_instantiation(instance):
    assert isinstance(instance, ClothesDryer)



@given(instance=ClothesDryer_strategy)
def test_clothesdryer_repairPlan_setter(instance):
    original = instance.repairPlan
    instance.repairPlan = original
    assert instance.repairPlan == original

@given(instance=KitchenRange_strategy)
@settings(max_examples=50)
def test_kitchenrange_instantiation(instance):
    assert isinstance(instance, KitchenRange)

@given(instance=Dishwasher_strategy)
@settings(max_examples=50)
def test_dishwasher_instantiation(instance):
    assert isinstance(instance, Dishwasher)

@given(instance=Furnace_strategy)
@settings(max_examples=50)
def test_furnace_instantiation(instance):
    assert isinstance(instance, Furnace)



@given(instance=Furnace_strategy)
def test_furnace_maximumHeatOutput_setter(instance):
    original = instance.maximumHeatOutput
    instance.maximumHeatOutput = original
    assert instance.maximumHeatOutput == original

@given(instance=Store_strategy)
@settings(max_examples=50)
def test_store_instantiation(instance):
    assert isinstance(instance, Store)



@given(instance=Store_strategy)
def test_store_customers_setter(instance):
    original = instance.customers
    instance.customers = original
    assert instance.customers == original



@given(instance=Store_strategy)
def test_store_sales_setter(instance):
    original = instance.sales
    instance.sales = original
    assert instance.sales == original



@given(instance=Store_strategy)
def test_store_inventory_setter(instance):
    original = instance.inventory
    instance.inventory = original
    assert instance.inventory == original



@given(instance=Store_strategy)
def test_store_orders_setter(instance):
    original = instance.orders
    instance.orders = original
    assert instance.orders == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_customer_setter(instance):
    original = instance.customer
    instance.customer = original
    assert instance.customer == original



@given(instance=Order_strategy)
def test_order_appliance_setter(instance):
    original = instance.appliance
    instance.appliance = original
    assert instance.appliance == original
