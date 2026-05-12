import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Request,
    Requirement,
    Administrator,
    Seller,
    Buyer,
    Unreg_User,
    Reg_User,
    User,
    Property,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_request_is_not_abstract():
    assert not inspect.isabstract(Request)


def test_request_constructor_exists():
    assert callable(Request.__init__)


def test_request_constructor_args():
    sig = inspect.signature(Request.__init__)
    params = list(sig.parameters.keys())
    assert "request_id" in params, "Missing parameter 'request_id'"
    assert "request_type" in params, "Missing parameter 'request_type'"
    assert "request_details" in params, "Missing parameter 'request_details'"
    assert "requser_id" in params, "Missing parameter 'requser_id'"

def test_request_has_request_id():
    assert hasattr(Request, "request_id")
    descriptor = None
    for klass in Request.__mro__:
        if "request_id" in klass.__dict__:
            descriptor = klass.__dict__["request_id"]
            break
    assert isinstance(descriptor, property)

def test_request_has_request_type():
    assert hasattr(Request, "request_type")
    descriptor = None
    for klass in Request.__mro__:
        if "request_type" in klass.__dict__:
            descriptor = klass.__dict__["request_type"]
            break
    assert isinstance(descriptor, property)

def test_request_has_request_details():
    assert hasattr(Request, "request_details")
    descriptor = None
    for klass in Request.__mro__:
        if "request_details" in klass.__dict__:
            descriptor = klass.__dict__["request_details"]
            break
    assert isinstance(descriptor, property)

def test_request_has_requser_id():
    assert hasattr(Request, "requser_id")
    descriptor = None
    for klass in Request.__mro__:
        if "requser_id" in klass.__dict__:
            descriptor = klass.__dict__["requser_id"]
            break
    assert isinstance(descriptor, property)



def test_requirement_is_not_abstract():
    assert not inspect.isabstract(Requirement)


def test_requirement_constructor_exists():
    assert callable(Requirement.__init__)


