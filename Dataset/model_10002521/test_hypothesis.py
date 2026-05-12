import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Client_Register_external,
    Make_Purchase_external,
    View_Items_external,
    Identity_Provider_Actor,
    Authentication_Actor,
    Online_grocery_shopping_Component,
    New_Customer_Actor,
    Registered_customer__Actor,
    web_customer_Actor,
    Cancellation,
    Supplier,
    Product,
    Payment,
    Shopping_Cart,
    Customer,
    administrator,
    user,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_client_register_external_is_not_abstract():
    assert not inspect.isabstract(Client_Register_external)


def test_client_register_external_constructor_exists():
    assert callable(Client_Register_external.__init__)


def test_client_register_external_constructor_args():
    sig = inspect.signature(Client_Register_external.__init__)
    params = list(sig.parameters.keys())



def test_make_purchase_external_is_not_abstract():
    assert not inspect.isabstract(Make_Purchase_external)


def test_make_purchase_external_constructor_exists():
    assert callable(Make_Purchase_external.__init__)


def test_make_purchase_external_constructor_args():
    sig = inspect.signature(Make_Purchase_external.__init__)
    params = list(sig.parameters.keys())



def test_view_items_external_is_not_abstract():
    assert not inspect.isabstract(View_Items_external)


def test_view_items_external_constructor_exists():
    assert callable(View_Items_external.__init__)


def test_view_items_external_constructor_args():
    sig = inspect.signature(View_Items_external.__init__)
    params = list(sig.parameters.keys())



def test_identity_provider_actor_is_not_abstract():
    assert not inspect.isabstract(Identity_Provider_Actor)


def test_identity_provider_actor_constructor_exists():
    assert callable(Identity_Provider_Actor.__init__)


def test_identity_provider_actor_constructor_args():
    sig = inspect.signature(Identity_Provider_Actor.__init__)
    params = list(sig.parameters.keys())



def test_authentication_actor_is_not_abstract():
    assert not inspect.isabstract(Authentication_Actor)


def test_authentication_actor_constructor_exists():
    assert callable(Authentication_Actor.__init__)


def test_authentication_actor_constructor_args():
    sig = inspect.signature(Authentication_Actor.__init__)
    params = list(sig.parameters.keys())



def test_online_grocery_shopping_component_is_not_abstract():
    assert not inspect.isabstract(Online_grocery_shopping_Component)


def test_online_grocery_shopping_component_constructor_exists():
    assert callable(Online_grocery_shopping_Component.__init__)


def test_online_grocery_shopping_component_constructor_args():
    sig = inspect.signature(Online_grocery_shopping_Component.__init__)
    params = list(sig.parameters.keys())



def test_new_customer_actor_is_not_abstract():
    assert not inspect.isabstract(New_Customer_Actor)


def test_new_customer_actor_constructor_exists():
    assert callable(New_Customer_Actor.__init__)


