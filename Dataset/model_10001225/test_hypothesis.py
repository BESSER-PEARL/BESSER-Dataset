import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    customer,
    manger,
    Chef,
    system,
    app,
    Waiter,
    meal,
    Order,
    Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_customer_is_not_abstract():
    assert not inspect.isabstract(customer)


def test_customer_constructor_exists():
    assert callable(customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(customer.__init__)
    params = list(sig.parameters.keys())



def test_manger_is_not_abstract():
    assert not inspect.isabstract(manger)


def test_manger_constructor_exists():
    assert callable(manger.__init__)


def test_manger_constructor_args():
    sig = inspect.signature(manger.__init__)
    params = list(sig.parameters.keys())



def test_chef_is_not_abstract():
    assert not inspect.isabstract(Chef)


def test_chef_constructor_exists():
    assert callable(Chef.__init__)


def test_chef_constructor_args():
    sig = inspect.signature(Chef.__init__)
    params = list(sig.parameters.keys())



def test_system_is_not_abstract():
    assert not inspect.isabstract(system)


def test_system_constructor_exists():
    assert callable(system.__init__)


def test_system_constructor_args():
    sig = inspect.signature(system.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_system_has_name():
    assert hasattr(system, "name")
    descriptor = None
    for klass in system.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_system_has_user_id():
    assert hasattr(system, "user_id")
    descriptor = None
    for klass in system.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)



def test_app_is_not_abstract():
    assert not inspect.isabstract(app)


def test_app_constructor_exists():
    assert callable(app.__init__)


def test_app_constructor_args():
    sig = inspect.signature(app.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_app_has_name():
    assert hasattr(app, "name")
    descriptor = None
    for klass in app.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_app_has_user_id():
    assert hasattr(app, "user_id")
    descriptor = None
    for klass in app.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)



def test_waiter_is_not_abstract():
    assert not inspect.isabstract(Waiter)


def test_waiter_constructor_exists():
    assert callable(Waiter.__init__)


def test_waiter_constructor_args():
    sig = inspect.signature(Waiter.__init__)
    params = list(sig.parameters.keys())



def test_meal_is_not_abstract():
    assert not inspect.isabstract(meal)


def test_meal_constructor_exists():
    assert callable(meal.__init__)


def test_meal_constructor_args():
    sig = inspect.signature(meal.__init__)
    params = list(sig.parameters.keys())
    assert "prepared" in params, "Missing parameter 'prepared'"
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"
    assert "meal_id" in params, "Missing parameter 'meal_id'"
    assert "served" in params, "Missing parameter 'served'"

def test_meal_has_prepared():
    assert hasattr(meal, "prepared")
    descriptor = None
    for klass in meal.__mro__:
        if "prepared" in klass.__dict__:
            descriptor = klass.__dict__["prepared"]
            break
    assert isinstance(descriptor, property)

def test_meal_has_price():
    assert hasattr(meal, "price")
    descriptor = None
    for klass in meal.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_meal_has_name():
    assert hasattr(meal, "name")
    descriptor = None
    for klass in meal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_meal_has_meal_id():
    assert hasattr(meal, "meal_id")
    descriptor = None
    for klass in meal.__mro__:
        if "meal_id" in klass.__dict__:
            descriptor = klass.__dict__["meal_id"]
            break
    assert isinstance(descriptor, property)

def test_meal_has_served():
    assert hasattr(meal, "served")
    descriptor = None
    for klass in meal.__mro__:
        if "served" in klass.__dict__:
            descriptor = klass.__dict__["served"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "order_id" in params, "Missing parameter 'order_id'"
    assert "foodList" in params, "Missing parameter 'foodList'"

def test_order_has_order_id():
    assert hasattr(Order, "order_id")
    descriptor = None
    for klass in Order.__mro__:
        if "order_id" in klass.__dict__:
            descriptor = klass.__dict__["order_id"]
            break
    assert isinstance(descriptor, property)

def test_order_has_foodList():
    assert hasattr(Order, "foodList")
    descriptor = None
    for klass in Order.__mro__:
        if "foodList" in klass.__dict__:
            descriptor = klass.__dict__["foodList"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "numSeats" in params, "Missing parameter 'numSeats'"
    assert "table_id" in params, "Missing parameter 'table_id'"
    assert "avaliable" in params, "Missing parameter 'avaliable'"

def test_table_has_numSeats():
    assert hasattr(Table, "numSeats")
    descriptor = None
    for klass in Table.__mro__:
        if "numSeats" in klass.__dict__:
            descriptor = klass.__dict__["numSeats"]
            break
    assert isinstance(descriptor, property)

def test_table_has_table_id():
    assert hasattr(Table, "table_id")
    descriptor = None
    for klass in Table.__mro__:
        if "table_id" in klass.__dict__:
            descriptor = klass.__dict__["table_id"]
            break
    assert isinstance(descriptor, property)

def test_table_has_avaliable():
    assert hasattr(Table, "avaliable")
    descriptor = None
    for klass in Table.__mro__:
        if "avaliable" in klass.__dict__:
            descriptor = klass.__dict__["avaliable"]
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
customer_strategy = st.builds(
    customer,
)
manger_strategy = st.builds(
    manger,
)
Chef_strategy = st.builds(
    Chef,
)
system_strategy = st.builds(
    system,
    name=
        safe_text,
    user_id=
        safe_text
)
app_strategy = st.builds(
    app,
    name=
        safe_text,
    user_id=
        safe_text
)
Waiter_strategy = st.builds(
    Waiter,
)
meal_strategy = st.builds(
    meal,
    prepared=
        st.booleans(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    meal_id=
        safe_text,
    served=
        st.booleans()
)
Order_strategy = st.builds(
    Order,
    order_id=
        safe_text,
    foodList=
        safe_text
)
Table_strategy = st.builds(
    Table,
    numSeats=
        st.integers(),
    table_id=
        safe_text,
    avaliable=
        st.booleans()
)

@given(instance=customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, customer)

@given(instance=manger_strategy)
@settings(max_examples=50)
def test_manger_instantiation(instance):
    assert isinstance(instance, manger)

@given(instance=Chef_strategy)
@settings(max_examples=50)
def test_chef_instantiation(instance):
    assert isinstance(instance, Chef)

@given(instance=system_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, system)



@given(instance=system_strategy)
def test_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=system_strategy)
def test_system_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=app_strategy)
@settings(max_examples=50)
def test_app_instantiation(instance):
    assert isinstance(instance, app)



@given(instance=app_strategy)
def test_app_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=app_strategy)
def test_app_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=Waiter_strategy)
@settings(max_examples=50)
def test_waiter_instantiation(instance):
    assert isinstance(instance, Waiter)

