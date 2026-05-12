import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ShoppinCart,
    Payment,
    Customer,
    MyClass,
    Product,
    LineItem,
    Order,
    WebUser,
    Account,
    OrderStatus,
    UserState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shoppincart_is_not_abstract():
    assert not inspect.isabstract(ShoppinCart)


def test_shoppincart_constructor_exists():
    assert callable(ShoppinCart.__init__)


def test_shoppincart_constructor_args():
    sig = inspect.signature(ShoppinCart.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_shoppincart_has_creationDate():
    assert hasattr(ShoppinCart, "creationDate")
    descriptor = None
    for klass in ShoppinCart.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "paidDate" in params, "Missing parameter 'paidDate'"
    assert "total" in params, "Missing parameter 'total'"
    assert "details" in params, "Missing parameter 'details'"

def test_payment_has_paidDate():
    assert hasattr(Payment, "paidDate")
    descriptor = None
    for klass in Payment.__mro__:
        if "paidDate" in klass.__dict__:
            descriptor = klass.__dict__["paidDate"]
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

def test_payment_has_details():
    assert hasattr(Payment, "details")
    descriptor = None
    for klass in Payment.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "address" in params, "Missing parameter 'address'"
    assert "email" in params, "Missing parameter 'email'"

def test_customer_has_phone():
    assert hasattr(Customer, "phone")
    descriptor = None
    for klass in Customer.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
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

def test_customer_has_email():
    assert hasattr(Customer, "email")
    descriptor = None
    for klass in Customer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute6" in params, "Missing parameter 'attribute6'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute4" in params, "Missing parameter 'attribute4'"
    assert "attribute7" in params, "Missing parameter 'attribute7'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"

def test_myclass_has_attribute2():
    assert hasattr(MyClass, "attribute2")
    descriptor = None
    for klass in MyClass.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_myclass_has_attribute6():
    assert hasattr(MyClass, "attribute6")
    descriptor = None
    for klass in MyClass.__mro__:
        if "attribute6" in klass.__dict__:
            descriptor = klass.__dict__["attribute6"]
            break
    assert isinstance(descriptor, property)

def test_myclass_has_attribute3():
    assert hasattr(MyClass, "attribute3")
    descriptor = None
    for klass in MyClass.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)

def test_myclass_has_attribute():
    assert hasattr(MyClass, "attribute")
    descriptor = None
    for klass in MyClass.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_myclass_has_attribute4():
    assert hasattr(MyClass, "attribute4")
    descriptor = None
    for klass in MyClass.__mro__:
        if "attribute4" in klass.__dict__:
            descriptor = klass.__dict__["attribute4"]
            break
    assert isinstance(descriptor, property)

def test_myclass_has_attribute7():
    assert hasattr(MyClass, "attribute7")
    descriptor = None
    for klass in MyClass.__mro__:
        if "attribute7" in klass.__dict__:
            descriptor = klass.__dict__["attribute7"]
            break
    assert isinstance(descriptor, property)

def test_myclass_has_attribute5():
    assert hasattr(MyClass, "attribute5")
    descriptor = None
    for klass in MyClass.__mro__:
        if "attribute5" in klass.__dict__:
            descriptor = klass.__dict__["attribute5"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "name" in params, "Missing parameter 'name'"
    assert "attribute7" in params, "Missing parameter 'attribute7'"
    assert "attribute4" in params, "Missing parameter 'attribute4'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "description" in params, "Missing parameter 'description'"
    assert "attribute8" in params, "Missing parameter 'attribute8'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"
    assert "attribute6" in params, "Missing parameter 'attribute6'"

def test_product_has_attribute3():
    assert hasattr(Product, "attribute3")
    descriptor = None
    for klass in Product.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)

def test_product_has_attribute2():
    assert hasattr(Product, "attribute2")
    descriptor = None
    for klass in Product.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
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

def test_product_has_attribute7():
    assert hasattr(Product, "attribute7")
    descriptor = None
    for klass in Product.__mro__:
        if "attribute7" in klass.__dict__:
            descriptor = klass.__dict__["attribute7"]
            break
    assert isinstance(descriptor, property)

def test_product_has_attribute4():
    assert hasattr(Product, "attribute4")
    descriptor = None
    for klass in Product.__mro__:
        if "attribute4" in klass.__dict__:
            descriptor = klass.__dict__["attribute4"]
            break
    assert isinstance(descriptor, property)

