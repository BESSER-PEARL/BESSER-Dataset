import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Manufacturer_Actor,
    Order_Cars_UseCase,
    Compute_Billables_UseCase,
    Check_Car_Stock_UseCase,
    Check_for_Parts_UseCase,
    Repair_Part_Purchase_UseCase,
    Maintenance_Team_Actor,
    Dealer_Actor,
    Send_for_Repair_UseCase,
    Purchase_Car_UseCase,
    Enquire_for_Cars_UseCase,
    Customer_Actor,
    Repair,
    RepairPart,
    Sale,
    Car,
    ConnectionInterface_Interface,
    ActiveRecord,
    Customer,
    CustomerType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_manufacturer_actor_is_not_abstract():
    assert not inspect.isabstract(Manufacturer_Actor)


def test_manufacturer_actor_constructor_exists():
    assert callable(Manufacturer_Actor.__init__)


def test_manufacturer_actor_constructor_args():
    sig = inspect.signature(Manufacturer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_order_cars_usecase_is_not_abstract():
    assert not inspect.isabstract(Order_Cars_UseCase)


def test_order_cars_usecase_constructor_exists():
    assert callable(Order_Cars_UseCase.__init__)


def test_order_cars_usecase_constructor_args():
    sig = inspect.signature(Order_Cars_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_compute_billables_usecase_is_not_abstract():
    assert not inspect.isabstract(Compute_Billables_UseCase)


def test_compute_billables_usecase_constructor_exists():
    assert callable(Compute_Billables_UseCase.__init__)


def test_compute_billables_usecase_constructor_args():
    sig = inspect.signature(Compute_Billables_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_check_car_stock_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_Car_Stock_UseCase)


def test_check_car_stock_usecase_constructor_exists():
    assert callable(Check_Car_Stock_UseCase.__init__)


def test_check_car_stock_usecase_constructor_args():
    sig = inspect.signature(Check_Car_Stock_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_check_for_parts_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_for_Parts_UseCase)


def test_check_for_parts_usecase_constructor_exists():
    assert callable(Check_for_Parts_UseCase.__init__)


def test_check_for_parts_usecase_constructor_args():
    sig = inspect.signature(Check_for_Parts_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_repair_part_purchase_usecase_is_not_abstract():
    assert not inspect.isabstract(Repair_Part_Purchase_UseCase)


def test_repair_part_purchase_usecase_constructor_exists():
    assert callable(Repair_Part_Purchase_UseCase.__init__)


def test_repair_part_purchase_usecase_constructor_args():
    sig = inspect.signature(Repair_Part_Purchase_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_maintenance_team_actor_is_not_abstract():
    assert not inspect.isabstract(Maintenance_Team_Actor)


def test_maintenance_team_actor_constructor_exists():
    assert callable(Maintenance_Team_Actor.__init__)


def test_maintenance_team_actor_constructor_args():
    sig = inspect.signature(Maintenance_Team_Actor.__init__)
    params = list(sig.parameters.keys())



def test_dealer_actor_is_not_abstract():
    assert not inspect.isabstract(Dealer_Actor)


def test_dealer_actor_constructor_exists():
    assert callable(Dealer_Actor.__init__)


def test_dealer_actor_constructor_args():
    sig = inspect.signature(Dealer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_send_for_repair_usecase_is_not_abstract():
    assert not inspect.isabstract(Send_for_Repair_UseCase)


def test_send_for_repair_usecase_constructor_exists():
    assert callable(Send_for_Repair_UseCase.__init__)


def test_send_for_repair_usecase_constructor_args():
    sig = inspect.signature(Send_for_Repair_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_purchase_car_usecase_is_not_abstract():
    assert not inspect.isabstract(Purchase_Car_UseCase)


def test_purchase_car_usecase_constructor_exists():
    assert callable(Purchase_Car_UseCase.__init__)


def test_purchase_car_usecase_constructor_args():
    sig = inspect.signature(Purchase_Car_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_enquire_for_cars_usecase_is_not_abstract():
    assert not inspect.isabstract(Enquire_for_Cars_UseCase)


def test_enquire_for_cars_usecase_constructor_exists():
    assert callable(Enquire_for_Cars_UseCase.__init__)


def test_enquire_for_cars_usecase_constructor_args():
    sig = inspect.signature(Enquire_for_Cars_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_customer_actor_is_not_abstract():
    assert not inspect.isabstract(Customer_Actor)


def test_customer_actor_constructor_exists():
    assert callable(Customer_Actor.__init__)


def test_customer_actor_constructor_args():
    sig = inspect.signature(Customer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_repair_is_not_abstract():
    assert not inspect.isabstract(Repair)


def test_repair_constructor_exists():
    assert callable(Repair.__init__)


def test_repair_constructor_args():
    sig = inspect.signature(Repair.__init__)
    params = list(sig.parameters.keys())
    assert "part" in params, "Missing parameter 'part'"
    assert "car" in params, "Missing parameter 'car'"
    assert "customer" in params, "Missing parameter 'customer'"
    assert "date" in params, "Missing parameter 'date'"

def test_repair_has_part():
    assert hasattr(Repair, "part")
    descriptor = None
    for klass in Repair.__mro__:
        if "part" in klass.__dict__:
            descriptor = klass.__dict__["part"]
            break
    assert isinstance(descriptor, property)

def test_repair_has_car():
    assert hasattr(Repair, "car")
    descriptor = None
    for klass in Repair.__mro__:
        if "car" in klass.__dict__:
            descriptor = klass.__dict__["car"]
            break
    assert isinstance(descriptor, property)

def test_repair_has_customer():
    assert hasattr(Repair, "customer")
    descriptor = None
    for klass in Repair.__mro__:
        if "customer" in klass.__dict__:
            descriptor = klass.__dict__["customer"]
            break
    assert isinstance(descriptor, property)

def test_repair_has_date():
    assert hasattr(Repair, "date")
    descriptor = None
    for klass in Repair.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_repairpart_is_not_abstract():
    assert not inspect.isabstract(RepairPart)


def test_repairpart_constructor_exists():
    assert callable(RepairPart.__init__)


def test_repairpart_constructor_args():
    sig = inspect.signature(RepairPart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "stock" in params, "Missing parameter 'stock'"
    assert "cost" in params, "Missing parameter 'cost'"

def test_repairpart_has_name():
    assert hasattr(RepairPart, "name")
    descriptor = None
    for klass in RepairPart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_repairpart_has_stock():
    assert hasattr(RepairPart, "stock")
    descriptor = None
    for klass in RepairPart.__mro__:
        if "stock" in klass.__dict__:
            descriptor = klass.__dict__["stock"]
            break
    assert isinstance(descriptor, property)

def test_repairpart_has_cost():
    assert hasattr(RepairPart, "cost")
    descriptor = None
    for klass in RepairPart.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)



def test_sale_is_not_abstract():
    assert not inspect.isabstract(Sale)


def test_sale_constructor_exists():
    assert callable(Sale.__init__)


def test_sale_constructor_args():
    sig = inspect.signature(Sale.__init__)
    params = list(sig.parameters.keys())
    assert "customer" in params, "Missing parameter 'customer'"
    assert "date" in params, "Missing parameter 'date'"
    assert "billable" in params, "Missing parameter 'billable'"
    assert "car" in params, "Missing parameter 'car'"

def test_sale_has_customer():
    assert hasattr(Sale, "customer")
    descriptor = None
    for klass in Sale.__mro__:
        if "customer" in klass.__dict__:
            descriptor = klass.__dict__["customer"]
            break
    assert isinstance(descriptor, property)

def test_sale_has_date():
    assert hasattr(Sale, "date")
    descriptor = None
    for klass in Sale.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_sale_has_billable():
    assert hasattr(Sale, "billable")
    descriptor = None
    for klass in Sale.__mro__:
        if "billable" in klass.__dict__:
            descriptor = klass.__dict__["billable"]
            break
    assert isinstance(descriptor, property)

def test_sale_has_car():
    assert hasattr(Sale, "car")
    descriptor = None
    for klass in Sale.__mro__:
        if "car" in klass.__dict__:
            descriptor = klass.__dict__["car"]
            break
    assert isinstance(descriptor, property)



def test_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_car_constructor_exists():
    assert callable(Car.__init__)


def test_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())
    assert "cost" in params, "Missing parameter 'cost'"
    assert "stock" in params, "Missing parameter 'stock'"
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"
    assert "name" in params, "Missing parameter 'name'"

def test_car_has_cost():
    assert hasattr(Car, "cost")
    descriptor = None
    for klass in Car.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_car_has_stock():
    assert hasattr(Car, "stock")
    descriptor = None
    for klass in Car.__mro__:
        if "stock" in klass.__dict__:
            descriptor = klass.__dict__["stock"]
            break
    assert isinstance(descriptor, property)

def test_car_has_manufacturer():
    assert hasattr(Car, "manufacturer")
    descriptor = None
    for klass in Car.__mro__:
        if "manufacturer" in klass.__dict__:
            descriptor = klass.__dict__["manufacturer"]
            break
    assert isinstance(descriptor, property)

def test_car_has_name():
    assert hasattr(Car, "name")
    descriptor = None
    for klass in Car.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_connectioninterface_interface_is_not_abstract():
    assert not inspect.isabstract(ConnectionInterface_Interface)


def test_connectioninterface_interface_constructor_exists():
    assert callable(ConnectionInterface_Interface.__init__)


def test_connectioninterface_interface_constructor_args():
    sig = inspect.signature(ConnectionInterface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_activerecord_is_not_abstract():
    assert not inspect.isabstract(ActiveRecord)


def test_activerecord_constructor_exists():
    assert callable(ActiveRecord.__init__)


def test_activerecord_constructor_args():
    sig = inspect.signature(ActiveRecord.__init__)
    params = list(sig.parameters.keys())
    assert "connection" in params, "Missing parameter 'connection'"
    assert "id" in params, "Missing parameter 'id'"

def test_activerecord_has_connection():
    assert hasattr(ActiveRecord, "connection")
    descriptor = None
    for klass in ActiveRecord.__mro__:
        if "connection" in klass.__dict__:
            descriptor = klass.__dict__["connection"]
            break
    assert isinstance(descriptor, property)

def test_activerecord_has_id():
    assert hasattr(ActiveRecord, "id")
    descriptor = None
    for klass in ActiveRecord.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_customer_has_address():
    assert hasattr(Customer, "address")
    descriptor = None
    for klass in Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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

def test_customer_has_type():
    assert hasattr(Customer, "type")
    descriptor = None
    for klass in Customer.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_customertype_exists():
    # Check that the Enumeration exists
    assert CustomerType is not None

def test_customertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CustomerType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CustomerType"


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
Manufacturer_Actor_strategy = st.builds(
    Manufacturer_Actor,
)
Order_Cars_UseCase_strategy = st.builds(
    Order_Cars_UseCase,
)
Compute_Billables_UseCase_strategy = st.builds(
    Compute_Billables_UseCase,
)
Check_Car_Stock_UseCase_strategy = st.builds(
    Check_Car_Stock_UseCase,
)
Check_for_Parts_UseCase_strategy = st.builds(
    Check_for_Parts_UseCase,
)
Repair_Part_Purchase_UseCase_strategy = st.builds(
    Repair_Part_Purchase_UseCase,
)
Maintenance_Team_Actor_strategy = st.builds(
    Maintenance_Team_Actor,
)
Dealer_Actor_strategy = st.builds(
    Dealer_Actor,
)
Send_for_Repair_UseCase_strategy = st.builds(
    Send_for_Repair_UseCase,
)
Purchase_Car_UseCase_strategy = st.builds(
    Purchase_Car_UseCase,
)
Enquire_for_Cars_UseCase_strategy = st.builds(
    Enquire_for_Cars_UseCase,
)
Customer_Actor_strategy = st.builds(
    Customer_Actor,
)
Repair_strategy = st.builds(
    Repair,
    part=
        st.none(),
    car=
        st.none(),
    customer=
        st.none(),
    date=
        st.dates()
)
RepairPart_strategy = st.builds(
    RepairPart,
    name=
        safe_text,
    stock=
        st.integers(),
    cost=
        safe_text
)
Sale_strategy = st.builds(
    Sale,
    customer=
        st.none(),
    date=
        st.dates(),
    billable=
        safe_text,
    car=
        st.none()
)
Car_strategy = st.builds(
    Car,
    cost=
        safe_text,
    stock=
        st.integers(),
    manufacturer=
        safe_text,
    name=
        safe_text
)
ConnectionInterface_Interface_strategy = st.builds(
    ConnectionInterface_Interface,
)
ActiveRecord_strategy = st.builds(
    ActiveRecord,
    connection=
        st.none(),
    id=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    address=
        safe_text,
    name=
        safe_text,
    type=
        st.none()
)

@given(instance=Manufacturer_Actor_strategy)
@settings(max_examples=50)
def test_manufacturer_actor_instantiation(instance):
    assert isinstance(instance, Manufacturer_Actor)

@given(instance=Order_Cars_UseCase_strategy)
@settings(max_examples=50)
def test_order_cars_usecase_instantiation(instance):
    assert isinstance(instance, Order_Cars_UseCase)

@given(instance=Compute_Billables_UseCase_strategy)
@settings(max_examples=50)
def test_compute_billables_usecase_instantiation(instance):
    assert isinstance(instance, Compute_Billables_UseCase)

@given(instance=Check_Car_Stock_UseCase_strategy)
@settings(max_examples=50)
def test_check_car_stock_usecase_instantiation(instance):
    assert isinstance(instance, Check_Car_Stock_UseCase)

@given(instance=Check_for_Parts_UseCase_strategy)
@settings(max_examples=50)
def test_check_for_parts_usecase_instantiation(instance):
    assert isinstance(instance, Check_for_Parts_UseCase)

@given(instance=Repair_Part_Purchase_UseCase_strategy)
@settings(max_examples=50)
def test_repair_part_purchase_usecase_instantiation(instance):
    assert isinstance(instance, Repair_Part_Purchase_UseCase)

@given(instance=Maintenance_Team_Actor_strategy)
@settings(max_examples=50)
def test_maintenance_team_actor_instantiation(instance):
    assert isinstance(instance, Maintenance_Team_Actor)

@given(instance=Dealer_Actor_strategy)
@settings(max_examples=50)
def test_dealer_actor_instantiation(instance):
    assert isinstance(instance, Dealer_Actor)

@given(instance=Send_for_Repair_UseCase_strategy)
@settings(max_examples=50)
def test_send_for_repair_usecase_instantiation(instance):
    assert isinstance(instance, Send_for_Repair_UseCase)

@given(instance=Purchase_Car_UseCase_strategy)
@settings(max_examples=50)
def test_purchase_car_usecase_instantiation(instance):
    assert isinstance(instance, Purchase_Car_UseCase)

@given(instance=Enquire_for_Cars_UseCase_strategy)
@settings(max_examples=50)
def test_enquire_for_cars_usecase_instantiation(instance):
    assert isinstance(instance, Enquire_for_Cars_UseCase)

@given(instance=Customer_Actor_strategy)
@settings(max_examples=50)
def test_customer_actor_instantiation(instance):
    assert isinstance(instance, Customer_Actor)

@given(instance=Repair_strategy)
@settings(max_examples=50)
def test_repair_instantiation(instance):
    assert isinstance(instance, Repair)



@given(instance=Repair_strategy)
def test_repair_part_setter(instance):
    original = instance.part
    instance.part = original
    assert instance.part == original



@given(instance=Repair_strategy)
def test_repair_car_setter(instance):
    original = instance.car
    instance.car = original
    assert instance.car == original



@given(instance=Repair_strategy)
def test_repair_customer_setter(instance):
    original = instance.customer
    instance.customer = original
    assert instance.customer == original



@given(instance=Repair_strategy)
def test_repair_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=RepairPart_strategy)
@settings(max_examples=50)
def test_repairpart_instantiation(instance):
    assert isinstance(instance, RepairPart)



@given(instance=RepairPart_strategy)
def test_repairpart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=RepairPart_strategy)
def test_repairpart_stock_setter(instance):
    original = instance.stock
    instance.stock = original
    assert instance.stock == original



@given(instance=RepairPart_strategy)
def test_repairpart_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=Sale_strategy)
@settings(max_examples=50)
def test_sale_instantiation(instance):
    assert isinstance(instance, Sale)



@given(instance=Sale_strategy)
def test_sale_customer_setter(instance):
    original = instance.customer
    instance.customer = original
    assert instance.customer == original



@given(instance=Sale_strategy)
def test_sale_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Sale_strategy)
def test_sale_billable_setter(instance):
    original = instance.billable
    instance.billable = original
    assert instance.billable == original



@given(instance=Sale_strategy)
def test_sale_car_setter(instance):
    original = instance.car
    instance.car = original
    assert instance.car == original

@given(instance=Car_strategy)
@settings(max_examples=50)
def test_car_instantiation(instance):
    assert isinstance(instance, Car)



@given(instance=Car_strategy)
def test_car_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=Car_strategy)
def test_car_stock_setter(instance):
    original = instance.stock
    instance.stock = original
    assert instance.stock == original



@given(instance=Car_strategy)
def test_car_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original



@given(instance=Car_strategy)
def test_car_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ConnectionInterface_Interface_strategy)
@settings(max_examples=50)
def test_connectioninterface_interface_instantiation(instance):
    assert isinstance(instance, ConnectionInterface_Interface)

@given(instance=ActiveRecord_strategy)
@settings(max_examples=50)
def test_activerecord_instantiation(instance):
    assert isinstance(instance, ActiveRecord)



@given(instance=ActiveRecord_strategy)
def test_activerecord_connection_setter(instance):
    original = instance.connection
    instance.connection = original
    assert instance.connection == original



@given(instance=ActiveRecord_strategy)
def test_activerecord_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_customer_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
