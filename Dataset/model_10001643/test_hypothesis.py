import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Order_Details,
    Shipping_Info,
    Orders,
    Shopping_Cart,
    Admin,
    User,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_order_details_is_not_abstract():
    assert not inspect.isabstract(Order_Details)


def test_order_details_constructor_exists():
    assert callable(Order_Details.__init__)


def test_order_details_constructor_args():
    sig = inspect.signature(Order_Details.__init__)
    params = list(sig.parameters.keys())
    assert "Order_Id" in params, "Missing parameter 'Order_Id'"
    assert "Unicast" in params, "Missing parameter 'Unicast'"
    assert "Product_Name" in params, "Missing parameter 'Product_Name'"
    assert "Product_Id" in params, "Missing parameter 'Product_Id'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "Sub_Total" in params, "Missing parameter 'Sub_Total'"

def test_order_details_has_Order_Id():
    assert hasattr(Order_Details, "Order_Id")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "Order_Id" in klass.__dict__:
            descriptor = klass.__dict__["Order_Id"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_Unicast():
    assert hasattr(Order_Details, "Unicast")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "Unicast" in klass.__dict__:
            descriptor = klass.__dict__["Unicast"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_Product_Name():
    assert hasattr(Order_Details, "Product_Name")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "Product_Name" in klass.__dict__:
            descriptor = klass.__dict__["Product_Name"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_Product_Id():
    assert hasattr(Order_Details, "Product_Id")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "Product_Id" in klass.__dict__:
            descriptor = klass.__dict__["Product_Id"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_Quantity():
    assert hasattr(Order_Details, "Quantity")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_order_details_has_Sub_Total():
    assert hasattr(Order_Details, "Sub_Total")
    descriptor = None
    for klass in Order_Details.__mro__:
        if "Sub_Total" in klass.__dict__:
            descriptor = klass.__dict__["Sub_Total"]
            break
    assert isinstance(descriptor, property)



def test_shipping_info_is_not_abstract():
    assert not inspect.isabstract(Shipping_Info)


def test_shipping_info_constructor_exists():
    assert callable(Shipping_Info.__init__)


def test_shipping_info_constructor_args():
    sig = inspect.signature(Shipping_Info.__init__)
    params = list(sig.parameters.keys())
    assert "Shipping_Id" in params, "Missing parameter 'Shipping_Id'"
    assert "Shipping_Type" in params, "Missing parameter 'Shipping_Type'"

def test_shipping_info_has_Shipping_Id():
    assert hasattr(Shipping_Info, "Shipping_Id")
    descriptor = None
    for klass in Shipping_Info.__mro__:
        if "Shipping_Id" in klass.__dict__:
            descriptor = klass.__dict__["Shipping_Id"]
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



def test_orders_is_not_abstract():
    assert not inspect.isabstract(Orders)


def test_orders_constructor_exists():
    assert callable(Orders.__init__)


def test_orders_constructor_args():
    sig = inspect.signature(Orders.__init__)
    params = list(sig.parameters.keys())
    assert "Customer_Id" in params, "Missing parameter 'Customer_Id'"
    assert "Order_id" in params, "Missing parameter 'Order_id'"
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Date_Shipped" in params, "Missing parameter 'Date_Shipped'"
    assert "Date_Created" in params, "Missing parameter 'Date_Created'"

def test_orders_has_Customer_Id():
    assert hasattr(Orders, "Customer_Id")
    descriptor = None
    for klass in Orders.__mro__:
        if "Customer_Id" in klass.__dict__:
            descriptor = klass.__dict__["Customer_Id"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_Order_id():
    assert hasattr(Orders, "Order_id")
    descriptor = None
    for klass in Orders.__mro__:
        if "Order_id" in klass.__dict__:
            descriptor = klass.__dict__["Order_id"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_Status():
    assert hasattr(Orders, "Status")
    descriptor = None
    for klass in Orders.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_Date_Shipped():
    assert hasattr(Orders, "Date_Shipped")
    descriptor = None
    for klass in Orders.__mro__:
        if "Date_Shipped" in klass.__dict__:
            descriptor = klass.__dict__["Date_Shipped"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_Date_Created():
    assert hasattr(Orders, "Date_Created")
    descriptor = None
    for klass in Orders.__mro__:
        if "Date_Created" in klass.__dict__:
            descriptor = klass.__dict__["Date_Created"]
            break
    assert isinstance(descriptor, property)



def test_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_Cart)


def test_shopping_cart_constructor_exists():
    assert callable(Shopping_Cart.__init__)


def test_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_Cart.__init__)
    params = list(sig.parameters.keys())
    assert "Cart_id" in params, "Missing parameter 'Cart_id'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "Product_id" in params, "Missing parameter 'Product_id'"

def test_shopping_cart_has_Cart_id():
    assert hasattr(Shopping_Cart, "Cart_id")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "Cart_id" in klass.__dict__:
            descriptor = klass.__dict__["Cart_id"]
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

def test_shopping_cart_has_Product_id():
    assert hasattr(Shopping_Cart, "Product_id")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "Product_id" in klass.__dict__:
            descriptor = klass.__dict__["Product_id"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "AdminName" in params, "Missing parameter 'AdminName'"
    assert "email" in params, "Missing parameter 'email'"

def test_admin_has_AdminName():
    assert hasattr(Admin, "AdminName")
    descriptor = None
    for klass in Admin.__mro__:
        if "AdminName" in klass.__dict__:
            descriptor = klass.__dict__["AdminName"]
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



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "User_Id" in params, "Missing parameter 'User_Id'"
    assert "Login_Status" in params, "Missing parameter 'Login_Status'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_user_has_User_Id():
    assert hasattr(User, "User_Id")
    descriptor = None
    for klass in User.__mro__:
        if "User_Id" in klass.__dict__:
            descriptor = klass.__dict__["User_Id"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Login_Status():
    assert hasattr(User, "Login_Status")
    descriptor = None
    for klass in User.__mro__:
        if "Login_Status" in klass.__dict__:
            descriptor = klass.__dict__["Login_Status"]
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



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Credit_Card_Info" in params, "Missing parameter 'Credit_Card_Info'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "email" in params, "Missing parameter 'email'"
    assert "Customer_Name" in params, "Missing parameter 'Customer_Name'"

def test_customer_has_Credit_Card_Info():
    assert hasattr(Customer, "Credit_Card_Info")
    descriptor = None
    for klass in Customer.__mro__:
        if "Credit_Card_Info" in klass.__dict__:
            descriptor = klass.__dict__["Credit_Card_Info"]
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

def test_customer_has_email():
    assert hasattr(Customer, "email")
    descriptor = None
    for klass in Customer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Customer_Name():
    assert hasattr(Customer, "Customer_Name")
    descriptor = None
    for klass in Customer.__mro__:
        if "Customer_Name" in klass.__dict__:
            descriptor = klass.__dict__["Customer_Name"]
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
Order_Details_strategy = st.builds(
    Order_Details,
    Order_Id=
        st.integers(),
    Unicast=
        safe_text,
    Product_Name=
        safe_text,
    Product_Id=
        st.integers(),
    Quantity=
        st.integers(),
    Sub_Total=
        safe_text
)
Shipping_Info_strategy = st.builds(
    Shipping_Info,
    Shipping_Id=
        st.integers(),
    Shipping_Type=
        safe_text
)
Orders_strategy = st.builds(
    Orders,
    Customer_Id=
        safe_text,
    Order_id=
        st.integers(),
    Status=
        safe_text,
    Date_Shipped=
        safe_text,
    Date_Created=
        safe_text
)
Shopping_Cart_strategy = st.builds(
    Shopping_Cart,
    Cart_id=
        st.integers(),
    Quantity=
        st.integers(),
    Product_id=
        st.integers()
)
Admin_strategy = st.builds(
    Admin,
    AdminName=
        safe_text,
    email=
        safe_text
)
User_strategy = st.builds(
    User,
    User_Id=
        st.integers(),
    Login_Status=
        safe_text,
    Password=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    Credit_Card_Info=
        st.integers(),
    Address=
        safe_text,
    email=
        safe_text,
    Customer_Name=
        safe_text
)

@given(instance=Order_Details_strategy)
@settings(max_examples=50)
def test_order_details_instantiation(instance):
    assert isinstance(instance, Order_Details)



@given(instance=Order_Details_strategy)
def test_order_details_Order_Id_setter(instance):
    original = instance.Order_Id
    instance.Order_Id = original
    assert instance.Order_Id == original



@given(instance=Order_Details_strategy)
def test_order_details_Unicast_setter(instance):
    original = instance.Unicast
    instance.Unicast = original
    assert instance.Unicast == original



@given(instance=Order_Details_strategy)
def test_order_details_Product_Name_setter(instance):
    original = instance.Product_Name
    instance.Product_Name = original
    assert instance.Product_Name == original



@given(instance=Order_Details_strategy)
def test_order_details_Product_Id_setter(instance):
    original = instance.Product_Id
    instance.Product_Id = original
    assert instance.Product_Id == original



@given(instance=Order_Details_strategy)
def test_order_details_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Order_Details_strategy)
def test_order_details_Sub_Total_setter(instance):
    original = instance.Sub_Total
    instance.Sub_Total = original
    assert instance.Sub_Total == original

@given(instance=Shipping_Info_strategy)
@settings(max_examples=50)
def test_shipping_info_instantiation(instance):
    assert isinstance(instance, Shipping_Info)



@given(instance=Shipping_Info_strategy)
def test_shipping_info_Shipping_Id_setter(instance):
    original = instance.Shipping_Id
    instance.Shipping_Id = original
    assert instance.Shipping_Id == original



@given(instance=Shipping_Info_strategy)
def test_shipping_info_Shipping_Type_setter(instance):
    original = instance.Shipping_Type
    instance.Shipping_Type = original
    assert instance.Shipping_Type == original

@given(instance=Orders_strategy)
@settings(max_examples=50)
def test_orders_instantiation(instance):
    assert isinstance(instance, Orders)



@given(instance=Orders_strategy)
def test_orders_Customer_Id_setter(instance):
    original = instance.Customer_Id
    instance.Customer_Id = original
    assert instance.Customer_Id == original



@given(instance=Orders_strategy)
def test_orders_Order_id_setter(instance):
    original = instance.Order_id
    instance.Order_id = original
    assert instance.Order_id == original



@given(instance=Orders_strategy)
def test_orders_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Orders_strategy)
def test_orders_Date_Shipped_setter(instance):
    original = instance.Date_Shipped
    instance.Date_Shipped = original
    assert instance.Date_Shipped == original



@given(instance=Orders_strategy)
def test_orders_Date_Created_setter(instance):
    original = instance.Date_Created
    instance.Date_Created = original
    assert instance.Date_Created == original

@given(instance=Shopping_Cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart)



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_Cart_id_setter(instance):
    original = instance.Cart_id
    instance.Cart_id = original
    assert instance.Cart_id == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_Product_id_setter(instance):
    original = instance.Product_id
    instance.Product_id = original
    assert instance.Product_id == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_AdminName_setter(instance):
    original = instance.AdminName
    instance.AdminName = original
    assert instance.AdminName == original



@given(instance=Admin_strategy)
def test_admin_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

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
def test_user_Login_Status_setter(instance):
    original = instance.Login_Status
    instance.Login_Status = original
    assert instance.Login_Status == original



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_Credit_Card_Info_setter(instance):
    original = instance.Credit_Card_Info
    instance.Credit_Card_Info = original
    assert instance.Credit_Card_Info == original



@given(instance=Customer_strategy)
def test_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Customer_strategy)
def test_customer_Customer_Name_setter(instance):
    original = instance.Customer_Name
    instance.Customer_Name = original
    assert instance.Customer_Name == original