def test_product_has_attribute():
    assert hasattr(Product, "attribute")
    descriptor = None
    for klass in Product.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
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

def test_product_has_attribute8():
    assert hasattr(Product, "attribute8")
    descriptor = None
    for klass in Product.__mro__:
        if "attribute8" in klass.__dict__:
            descriptor = klass.__dict__["attribute8"]
            break
    assert isinstance(descriptor, property)

def test_product_has_attribute5():
    assert hasattr(Product, "attribute5")
    descriptor = None
    for klass in Product.__mro__:
        if "attribute5" in klass.__dict__:
            descriptor = klass.__dict__["attribute5"]
            break
    assert isinstance(descriptor, property)

def test_product_has_attribute6():
    assert hasattr(Product, "attribute6")
    descriptor = None
    for klass in Product.__mro__:
        if "attribute6" in klass.__dict__:
            descriptor = klass.__dict__["attribute6"]
            break
    assert isinstance(descriptor, property)



def test_lineitem_is_not_abstract():
    assert not inspect.isabstract(LineItem)


def test_lineitem_constructor_exists():
    assert callable(LineItem.__init__)


def test_lineitem_constructor_args():
    sig = inspect.signature(LineItem.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_lineitem_has_price():
    assert hasattr(LineItem, "price")
    descriptor = None
    for klass in LineItem.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_lineitem_has_quantity():
    assert hasattr(LineItem, "quantity")
    descriptor = None
    for klass in LineItem.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "shipped" in params, "Missing parameter 'shipped'"
    assert "total" in params, "Missing parameter 'total'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "status" in params, "Missing parameter 'status'"
    assert "shipTo" in params, "Missing parameter 'shipTo'"

def test_order_has_number():
    assert hasattr(Order, "number")
    descriptor = None
    for klass in Order.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shipped():
    assert hasattr(Order, "shipped")
    descriptor = None
    for klass in Order.__mro__:
        if "shipped" in klass.__dict__:
            descriptor = klass.__dict__["shipped"]
            break
    assert isinstance(descriptor, property)

def test_order_has_total():
    assert hasattr(Order, "total")
    descriptor = None
    for klass in Order.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
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

def test_order_has_status():
    assert hasattr(Order, "status")
    descriptor = None
    for klass in Order.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shipTo():
    assert hasattr(Order, "shipTo")
    descriptor = None
    for klass in Order.__mro__:
        if "shipTo" in klass.__dict__:
            descriptor = klass.__dict__["shipTo"]
            break
    assert isinstance(descriptor, property)



def test_webuser_is_not_abstract():
    assert not inspect.isabstract(WebUser)


def test_webuser_constructor_exists():
    assert callable(WebUser.__init__)


def test_webuser_constructor_args():
    sig = inspect.signature(WebUser.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "login" in params, "Missing parameter 'login'"
    assert "password" in params, "Missing parameter 'password'"

def test_webuser_has_state():
    assert hasattr(WebUser, "state")
    descriptor = None
    for klass in WebUser.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_webuser_has_login():
    assert hasattr(WebUser, "login")
    descriptor = None
    for klass in WebUser.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)

def test_webuser_has_password():
    assert hasattr(WebUser, "password")
    descriptor = None
    for klass in WebUser.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "closed" in params, "Missing parameter 'closed'"
    assert "open" in params, "Missing parameter 'open'"
    assert "isClosed" in params, "Missing parameter 'isClosed'"
    assert "billingAddress" in params, "Missing parameter 'billingAddress'"

def test_account_has_closed():
    assert hasattr(Account, "closed")
    descriptor = None
    for klass in Account.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)

def test_account_has_open():
    assert hasattr(Account, "open")
    descriptor = None
    for klass in Account.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)

def test_account_has_isClosed():
    assert hasattr(Account, "isClosed")
    descriptor = None
    for klass in Account.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
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

def test_userstate_exists():
    # Check that the Enumeration exists
    assert UserState is not None

