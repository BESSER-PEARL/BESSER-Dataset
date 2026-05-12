import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    delivery,
    supplier,
    gest,
    cart,
    product,
    Payment,
    char,
    customer,
    admin,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_delivery_is_not_abstract():
    assert not inspect.isabstract(delivery)


def test_delivery_constructor_exists():
    assert callable(delivery.__init__)


def test_delivery_constructor_args():
    sig = inspect.signature(delivery.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"

def test_delivery_has_password():
    assert hasattr(delivery, "password")
    descriptor = None
    for klass in delivery.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_delivery_has_name():
    assert hasattr(delivery, "name")
    descriptor = None
    for klass in delivery.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_supplier_is_not_abstract():
    assert not inspect.isabstract(supplier)


def test_supplier_constructor_exists():
    assert callable(supplier.__init__)


def test_supplier_constructor_args():
    sig = inspect.signature(supplier.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"

def test_supplier_has_password():
    assert hasattr(supplier, "password")
    descriptor = None
    for klass in supplier.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_name():
    assert hasattr(supplier, "name")
    descriptor = None
    for klass in supplier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gest_is_not_abstract():
    assert not inspect.isabstract(gest)


def test_gest_constructor_exists():
    assert callable(gest.__init__)


def test_gest_constructor_args():
    sig = inspect.signature(gest.__init__)
    params = list(sig.parameters.keys())



def test_cart_is_not_abstract():
    assert not inspect.isabstract(cart)


def test_cart_constructor_exists():
    assert callable(cart.__init__)


def test_cart_constructor_args():
    sig = inspect.signature(cart.__init__)
    params = list(sig.parameters.keys())
    assert "productn" in params, "Missing parameter 'productn'"
    assert "total" in params, "Missing parameter 'total'"
    assert "price" in params, "Missing parameter 'price'"
    assert "id" in params, "Missing parameter 'id'"
    assert "NumberOfProduct" in params, "Missing parameter 'NumberOfProduct'"
    assert "product2" in params, "Missing parameter 'product2'"
    assert "product1" in params, "Missing parameter 'product1'"

def test_cart_has_productn():
    assert hasattr(cart, "productn")
    descriptor = None
    for klass in cart.__mro__:
        if "productn" in klass.__dict__:
            descriptor = klass.__dict__["productn"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_total():
    assert hasattr(cart, "total")
    descriptor = None
    for klass in cart.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_price():
    assert hasattr(cart, "price")
    descriptor = None
    for klass in cart.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_id():
    assert hasattr(cart, "id")
    descriptor = None
    for klass in cart.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_NumberOfProduct():
    assert hasattr(cart, "NumberOfProduct")
    descriptor = None
    for klass in cart.__mro__:
        if "NumberOfProduct" in klass.__dict__:
            descriptor = klass.__dict__["NumberOfProduct"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_product2():
    assert hasattr(cart, "product2")
    descriptor = None
    for klass in cart.__mro__:
        if "product2" in klass.__dict__:
            descriptor = klass.__dict__["product2"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_product1():
    assert hasattr(cart, "product1")
    descriptor = None
    for klass in cart.__mro__:
        if "product1" in klass.__dict__:
            descriptor = klass.__dict__["product1"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(product)


def test_product_constructor_exists():
    assert callable(product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(product.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"
    assert "subgroub" in params, "Missing parameter 'subgroub'"
    assert "id" in params, "Missing parameter 'id'"

def test_product_has_group():
    assert hasattr(product, "group")
    descriptor = None
    for klass in product.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_product_has_name():
    assert hasattr(product, "name")
    descriptor = None
    for klass in product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_product_has_subgroub():
    assert hasattr(product, "subgroub")
    descriptor = None
    for klass in product.__mro__:
        if "subgroub" in klass.__dict__:
            descriptor = klass.__dict__["subgroub"]
            break
    assert isinstance(descriptor, property)

def test_product_has_id():
    assert hasattr(product, "id")
    descriptor = None
    for klass in product.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "customerName" in params, "Missing parameter 'customerName'"
    assert "customerName1" in params, "Missing parameter 'customerName1'"
    assert "cardType" in params, "Missing parameter 'cardType'"
    assert "cardNo" in params, "Missing parameter 'cardNo'"

def test_payment_has_customerName():
    assert hasattr(Payment, "customerName")
    descriptor = None
    for klass in Payment.__mro__:
        if "customerName" in klass.__dict__:
            descriptor = klass.__dict__["customerName"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_customerName1():
    assert hasattr(Payment, "customerName1")
    descriptor = None
    for klass in Payment.__mro__:
        if "customerName1" in klass.__dict__:
            descriptor = klass.__dict__["customerName1"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_cardType():
    assert hasattr(Payment, "cardType")
    descriptor = None
    for klass in Payment.__mro__:
        if "cardType" in klass.__dict__:
            descriptor = klass.__dict__["cardType"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_cardNo():
    assert hasattr(Payment, "cardNo")
    descriptor = None
    for klass in Payment.__mro__:
        if "cardNo" in klass.__dict__:
            descriptor = klass.__dict__["cardNo"]
            break
    assert isinstance(descriptor, property)



def test_char_is_not_abstract():
    assert not inspect.isabstract(char)


def test_char_constructor_exists():
    assert callable(char.__init__)


def test_char_constructor_args():
    sig = inspect.signature(char.__init__)
    params = list(sig.parameters.keys())



def test_customer_is_not_abstract():
    assert not inspect.isabstract(customer)


def test_customer_constructor_exists():
    assert callable(customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(customer.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "phone" in params, "Missing parameter 'phone'"

def test_customer_has_email():
    assert hasattr(customer, "email")
    descriptor = None
    for klass in customer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_password():
    assert hasattr(customer, "password")
    descriptor = None
    for klass in customer.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_name():
    assert hasattr(customer, "name")
    descriptor = None
    for klass in customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_address():
    assert hasattr(customer, "address")
    descriptor = None
    for klass in customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_phone():
    assert hasattr(customer, "phone")
    descriptor = None
    for klass in customer.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(admin)


def test_admin_constructor_exists():
    assert callable(admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(admin.__init__)
    params = list(sig.parameters.keys())
    assert "user_mobile" in params, "Missing parameter 'user_mobile'"
    assert "user_name" in params, "Missing parameter 'user_name'"
    assert "user_type" in params, "Missing parameter 'user_type'"

def test_admin_has_user_mobile():
    assert hasattr(admin, "user_mobile")
    descriptor = None
    for klass in admin.__mro__:
        if "user_mobile" in klass.__dict__:
            descriptor = klass.__dict__["user_mobile"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_user_name():
    assert hasattr(admin, "user_name")
    descriptor = None
    for klass in admin.__mro__:
        if "user_name" in klass.__dict__:
            descriptor = klass.__dict__["user_name"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_user_type():
    assert hasattr(admin, "user_type")
    descriptor = None
    for klass in admin.__mro__:
        if "user_type" in klass.__dict__:
            descriptor = klass.__dict__["user_type"]
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
delivery_strategy = st.builds(
    delivery,
    password=
        st.none(),
    name=
        st.none()
)
supplier_strategy = st.builds(
    supplier,
    password=
        st.integers(),
    name=
        st.none()
)
gest_strategy = st.builds(
    gest,
)
cart_strategy = st.builds(
    cart,
    productn=
        st.none(),
    total=
        safe_text,
    price=
        safe_text,
    id=
        st.integers(),
    NumberOfProduct=
        st.integers(),
    product2=
        st.none(),
    product1=
        st.none()
)
product_strategy = st.builds(
    product,
    group=
        st.none(),
    name=
        st.none(),
    subgroub=
        st.none(),
    id=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    customerName=
        st.none(),
    customerName1=
        st.none(),
    cardType=
        st.none(),
    cardNo=
        st.integers()
)
char_strategy = st.builds(
    char,
)
customer_strategy = st.builds(
    customer,
    email=
        st.none(),
    password=
        st.integers(),
    name=
        st.none(),
    address=
        st.none(),
    phone=
        st.integers()
)
admin_strategy = st.builds(
    admin,
    user_mobile=
        st.integers(),
    user_name=
        safe_text,
    user_type=
        st.integers()
)

@given(instance=delivery_strategy)
@settings(max_examples=50)
def test_delivery_instantiation(instance):
    assert isinstance(instance, delivery)



@given(instance=delivery_strategy)
def test_delivery_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=delivery_strategy)
def test_delivery_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=supplier_strategy)
@settings(max_examples=50)
def test_supplier_instantiation(instance):
    assert isinstance(instance, supplier)



@given(instance=supplier_strategy)
def test_supplier_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=supplier_strategy)
def test_supplier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gest_strategy)
@settings(max_examples=50)
def test_gest_instantiation(instance):
    assert isinstance(instance, gest)

@given(instance=cart_strategy)
@settings(max_examples=50)
def test_cart_instantiation(instance):
    assert isinstance(instance, cart)



@given(instance=cart_strategy)
def test_cart_productn_setter(instance):
    original = instance.productn
    instance.productn = original
    assert instance.productn == original



@given(instance=cart_strategy)
def test_cart_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=cart_strategy)
def test_cart_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=cart_strategy)
def test_cart_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=cart_strategy)
def test_cart_NumberOfProduct_setter(instance):
    original = instance.NumberOfProduct
    instance.NumberOfProduct = original
    assert instance.NumberOfProduct == original



@given(instance=cart_strategy)
def test_cart_product2_setter(instance):
    original = instance.product2
    instance.product2 = original
    assert instance.product2 == original



@given(instance=cart_strategy)
def test_cart_product1_setter(instance):
    original = instance.product1
    instance.product1 = original
    assert instance.product1 == original

@given(instance=product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, product)



@given(instance=product_strategy)
def test_product_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=product_strategy)
def test_product_subgroub_setter(instance):
    original = instance.subgroub
    instance.subgroub = original
    assert instance.subgroub == original



@given(instance=product_strategy)
def test_product_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_customerName_setter(instance):
    original = instance.customerName
    instance.customerName = original
    assert instance.customerName == original



@given(instance=Payment_strategy)
def test_payment_customerName1_setter(instance):
    original = instance.customerName1
    instance.customerName1 = original
    assert instance.customerName1 == original



@given(instance=Payment_strategy)
def test_payment_cardType_setter(instance):
    original = instance.cardType
    instance.cardType = original
    assert instance.cardType == original



@given(instance=Payment_strategy)
def test_payment_cardNo_setter(instance):
    original = instance.cardNo
    instance.cardNo = original
    assert instance.cardNo == original

@given(instance=char_strategy)
@settings(max_examples=50)
def test_char_instantiation(instance):
    assert isinstance(instance, char)

@given(instance=customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, customer)



@given(instance=customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=customer_strategy)
def test_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=customer_strategy)
def test_customer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original

@given(instance=admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, admin)



@given(instance=admin_strategy)
def test_admin_user_mobile_setter(instance):
    original = instance.user_mobile
    instance.user_mobile = original
    assert instance.user_mobile == original



@given(instance=admin_strategy)
def test_admin_user_name_setter(instance):
    original = instance.user_name
    instance.user_name = original
    assert instance.user_name == original



@given(instance=admin_strategy)
def test_admin_user_type_setter(instance):
    original = instance.user_type
    instance.user_type = original
    assert instance.user_type == original
