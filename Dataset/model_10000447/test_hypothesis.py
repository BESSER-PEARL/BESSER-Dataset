import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Food,
    app,
    cost,
    Chef,
    Items,
    Table,
    Host,
    robotWaiter,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_food_constructor_exists():
    assert callable(Food.__init__)


def test_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "food_id" in params, "Missing parameter 'food_id'"
    assert "served" in params, "Missing parameter 'served'"
    assert "price" in params, "Missing parameter 'price'"
    assert "prepared" in params, "Missing parameter 'prepared'"

def test_food_has_name():
    assert hasattr(Food, "name")
    descriptor = None
    for klass in Food.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_food_has_food_id():
    assert hasattr(Food, "food_id")
    descriptor = None
    for klass in Food.__mro__:
        if "food_id" in klass.__dict__:
            descriptor = klass.__dict__["food_id"]
            break
    assert isinstance(descriptor, property)

def test_food_has_served():
    assert hasattr(Food, "served")
    descriptor = None
    for klass in Food.__mro__:
        if "served" in klass.__dict__:
            descriptor = klass.__dict__["served"]
            break
    assert isinstance(descriptor, property)

def test_food_has_price():
    assert hasattr(Food, "price")
    descriptor = None
    for klass in Food.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_food_has_prepared():
    assert hasattr(Food, "prepared")
    descriptor = None
    for klass in Food.__mro__:
        if "prepared" in klass.__dict__:
            descriptor = klass.__dict__["prepared"]
            break
    assert isinstance(descriptor, property)



def test_app_is_not_abstract():
    assert not inspect.isabstract(app)


def test_app_constructor_exists():
    assert callable(app.__init__)


def test_app_constructor_args():
    sig = inspect.signature(app.__init__)
    params = list(sig.parameters.keys())



def test_cost_is_not_abstract():
    assert not inspect.isabstract(cost)


def test_cost_constructor_exists():
    assert callable(cost.__init__)


def test_cost_constructor_args():
    sig = inspect.signature(cost.__init__)
    params = list(sig.parameters.keys())



def test_chef_is_not_abstract():
    assert not inspect.isabstract(Chef)


def test_chef_constructor_exists():
    assert callable(Chef.__init__)


def test_chef_constructor_args():
    sig = inspect.signature(Chef.__init__)
    params = list(sig.parameters.keys())



def test_items_is_not_abstract():
    assert not inspect.isabstract(Items)


def test_items_constructor_exists():
    assert callable(Items.__init__)


def test_items_constructor_args():
    sig = inspect.signature(Items.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "tableNumber" in params, "Missing parameter 'tableNumber'"
    assert "seats" in params, "Missing parameter 'seats'"

def test_table_has_tableNumber():
    assert hasattr(Table, "tableNumber")
    descriptor = None
    for klass in Table.__mro__:
        if "tableNumber" in klass.__dict__:
            descriptor = klass.__dict__["tableNumber"]
            break
    assert isinstance(descriptor, property)

def test_table_has_seats():
    assert hasattr(Table, "seats")
    descriptor = None
    for klass in Table.__mro__:
        if "seats" in klass.__dict__:
            descriptor = klass.__dict__["seats"]
            break
    assert isinstance(descriptor, property)



def test_host_is_not_abstract():
    assert not inspect.isabstract(Host)


def test_host_constructor_exists():
    assert callable(Host.__init__)


def test_host_constructor_args():
    sig = inspect.signature(Host.__init__)
    params = list(sig.parameters.keys())
    assert "shift" in params, "Missing parameter 'shift'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_host_has_shift():
    assert hasattr(Host, "shift")
    descriptor = None
    for klass in Host.__mro__:
        if "shift" in klass.__dict__:
            descriptor = klass.__dict__["shift"]
            break
    assert isinstance(descriptor, property)

def test_host_has_ID():
    assert hasattr(Host, "ID")
    descriptor = None
    for klass in Host.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_robotwaiter_is_not_abstract():
    assert not inspect.isabstract(robotWaiter)


def test_robotwaiter_constructor_exists():
    assert callable(robotWaiter.__init__)


def test_robotwaiter_constructor_args():
    sig = inspect.signature(robotWaiter.__init__)
    params = list(sig.parameters.keys())



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "numberPeople" in params, "Missing parameter 'numberPeople'"
    assert "name" in params, "Missing parameter 'name'"

def test_customer_has_numberPeople():
    assert hasattr(Customer, "numberPeople")
    descriptor = None
    for klass in Customer.__mro__:
        if "numberPeople" in klass.__dict__:
            descriptor = klass.__dict__["numberPeople"]
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
Food_strategy = st.builds(
    Food,
    name=
        safe_text,
    food_id=
        safe_text,
    served=
        st.booleans(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    prepared=
        st.booleans()
)
app_strategy = st.builds(
    app,
)
cost_strategy = st.builds(
    cost,
)
Chef_strategy = st.builds(
    Chef,
)
Items_strategy = st.builds(
    Items,
)
Table_strategy = st.builds(
    Table,
    tableNumber=
        st.integers(),
    seats=
        st.integers()
)
Host_strategy = st.builds(
    Host,
    shift=
        safe_text,
    ID=
        safe_text
)
robotWaiter_strategy = st.builds(
    robotWaiter,
)
Customer_strategy = st.builds(
    Customer,
    numberPeople=
        st.integers(),
    name=
        safe_text
)

@given(instance=Food_strategy)
@settings(max_examples=50)
def test_food_instantiation(instance):
    assert isinstance(instance, Food)



@given(instance=Food_strategy)
def test_food_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Food_strategy)
def test_food_food_id_setter(instance):
    original = instance.food_id
    instance.food_id = original
    assert instance.food_id == original



@given(instance=Food_strategy)
def test_food_served_setter(instance):
    original = instance.served
    instance.served = original
    assert instance.served == original



@given(instance=Food_strategy)
def test_food_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Food_strategy)
def test_food_prepared_setter(instance):
    original = instance.prepared
    instance.prepared = original
    assert instance.prepared == original

@given(instance=app_strategy)
@settings(max_examples=50)
def test_app_instantiation(instance):
    assert isinstance(instance, app)

@given(instance=cost_strategy)
@settings(max_examples=50)
def test_cost_instantiation(instance):
    assert isinstance(instance, cost)

@given(instance=Chef_strategy)
@settings(max_examples=50)
def test_chef_instantiation(instance):
    assert isinstance(instance, Chef)

@given(instance=Items_strategy)
@settings(max_examples=50)
def test_items_instantiation(instance):
    assert isinstance(instance, Items)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_tableNumber_setter(instance):
    original = instance.tableNumber
    instance.tableNumber = original
    assert instance.tableNumber == original



@given(instance=Table_strategy)
def test_table_seats_setter(instance):
    original = instance.seats
    instance.seats = original
    assert instance.seats == original

@given(instance=Host_strategy)
@settings(max_examples=50)
def test_host_instantiation(instance):
    assert isinstance(instance, Host)



@given(instance=Host_strategy)
def test_host_shift_setter(instance):
    original = instance.shift
    instance.shift = original
    assert instance.shift == original



@given(instance=Host_strategy)
def test_host_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=robotWaiter_strategy)
@settings(max_examples=50)
def test_robotwaiter_instantiation(instance):
    assert isinstance(instance, robotWaiter)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_numberPeople_setter(instance):
    original = instance.numberPeople
    instance.numberPeople = original
    assert instance.numberPeople == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
