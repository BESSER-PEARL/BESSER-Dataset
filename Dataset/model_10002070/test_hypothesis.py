import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Booking,
    Report,
    RMS,
    Vegetariano,
    Class2,
    Class,
    Alimento,
    Orden,
    int,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "date" in params, "Missing parameter 'date'"
    assert "booking_Id" in params, "Missing parameter 'booking_Id'"
    assert "reservedTables" in params, "Missing parameter 'reservedTables'"
    assert "type" in params, "Missing parameter 'type'"
    assert "contact" in params, "Missing parameter 'contact'"

def test_booking_has_name():
    assert hasattr(Booking, "name")
    descriptor = None
    for klass in Booking.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_date():
    assert hasattr(Booking, "date")
    descriptor = None
    for klass in Booking.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_booking_Id():
    assert hasattr(Booking, "booking_Id")
    descriptor = None
    for klass in Booking.__mro__:
        if "booking_Id" in klass.__dict__:
            descriptor = klass.__dict__["booking_Id"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_reservedTables():
    assert hasattr(Booking, "reservedTables")
    descriptor = None
    for klass in Booking.__mro__:
        if "reservedTables" in klass.__dict__:
            descriptor = klass.__dict__["reservedTables"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_type():
    assert hasattr(Booking, "type")
    descriptor = None
    for klass in Booking.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_contact():
    assert hasattr(Booking, "contact")
    descriptor = None
    for klass in Booking.__mro__:
        if "contact" in klass.__dict__:
            descriptor = klass.__dict__["contact"]
            break
    assert isinstance(descriptor, property)



def test_report_is_not_abstract():
    assert not inspect.isabstract(Report)


def test_report_constructor_exists():
    assert callable(Report.__init__)


def test_report_constructor_args():
    sig = inspect.signature(Report.__init__)
    params = list(sig.parameters.keys())
    assert "totalSales" in params, "Missing parameter 'totalSales'"
    assert "orders" in params, "Missing parameter 'orders'"
    assert "profit" in params, "Missing parameter 'profit'"

def test_report_has_totalSales():
    assert hasattr(Report, "totalSales")
    descriptor = None
    for klass in Report.__mro__:
        if "totalSales" in klass.__dict__:
            descriptor = klass.__dict__["totalSales"]
            break
    assert isinstance(descriptor, property)

def test_report_has_orders():
    assert hasattr(Report, "orders")
    descriptor = None
    for klass in Report.__mro__:
        if "orders" in klass.__dict__:
            descriptor = klass.__dict__["orders"]
            break
    assert isinstance(descriptor, property)

def test_report_has_profit():
    assert hasattr(Report, "profit")
    descriptor = None
    for klass in Report.__mro__:
        if "profit" in klass.__dict__:
            descriptor = klass.__dict__["profit"]
            break
    assert isinstance(descriptor, property)



def test_rms_is_not_abstract():
    assert not inspect.isabstract(RMS)


def test_rms_constructor_exists():
    assert callable(RMS.__init__)


def test_rms_constructor_args():
    sig = inspect.signature(RMS.__init__)
    params = list(sig.parameters.keys())
    assert "bookings" in params, "Missing parameter 'bookings'"

def test_rms_has_bookings():
    assert hasattr(RMS, "bookings")
    descriptor = None
    for klass in RMS.__mro__:
        if "bookings" in klass.__dict__:
            descriptor = klass.__dict__["bookings"]
            break
    assert isinstance(descriptor, property)



def test_vegetariano_is_not_abstract():
    assert not inspect.isabstract(Vegetariano)


def test_vegetariano_constructor_exists():
    assert callable(Vegetariano.__init__)


def test_vegetariano_constructor_args():
    sig = inspect.signature(Vegetariano.__init__)
    params = list(sig.parameters.keys())
    assert "tipoDieta" in params, "Missing parameter 'tipoDieta'"

def test_vegetariano_has_tipoDieta():
    assert hasattr(Vegetariano, "tipoDieta")
    descriptor = None
    for klass in Vegetariano.__mro__:
        if "tipoDieta" in klass.__dict__:
            descriptor = klass.__dict__["tipoDieta"]
            break
    assert isinstance(descriptor, property)



def test_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_alimento_is_not_abstract():
    assert not inspect.isabstract(Alimento)


def test_alimento_constructor_exists():
    assert callable(Alimento.__init__)


def test_alimento_constructor_args():
    sig = inspect.signature(Alimento.__init__)
    params = list(sig.parameters.keys())
    assert "refrigeraci_n" in params, "Missing parameter 'refrigeraci_n'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "alimento_Id" in params, "Missing parameter 'alimento_Id'"
    assert "precio" in params, "Missing parameter 'precio'"

def test_alimento_has_refrigeraci_n():
    assert hasattr(Alimento, "refrigeraci_n")
    descriptor = None
    for klass in Alimento.__mro__:
        if "refrigeraci_n" in klass.__dict__:
            descriptor = klass.__dict__["refrigeraci_n"]
            break
    assert isinstance(descriptor, property)

def test_alimento_has_nombre():
    assert hasattr(Alimento, "nombre")
    descriptor = None
    for klass in Alimento.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_alimento_has_alimento_Id():
    assert hasattr(Alimento, "alimento_Id")
    descriptor = None
    for klass in Alimento.__mro__:
        if "alimento_Id" in klass.__dict__:
            descriptor = klass.__dict__["alimento_Id"]
            break
    assert isinstance(descriptor, property)

def test_alimento_has_precio():
    assert hasattr(Alimento, "precio")
    descriptor = None
    for klass in Alimento.__mro__:
        if "precio" in klass.__dict__:
            descriptor = klass.__dict__["precio"]
            break
    assert isinstance(descriptor, property)



def test_orden_is_not_abstract():
    assert not inspect.isabstract(Orden)


def test_orden_constructor_exists():
    assert callable(Orden.__init__)


def test_orden_constructor_args():
    sig = inspect.signature(Orden.__init__)
    params = list(sig.parameters.keys())
    assert "fecha" in params, "Missing parameter 'fecha'"
    assert "mesa" in params, "Missing parameter 'mesa'"
    assert "pagada" in params, "Missing parameter 'pagada'"
    assert "servida" in params, "Missing parameter 'servida'"
    assert "preparada" in params, "Missing parameter 'preparada'"
    assert "orden_Id" in params, "Missing parameter 'orden_Id'"
    assert "numComensales" in params, "Missing parameter 'numComensales'"

def test_orden_has_fecha():
    assert hasattr(Orden, "fecha")
    descriptor = None
    for klass in Orden.__mro__:
        if "fecha" in klass.__dict__:
            descriptor = klass.__dict__["fecha"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_mesa():
    assert hasattr(Orden, "mesa")
    descriptor = None
    for klass in Orden.__mro__:
        if "mesa" in klass.__dict__:
            descriptor = klass.__dict__["mesa"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_pagada():
    assert hasattr(Orden, "pagada")
    descriptor = None
    for klass in Orden.__mro__:
        if "pagada" in klass.__dict__:
            descriptor = klass.__dict__["pagada"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_servida():
    assert hasattr(Orden, "servida")
    descriptor = None
    for klass in Orden.__mro__:
        if "servida" in klass.__dict__:
            descriptor = klass.__dict__["servida"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_preparada():
    assert hasattr(Orden, "preparada")
    descriptor = None
    for klass in Orden.__mro__:
        if "preparada" in klass.__dict__:
            descriptor = klass.__dict__["preparada"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_orden_Id():
    assert hasattr(Orden, "orden_Id")
    descriptor = None
    for klass in Orden.__mro__:
        if "orden_Id" in klass.__dict__:
            descriptor = klass.__dict__["orden_Id"]
            break
    assert isinstance(descriptor, property)

def test_orden_has_numComensales():
    assert hasattr(Orden, "numComensales")
    descriptor = None
    for klass in Orden.__mro__:
        if "numComensales" in klass.__dict__:
            descriptor = klass.__dict__["numComensales"]
            break
    assert isinstance(descriptor, property)

def test_int_exists():
    # Check that the Enumeration exists
    assert int is not None

def test_int_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in int]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in int"


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
Booking_strategy = st.builds(
    Booking,
    name=
        safe_text,
    date=
        safe_text,
    booking_Id=
        safe_text,
    reservedTables=
        safe_text,
    type=
        st.integers(),
    contact=
        safe_text
)
Report_strategy = st.builds(
    Report,
    totalSales=
        safe_text,
    orders=
        safe_text,
    profit=
        safe_text
)
RMS_strategy = st.builds(
    RMS,
    bookings=
        safe_text
)
Vegetariano_strategy = st.builds(
    Vegetariano,
    tipoDieta=
        safe_text
)
Class2_strategy = st.builds(
    Class2,
)
Class_strategy = st.builds(
    Class,
)
Alimento_strategy = st.builds(
    Alimento,
    refrigeraci_n=
        st.booleans(),
    nombre=
        safe_text,
    alimento_Id=
        safe_text,
    precio=
        safe_text
)
Orden_strategy = st.builds(
    Orden,
    fecha=
        safe_text,
    mesa=
        st.integers(),
    pagada=
        st.booleans(),
    servida=
        st.booleans(),
    preparada=
        st.booleans(),
    orden_Id=
        safe_text,
    numComensales=
        st.integers()
)

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)



@given(instance=Booking_strategy)
def test_booking_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Booking_strategy)
def test_booking_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Booking_strategy)
def test_booking_booking_Id_setter(instance):
    original = instance.booking_Id
    instance.booking_Id = original
    assert instance.booking_Id == original



@given(instance=Booking_strategy)
def test_booking_reservedTables_setter(instance):
    original = instance.reservedTables
    instance.reservedTables = original
    assert instance.reservedTables == original



@given(instance=Booking_strategy)
def test_booking_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Booking_strategy)
def test_booking_contact_setter(instance):
    original = instance.contact
    instance.contact = original
    assert instance.contact == original

@given(instance=Report_strategy)
@settings(max_examples=50)
def test_report_instantiation(instance):
    assert isinstance(instance, Report)



@given(instance=Report_strategy)
def test_report_totalSales_setter(instance):
    original = instance.totalSales
    instance.totalSales = original
    assert instance.totalSales == original



@given(instance=Report_strategy)
def test_report_orders_setter(instance):
    original = instance.orders
    instance.orders = original
    assert instance.orders == original



@given(instance=Report_strategy)
def test_report_profit_setter(instance):
    original = instance.profit
    instance.profit = original
    assert instance.profit == original

@given(instance=RMS_strategy)
@settings(max_examples=50)
def test_rms_instantiation(instance):
    assert isinstance(instance, RMS)



@given(instance=RMS_strategy)
def test_rms_bookings_setter(instance):
    original = instance.bookings
    instance.bookings = original
    assert instance.bookings == original

@given(instance=Vegetariano_strategy)
@settings(max_examples=50)
def test_vegetariano_instantiation(instance):
    assert isinstance(instance, Vegetariano)



@given(instance=Vegetariano_strategy)
def test_vegetariano_tipoDieta_setter(instance):
    original = instance.tipoDieta
    instance.tipoDieta = original
    assert instance.tipoDieta == original

@given(instance=Class2_strategy)
@settings(max_examples=50)
def test_class2_instantiation(instance):
    assert isinstance(instance, Class2)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Alimento_strategy)
@settings(max_examples=50)
def test_alimento_instantiation(instance):
    assert isinstance(instance, Alimento)



@given(instance=Alimento_strategy)
def test_alimento_refrigeraci_n_setter(instance):
    original = instance.refrigeraci_n
    instance.refrigeraci_n = original
    assert instance.refrigeraci_n == original



@given(instance=Alimento_strategy)
def test_alimento_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Alimento_strategy)
def test_alimento_alimento_Id_setter(instance):
    original = instance.alimento_Id
    instance.alimento_Id = original
    assert instance.alimento_Id == original



