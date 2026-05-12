import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Buildings,
    Management,
    Request,
    Requirement,
    Payment,
    Administrator,
    Owner,
    Tenant,
    Manager,
    Unreg_User,
    Reg_User,
    User,
    Property,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_buildings_is_not_abstract():
    assert not inspect.isabstract(Buildings)


def test_buildings_constructor_exists():
    assert callable(Buildings.__init__)


def test_buildings_constructor_args():
    sig = inspect.signature(Buildings.__init__)
    params = list(sig.parameters.keys())
    assert "management_id" in params, "Missing parameter 'management_id'"
    assert "end_date" in params, "Missing parameter 'end_date'"
    assert "start_date" in params, "Missing parameter 'start_date'"
    assert "manager_id" in params, "Missing parameter 'manager_id'"

def test_buildings_has_management_id():
    assert hasattr(Buildings, "management_id")
    descriptor = None
    for klass in Buildings.__mro__:
        if "management_id" in klass.__dict__:
            descriptor = klass.__dict__["management_id"]
            break
    assert isinstance(descriptor, property)

def test_buildings_has_end_date():
    assert hasattr(Buildings, "end_date")
    descriptor = None
    for klass in Buildings.__mro__:
        if "end_date" in klass.__dict__:
            descriptor = klass.__dict__["end_date"]
            break
    assert isinstance(descriptor, property)

def test_buildings_has_start_date():
    assert hasattr(Buildings, "start_date")
    descriptor = None
    for klass in Buildings.__mro__:
        if "start_date" in klass.__dict__:
            descriptor = klass.__dict__["start_date"]
            break
    assert isinstance(descriptor, property)

def test_buildings_has_manager_id():
    assert hasattr(Buildings, "manager_id")
    descriptor = None
    for klass in Buildings.__mro__:
        if "manager_id" in klass.__dict__:
            descriptor = klass.__dict__["manager_id"]
            break
    assert isinstance(descriptor, property)



def test_management_is_not_abstract():
    assert not inspect.isabstract(Management)


def test_management_constructor_exists():
    assert callable(Management.__init__)


def test_management_constructor_args():
    sig = inspect.signature(Management.__init__)
    params = list(sig.parameters.keys())
    assert "specialoffers" in params, "Missing parameter 'specialoffers'"
    assert "suggetions" in params, "Missing parameter 'suggetions'"

def test_management_has_specialoffers():
    assert hasattr(Management, "specialoffers")
    descriptor = None
    for klass in Management.__mro__:
        if "specialoffers" in klass.__dict__:
            descriptor = klass.__dict__["specialoffers"]
            break
    assert isinstance(descriptor, property)

def test_management_has_suggetions():
    assert hasattr(Management, "suggetions")
    descriptor = None
    for klass in Management.__mro__:
        if "suggetions" in klass.__dict__:
            descriptor = klass.__dict__["suggetions"]
            break
    assert isinstance(descriptor, property)



def test_request_is_not_abstract():
    assert not inspect.isabstract(Request)


def test_request_constructor_exists():
    assert callable(Request.__init__)


def test_request_constructor_args():
    sig = inspect.signature(Request.__init__)
    params = list(sig.parameters.keys())
    assert "request_type" in params, "Missing parameter 'request_type'"
    assert "request_details" in params, "Missing parameter 'request_details'"
    assert "requser_id" in params, "Missing parameter 'requser_id'"
    assert "request_id" in params, "Missing parameter 'request_id'"

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

def test_request_has_request_id():
    assert hasattr(Request, "request_id")
    descriptor = None
    for klass in Request.__mro__:
        if "request_id" in klass.__dict__:
            descriptor = klass.__dict__["request_id"]
            break
    assert isinstance(descriptor, property)



def test_requirement_is_not_abstract():
    assert not inspect.isabstract(Requirement)


def test_requirement_constructor_exists():
    assert callable(Requirement.__init__)