@given(instance=meal_strategy)
@settings(max_examples=50)
def test_meal_instantiation(instance):
    assert isinstance(instance, meal)



@given(instance=meal_strategy)
def test_meal_prepared_setter(instance):
    original = instance.prepared
    instance.prepared = original
    assert instance.prepared == original



@given(instance=meal_strategy)
def test_meal_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=meal_strategy)
def test_meal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=meal_strategy)
def test_meal_meal_id_setter(instance):
    original = instance.meal_id
    instance.meal_id = original
    assert instance.meal_id == original



@given(instance=meal_strategy)
def test_meal_served_setter(instance):
    original = instance.served
    instance.served = original
    assert instance.served == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original



@given(instance=Order_strategy)
def test_order_foodList_setter(instance):
    original = instance.foodList
    instance.foodList = original
    assert instance.foodList == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_numSeats_setter(instance):
    original = instance.numSeats
    instance.numSeats = original
    assert instance.numSeats == original



@given(instance=Table_strategy)
def test_table_table_id_setter(instance):
    original = instance.table_id
    instance.table_id = original
    assert instance.table_id == original



@given(instance=Table_strategy)
def test_table_avaliable_setter(instance):
    original = instance.avaliable
    instance.avaliable = original
    assert instance.avaliable == original
