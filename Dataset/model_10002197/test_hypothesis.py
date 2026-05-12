import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Admin_,
    member,
    Workers,
    customers,
    Accessories,
    Devices,
    ComputerParts,
    Items,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_admin__is_not_abstract():
    assert not inspect.isabstract(Admin_)


def test_admin__constructor_exists():
    assert callable(Admin_.__init__)


def test_admin__constructor_args():
    sig = inspect.signature(Admin_.__init__)
    params = list(sig.parameters.keys())
    assert "ArrayList_worker_" in params, "Missing parameter 'ArrayList_worker_'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "ArrayList_member_" in params, "Missing parameter 'ArrayList_member_'"

def test_admin__has_ArrayList_worker_():
    assert hasattr(Admin_, "ArrayList_worker_")
    descriptor = None
    for klass in Admin_.__mro__:
        if "ArrayList_worker_" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList_worker_"]
            break
    assert isinstance(descriptor, property)

def test_admin__has_Password():
    assert hasattr(Admin_, "Password")
    descriptor = None
    for klass in Admin_.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_admin__has_ArrayList_member_():
    assert hasattr(Admin_, "ArrayList_member_")
    descriptor = None
    for klass in Admin_.__mro__:
        if "ArrayList_member_" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList_member_"]
            break
    assert isinstance(descriptor, property)



def test_member_is_not_abstract():
    assert not inspect.isabstract(member)


def test_member_constructor_exists():
    assert callable(member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "memberType" in params, "Missing parameter 'memberType'"

def test_member_has_name():
    assert hasattr(member, "name")
    descriptor = None
    for klass in member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_member_has_password():
    assert hasattr(member, "password")
    descriptor = None
    for klass in member.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_member_has_memberType():
    assert hasattr(member, "memberType")
    descriptor = None
    for klass in member.__mro__:
        if "memberType" in klass.__dict__:
            descriptor = klass.__dict__["memberType"]
            break
    assert isinstance(descriptor, property)



def test_workers_is_not_abstract():
    assert not inspect.isabstract(Workers)


def test_workers_constructor_exists():
    assert callable(Workers.__init__)


def test_workers_constructor_args():
    sig = inspect.signature(Workers.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Designation" in params, "Missing parameter 'Designation'"

def test_workers_has_name():
    assert hasattr(Workers, "name")
    descriptor = None
    for klass in Workers.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_workers_has_salary():
    assert hasattr(Workers, "salary")
    descriptor = None
    for klass in Workers.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_workers_has_Password():
    assert hasattr(Workers, "Password")
    descriptor = None
    for klass in Workers.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_workers_has_Designation():
    assert hasattr(Workers, "Designation")
    descriptor = None
    for klass in Workers.__mro__:
        if "Designation" in klass.__dict__:
            descriptor = klass.__dict__["Designation"]
            break
    assert isinstance(descriptor, property)



def test_customers_is_not_abstract():
    assert not inspect.isabstract(customers)


def test_customers_constructor_exists():
    assert callable(customers.__init__)


def test_customers_constructor_args():
    sig = inspect.signature(customers.__init__)
    params = list(sig.parameters.keys())
    assert "shoppingCost" in params, "Missing parameter 'shoppingCost'"
    assert "name" in params, "Missing parameter 'name'"

def test_customers_has_shoppingCost():
    assert hasattr(customers, "shoppingCost")
    descriptor = None
    for klass in customers.__mro__:
        if "shoppingCost" in klass.__dict__:
            descriptor = klass.__dict__["shoppingCost"]
            break
    assert isinstance(descriptor, property)

def test_customers_has_name():
    assert hasattr(customers, "name")
    descriptor = None
    for klass in customers.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_accessories_is_not_abstract():
    assert not inspect.isabstract(Accessories)


def test_accessories_constructor_exists():
    assert callable(Accessories.__init__)


def test_accessories_constructor_args():
    sig = inspect.signature(Accessories.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"

def test_accessories_has_name():
    assert hasattr(Accessories, "name")
    descriptor = None
    for klass in Accessories.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_accessories_has_price():
    assert hasattr(Accessories, "price")
    descriptor = None
    for klass in Accessories.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_devices_is_not_abstract():
    assert not inspect.isabstract(Devices)


def test_devices_constructor_exists():
    assert callable(Devices.__init__)


def test_devices_constructor_args():
    sig = inspect.signature(Devices.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"

def test_devices_has_price():
    assert hasattr(Devices, "price")
    descriptor = None
    for klass in Devices.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_devices_has_name():
    assert hasattr(Devices, "name")
    descriptor = None
    for klass in Devices.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_computerparts_is_not_abstract():
    assert not inspect.isabstract(ComputerParts)


def test_computerparts_constructor_exists():
    assert callable(ComputerParts.__init__)


def test_computerparts_constructor_args():
    sig = inspect.signature(ComputerParts.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"

def test_computerparts_has_name():
    assert hasattr(ComputerParts, "name")
    descriptor = None
    for klass in ComputerParts.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_computerparts_has_price():
    assert hasattr(ComputerParts, "price")
    descriptor = None
    for klass in ComputerParts.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_items_is_not_abstract():
    assert not inspect.isabstract(Items)


def test_items_constructor_exists():
    assert callable(Items.__init__)


def test_items_constructor_args():
    sig = inspect.signature(Items.__init__)
    params = list(sig.parameters.keys())
    assert "ArrayList_devices_" in params, "Missing parameter 'ArrayList_devices_'"
    assert "ArrayList_accessories_" in params, "Missing parameter 'ArrayList_accessories_'"
    assert "ArrayList_ComputerParts_" in params, "Missing parameter 'ArrayList_ComputerParts_'"
    assert "typeOfItems" in params, "Missing parameter 'typeOfItems'"

def test_items_has_ArrayList_devices_():
    assert hasattr(Items, "ArrayList_devices_")
    descriptor = None
    for klass in Items.__mro__:
        if "ArrayList_devices_" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList_devices_"]
            break
    assert isinstance(descriptor, property)

def test_items_has_ArrayList_accessories_():
    assert hasattr(Items, "ArrayList_accessories_")
    descriptor = None
    for klass in Items.__mro__:
        if "ArrayList_accessories_" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList_accessories_"]
            break
    assert isinstance(descriptor, property)

def test_items_has_ArrayList_ComputerParts_():
    assert hasattr(Items, "ArrayList_ComputerParts_")
    descriptor = None
    for klass in Items.__mro__:
        if "ArrayList_ComputerParts_" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList_ComputerParts_"]
            break
    assert isinstance(descriptor, property)

def test_items_has_typeOfItems():
    assert hasattr(Items, "typeOfItems")
    descriptor = None
    for klass in Items.__mro__:
        if "typeOfItems" in klass.__dict__:
            descriptor = klass.__dict__["typeOfItems"]
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
Admin__strategy = st.builds(
    Admin_,
    ArrayList_worker_=
        safe_text,
    Password=
        safe_text,
    ArrayList_member_=
        safe_text
)
member_strategy = st.builds(
    member,
    name=
        safe_text,
    password=
        safe_text,
    memberType=
        safe_text
)
Workers_strategy = st.builds(
    Workers,
    name=
        safe_text,
    salary=
        st.integers(),
    Password=
        safe_text,
    Designation=
        safe_text
)
customers_strategy = st.builds(
    customers,
    shoppingCost=
        st.integers(),
    name=
        safe_text
)
Accessories_strategy = st.builds(
    Accessories,
    name=
        safe_text,
    price=
        st.integers()
)
Devices_strategy = st.builds(
    Devices,
    price=
        st.integers(),
    name=
        safe_text
)
ComputerParts_strategy = st.builds(
    ComputerParts,
    name=
        safe_text,
    price=
        st.integers()
)
Items_strategy = st.builds(
    Items,
    ArrayList_devices_=
        safe_text,
    ArrayList_accessories_=
        safe_text,
    ArrayList_ComputerParts_=
        safe_text,
    typeOfItems=
        st.integers()
)

@given(instance=Admin__strategy)
@settings(max_examples=50)
def test_admin__instantiation(instance):
    assert isinstance(instance, Admin_)



@given(instance=Admin__strategy)
def test_admin__ArrayList_worker__setter(instance):
    original = instance.ArrayList_worker_
    instance.ArrayList_worker_ = original
    assert instance.ArrayList_worker_ == original



@given(instance=Admin__strategy)
def test_admin__Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Admin__strategy)
def test_admin__ArrayList_member__setter(instance):
    original = instance.ArrayList_member_
    instance.ArrayList_member_ = original
    assert instance.ArrayList_member_ == original

@given(instance=member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, member)



@given(instance=member_strategy)
def test_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=member_strategy)
def test_member_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=member_strategy)
def test_member_memberType_setter(instance):
    original = instance.memberType
    instance.memberType = original
    assert instance.memberType == original

@given(instance=Workers_strategy)
@settings(max_examples=50)
def test_workers_instantiation(instance):
    assert isinstance(instance, Workers)



@given(instance=Workers_strategy)
def test_workers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Workers_strategy)
def test_workers_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=Workers_strategy)
def test_workers_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Workers_strategy)
def test_workers_Designation_setter(instance):
    original = instance.Designation
    instance.Designation = original
    assert instance.Designation == original

