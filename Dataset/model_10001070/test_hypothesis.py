import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Shopping_Cart,
    Order,
    Payment,
    Content,
    __enumeration___OderStatus,
    Customer,
    Product,
    New_Customer,
    __enumeration___UserState,
    Registered_Customer,
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
    assert "total" in params, "Missing parameter 'total'"
    assert "number" in params, "Missing parameter 'number'"
    assert "id" in params, "Missing parameter 'id'"

def test_shopping_cart_has_total():
    assert hasattr(Shopping_Cart, "total")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_number():
    assert hasattr(Shopping_Cart, "number")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_id():
    assert hasattr(Shopping_Cart, "id")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "shipped" in params, "Missing parameter 'shipped'"
    assert "ship_to" in params, "Missing parameter 'ship_to'"
    assert "number" in params, "Missing parameter 'number'"
    assert "ordered" in params, "Missing parameter 'ordered'"

def test_order_has_shipped():
    assert hasattr(Order, "shipped")
    descriptor = None
    for klass in Order.__mro__:
        if "shipped" in klass.__dict__:
            descriptor = klass.__dict__["shipped"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ship_to():
    assert hasattr(Order, "ship_to")
    descriptor = None
    for klass in Order.__mro__:
        if "ship_to" in klass.__dict__:
            descriptor = klass.__dict__["ship_to"]
            break
    assert isinstance(descriptor, property)

def test_order_has_number():
    assert hasattr(Order, "number")
    descriptor = None
    for klass in Order.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ordered():
    assert hasattr(Order, "ordered")
    descriptor = None
    for klass in Order.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "details" in params, "Missing parameter 'details'"
    assert "id" in params, "Missing parameter 'id'"
    assert "paid" in params, "Missing parameter 'paid'"
    assert "total" in params, "Missing parameter 'total'"

def test_payment_has_details():
    assert hasattr(Payment, "details")
    descriptor = None
    for klass in Payment.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_id():
    assert hasattr(Payment, "id")
    descriptor = None
    for klass in Payment.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_paid():
    assert hasattr(Payment, "paid")
    descriptor = None
    for klass in Payment.__mro__:
        if "paid" in klass.__dict__:
            descriptor = klass.__dict__["paid"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_total():
    assert hasattr(Payment, "total")
    descriptor = None
    for klass in Payment.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)



def test_content_is_not_abstract():
    assert not inspect.isabstract(Content)


def test_content_constructor_exists():
    assert callable(Content.__init__)


def test_content_constructor_args():
    sig = inspect.signature(Content.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "price" in params, "Missing parameter 'price'"

def test_content_has_quantity():
    assert hasattr(Content, "quantity")
    descriptor = None
    for klass in Content.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_content_has_price():
    assert hasattr(Content, "price")
    descriptor = None
    for klass in Content.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test___enumeration___oderstatus_is_not_abstract():
    assert not inspect.isabstract(__enumeration___OderStatus)


def test___enumeration___oderstatus_constructor_exists():
    assert callable(__enumeration___OderStatus.__init__)


def test___enumeration___oderstatus_constructor_args():
    sig = inspect.signature(__enumeration___OderStatus.__init__)
    params = list(sig.parameters.keys())
    assert "closed" in params, "Missing parameter 'closed'"
    assert "hold" in params, "Missing parameter 'hold'"
    assert "new" in params, "Missing parameter 'new'"
    assert "return" in params, "Missing parameter 'return'"
    assert "delivery" in params, "Missing parameter 'delivery'"
    assert "shipped" in params, "Missing parameter 'shipped'"

def test___enumeration___oderstatus_has_closed():
    assert hasattr(__enumeration___OderStatus, "closed")
    descriptor = None
    for klass in __enumeration___OderStatus.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)

def test___enumeration___oderstatus_has_hold():
    assert hasattr(__enumeration___OderStatus, "hold")
    descriptor = None
    for klass in __enumeration___OderStatus.__mro__:
        if "hold" in klass.__dict__:
            descriptor = klass.__dict__["hold"]
            break
    assert isinstance(descriptor, property)

def test___enumeration___oderstatus_has_new():
    assert hasattr(__enumeration___OderStatus, "new")
    descriptor = None
    for klass in __enumeration___OderStatus.__mro__:
        if "new" in klass.__dict__:
            descriptor = klass.__dict__["new"]
            break
    assert isinstance(descriptor, property)

def test___enumeration___oderstatus_has_return():
    assert hasattr(__enumeration___OderStatus, "return")
    descriptor = None
    for klass in __enumeration___OderStatus.__mro__:
        if "return" in klass.__dict__:
            descriptor = klass.__dict__["return"]
            break
    assert isinstance(descriptor, property)

def test___enumeration___oderstatus_has_delivery():
    assert hasattr(__enumeration___OderStatus, "delivery")
    descriptor = None
    for klass in __enumeration___OderStatus.__mro__:
        if "delivery" in klass.__dict__:
            descriptor = klass.__dict__["delivery"]
            break
    assert isinstance(descriptor, property)

def test___enumeration___oderstatus_has_shipped():
    assert hasattr(__enumeration___OderStatus, "shipped")
    descriptor = None
    for klass in __enumeration___OderStatus.__mro__:
        if "shipped" in klass.__dict__:
            descriptor = klass.__dict__["shipped"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"

def test_customer_has_address():
    assert hasattr(Customer, "address")
    descriptor = None
    for klass in Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_phone():
    assert hasattr(Customer, "phone")
    descriptor = None
    for klass in Customer.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "supplier" in params, "Missing parameter 'supplier'"

def test_product_has_name():
    assert hasattr(Product, "name")
    descriptor = None
    for klass in Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_product_has_id():
    assert hasattr(Product, "id")
    descriptor = None
    for klass in Product.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_product_has_supplier():
    assert hasattr(Product, "supplier")
    descriptor = None
    for klass in Product.__mro__:
        if "supplier" in klass.__dict__:
            descriptor = klass.__dict__["supplier"]
            break
    assert isinstance(descriptor, property)



def test_new_customer_is_not_abstract():
    assert not inspect.isabstract(New_Customer)


def test_new_customer_constructor_exists():
    assert callable(New_Customer.__init__)


def test_new_customer_constructor_args():
    sig = inspect.signature(New_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "password" in params, "Missing parameter 'password'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "email" in params, "Missing parameter 'email'"

def test_new_customer_has_address():
    assert hasattr(New_Customer, "address")
    descriptor = None
    for klass in New_Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_new_customer_has_phone():
    assert hasattr(New_Customer, "phone")
    descriptor = None
    for klass in New_Customer.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_new_customer_has_password():
    assert hasattr(New_Customer, "password")
    descriptor = None
    for klass in New_Customer.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_new_customer_has_Name():
    assert hasattr(New_Customer, "Name")
    descriptor = None
    for klass in New_Customer.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_new_customer_has_email():
    assert hasattr(New_Customer, "email")
    descriptor = None
    for klass in New_Customer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test___enumeration___userstate_is_not_abstract():
    assert not inspect.isabstract(__enumeration___UserState)


def test___enumeration___userstate_constructor_exists():
    assert callable(__enumeration___UserState.__init__)


def test___enumeration___userstate_constructor_args():
    sig = inspect.signature(__enumeration___UserState.__init__)
    params = list(sig.parameters.keys())
    assert "new" in params, "Missing parameter 'new'"
    assert "banned" in params, "Missing parameter 'banned'"
    assert "blocked" in params, "Missing parameter 'blocked'"
    assert "active" in params, "Missing parameter 'active'"

def test___enumeration___userstate_has_new():
    assert hasattr(__enumeration___UserState, "new")
    descriptor = None
    for klass in __enumeration___UserState.__mro__:
        if "new" in klass.__dict__:
            descriptor = klass.__dict__["new"]
            break
    assert isinstance(descriptor, property)

def test___enumeration___userstate_has_banned():
    assert hasattr(__enumeration___UserState, "banned")
    descriptor = None
    for klass in __enumeration___UserState.__mro__:
        if "banned" in klass.__dict__:
            descriptor = klass.__dict__["banned"]
            break
    assert isinstance(descriptor, property)

def test___enumeration___userstate_has_blocked():
    assert hasattr(__enumeration___UserState, "blocked")
    descriptor = None
    for klass in __enumeration___UserState.__mro__:
        if "blocked" in klass.__dict__:
            descriptor = klass.__dict__["blocked"]
            break
    assert isinstance(descriptor, property)

def test___enumeration___userstate_has_active():
    assert hasattr(__enumeration___UserState, "active")
    descriptor = None
    for klass in __enumeration___UserState.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_registered_customer_is_not_abstract():
    assert not inspect.isabstract(Registered_Customer)


def test_registered_customer_constructor_exists():
    assert callable(Registered_Customer.__init__)


def test_registered_customer_constructor_args():
    sig = inspect.signature(Registered_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "password" in params, "Missing parameter 'password'"

def test_registered_customer_has_Email():
    assert hasattr(Registered_Customer, "Email")
    descriptor = None
    for klass in Registered_Customer.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_registered_customer_has_password():
    assert hasattr(Registered_Customer, "password")
    descriptor = None
    for klass in Registered_Customer.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    number=
        safe_text,
    id=
        safe_text
)
Order_strategy = st.builds(
    Order,
    shipped=
        st.dates(),
    ship_to=
        safe_text,
    number=
        safe_text,
    ordered=
        st.dates()
)
Payment_strategy = st.builds(
    Payment,
    details=
        safe_text,
    id=
        safe_text,
    paid=
        st.dates(),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Content_strategy = st.builds(
    Content,
    quantity=
        st.integers(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
__enumeration___OderStatus_strategy = st.builds(
    __enumeration___OderStatus,
    closed=
        safe_text,
    hold=
        safe_text,
    new=
        safe_text,
    return=
        safe_text,
    delivery=
        safe_text,
    shipped=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    address=
        safe_text,
    phone=
        safe_text,
    name=
        safe_text,
    email=
        safe_text
)
Product_strategy = st.builds(
    Product,
    name=
        safe_text,
    id=
        safe_text,
    supplier=
        safe_text
)
New_Customer_strategy = st.builds(
    New_Customer,
    address=
        safe_text,
    phone=
        safe_text,
    password=
        safe_text,
    Name=
        safe_text,
    email=
        safe_text
)
__enumeration___UserState_strategy = st.builds(
    __enumeration___UserState,
    new=
        safe_text,
    banned=
        safe_text,
    blocked=
        safe_text,
    active=
        safe_text
)
Registered_Customer_strategy = st.builds(
    Registered_Customer,
    Email=
        safe_text,
    password=
        safe_text
)

@given(instance=Shopping_Cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart)



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_shipped_setter(instance):
    original = instance.shipped
    instance.shipped = original
    assert instance.shipped == original



@given(instance=Order_strategy)
def test_order_ship_to_setter(instance):
    original = instance.ship_to
    instance.ship_to = original
    assert instance.ship_to == original



@given(instance=Order_strategy)
def test_order_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Order_strategy)
def test_order_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=Payment_strategy)
def test_payment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Payment_strategy)
def test_payment_paid_setter(instance):
    original = instance.paid
    instance.paid = original
    assert instance.paid == original



@given(instance=Payment_strategy)
def test_payment_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original

@given(instance=Content_strategy)
@settings(max_examples=50)
def test_content_instantiation(instance):
    assert isinstance(instance, Content)



@given(instance=Content_strategy)
def test_content_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Content_strategy)
def test_content_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=__enumeration___OderStatus_strategy)
@settings(max_examples=50)
def test___enumeration___oderstatus_instantiation(instance):
    assert isinstance(instance, __enumeration___OderStatus)



@given(instance=__enumeration___OderStatus_strategy)
def test___enumeration___oderstatus_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original



@given(instance=__enumeration___OderStatus_strategy)
def test___enumeration___oderstatus_hold_setter(instance):
    original = instance.hold
    instance.hold = original
    assert instance.hold == original



@given(instance=__enumeration___OderStatus_strategy)
def test___enumeration___oderstatus_new_setter(instance):
    original = instance.new
    instance.new = original
    assert instance.new == original



@given(instance=__enumeration___OderStatus_strategy)
def test___enumeration___oderstatus_return_setter(instance):
    original = instance.return
    instance.return = original
    assert instance.return == original



@given(instance=__enumeration___OderStatus_strategy)
def test___enumeration___oderstatus_delivery_setter(instance):
    original = instance.delivery
    instance.delivery = original
    assert instance.delivery == original



@given(instance=__enumeration___OderStatus_strategy)
def test___enumeration___oderstatus_shipped_setter(instance):
    original = instance.shipped
    instance.shipped = original
    assert instance.shipped == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Product_strategy)