def test_new_customer_actor_constructor_args():
    sig = inspect.signature(New_Customer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_registered_customer__actor_is_not_abstract():
    assert not inspect.isabstract(Registered_customer__Actor)


def test_registered_customer__actor_constructor_exists():
    assert callable(Registered_customer__Actor.__init__)


def test_registered_customer__actor_constructor_args():
    sig = inspect.signature(Registered_customer__Actor.__init__)
    params = list(sig.parameters.keys())



def test_web_customer_actor_is_not_abstract():
    assert not inspect.isabstract(web_customer_Actor)


def test_web_customer_actor_constructor_exists():
    assert callable(web_customer_Actor.__init__)


def test_web_customer_actor_constructor_args():
    sig = inspect.signature(web_customer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_cancellation_is_not_abstract():
    assert not inspect.isabstract(Cancellation)


def test_cancellation_constructor_exists():
    assert callable(Cancellation.__init__)


def test_cancellation_constructor_args():
    sig = inspect.signature(Cancellation.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "productID" in params, "Missing parameter 'productID'"
    assert "customerID" in params, "Missing parameter 'customerID'"

def test_cancellation_has_amount():
    assert hasattr(Cancellation, "amount")
    descriptor = None
    for klass in Cancellation.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_cancellation_has_productID():
    assert hasattr(Cancellation, "productID")
    descriptor = None
    for klass in Cancellation.__mro__:
        if "productID" in klass.__dict__:
            descriptor = klass.__dict__["productID"]
            break
    assert isinstance(descriptor, property)

def test_cancellation_has_customerID():
    assert hasattr(Cancellation, "customerID")
    descriptor = None
    for klass in Cancellation.__mro__:
        if "customerID" in klass.__dict__:
            descriptor = klass.__dict__["customerID"]
            break
    assert isinstance(descriptor, property)



def test_supplier_is_not_abstract():
    assert not inspect.isabstract(Supplier)


def test_supplier_constructor_exists():
    assert callable(Supplier.__init__)


def test_supplier_constructor_args():
    sig = inspect.signature(Supplier.__init__)
    params = list(sig.parameters.keys())
    assert "suppName" in params, "Missing parameter 'suppName'"
    assert "address" in params, "Missing parameter 'address'"
    assert "suppID" in params, "Missing parameter 'suppID'"

def test_supplier_has_suppName():
    assert hasattr(Supplier, "suppName")
    descriptor = None
    for klass in Supplier.__mro__:
        if "suppName" in klass.__dict__:
            descriptor = klass.__dict__["suppName"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_address():
    assert hasattr(Supplier, "address")
    descriptor = None
    for klass in Supplier.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_suppID():
    assert hasattr(Supplier, "suppID")
    descriptor = None
    for klass in Supplier.__mro__:
        if "suppID" in klass.__dict__:
            descriptor = klass.__dict__["suppID"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "price" in params, "Missing parameter 'price'"
    assert "productID" in params, "Missing parameter 'productID'"
    assert "name" in params, "Missing parameter 'name'"

def test_product_has_quantity():
    assert hasattr(Product, "quantity")
    descriptor = None
    for klass in Product.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
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

def test_product_has_productID():
    assert hasattr(Product, "productID")
    descriptor = None
    for klass in Product.__mro__:
        if "productID" in klass.__dict__:
            descriptor = klass.__dict__["productID"]
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



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "customerId" in params, "Missing parameter 'customerId'"
    assert "productID" in params, "Missing parameter 'productID'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_payment_has_customerId():
    assert hasattr(Payment, "customerId")
    descriptor = None
    for klass in Payment.__mro__:
        if "customerId" in klass.__dict__:
            descriptor = klass.__dict__["customerId"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_productID():
    assert hasattr(Payment, "productID")
    descriptor = None
    for klass in Payment.__mro__:
        if "productID" in klass.__dict__:
            descriptor = klass.__dict__["productID"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_amount():
    assert hasattr(Payment, "amount")
    descriptor = None
    for klass in Payment.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
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
    assert "cartId" in params, "Missing parameter 'cartId'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_shopping_cart_has_dateAdded():
    assert hasattr(Shopping_Cart, "dateAdded")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "dateAdded" in klass.__dict__:
            descriptor = klass.__dict__["dateAdded"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_cartId():
    assert hasattr(Shopping_Cart, "cartId")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "cartId" in klass.__dict__:
            descriptor = klass.__dict__["cartId"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_quantity():
    assert hasattr(Shopping_Cart, "quantity")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "mobileNo" in params, "Missing parameter 'mobileNo'"
    assert "loginName" in params, "Missing parameter 'loginName'"
    assert "address" in params, "Missing parameter 'address'"

def test_customer_has_mobileNo():
    assert hasattr(Customer, "mobileNo")
    descriptor = None
    for klass in Customer.__mro__:
        if "mobileNo" in klass.__dict__:
            descriptor = klass.__dict__["mobileNo"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_loginName():
    assert hasattr(Customer, "loginName")
    descriptor = None
    for klass in Customer.__mro__:
        if "loginName" in klass.__dict__:
            descriptor = klass.__dict__["loginName"]
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



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(administrator)


def test_administrator_constructor_exists():
    assert callable(administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(administrator.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "adminName" in params, "Missing parameter 'adminName'"

def test_administrator_has_email():
    assert hasattr(administrator, "email")
    descriptor = None
    for klass in administrator.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_adminName():
    assert hasattr(administrator, "adminName")
    descriptor = None
    for klass in administrator.__mro__:
        if "adminName" in klass.__dict__:
            descriptor = klass.__dict__["adminName"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(user)


def test_user_constructor_exists():
    assert callable(user.__init__)


def test_user_constructor_args():
    sig = inspect.signature(user.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"

def test_user_has_password():
    assert hasattr(user, "password")
    descriptor = None
    for klass in user.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_userID():
    assert hasattr(user, "userID")
    descriptor = None
    for klass in user.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_user_has_loginStatus():
    assert hasattr(user, "loginStatus")
    descriptor = None
    for klass in user.__mro__:
        if "loginStatus" in klass.__dict__:
            descriptor = klass.__dict__["loginStatus"]
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
Client_Register_external_strategy = st.builds(
    Client_Register_external,
)
Make_Purchase_external_strategy = st.builds(
    Make_Purchase_external,
)
View_Items_external_strategy = st.builds(
    View_Items_external,
)
Identity_Provider_Actor_strategy = st.builds(
    Identity_Provider_Actor,
)
Authentication_Actor_strategy = st.builds(
    Authentication_Actor,
)
Online_grocery_shopping_Component_strategy = st.builds(
    Online_grocery_shopping_Component,
)
New_Customer_Actor_strategy = st.builds(
    New_Customer_Actor,
)
Registered_customer__Actor_strategy = st.builds(
    Registered_customer__Actor,
)
web_customer_Actor_strategy = st.builds(
    web_customer_Actor,
)
Cancellation_strategy = st.builds(
    Cancellation,
    amount=
        safe_text,
    productID=
        safe_text,
    customerID=
        safe_text
)
Supplier_strategy = st.builds(
    Supplier,
    suppName=
        safe_text,
    address=
        safe_text,
    suppID=
        safe_text
)
Product_strategy = st.builds(
    Product,
    quantity=
        st.integers(),
    price=
        st.integers(),
    productID=
        safe_text,
    name=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    customerId=
        safe_text,
    productID=
        safe_text,
    amount=
        st.integers()
)
Shopping_Cart_strategy = st.builds(
    Shopping_Cart,
    dateAdded=
        safe_text,
    cartId=
        safe_text,
    quantity=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    mobileNo=
        st.integers(),
    loginName=
        safe_text,
    address=
        safe_text
)
administrator_strategy = st.builds(
    administrator,
    email=
        safe_text,
    adminName=
        safe_text
)
user_strategy = st.builds(
    user,
    password=
        safe_text,
    userID=
        safe_text,
    loginStatus=
        safe_text
)

@given(instance=Client_Register_external_strategy)
@settings(max_examples=50)
def test_client_register_external_instantiation(instance):
    assert isinstance(instance, Client_Register_external)

@given(instance=Make_Purchase_external_strategy)
@settings(max_examples=50)
def test_make_purchase_external_instantiation(instance):
    assert isinstance(instance, Make_Purchase_external)

@given(instance=View_Items_external_strategy)
@settings(max_examples=50)
def test_view_items_external_instantiation(instance):
    assert isinstance(instance, View_Items_external)

@given(instance=Identity_Provider_Actor_strategy)
@settings(max_examples=50)
def test_identity_provider_actor_instantiation(instance):
    assert isinstance(instance, Identity_Provider_Actor)

@given(instance=Authentication_Actor_strategy)
@settings(max_examples=50)
def test_authentication_actor_instantiation(instance):
    assert isinstance(instance, Authentication_Actor)

@given(instance=Online_grocery_shopping_Component_strategy)
@settings(max_examples=50)
def test_online_grocery_shopping_component_instantiation(instance):
    assert isinstance(instance, Online_grocery_shopping_Component)

@given(instance=New_Customer_Actor_strategy)
@settings(max_examples=50)
def test_new_customer_actor_instantiation(instance):
    assert isinstance(instance, New_Customer_Actor)

@given(instance=Registered_customer__Actor_strategy)
@settings(max_examples=50)
def test_registered_customer__actor_instantiation(instance):
    assert isinstance(instance, Registered_customer__Actor)

@given(instance=web_customer_Actor_strategy)
@settings(max_examples=50)
def test_web_customer_actor_instantiation(instance):
    assert isinstance(instance, web_customer_Actor)

@given(instance=Cancellation_strategy)
@settings(max_examples=50)
def test_cancellation_instantiation(instance):
    assert isinstance(instance, Cancellation)



@given(instance=Cancellation_strategy)
def test_cancellation_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Cancellation_strategy)
def test_cancellation_productID_setter(instance):
    original = instance.productID
    instance.productID = original
    assert instance.productID == original



@given(instance=Cancellation_strategy)
def test_cancellation_customerID_setter(instance):
    original = instance.customerID
    instance.customerID = original
    assert instance.customerID == original

@given(instance=Supplier_strategy)
@settings(max_examples=50)
def test_supplier_instantiation(instance):
    assert isinstance(instance, Supplier)



@given(instance=Supplier_strategy)
def test_supplier_suppName_setter(instance):
    original = instance.suppName
    instance.suppName = original
    assert instance.suppName == original



@given(instance=Supplier_strategy)
def test_supplier_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Supplier_strategy)
def test_supplier_suppID_setter(instance):
    original = instance.suppID
    instance.suppID = original
    assert instance.suppID == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Product_strategy)
def test_product_productID_setter(instance):
    original = instance.productID
    instance.productID = original
    assert instance.productID == original



@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_customerId_setter(instance):
    original = instance.customerId
    instance.customerId = original
    assert instance.customerId == original



@given(instance=Payment_strategy)
def test_payment_productID_setter(instance):
    original = instance.productID
    instance.productID = original
    assert instance.productID == original



@given(instance=Payment_strategy)
def test_payment_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

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
def test_shopping_cart_cartId_setter(instance):
    original = instance.cartId
    instance.cartId = original
    assert instance.cartId == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_mobileNo_setter(instance):
    original = instance.mobileNo
    instance.mobileNo = original
    assert instance.mobileNo == original



@given(instance=Customer_strategy)
def test_customer_loginName_setter(instance):
    original = instance.loginName
    instance.loginName = original
    assert instance.loginName == original



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, administrator)



@given(instance=administrator_strategy)
def test_administrator_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=administrator_strategy)
def test_administrator_adminName_setter(instance):
    original = instance.adminName
    instance.adminName = original
    assert instance.adminName == original

@given(instance=user_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, user)



@given(instance=user_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=user_strategy)
def test_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=user_strategy)
def test_user_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original