def test_requirement_constructor_args():
    sig = inspect.signature(Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "req_description" in params, "Missing parameter 'req_description'"
    assert "requirement_type" in params, "Missing parameter 'requirement_type'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "requirement_location" in params, "Missing parameter 'requirement_location'"

def test_requirement_has_req_description():
    assert hasattr(Requirement, "req_description")
    descriptor = None
    for klass in Requirement.__mro__:
        if "req_description" in klass.__dict__:
            descriptor = klass.__dict__["req_description"]
            break
    assert isinstance(descriptor, property)

def test_requirement_has_requirement_type():
    assert hasattr(Requirement, "requirement_type")
    descriptor = None
    for klass in Requirement.__mro__:
        if "requirement_type" in klass.__dict__:
            descriptor = klass.__dict__["requirement_type"]
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



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "pay_mode" in params, "Missing parameter 'pay_mode'"
    assert "ex_date" in params, "Missing parameter 'ex_date'"
    assert "card_no" in params, "Missing parameter 'card_no'"
    assert "pay_amount" in params, "Missing parameter 'pay_amount'"
    assert "pay_id" in params, "Missing parameter 'pay_id'"

def test_payment_has_pay_mode():
    assert hasattr(Payment, "pay_mode")
    descriptor = None
    for klass in Payment.__mro__:
        if "pay_mode" in klass.__dict__:
            descriptor = klass.__dict__["pay_mode"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_ex_date():
    assert hasattr(Payment, "ex_date")
    descriptor = None
    for klass in Payment.__mro__:
        if "ex_date" in klass.__dict__:
            descriptor = klass.__dict__["ex_date"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_card_no():
    assert hasattr(Payment, "card_no")
    descriptor = None
    for klass in Payment.__mro__:
        if "card_no" in klass.__dict__:
            descriptor = klass.__dict__["card_no"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_pay_amount():
    assert hasattr(Payment, "pay_amount")
    descriptor = None
    for klass in Payment.__mro__:
        if "pay_amount" in klass.__dict__:
            descriptor = klass.__dict__["pay_amount"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_pay_id():
    assert hasattr(Payment, "pay_id")
    descriptor = None
    for klass in Payment.__mro__:
        if "pay_id" in klass.__dict__:
            descriptor = klass.__dict__["pay_id"]
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
    assert not inspect.isabstract(Owner)


def test_owner_constructor_exists():
    assert callable(Owner.__init__)


def test_owner_constructor_args():
    sig = inspect.signature(Owner.__init__)
    params = list(sig.parameters.keys())
    assert "property_id" in params, "Missing parameter 'property_id'"
    assert "owner_id" in params, "Missing parameter 'owner_id'"

def test_owner_has_property_id():
    assert hasattr(Owner, "property_id")
    descriptor = None
    for klass in Owner.__mro__:
        if "property_id" in klass.__dict__:
            descriptor = klass.__dict__["property_id"]
            break
    assert isinstance(descriptor, property)

def test_owner_has_owner_id():
    assert hasattr(Owner, "owner_id")
    descriptor = None
    for klass in Owner.__mro__:
        if "owner_id" in klass.__dict__:
            descriptor = klass.__dict__["owner_id"]
            break
    assert isinstance(descriptor, property)



def test_tenant_is_not_abstract():
    assert not inspect.isabstract(Tenant)


def test_tenant_constructor_exists():
    assert callable(Tenant.__init__)


def test_tenant_constructor_args():
    sig = inspect.signature(Tenant.__init__)
    params = list(sig.parameters.keys())
    assert "tenant_id" in params, "Missing parameter 'tenant_id'"

def test_tenant_has_tenant_id():
    assert hasattr(Tenant, "tenant_id")
    descriptor = None
    for klass in Tenant.__mro__:
        if "tenant_id" in klass.__dict__:
            descriptor = klass.__dict__["tenant_id"]
            break
    assert isinstance(descriptor, property)



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "manager_id" in params, "Missing parameter 'manager_id'"
    assert "management_id" in params, "Missing parameter 'management_id'"

def test_manager_has_manager_id():
    assert hasattr(Manager, "manager_id")
    descriptor = None
    for klass in Manager.__mro__:
        if "manager_id" in klass.__dict__:
            descriptor = klass.__dict__["manager_id"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_management_id():
    assert hasattr(Manager, "management_id")
    descriptor = None
    for klass in Manager.__mro__:
        if "management_id" in klass.__dict__:
            descriptor = klass.__dict__["management_id"]
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
    assert "Address" in params, "Missing parameter 'Address'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"

def test_reg_user_has_Address():
    assert hasattr(Reg_User, "Address")
    descriptor = None
    for klass in Reg_User.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

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
    assert "address" in params, "Missing parameter 'address'"
    assert "location" in params, "Missing parameter 'location'"
    assert "property_type" in params, "Missing parameter 'property_type'"

def test_property_has_property_id():
    assert hasattr(Property, "property_id")
    descriptor = None
    for klass in Property.__mro__:
        if "property_id" in klass.__dict__:
            descriptor = klass.__dict__["property_id"]
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

def test_property_has_property_type():
    assert hasattr(Property, "property_type")
    descriptor = None
    for klass in Property.__mro__:
        if "property_type" in klass.__dict__:
            descriptor = klass.__dict__["property_type"]
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
Buildings_strategy = st.builds(
    Buildings,
    management_id=
        st.integers(),
    end_date=
        safe_text,
    start_date=
        safe_text,
    manager_id=
        safe_text
)
Management_strategy = st.builds(
    Management,
    specialoffers=
        safe_text,
    suggetions=
        safe_text
)
Request_strategy = st.builds(
    Request,
    request_type=
        safe_text,
    request_details=
        safe_text,
    requser_id=
        safe_text,
    request_id=
        st.integers()
)
Requirement_strategy = st.builds(
    Requirement,
    req_description=
        safe_text,
    requirement_type=
        safe_text,
    user_id=
        safe_text,
    requirement_location=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    pay_mode=
        safe_text,
    ex_date=
        safe_text,
    card_no=
        safe_text,
    pay_amount=
        safe_text,
    pay_id=
        st.integers()
)
Administrator_strategy = st.builds(
    Administrator,
    admin_name=
        safe_text,
    password=
        safe_text
)
Owner_strategy = st.builds(
    Owner,
    property_id=
        safe_text,
    owner_id=
        safe_text
)
Tenant_strategy = st.builds(
    Tenant,
    tenant_id=
        safe_text
)
Manager_strategy = st.builds(
    Manager,
    manager_id=
        safe_text,
    management_id=
        safe_text
)
Unreg_User_strategy = st.builds(
    Unreg_User,
)
Reg_User_strategy = st.builds(
    Reg_User,
    Address=
        safe_text,
    password=
        safe_text,
    username=
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
    address=
        safe_text,
    location=
        safe_text,
    property_type=
        safe_text
)

@given(instance=Buildings_strategy)
@settings(max_examples=50)
def test_buildings_instantiation(instance):
    assert isinstance(instance, Buildings)



@given(instance=Buildings_strategy)
def test_buildings_management_id_setter(instance):
    original = instance.management_id
    instance.management_id = original
    assert instance.management_id == original



@given(instance=Buildings_strategy)
def test_buildings_end_date_setter(instance):
    original = instance.end_date
    instance.end_date = original
    assert instance.end_date == original



@given(instance=Buildings_strategy)
def test_buildings_start_date_setter(instance):
    original = instance.start_date
    instance.start_date = original
    assert instance.start_date == original



@given(instance=Buildings_strategy)
def test_buildings_manager_id_setter(instance):
    original = instance.manager_id
    instance.manager_id = original
    assert instance.manager_id == original

@given(instance=Management_strategy)
@settings(max_examples=50)
def test_management_instantiation(instance):
    assert isinstance(instance, Management)



@given(instance=Management_strategy)
def test_management_specialoffers_setter(instance):
    original = instance.specialoffers
    instance.specialoffers = original
    assert instance.specialoffers == original



@given(instance=Management_strategy)
def test_management_suggetions_setter(instance):
    original = instance.suggetions
    instance.suggetions = original
    assert instance.suggetions == original

@given(instance=Request_strategy)
@settings(max_examples=50)
def test_request_instantiation(instance):
    assert isinstance(instance, Request)



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



@given(instance=Request_strategy)
def test_request_request_id_setter(instance):
    original = instance.request_id
    instance.request_id = original
    assert instance.request_id == original

@given(instance=Requirement_strategy)
@settings(max_examples=50)
def test_requirement_instantiation(instance):
    assert isinstance(instance, Requirement)



@given(instance=Requirement_strategy)
def test_requirement_req_description_setter(instance):
    original = instance.req_description
    instance.req_description = original
    assert instance.req_description == original



@given(instance=Requirement_strategy)
def test_requirement_requirement_type_setter(instance):
    original = instance.requirement_type
    instance.requirement_type = original
    assert instance.requirement_type == original



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

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_pay_mode_setter(instance):
    original = instance.pay_mode
    instance.pay_mode = original
    assert instance.pay_mode == original



@given(instance=Payment_strategy)
def test_payment_ex_date_setter(instance):
    original = instance.ex_date
    instance.ex_date = original
    assert instance.ex_date == original



@given(instance=Payment_strategy)
def test_payment_card_no_setter(instance):
    original = instance.card_no
    instance.card_no = original
    assert instance.card_no == original



@given(instance=Payment_strategy)
def test_payment_pay_amount_setter(instance):
    original = instance.pay_amount
    instance.pay_amount = original
    assert instance.pay_amount == original



@given(instance=Payment_strategy)
def test_payment_pay_id_setter(instance):
    original = instance.pay_id
    instance.pay_id = original
    assert instance.pay_id == original

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

@given(instance=Owner_strategy)
@settings(max_examples=50)
def test_owner_instantiation(instance):
    assert isinstance(instance, Owner)



@given(instance=Owner_strategy)
def test_owner_property_id_setter(instance):
    original = instance.property_id
    instance.property_id = original
    assert instance.property_id == original



@given(instance=Owner_strategy)
def test_owner_owner_id_setter(instance):
    original = instance.owner_id
    instance.owner_id = original
    assert instance.owner_id == original

@given(instance=Tenant_strategy)
@settings(max_examples=50)
def test_tenant_instantiation(instance):
    assert isinstance(instance, Tenant)



@given(instance=Tenant_strategy)
def test_tenant_tenant_id_setter(instance):
    original = instance.tenant_id
    instance.tenant_id = original
    assert instance.tenant_id == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_manager_manager_id_setter(instance):
    original = instance.manager_id
    instance.manager_id = original
    assert instance.manager_id == original



@given(instance=Manager_strategy)
def test_manager_management_id_setter(instance):
    original = instance.management_id
    instance.management_id = original
    assert instance.management_id == original

@given(instance=Unreg_User_strategy)
@settings(max_examples=50)
def test_unreg_user_instantiation(instance):
    assert isinstance(instance, Unreg_User)

@given(instance=Reg_User_strategy)
@settings(max_examples=50)
def test_reg_user_instantiation(instance):
    assert isinstance(instance, Reg_User)



@given(instance=Reg_User_strategy)
def test_reg_user_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



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
def test_property_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Property_strategy)
def test_property_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Property_strategy)
def test_property_property_type_setter(instance):
    original = instance.property_type
    instance.property_type = original
    assert instance.property_type == original