def test_product_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Product_strategy)
def test_product_supplier_setter(instance):
    original = instance.supplier
    instance.supplier = original
    assert instance.supplier == original

@given(instance=New_Customer_strategy)
@settings(max_examples=50)
def test_new_customer_instantiation(instance):
    assert isinstance(instance, New_Customer)



@given(instance=New_Customer_strategy)
def test_new_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=New_Customer_strategy)
def test_new_customer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=New_Customer_strategy)
def test_new_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=New_Customer_strategy)
def test_new_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=New_Customer_strategy)
def test_new_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=__enumeration___UserState_strategy)
@settings(max_examples=50)
def test___enumeration___userstate_instantiation(instance):
    assert isinstance(instance, __enumeration___UserState)



@given(instance=__enumeration___UserState_strategy)
def test___enumeration___userstate_new_setter(instance):
    original = instance.new
    instance.new = original
    assert instance.new == original



@given(instance=__enumeration___UserState_strategy)
def test___enumeration___userstate_banned_setter(instance):
    original = instance.banned
    instance.banned = original
    assert instance.banned == original



@given(instance=__enumeration___UserState_strategy)
def test___enumeration___userstate_blocked_setter(instance):
    original = instance.blocked
    instance.blocked = original
    assert instance.blocked == original



@given(instance=__enumeration___UserState_strategy)
def test___enumeration___userstate_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=Registered_Customer_strategy)
@settings(max_examples=50)
def test_registered_customer_instantiation(instance):
    assert isinstance(instance, Registered_Customer)



@given(instance=Registered_Customer_strategy)
def test_registered_customer_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Registered_Customer_strategy)
def test_registered_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
