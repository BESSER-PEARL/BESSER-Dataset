import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    customers::CustomersDB,
    customers::Address,
    customers::CreditCard,
    Address,
    customers::CanadaAddress,
    customers::USAddress,
    customers::Customer,
    CanadaProvinces,
    USStates,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_customers::customersdb_is_not_abstract():
    assert not inspect.isabstract(customers::CustomersDB)


def test_customers::customersdb_constructor_exists():
    assert callable(customers::CustomersDB.__init__)


def test_customers::customersdb_constructor_args():
    sig = inspect.signature(customers::CustomersDB.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_customers::customersdb_has_comment():
    assert hasattr(customers::CustomersDB, "comment")
    descriptor = None
    for klass in customers::CustomersDB.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_customers::address_is_not_abstract():
    assert not inspect.isabstract(customers::Address)


def test_customers::address_constructor_exists():
    assert callable(customers::Address.__init__)


def test_customers::address_constructor_args():
    sig = inspect.signature(customers::Address.__init__)
    params = list(sig.parameters.keys())
    assert "town" in params, "Missing parameter 'town'"
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "street" in params, "Missing parameter 'street'"

def test_customers::address_has_town():
    assert hasattr(customers::Address, "town")
    descriptor = None
    for klass in customers::Address.__mro__:
        if "town" in klass.__dict__:
            descriptor = klass.__dict__["town"]
            break
    assert isinstance(descriptor, property)

def test_customers::address_has_zipCode():
    assert hasattr(customers::Address, "zipCode")
    descriptor = None
    for klass in customers::Address.__mro__:
        if "zipCode" in klass.__dict__:
            descriptor = klass.__dict__["zipCode"]
            break
    assert isinstance(descriptor, property)

def test_customers::address_has_street():
    assert hasattr(customers::Address, "street")
    descriptor = None
    for klass in customers::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)



def test_customers::creditcard_is_not_abstract():
    assert not inspect.isabstract(customers::CreditCard)


def test_customers::creditcard_constructor_exists():
    assert callable(customers::CreditCard.__init__)


def test_customers::creditcard_constructor_args():
    sig = inspect.signature(customers::CreditCard.__init__)
    params = list(sig.parameters.keys())
    assert "ccNumber" in params, "Missing parameter 'ccNumber'"
    assert "type" in params, "Missing parameter 'type'"
    assert "expiresDate" in params, "Missing parameter 'expiresDate'"

def test_customers::creditcard_has_ccNumber():
    assert hasattr(customers::CreditCard, "ccNumber")
    descriptor = None
    for klass in customers::CreditCard.__mro__:
        if "ccNumber" in klass.__dict__:
            descriptor = klass.__dict__["ccNumber"]
            break
    assert isinstance(descriptor, property)

def test_customers::creditcard_has_type():
    assert hasattr(customers::CreditCard, "type")
    descriptor = None
    for klass in customers::CreditCard.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_customers::creditcard_has_expiresDate():
    assert hasattr(customers::CreditCard, "expiresDate")
    descriptor = None
    for klass in customers::CreditCard.__mro__:
        if "expiresDate" in klass.__dict__:
            descriptor = klass.__dict__["expiresDate"]
            break
    assert isinstance(descriptor, property)



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_customers::canadaaddress_is_not_abstract():
    assert not inspect.isabstract(customers::CanadaAddress)


def test_customers::canadaaddress_constructor_exists():
    assert callable(customers::CanadaAddress.__init__)


def test_customers::canadaaddress_constructor_args():
    sig = inspect.signature(customers::CanadaAddress.__init__)
    params = list(sig.parameters.keys())
    assert "province" in params, "Missing parameter 'province'"

def test_customers::canadaaddress_has_province():
    assert hasattr(customers::CanadaAddress, "province")
    descriptor = None
    for klass in customers::CanadaAddress.__mro__:
        if "province" in klass.__dict__:
            descriptor = klass.__dict__["province"]
            break
    assert isinstance(descriptor, property)



def test_customers::usaddress_is_not_abstract():
    assert not inspect.isabstract(customers::USAddress)


def test_customers::usaddress_constructor_exists():
    assert callable(customers::USAddress.__init__)


