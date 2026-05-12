import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Craft,
    CarRentalModel_Automobile,
    CarRentalModel_Motorcycle,
    CarRentalModel_Order,
    CarRentalModel_Craft,
    CarRentalModel_Agency,
    CarRentalModel_Customer,
    CarRentalModel_CarRental,
    Customer,
    CarRentalModel_VipCustomer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_craft_is_not_abstract():
    assert not inspect.isabstract(Craft)


def test_craft_constructor_exists():
    assert callable(Craft.__init__)


def test_craft_constructor_args():
    sig = inspect.signature(Craft.__init__)
    params = list(sig.parameters.keys())



def test_carrentalmodel_automobile_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel_Automobile)


def test_carrentalmodel_automobile_constructor_exists():
    assert callable(CarRentalModel_Automobile.__init__)


def test_carrentalmodel_automobile_constructor_args():
    sig = inspect.signature(CarRentalModel_Automobile.__init__)
    params = list(sig.parameters.keys())
    assert "isCabrio" in params, "Missing parameter 'isCabrio'"

def test_carrentalmodel_automobile_has_isCabrio():
    assert hasattr(CarRentalModel_Automobile, "isCabrio")
    descriptor = None
    for klass in CarRentalModel_Automobile.__mro__:
        if "isCabrio" in klass.__dict__:
            descriptor = klass.__dict__["isCabrio"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel_motorcycle_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel_Motorcycle)


def test_carrentalmodel_motorcycle_constructor_exists():
    assert callable(CarRentalModel_Motorcycle.__init__)


def test_carrentalmodel_motorcycle_constructor_args():
    sig = inspect.signature(CarRentalModel_Motorcycle.__init__)
    params = list(sig.parameters.keys())
    assert "cm3" in params, "Missing parameter 'cm3'"

def test_carrentalmodel_motorcycle_has_cm3():
    assert hasattr(CarRentalModel_Motorcycle, "cm3")
    descriptor = None
    for klass in CarRentalModel_Motorcycle.__mro__:
        if "cm3" in klass.__dict__:
            descriptor = klass.__dict__["cm3"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel_order_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel_Order)


def test_carrentalmodel_order_constructor_exists():
    assert callable(CarRentalModel_Order.__init__)


