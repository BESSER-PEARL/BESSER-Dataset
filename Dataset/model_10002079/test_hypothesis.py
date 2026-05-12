import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Shopping,
    OrderDetails,
    ShippingInfo,
    Order,
    ShoppingCart,
    Administrator,
    Customer,
    Users,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shopping_is_not_abstract():
    assert not inspect.isabstract(Shopping)


def test_shopping_constructor_exists():
    assert callable(Shopping.__init__)


def test_shopping_constructor_args():
    sig = inspect.signature(Shopping.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Identity" in params, "Missing parameter 'Identity'"
    assert "Location" in params, "Missing parameter 'Location'"

def test_shopping_has_Name():
    assert hasattr(Shopping, "Name")
    descriptor = None
    for klass in Shopping.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_shopping_has_Identity():
    assert hasattr(Shopping, "Identity")
    descriptor = None
    for klass in Shopping.__mro__:
        if "Identity" in klass.__dict__:
            descriptor = klass.__dict__["Identity"]
            break
    assert isinstance(descriptor, property)

def test_shopping_has_Location():
    assert hasattr(Shopping, "Location")
    descriptor = None
    for klass in Shopping.__mro__:
        if "Location" in klass.__dict__:
            descriptor = klass.__dict__["Location"]
            break
    assert isinstance(descriptor, property)



def test_orderdetails_is_not_abstract():
    assert not inspect.isabstract(OrderDetails)


def test_orderdetails_constructor_exists():
    assert callable(OrderDetails.__init__)


def test_orderdetails_constructor_args():
    sig = inspect.signature(OrderDetails.__init__)
    params = list(sig.parameters.keys())
    assert "ProductName" in params, "Missing parameter 'ProductName'"
    assert "UnitCost" in params, "Missing parameter 'UnitCost'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "SubTotal" in params, "Missing parameter 'SubTotal'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"

def test_orderdetails_has_ProductName():
    assert hasattr(OrderDetails, "ProductName")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "ProductName" in klass.__dict__:
            descriptor = klass.__dict__["ProductName"]
            break
    assert isinstance(descriptor, property)

def test_orderdetails_has_UnitCost():
    assert hasattr(OrderDetails, "UnitCost")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "UnitCost" in klass.__dict__:
            descriptor = klass.__dict__["UnitCost"]
            break
    assert isinstance(descriptor, property)

def test_orderdetails_has_OrderID():
    assert hasattr(OrderDetails, "OrderID")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_orderdetails_has_Quantity():
    assert hasattr(OrderDetails, "Quantity")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_orderdetails_has_SubTotal():
    assert hasattr(OrderDetails, "SubTotal")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "SubTotal" in klass.__dict__:
            descriptor = klass.__dict__["SubTotal"]
            break
    assert isinstance(descriptor, property)

def test_orderdetails_has_ProductID():
    assert hasattr(OrderDetails, "ProductID")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)



def test_shippinginfo_is_not_abstract():
    assert not inspect.isabstract(ShippingInfo)


def test_shippinginfo_constructor_exists():
    assert callable(ShippingInfo.__init__)


def test_shippinginfo_constructor_args():
    sig = inspect.signature(ShippingInfo.__init__)
    params = list(sig.parameters.keys())
    assert "ShippingID" in params, "Missing parameter 'ShippingID'"
    assert "ShippingRegionID" in params, "Missing parameter 'ShippingRegionID'"
    assert "ShippingCost" in params, "Missing parameter 'ShippingCost'"
    assert "ShippingType" in params, "Missing parameter 'ShippingType'"

