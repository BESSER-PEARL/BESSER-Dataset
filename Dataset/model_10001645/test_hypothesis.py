import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    CuentaBancaria,
    Gato,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_cuentabancaria_is_not_abstract():
    assert not inspect.isabstract(CuentaBancaria)


def test_cuentabancaria_constructor_exists():
    assert callable(CuentaBancaria.__init__)


def test_cuentabancaria_constructor_args():
    sig = inspect.signature(CuentaBancaria.__init__)
    params = list(sig.parameters.keys())
    assert "saldo" in params, "Missing parameter 'saldo'"

def test_cuentabancaria_has_saldo():
    assert hasattr(CuentaBancaria, "saldo")
    descriptor = None
    for klass in CuentaBancaria.__mro__:
        if "saldo" in klass.__dict__:
            descriptor = klass.__dict__["saldo"]
            break
    assert isinstance(descriptor, property)



def test_gato_is_not_abstract():
    assert not inspect.isabstract(Gato)


def test_gato_constructor_exists():
    assert callable(Gato.__init__)


def test_gato_constructor_args():
    sig = inspect.signature(Gato.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "raza" in params, "Missing parameter 'raza'"

def test_gato_has_color():
    assert hasattr(Gato, "color")
    descriptor = None
    for klass in Gato.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_gato_has_nombre():
    assert hasattr(Gato, "nombre")
    descriptor = None
    for klass in Gato.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_gato_has_raza():
    assert hasattr(Gato, "raza")
    descriptor = None
    for klass in Gato.__mro__:
        if "raza" in klass.__dict__:
            descriptor = klass.__dict__["raza"]
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
Class_strategy = st.builds(
    Class,
)
CuentaBancaria_strategy = st.builds(
    CuentaBancaria,
    saldo=
        st.integers()
)
Gato_strategy = st.builds(
    Gato,
    color=
        safe_text,
    nombre=
        safe_text,
    raza=
        safe_text
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=CuentaBancaria_strategy)
@settings(max_examples=50)
def test_cuentabancaria_instantiation(instance):
    assert isinstance(instance, CuentaBancaria)



@given(instance=CuentaBancaria_strategy)
def test_cuentabancaria_saldo_setter(instance):
    original = instance.saldo
    instance.saldo = original
    assert instance.saldo == original

@given(instance=Gato_strategy)
@settings(max_examples=50)
def test_gato_instantiation(instance):
    assert isinstance(instance, Gato)



@given(instance=Gato_strategy)
def test_gato_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Gato_strategy)
def test_gato_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Gato_strategy)
def test_gato_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original