@given(instance=customers_strategy)
@settings(max_examples=50)
def test_customers_instantiation(instance):
    assert isinstance(instance, customers)



@given(instance=customers_strategy)
def test_customers_shoppingCost_setter(instance):
    original = instance.shoppingCost
    instance.shoppingCost = original
    assert instance.shoppingCost == original



@given(instance=customers_strategy)
def test_customers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Accessories_strategy)
@settings(max_examples=50)
def test_accessories_instantiation(instance):
    assert isinstance(instance, Accessories)



@given(instance=Accessories_strategy)
def test_accessories_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Accessories_strategy)
def test_accessories_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Devices_strategy)
@settings(max_examples=50)
def test_devices_instantiation(instance):
    assert isinstance(instance, Devices)



@given(instance=Devices_strategy)
def test_devices_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Devices_strategy)
def test_devices_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ComputerParts_strategy)
@settings(max_examples=50)
def test_computerparts_instantiation(instance):
    assert isinstance(instance, ComputerParts)



@given(instance=ComputerParts_strategy)
def test_computerparts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ComputerParts_strategy)
def test_computerparts_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Items_strategy)
@settings(max_examples=50)
def test_items_instantiation(instance):
    assert isinstance(instance, Items)



@given(instance=Items_strategy)
def test_items_ArrayList_devices__setter(instance):
    original = instance.ArrayList_devices_
    instance.ArrayList_devices_ = original
    assert instance.ArrayList_devices_ == original



@given(instance=Items_strategy)
def test_items_ArrayList_accessories__setter(instance):
    original = instance.ArrayList_accessories_
    instance.ArrayList_accessories_ = original
    assert instance.ArrayList_accessories_ == original



@given(instance=Items_strategy)
def test_items_ArrayList_ComputerParts__setter(instance):
    original = instance.ArrayList_ComputerParts_
    instance.ArrayList_ComputerParts_ = original
    assert instance.ArrayList_ComputerParts_ == original



@given(instance=Items_strategy)
def test_items_typeOfItems_setter(instance):
    original = instance.typeOfItems
    instance.typeOfItems = original
    assert instance.typeOfItems == original
