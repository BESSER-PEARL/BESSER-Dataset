import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Store,
    Admin_,
    member,
    Employee,
    customers,
    food,
    Appliacne,
    Furniture,
    Product,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_store_is_not_abstract():
    assert not inspect.isabstract(Store)


def test_store_constructor_exists():
    assert callable(Store.__init__)


def test_store_constructor_args():
    sig = inspect.signature(Store.__init__)
    params = list(sig.parameters.keys())
    assert "SName" in params, "Missing parameter 'SName'"
    assert "Sid" in params, "Missing parameter 'Sid'"

def test_store_has_SName():
    assert hasattr(Store, "SName")
    descriptor = None
    for klass in Store.__mro__:
        if "SName" in klass.__dict__:
            descriptor = klass.__dict__["SName"]
            break
    assert isinstance(descriptor, property)

def test_store_has_Sid():
    assert hasattr(Store, "Sid")
    descriptor = None
    for klass in Store.__mro__:
        if "Sid" in klass.__dict__:
            descriptor = klass.__dict__["Sid"]
            break
    assert isinstance(descriptor, property)



def test_admin__is_not_abstract():
    assert not inspect.isabstract(Admin_)


def test_admin__constructor_exists():
    assert callable(Admin_.__init__)


def test_admin__constructor_args():
    sig = inspect.signature(Admin_.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "ArrayList_member_" in params, "Missing parameter 'ArrayList_member_'"
    assert "ArryList_Employee" in params, "Missing parameter 'ArryList_Employee'"

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

def test_admin__has_ArryList_Employee():
    assert hasattr(Admin_, "ArryList_Employee")
    descriptor = None
    for klass in Admin_.__mro__:
        if "ArryList_Employee" in klass.__dict__:
            descriptor = klass.__dict__["ArryList_Employee"]
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



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Designation" in params, "Missing parameter 'Designation'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "name" in params, "Missing parameter 'name'"

def test_employee_has_Designation():
    assert hasattr(Employee, "Designation")
    descriptor = None
    for klass in Employee.__mro__:
        if "Designation" in klass.__dict__:
            descriptor = klass.__dict__["Designation"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_salary():
    assert hasattr(Employee, "salary")
    descriptor = None
    for klass in Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Password():
    assert hasattr(Employee, "Password")
    descriptor = None
    for klass in Employee.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_name():
    assert hasattr(Employee, "name")
    descriptor = None
    for klass in Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_food_is_not_abstract():
    assert not inspect.isabstract(food)


def test_food_constructor_exists():
    assert callable(food.__init__)


def test_food_constructor_args():
    sig = inspect.signature(food.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"

def test_food_has_name():
    assert hasattr(food, "name")
    descriptor = None
    for klass in food.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_food_has_price():
    assert hasattr(food, "price")
    descriptor = None
    for klass in food.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_appliacne_is_not_abstract():
    assert not inspect.isabstract(Appliacne)


def test_appliacne_constructor_exists():
    assert callable(Appliacne.__init__)


def test_appliacne_constructor_args():
    sig = inspect.signature(Appliacne.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"

def test_appliacne_has_price():
    assert hasattr(Appliacne, "price")
    descriptor = None
    for klass in Appliacne.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_appliacne_has_name():
    assert hasattr(Appliacne, "name")
    descriptor = None
    for klass in Appliacne.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_furniture_is_not_abstract():
    assert not inspect.isabstract(Furniture)


def test_furniture_constructor_exists():
    assert callable(Furniture.__init__)


def test_furniture_constructor_args():
    sig = inspect.signature(Furniture.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"

def test_furniture_has_name():
    assert hasattr(Furniture, "name")
    descriptor = None
    for klass in Furniture.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_furniture_has_price():
    assert hasattr(Furniture, "price")
    descriptor = None
    for klass in Furniture.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "ArrayList_appliance_" in params, "Missing parameter 'ArrayList_appliance_'"
    assert "ArrayList_food_" in params, "Missing parameter 'ArrayList_food_'"
    assert "ArrayList_furniture_" in params, "Missing parameter 'ArrayList_furniture_'"
    assert "typeOfItems" in params, "Missing parameter 'typeOfItems'"

def test_product_has_ArrayList_appliance_():
    assert hasattr(Product, "ArrayList_appliance_")
    descriptor = None
    for klass in Product.__mro__:
        if "ArrayList_appliance_" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList_appliance_"]
            break
    assert isinstance(descriptor, property)

def test_product_has_ArrayList_food_():
    assert hasattr(Product, "ArrayList_food_")
    descriptor = None
    for klass in Product.__mro__:
        if "ArrayList_food_" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList_food_"]
            break
    assert isinstance(descriptor, property)

def test_product_has_ArrayList_furniture_():
    assert hasattr(Product, "ArrayList_furniture_")
    descriptor = None
    for klass in Product.__mro__:
        if "ArrayList_furniture_" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList_furniture_"]
            break
    assert isinstance(descriptor, property)

def test_product_has_typeOfItems():
    assert hasattr(Product, "typeOfItems")
    descriptor = None
    for klass in Product.__mro__:
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
Store_strategy = st.builds(
    Store,
    SName=
        safe_text,
    Sid=
        st.integers()
)
Admin__strategy = st.builds(
    Admin_,
    Password=
        safe_text,
    ArrayList_member_=
        safe_text,
    ArryList_Employee=
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
Employee_strategy = st.builds(
    Employee,
    Designation=
        safe_text,
    salary=
        st.integers(),
    Password=
        safe_text,
    name=
        safe_text
)
customers_strategy = st.builds(
    customers,
    shoppingCost=
        st.integers(),
    name=
        safe_text
)
food_strategy = st.builds(
    food,
    name=
        safe_text,
    price=
        st.integers()
)
Appliacne_strategy = st.builds(
    Appliacne,
    price=
        st.integers(),
    name=
        safe_text
)
Furniture_strategy = st.builds(
    Furniture,
    name=
        safe_text,
    price=
        st.integers()
)
Product_strategy = st.builds(
    Product,
    ArrayList_appliance_=
        safe_text,
    ArrayList_food_=
        safe_text,
    ArrayList_furniture_=
        safe_text,
    typeOfItems=
        st.integers()
)

@given(instance=Store_strategy)
@settings(max_examples=50)
def test_store_instantiation(instance):
    assert isinstance(instance, Store)



@given(instance=Store_strategy)
def test_store_SName_setter(instance):
    original = instance.SName
    instance.SName = original
    assert instance.SName == original



@given(instance=Store_strategy)
def test_store_Sid_setter(instance):
    original = instance.Sid
    instance.Sid = original
    assert instance.Sid == original

@given(instance=Admin__strategy)
@settings(max_examples=50)
def test_admin__instantiation(instance):
    assert isinstance(instance, Admin_)



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



@given(instance=Admin__strategy)
def test_admin__ArryList_Employee_setter(instance):
    original = instance.ArryList_Employee
    instance.ArryList_Employee = original
    assert instance.ArryList_Employee == original

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

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_Designation_setter(instance):
    original = instance.Designation
    instance.Designation = original
    assert instance.Designation == original



@given(instance=Employee_strategy)
def test_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=Employee_strategy)
def test_employee_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Employee_strategy)
def test_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=food_strategy)
@settings(max_examples=50)
def test_food_instantiation(instance):
    assert isinstance(instance, food)



@given(instance=food_strategy)
def test_food_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=food_strategy)
def test_food_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Appliacne_strategy)
@settings(max_examples=50)
def test_appliacne_instantiation(instance):
    assert isinstance(instance, Appliacne)



@given(instance=Appliacne_strategy)
def test_appliacne_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Appliacne_strategy)
def test_appliacne_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Furniture_strategy)
@settings(max_examples=50)
def test_furniture_instantiation(instance):
    assert isinstance(instance, Furniture)



@given(instance=Furniture_strategy)
def test_furniture_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Furniture_strategy)
def test_furniture_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_ArrayList_appliance__setter(instance):
    original = instance.ArrayList_appliance_
    instance.ArrayList_appliance_ = original
    assert instance.ArrayList_appliance_ == original



@given(instance=Product_strategy)
def test_product_ArrayList_food__setter(instance):
    original = instance.ArrayList_food_
    instance.ArrayList_food_ = original
    assert instance.ArrayList_food_ == original



@given(instance=Product_strategy)
def test_product_ArrayList_furniture__setter(instance):
    original = instance.ArrayList_furniture_
    instance.ArrayList_furniture_ = original
    assert instance.ArrayList_furniture_ == original



@given(instance=Product_strategy)
def test_product_typeOfItems_setter(instance):
    original = instance.typeOfItems
    instance.typeOfItems = original
    assert instance.typeOfItems == original