def test_shippinginfo_has_ShippingID():
    assert hasattr(ShippingInfo, "ShippingID")
    descriptor = None
    for klass in ShippingInfo.__mro__:
        if "ShippingID" in klass.__dict__:
            descriptor = klass.__dict__["ShippingID"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_ShippingRegionID():
    assert hasattr(ShippingInfo, "ShippingRegionID")
    descriptor = None
    for klass in ShippingInfo.__mro__:
        if "ShippingRegionID" in klass.__dict__:
            descriptor = klass.__dict__["ShippingRegionID"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_ShippingCost():
    assert hasattr(ShippingInfo, "ShippingCost")
    descriptor = None
    for klass in ShippingInfo.__mro__:
        if "ShippingCost" in klass.__dict__:
            descriptor = klass.__dict__["ShippingCost"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_ShippingType():
    assert hasattr(ShippingInfo, "ShippingType")
    descriptor = None
    for klass in ShippingInfo.__mro__:
        if "ShippingType" in klass.__dict__:
            descriptor = klass.__dict__["ShippingType"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"
    assert "DateShipped" in params, "Missing parameter 'DateShipped'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "CustomerID" in params, "Missing parameter 'CustomerID'"
    assert "DateCreated" in params, "Missing parameter 'DateCreated'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "ShippingID" in params, "Missing parameter 'ShippingID'"

def test_order_has_Status():
    assert hasattr(Order, "Status")
    descriptor = None
    for klass in Order.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_order_has_DateShipped():
    assert hasattr(Order, "DateShipped")
    descriptor = None
    for klass in Order.__mro__:
        if "DateShipped" in klass.__dict__:
            descriptor = klass.__dict__["DateShipped"]
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

def test_order_has_CustomerID():
    assert hasattr(Order, "CustomerID")
    descriptor = None
    for klass in Order.__mro__:
        if "CustomerID" in klass.__dict__:
            descriptor = klass.__dict__["CustomerID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_DateCreated():
    assert hasattr(Order, "DateCreated")
    descriptor = None
    for klass in Order.__mro__:
        if "DateCreated" in klass.__dict__:
            descriptor = klass.__dict__["DateCreated"]
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

def test_order_has_ShippingID():
    assert hasattr(Order, "ShippingID")
    descriptor = None
    for klass in Order.__mro__:
        if "ShippingID" in klass.__dict__:
            descriptor = klass.__dict__["ShippingID"]
            break
    assert isinstance(descriptor, property)



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "DateAdded" in params, "Missing parameter 'DateAdded'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "CartID" in params, "Missing parameter 'CartID'"

def test_shoppingcart_has_ProductID():
    assert hasattr(ShoppingCart, "ProductID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_DateAdded():
    assert hasattr(ShoppingCart, "DateAdded")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "DateAdded" in klass.__dict__:
            descriptor = klass.__dict__["DateAdded"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_Quantity():
    assert hasattr(ShoppingCart, "Quantity")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_CartID():
    assert hasattr(ShoppingCart, "CartID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "CartID" in klass.__dict__:
            descriptor = klass.__dict__["CartID"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "AdminName" in params, "Missing parameter 'AdminName'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_administrator_has_AdminName():
    assert hasattr(Administrator, "AdminName")
    descriptor = None
    for klass in Administrator.__mro__:
        if "AdminName" in klass.__dict__:
            descriptor = klass.__dict__["AdminName"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Email():
    assert hasattr(Administrator, "Email")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "CreditCartInfo" in params, "Missing parameter 'CreditCartInfo'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "AccountBalance" in params, "Missing parameter 'AccountBalance'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "ShippingInfo" in params, "Missing parameter 'ShippingInfo'"

def test_customer_has_CreditCartInfo():
    assert hasattr(Customer, "CreditCartInfo")
    descriptor = None
    for klass in Customer.__mro__:
        if "CreditCartInfo" in klass.__dict__:
            descriptor = klass.__dict__["CreditCartInfo"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_CustomerName():
    assert hasattr(Customer, "CustomerName")
    descriptor = None
    for klass in Customer.__mro__:
        if "CustomerName" in klass.__dict__:
            descriptor = klass.__dict__["CustomerName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_AccountBalance():
    assert hasattr(Customer, "AccountBalance")
    descriptor = None
    for klass in Customer.__mro__:
        if "AccountBalance" in klass.__dict__:
            descriptor = klass.__dict__["AccountBalance"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Address():
    assert hasattr(Customer, "Address")
    descriptor = None
    for klass in Customer.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Email():
    assert hasattr(Customer, "Email")
    descriptor = None
    for klass in Customer.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_ShippingInfo():
    assert hasattr(Customer, "ShippingInfo")
    descriptor = None
    for klass in Customer.__mro__:
        if "ShippingInfo" in klass.__dict__:
            descriptor = klass.__dict__["ShippingInfo"]
            break
    assert isinstance(descriptor, property)



def test_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_users_constructor_exists():
    assert callable(Users.__init__)


def test_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "RegisterDate" in params, "Missing parameter 'RegisterDate'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "LoginStatus" in params, "Missing parameter 'LoginStatus'"

def test_users_has_Password():
    assert hasattr(Users, "Password")
    descriptor = None
    for klass in Users.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_users_has_RegisterDate():
    assert hasattr(Users, "RegisterDate")
    descriptor = None
    for klass in Users.__mro__:
        if "RegisterDate" in klass.__dict__:
            descriptor = klass.__dict__["RegisterDate"]
            break
    assert isinstance(descriptor, property)

def test_users_has_UserID():
    assert hasattr(Users, "UserID")
    descriptor = None
    for klass in Users.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_users_has_LoginStatus():
    assert hasattr(Users, "LoginStatus")
    descriptor = None
    for klass in Users.__mro__:
        if "LoginStatus" in klass.__dict__:
            descriptor = klass.__dict__["LoginStatus"]
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
Shopping_strategy = st.builds(
    Shopping,
    Name=
        safe_text,
    Identity=
        st.integers(),
    Location=
        safe_text
)
OrderDetails_strategy = st.builds(
    OrderDetails,
    ProductName=
        safe_text,
    UnitCost=
        st.integers(),
    OrderID=
        st.integers(),
    Quantity=
        st.integers(),
    SubTotal=
        st.integers(),
    ProductID=
        st.integers()
)
ShippingInfo_strategy = st.builds(
    ShippingInfo,
    ShippingID=
        st.integers(),
    ShippingRegionID=
        st.integers(),
    ShippingCost=
        st.integers(),
    ShippingType=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Status=
        safe_text,
    DateShipped=
        safe_text,
    OrderID=
        st.integers(),
    CustomerID=
        safe_text,
    DateCreated=
        safe_text,
    CustomerName=
        safe_text,
    ShippingID=
        safe_text
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    ProductID=
        st.integers(),
    DateAdded=
        st.integers(),
    Quantity=
        st.integers(),
    CartID=
        st.integers()
)
Administrator_strategy = st.builds(
    Administrator,
    AdminName=
        safe_text,
    Email=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    CreditCartInfo=
        safe_text,
    CustomerName=
        safe_text,
    AccountBalance=
        st.integers(),
    Address=
        safe_text,
    Email=
        safe_text,
    ShippingInfo=
        safe_text
)
Users_strategy = st.builds(
    Users,
    Password=
        safe_text,
    RegisterDate=
        st.integers(),
    UserID=
        safe_text,
    LoginStatus=
        safe_text
)

@given(instance=Shopping_strategy)
@settings(max_examples=50)
def test_shopping_instantiation(instance):
    assert isinstance(instance, Shopping)



@given(instance=Shopping_strategy)
def test_shopping_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Shopping_strategy)
def test_shopping_Identity_setter(instance):
    original = instance.Identity
    instance.Identity = original
    assert instance.Identity == original



@given(instance=Shopping_strategy)
def test_shopping_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original

@given(instance=OrderDetails_strategy)
@settings(max_examples=50)
def test_orderdetails_instantiation(instance):
    assert isinstance(instance, OrderDetails)



@given(instance=OrderDetails_strategy)
def test_orderdetails_ProductName_setter(instance):
    original = instance.ProductName
    instance.ProductName = original
    assert instance.ProductName == original



@given(instance=OrderDetails_strategy)
def test_orderdetails_UnitCost_setter(instance):
    original = instance.UnitCost
    instance.UnitCost = original
    assert instance.UnitCost == original



@given(instance=OrderDetails_strategy)
def test_orderdetails_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=OrderDetails_strategy)
def test_orderdetails_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=OrderDetails_strategy)
def test_orderdetails_SubTotal_setter(instance):
    original = instance.SubTotal
    instance.SubTotal = original
    assert instance.SubTotal == original



@given(instance=OrderDetails_strategy)
def test_orderdetails_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original

@given(instance=ShippingInfo_strategy)
@settings(max_examples=50)
def test_shippinginfo_instantiation(instance):
    assert isinstance(instance, ShippingInfo)



@given(instance=ShippingInfo_strategy)
def test_shippinginfo_ShippingID_setter(instance):
    original = instance.ShippingID
    instance.ShippingID = original
    assert instance.ShippingID == original



@given(instance=ShippingInfo_strategy)
def test_shippinginfo_ShippingRegionID_setter(instance):
    original = instance.ShippingRegionID
    instance.ShippingRegionID = original
    assert instance.ShippingRegionID == original



@given(instance=ShippingInfo_strategy)
def test_shippinginfo_ShippingCost_setter(instance):
    original = instance.ShippingCost
    instance.ShippingCost = original
    assert instance.ShippingCost == original



@given(instance=ShippingInfo_strategy)
def test_shippinginfo_ShippingType_setter(instance):
    original = instance.ShippingType
    instance.ShippingType = original
    assert instance.ShippingType == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Order_strategy)
def test_order_DateShipped_setter(instance):
    original = instance.DateShipped
    instance.DateShipped = original
    assert instance.DateShipped == original



@given(instance=Order_strategy)
def test_order_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=Order_strategy)
def test_order_CustomerID_setter(instance):
    original = instance.CustomerID
    instance.CustomerID = original
    assert instance.CustomerID == original



@given(instance=Order_strategy)
def test_order_DateCreated_setter(instance):
    original = instance.DateCreated
    instance.DateCreated = original
    assert instance.DateCreated == original



@given(instance=Order_strategy)
def test_order_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=Order_strategy)
def test_order_ShippingID_setter(instance):
    original = instance.ShippingID
    instance.ShippingID = original
    assert instance.ShippingID == original

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_DateAdded_setter(instance):
    original = instance.DateAdded
    instance.DateAdded = original
    assert instance.DateAdded == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_CartID_setter(instance):
    original = instance.CartID
    instance.CartID = original
    assert instance.CartID == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_AdminName_setter(instance):
    original = instance.AdminName
    instance.AdminName = original
    assert instance.AdminName == original



@given(instance=Administrator_strategy)
def test_administrator_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_CreditCartInfo_setter(instance):
    original = instance.CreditCartInfo
    instance.CreditCartInfo = original
    assert instance.CreditCartInfo == original



@given(instance=Customer_strategy)
def test_customer_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=Customer_strategy)
def test_customer_AccountBalance_setter(instance):
    original = instance.AccountBalance
    instance.AccountBalance = original
    assert instance.AccountBalance == original



@given(instance=Customer_strategy)
def test_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Customer_strategy)
def test_customer_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Customer_strategy)
def test_customer_ShippingInfo_setter(instance):
    original = instance.ShippingInfo
    instance.ShippingInfo = original
    assert instance.ShippingInfo == original

@given(instance=Users_strategy)
@settings(max_examples=50)
def test_users_instantiation(instance):
    assert isinstance(instance, Users)



@given(instance=Users_strategy)
def test_users_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Users_strategy)
def test_users_RegisterDate_setter(instance):
    original = instance.RegisterDate
    instance.RegisterDate = original
    assert instance.RegisterDate == original



@given(instance=Users_strategy)
def test_users_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=Users_strategy)
def test_users_LoginStatus_setter(instance):
    original = instance.LoginStatus
    instance.LoginStatus = original
    assert instance.LoginStatus == original
