import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    Shopping_cart,
    Orders,
    Order_Details,
    shippingInfo,
    Admin,
    User,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_cart)


def test_shopping_cart_constructor_exists():
    assert callable(Shopping_cart.__init__)


def test_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_cart.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "change_to_cart__" in params, "Missing parameter 'change_to_cart__'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "Checkout__" in params, "Missing parameter 'Checkout__'"
    assert "cartId" in params, "Missing parameter 'cartId'"
    assert "Add_items_to_shopping_cart__" in params, "Missing parameter 'Add_items_to_shopping_cart__'"
    assert "Delete_from_Shopping_Cart__" in params, "Missing parameter 'Delete_from_Shopping_Cart__'"

def test_shopping_cart_has_date():
    assert hasattr(Shopping_cart, "date")
    descriptor = None
    for klass in Shopping_cart.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_change_to_cart__():
    assert hasattr(Shopping_cart, "change_to_cart__")
    descriptor = None
    for klass in Shopping_cart.__mro__:
        if "change_to_cart__" in klass.__dict__:
            descriptor = klass.__dict__["change_to_cart__"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_productId():
    assert hasattr(Shopping_cart, "productId")
    descriptor = None
    for klass in Shopping_cart.__mro__:
        if "productId" in klass.__dict__:
            descriptor = klass.__dict__["productId"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_quantity():
    assert hasattr(Shopping_cart, "quantity")
    descriptor = None
    for klass in Shopping_cart.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_Checkout__():
    assert hasattr(Shopping_cart, "Checkout__")
    descriptor = None
    for klass in Shopping_cart.__mro__:
        if "Checkout__" in klass.__dict__:
            descriptor = klass.__dict__["Checkout__"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_cartId():
    assert hasattr(Shopping_cart, "cartId")
    descriptor = None
    for klass in Shopping_cart.__mro__:
        if "cartId" in klass.__dict__:
            descriptor = klass.__dict__["cartId"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_Add_items_to_shopping_cart__():
    assert hasattr(Shopping_cart, "Add_items_to_shopping_cart__")
    descriptor = None
    for klass in Shopping_cart.__mro__:
        if "Add_items_to_shopping_cart__" in klass.__dict__:
            descriptor = klass.__dict__["Add_items_to_shopping_cart__"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_Delete_from_Shopping_Cart__():
    assert hasattr(Shopping_cart, "Delete_from_Shopping_Cart__")
    descriptor = None
    for klass in Shopping_cart.__mro__:
        if "Delete_from_Shopping_Cart__" in klass.__dict__:
            descriptor = klass.__dict__["Delete_from_Shopping_Cart__"]
            break
    assert isinstance(descriptor, property)



def test_orders_is_not_abstract():
    assert not inspect.isabstract(Orders)


def test_orders_constructor_exists():
    assert callable(Orders.__init__)


def test_orders_constructor_args():
    sig = inspect.signature(Orders.__init__)
    params = list(sig.parameters.keys())
    assert "dateShipped" in params, "Missing parameter 'dateShipped'"
    assert "customerName" in params, "Missing parameter 'customerName'"
    assert "status" in params, "Missing parameter 'status'"
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "shippingId" in params, "Missing parameter 'shippingId'"
    assert "dateCreated" in params, "Missing parameter 'dateCreated'"
    assert "customerId" in params, "Missing parameter 'customerId'"

def test_orders_has_dateShipped():
    assert hasattr(Orders, "dateShipped")
    descriptor = None
    for klass in Orders.__mro__:
        if "dateShipped" in klass.__dict__:
            descriptor = klass.__dict__["dateShipped"]
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

def test_orders_has_orderId():
    assert hasattr(Orders, "orderId")
    descriptor = None
    for klass in Orders.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_shippingId():
    assert hasattr(Orders, "shippingId")
    descriptor = None
    for klass in Orders.__mro__:
        if "shippingId" in klass.__dict__:
            descriptor = klass.__dict__["shippingId"]
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

def test_orders_has_customerId():
    assert hasattr(Orders, "customerId")
    descriptor = None
    for klass in Orders.__mro__:
        if "customerId" in klass.__dict__:
            descriptor = klass.__dict__["customerId"]
            break
    assert isinstance(descriptor, property)



def test_order_details_is_not_abstract():
    assert not inspect.isabstract(Order_Details)


def test_order_details_constructor_exists():
    assert callable(Order_Details.__init__)


def test_order_details_constructor_args():
    sig = inspect.signature(Order_Details.__init__)
    params = list(sig.parameters.keys())
    assert "productId" in params, "Missing parameter 'productId'"
    assert "Payment__" in params, "Missing parameter 'Payment__'"
    assert "productName" in params, "Missing parameter 'productName'"
    assert "Report_Generation" in params, "Missing parameter 'Report_Generation'"
    assert "unitCost" in params, "Missing parameter 'unitCost'"
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "subTotal" in params, "Missing parameter 'subTotal'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_order_details_has_productId():
    assert hasattr(Order_Details, "productId")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "productId" in klass.__dict__:
            descriptor = klass.__dict__["productId"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_Payment__():
    assert hasattr(Order_Details, "Payment__")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "Payment__" in klass.__dict__:
            descriptor = klass.__dict__["Payment__"]
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

def test_order_details_has_Report_Generation():
    assert hasattr(Order_Details, "Report_Generation")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "Report_Generation" in klass.__dict__:
            descriptor = klass.__dict__["Report_Generation"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_unitCost():
    assert hasattr(Order_Details, "unitCost")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "unitCost" in klass.__dict__:
            descriptor = klass.__dict__["unitCost"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_orderId():
    assert hasattr(Order_Details, "orderId")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_subTotal():
    assert hasattr(Order_Details, "subTotal")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "subTotal" in klass.__dict__:
            descriptor = klass.__dict__["subTotal"]
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



def test_shippinginfo_is_not_abstract():
    assert not inspect.isabstract(shippingInfo)


def test_shippinginfo_constructor_exists():
    assert callable(shippingInfo.__init__)


def test_shippinginfo_constructor_args():
    sig = inspect.signature(shippingInfo.__init__)
    params = list(sig.parameters.keys())
    assert "View_Shipping_Status__" in params, "Missing parameter 'View_Shipping_Status__'"
    assert "shippingType" in params, "Missing parameter 'shippingType'"
    assert "shippingId" in params, "Missing parameter 'shippingId'"
    assert "shippingRegionId" in params, "Missing parameter 'shippingRegionId'"
    assert "shippingCost" in params, "Missing parameter 'shippingCost'"

def test_shippinginfo_has_View_Shipping_Status__():
    assert hasattr(shippingInfo, "View_Shipping_Status__")
    descriptor = None
    for klass in shippingInfo.__mro__:
        if "View_Shipping_Status__" in klass.__dict__:
            descriptor = klass.__dict__["View_Shipping_Status__"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_shippingType():
    assert hasattr(shippingInfo, "shippingType")
    descriptor = None
    for klass in shippingInfo.__mro__:
        if "shippingType" in klass.__dict__:
            descriptor = klass.__dict__["shippingType"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_shippingId():
    assert hasattr(shippingInfo, "shippingId")
    descriptor = None
    for klass in shippingInfo.__mro__:
        if "shippingId" in klass.__dict__:
            descriptor = klass.__dict__["shippingId"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_shippingRegionId():
    assert hasattr(shippingInfo, "shippingRegionId")
    descriptor = None
    for klass in shippingInfo.__mro__:
        if "shippingRegionId" in klass.__dict__:
            descriptor = klass.__dict__["shippingRegionId"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_shippingCost():
    assert hasattr(shippingInfo, "shippingCost")
    descriptor = None
    for klass in shippingInfo.__mro__:
        if "shippingCost" in klass.__dict__:
            descriptor = klass.__dict__["shippingCost"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "adminName" in params, "Missing parameter 'adminName'"
    assert "Contact_Us__" in params, "Missing parameter 'Contact_Us__'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "Help__" in params, "Missing parameter 'Help__'"
    assert "email" in params, "Missing parameter 'email'"
    assert "Reverse__" in params, "Missing parameter 'Reverse__'"

def test_admin_has_adminName():
    assert hasattr(Admin, "adminName")
    descriptor = None
    for klass in Admin.__mro__:
        if "adminName" in klass.__dict__:
            descriptor = klass.__dict__["adminName"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_Contact_Us__():
    assert hasattr(Admin, "Contact_Us__")
    descriptor = None
    for klass in Admin.__mro__:
        if "Contact_Us__" in klass.__dict__:
            descriptor = klass.__dict__["Contact_Us__"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_attribute():
    assert hasattr(Admin, "attribute")
    descriptor = None
    for klass in Admin.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_Help__():
    assert hasattr(Admin, "Help__")
    descriptor = None
    for klass in Admin.__mro__:
        if "Help__" in klass.__dict__:
            descriptor = klass.__dict__["Help__"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_email():
    assert hasattr(Admin, "email")
    descriptor = None
    for klass in Admin.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_Reverse__():
    assert hasattr(Admin, "Reverse__")
    descriptor = None
    for klass in Admin.__mro__:
        if "Reverse__" in klass.__dict__:
            descriptor = klass.__dict__["Reverse__"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "password" in params, "Missing parameter 'password'"
    assert "View_Account_Purchase_History__" in params, "Missing parameter 'View_Account_Purchase_History__'"
    assert "Update_Account_Information__" in params, "Missing parameter 'Update_Account_Information__'"
    assert "Logout__" in params, "Missing parameter 'Logout__'"

def test_user_has_loginStatus():
    assert hasattr(User, "loginStatus")
    descriptor = None
    for klass in User.__mro__:
        if "loginStatus" in klass.__dict__:
            descriptor = klass.__dict__["loginStatus"]
            break
    assert isinstance(descriptor, property)

def test_user_has_userId():
    assert hasattr(User, "userId")
    descriptor = None
    for klass in User.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
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

def test_user_has_View_Account_Purchase_History__():
    assert hasattr(User, "View_Account_Purchase_History__")
    descriptor = None
    for klass in User.__mro__:
        if "View_Account_Purchase_History__" in klass.__dict__:
            descriptor = klass.__dict__["View_Account_Purchase_History__"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Update_Account_Information__():
    assert hasattr(User, "Update_Account_Information__")
    descriptor = None
    for klass in User.__mro__:
        if "Update_Account_Information__" in klass.__dict__:
            descriptor = klass.__dict__["Update_Account_Information__"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Logout__():
    assert hasattr(User, "Logout__")
    descriptor = None
    for klass in User.__mro__:
        if "Logout__" in klass.__dict__:
            descriptor = klass.__dict__["Logout__"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "creditCardInfo" in params, "Missing parameter 'creditCardInfo'"
    assert "address" in params, "Missing parameter 'address'"
    assert "search__" in params, "Missing parameter 'search__'"
    assert "registration__" in params, "Missing parameter 'registration__'"
    assert "shippingInfo" in params, "Missing parameter 'shippingInfo'"
    assert "login__" in params, "Missing parameter 'login__'"
    assert "customerName" in params, "Missing parameter 'customerName'"
    assert "email" in params, "Missing parameter 'email'"

def test_customer_has_creditCardInfo():
    assert hasattr(Customer, "creditCardInfo")
    descriptor = None
    for klass in Customer.__mro__:
        if "creditCardInfo" in klass.__dict__:
            descriptor = klass.__dict__["creditCardInfo"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_address():
    assert hasattr(Customer, "address")
    descriptor = None
    for klass in Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_search__():
    assert hasattr(Customer, "search__")
    descriptor = None
    for klass in Customer.__mro__:
        if "search__" in klass.__dict__:
            descriptor = klass.__dict__["search__"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_registration__():
    assert hasattr(Customer, "registration__")
    descriptor = None
    for klass in Customer.__mro__:
        if "registration__" in klass.__dict__:
            descriptor = klass.__dict__["registration__"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_shippingInfo():
    assert hasattr(Customer, "shippingInfo")
    descriptor = None
    for klass in Customer.__mro__:
        if "shippingInfo" in klass.__dict__:
            descriptor = klass.__dict__["shippingInfo"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_login__():
    assert hasattr(Customer, "login__")
    descriptor = None
    for klass in Customer.__mro__:
        if "login__" in klass.__dict__:
            descriptor = klass.__dict__["login__"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_customerName():
    assert hasattr(Customer, "customerName")
    descriptor = None
    for klass in Customer.__mro__:
        if "customerName" in klass.__dict__:
            descriptor = klass.__dict__["customerName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_email():
    assert hasattr(Customer, "email")
    descriptor = None
    for klass in Customer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
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
Shopping_cart_strategy = st.builds(
    Shopping_cart,
    date=
        st.integers(),
    change_to_cart__=
        st.none(),
    productId=
        st.integers(),
    quantity=
        st.integers(),
    Checkout__=
        st.none(),
    cartId=
        st.integers(),
    Add_items_to_shopping_cart__=
        st.none(),
    Delete_from_Shopping_Cart__=
        st.none()
)
Orders_strategy = st.builds(
    Orders,
    dateShipped=
        safe_text,
    customerName=
        safe_text,
    status=
        safe_text,
    orderId=
        st.integers(),
    shippingId=
        safe_text,
    dateCreated=
        safe_text,
    customerId=
        safe_text
)
Order_Details_strategy = st.builds(
    Order_Details,
    productId=
        st.integers(),
    Payment__=
        st.none(),
    productName=
        safe_text,
    Report_Generation=
        st.none(),
    unitCost=
        st.integers(),
    orderId=
        st.integers(),
    subTotal=
        st.integers(),
    quantity=
        st.integers()
)
shippingInfo_strategy = st.builds(
    shippingInfo,
    View_Shipping_Status__=
        st.none(),
    shippingType=
        safe_text,
    shippingId=
        st.integers(),
    shippingRegionId=
        st.integers(),
    shippingCost=
        st.integers()
)
Admin_strategy = st.builds(
    Admin,
    adminName=
        safe_text,
    Contact_Us__=
        st.none(),
    attribute=
        safe_text,
    Help__=
        st.none(),
    email=
        safe_text,
    Reverse__=
        st.none()
)
User_strategy = st.builds(
    User,
    loginStatus=
        safe_text,
    userId=
        safe_text,
    password=
        safe_text,
    View_Account_Purchase_History__=
        st.none(),
    Update_Account_Information__=
        st.none(),
    Logout__=
        st.none()
)
Customer_strategy = st.builds(
    Customer,
    creditCardInfo=
        safe_text,
    address=
        safe_text,
    search__=
        st.none(),
    registration__=
        st.none(),
    shippingInfo=
        safe_text,
    login__=
        st.none(),
    customerName=
        safe_text,
    email=
        safe_text
)

@given(instance=Shopping_cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_cart)

@given(instance=Shopping_cart_strategy)
def test_shopping_cart_date_type(instance):
    assert isinstance(instance.date, int)


@given(instance=Shopping_cart_strategy)
def test_shopping_cart_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Shopping_cart_strategy)
def test_shopping_cart_change_to_cart___type(instance):
    assert isinstance(instance.change_to_cart__, shopping_cart)


@given(instance=Shopping_cart_strategy)
def test_shopping_cart_change_to_cart___setter(instance):
    original = instance.change_to_cart__
    instance.change_to_cart__ = original
    assert instance.change_to_cart__ == original

@given(instance=Shopping_cart_strategy)
def test_shopping_cart_productId_type(instance):
    assert isinstance(instance.productId, int)


@given(instance=Shopping_cart_strategy)
def test_shopping_cart_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original

@given(instance=Shopping_cart_strategy)
def test_shopping_cart_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=Shopping_cart_strategy)
def test_shopping_cart_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Shopping_cart_strategy)
def test_shopping_cart_Checkout___type(instance):
    assert isinstance(instance.Checkout__, shopping_cart)


@given(instance=Shopping_cart_strategy)
def test_shopping_cart_Checkout___setter(instance):
    original = instance.Checkout__
    instance.Checkout__ = original
    assert instance.Checkout__ == original

@given(instance=Shopping_cart_strategy)
def test_shopping_cart_cartId_type(instance):
    assert isinstance(instance.cartId, int)


@given(instance=Shopping_cart_strategy)
def test_shopping_cart_cartId_setter(instance):
    original = instance.cartId
    instance.cartId = original
    assert instance.cartId == original

@given(instance=Shopping_cart_strategy)
def test_shopping_cart_Add_items_to_shopping_cart___type(instance):
    assert isinstance(instance.Add_items_to_shopping_cart__, shopping_cart)


@given(instance=Shopping_cart_strategy)
def test_shopping_cart_Add_items_to_shopping_cart___setter(instance):
    original = instance.Add_items_to_shopping_cart__
    instance.Add_items_to_shopping_cart__ = original
    assert instance.Add_items_to_shopping_cart__ == original

@given(instance=Shopping_cart_strategy)
def test_shopping_cart_Delete_from_Shopping_Cart___type(instance):
    assert isinstance(instance.Delete_from_Shopping_Cart__, shopping_cart)


@given(instance=Shopping_cart_strategy)
def test_shopping_cart_Delete_from_Shopping_Cart___setter(instance):
    original = instance.Delete_from_Shopping_Cart__
    instance.Delete_from_Shopping_Cart__ = original
    assert instance.Delete_from_Shopping_Cart__ == original

@given(instance=Orders_strategy)
@settings(max_examples=50)
def test_orders_instantiation(instance):
    assert isinstance(instance, Orders)

@given(instance=Orders_strategy)
def test_orders_dateShipped_type(instance):
    assert isinstance(instance.dateShipped, str)


@given(instance=Orders_strategy)
def test_orders_dateShipped_setter(instance):
    original = instance.dateShipped
    instance.dateShipped = original
    assert instance.dateShipped == original

@given(instance=Orders_strategy)
def test_orders_customerName_type(instance):
    assert isinstance(instance.customerName, str)


@given(instance=Orders_strategy)
def test_orders_customerName_setter(instance):
    original = instance.customerName
    instance.customerName = original
    assert instance.customerName == original

@given(instance=Orders_strategy)
def test_orders_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=Orders_strategy)
def test_orders_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Orders_strategy)
def test_orders_orderId_type(instance):
    assert isinstance(instance.orderId, int)


@given(instance=Orders_strategy)
def test_orders_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original

@given(instance=Orders_strategy)
def test_orders_shippingId_type(instance):
    assert isinstance(instance.shippingId, str)


@given(instance=Orders_strategy)
def test_orders_shippingId_setter(instance):
    original = instance.shippingId
    instance.shippingId = original
    assert instance.shippingId == original

@given(instance=Orders_strategy)
def test_orders_dateCreated_type(instance):
    assert isinstance(instance.dateCreated, str)


@given(instance=Orders_strategy)
def test_orders_dateCreated_setter(instance):
    original = instance.dateCreated
    instance.dateCreated = original
    assert instance.dateCreated == original

@given(instance=Orders_strategy)
def test_orders_customerId_type(instance):
    assert isinstance(instance.customerId, str)


@given(instance=Orders_strategy)
def test_orders_customerId_setter(instance):
    original = instance.customerId
    instance.customerId = original
    assert instance.customerId == original

@given(instance=Order_Details_strategy)
@settings(max_examples=50)
def test_order_details_instantiation(instance):
    assert isinstance(instance, Order_Details)

@given(instance=Order_Details_strategy)
def test_order_details_productId_type(instance):
    assert isinstance(instance.productId, int)


@given(instance=Order_Details_strategy)
def test_order_details_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original

@given(instance=Order_Details_strategy)
def test_order_details_Payment___type(instance):
    assert isinstance(instance.Payment__, order_details)


@given(instance=Order_Details_strategy)
def test_order_details_Payment___setter(instance):
    original = instance.Payment__
    instance.Payment__ = original
    assert instance.Payment__ == original

@given(instance=Order_Details_strategy)
def test_order_details_productName_type(instance):
    assert isinstance(instance.productName, str)


@given(instance=Order_Details_strategy)
def test_order_details_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original

@given(instance=Order_Details_strategy)
def test_order_details_Report_Generation_type(instance):
    assert isinstance(instance.Report_Generation, order_details)


@given(instance=Order_Details_strategy)
def test_order_details_Report_Generation_setter(instance):
    original = instance.Report_Generation
    instance.Report_Generation = original
    assert instance.Report_Generation == original

@given(instance=Order_Details_strategy)
def test_order_details_unitCost_type(instance):
    assert isinstance(instance.unitCost, int)


@given(instance=Order_Details_strategy)
def test_order_details_unitCost_setter(instance):
    original = instance.unitCost
    instance.unitCost = original
    assert instance.unitCost == original

@given(instance=Order_Details_strategy)
def test_order_details_orderId_type(instance):
    assert isinstance(instance.orderId, int)


@given(instance=Order_Details_strategy)
def test_order_details_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original

@given(instance=Order_Details_strategy)
def test_order_details_subTotal_type(instance):
    assert isinstance(instance.subTotal, int)


@given(instance=Order_Details_strategy)
def test_order_details_subTotal_setter(instance):
    original = instance.subTotal
    instance.subTotal = original
    assert instance.subTotal == original

@given(instance=Order_Details_strategy)
def test_order_details_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=Order_Details_strategy)
def test_order_details_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=shippingInfo_strategy)
@settings(max_examples=50)
def test_shippinginfo_instantiation(instance):
    assert isinstance(instance, shippingInfo)

@given(instance=shippingInfo_strategy)
def test_shippinginfo_View_Shipping_Status___type(instance):
    assert isinstance(instance.View_Shipping_Status__, shippinginfo)


@given(instance=shippingInfo_strategy)
def test_shippinginfo_View_Shipping_Status___setter(instance):
    original = instance.View_Shipping_Status__
    instance.View_Shipping_Status__ = original
    assert instance.View_Shipping_Status__ == original

@given(instance=shippingInfo_strategy)
def test_shippinginfo_shippingType_type(instance):
    assert isinstance(instance.shippingType, str)


@given(instance=shippingInfo_strategy)
def test_shippinginfo_shippingType_setter(instance):
    original = instance.shippingType
    instance.shippingType = original
    assert instance.shippingType == original

@given(instance=shippingInfo_strategy)
def test_shippinginfo_shippingId_type(instance):
    assert isinstance(instance.shippingId, int)


@given(instance=shippingInfo_strategy)
def test_shippinginfo_shippingId_setter(instance):
    original = instance.shippingId
    instance.shippingId = original
    assert instance.shippingId == original

@given(instance=shippingInfo_strategy)
def test_shippinginfo_shippingRegionId_type(instance):
    assert isinstance(instance.shippingRegionId, int)


@given(instance=shippingInfo_strategy)
def test_shippinginfo_shippingRegionId_setter(instance):
    original = instance.shippingRegionId
    instance.shippingRegionId = original
    assert instance.shippingRegionId == original

@given(instance=shippingInfo_strategy)
def test_shippinginfo_shippingCost_type(instance):
    assert isinstance(instance.shippingCost, int)


@given(instance=shippingInfo_strategy)
def test_shippinginfo_shippingCost_setter(instance):
    original = instance.shippingCost
    instance.shippingCost = original
    assert instance.shippingCost == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)

@given(instance=Admin_strategy)
def test_admin_adminName_type(instance):
    assert isinstance(instance.adminName, str)


@given(instance=Admin_strategy)
def test_admin_adminName_setter(instance):
    original = instance.adminName
    instance.adminName = original
    assert instance.adminName == original

@given(instance=Admin_strategy)
def test_admin_Contact_Us___type(instance):
    assert isinstance(instance.Contact_Us__, admin)


@given(instance=Admin_strategy)
def test_admin_Contact_Us___setter(instance):
    original = instance.Contact_Us__
    instance.Contact_Us__ = original
    assert instance.Contact_Us__ == original

@given(instance=Admin_strategy)
def test_admin_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=Admin_strategy)
def test_admin_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Admin_strategy)
def test_admin_Help___type(instance):
    assert isinstance(instance.Help__, admin)


@given(instance=Admin_strategy)
def test_admin_Help___setter(instance):
    original = instance.Help__
    instance.Help__ = original
    assert instance.Help__ == original

@given(instance=Admin_strategy)
def test_admin_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=Admin_strategy)
def test_admin_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Admin_strategy)
def test_admin_Reverse___type(instance):
    assert isinstance(instance.Reverse__, admin)


@given(instance=Admin_strategy)
def test_admin_Reverse___setter(instance):
    original = instance.Reverse__
    instance.Reverse__ = original
    assert instance.Reverse__ == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=User_strategy)
def test_user_loginStatus_type(instance):
    assert isinstance(instance.loginStatus, str)


@given(instance=User_strategy)
def test_user_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original

@given(instance=User_strategy)
def test_user_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=User_strategy)
def test_user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=User_strategy)
def test_user_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=User_strategy)
def test_user_View_Account_Purchase_History___type(instance):
    assert isinstance(instance.View_Account_Purchase_History__, user)


@given(instance=User_strategy)
def test_user_View_Account_Purchase_History___setter(instance):
    original = instance.View_Account_Purchase_History__
    instance.View_Account_Purchase_History__ = original
    assert instance.View_Account_Purchase_History__ == original

@given(instance=User_strategy)
def test_user_Update_Account_Information___type(instance):
    assert isinstance(instance.Update_Account_Information__, user)


@given(instance=User_strategy)
def test_user_Update_Account_Information___setter(instance):
    original = instance.Update_Account_Information__
    instance.Update_Account_Information__ = original
    assert instance.Update_Account_Information__ == original

@given(instance=User_strategy)
def test_user_Logout___type(instance):
    assert isinstance(instance.Logout__, user)


@given(instance=User_strategy)
def test_user_Logout___setter(instance):
    original = instance.Logout__
    instance.Logout__ = original
    assert instance.Logout__ == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=Customer_strategy)
def test_customer_creditCardInfo_type(instance):
    assert isinstance(instance.creditCardInfo, str)


@given(instance=Customer_strategy)
def test_customer_creditCardInfo_setter(instance):
    original = instance.creditCardInfo
    instance.creditCardInfo = original
    assert instance.creditCardInfo == original

@given(instance=Customer_strategy)
def test_customer_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Customer_strategy)
def test_customer_search___type(instance):
    assert isinstance(instance.search__, customer)


@given(instance=Customer_strategy)
def test_customer_search___setter(instance):
    original = instance.search__
    instance.search__ = original
    assert instance.search__ == original

@given(instance=Customer_strategy)
def test_customer_registration___type(instance):
    assert isinstance(instance.registration__, customer)


@given(instance=Customer_strategy)
def test_customer_registration___setter(instance):
    original = instance.registration__
    instance.registration__ = original
    assert instance.registration__ == original

@given(instance=Customer_strategy)
def test_customer_shippingInfo_type(instance):
    assert isinstance(instance.shippingInfo, str)


@given(instance=Customer_strategy)
def test_customer_shippingInfo_setter(instance):
    original = instance.shippingInfo
    instance.shippingInfo = original
    assert instance.shippingInfo == original

@given(instance=Customer_strategy)
def test_customer_login___type(instance):
    assert isinstance(instance.login__, customer)


@given(instance=Customer_strategy)
def test_customer_login___setter(instance):
    original = instance.login__
    instance.login__ = original
    assert instance.login__ == original

@given(instance=Customer_strategy)
def test_customer_customerName_type(instance):
    assert isinstance(instance.customerName, str)


@given(instance=Customer_strategy)
def test_customer_customerName_setter(instance):
    original = instance.customerName
    instance.customerName = original
    assert instance.customerName == original

@given(instance=Customer_strategy)
def test_customer_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=Customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original
