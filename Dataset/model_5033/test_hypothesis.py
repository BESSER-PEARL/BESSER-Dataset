import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    customers_CustomersDB,
    customers_Address,
    customers_CreditCard,
    Address,
    customers_CanadaAddress,
    customers_USAddress,
    customers_Customer,
    CanadaProvinces,
    USStates,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_customers_customersdb_is_not_abstract():
    assert not inspect.isabstract(customers_CustomersDB)


def test_customers_customersdb_constructor_exists():
    assert callable(customers_CustomersDB.__init__)


def test_customers_customersdb_constructor_args():
    sig = inspect.signature(customers_CustomersDB.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_customers_customersdb_has_comment():
    assert hasattr(customers_CustomersDB, "comment")
    descriptor = None
    for klass in customers_CustomersDB.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_customers_address_is_not_abstract():
    assert not inspect.isabstract(customers_Address)


def test_customers_address_constructor_exists():
    assert callable(customers_Address.__init__)


def test_customers_address_constructor_args():
    sig = inspect.signature(customers_Address.__init__)
    params = list(sig.parameters.keys())
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "town" in params, "Missing parameter 'town'"
    assert "street" in params, "Missing parameter 'street'"

def test_customers_address_has_zipCode():
    assert hasattr(customers_Address, "zipCode")
    descriptor = None
    for klass in customers_Address.__mro__:
        if "zipCode" in klass.__dict__:
            descriptor = klass.__dict__["zipCode"]
            break
    assert isinstance(descriptor, property)

def test_customers_address_has_town():
    assert hasattr(customers_Address, "town")
    descriptor = None
    for klass in customers_Address.__mro__:
        if "town" in klass.__dict__:
            descriptor = klass.__dict__["town"]
            break
    assert isinstance(descriptor, property)

def test_customers_address_has_street():
    assert hasattr(customers_Address, "street")
    descriptor = None
    for klass in customers_Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)



def test_customers_creditcard_is_not_abstract():
    assert not inspect.isabstract(customers_CreditCard)


def test_customers_creditcard_constructor_exists():
    assert callable(customers_CreditCard.__init__)


