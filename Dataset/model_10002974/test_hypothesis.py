import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Products,
    Item,
    Administrator,
    Order_Details,
    Orders,
    Shopping_Cart,
    Shipping_Info,
    User,
    Client,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_products_is_not_abstract():
    assert not inspect.isabstract(Products)


def test_products_constructor_exists():
    assert callable(Products.__init__)


def test_products_constructor_args():
    sig = inspect.signature(Products.__init__)
    params = list(sig.parameters.keys())
    assert "totral" in params, "Missing parameter 'totral'"
    assert "racknumber" in params, "Missing parameter 'racknumber'"

def test_products_has_totral():
    assert hasattr(Products, "totral")
    descriptor = None
    for klass in Products.__mro__:
        if "totral" in klass.__dict__:
            descriptor = klass.__dict__["totral"]
            break
    assert isinstance(descriptor, property)

def test_products_has_racknumber():
    assert hasattr(Products, "racknumber")
    descriptor = None
    for klass in Products.__mro__:
        if "racknumber" in klass.__dict__:
            descriptor = klass.__dict__["racknumber"]
            break
    assert isinstance(descriptor, property)



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pieceAvailable" in params, "Missing parameter 'pieceAvailable'"
    assert "unitcost" in params, "Missing parameter 'unitcost'"

def test_item_has_name():
    assert hasattr(Item, "name")
    descriptor = None
    for klass in Item.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_item_has_pieceAvailable():
    assert hasattr(Item, "pieceAvailable")
    descriptor = None
    for klass in Item.__mro__:
        if "pieceAvailable" in klass.__dict__:
            descriptor = klass.__dict__["pieceAvailable"]
            break
    assert isinstance(descriptor, property)

