import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Fragmentos::Fragmento,
    Fragmentos::Fichero,
    Fragmentos::Aplicacion,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fragmentos::fragmento_is_not_abstract():
    assert not inspect.isabstract(Fragmentos::Fragmento)


def test_fragmentos::fragmento_constructor_exists():
    assert callable(Fragmentos::Fragmento.__init__)


def test_fragmentos::fragmento_constructor_args():
    sig = inspect.signature(Fragmentos::Fragmento.__init__)
    params = list(sig.parameters.keys())
    assert "numLinea" in params, "Missing parameter 'numLinea'"
    assert "texto" in params, "Missing parameter 'texto'"
    assert "posCaracter" in params, "Missing parameter 'posCaracter'"

def test_fragmentos::fragmento_has_numLinea():
    assert hasattr(Fragmentos::Fragmento, "numLinea")
    descriptor = None
    for klass in Fragmentos::Fragmento.__mro__:
        if "numLinea" in klass.__dict__:
            descriptor = klass.__dict__["numLinea"]
            break
    assert isinstance(descriptor, property)

def test_fragmentos::fragmento_has_texto():
    assert hasattr(Fragmentos::Fragmento, "texto")
    descriptor = None
    for klass in Fragmentos::Fragmento.__mro__:
        if "texto" in klass.__dict__:
            descriptor = klass.__dict__["texto"]
            break
    assert isinstance(descriptor, property)

def test_fragmentos::fragmento_has_posCaracter():
    assert hasattr(Fragmentos::Fragmento, "posCaracter")
    descriptor = None
    for klass in Fragmentos::Fragmento.__mro__:
        if "posCaracter" in klass.__dict__:
            descriptor = klass.__dict__["posCaracter"]
            break
    assert isinstance(descriptor, property)



def test_fragmentos::fichero_is_not_abstract():
    assert not inspect.isabstract(Fragmentos::Fichero)


def test_fragmentos::fichero_constructor_exists():
    assert callable(Fragmentos::Fichero.__init__)


def test_fragmentos::fichero_constructor_args():
    sig = inspect.signature(Fragmentos::Fichero.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_fragmentos::fichero_has_nombre():
    assert hasattr(Fragmentos::Fichero, "nombre")
    descriptor = None
    for klass in Fragmentos::Fichero.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_fragmentos::aplicacion_is_not_abstract():
    assert not inspect.isabstract(Fragmentos::Aplicacion)


def test_fragmentos::aplicacion_constructor_exists():
    assert callable(Fragmentos::Aplicacion.__init__)


def test_fragmentos::aplicacion_constructor_args():
    sig = inspect.signature(Fragmentos::Aplicacion.__init__)
    params = list(sig.parameters.keys())


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
Fragmentos::Fragmento_strategy = st.builds(
    Fragmentos::Fragmento,
    numLinea=
        st.integers(),
    texto=
        safe_text,
    posCaracter=
        st.integers()
)
Fragmentos::Fichero_strategy = st.builds(
    Fragmentos::Fichero,
    nombre=
        safe_text
)
Fragmentos::Aplicacion_strategy = st.builds(
    Fragmentos::Aplicacion,
)

@given(instance=Fragmentos::Fragmento_strategy)
@settings(max_examples=50)
def test_fragmentos::fragmento_instantiation(instance):
    assert isinstance(instance, Fragmentos::Fragmento)

@given(instance=Fragmentos::Fragmento_strategy)
def test_fragmentos::fragmento_numLinea_type(instance):
    assert isinstance(instance.numLinea, int)


@given(instance=Fragmentos::Fragmento_strategy)
def test_fragmentos::fragmento_numLinea_setter(instance):
    original = instance.numLinea
    instance.numLinea = original
    assert instance.numLinea == original

@given(instance=Fragmentos::Fragmento_strategy)
def test_fragmentos::fragmento_texto_type(instance):
    assert isinstance(instance.texto, str)


@given(instance=Fragmentos::Fragmento_strategy)
def test_fragmentos::fragmento_texto_setter(instance):
    original = instance.texto
    instance.texto = original
    assert instance.texto == original

@given(instance=Fragmentos::Fragmento_strategy)
def test_fragmentos::fragmento_posCaracter_type(instance):
    assert isinstance(instance.posCaracter, int)


@given(instance=Fragmentos::Fragmento_strategy)
def test_fragmentos::fragmento_posCaracter_setter(instance):
    original = instance.posCaracter
    instance.posCaracter = original
    assert instance.posCaracter == original

@given(instance=Fragmentos::Fichero_strategy)
@settings(max_examples=50)
def test_fragmentos::fichero_instantiation(instance):
    assert isinstance(instance, Fragmentos::Fichero)

@given(instance=Fragmentos::Fichero_strategy)
def test_fragmentos::fichero_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=Fragmentos::Fichero_strategy)
def test_fragmentos::fichero_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Fragmentos::Aplicacion_strategy)
@settings(max_examples=50)
def test_fragmentos::aplicacion_instantiation(instance):
    assert isinstance(instance, Fragmentos::Aplicacion)
