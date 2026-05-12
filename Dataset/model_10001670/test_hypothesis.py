import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Custom_Login,
    Social_Login,
    Corporate_Order,
    Phone_Order,
    Items,
    Account,
    Order,
    Payment,
    Shopping_Cart,
    Products,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_custom_login_is_not_abstract():
    assert not inspect.isabstract(Custom_Login)


def test_custom_login_constructor_exists():
    assert callable(Custom_Login.__init__)


def test_custom_login_constructor_args():
    sig = inspect.signature(Custom_Login.__init__)
    params = list(sig.parameters.keys())
    assert "Login" in params, "Missing parameter 'Login'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_custom_login_has_Login():
    assert hasattr(Custom_Login, "Login")
    descriptor = None
    for klass in Custom_Login.__mro__:
        if "Login" in klass.__dict__:
            descriptor = klass.__dict__["Login"]
            break
    assert isinstance(descriptor, property)

def test_custom_login_has_Password():
    assert hasattr(Custom_Login, "Password")
    descriptor = None
    for klass in Custom_Login.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_social_login_is_not_abstract():
    assert not inspect.isabstract(Social_Login)


def test_social_login_constructor_exists():
    assert callable(Social_Login.__init__)


def test_social_login_constructor_args():
    sig = inspect.signature(Social_Login.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"

def test_social_login_has_email():
    assert hasattr(Social_Login, "email")
    descriptor = None
    for klass in Social_Login.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_social_login_has_password():
    assert hasattr(Social_Login, "password")
    descriptor = None
    for klass in Social_Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_corporate_order_is_not_abstract():
    assert not inspect.isabstract(Corporate_Order)


def test_corporate_order_constructor_exists():
    assert callable(Corporate_Order.__init__)


def test_corporate_order_constructor_args():
    sig = inspect.signature(Corporate_Order.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"

def test_corporate_order_has_Date():
    assert hasattr(Corporate_Order, "Date")
    descriptor = None
    for klass in Corporate_Order.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_phone_order_is_not_abstract():
    assert not inspect.isabstract(Phone_Order)


def test_phone_order_constructor_exists():
    assert callable(Phone_Order.__init__)


def test_phone_order_constructor_args():
    sig = inspect.signature(Phone_Order.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"

def test_phone_order_has_Date():
    assert hasattr(Phone_Order, "Date")
    descriptor = None
    for klass in Phone_Order.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_items_is_not_abstract():
    assert not inspect.isabstract(Items)


def test_items_constructor_exists():
    assert callable(Items.__init__)


def test_items_constructor_args():
    sig = inspect.signature(Items.__init__)
    params = list(sig.parameters.keys())
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "SKUCode" in params, "Missing parameter 'SKUCode'"

def test_items_has_Quantity():
    assert hasattr(Items, "Quantity")
    descriptor = None
    for klass in Items.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_items_has_SKUCode():
    assert hasattr(Items, "SKUCode")
    descriptor = None
    for klass in Items.__mro__:
        if "SKUCode" in klass.__dict__:
            descriptor = klass.__dict__["SKUCode"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "ContactNo" in params, "Missing parameter 'ContactNo'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_account_has_Email():
    assert hasattr(Account, "Email")
    descriptor = None
    for klass in Account.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_account_has_ContactNo():
    assert hasattr(Account, "ContactNo")
    descriptor = None
    for klass in Account.__mro__:
        if "ContactNo" in klass.__dict__:
            descriptor = klass.__dict__["ContactNo"]
            break
    assert isinstance(descriptor, property)

def test_account_has_Address():
    assert hasattr(Account, "Address")
    descriptor = None
    for klass in Account.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Order_ID" in params, "Missing parameter 'Order_ID'"
    assert "ReceipientAddress" in params, "Missing parameter 'ReceipientAddress'"
    assert "GiftMessage" in params, "Missing parameter 'GiftMessage'"
    assert "ReceipientContactNo" in params, "Missing parameter 'ReceipientContactNo'"
    assert "ReceipientName" in params, "Missing parameter 'ReceipientName'"
    assert "ReceipientEmail" in params, "Missing parameter 'ReceipientEmail'"

def test_order_has_Order_ID():
    assert hasattr(Order, "Order_ID")
    descriptor = None
    for klass in Order.__mro__:
        if "Order_ID" in klass.__dict__:
            descriptor = klass.__dict__["Order_ID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ReceipientAddress():
    assert hasattr(Order, "ReceipientAddress")
    descriptor = None
    for klass in Order.__mro__:
        if "ReceipientAddress" in klass.__dict__:
            descriptor = klass.__dict__["ReceipientAddress"]
            break
    assert isinstance(descriptor, property)

def test_order_has_GiftMessage():
    assert hasattr(Order, "GiftMessage")
    descriptor = None
    for klass in Order.__mro__:
        if "GiftMessage" in klass.__dict__:
            descriptor = klass.__dict__["GiftMessage"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ReceipientContactNo():
    assert hasattr(Order, "ReceipientContactNo")
    descriptor = None
    for klass in Order.__mro__:
        if "ReceipientContactNo" in klass.__dict__:
            descriptor = klass.__dict__["ReceipientContactNo"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ReceipientName():
    assert hasattr(Order, "ReceipientName")
    descriptor = None
    for klass in Order.__mro__:
        if "ReceipientName" in klass.__dict__:
            descriptor = klass.__dict__["ReceipientName"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ReceipientEmail():
    assert hasattr(Order, "ReceipientEmail")
    descriptor = None
    for klass in Order.__mro__:
        if "ReceipientEmail" in klass.__dict__:
            descriptor = klass.__dict__["ReceipientEmail"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Payment_ID" in params, "Missing parameter 'Payment_ID'"
    assert "Date" in params, "Missing parameter 'Date'"

def test_payment_has_Payment_ID():
    assert hasattr(Payment, "Payment_ID")
    descriptor = None
    for klass in Payment.__mro__:
        if "Payment_ID" in klass.__dict__:
            descriptor = klass.__dict__["Payment_ID"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Date():
    assert hasattr(Payment, "Date")
    descriptor = None
    for klass in Payment.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_Cart)


def test_shopping_cart_constructor_exists():
    assert callable(Shopping_Cart.__init__)


def test_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_Cart.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"

def test_shopping_cart_has_Date():
    assert hasattr(Shopping_Cart, "Date")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_products_is_not_abstract():
    assert not inspect.isabstract(Products)


def test_products_constructor_exists():
    assert callable(Products.__init__)


def test_products_constructor_args():
    sig = inspect.signature(Products.__init__)
    params = list(sig.parameters.keys())
    assert "Product_Name" in params, "Missing parameter 'Product_Name'"
    assert "SKU_Code" in params, "Missing parameter 'SKU_Code'"

def test_products_has_Product_Name():
    assert hasattr(Products, "Product_Name")
    descriptor = None
    for klass in Products.__mro__:
        if "Product_Name" in klass.__dict__:
            descriptor = klass.__dict__["Product_Name"]
            break
    assert isinstance(descriptor, property)

def test_products_has_SKU_Code():
    assert hasattr(Products, "SKU_Code")
    descriptor = None
    for klass in Products.__mro__:
        if "SKU_Code" in klass.__dict__:
            descriptor = klass.__dict__["SKU_Code"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Customer_ID" in params, "Missing parameter 'Customer_ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_customer_has_Customer_ID():
    assert hasattr(Customer, "Customer_ID")
    descriptor = None
    for klass in Customer.__mro__:
        if "Customer_ID" in klass.__dict__:
            descriptor = klass.__dict__["Customer_ID"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Name():
    assert hasattr(Customer, "Name")
    descriptor = None
    for klass in Customer.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
Custom_Login_strategy = st.builds(
    Custom_Login,
    Login=
        safe_text,
    Password=
        safe_text
)
Social_Login_strategy = st.builds(
    Social_Login,
    email=
        safe_text,
    password=
        safe_text
)
Corporate_Order_strategy = st.builds(
    Corporate_Order,
    Date=
        safe_text
)
Phone_Order_strategy = st.builds(
    Phone_Order,
    Date=
        safe_text
)
Items_strategy = st.builds(
    Items,
    Quantity=
        safe_text,
    SKUCode=
        safe_text
)
Account_strategy = st.builds(
    Account,
    Email=
        safe_text,
    ContactNo=
        safe_text,
    Address=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Order_ID=
        safe_text,
    ReceipientAddress=
        safe_text,
    GiftMessage=
        safe_text,
    ReceipientContactNo=
        safe_text,
    ReceipientName=
        safe_text,
    ReceipientEmail=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    Payment_ID=
        safe_text,
    Date=
        st.integers()
)
Shopping_Cart_strategy = st.builds(
    Shopping_Cart,
    Date=
        safe_text
)
Products_strategy = st.builds(
    Products,
    Product_Name=
        safe_text,
    SKU_Code=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    Customer_ID=
        safe_text,
    Name=
        safe_text
)

@given(instance=Custom_Login_strategy)
@settings(max_examples=50)
def test_custom_login_instantiation(instance):
    assert isinstance(instance, Custom_Login)



@given(instance=Custom_Login_strategy)
def test_custom_login_Login_setter(instance):
    original = instance.Login
    instance.Login = original
    assert instance.Login == original



@given(instance=Custom_Login_strategy)
def test_custom_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Social_Login_strategy)
@settings(max_examples=50)
def test_social_login_instantiation(instance):
    assert isinstance(instance, Social_Login)



@given(instance=Social_Login_strategy)
def test_social_login_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Social_Login_strategy)
def test_social_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Corporate_Order_strategy)
@settings(max_examples=50)
def test_corporate_order_instantiation(instance):
    assert isinstance(instance, Corporate_Order)



@given(instance=Corporate_Order_strategy)
def test_corporate_order_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Phone_Order_strategy)
@settings(max_examples=50)
def test_phone_order_instantiation(instance):
    assert isinstance(instance, Phone_Order)



@given(instance=Phone_Order_strategy)
def test_phone_order_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Items_strategy)
@settings(max_examples=50)
def test_items_instantiation(instance):
    assert isinstance(instance, Items)



@given(instance=Items_strategy)
def test_items_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Items_strategy)
def test_items_SKUCode_setter(instance):
    original = instance.SKUCode
    instance.SKUCode = original
    assert instance.SKUCode == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Account_strategy)
def test_account_ContactNo_setter(instance):
    original = instance.ContactNo
    instance.ContactNo = original
    assert instance.ContactNo == original



@given(instance=Account_strategy)
def test_account_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Order_ID_setter(instance):
    original = instance.Order_ID
    instance.Order_ID = original
    assert instance.Order_ID == original



@given(instance=Order_strategy)
def test_order_ReceipientAddress_setter(instance):
    original = instance.ReceipientAddress
    instance.ReceipientAddress = original
    assert instance.ReceipientAddress == original



@given(instance=Order_strategy)
def test_order_GiftMessage_setter(instance):
    original = instance.GiftMessage
    instance.GiftMessage = original
    assert instance.GiftMessage == original



@given(instance=Order_strategy)
def test_order_ReceipientContactNo_setter(instance):
    original = instance.ReceipientContactNo
    instance.ReceipientContactNo = original
    assert instance.ReceipientContactNo == original



@given(instance=Order_strategy)
def test_order_ReceipientName_setter(instance):
    original = instance.ReceipientName
    instance.ReceipientName = original
    assert instance.ReceipientName == original



@given(instance=Order_strategy)
def test_order_ReceipientEmail_setter(instance):
    original = instance.ReceipientEmail
    instance.ReceipientEmail = original
    assert instance.ReceipientEmail == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_Payment_ID_setter(instance):
    original = instance.Payment_ID
    instance.Payment_ID = original
    assert instance.Payment_ID == original



@given(instance=Payment_strategy)
def test_payment_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Shopping_Cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart)



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Products_strategy)
@settings(max_examples=50)
def test_products_instantiation(instance):
    assert isinstance(instance, Products)



@given(instance=Products_strategy)
def test_products_Product_Name_setter(instance):
    original = instance.Product_Name
    instance.Product_Name = original
    assert instance.Product_Name == original



@given(instance=Products_strategy)
def test_products_SKU_Code_setter(instance):
    original = instance.SKU_Code
    instance.SKU_Code = original
    assert instance.SKU_Code == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_Customer_ID_setter(instance):
    original = instance.Customer_ID
    instance.Customer_ID = original
    assert instance.Customer_ID == original



@given(instance=Customer_strategy)
def test_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
