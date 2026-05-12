import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    User,
    Order,
    Stock,
    Shopping_cart,
    Product,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "Surname" in params, "Missing parameter 'Surname'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_person_has_Surname():
    assert hasattr(Person, "Surname")
    descriptor = None
    for klass in Person.__mro__:
        if "Surname" in klass.__dict__:
            descriptor = klass.__dict__["Surname"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Address():
    assert hasattr(Person, "Address")
    descriptor = None
    for klass in Person.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Name():
    assert hasattr(Person, "Name")
    descriptor = None
    for klass in Person.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Email():
    assert hasattr(Person, "Email")
    descriptor = None
    for klass in Person.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_user_has_Password():
    assert hasattr(User, "Password")
    descriptor = None
    for klass in User.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_UserID():
    assert hasattr(User, "UserID")
    descriptor = None
    for klass in User.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_user_has_UserName():
    assert hasattr(User, "UserName")
    descriptor = None
    for klass in User.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Customer" in params, "Missing parameter 'Customer'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "items" in params, "Missing parameter 'items'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"

def test_order_has_Customer():
    assert hasattr(Order, "Customer")
    descriptor = None
    for klass in Order.__mro__:
        if "Customer" in klass.__dict__:
            descriptor = klass.__dict__["Customer"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Date():
    assert hasattr(Order, "Date")
    descriptor = None
    for klass in Order.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_order_has_items():
    assert hasattr(Order, "items")
    descriptor = None
    for klass in Order.__mro__:
        if "items" in klass.__dict__:
            descriptor = klass.__dict__["items"]
            break
    assert isinstance(descriptor, property)

def test_order_has_OrderID():
    assert hasattr(Order, "OrderID")
    descriptor = None
    for klass in Order.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)



def test_stock_is_not_abstract():
    assert not inspect.isabstract(Stock)


def test_stock_constructor_exists():
    assert callable(Stock.__init__)


def test_stock_constructor_args():
    sig = inspect.signature(Stock.__init__)
    params = list(sig.parameters.keys())
    assert "Items" in params, "Missing parameter 'Items'"

def test_stock_has_Items():
    assert hasattr(Stock, "Items")
    descriptor = None
    for klass in Stock.__mro__:
        if "Items" in klass.__dict__:
            descriptor = klass.__dict__["Items"]
            break
    assert isinstance(descriptor, property)



def test_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_cart)


def test_shopping_cart_constructor_exists():
    assert callable(Shopping_cart.__init__)


def test_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_cart.__init__)
    params = list(sig.parameters.keys())
    assert "Products" in params, "Missing parameter 'Products'"

def test_shopping_cart_has_Products():
    assert hasattr(Shopping_cart, "Products")
    descriptor = None
    for klass in Shopping_cart.__mro__:
        if "Products" in klass.__dict__:
            descriptor = klass.__dict__["Products"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_product_has_description():
    assert hasattr(Product, "description")
    descriptor = None
    for klass in Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_product_has_name():
    assert hasattr(Product, "name")
    descriptor = None
    for klass in Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_product_has_price():
    assert hasattr(Product, "price")
    descriptor = None
    for klass in Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_product_has_ProductID():
    assert hasattr(Product, "ProductID")
    descriptor = None
    for klass in Product.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_product_has_quantity():
    assert hasattr(Product, "quantity")
    descriptor = None
    for klass in Product.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
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
Person_strategy = st.builds(
    Person,
    Surname=
        safe_text,
    Address=
        safe_text,
    Name=
        safe_text,
    Email=
        safe_text
)
User_strategy = st.builds(
    User,
    Password=
        safe_text,
    UserID=
        st.integers(),
    UserName=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Customer=
        st.none(),
    Date=
        safe_text,
    items=
        st.none(),
    OrderID=
        st.integers()
)
Stock_strategy = st.builds(
    Stock,
    Items=
        safe_text
)
Shopping_cart_strategy = st.builds(
    Shopping_cart,
    Products=
        safe_text
)
Product_strategy = st.builds(
    Product,
    description=
        safe_text,
    name=
        safe_text,
    price=
        st.integers(),
    ProductID=
        st.integers(),
    quantity=
        st.integers()
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_Surname_setter(instance):
    original = instance.Surname
    instance.Surname = original
    assert instance.Surname == original



@given(instance=Person_strategy)
def test_person_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Person_strategy)
def test_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Person_strategy)
def test_person_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_user_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=User_strategy)
def test_user_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Customer_setter(instance):
    original = instance.Customer
    instance.Customer = original
    assert instance.Customer == original



@given(instance=Order_strategy)
def test_order_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Order_strategy)
def test_order_items_setter(instance):
    original = instance.items
    instance.items = original
    assert instance.items == original



@given(instance=Order_strategy)
def test_order_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original

@given(instance=Stock_strategy)
@settings(max_examples=50)
def test_stock_instantiation(instance):
    assert isinstance(instance, Stock)



@given(instance=Stock_strategy)
def test_stock_Items_setter(instance):
    original = instance.Items
    instance.Items = original
    assert instance.Items == original

@given(instance=Shopping_cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_cart)



@given(instance=Shopping_cart_strategy)
def test_shopping_cart_Products_setter(instance):
    original = instance.Products
    instance.Products = original
    assert instance.Products == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Product_strategy)
def test_product_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Product_strategy)
def test_product_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original
