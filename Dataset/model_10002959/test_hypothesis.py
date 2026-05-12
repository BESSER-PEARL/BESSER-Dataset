import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MealDeal,
    Base,
    Address,
    Sides,
    Toppings,
    Pizza,
    GPSLocation,
    Order,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mealdeal_is_not_abstract():
    assert not inspect.isabstract(MealDeal)


def test_mealdeal_constructor_exists():
    assert callable(MealDeal.__init__)


def test_mealdeal_constructor_args():
    sig = inspect.signature(MealDeal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "price" in params, "Missing parameter 'price'"
    assert "isVegetarian" in params, "Missing parameter 'isVegetarian'"

def test_mealdeal_has_name():
    assert hasattr(MealDeal, "name")
    descriptor = None
    for klass in MealDeal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mealdeal_has_description():
    assert hasattr(MealDeal, "description")
    descriptor = None
    for klass in MealDeal.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mealdeal_has_price():
    assert hasattr(MealDeal, "price")
    descriptor = None
    for klass in MealDeal.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_mealdeal_has_isVegetarian():
    assert hasattr(MealDeal, "isVegetarian")
    descriptor = None
    for klass in MealDeal.__mro__:
        if "isVegetarian" in klass.__dict__:
            descriptor = klass.__dict__["isVegetarian"]
            break
    assert isinstance(descriptor, property)



def test_base_is_not_abstract():
    assert not inspect.isabstract(Base)


def test_base_constructor_exists():
    assert callable(Base.__init__)


def test_base_constructor_args():
    sig = inspect.signature(Base.__init__)
    params = list(sig.parameters.keys())
    assert "isVegetarian" in params, "Missing parameter 'isVegetarian'"
    assert "name" in params, "Missing parameter 'name'"

def test_base_has_isVegetarian():
    assert hasattr(Base, "isVegetarian")
    descriptor = None
    for klass in Base.__mro__:
        if "isVegetarian" in klass.__dict__:
            descriptor = klass.__dict__["isVegetarian"]
            break
    assert isinstance(descriptor, property)

def test_base_has_name():
    assert hasattr(Base, "name")
    descriptor = None
    for klass in Base.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())
    assert "Line1" in params, "Missing parameter 'Line1'"
    assert "City" in params, "Missing parameter 'City'"
    assert "Line_2" in params, "Missing parameter 'Line_2'"
    assert "County" in params, "Missing parameter 'County'"

def test_address_has_Line1():
    assert hasattr(Address, "Line1")
    descriptor = None
    for klass in Address.__mro__:
        if "Line1" in klass.__dict__:
            descriptor = klass.__dict__["Line1"]
            break
    assert isinstance(descriptor, property)

def test_address_has_City():
    assert hasattr(Address, "City")
    descriptor = None
    for klass in Address.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)

def test_address_has_Line_2():
    assert hasattr(Address, "Line_2")
    descriptor = None
    for klass in Address.__mro__:
        if "Line_2" in klass.__dict__:
            descriptor = klass.__dict__["Line_2"]
            break
    assert isinstance(descriptor, property)

def test_address_has_County():
    assert hasattr(Address, "County")
    descriptor = None
    for klass in Address.__mro__:
        if "County" in klass.__dict__:
            descriptor = klass.__dict__["County"]
            break
    assert isinstance(descriptor, property)



def test_sides_is_not_abstract():
    assert not inspect.isabstract(Sides)


def test_sides_constructor_exists():
    assert callable(Sides.__init__)