def test_userstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UserState]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UserState"


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
ShoppinCart_strategy = st.builds(
    ShoppinCart,
    creationDate=
        st.dates()
)
Payment_strategy = st.builds(
    Payment,
    paidDate=
        st.dates(),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    details=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    phone=
        safe_text,
    address=
        safe_text,
    email=
        safe_text
)
MyClass_strategy = st.builds(
    MyClass,
    attribute2=
        safe_text,
    attribute6=
        safe_text,
    attribute3=
        safe_text,
    attribute=
        safe_text,
    attribute4=
        safe_text,
    attribute7=
        safe_text,
    attribute5=
        safe_text
)
Product_strategy = st.builds(
    Product,
    attribute3=
        safe_text,
    attribute2=
        safe_text,
    name=
        safe_text,
    attribute7=
        safe_text,
    attribute4=
        safe_text,
    attribute=
        safe_text,
    description=
        safe_text,
    attribute8=
        safe_text,
    attribute5=
        safe_text,
    attribute6=
        safe_text
)
LineItem_strategy = st.builds(
    LineItem,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    quantity=
        st.integers()
)
Order_strategy = st.builds(
    Order,
    number=
        st.integers(),
    shipped=
        st.booleans(),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    ordered=
        st.dates(),
    status=
        st.none(),
    shipTo=
        safe_text
)
WebUser_strategy = st.builds(
    WebUser,
    state=
        st.none(),
    login=
        safe_text,
    password=
        safe_text
)
Account_strategy = st.builds(
    Account,
    closed=
        st.dates(),
    open=
        st.dates(),
    isClosed=
        st.booleans(),
    billingAddress=
        safe_text
)

@given(instance=ShoppinCart_strategy)
@settings(max_examples=50)
def test_shoppincart_instantiation(instance):
    assert isinstance(instance, ShoppinCart)



@given(instance=ShoppinCart_strategy)
def test_shoppincart_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_paidDate_setter(instance):
    original = instance.paidDate
    instance.paidDate = original
    assert instance.paidDate == original



@given(instance=Payment_strategy)
def test_payment_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Payment_strategy)
def test_payment_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)



@given(instance=MyClass_strategy)
def test_myclass_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=MyClass_strategy)
def test_myclass_attribute6_setter(instance):
    original = instance.attribute6
    instance.attribute6 = original
    assert instance.attribute6 == original



@given(instance=MyClass_strategy)
def test_myclass_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original



@given(instance=MyClass_strategy)
def test_myclass_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=MyClass_strategy)
def test_myclass_attribute4_setter(instance):
    original = instance.attribute4
    instance.attribute4 = original
    assert instance.attribute4 == original



@given(instance=MyClass_strategy)
def test_myclass_attribute7_setter(instance):
    original = instance.attribute7
    instance.attribute7 = original
    assert instance.attribute7 == original



@given(instance=MyClass_strategy)
def test_myclass_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original



@given(instance=Product_strategy)
def test_product_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Product_strategy)
def test_product_attribute7_setter(instance):
    original = instance.attribute7
    instance.attribute7 = original
    assert instance.attribute7 == original



@given(instance=Product_strategy)
def test_product_attribute4_setter(instance):
    original = instance.attribute4
    instance.attribute4 = original
    assert instance.attribute4 == original



@given(instance=Product_strategy)
def test_product_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Product_strategy)
def test_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Product_strategy)
def test_product_attribute8_setter(instance):
    original = instance.attribute8
    instance.attribute8 = original
    assert instance.attribute8 == original



@given(instance=Product_strategy)
def test_product_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original



@given(instance=Product_strategy)
def test_product_attribute6_setter(instance):
    original = instance.attribute6
    instance.attribute6 = original
    assert instance.attribute6 == original

@given(instance=LineItem_strategy)
@settings(max_examples=50)
def test_lineitem_instantiation(instance):
    assert isinstance(instance, LineItem)



@given(instance=LineItem_strategy)
def test_lineitem_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=LineItem_strategy)
def test_lineitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Order_strategy)
def test_order_shipped_setter(instance):
    original = instance.shipped
    instance.shipped = original
    assert instance.shipped == original



@given(instance=Order_strategy)
def test_order_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Order_strategy)
def test_order_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=Order_strategy)
def test_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Order_strategy)
def test_order_shipTo_setter(instance):
    original = instance.shipTo
    instance.shipTo = original
    assert instance.shipTo == original

@given(instance=WebUser_strategy)
@settings(max_examples=50)
def test_webuser_instantiation(instance):
    assert isinstance(instance, WebUser)



@given(instance=WebUser_strategy)
def test_webuser_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=WebUser_strategy)
def test_webuser_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=WebUser_strategy)
def test_webuser_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original



@given(instance=Account_strategy)
def test_account_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original



@given(instance=Account_strategy)
def test_account_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original



@given(instance=Account_strategy)
def test_account_billingAddress_setter(instance):
    original = instance.billingAddress
    instance.billingAddress = original
    assert instance.billingAddress == original
