import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    operation_or_contract,
    Administrator,
    owner,
    customer,
    User,
    Property,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_operation_or_contract_is_not_abstract():
    assert not inspect.isabstract(operation_or_contract)


def test_operation_or_contract_constructor_exists():
    assert callable(operation_or_contract.__init__)


def test_operation_or_contract_constructor_args():
    sig = inspect.signature(operation_or_contract.__init__)
    params = list(sig.parameters.keys())
    assert "operation_id" in params, "Missing parameter 'operation_id'"
    assert "operation_type" in params, "Missing parameter 'operation_type'"
    assert "owner_id" in params, "Missing parameter 'owner_id'"
    assert "customer_id" in params, "Missing parameter 'customer_id'"
    assert "Property_id" in params, "Missing parameter 'Property_id'"

def test_operation_or_contract_has_operation_id():
    assert hasattr(operation_or_contract, "operation_id")
    descriptor = None
    for klass in operation_or_contract.__mro__:
        if "operation_id" in klass.__dict__:
            descriptor = klass.__dict__["operation_id"]
            break
    assert isinstance(descriptor, property)

def test_operation_or_contract_has_operation_type():
    assert hasattr(operation_or_contract, "operation_type")
    descriptor = None
    for klass in operation_or_contract.__mro__:
        if "operation_type" in klass.__dict__:
            descriptor = klass.__dict__["operation_type"]
            break
    assert isinstance(descriptor, property)

def test_operation_or_contract_has_owner_id():
    assert hasattr(operation_or_contract, "owner_id")
    descriptor = None
    for klass in operation_or_contract.__mro__:
        if "owner_id" in klass.__dict__:
            descriptor = klass.__dict__["owner_id"]
            break
    assert isinstance(descriptor, property)

def test_operation_or_contract_has_customer_id():
    assert hasattr(operation_or_contract, "customer_id")
    descriptor = None
    for klass in operation_or_contract.__mro__:
        if "customer_id" in klass.__dict__:
            descriptor = klass.__dict__["customer_id"]
            break
    assert isinstance(descriptor, property)