def test_item_has_unitcost():
    assert hasattr(Item, "unitcost")
    descriptor = None
    for klass in Item.__mro__:
        if "unitcost" in klass.__dict__:
            descriptor = klass.__dict__["unitcost"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "adminName" in params, "Missing parameter 'adminName'"

def test_administrator_has_email():
    assert hasattr(Administrator, "email")
    descriptor = None
    for klass in Administrator.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_adminName():
    assert hasattr(Administrator, "adminName")
    descriptor = None
    for klass in Administrator.__mro__:
        if "adminName" in klass.__dict__:
            descriptor = klass.__dict__["adminName"]
            break
    assert isinstance(descriptor, property)



def test_order_details_is_not_abstract():
    assert not inspect.isabstract(Order_Details)


def test_order_details_constructor_exists():
    assert callable(Order_Details.__init__)


def test_order_details_constructor_args():
    sig = inspect.signature(Order_Details.__init__)
    params = list(sig.parameters.keys())
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "unitcost" in params, "Missing parameter 'unitcost'"
    assert "subtotal" in params, "Missing parameter 'subtotal'"
    assert "productName" in params, "Missing parameter 'productName'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_order_details_has_orderId():
    assert hasattr(Order_Details, "orderId")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_unitcost():
    assert hasattr(Order_Details, "unitcost")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "unitcost" in klass.__dict__:
            descriptor = klass.__dict__["unitcost"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_subtotal():
    assert hasattr(Order_Details, "subtotal")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "subtotal" in klass.__dict__:
            descriptor = klass.__dict__["subtotal"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_productName():
    assert hasattr(Order_Details, "productName")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "productName" in klass.__dict__:
            descriptor = klass.__dict__["productName"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_productId():
    assert hasattr(Order_Details, "productId")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "productId" in klass.__dict__:
            descriptor = klass.__dict__["productId"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_quantity():
    assert hasattr(Order_Details, "quantity")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_orders_is_not_abstract():
    assert not inspect.isabstract(Orders)


def test_orders_constructor_exists():
    assert callable(Orders.__init__)


def test_orders_constructor_args():
    sig = inspect.signature(Orders.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "CustomerId" in params, "Missing parameter 'CustomerId'"
    assert "OrderId" in params, "Missing parameter 'OrderId'"
    assert "ShippingId" in params, "Missing parameter 'ShippingId'"
    assert "dateCreated" in params, "Missing parameter 'dateCreated'"
    assert "customerName" in params, "Missing parameter 'customerName'"
    assert "status" in params, "Missing parameter 'status'"

def test_orders_has_Date():
    assert hasattr(Orders, "Date")
    descriptor = None
    for klass in Orders.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_CustomerId():
    assert hasattr(Orders, "CustomerId")
    descriptor = None
    for klass in Orders.__mro__:
        if "CustomerId" in klass.__dict__:
            descriptor = klass.__dict__["CustomerId"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_OrderId():
    assert hasattr(Orders, "OrderId")
    descriptor = None
    for klass in Orders.__mro__:
        if "OrderId" in klass.__dict__:
            descriptor = klass.__dict__["OrderId"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_ShippingId():
    assert hasattr(Orders, "ShippingId")
    descriptor = None
    for klass in Orders.__mro__:
        if "ShippingId" in klass.__dict__:
            descriptor = klass.__dict__["ShippingId"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_dateCreated():
    assert hasattr(Orders, "dateCreated")
    descriptor = None
    for klass in Orders.__mro__:
        if "dateCreated" in klass.__dict__:
            descriptor = klass.__dict__["dateCreated"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_customerName():
    assert hasattr(Orders, "customerName")
    descriptor = None
    for klass in Orders.__mro__:
        if "customerName" in klass.__dict__:
            descriptor = klass.__dict__["customerName"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_status():
    assert hasattr(Orders, "status")
    descriptor = None
    for klass in Orders.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_Cart)


def test_shopping_cart_constructor_exists():
    assert callable(Shopping_Cart.__init__)


def test_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_Cart.__init__)
    params = list(sig.parameters.keys())
    assert "dateAdded" in params, "Missing parameter 'dateAdded'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "CartId" in params, "Missing parameter 'CartId'"
    assert "productId" in params, "Missing parameter 'productId'"

def test_shopping_cart_has_dateAdded():
    assert hasattr(Shopping_Cart, "dateAdded")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "dateAdded" in klass.__dict__:
            descriptor = klass.__dict__["dateAdded"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_Quantity():
    assert hasattr(Shopping_Cart, "Quantity")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_CartId():
    assert hasattr(Shopping_Cart, "CartId")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "CartId" in klass.__dict__:
            descriptor = klass.__dict__["CartId"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_productId():
    assert hasattr(Shopping_Cart, "productId")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "productId" in klass.__dict__:
            descriptor = klass.__dict__["productId"]
            break
    assert isinstance(descriptor, property)



def test_shipping_info_is_not_abstract():
    assert not inspect.isabstract(Shipping_Info)


def test_shipping_info_constructor_exists():
    assert callable(Shipping_Info.__init__)


def test_shipping_info_constructor_args():
    sig = inspect.signature(Shipping_Info.__init__)
    params = list(sig.parameters.keys())
    assert "ShippingRegionId" in params, "Missing parameter 'ShippingRegionId'"
    assert "Shipping_Type" in params, "Missing parameter 'Shipping_Type'"
    assert "Shipping_Cost" in params, "Missing parameter 'Shipping_Cost'"
    assert "Shipping_Id" in params, "Missing parameter 'Shipping_Id'"

def test_shipping_info_has_ShippingRegionId():
    assert hasattr(Shipping_Info, "ShippingRegionId")
    descriptor = None
    for klass in Shipping_Info.__mro__:
        if "ShippingRegionId" in klass.__dict__:
            descriptor = klass.__dict__["ShippingRegionId"]
            break
    assert isinstance(descriptor, property)

def test_shipping_info_has_Shipping_Type():
    assert hasattr(Shipping_Info, "Shipping_Type")
    descriptor = None
    for klass in Shipping_Info.__mro__:
        if "Shipping_Type" in klass.__dict__:
            descriptor = klass.__dict__["Shipping_Type"]
            break
    assert isinstance(descriptor, property)

def test_shipping_info_has_Shipping_Cost():
    assert hasattr(Shipping_Info, "Shipping_Cost")
    descriptor = None
    for klass in Shipping_Info.__mro__:
        if "Shipping_Cost" in klass.__dict__:
            descriptor = klass.__dict__["Shipping_Cost"]
            break
    assert isinstance(descriptor, property)

def test_shipping_info_has_Shipping_Id():
    assert hasattr(Shipping_Info, "Shipping_Id")
    descriptor = None
    for klass in Shipping_Info.__mro__:
        if "Shipping_Id" in klass.__dict__:
            descriptor = klass.__dict__["Shipping_Id"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "User_Id" in params, "Missing parameter 'User_Id'"
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_user_has_User_Id():
    assert hasattr(User, "User_Id")
    descriptor = None
    for klass in User.__mro__:
        if "User_Id" in klass.__dict__:
            descriptor = klass.__dict__["User_Id"]
            break
    assert isinstance(descriptor, property)

def test_user_has_loginStatus():
    assert hasattr(User, "loginStatus")
    descriptor = None
    for klass in User.__mro__:
        if "loginStatus" in klass.__dict__:
            descriptor = klass.__dict__["loginStatus"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Password():
    assert hasattr(User, "Password")
    descriptor = None
    for klass in User.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_client_is_not_abstract():
    assert not inspect.isabstract(Client)


def test_client_constructor_exists():
    assert callable(Client.__init__)


def test_client_constructor_args():
    sig = inspect.signature(Client.__init__)
    params = list(sig.parameters.keys())
    assert "shipping_info" in params, "Missing parameter 'shipping_info'"
    assert "customer" in params, "Missing parameter 'customer'"
    assert "email" in params, "Missing parameter 'email'"
    assert "address" in params, "Missing parameter 'address'"
    assert "credit_card_info" in params, "Missing parameter 'credit_card_info'"

def test_client_has_shipping_info():
    assert hasattr(Client, "shipping_info")
    descriptor = None
    for klass in Client.__mro__:
        if "shipping_info" in klass.__dict__:
            descriptor = klass.__dict__["shipping_info"]
            break
    assert isinstance(descriptor, property)

def test_client_has_customer():
    assert hasattr(Client, "customer")
    descriptor = None
    for klass in Client.__mro__:
        if "customer" in klass.__dict__:
            descriptor = klass.__dict__["customer"]
            break
    assert isinstance(descriptor, property)

def test_client_has_email():
    assert hasattr(Client, "email")
    descriptor = None
    for klass in Client.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_client_has_address():
    assert hasattr(Client, "address")
    descriptor = None
    for klass in Client.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_client_has_credit_card_info():
    assert hasattr(Client, "credit_card_info")
    descriptor = None
    for klass in Client.__mro__:
        if "credit_card_info" in klass.__dict__:
            descriptor = klass.__dict__["credit_card_info"]
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
Products_strategy = st.builds(
    Products,
    totral=
        st.integers(),
    racknumber=
        st.integers()
)
Item_strategy = st.builds(
    Item,
    name=
        safe_text,
    pieceAvailable=
        st.integers(),
    unitcost=
        st.integers()
)
Administrator_strategy = st.builds(
    Administrator,
    email=
        safe_text,
    adminName=
        safe_text
)
Order_Details_strategy = st.builds(
    Order_Details,
    orderId=
        st.integers(),
    unitcost=
        st.integers(),
    subtotal=
        st.integers(),
    productName=
        safe_text,
    productId=
        st.integers(),
    quantity=
        st.integers()
)
Orders_strategy = st.builds(
    Orders,
    Date=
        safe_text,
    CustomerId=
        safe_text,
    OrderId=
        st.integers(),
    ShippingId=
        safe_text,
    dateCreated=
        safe_text,
    customerName=
        safe_text,
    status=
        safe_text
)
Shopping_Cart_strategy = st.builds(
    Shopping_Cart,
    dateAdded=
        st.integers(),
    Quantity=
        st.integers(),
    CartId=
        st.integers(),
    productId=
        st.integers()
)
Shipping_Info_strategy = st.builds(
    Shipping_Info,
    ShippingRegionId=
        st.integers(),
    Shipping_Type=
        safe_text,
    Shipping_Cost=
        st.integers(),
    Shipping_Id=
        st.integers()
)
User_strategy = st.builds(
    User,
    User_Id=
        safe_text,
    loginStatus=
        safe_text,
    Password=
        safe_text
)
Client_strategy = st.builds(
    Client,
    shipping_info=
        safe_text,
    customer=
        safe_text,
    email=
        safe_text,
    address=
        safe_text,
    credit_card_info=
        safe_text
)

@given(instance=Products_strategy)
@settings(max_examples=50)
def test_products_instantiation(instance):
    assert isinstance(instance, Products)



@given(instance=Products_strategy)
def test_products_totral_setter(instance):
    original = instance.totral
    instance.totral = original
    assert instance.totral == original



@given(instance=Products_strategy)
def test_products_racknumber_setter(instance):
    original = instance.racknumber
    instance.racknumber = original
    assert instance.racknumber == original

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)



@given(instance=Item_strategy)
def test_item_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Item_strategy)
def test_item_pieceAvailable_setter(instance):
    original = instance.pieceAvailable
    instance.pieceAvailable = original
    assert instance.pieceAvailable == original



@given(instance=Item_strategy)
def test_item_unitcost_setter(instance):
    original = instance.unitcost
    instance.unitcost = original
    assert instance.unitcost == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Administrator_strategy)
def test_administrator_adminName_setter(instance):
    original = instance.adminName
    instance.adminName = original
    assert instance.adminName == original

@given(instance=Order_Details_strategy)
@settings(max_examples=50)
def test_order_details_instantiation(instance):
    assert isinstance(instance, Order_Details)



@given(instance=Order_Details_strategy)
def test_order_details_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original



@given(instance=Order_Details_strategy)
def test_order_details_unitcost_setter(instance):
    original = instance.unitcost
    instance.unitcost = original
    assert instance.unitcost == original



@given(instance=Order_Details_strategy)
def test_order_details_subtotal_setter(instance):
    original = instance.subtotal
    instance.subtotal = original
    assert instance.subtotal == original



@given(instance=Order_Details_strategy)
def test_order_details_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original



@given(instance=Order_Details_strategy)
def test_order_details_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=Order_Details_strategy)
def test_order_details_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Orders_strategy)
@settings(max_examples=50)
def test_orders_instantiation(instance):
    assert isinstance(instance, Orders)



@given(instance=Orders_strategy)
def test_orders_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Orders_strategy)
def test_orders_CustomerId_setter(instance):
    original = instance.CustomerId
    instance.CustomerId = original
    assert instance.CustomerId == original



@given(instance=Orders_strategy)
def test_orders_OrderId_setter(instance):
    original = instance.OrderId
    instance.OrderId = original
    assert instance.OrderId == original



@given(instance=Orders_strategy)
def test_orders_ShippingId_setter(instance):
    original = instance.ShippingId
    instance.ShippingId = original
    assert instance.ShippingId == original



@given(instance=Orders_strategy)
def test_orders_dateCreated_setter(instance):
    original = instance.dateCreated
    instance.dateCreated = original
    assert instance.dateCreated == original



@given(instance=Orders_strategy)
def test_orders_customerName_setter(instance):
    original = instance.customerName
    instance.customerName = original
    assert instance.customerName == original



@given(instance=Orders_strategy)
def test_orders_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Shopping_Cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart)



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_dateAdded_setter(instance):
    original = instance.dateAdded
    instance.dateAdded = original
    assert instance.dateAdded == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_CartId_setter(instance):
    original = instance.CartId
    instance.CartId = original
    assert instance.CartId == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original

@given(instance=Shipping_Info_strategy)
@settings(max_examples=50)
def test_shipping_info_instantiation(instance):
    assert isinstance(instance, Shipping_Info)



@given(instance=Shipping_Info_strategy)
def test_shipping_info_ShippingRegionId_setter(instance):
    original = instance.ShippingRegionId
    instance.ShippingRegionId = original
    assert instance.ShippingRegionId == original



@given(instance=Shipping_Info_strategy)
def test_shipping_info_Shipping_Type_setter(instance):
    original = instance.Shipping_Type
    instance.Shipping_Type = original
    assert instance.Shipping_Type == original



@given(instance=Shipping_Info_strategy)
def test_shipping_info_Shipping_Cost_setter(instance):
    original = instance.Shipping_Cost
    instance.Shipping_Cost = original
    assert instance.Shipping_Cost == original



@given(instance=Shipping_Info_strategy)
def test_shipping_info_Shipping_Id_setter(instance):
    original = instance.Shipping_Id
    instance.Shipping_Id = original
    assert instance.Shipping_Id == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_User_Id_setter(instance):
    original = instance.User_Id
    instance.User_Id = original
    assert instance.User_Id == original



@given(instance=User_strategy)
def test_user_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Client_strategy)
@settings(max_examples=50)
def test_client_instantiation(instance):
    assert isinstance(instance, Client)



@given(instance=Client_strategy)
def test_client_shipping_info_setter(instance):
    original = instance.shipping_info
    instance.shipping_info = original
    assert instance.shipping_info == original



@given(instance=Client_strategy)
def test_client_customer_setter(instance):
    original = instance.customer
    instance.customer = original
    assert instance.customer == original



@given(instance=Client_strategy)
def test_client_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Client_strategy)
def test_client_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Client_strategy)
def test_client_credit_card_info_setter(instance):
    original = instance.credit_card_info
    instance.credit_card_info = original
    assert instance.credit_card_info == original