def test_customers_creditcard_constructor_args():
    sig = inspect.signature(customers_CreditCard.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "expiresDate" in params, "Missing parameter 'expiresDate'"
    assert "ccNumber" in params, "Missing parameter 'ccNumber'"

def test_customers_creditcard_has_type():
    assert hasattr(customers_CreditCard, "type")
    descriptor = None
    for klass in customers_CreditCard.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_customers_creditcard_has_expiresDate():
    assert hasattr(customers_CreditCard, "expiresDate")
    descriptor = None
    for klass in customers_CreditCard.__mro__:
        if "expiresDate" in klass.__dict__:
            descriptor = klass.__dict__["expiresDate"]
            break
    assert isinstance(descriptor, property)

def test_customers_creditcard_has_ccNumber():
    assert hasattr(customers_CreditCard, "ccNumber")
    descriptor = None
    for klass in customers_CreditCard.__mro__:
        if "ccNumber" in klass.__dict__:
            descriptor = klass.__dict__["ccNumber"]
            break
    assert isinstance(descriptor, property)



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_customers_canadaaddress_is_not_abstract():
    assert not inspect.isabstract(customers_CanadaAddress)


def test_customers_canadaaddress_constructor_exists():
    assert callable(customers_CanadaAddress.__init__)


def test_customers_canadaaddress_constructor_args():
    sig = inspect.signature(customers_CanadaAddress.__init__)
    params = list(sig.parameters.keys())
    assert "province" in params, "Missing parameter 'province'"

def test_customers_canadaaddress_has_province():
    assert hasattr(customers_CanadaAddress, "province")
    descriptor = None
    for klass in customers_CanadaAddress.__mro__:
        if "province" in klass.__dict__:
            descriptor = klass.__dict__["province"]
            break
    assert isinstance(descriptor, property)



def test_customers_usaddress_is_not_abstract():
    assert not inspect.isabstract(customers_USAddress)


def test_customers_usaddress_constructor_exists():
    assert callable(customers_USAddress.__init__)


def test_customers_usaddress_constructor_args():
    sig = inspect.signature(customers_USAddress.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_customers_usaddress_has_state():
    assert hasattr(customers_USAddress, "state")
    descriptor = None
    for klass in customers_USAddress.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_customers_customer_is_not_abstract():
    assert not inspect.isabstract(customers_Customer)


def test_customers_customer_constructor_exists():
    assert callable(customers_Customer.__init__)


def test_customers_customer_constructor_args():
    sig = inspect.signature(customers_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_customers_customer_has_firstName():
    assert hasattr(customers_Customer, "firstName")
    descriptor = None
    for klass in customers_Customer.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_customers_customer_has_lastName():
    assert hasattr(customers_Customer, "lastName")
    descriptor = None
    for klass in customers_Customer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_customers_customer_has_dateOfBirth():
    assert hasattr(customers_Customer, "dateOfBirth")
    descriptor = None
    for klass in customers_Customer.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_customers_customer_has_comment():
    assert hasattr(customers_Customer, "comment")
    descriptor = None
    for klass in customers_Customer.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_canadaprovinces_exists():
    # Check that the Enumeration exists
    assert CanadaProvinces is not None

def test_canadaprovinces_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CanadaProvinces]
    expected_literals = [
        "NB",
        "BC",
        "AB",
        "NT",
        "NL",
        "MB",
        "UNKNOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CanadaProvinces"

def test_usstates_exists():
    # Check that the Enumeration exists
    assert USStates is not None

def test_usstates_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in USStates]
    expected_literals = [
        "UNKNOWN",
        "CO",
        "AL",
        "AZ",
        "CA",
        "AS",
        "AR",
        "AK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in USStates"


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
customers_CustomersDB_strategy = st.builds(
    customers_CustomersDB,
    comment=
        safe_text
)
customers_Address_strategy = st.builds(
    customers_Address,
    zipCode=
        safe_text,
    town=
        safe_text,
    street=
        safe_text
)
customers_CreditCard_strategy = st.builds(
    customers_CreditCard,
    type=
        safe_text,
    expiresDate=
        st.dates(),
    ccNumber=
        safe_text
)
Address_strategy = st.builds(
    Address,
)
customers_CanadaAddress_strategy = st.builds(
    customers_CanadaAddress,
    province=
        safe_text
)
customers_USAddress_strategy = st.builds(
    customers_USAddress,
    state=
        safe_text
)
customers_Customer_strategy = st.builds(
    customers_Customer,
    firstName=
        safe_text,
    lastName=
        safe_text,
    dateOfBirth=
        st.dates(),
    comment=
        safe_text
)

@given(instance=customers_CustomersDB_strategy)
@settings(max_examples=50)
def test_customers_customersdb_instantiation(instance):
    assert isinstance(instance, customers_CustomersDB)



@given(instance=customers_CustomersDB_strategy)
def test_customers_customersdb_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=customers_Address_strategy)
@settings(max_examples=50)
def test_customers_address_instantiation(instance):
    assert isinstance(instance, customers_Address)



@given(instance=customers_Address_strategy)
def test_customers_address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original



@given(instance=customers_Address_strategy)
def test_customers_address_town_setter(instance):
    original = instance.town
    instance.town = original
    assert instance.town == original



@given(instance=customers_Address_strategy)
def test_customers_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=customers_CreditCard_strategy)
@settings(max_examples=50)
def test_customers_creditcard_instantiation(instance):
    assert isinstance(instance, customers_CreditCard)



@given(instance=customers_CreditCard_strategy)
def test_customers_creditcard_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=customers_CreditCard_strategy)
def test_customers_creditcard_expiresDate_setter(instance):
    original = instance.expiresDate
    instance.expiresDate = original
    assert instance.expiresDate == original



@given(instance=customers_CreditCard_strategy)
def test_customers_creditcard_ccNumber_setter(instance):
    original = instance.ccNumber
    instance.ccNumber = original
    assert instance.ccNumber == original

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)

@given(instance=customers_CanadaAddress_strategy)
@settings(max_examples=50)
def test_customers_canadaaddress_instantiation(instance):
    assert isinstance(instance, customers_CanadaAddress)



@given(instance=customers_CanadaAddress_strategy)
def test_customers_canadaaddress_province_setter(instance):
    original = instance.province
    instance.province = original
    assert instance.province == original

@given(instance=customers_USAddress_strategy)
@settings(max_examples=50)
def test_customers_usaddress_instantiation(instance):
    assert isinstance(instance, customers_USAddress)



@given(instance=customers_USAddress_strategy)
def test_customers_usaddress_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=customers_Customer_strategy)
@settings(max_examples=50)
def test_customers_customer_instantiation(instance):
    assert isinstance(instance, customers_Customer)



@given(instance=customers_Customer_strategy)
def test_customers_customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=customers_Customer_strategy)
def test_customers_customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=customers_Customer_strategy)
def test_customers_customer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=customers_Customer_strategy)
def test_customers_customer_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original