def test_customers::usaddress_constructor_args():
    sig = inspect.signature(customers::USAddress.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_customers::usaddress_has_state():
    assert hasattr(customers::USAddress, "state")
    descriptor = None
    for klass in customers::USAddress.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_customers::customer_is_not_abstract():
    assert not inspect.isabstract(customers::Customer)


def test_customers::customer_constructor_exists():
    assert callable(customers::Customer.__init__)


def test_customers::customer_constructor_args():
    sig = inspect.signature(customers::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"

def test_customers::customer_has_lastName():
    assert hasattr(customers::Customer, "lastName")
    descriptor = None
    for klass in customers::Customer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_customers::customer_has_comment():
    assert hasattr(customers::Customer, "comment")
    descriptor = None
    for klass in customers::Customer.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_customers::customer_has_firstName():
    assert hasattr(customers::Customer, "firstName")
    descriptor = None
    for klass in customers::Customer.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_customers::customer_has_dateOfBirth():
    assert hasattr(customers::Customer, "dateOfBirth")
    descriptor = None
    for klass in customers::Customer.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_canadaprovinces_exists():
    # Check that the Enumeration exists
    assert CanadaProvinces is not None

def test_canadaprovinces_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CanadaProvinces]
    expected_literals = [
        "AB",
        "BC",
        "NT",
        "NB",
        "MB",
        "NL",
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
        "AL",
        "CO",
        "AR",
        "AS",
        "CA",
        "AZ",
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
customers::CustomersDB_strategy = st.builds(
    customers::CustomersDB,
    comment=
        safe_text
)
customers::Address_strategy = st.builds(
    customers::Address,
    town=
        safe_text,
    zipCode=
        safe_text,
    street=
        safe_text
)
customers::CreditCard_strategy = st.builds(
    customers::CreditCard,
    ccNumber=
        safe_text,
    type=
        safe_text,
    expiresDate=
        st.dates()
)
Address_strategy = st.builds(
    Address,
)
customers::CanadaAddress_strategy = st.builds(
    customers::CanadaAddress,
    province=
        safe_text
)
customers::USAddress_strategy = st.builds(
    customers::USAddress,
    state=
        safe_text
)
customers::Customer_strategy = st.builds(
    customers::Customer,
    lastName=
        safe_text,
    comment=
        safe_text,
    firstName=
        safe_text,
    dateOfBirth=
        st.dates()
)

@given(instance=customers::CustomersDB_strategy)
@settings(max_examples=50)
def test_customers::customersdb_instantiation(instance):
    assert isinstance(instance, customers::CustomersDB)

@given(instance=customers::CustomersDB_strategy)
def test_customers::customersdb_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=customers::CustomersDB_strategy)
def test_customers::customersdb_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=customers::Address_strategy)
@settings(max_examples=50)
def test_customers::address_instantiation(instance):
    assert isinstance(instance, customers::Address)

@given(instance=customers::Address_strategy)
def test_customers::address_town_type(instance):
    assert isinstance(instance.town, str)


@given(instance=customers::Address_strategy)
def test_customers::address_town_setter(instance):
    original = instance.town
    instance.town = original
    assert instance.town == original

@given(instance=customers::Address_strategy)
def test_customers::address_zipCode_type(instance):
    assert isinstance(instance.zipCode, str)


@given(instance=customers::Address_strategy)
def test_customers::address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original

@given(instance=customers::Address_strategy)
def test_customers::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=customers::Address_strategy)
def test_customers::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=customers::CreditCard_strategy)
@settings(max_examples=50)
def test_customers::creditcard_instantiation(instance):
    assert isinstance(instance, customers::CreditCard)

@given(instance=customers::CreditCard_strategy)
def test_customers::creditcard_ccNumber_type(instance):
    assert isinstance(instance.ccNumber, str)


@given(instance=customers::CreditCard_strategy)
def test_customers::creditcard_ccNumber_setter(instance):
    original = instance.ccNumber
    instance.ccNumber = original
    assert instance.ccNumber == original

@given(instance=customers::CreditCard_strategy)
def test_customers::creditcard_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=customers::CreditCard_strategy)
def test_customers::creditcard_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=customers::CreditCard_strategy)
def test_customers::creditcard_expiresDate_type(instance):
    assert isinstance(instance.expiresDate, date)


@given(instance=customers::CreditCard_strategy)
def test_customers::creditcard_expiresDate_setter(instance):
    original = instance.expiresDate
    instance.expiresDate = original
    assert instance.expiresDate == original

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)

@given(instance=customers::CanadaAddress_strategy)
@settings(max_examples=50)
def test_customers::canadaaddress_instantiation(instance):
    assert isinstance(instance, customers::CanadaAddress)

@given(instance=customers::CanadaAddress_strategy)
def test_customers::canadaaddress_province_type(instance):
    assert isinstance(instance.province, str)


@given(instance=customers::CanadaAddress_strategy)
def test_customers::canadaaddress_province_setter(instance):
    original = instance.province
    instance.province = original
    assert instance.province == original

@given(instance=customers::USAddress_strategy)
@settings(max_examples=50)
def test_customers::usaddress_instantiation(instance):
    assert isinstance(instance, customers::USAddress)

@given(instance=customers::USAddress_strategy)
def test_customers::usaddress_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=customers::USAddress_strategy)
def test_customers::usaddress_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=customers::Customer_strategy)
@settings(max_examples=50)
def test_customers::customer_instantiation(instance):
    assert isinstance(instance, customers::Customer)

@given(instance=customers::Customer_strategy)
def test_customers::customer_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=customers::Customer_strategy)
def test_customers::customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=customers::Customer_strategy)
def test_customers::customer_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=customers::Customer_strategy)
def test_customers::customer_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=customers::Customer_strategy)
def test_customers::customer_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=customers::Customer_strategy)
def test_customers::customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=customers::Customer_strategy)
def test_customers::customer_dateOfBirth_type(instance):
    assert isinstance(instance.dateOfBirth, date)


@given(instance=customers::Customer_strategy)
def test_customers::customer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original
