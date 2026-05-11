import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Craft,
    CarRentalModel::Automobile,
    CarRentalModel::Motorcycle,
    CarRentalModel::Order,
    CarRentalModel::Craft,
    CarRentalModel::Agency,
    CarRentalModel::Customer,
    CarRentalModel::CarRental,
    Customer,
    CarRentalModel::VipCustomer,
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



def test_carrentalmodel::automobile_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel::Automobile)


def test_carrentalmodel::automobile_constructor_exists():
    assert callable(CarRentalModel::Automobile.__init__)


def test_carrentalmodel::automobile_constructor_args():
    sig = inspect.signature(CarRentalModel::Automobile.__init__)
    params = list(sig.parameters.keys())
    assert "isCabrio" in params, "Missing parameter 'isCabrio'"

def test_carrentalmodel::automobile_has_isCabrio():
    assert hasattr(CarRentalModel::Automobile, "isCabrio")
    descriptor = None
    for klass in CarRentalModel::Automobile.__mro__:
        if "isCabrio" in klass.__dict__:
            descriptor = klass.__dict__["isCabrio"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel::motorcycle_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel::Motorcycle)


def test_carrentalmodel::motorcycle_constructor_exists():
    assert callable(CarRentalModel::Motorcycle.__init__)


def test_carrentalmodel::motorcycle_constructor_args():
    sig = inspect.signature(CarRentalModel::Motorcycle.__init__)
    params = list(sig.parameters.keys())
    assert "cm3" in params, "Missing parameter 'cm3'"

def test_carrentalmodel::motorcycle_has_cm3():
    assert hasattr(CarRentalModel::Motorcycle, "cm3")
    descriptor = None
    for klass in CarRentalModel::Motorcycle.__mro__:
        if "cm3" in klass.__dict__:
            descriptor = klass.__dict__["cm3"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel::order_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel::Order)


def test_carrentalmodel::order_constructor_exists():
    assert callable(CarRentalModel::Order.__init__)