def test_carrentalmodel_order_constructor_args():
    sig = inspect.signature(CarRentalModel_Order.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "orderDate" in params, "Missing parameter 'orderDate'"

def test_carrentalmodel_order_has_price():
    assert hasattr(CarRentalModel_Order, "price")
    descriptor = None
    for klass in CarRentalModel_Order.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel_order_has_orderDate():
    assert hasattr(CarRentalModel_Order, "orderDate")
    descriptor = None
    for klass in CarRentalModel_Order.__mro__:
        if "orderDate" in klass.__dict__:
            descriptor = klass.__dict__["orderDate"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel_craft_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel_Craft)


def test_carrentalmodel_craft_constructor_exists():
    assert callable(CarRentalModel_Craft.__init__)


def test_carrentalmodel_craft_constructor_args():
    sig = inspect.signature(CarRentalModel_Craft.__init__)
    params = list(sig.parameters.keys())
    assert "vin" in params, "Missing parameter 'vin'"
    assert "licenseNo" in params, "Missing parameter 'licenseNo'"
    assert "charge" in params, "Missing parameter 'charge'"

def test_carrentalmodel_craft_has_vin():
    assert hasattr(CarRentalModel_Craft, "vin")
    descriptor = None
    for klass in CarRentalModel_Craft.__mro__:
        if "vin" in klass.__dict__:
            descriptor = klass.__dict__["vin"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel_craft_has_licenseNo():
    assert hasattr(CarRentalModel_Craft, "licenseNo")
    descriptor = None
    for klass in CarRentalModel_Craft.__mro__:
        if "licenseNo" in klass.__dict__:
            descriptor = klass.__dict__["licenseNo"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel_craft_has_charge():
    assert hasattr(CarRentalModel_Craft, "charge")
    descriptor = None
    for klass in CarRentalModel_Craft.__mro__:
        if "charge" in klass.__dict__:
            descriptor = klass.__dict__["charge"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel_agency_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel_Agency)


def test_carrentalmodel_agency_constructor_exists():
    assert callable(CarRentalModel_Agency.__init__)


def test_carrentalmodel_agency_constructor_args():
    sig = inspect.signature(CarRentalModel_Agency.__init__)
    params = list(sig.parameters.keys())
    assert "zip" in params, "Missing parameter 'zip'"
    assert "street" in params, "Missing parameter 'street'"
    assert "place" in params, "Missing parameter 'place'"

def test_carrentalmodel_agency_has_zip():
    assert hasattr(CarRentalModel_Agency, "zip")
    descriptor = None
    for klass in CarRentalModel_Agency.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel_agency_has_street():
    assert hasattr(CarRentalModel_Agency, "street")
    descriptor = None
    for klass in CarRentalModel_Agency.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel_agency_has_place():
    assert hasattr(CarRentalModel_Agency, "place")
    descriptor = None
    for klass in CarRentalModel_Agency.__mro__:
        if "place" in klass.__dict__:
            descriptor = klass.__dict__["place"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel_customer_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel_Customer)


def test_carrentalmodel_customer_constructor_exists():
    assert callable(CarRentalModel_Customer.__init__)


def test_carrentalmodel_customer_constructor_args():
    sig = inspect.signature(CarRentalModel_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_carrentalmodel_customer_has_lastname():
    assert hasattr(CarRentalModel_Customer, "lastname")
    descriptor = None
    for klass in CarRentalModel_Customer.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel_customer_has_identifier():
    assert hasattr(CarRentalModel_Customer, "identifier")
    descriptor = None
    for klass in CarRentalModel_Customer.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel_customer_has_surname():
    assert hasattr(CarRentalModel_Customer, "surname")
    descriptor = None
    for klass in CarRentalModel_Customer.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel_carrental_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel_CarRental)


def test_carrentalmodel_carrental_constructor_exists():
    assert callable(CarRentalModel_CarRental.__init__)


def test_carrentalmodel_carrental_constructor_args():
    sig = inspect.signature(CarRentalModel_CarRental.__init__)
    params = list(sig.parameters.keys())



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())



def test_carrentalmodel_vipcustomer_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel_VipCustomer)


def test_carrentalmodel_vipcustomer_constructor_exists():
    assert callable(CarRentalModel_VipCustomer.__init__)


def test_carrentalmodel_vipcustomer_constructor_args():
    sig = inspect.signature(CarRentalModel_VipCustomer.__init__)
    params = list(sig.parameters.keys())
    assert "discount" in params, "Missing parameter 'discount'"

def test_carrentalmodel_vipcustomer_has_discount():
    assert hasattr(CarRentalModel_VipCustomer, "discount")
    descriptor = None
    for klass in CarRentalModel_VipCustomer.__mro__:
        if "discount" in klass.__dict__:
            descriptor = klass.__dict__["discount"]
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
Craft_strategy = st.builds(
    Craft,
)
CarRentalModel_Automobile_strategy = st.builds(
    CarRentalModel_Automobile,
    isCabrio=
        st.booleans()
)
CarRentalModel_Motorcycle_strategy = st.builds(
    CarRentalModel_Motorcycle,
    cm3=
        st.integers()
)
CarRentalModel_Order_strategy = st.builds(
    CarRentalModel_Order,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    orderDate=
        st.dates()
)
CarRentalModel_Craft_strategy = st.builds(
    CarRentalModel_Craft,
    vin=
        st.integers(),
    licenseNo=
        safe_text,
    charge=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CarRentalModel_Agency_strategy = st.builds(
    CarRentalModel_Agency,
    zip=
        st.integers(),
    street=
        safe_text,
    place=
        safe_text
)
CarRentalModel_Customer_strategy = st.builds(
    CarRentalModel_Customer,
    lastname=
        safe_text,
    identifier=
        safe_text,
    surname=
        safe_text
)
CarRentalModel_CarRental_strategy = st.builds(
    CarRentalModel_CarRental,
)
Customer_strategy = st.builds(
    Customer,
)
CarRentalModel_VipCustomer_strategy = st.builds(
    CarRentalModel_VipCustomer,
    discount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Craft_strategy)
@settings(max_examples=50)
def test_craft_instantiation(instance):
    assert isinstance(instance, Craft)

@given(instance=CarRentalModel_Automobile_strategy)
@settings(max_examples=50)
def test_carrentalmodel_automobile_instantiation(instance):
    assert isinstance(instance, CarRentalModel_Automobile)



@given(instance=CarRentalModel_Automobile_strategy)
def test_carrentalmodel_automobile_isCabrio_setter(instance):
    original = instance.isCabrio
    instance.isCabrio = original
    assert instance.isCabrio == original

@given(instance=CarRentalModel_Motorcycle_strategy)
@settings(max_examples=50)
def test_carrentalmodel_motorcycle_instantiation(instance):
    assert isinstance(instance, CarRentalModel_Motorcycle)



@given(instance=CarRentalModel_Motorcycle_strategy)
def test_carrentalmodel_motorcycle_cm3_setter(instance):
    original = instance.cm3
    instance.cm3 = original
    assert instance.cm3 == original

@given(instance=CarRentalModel_Order_strategy)
@settings(max_examples=50)
def test_carrentalmodel_order_instantiation(instance):
    assert isinstance(instance, CarRentalModel_Order)



@given(instance=CarRentalModel_Order_strategy)
def test_carrentalmodel_order_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=CarRentalModel_Order_strategy)
def test_carrentalmodel_order_orderDate_setter(instance):
    original = instance.orderDate
    instance.orderDate = original
    assert instance.orderDate == original

@given(instance=CarRentalModel_Craft_strategy)
@settings(max_examples=50)
def test_carrentalmodel_craft_instantiation(instance):
    assert isinstance(instance, CarRentalModel_Craft)



@given(instance=CarRentalModel_Craft_strategy)
def test_carrentalmodel_craft_vin_setter(instance):
    original = instance.vin
    instance.vin = original
    assert instance.vin == original



@given(instance=CarRentalModel_Craft_strategy)
def test_carrentalmodel_craft_licenseNo_setter(instance):
    original = instance.licenseNo
    instance.licenseNo = original
    assert instance.licenseNo == original



@given(instance=CarRentalModel_Craft_strategy)
def test_carrentalmodel_craft_charge_setter(instance):
    original = instance.charge
    instance.charge = original
    assert instance.charge == original

@given(instance=CarRentalModel_Agency_strategy)
@settings(max_examples=50)
def test_carrentalmodel_agency_instantiation(instance):
    assert isinstance(instance, CarRentalModel_Agency)



@given(instance=CarRentalModel_Agency_strategy)
def test_carrentalmodel_agency_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original



@given(instance=CarRentalModel_Agency_strategy)
def test_carrentalmodel_agency_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=CarRentalModel_Agency_strategy)
def test_carrentalmodel_agency_place_setter(instance):
    original = instance.place
    instance.place = original
    assert instance.place == original

@given(instance=CarRentalModel_Customer_strategy)
@settings(max_examples=50)
def test_carrentalmodel_customer_instantiation(instance):
    assert isinstance(instance, CarRentalModel_Customer)



@given(instance=CarRentalModel_Customer_strategy)
def test_carrentalmodel_customer_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=CarRentalModel_Customer_strategy)
def test_carrentalmodel_customer_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=CarRentalModel_Customer_strategy)
def test_carrentalmodel_customer_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=CarRentalModel_CarRental_strategy)
@settings(max_examples=50)
def test_carrentalmodel_carrental_instantiation(instance):
    assert isinstance(instance, CarRentalModel_CarRental)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=CarRentalModel_VipCustomer_strategy)
@settings(max_examples=50)
def test_carrentalmodel_vipcustomer_instantiation(instance):
    assert isinstance(instance, CarRentalModel_VipCustomer)



@given(instance=CarRentalModel_VipCustomer_strategy)
def test_carrentalmodel_vipcustomer_discount_setter(instance):
    original = instance.discount
    instance.discount = original
    assert instance.discount == original