def test_requirement_constructor_args():
    sig = inspect.signature(Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "requirement_type" in params, "Missing parameter 'requirement_type'"
    assert "req_description" in params, "Missing parameter 'req_description'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "requirement_location" in params, "Missing parameter 'requirement_location'"

def test_requirement_has_requirement_type():
    assert hasattr(Requirement, "requirement_type")
    descriptor = None
    for klass in Requirement.__mro__:
        if "requirement_type" in klass.__dict__:
            descriptor = klass.__dict__["requirement_type"]
            break
    assert isinstance(descriptor, property)

def test_requirement_has_req_description():
    assert hasattr(Requirement, "req_description")
    descriptor = None
    for klass in Requirement.__mro__:
        if "req_description" in klass.__dict__:
            descriptor = klass.__dict__["req_description"]
            break
    assert isinstance(descriptor, property)

def test_requirement_has_user_id():
    assert hasattr(Requirement, "user_id")
    descriptor = None
    for klass in Requirement.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_requirement_has_requirement_location():
    assert hasattr(Requirement, "requirement_location")
    descriptor = None
    for klass in Requirement.__mro__:
        if "requirement_location" in klass.__dict__:
            descriptor = klass.__dict__["requirement_location"]
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



def test_seller_is_not_abstract():
    assert not inspect.isabstract(Seller)


def test_seller_constructor_exists():
    assert callable(Seller.__init__)


def test_seller_constructor_args():
    sig = inspect.signature(Seller.__init__)
    params = list(sig.parameters.keys())
    assert "property_id" in params, "Missing parameter 'property_id'"
    assert "seller_id" in params, "Missing parameter 'seller_id'"

def test_seller_has_property_id():
    assert hasattr(Seller, "property_id")
    descriptor = None
    for klass in Seller.__mro__:
        if "property_id" in klass.__dict__:
            descriptor = klass.__dict__["property_id"]
            break
    assert isinstance(descriptor, property)

def test_seller_has_seller_id():
    assert hasattr(Seller, "seller_id")
    descriptor = None
    for klass in Seller.__mro__:
        if "seller_id" in klass.__dict__:
            descriptor = klass.__dict__["seller_id"]
            break
    assert isinstance(descriptor, property)



def test_buyer_is_not_abstract():
    assert not inspect.isabstract(Buyer)


def test_buyer_constructor_exists():
    assert callable(Buyer.__init__)


def test_buyer_constructor_args():
    sig = inspect.signature(Buyer.__init__)
    params = list(sig.parameters.keys())
    assert "buyer_id" in params, "Missing parameter 'buyer_id'"

def test_buyer_has_buyer_id():
    assert hasattr(Buyer, "buyer_id")
    descriptor = None
    for klass in Buyer.__mro__:
        if "buyer_id" in klass.__dict__:
            descriptor = klass.__dict__["buyer_id"]
            break
    assert isinstance(descriptor, property)



def test_unreg_user_is_not_abstract():
    assert not inspect.isabstract(Unreg_User)


def test_unreg_user_constructor_exists():
    assert callable(Unreg_User.__init__)


def test_unreg_user_constructor_args():
    sig = inspect.signature(Unreg_User.__init__)
    params = list(sig.parameters.keys())



def test_reg_user_is_not_abstract():
    assert not inspect.isabstract(Reg_User)


def test_reg_user_constructor_exists():
    assert callable(Reg_User.__init__)


def test_reg_user_constructor_args():
    sig = inspect.signature(Reg_User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_reg_user_has_password():
    assert hasattr(Reg_User, "password")
    descriptor = None
    for klass in Reg_User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_reg_user_has_username():
    assert hasattr(Reg_User, "username")
    descriptor = None
    for klass in Reg_User.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_reg_user_has_Address():
    assert hasattr(Reg_User, "Address")
    descriptor = None
    for klass in Reg_User.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "location" in params, "Missing parameter 'location'"

def test_user_has_email():
    assert hasattr(User, "email")
    descriptor = None
    for klass in User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_location():
    assert hasattr(User, "location")
    descriptor = None
    for klass in User.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())
    assert "property_id" in params, "Missing parameter 'property_id'"
    assert "property_type" in params, "Missing parameter 'property_type'"
    assert "address" in params, "Missing parameter 'address'"
    assert "location" in params, "Missing parameter 'location'"

def test_property_has_property_id():
    assert hasattr(Property, "property_id")
    descriptor = None
    for klass in Property.__mro__:
        if "property_id" in klass.__dict__:
            descriptor = klass.__dict__["property_id"]
            break
    assert isinstance(descriptor, property)

def test_property_has_property_type():
    assert hasattr(Property, "property_type")
    descriptor = None
    for klass in Property.__mro__:
        if "property_type" in klass.__dict__:
            descriptor = klass.__dict__["property_type"]
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

def test_property_has_location():
    assert hasattr(Property, "location")
    descriptor = None
    for klass in Property.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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
Request_strategy = st.builds(
    Request,
    request_id=
        st.integers(),
    request_type=
        safe_text,
    request_details=
        safe_text,
    requser_id=
        safe_text
)
Requirement_strategy = st.builds(
    Requirement,
    requirement_type=
        safe_text,
    req_description=
        safe_text,
    user_id=
        safe_text,
    requirement_location=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    admin_name=
        safe_text,
    password=
        safe_text
)
Seller_strategy = st.builds(
    Seller,
    property_id=
        safe_text,
    seller_id=
        safe_text
)
Buyer_strategy = st.builds(
    Buyer,
    buyer_id=
        safe_text
)
Unreg_User_strategy = st.builds(
    Unreg_User,
)
Reg_User_strategy = st.builds(
    Reg_User,
    password=
        safe_text,
    username=
        safe_text,
    Address=
        safe_text
)
User_strategy = st.builds(
    User,
    email=
        safe_text,
    location=
        safe_text
)
Property_strategy = st.builds(
    Property,
    property_id=
        safe_text,
    property_type=
        safe_text,
    address=
        safe_text,
    location=
        safe_text
)

@given(instance=Request_strategy)
@settings(max_examples=50)
def test_request_instantiation(instance):
    assert isinstance(instance, Request)



@given(instance=Request_strategy)
def test_request_request_id_setter(instance):
    original = instance.request_id
    instance.request_id = original
    assert instance.request_id == original



@given(instance=Request_strategy)
def test_request_request_type_setter(instance):
    original = instance.request_type
    instance.request_type = original
    assert instance.request_type == original



@given(instance=Request_strategy)
def test_request_request_details_setter(instance):
    original = instance.request_details
    instance.request_details = original
    assert instance.request_details == original



@given(instance=Request_strategy)
def test_request_requser_id_setter(instance):
    original = instance.requser_id
    instance.requser_id = original
    assert instance.requser_id == original

@given(instance=Requirement_strategy)
@settings(max_examples=50)
def test_requirement_instantiation(instance):
    assert isinstance(instance, Requirement)



@given(instance=Requirement_strategy)
def test_requirement_requirement_type_setter(instance):
    original = instance.requirement_type
    instance.requirement_type = original
    assert instance.requirement_type == original



@given(instance=Requirement_strategy)
def test_requirement_req_description_setter(instance):
    original = instance.req_description
    instance.req_description = original
    assert instance.req_description == original



@given(instance=Requirement_strategy)
def test_requirement_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Requirement_strategy)
def test_requirement_requirement_location_setter(instance):
    original = instance.requirement_location
    instance.requirement_location = original
    assert instance.requirement_location == original

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

@given(instance=Seller_strategy)
@settings(max_examples=50)
def test_seller_instantiation(instance):
    assert isinstance(instance, Seller)



@given(instance=Seller_strategy)
def test_seller_property_id_setter(instance):
    original = instance.property_id
    instance.property_id = original
    assert instance.property_id == original



@given(instance=Seller_strategy)
def test_seller_seller_id_setter(instance):
    original = instance.seller_id
    instance.seller_id = original
    assert instance.seller_id == original

@given(instance=Buyer_strategy)
@settings(max_examples=50)
def test_buyer_instantiation(instance):
    assert isinstance(instance, Buyer)



@given(instance=Buyer_strategy)
def test_buyer_buyer_id_setter(instance):
    original = instance.buyer_id
    instance.buyer_id = original
    assert instance.buyer_id == original

@given(instance=Unreg_User_strategy)
@settings(max_examples=50)
def test_unreg_user_instantiation(instance):
    assert isinstance(instance, Unreg_User)

@given(instance=Reg_User_strategy)
@settings(max_examples=50)
def test_reg_user_instantiation(instance):
    assert isinstance(instance, Reg_User)



@given(instance=Reg_User_strategy)
def test_reg_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Reg_User_strategy)
def test_reg_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Reg_User_strategy)
def test_reg_user_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

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
def test_user_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)



@given(instance=Property_strategy)
def test_property_property_id_setter(instance):
    original = instance.property_id
    instance.property_id = original
    assert instance.property_id == original



@given(instance=Property_strategy)
def test_property_property_type_setter(instance):
    original = instance.property_type
    instance.property_type = original
    assert instance.property_type == original



@given(instance=Property_strategy)
def test_property_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Property_strategy)
def test_property_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