def test_operation_or_contract_has_Property_id():
    assert hasattr(operation_or_contract, "Property_id")
    descriptor = None
    for klass in operation_or_contract.__mro__:
        if "Property_id" in klass.__dict__:
            descriptor = klass.__dict__["Property_id"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "admin_name" in params, "Missing parameter 'admin_name'"
    assert "password" in params, "Missing parameter 'password'"

def test_administrator_has_admin_name():
    assert hasattr(Administrator, "admin_name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "admin_name" in klass.__dict__:
            descriptor = klass.__dict__["admin_name"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_password():
    assert hasattr(Administrator, "password")
    descriptor = None
    for klass in Administrator.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_owner_is_not_abstract():
    assert not inspect.isabstract(owner)


def test_owner_constructor_exists():
    assert callable(owner.__init__)


def test_owner_constructor_args():
    sig = inspect.signature(owner.__init__)
    params = list(sig.parameters.keys())



def test_customer_is_not_abstract():
    assert not inspect.isabstract(customer)


def test_customer_constructor_exists():
    assert callable(customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(customer.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_user_has_email():
    assert hasattr(User, "email")
    descriptor = None
    for klass in User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Address():
    assert hasattr(User, "Address")
    descriptor = None
    for klass in User.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_user_has_phone():
    assert hasattr(User, "phone")
    descriptor = None
    for klass in User.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Id():
    assert hasattr(User, "Id")
    descriptor = None
    for klass in User.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())
    assert "property_type" in params, "Missing parameter 'property_type'"
    assert "location" in params, "Missing parameter 'location'"
    assert "Available" in params, "Missing parameter 'Available'"
    assert "size" in params, "Missing parameter 'size'"
    assert "address" in params, "Missing parameter 'address'"
    assert "property_id" in params, "Missing parameter 'property_id'"

def test_property_has_property_type():
    assert hasattr(Property, "property_type")
    descriptor = None
    for klass in Property.__mro__:
        if "property_type" in klass.__dict__:
            descriptor = klass.__dict__["property_type"]
            break
    assert isinstance(descriptor, property)

def test_property_has_location():
    assert hasattr(Property, "location")
    descriptor = None
    for klass in Property.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_property_has_Available():
    assert hasattr(Property, "Available")
    descriptor = None
    for klass in Property.__mro__:
        if "Available" in klass.__dict__:
            descriptor = klass.__dict__["Available"]
            break
    assert isinstance(descriptor, property)

def test_property_has_size():
    assert hasattr(Property, "size")
    descriptor = None
    for klass in Property.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_property_has_address():
    assert hasattr(Property, "address")
    descriptor = None
    for klass in Property.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_property_has_property_id():
    assert hasattr(Property, "property_id")
    descriptor = None
    for klass in Property.__mro__:
        if "property_id" in klass.__dict__:
            descriptor = klass.__dict__["property_id"]
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
operation_or_contract_strategy = st.builds(
    operation_or_contract,
    operation_id=
        st.integers(),
    operation_type=
        safe_text,
    owner_id=
        safe_text,
    customer_id=
        safe_text,
    Property_id=
        st.integers()
)
Administrator_strategy = st.builds(
    Administrator,
    admin_name=
        safe_text,
    password=
        safe_text
)
owner_strategy = st.builds(
    owner,
)
customer_strategy = st.builds(
    customer,
)
User_strategy = st.builds(
    User,
    email=
        safe_text,
    password=
        safe_text,
    Address=
        safe_text,
    phone=
        st.integers(),
    Id=
        st.integers()
)
Property_strategy = st.builds(
    Property,
    property_type=
        safe_text,
    location=
        safe_text,
    Available=
        st.booleans(),
    size=
        safe_text,
    address=
        safe_text,
    property_id=
        safe_text
)

@given(instance=operation_or_contract_strategy)
@settings(max_examples=50)
def test_operation_or_contract_instantiation(instance):
    assert isinstance(instance, operation_or_contract)



@given(instance=operation_or_contract_strategy)
def test_operation_or_contract_operation_id_setter(instance):
    original = instance.operation_id
    instance.operation_id = original
    assert instance.operation_id == original



@given(instance=operation_or_contract_strategy)
def test_operation_or_contract_operation_type_setter(instance):
    original = instance.operation_type
    instance.operation_type = original
    assert instance.operation_type == original



@given(instance=operation_or_contract_strategy)
def test_operation_or_contract_owner_id_setter(instance):
    original = instance.owner_id
    instance.owner_id = original
    assert instance.owner_id == original



@given(instance=operation_or_contract_strategy)
def test_operation_or_contract_customer_id_setter(instance):
    original = instance.customer_id
    instance.customer_id = original
    assert instance.customer_id == original



@given(instance=operation_or_contract_strategy)
def test_operation_or_contract_Property_id_setter(instance):
    original = instance.Property_id
    instance.Property_id = original
    assert instance.Property_id == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_admin_name_setter(instance):
    original = instance.admin_name
    instance.admin_name = original
    assert instance.admin_name == original



@given(instance=Administrator_strategy)
def test_administrator_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=owner_strategy)
@settings(max_examples=50)
def test_owner_instantiation(instance):
    assert isinstance(instance, owner)

@given(instance=customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, customer)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=User_strategy)
def test_user_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=User_strategy)
def test_user_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)



@given(instance=Property_strategy)
def test_property_property_type_setter(instance):
    original = instance.property_type
    instance.property_type = original
    assert instance.property_type == original



@given(instance=Property_strategy)
def test_property_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Property_strategy)
def test_property_Available_setter(instance):
    original = instance.Available
    instance.Available = original
    assert instance.Available == original



@given(instance=Property_strategy)
def test_property_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=Property_strategy)
def test_property_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Property_strategy)
def test_property_property_id_setter(instance):
    original = instance.property_id
    instance.property_id = original
    assert instance.property_id == original
