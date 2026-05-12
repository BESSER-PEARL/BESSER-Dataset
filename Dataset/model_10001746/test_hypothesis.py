import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Shopping_Cart,
    Order,
    Double_Interface,
    ClientAccount,
    User,
    Product,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_Cart)


def test_shopping_cart_constructor_exists():
    assert callable(Shopping_Cart.__init__)


def test_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_Cart.__init__)
    params = list(sig.parameters.keys())
    assert "ProductPurchased" in params, "Missing parameter 'ProductPurchased'"

def test_shopping_cart_has_ProductPurchased():
    assert hasattr(Shopping_Cart, "ProductPurchased")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "ProductPurchased" in klass.__dict__:
            descriptor = klass.__dict__["ProductPurchased"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Products" in params, "Missing parameter 'Products'"
    assert "PaymentMethod" in params, "Missing parameter 'PaymentMethod'"
    assert "HomeAddress" in params, "Missing parameter 'HomeAddress'"
    assert "OrderNumber" in params, "Missing parameter 'OrderNumber'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "Date" in params, "Missing parameter 'Date'"

def test_order_has_Products():
    assert hasattr(Order, "Products")
    descriptor = None
    for klass in Order.__mro__:
        if "Products" in klass.__dict__:
            descriptor = klass.__dict__["Products"]
            break
    assert isinstance(descriptor, property)

def test_order_has_PaymentMethod():
    assert hasattr(Order, "PaymentMethod")
    descriptor = None
    for klass in Order.__mro__:
        if "PaymentMethod" in klass.__dict__:
            descriptor = klass.__dict__["PaymentMethod"]
            break
    assert isinstance(descriptor, property)

def test_order_has_HomeAddress():
    assert hasattr(Order, "HomeAddress")
    descriptor = None
    for klass in Order.__mro__:
        if "HomeAddress" in klass.__dict__:
            descriptor = klass.__dict__["HomeAddress"]
            break
    assert isinstance(descriptor, property)

def test_order_has_OrderNumber():
    assert hasattr(Order, "OrderNumber")
    descriptor = None
    for klass in Order.__mro__:
        if "OrderNumber" in klass.__dict__:
            descriptor = klass.__dict__["OrderNumber"]
            break
    assert isinstance(descriptor, property)

def test_order_has_CustomerName():
    assert hasattr(Order, "CustomerName")
    descriptor = None
    for klass in Order.__mro__:
        if "CustomerName" in klass.__dict__:
            descriptor = klass.__dict__["CustomerName"]
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



def test_double_interface_is_not_abstract():
    assert not inspect.isabstract(Double_Interface)


def test_double_interface_constructor_exists():
    assert callable(Double_Interface.__init__)


def test_double_interface_constructor_args():
    sig = inspect.signature(Double_Interface.__init__)
    params = list(sig.parameters.keys())



def test_clientaccount_is_not_abstract():
    assert not inspect.isabstract(ClientAccount)


def test_clientaccount_constructor_exists():
    assert callable(ClientAccount.__init__)


def test_clientaccount_constructor_args():
    sig = inspect.signature(ClientAccount.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"

def test_clientaccount_has_Password():
    assert hasattr(ClientAccount, "Password")
    descriptor = None
    for klass in ClientAccount.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Age" in params, "Missing parameter 'Age'"
    assert "HomeAddress" in params, "Missing parameter 'HomeAddress'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Surname" in params, "Missing parameter 'Surname'"

def test_user_has_Age():
    assert hasattr(User, "Age")
    descriptor = None
    for klass in User.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_user_has_HomeAddress():
    assert hasattr(User, "HomeAddress")
    descriptor = None
    for klass in User.__mro__:
        if "HomeAddress" in klass.__dict__:
            descriptor = klass.__dict__["HomeAddress"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Name():
    assert hasattr(User, "Name")
    descriptor = None
    for klass in User.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Email():
    assert hasattr(User, "Email")
    descriptor = None
    for klass in User.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Surname():
    assert hasattr(User, "Surname")
    descriptor = None
    for klass in User.__mro__:
        if "Surname" in klass.__dict__:
            descriptor = klass.__dict__["Surname"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "ProductDescription" in params, "Missing parameter 'ProductDescription'"
    assert "ProductName" in params, "Missing parameter 'ProductName'"
    assert "ProductType" in params, "Missing parameter 'ProductType'"
    assert "ProductPrice" in params, "Missing parameter 'ProductPrice'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "ProductImage" in params, "Missing parameter 'ProductImage'"

def test_product_has_ProductDescription():
    assert hasattr(Product, "ProductDescription")
    descriptor = None
    for klass in Product.__mro__:
        if "ProductDescription" in klass.__dict__:
            descriptor = klass.__dict__["ProductDescription"]
            break
    assert isinstance(descriptor, property)

def test_product_has_ProductName():
    assert hasattr(Product, "ProductName")
    descriptor = None
    for klass in Product.__mro__:
        if "ProductName" in klass.__dict__:
            descriptor = klass.__dict__["ProductName"]
            break
    assert isinstance(descriptor, property)

def test_product_has_ProductType():
    assert hasattr(Product, "ProductType")
    descriptor = None
    for klass in Product.__mro__:
        if "ProductType" in klass.__dict__:
            descriptor = klass.__dict__["ProductType"]
            break
    assert isinstance(descriptor, property)

def test_product_has_ProductPrice():
    assert hasattr(Product, "ProductPrice")
    descriptor = None
    for klass in Product.__mro__:
        if "ProductPrice" in klass.__dict__:
            descriptor = klass.__dict__["ProductPrice"]
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

def test_product_has_ProductImage():
    assert hasattr(Product, "ProductImage")
    descriptor = None
    for klass in Product.__mro__:
        if "ProductImage" in klass.__dict__:
            descriptor = klass.__dict__["ProductImage"]
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
Shopping_Cart_strategy = st.builds(
    Shopping_Cart,
    ProductPurchased=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Products=
        st.none(),
    PaymentMethod=
        safe_text,
    HomeAddress=
        st.none(),
    OrderNumber=
        st.integers(),
    CustomerName=
        st.none(),
    Date=
        safe_text
)
Double_Interface_strategy = st.builds(
    Double_Interface,
)
ClientAccount_strategy = st.builds(
    ClientAccount,
    Password=
        safe_text
)
User_strategy = st.builds(
    User,
    Age=
        st.integers(),
    HomeAddress=
        safe_text,
    Name=
        safe_text,
    Email=
        safe_text,
    Surname=
        safe_text
)
Product_strategy = st.builds(
    Product,
    ProductDescription=
        safe_text,
    ProductName=
        safe_text,
    ProductType=
        safe_text,
    ProductPrice=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    ProductID=
        st.integers(),
    ProductImage=
        safe_text
)

@given(instance=Shopping_Cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart)



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_ProductPurchased_setter(instance):
    original = instance.ProductPurchased
    instance.ProductPurchased = original
    assert instance.ProductPurchased == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Products_setter(instance):
    original = instance.Products
    instance.Products = original
    assert instance.Products == original



@given(instance=Order_strategy)
def test_order_PaymentMethod_setter(instance):
    original = instance.PaymentMethod
    instance.PaymentMethod = original
    assert instance.PaymentMethod == original



@given(instance=Order_strategy)
def test_order_HomeAddress_setter(instance):
    original = instance.HomeAddress
    instance.HomeAddress = original
    assert instance.HomeAddress == original



@given(instance=Order_strategy)
def test_order_OrderNumber_setter(instance):
    original = instance.OrderNumber
    instance.OrderNumber = original
    assert instance.OrderNumber == original



@given(instance=Order_strategy)
def test_order_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=Order_strategy)
def test_order_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Double_Interface_strategy)
@settings(max_examples=50)
def test_double_interface_instantiation(instance):
    assert isinstance(instance, Double_Interface)

@given(instance=ClientAccount_strategy)
@settings(max_examples=50)
def test_clientaccount_instantiation(instance):
    assert isinstance(instance, ClientAccount)



@given(instance=ClientAccount_strategy)
def test_clientaccount_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=User_strategy)
def test_user_HomeAddress_setter(instance):
    original = instance.HomeAddress
    instance.HomeAddress = original
    assert instance.HomeAddress == original



@given(instance=User_strategy)
def test_user_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=User_strategy)
def test_user_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=User_strategy)
def test_user_Surname_setter(instance):
    original = instance.Surname
    instance.Surname = original
    assert instance.Surname == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_ProductDescription_setter(instance):
    original = instance.ProductDescription
    instance.ProductDescription = original
    assert instance.ProductDescription == original



@given(instance=Product_strategy)
def test_product_ProductName_setter(instance):
    original = instance.ProductName
    instance.ProductName = original
    assert instance.ProductName == original



@given(instance=Product_strategy)
def test_product_ProductType_setter(instance):
    original = instance.ProductType
    instance.ProductType = original
    assert instance.ProductType == original



@given(instance=Product_strategy)
def test_product_ProductPrice_setter(instance):
    original = instance.ProductPrice
    instance.ProductPrice = original
    assert instance.ProductPrice == original



@given(instance=Product_strategy)
def test_product_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Product_strategy)
def test_product_ProductImage_setter(instance):
    original = instance.ProductImage
    instance.ProductImage = original
    assert instance.ProductImage == original
