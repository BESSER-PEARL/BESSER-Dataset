import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Licor,
    ItemOrden,
    Orden,
    Login,
    Cuenta,
    Venta,
    Pago,
    Vendedor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_licor_is_not_abstract():
    assert not inspect.isabstract(Licor)


def test_licor_constructor_exists():
    assert callable(Licor.__init__)


def test_licor_constructor_args():
    sig = inspect.signature(Licor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_licor_has_name():
    assert hasattr(Licor, "name")
    descriptor = None
    for klass in Licor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_licor_has_description():
    assert hasattr(Licor, "description")
    descriptor = None
    for klass in Licor.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_itemorden_is_not_abstract():
    assert not inspect.isabstract(ItemOrden)


def test_itemorden_constructor_exists():
    assert callable(ItemOrden.__init__)


def test_itemorden_constructor_args():
    sig = inspect.signature(ItemOrden.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "price" in params, "Missing parameter 'price'"

def test_itemorden_has_quantity():
    assert hasattr(ItemOrden, "quantity")
    descriptor = None
    for klass in ItemOrden.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_itemorden_has_price():
    assert hasattr(ItemOrden, "price")
    descriptor = None
    for klass in ItemOrden.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_orden_is_not_abstract():
    assert not inspect.isabstract(Orden)


def test_orden_constructor_exists():
    assert callable(Orden.__init__)


def test_orden_constructor_args():
    sig = inspect.signature(Orden.__init__)
    params = list(sig.parameters.keys())
    assert "shipped" in params, "Missing parameter 'shipped'"
    assert "shipTo" in params, "Missing parameter 'shipTo'"
    assert "status" in params, "Missing parameter 'status'"
    assert "number" in params, "Missing parameter 'number'"
    assert "total" in params, "Missing parameter 'total'"
    assert "ordered" in params, "Missing parameter 'ordered'"

def test_orden_has_shipped():
    assert hasattr(Orden, "shipped")
    descriptor = None
    for klass in Orden.__mro__:
        if "shipped" in klass.__dict__:
            descriptor = klass.__dict__["shipped"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_shipTo():
    assert hasattr(Orden, "shipTo")
    descriptor = None
    for klass in Orden.__mro__:
        if "shipTo" in klass.__dict__:
            descriptor = klass.__dict__["shipTo"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_status():
    assert hasattr(Orden, "status")
    descriptor = None
    for klass in Orden.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_number():
    assert hasattr(Orden, "number")
    descriptor = None
    for klass in Orden.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_total():
    assert hasattr(Orden, "total")
    descriptor = None
    for klass in Orden.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_ordered():
    assert hasattr(Orden, "ordered")
    descriptor = None
    for klass in Orden.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "password" in params, "Missing parameter 'password'"
    assert "login" in params, "Missing parameter 'login'"

def test_login_has_state():
    assert hasattr(Login, "state")
    descriptor = None
    for klass in Login.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_login():
    assert hasattr(Login, "login")
    descriptor = None
    for klass in Login.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)



def test_cuenta_is_not_abstract():
    assert not inspect.isabstract(Cuenta)


def test_cuenta_constructor_exists():
    assert callable(Cuenta.__init__)


def test_cuenta_constructor_args():
    sig = inspect.signature(Cuenta.__init__)
    params = list(sig.parameters.keys())
    assert "billingAddress" in params, "Missing parameter 'billingAddress'"
    assert "closed" in params, "Missing parameter 'closed'"
    assert "open" in params, "Missing parameter 'open'"
    assert "isClosed" in params, "Missing parameter 'isClosed'"

def test_cuenta_has_billingAddress():
    assert hasattr(Cuenta, "billingAddress")
    descriptor = None
    for klass in Cuenta.__mro__:
        if "billingAddress" in klass.__dict__:
            descriptor = klass.__dict__["billingAddress"]
            break
    assert isinstance(descriptor, property)

def test_cuenta_has_closed():
    assert hasattr(Cuenta, "closed")
    descriptor = None
    for klass in Cuenta.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)

def test_cuenta_has_open():
    assert hasattr(Cuenta, "open")
    descriptor = None
    for klass in Cuenta.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)

def test_cuenta_has_isClosed():
    assert hasattr(Cuenta, "isClosed")
    descriptor = None
    for klass in Cuenta.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)



def test_venta_is_not_abstract():
    assert not inspect.isabstract(Venta)


def test_venta_constructor_exists():
    assert callable(Venta.__init__)