def test_carrentalmodel::order_constructor_args():
    sig = inspect.signature(CarRentalModel::Order.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "orderDate" in params, "Missing parameter 'orderDate'"

def test_carrentalmodel::order_has_price():
    assert hasattr(CarRentalModel::Order, "price")
    descriptor = None
    for klass in CarRentalModel::Order.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel::order_has_orderDate():
    assert hasattr(CarRentalModel::Order, "orderDate")
    descriptor = None
    for klass in CarRentalModel::Order.__mro__:
        if "orderDate" in klass.__dict__:
            descriptor = klass.__dict__["orderDate"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel::craft_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel::Craft)


def test_carrentalmodel::craft_constructor_exists():
    assert callable(CarRentalModel::Craft.__init__)


def test_carrentalmodel::craft_constructor_args():
    sig = inspect.signature(CarRentalModel::Craft.__init__)
    params = list(sig.parameters.keys())
    assert "vin" in params, "Missing parameter 'vin'"
    assert "charge" in params, "Missing parameter 'charge'"
    assert "licenseNo" in params, "Missing parameter 'licenseNo'"

def test_carrentalmodel::craft_has_vin():
    assert hasattr(CarRentalModel::Craft, "vin")
    descriptor = None
    for klass in CarRentalModel::Craft.__mro__:
        if "vin" in klass.__dict__:
            descriptor = klass.__dict__["vin"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel::craft_has_charge():
    assert hasattr(CarRentalModel::Craft, "charge")
    descriptor = None
    for klass in CarRentalModel::Craft.__mro__:
        if "charge" in klass.__dict__:
            descriptor = klass.__dict__["charge"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel::craft_has_licenseNo():
    assert hasattr(CarRentalModel::Craft, "licenseNo")
    descriptor = None
    for klass in CarRentalModel::Craft.__mro__:
        if "licenseNo" in klass.__dict__:
            descriptor = klass.__dict__["licenseNo"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel::agency_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel::Agency)


def test_carrentalmodel::agency_constructor_exists():
    assert callable(CarRentalModel::Agency.__init__)


def test_carrentalmodel::agency_constructor_args():
    sig = inspect.signature(CarRentalModel::Agency.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "zip" in params, "Missing parameter 'zip'"
    assert "place" in params, "Missing parameter 'place'"

def test_carrentalmodel::agency_has_street():
    assert hasattr(CarRentalModel::Agency, "street")
    descriptor = None
    for klass in CarRentalModel::Agency.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel::agency_has_zip():
    assert hasattr(CarRentalModel::Agency, "zip")
    descriptor = None
    for klass in CarRentalModel::Agency.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel::agency_has_place():
    assert hasattr(CarRentalModel::Agency, "place")
    descriptor = None
    for klass in CarRentalModel::Agency.__mro__:
        if "place" in klass.__dict__:
            descriptor = klass.__dict__["place"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel::customer_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel::Customer)


def test_carrentalmodel::customer_constructor_exists():
    assert callable(CarRentalModel::Customer.__init__)


def test_carrentalmodel::customer_constructor_args():
    sig = inspect.signature(CarRentalModel::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_carrentalmodel::customer_has_identifier():
    assert hasattr(CarRentalModel::Customer, "identifier")
    descriptor = None
    for klass in CarRentalModel::Customer.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel::customer_has_lastname():
    assert hasattr(CarRentalModel::Customer, "lastname")
    descriptor = None
    for klass in CarRentalModel::Customer.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_carrentalmodel::customer_has_surname():
    assert hasattr(CarRentalModel::Customer, "surname")
    descriptor = None
    for klass in CarRentalModel::Customer.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)



def test_carrentalmodel::carrental_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel::CarRental)


def test_carrentalmodel::carrental_constructor_exists():
    assert callable(CarRentalModel::CarRental.__init__)


def test_carrentalmodel::carrental_constructor_args():
    sig = inspect.signature(CarRentalModel::CarRental.__init__)
    params = list(sig.parameters.keys())



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())



def test_carrentalmodel::vipcustomer_is_not_abstract():
    assert not inspect.isabstract(CarRentalModel::VipCustomer)


def test_carrentalmodel::vipcustomer_constructor_exists():
    assert callable(CarRentalModel::VipCustomer.__init__)


def test_carrentalmodel::vipcustomer_constructor_args():
    sig = inspect.signature(CarRentalModel::VipCustomer.__init__)
    params = list(sig.parameters.keys())
    assert "discount" in params, "Missing parameter 'discount'"

def test_carrentalmodel::vipcustomer_has_discount():
    assert hasattr(CarRentalModel::VipCustomer, "discount")
    descriptor = None
    for klass in CarRentalModel::VipCustomer.__mro__:
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
CarRentalModel::Automobile_strategy = st.builds(
    CarRentalModel::Automobile,
    isCabrio=
        st.booleans()
)
CarRentalModel::Motorcycle_strategy = st.builds(
    CarRentalModel::Motorcycle,
    cm3=
        st.integers()
)
CarRentalModel::Order_strategy = st.builds(
    CarRentalModel::Order,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    orderDate=
        st.dates()
)
CarRentalModel::Craft_strategy = st.builds(
    CarRentalModel::Craft,
    vin=
        st.integers(),
    charge=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    licenseNo=
        safe_text
)
CarRentalModel::Agency_strategy = st.builds(
    CarRentalModel::Agency,
    street=
        safe_text,
    zip=
        st.integers(),
    place=
        safe_text
)
CarRentalModel::Customer_strategy = st.builds(
    CarRentalModel::Customer,
    identifier=
        safe_text,
    lastname=
        safe_text,
    surname=
        safe_text
)
CarRentalModel::CarRental_strategy = st.builds(
    CarRentalModel::CarRental,
)
Customer_strategy = st.builds(
    Customer,
)
CarRentalModel::VipCustomer_strategy = st.builds(
    CarRentalModel::VipCustomer,
    discount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Craft_strategy)
@settings(max_examples=50)
def test_craft_instantiation(instance):
    assert isinstance(instance, Craft)

@given(instance=CarRentalModel::Automobile_strategy)
@settings(max_examples=50)
def test_carrentalmodel::automobile_instantiation(instance):
    assert isinstance(instance, CarRentalModel::Automobile)

@given(instance=CarRentalModel::Automobile_strategy)
def test_carrentalmodel::automobile_isCabrio_type(instance):
    assert isinstance(instance.isCabrio, bool)


@given(instance=CarRentalModel::Automobile_strategy)
def test_carrentalmodel::automobile_isCabrio_setter(instance):
    original = instance.isCabrio
    instance.isCabrio = original
    assert instance.isCabrio == original

@given(instance=CarRentalModel::Motorcycle_strategy)
@settings(max_examples=50)
def test_carrentalmodel::motorcycle_instantiation(instance):
    assert isinstance(instance, CarRentalModel::Motorcycle)

@given(instance=CarRentalModel::Motorcycle_strategy)
def test_carrentalmodel::motorcycle_cm3_type(instance):
    assert isinstance(instance.cm3, int)


@given(instance=CarRentalModel::Motorcycle_strategy)
def test_carrentalmodel::motorcycle_cm3_setter(instance):
    original = instance.cm3
    instance.cm3 = original
    assert instance.cm3 == original

@given(instance=CarRentalModel::Order_strategy)
@settings(max_examples=50)
def test_carrentalmodel::order_instantiation(instance):
    assert isinstance(instance, CarRentalModel::Order)

@given(instance=CarRentalModel::Order_strategy)
def test_carrentalmodel::order_price_type(instance):
    assert isinstance(instance.price, float)


@given(instance=CarRentalModel::Order_strategy)
def test_carrentalmodel::order_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=CarRentalModel::Order_strategy)
def test_carrentalmodel::order_orderDate_type(instance):
    assert isinstance(instance.orderDate, date)


@given(instance=CarRentalModel::Order_strategy)
def test_carrentalmodel::order_orderDate_setter(instance):
    original = instance.orderDate
    instance.orderDate = original
    assert instance.orderDate == original

@given(instance=CarRentalModel::Craft_strategy)
@settings(max_examples=50)
def test_carrentalmodel::craft_instantiation(instance):
    assert isinstance(instance, CarRentalModel::Craft)

@given(instance=CarRentalModel::Craft_strategy)
def test_carrentalmodel::craft_vin_type(instance):
    assert isinstance(instance.vin, int)


@given(instance=CarRentalModel::Craft_strategy)
def test_carrentalmodel::craft_vin_setter(instance):
    original = instance.vin
    instance.vin = original
    assert instance.vin == original

@given(instance=CarRentalModel::Craft_strategy)
def test_carrentalmodel::craft_charge_type(instance):
    assert isinstance(instance.charge, float)


@given(instance=CarRentalModel::Craft_strategy)
def test_carrentalmodel::craft_charge_setter(instance):
    original = instance.charge
    instance.charge = original
    assert instance.charge == original

@given(instance=CarRentalModel::Craft_strategy)
def test_carrentalmodel::craft_licenseNo_type(instance):
    assert isinstance(instance.licenseNo, str)


@given(instance=CarRentalModel::Craft_strategy)
def test_carrentalmodel::craft_licenseNo_setter(instance):
    original = instance.licenseNo
    instance.licenseNo = original
    assert instance.licenseNo == original

@given(instance=CarRentalModel::Agency_strategy)
@settings(max_examples=50)
def test_carrentalmodel::agency_instantiation(instance):
    assert isinstance(instance, CarRentalModel::Agency)

@given(instance=CarRentalModel::Agency_strategy)
def test_carrentalmodel::agency_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=CarRentalModel::Agency_strategy)
def test_carrentalmodel::agency_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=CarRentalModel::Agency_strategy)
def test_carrentalmodel::agency_zip_type(instance):
    assert isinstance(instance.zip, int)


