import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Product,
    Order,
    Cliente,
    Account,
    Carro_de_Compras,
    Payment,
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



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "shipTo" in params, "Missing parameter 'shipTo'"
    assert "number" in params, "Missing parameter 'number'"
    assert "total" in params, "Missing parameter 'total'"
    assert "status" in params, "Missing parameter 'status'"
    assert "shipped" in params, "Missing parameter 'shipped'"

def test_order_has_ordered():
    assert hasattr(Order, "ordered")
    descriptor = None
    for klass in Order.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
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

def test_order_has_shipped():
    assert hasattr(Order, "shipped")
    descriptor = None
    for klass in Order.__mro__:
        if "shipped" in klass.__dict__:
            descriptor = klass.__dict__["shipped"]
            break
    assert isinstance(descriptor, property)



def test_cliente_is_not_abstract():
    assert not inspect.isabstract(Cliente)


def test_cliente_constructor_exists():
    assert callable(Cliente.__init__)


def test_cliente_constructor_args():
    sig = inspect.signature(Cliente.__init__)
    params = list(sig.parameters.keys())
    assert "Contacto" in params, "Missing parameter 'Contacto'"
    assert "email" in params, "Missing parameter 'email'"
    assert "Direcci_n" in params, "Missing parameter 'Direcci_n'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"

def test_cliente_has_Contacto():
    assert hasattr(Cliente, "Contacto")
    descriptor = None
    for klass in Cliente.__mro__:
        if "Contacto" in klass.__dict__:
            descriptor = klass.__dict__["Contacto"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_email():
    assert hasattr(Cliente, "email")
    descriptor = None
    for klass in Cliente.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_Direcci_n():
    assert hasattr(Cliente, "Direcci_n")
    descriptor = None
    for klass in Cliente.__mro__:
        if "Direcci_n" in klass.__dict__:
            descriptor = klass.__dict__["Direcci_n"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_Nombre():
    assert hasattr(Cliente, "Nombre")
    descriptor = None
    for klass in Cliente.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "isClosed" in params, "Missing parameter 'isClosed'"
    assert "open" in params, "Missing parameter 'open'"
    assert "billingAddress" in params, "Missing parameter 'billingAddress'"
    assert "closed" in params, "Missing parameter 'closed'"

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



def test_carro_de_compras_is_not_abstract():
    assert not inspect.isabstract(Carro_de_Compras)


def test_carro_de_compras_constructor_exists():
    assert callable(Carro_de_Compras.__init__)


def test_carro_de_compras_constructor_args():
    sig = inspect.signature(Carro_de_Compras.__init__)
    params = list(sig.parameters.keys())
    assert "IdCarro" in params, "Missing parameter 'IdCarro'"
    assert "Producto" in params, "Missing parameter 'Producto'"
    assert "Precio" in params, "Missing parameter 'Precio'"
    assert "Cantidad" in params, "Missing parameter 'Cantidad'"

def test_carro_de_compras_has_IdCarro():
    assert hasattr(Carro_de_Compras, "IdCarro")
    descriptor = None
    for klass in Carro_de_Compras.__mro__:
        if "IdCarro" in klass.__dict__:
            descriptor = klass.__dict__["IdCarro"]
            break
    assert isinstance(descriptor, property)

def test_carro_de_compras_has_Producto():
    assert hasattr(Carro_de_Compras, "Producto")
    descriptor = None
    for klass in Carro_de_Compras.__mro__:
        if "Producto" in klass.__dict__:
            descriptor = klass.__dict__["Producto"]
            break
    assert isinstance(descriptor, property)

def test_carro_de_compras_has_Precio():
    assert hasattr(Carro_de_Compras, "Precio")
    descriptor = None
    for klass in Carro_de_Compras.__mro__:
        if "Precio" in klass.__dict__:
            descriptor = klass.__dict__["Precio"]
            break
    assert isinstance(descriptor, property)

def test_carro_de_compras_has_Cantidad():
    assert hasattr(Carro_de_Compras, "Cantidad")
    descriptor = None
    for klass in Carro_de_Compras.__mro__:
        if "Cantidad" in klass.__dict__:
            descriptor = klass.__dict__["Cantidad"]
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
    assert "details" in params, "Missing parameter 'details'"
    assert "total" in params, "Missing parameter 'total'"

def test_payment_has_paidDate():
    assert hasattr(Payment, "paidDate")
    descriptor = None
    for klass in Payment.__mro__:
        if "paidDate" in klass.__dict__:
            descriptor = klass.__dict__["paidDate"]
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

def test_payment_has_total():
    assert hasattr(Payment, "total")
    descriptor = None
    for klass in Payment.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
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
Product_strategy = st.builds(
    Product,
    name=
        safe_text,
    id=
        st.integers(),
    description=
        safe_text
)
Order_strategy = st.builds(
    Order,
    ordered=
        st.dates(),
    shipTo=
        safe_text,
    number=
        st.integers(),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    status=
        safe_text,
    shipped=
        st.booleans()
)
Cliente_strategy = st.builds(
    Cliente,
    Contacto=
        st.integers(),
    email=
        safe_text,
    Direcci_n=
        safe_text,
    Nombre=
        safe_text
)
Account_strategy = st.builds(
    Account,
    isClosed=
        st.booleans(),
    open=
        st.dates(),
    billingAddress=
        safe_text,
    closed=
        st.dates()
)
Carro_de_Compras_strategy = st.builds(
    Carro_de_Compras,
    IdCarro=
        st.integers(),
    Producto=
        safe_text,
    Precio=
        st.integers(),
    Cantidad=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    paidDate=
        st.dates(),
    details=
        safe_text,
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

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



@given(instance=Order_strategy)
def test_order_shipped_setter(instance):
    original = instance.shipped
    instance.shipped = original
    assert instance.shipped == original

@given(instance=Cliente_strategy)
@settings(max_examples=50)
def test_cliente_instantiation(instance):
    assert isinstance(instance, Cliente)



@given(instance=Cliente_strategy)
def test_cliente_Contacto_setter(instance):
    original = instance.Contacto
    instance.Contacto = original
    assert instance.Contacto == original



@given(instance=Cliente_strategy)
def test_cliente_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Cliente_strategy)
def test_cliente_Direcci_n_setter(instance):
    original = instance.Direcci_n
    instance.Direcci_n = original
    assert instance.Direcci_n == original



@given(instance=Cliente_strategy)
def test_cliente_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



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

@given(instance=Carro_de_Compras_strategy)
@settings(max_examples=50)
def test_carro_de_compras_instantiation(instance):
    assert isinstance(instance, Carro_de_Compras)



@given(instance=Carro_de_Compras_strategy)
def test_carro_de_compras_IdCarro_setter(instance):
    original = instance.IdCarro
    instance.IdCarro = original
    assert instance.IdCarro == original



@given(instance=Carro_de_Compras_strategy)
def test_carro_de_compras_Producto_setter(instance):
    original = instance.Producto
    instance.Producto = original
    assert instance.Producto == original



@given(instance=Carro_de_Compras_strategy)
def test_carro_de_compras_Precio_setter(instance):
    original = instance.Precio
    instance.Precio = original
    assert instance.Precio == original



@given(instance=Carro_de_Compras_strategy)
def test_carro_de_compras_Cantidad_setter(instance):
    original = instance.Cantidad
    instance.Cantidad = original
    assert instance.Cantidad == original

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
def test_payment_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=Payment_strategy)
def test_payment_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original