@given(instance=Alimento_strategy)
def test_alimento_precio_setter(instance):
    original = instance.precio
    instance.precio = original
    assert instance.precio == original

@given(instance=Orden_strategy)
@settings(max_examples=50)
def test_orden_instantiation(instance):
    assert isinstance(instance, Orden)



@given(instance=Orden_strategy)
def test_orden_fecha_setter(instance):
    original = instance.fecha
    instance.fecha = original
    assert instance.fecha == original



@given(instance=Orden_strategy)
def test_orden_mesa_setter(instance):
    original = instance.mesa
    instance.mesa = original
    assert instance.mesa == original



@given(instance=Orden_strategy)
def test_orden_pagada_setter(instance):
    original = instance.pagada
    instance.pagada = original
    assert instance.pagada == original



@given(instance=Orden_strategy)
def test_orden_servida_setter(instance):
    original = instance.servida
    instance.servida = original
    assert instance.servida == original



@given(instance=Orden_strategy)
def test_orden_preparada_setter(instance):
    original = instance.preparada
    instance.preparada = original
    assert instance.preparada == original



@given(instance=Orden_strategy)
def test_orden_orden_Id_setter(instance):
    original = instance.orden_Id
    instance.orden_Id = original
    assert instance.orden_Id == original



@given(instance=Orden_strategy)
def test_orden_numComensales_setter(instance):
    original = instance.numComensales
    instance.numComensales = original
    assert instance.numComensales == original
