import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    USUARIO,
    CUENTA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_usuario_is_not_abstract():
    assert not inspect.isabstract(USUARIO)


def test_usuario_constructor_exists():
    assert callable(USUARIO.__init__)


def test_usuario_constructor_args():
    sig = inspect.signature(USUARIO.__init__)
    params = list(sig.parameters.keys())
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Contrase_a" in params, "Missing parameter 'Contrase_a'"

def test_usuario_has_Nombre():
    assert hasattr(USUARIO, "Nombre")
    descriptor = None
    for klass in USUARIO.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)

def test_usuario_has_ID():
    assert hasattr(USUARIO, "ID")
    descriptor = None
    for klass in USUARIO.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_usuario_has_Contrase_a():
    assert hasattr(USUARIO, "Contrase_a")
    descriptor = None
    for klass in USUARIO.__mro__:
        if "Contrase_a" in klass.__dict__:
            descriptor = klass.__dict__["Contrase_a"]
            break
    assert isinstance(descriptor, property)



def test_cuenta_is_not_abstract():
    assert not inspect.isabstract(CUENTA)


def test_cuenta_constructor_exists():
    assert callable(CUENTA.__init__)


def test_cuenta_constructor_args():
    sig = inspect.signature(CUENTA.__init__)
    params = list(sig.parameters.keys())
    assert "Balance" in params, "Missing parameter 'Balance'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "Tipo_de_Cuenta" in params, "Missing parameter 'Tipo_de_Cuenta'"

def test_cuenta_has_Balance():
    assert hasattr(CUENTA, "Balance")
    descriptor = None
    for klass in CUENTA.__mro__:
        if "Balance" in klass.__dict__:
            descriptor = klass.__dict__["Balance"]
            break
    assert isinstance(descriptor, property)

def test_cuenta_has_Nombre():
    assert hasattr(CUENTA, "Nombre")
    descriptor = None
    for klass in CUENTA.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)

def test_cuenta_has_Tipo_de_Cuenta():
    assert hasattr(CUENTA, "Tipo_de_Cuenta")
    descriptor = None
    for klass in CUENTA.__mro__:
        if "Tipo_de_Cuenta" in klass.__dict__:
            descriptor = klass.__dict__["Tipo_de_Cuenta"]
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
USUARIO_strategy = st.builds(
    USUARIO,
    Nombre=
        safe_text,
    ID=
        safe_text,
    Contrase_a=
        safe_text
)
CUENTA_strategy = st.builds(
    CUENTA,
    Balance=
        st.integers(),
    Nombre=
        safe_text,
    Tipo_de_Cuenta=
        safe_text
)

@given(instance=USUARIO_strategy)
@settings(max_examples=50)
def test_usuario_instantiation(instance):
    assert isinstance(instance, USUARIO)



@given(instance=USUARIO_strategy)
def test_usuario_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=USUARIO_strategy)
def test_usuario_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=USUARIO_strategy)
def test_usuario_Contrase_a_setter(instance):
    original = instance.Contrase_a
    instance.Contrase_a = original
    assert instance.Contrase_a == original

@given(instance=CUENTA_strategy)
@settings(max_examples=50)
def test_cuenta_instantiation(instance):
    assert isinstance(instance, CUENTA)



@given(instance=CUENTA_strategy)
def test_cuenta_Balance_setter(instance):
    original = instance.Balance
    instance.Balance = original
    assert instance.Balance == original



@given(instance=CUENTA_strategy)
def test_cuenta_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=CUENTA_strategy)
def test_cuenta_Tipo_de_Cuenta_setter(instance):
    original = instance.Tipo_de_Cuenta
    instance.Tipo_de_Cuenta = original
    assert instance.Tipo_de_Cuenta == original
