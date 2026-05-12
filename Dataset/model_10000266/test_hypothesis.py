import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Customer,
    Order,
    Payment,
    Account,
    Product,
    Item,
    ShoppingCart,
    OrderStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "id" in params, "Missing parameter 'id'"
    assert "login" in params, "Missing parameter 'login'"
    assert "isBan" in params, "Missing parameter 'isBan'"
    assert "password" in params, "Missing parameter 'password'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_customer_has_lastname():
    assert hasattr(Customer, "lastname")
    descriptor = None
    for klass in Customer.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_id():
    assert hasattr(Customer, "id")
    descriptor = None
    for klass in Customer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_login():
    assert hasattr(Customer, "login")
    descriptor = None
    for klass in Customer.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_isBan():
    assert hasattr(Customer, "isBan")
    descriptor = None
    for klass in Customer.__mro__:
        if "isBan" in klass.__dict__:
            descriptor = klass.__dict__["isBan"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_password():
    assert hasattr(Customer, "password")
    descriptor = None
    for klass in Customer.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_emailAddress():
    assert hasattr(Customer, "emailAddress")
    descriptor = None
    for klass in Customer.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_firstname():
    assert hasattr(Customer, "firstname")
    descriptor = None
    for klass in Customer.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "finalTotal" in params, "Missing parameter 'finalTotal'"
    assert "status" in params, "Missing parameter 'status'"
    assert "shippingAddress" in params, "Missing parameter 'shippingAddress'"
    assert "id" in params, "Missing parameter 'id'"

def test_order_has_finalTotal():
    assert hasattr(Order, "finalTotal")
    descriptor = None
    for klass in Order.__mro__:
        if "finalTotal" in klass.__dict__:
            descriptor = klass.__dict__["finalTotal"]
            break
    assert isinstance(descriptor, property)

def test_order_has_status():
    assert hasattr(Order, "status")
    descriptor = None
    for klass in Order.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shippingAddress():
    assert hasattr(Order, "shippingAddress")
    descriptor = None
    for klass in Order.__mro__:
        if "shippingAddress" in klass.__dict__:
            descriptor = klass.__dict__["shippingAddress"]
            break
    assert isinstance(descriptor, property)

def test_order_has_id():
    assert hasattr(Order, "id")
    descriptor = None
    for klass in Order.__mro__:
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
    assert "total" in params, "Missing parameter 'total'"
    assert "id" in params, "Missing parameter 'id'"
    assert "comments" in params, "Missing parameter 'comments'"

def test_payment_has_total():
    assert hasattr(Payment, "total")
    descriptor = None
    for klass in Payment.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
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

def test_payment_has_comments():
    assert hasattr(Payment, "comments")
    descriptor = None
    for klass in Payment.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "openDate" in params, "Missing parameter 'openDate'"
    assert "billingAddress" in params, "Missing parameter 'billingAddress'"
    assert "id" in params, "Missing parameter 'id'"

def test_account_has_openDate():
    assert hasattr(Account, "openDate")
    descriptor = None
    for klass in Account.__mro__:
        if "openDate" in klass.__dict__:
            descriptor = klass.__dict__["openDate"]
            break
    assert isinstance(descriptor, property)

def test_account_has_billingAddress():
    assert hasattr(Account, "billingAddress")
    descriptor = None
    for klass in Account.__mro__:
        if "billingAddress" in klass.__dict__:
            descriptor = klass.__dict__["billingAddress"]
            break
    assert isinstance(descriptor, property)

def test_account_has_id():
    assert hasattr(Account, "id")
    descriptor = None
    for klass in Account.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
    assert "description" in params, "Missing parameter 'description'"

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

def test_product_has_description():
    assert hasattr(Product, "description")
    descriptor = None
    for klass in Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "id" in params, "Missing parameter 'id'"

def test_item_has_price():
    assert hasattr(Item, "price")
    descriptor = None
    for klass in Item.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_item_has_quantity():
    assert hasattr(Item, "quantity")
    descriptor = None
    for klass in Item.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_item_has_id():
    assert hasattr(Item, "id")
    descriptor = None
    for klass in Item.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_shoppingcart_has_id():
    assert hasattr(ShoppingCart, "id")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_creationDate():
    assert hasattr(ShoppingCart, "creationDate")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_orderstatus_exists():
    # Check that the Enumeration exists
    assert OrderStatus is not None

def test_orderstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderStatus"


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
Customer_strategy = st.builds(
    Customer,
    lastname=
        safe_text,
    id=
        st.integers(),
    login=
        safe_text,
    isBan=
        st.booleans(),
    password=
        safe_text,
    emailAddress=
        safe_text,
    firstname=
        safe_text
)
Order_strategy = st.builds(
    Order,
    finalTotal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    status=
        st.none(),
    shippingAddress=
        safe_text,
    id=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    total=
        st.integers(),
    id=
        st.integers(),
    comments=
        safe_text
)
Account_strategy = st.builds(
    Account,
    openDate=
        st.dates(),
    billingAddress=
        safe_text,
    id=
        st.integers()
)
Product_strategy = st.builds(
    Product,
    name=
        safe_text,
    id=
        st.integers(),
    description=
        safe_text
)
Item_strategy = st.builds(
    Item,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    quantity=
        st.integers(),
    id=
        st.integers()
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    id=
        st.integers(),
    creationDate=
        st.dates()
)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Customer_strategy)
def test_customer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Customer_strategy)
def test_customer_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=Customer_strategy)
def test_customer_isBan_setter(instance):
    original = instance.isBan
    instance.isBan = original
    assert instance.isBan == original



@given(instance=Customer_strategy)
def test_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Customer_strategy)
def test_customer_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original



@given(instance=Customer_strategy)
def test_customer_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_finalTotal_setter(instance):
    original = instance.finalTotal
    instance.finalTotal = original
    assert instance.finalTotal == original



@given(instance=Order_strategy)
def test_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Order_strategy)
def test_order_shippingAddress_setter(instance):
    original = instance.shippingAddress
    instance.shippingAddress = original
    assert instance.shippingAddress == original



@given(instance=Order_strategy)
def test_order_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Payment_strategy)
def test_payment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Payment_strategy)
def test_payment_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_openDate_setter(instance):
    original = instance.openDate
    instance.openDate = original
    assert instance.openDate == original



@given(instance=Account_strategy)
def test_account_billingAddress_setter(instance):
    original = instance.billingAddress
    instance.billingAddress = original
    assert instance.billingAddress == original



@given(instance=Account_strategy)
def test_account_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

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
def test_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)



@given(instance=Item_strategy)
def test_item_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Item_strategy)
def test_item_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Item_strategy)
def test_item_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original