@given(instance=CarRentalModel::Agency_strategy)
def test_carrentalmodel::agency_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=CarRentalModel::Agency_strategy)
def test_carrentalmodel::agency_place_type(instance):
    assert isinstance(instance.place, str)


@given(instance=CarRentalModel::Agency_strategy)
def test_carrentalmodel::agency_place_setter(instance):
    original = instance.place
    instance.place = original
    assert instance.place == original

@given(instance=CarRentalModel::Customer_strategy)
@settings(max_examples=50)
def test_carrentalmodel::customer_instantiation(instance):
    assert isinstance(instance, CarRentalModel::Customer)

@given(instance=CarRentalModel::Customer_strategy)
def test_carrentalmodel::customer_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=CarRentalModel::Customer_strategy)
def test_carrentalmodel::customer_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=CarRentalModel::Customer_strategy)
def test_carrentalmodel::customer_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=CarRentalModel::Customer_strategy)
def test_carrentalmodel::customer_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=CarRentalModel::Customer_strategy)
def test_carrentalmodel::customer_surname_type(instance):
    assert isinstance(instance.surname, str)


@given(instance=CarRentalModel::Customer_strategy)
def test_carrentalmodel::customer_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=CarRentalModel::CarRental_strategy)
@settings(max_examples=50)
def test_carrentalmodel::carrental_instantiation(instance):
    assert isinstance(instance, CarRentalModel::CarRental)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=CarRentalModel::VipCustomer_strategy)
@settings(max_examples=50)
def test_carrentalmodel::vipcustomer_instantiation(instance):
    assert isinstance(instance, CarRentalModel::VipCustomer)

@given(instance=CarRentalModel::VipCustomer_strategy)
def test_carrentalmodel::vipcustomer_discount_type(instance):
    assert isinstance(instance.discount, float)


@given(instance=CarRentalModel::VipCustomer_strategy)
def test_carrentalmodel::vipcustomer_discount_setter(instance):
    original = instance.discount
    instance.discount = original
    assert instance.discount == original