def test_sides_constructor_args():
    sig = inspect.signature(Sides.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isVegetarian" in params, "Missing parameter 'isVegetarian'"
    assert "price" in params, "Missing parameter 'price'"

def test_sides_has_name():
    assert hasattr(Sides, "name")
    descriptor = None
    for klass in Sides.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sides_has_isVegetarian():
    assert hasattr(Sides, "isVegetarian")
    descriptor = None
    for klass in Sides.__mro__:
        if "isVegetarian" in klass.__dict__:
            descriptor = klass.__dict__["isVegetarian"]
            break
    assert isinstance(descriptor, property)

def test_sides_has_price():
    assert hasattr(Sides, "price")
    descriptor = None
    for klass in Sides.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_toppings_is_not_abstract():
    assert not inspect.isabstract(Toppings)


def test_toppings_constructor_exists():
    assert callable(Toppings.__init__)


def test_toppings_constructor_args():
    sig = inspect.signature(Toppings.__init__)
    params = list(sig.parameters.keys())
    assert "isVegetarian" in params, "Missing parameter 'isVegetarian'"
    assert "name" in params, "Missing parameter 'name'"

def test_toppings_has_isVegetarian():
    assert hasattr(Toppings, "isVegetarian")
    descriptor = None
    for klass in Toppings.__mro__:
        if "isVegetarian" in klass.__dict__:
            descriptor = klass.__dict__["isVegetarian"]
            break
    assert isinstance(descriptor, property)

def test_toppings_has_name():
    assert hasattr(Toppings, "name")
    descriptor = None
    for klass in Toppings.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pizza_is_not_abstract():
    assert not inspect.isabstract(Pizza)


def test_pizza_constructor_exists():
    assert callable(Pizza.__init__)


def test_pizza_constructor_args():
    sig = inspect.signature(Pizza.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "isVegetarian" in params, "Missing parameter 'isVegetarian'"

def test_pizza_has_price():
    assert hasattr(Pizza, "price")
    descriptor = None
    for klass in Pizza.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_pizza_has_isVegetarian():
    assert hasattr(Pizza, "isVegetarian")
    descriptor = None
    for klass in Pizza.__mro__:
        if "isVegetarian" in klass.__dict__:
            descriptor = klass.__dict__["isVegetarian"]
            break
    assert isinstance(descriptor, property)



def test_gpslocation_is_not_abstract():
    assert not inspect.isabstract(GPSLocation)


def test_gpslocation_constructor_exists():
    assert callable(GPSLocation.__init__)


def test_gpslocation_constructor_args():
    sig = inspect.signature(GPSLocation.__init__)
    params = list(sig.parameters.keys())
    assert "GPS" in params, "Missing parameter 'GPS'"

def test_gpslocation_has_GPS():
    assert hasattr(GPSLocation, "GPS")
    descriptor = None
    for klass in GPSLocation.__mro__:
        if "GPS" in klass.__dict__:
            descriptor = klass.__dict__["GPS"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "orderNotes" in params, "Missing parameter 'orderNotes'"
    assert "orderID" in params, "Missing parameter 'orderID'"
    assert "creditCardDetails" in params, "Missing parameter 'creditCardDetails'"
    assert "time" in params, "Missing parameter 'time'"

def test_order_has_date():
    assert hasattr(Order, "date")
    descriptor = None
    for klass in Order.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_order_has_orderNotes():
    assert hasattr(Order, "orderNotes")
    descriptor = None
    for klass in Order.__mro__:
        if "orderNotes" in klass.__dict__:
            descriptor = klass.__dict__["orderNotes"]
            break
    assert isinstance(descriptor, property)

def test_order_has_orderID():
    assert hasattr(Order, "orderID")
    descriptor = None
    for klass in Order.__mro__:
        if "orderID" in klass.__dict__:
            descriptor = klass.__dict__["orderID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_creditCardDetails():
    assert hasattr(Order, "creditCardDetails")
    descriptor = None
    for klass in Order.__mro__:
        if "creditCardDetails" in klass.__dict__:
            descriptor = klass.__dict__["creditCardDetails"]
            break
    assert isinstance(descriptor, property)

def test_order_has_time():
    assert hasattr(Order, "time")
    descriptor = None
    for klass in Order.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "customerID" in params, "Missing parameter 'customerID'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "customerName" in params, "Missing parameter 'customerName'"

def test_customer_has_customerID():
    assert hasattr(Customer, "customerID")
    descriptor = None
    for klass in Customer.__mro__:
        if "customerID" in klass.__dict__:
            descriptor = klass.__dict__["customerID"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_phoneNumber():
    assert hasattr(Customer, "phoneNumber")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_customerName():
    assert hasattr(Customer, "customerName")
    descriptor = None
    for klass in Customer.__mro__:
        if "customerName" in klass.__dict__:
            descriptor = klass.__dict__["customerName"]
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
MealDeal_strategy = st.builds(
    MealDeal,
    name=
        safe_text,
    description=
        safe_text,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isVegetarian=
        st.booleans()
)
Base_strategy = st.builds(
    Base,
    isVegetarian=
        st.booleans(),
    name=
        safe_text
)
Address_strategy = st.builds(
    Address,
    Line1=
        safe_text,
    City=
        safe_text,
    Line_2=
        safe_text,
    County=
        safe_text
)
Sides_strategy = st.builds(
    Sides,
    name=
        safe_text,
    isVegetarian=
        st.booleans(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Toppings_strategy = st.builds(
    Toppings,
    isVegetarian=
        st.booleans(),
    name=
        safe_text
)
Pizza_strategy = st.builds(
    Pizza,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isVegetarian=
        st.booleans()
)
GPSLocation_strategy = st.builds(
    GPSLocation,
    GPS=
        safe_text
)
Order_strategy = st.builds(
    Order,
    date=
        safe_text,
    orderNotes=
        safe_text,
    orderID=
        st.integers(),
    creditCardDetails=
        safe_text,
    time=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    customerID=
        st.integers(),
    phoneNumber=
        st.integers(),
    customerName=
        safe_text
)

@given(instance=MealDeal_strategy)
@settings(max_examples=50)
def test_mealdeal_instantiation(instance):
    assert isinstance(instance, MealDeal)



@given(instance=MealDeal_strategy)
def test_mealdeal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MealDeal_strategy)
def test_mealdeal_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=MealDeal_strategy)
def test_mealdeal_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=MealDeal_strategy)
def test_mealdeal_isVegetarian_setter(instance):
    original = instance.isVegetarian
    instance.isVegetarian = original
    assert instance.isVegetarian == original

@given(instance=Base_strategy)
@settings(max_examples=50)
def test_base_instantiation(instance):
    assert isinstance(instance, Base)



@given(instance=Base_strategy)
def test_base_isVegetarian_setter(instance):
    original = instance.isVegetarian
    instance.isVegetarian = original
    assert instance.isVegetarian == original



@given(instance=Base_strategy)
def test_base_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)



@given(instance=Address_strategy)
def test_address_Line1_setter(instance):
    original = instance.Line1
    instance.Line1 = original
    assert instance.Line1 == original



@given(instance=Address_strategy)
def test_address_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=Address_strategy)
def test_address_Line_2_setter(instance):
    original = instance.Line_2
    instance.Line_2 = original
    assert instance.Line_2 == original



@given(instance=Address_strategy)
def test_address_County_setter(instance):
    original = instance.County
    instance.County = original
    assert instance.County == original

@given(instance=Sides_strategy)
@settings(max_examples=50)
def test_sides_instantiation(instance):
    assert isinstance(instance, Sides)



@given(instance=Sides_strategy)
def test_sides_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Sides_strategy)
def test_sides_isVegetarian_setter(instance):
    original = instance.isVegetarian
    instance.isVegetarian = original
    assert instance.isVegetarian == original



@given(instance=Sides_strategy)
def test_sides_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Toppings_strategy)
@settings(max_examples=50)
def test_toppings_instantiation(instance):
    assert isinstance(instance, Toppings)



