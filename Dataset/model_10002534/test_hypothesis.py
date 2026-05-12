import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Product,
    LineItem,
    Order,
    SinhVien,
    Account,
    ConNguoi,
    Payment,
    Customer,
    UserState,
    OrderStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_product_has_description():
    assert hasattr(Product, "description")
    descriptor = None
    for klass in Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
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
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "shipped" in params, "Missing parameter 'shipped'"
    assert "shipTo" in params, "Missing parameter 'shipTo'"
    assert "number" in params, "Missing parameter 'number'"
    assert "total" in params, "Missing parameter 'total'"
    assert "status" in params, "Missing parameter 'status'"

def test_order_has_ordered():
    assert hasattr(Order, "ordered")
    descriptor = None
    for klass in Order.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
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

def test_order_has_shipTo():
    assert hasattr(Order, "shipTo")
    descriptor = None
    for klass in Order.__mro__:
        if "shipTo" in klass.__dict__:
            descriptor = klass.__dict__["shipTo"]
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

def test_order_has_total():
    assert hasattr(Order, "total")
    descriptor = None
    for klass in Order.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
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



def test_sinhvien_is_not_abstract():
    assert not inspect.isabstract(SinhVien)


def test_sinhvien_constructor_exists():
    assert callable(SinhVien.__init__)


def test_sinhvien_constructor_args():
    sig = inspect.signature(SinhVien.__init__)
    params = list(sig.parameters.keys())
    assert "login" in params, "Missing parameter 'login'"
    assert "state" in params, "Missing parameter 'state'"
    assert "password" in params, "Missing parameter 'password'"

def test_sinhvien_has_login():
    assert hasattr(SinhVien, "login")
    descriptor = None
    for klass in SinhVien.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)

def test_sinhvien_has_state():
    assert hasattr(SinhVien, "state")
    descriptor = None
    for klass in SinhVien.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_sinhvien_has_password():
    assert hasattr(SinhVien, "password")
    descriptor = None
    for klass in SinhVien.__mro__:
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
    assert "billingAddress" in params, "Missing parameter 'billingAddress'"
    assert "closed" in params, "Missing parameter 'closed'"
    assert "isClosed" in params, "Missing parameter 'isClosed'"
    assert "open" in params, "Missing parameter 'open'"

def test_account_has_billingAddress():
    assert hasattr(Account, "billingAddress")
    descriptor = None
    for klass in Account.__mro__:
        if "billingAddress" in klass.__dict__:
            descriptor = klass.__dict__["billingAddress"]
            break
    assert isinstance(descriptor, property)

def test_account_has_closed():
    assert hasattr(Account, "closed")
    descriptor = None
    for klass in Account.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
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

def test_account_has_open():
    assert hasattr(Account, "open")
    descriptor = None
    for klass in Account.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)



def test_connguoi_is_not_abstract():
    assert not inspect.isabstract(ConNguoi)


def test_connguoi_constructor_exists():
    assert callable(ConNguoi.__init__)


def test_connguoi_constructor_args():
    sig = inspect.signature(ConNguoi.__init__)
    params = list(sig.parameters.keys())
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute4" in params, "Missing parameter 'attribute4'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute6" in params, "Missing parameter 'attribute6'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"
    assert "CMND" in params, "Missing parameter 'CMND'"

def test_connguoi_has_attribute3():
    assert hasattr(ConNguoi, "attribute3")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)

def test_connguoi_has_attribute4():
    assert hasattr(ConNguoi, "attribute4")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "attribute4" in klass.__dict__:
            descriptor = klass.__dict__["attribute4"]
            break
    assert isinstance(descriptor, property)

def test_connguoi_has_attribute():
    assert hasattr(ConNguoi, "attribute")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_connguoi_has_attribute2():
    assert hasattr(ConNguoi, "attribute2")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_connguoi_has_attribute6():
    assert hasattr(ConNguoi, "attribute6")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "attribute6" in klass.__dict__:
            descriptor = klass.__dict__["attribute6"]
            break
    assert isinstance(descriptor, property)

def test_connguoi_has_attribute5():
    assert hasattr(ConNguoi, "attribute5")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "attribute5" in klass.__dict__:
            descriptor = klass.__dict__["attribute5"]
            break
    assert isinstance(descriptor, property)

def test_connguoi_has_CMND():
    assert hasattr(ConNguoi, "CMND")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "CMND" in klass.__dict__:
            descriptor = klass.__dict__["CMND"]
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
Product_strategy = st.builds(
    Product,
    description=
        safe_text,
    name=
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
    ordered=
        st.dates(),
    shipped=
        st.booleans(),
    shipTo=
        safe_text,
    number=
        st.integers(),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    status=
        st.none()
)
SinhVien_strategy = st.builds(
    SinhVien,
    login=
        safe_text,
    state=
        st.none(),
    password=
        safe_text
)
Account_strategy = st.builds(
    Account,
    billingAddress=
        safe_text,
    closed=
        st.dates(),
    isClosed=
        st.booleans(),
    open=
        st.dates()
)
ConNguoi_strategy = st.builds(
    ConNguoi,
    attribute3=
        safe_text,
    attribute4=
        safe_text,
    attribute=
        safe_text,
    attribute2=
        safe_text,
    attribute6=
        safe_text,
    attribute5=
        safe_text,
    CMND=
        safe_text
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

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_order_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=Order_strategy)
def test_order_shipped_setter(instance):
    original = instance.shipped
    instance.shipped = original
    assert instance.shipped == original



@given(instance=Order_strategy)
def test_order_shipTo_setter(instance):
    original = instance.shipTo
    instance.shipTo = original
    assert instance.shipTo == original



@given(instance=Order_strategy)
def test_order_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Order_strategy)
def test_order_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Order_strategy)
def test_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=SinhVien_strategy)
@settings(max_examples=50)
def test_sinhvien_instantiation(instance):
    assert isinstance(instance, SinhVien)



@given(instance=SinhVien_strategy)
def test_sinhvien_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=SinhVien_strategy)
def test_sinhvien_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=SinhVien_strategy)
def test_sinhvien_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_billingAddress_setter(instance):
    original = instance.billingAddress
    instance.billingAddress = original
    assert instance.billingAddress == original



@given(instance=Account_strategy)
def test_account_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original



@given(instance=Account_strategy)
def test_account_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original



@given(instance=Account_strategy)
def test_account_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original

@given(instance=ConNguoi_strategy)
@settings(max_examples=50)
def test_connguoi_instantiation(instance):
    assert isinstance(instance, ConNguoi)



@given(instance=ConNguoi_strategy)
def test_connguoi_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original



@given(instance=ConNguoi_strategy)
def test_connguoi_attribute4_setter(instance):
    original = instance.attribute4
    instance.attribute4 = original
    assert instance.attribute4 == original



@given(instance=ConNguoi_strategy)
def test_connguoi_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=ConNguoi_strategy)
def test_connguoi_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=ConNguoi_strategy)
def test_connguoi_attribute6_setter(instance):
    original = instance.attribute6
    instance.attribute6 = original
    assert instance.attribute6 == original



@given(instance=ConNguoi_strategy)
def test_connguoi_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original



@given(instance=ConNguoi_strategy)
def test_connguoi_CMND_setter(instance):
    original = instance.CMND
    instance.CMND = original
    assert instance.CMND == original

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