def test_venta_constructor_args():
    sig = inspect.signature(Venta.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_venta_has_creationDate():
    assert hasattr(Venta, "creationDate")
    descriptor = None
    for klass in Venta.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_pago_is_not_abstract():
    assert not inspect.isabstract(Pago)


def test_pago_constructor_exists():
    assert callable(Pago.__init__)


def test_pago_constructor_args():
    sig = inspect.signature(Pago.__init__)
    params = list(sig.parameters.keys())
    assert "total" in params, "Missing parameter 'total'"
    assert "paidDate" in params, "Missing parameter 'paidDate'"
    assert "details" in params, "Missing parameter 'details'"

def test_pago_has_total():
    assert hasattr(Pago, "total")
    descriptor = None
    for klass in Pago.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_pago_has_paidDate():
    assert hasattr(Pago, "paidDate")
    descriptor = None
    for klass in Pago.__mro__:
        if "paidDate" in klass.__dict__:
            descriptor = klass.__dict__["paidDate"]
            break
    assert isinstance(descriptor, property)

def test_pago_has_details():
    assert hasattr(Pago, "details")
    descriptor = None
    for klass in Pago.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_vendedor_is_not_abstract():
    assert not inspect.isabstract(Vendedor)


def test_vendedor_constructor_exists():
    assert callable(Vendedor.__init__)


def test_vendedor_constructor_args():
    sig = inspect.signature(Vendedor.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "email" in params, "Missing parameter 'email'"
    assert "address" in params, "Missing parameter 'address'"

def test_vendedor_has_phone():
    assert hasattr(Vendedor, "phone")
    descriptor = None
    for klass in Vendedor.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_vendedor_has_email():
    assert hasattr(Vendedor, "email")
    descriptor = None
    for klass in Vendedor.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_vendedor_has_address():
    assert hasattr(Vendedor, "address")
    descriptor = None
    for klass in Vendedor.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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
Licor_strategy = st.builds(
    Licor,
    name=
        safe_text,
    description=
        safe_text
)
ItemOrden_strategy = st.builds(
    ItemOrden,
    quantity=
        st.integers(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Orden_strategy = st.builds(
    Orden,
    shipped=
        st.booleans(),
    shipTo=
        safe_text,
    status=
        safe_text,
    number=
        st.integers(),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    ordered=
        st.dates()
)
Login_strategy = st.builds(
    Login,
    state=
        safe_text,
    password=
        safe_text,
    login=
        safe_text
)
Cuenta_strategy = st.builds(
    Cuenta,
    billingAddress=
        safe_text,
    closed=
        st.dates(),
    open=
        st.dates(),
    isClosed=
        st.booleans()
)
Venta_strategy = st.builds(
    Venta,
    creationDate=
        st.dates()
)
Pago_strategy = st.builds(
    Pago,
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    paidDate=
        st.dates(),
    details=
        safe_text
)
Vendedor_strategy = st.builds(
    Vendedor,
    phone=
        safe_text,
    email=
        safe_text,
    address=
        safe_text
)

@given(instance=Licor_strategy)
@settings(max_examples=50)
def test_licor_instantiation(instance):
    assert isinstance(instance, Licor)



@given(instance=Licor_strategy)
def test_licor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Licor_strategy)
def test_licor_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ItemOrden_strategy)
@settings(max_examples=50)
def test_itemorden_instantiation(instance):
    assert isinstance(instance, ItemOrden)



@given(instance=ItemOrden_strategy)
def test_itemorden_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=ItemOrden_strategy)
def test_itemorden_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Orden_strategy)
@settings(max_examples=50)
def test_orden_instantiation(instance):
    assert isinstance(instance, Orden)



@given(instance=Orden_strategy)
def test_orden_shipped_setter(instance):
    original = instance.shipped
    instance.shipped = original
    assert instance.shipped == original



@given(instance=Orden_strategy)
def test_orden_shipTo_setter(instance):
    original = instance.shipTo
    instance.shipTo = original
    assert instance.shipTo == original



@given(instance=Orden_strategy)
def test_orden_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Orden_strategy)
def test_orden_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Orden_strategy)
def test_orden_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Orden_strategy)
def test_orden_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_login_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original

@given(instance=Cuenta_strategy)
@settings(max_examples=50)
def test_cuenta_instantiation(instance):
    assert isinstance(instance, Cuenta)



@given(instance=Cuenta_strategy)
def test_cuenta_billingAddress_setter(instance):
    original = instance.billingAddress
    instance.billingAddress = original
    assert instance.billingAddress == original



@given(instance=Cuenta_strategy)
def test_cuenta_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original



@given(instance=Cuenta_strategy)
def test_cuenta_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original



@given(instance=Cuenta_strategy)
def test_cuenta_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original

@given(instance=Venta_strategy)
@settings(max_examples=50)
def test_venta_instantiation(instance):
    assert isinstance(instance, Venta)



@given(instance=Venta_strategy)
def test_venta_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=Pago_strategy)
@settings(max_examples=50)
def test_pago_instantiation(instance):
    assert isinstance(instance, Pago)



@given(instance=Pago_strategy)
def test_pago_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Pago_strategy)
def test_pago_paidDate_setter(instance):
    original = instance.paidDate
    instance.paidDate = original
    assert instance.paidDate == original



@given(instance=Pago_strategy)
def test_pago_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=Vendedor_strategy)
@settings(max_examples=50)
def test_vendedor_instantiation(instance):
    assert isinstance(instance, Vendedor)



@given(instance=Vendedor_strategy)
def test_vendedor_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Vendedor_strategy)
def test_vendedor_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Vendedor_strategy)
def test_vendedor_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