@given(instance=Toppings_strategy)
def test_toppings_isVegetarian_setter(instance):
    original = instance.isVegetarian
    instance.isVegetarian = original
    assert instance.isVegetarian == original



@given(instance=Toppings_strategy)
def test_toppings_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Pizza_strategy)
@settings(max_examples=50)
def test_pizza_instantiation(instance):
    assert isinstance(instance, Pizza)



@given(instance=Pizza_strategy)
def test_pizza_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Pizza_strategy)
def test_pizza_isVegetarian_setter(instance):
    original = instance.isVegetarian
    instance.isVegetarian = original
    assert instance.isVegetarian == original

@given(instance=GPSLocation_strategy)
@settings(max_examples=50)
def test_gpslocation_instantiation(instance):
    assert isinstance(instance, GPSLocation)



@given(instance=GPSLocation_strategy)
def test_gpslocation_GPS_setter(instance):
    original = instance.GPS
    instance.GPS = original
    assert instance.GPS == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Order_strategy)
def test_order_orderNotes_setter(instance):
    original = instance.orderNotes
    instance.orderNotes = original
    assert instance.orderNotes == original



@given(instance=Order_strategy)
def test_order_orderID_setter(instance):
    original = instance.orderID
    instance.orderID = original
    assert instance.orderID == original



@given(instance=Order_strategy)
def test_order_creditCardDetails_setter(instance):
    original = instance.creditCardDetails
    instance.creditCardDetails = original
    assert instance.creditCardDetails == original



@given(instance=Order_strategy)
def test_order_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_customerID_setter(instance):
    original = instance.customerID
    instance.customerID = original
    assert instance.customerID == original



@given(instance=Customer_strategy)
def test_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Customer_strategy)
def test_customer_customerName_setter(instance):
    original = instance.customerName
    instance.customerName = original
    assert instance.customerName == original
