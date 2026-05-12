import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Fragmentos_Fragmento,
    Fragmentos_Fichero,
    Fragmentos_Aplicacion,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fragmentos_fragmento_is_not_abstract():
    assert not inspect.isabstract(Fragmentos_Fragmento)


def test_fragmentos_fragmento_constructor_exists():
    assert callable(Fragmentos_Fragmento.__init__)


def test_fragmentos_fragmento_constructor_args():
    sig = inspect.signature(Fragmentos_Fragmento.__init__)
    params = list(sig.parameters.keys())
    assert "posCaracter" in params, "Missing parameter 'posCaracter'"
    assert "texto" in params, "Missing parameter 'texto'"
    assert "numLinea" in params, "Missing parameter 'numLinea'"

def test_fragmentos_fragmento_has_posCaracter():
    assert hasattr(Fragmentos_Fragmento, "posCaracter")
    descriptor = None
    for klass in Fragmentos_Fragmento.__mro__:
        if "posCaracter" in klass.__dict__:
            descriptor = klass.__dict__["posCaracter"]
            break
    assert isinstance(descriptor, property)

def test_fragmentos_fragmento_has_texto():
    assert hasattr(Fragmentos_Fragmento, "texto")
    descriptor = None
    for klass in Fragmentos_Fragmento.__mro__:
        if "texto" in klass.__dict__:
            descriptor = klass.__dict__["texto"]
            break
    assert isinstance(descriptor, property)

def test_fragmentos_fragmento_has_numLinea():
    assert hasattr(Fragmentos_Fragmento, "numLinea")
    descriptor = None
    for klass in Fragmentos_Fragmento.__mro__:
        if "numLinea" in klass.__dict__:
            descriptor = klass.__dict__["numLinea"]
            break
    assert isinstance(descriptor, property)



def test_fragmentos_fichero_is_not_abstract():
    assert not inspect.isabstract(Fragmentos_Fichero)


def test_fragmentos_fichero_constructor_exists():
    assert callable(Fragmentos_Fichero.__init__)


def test_fragmentos_fichero_constructor_args():
    sig = inspect.signature(Fragmentos_Fichero.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_fragmentos_fichero_has_nombre():
    assert hasattr(Fragmentos_Fichero, "nombre")
    descriptor = None
    for klass in Fragmentos_Fichero.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_fragmentos_aplicacion_is_not_abstract():
    assert not inspect.isabstract(Fragmentos_Aplicacion)


def test_fragmentos_aplicacion_constructor_exists():
    assert callable(Fragmentos_Aplicacion.__init__)


def test_fragmentos_aplicacion_constructor_args():
    sig = inspect.signature(Fragmentos_Aplicacion.__init__)
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
Fragmentos_Fragmento_strategy = st.builds(
    Fragmentos_Fragmento,
    posCaracter=
        st.integers(),
    texto=
        safe_text,
    numLinea=
        st.integers()
)
Fragmentos_Fichero_strategy = st.builds(
    Fragmentos_Fichero,
    nombre=
        safe_text
)
Fragmentos_Aplicacion_strategy = st.builds(
    Fragmentos_Aplicacion,
)

@given(instance=Fragmentos_Fragmento_strategy)
@settings(max_examples=50)
def test_fragmentos_fragmento_instantiation(instance):
    assert isinstance(instance, Fragmentos_Fragmento)



@given(instance=Fragmentos_Fragmento_strategy)
def test_fragmentos_fragmento_posCaracter_setter(instance):
    original = instance.posCaracter
    instance.posCaracter = original
    assert instance.posCaracter == original



@given(instance=Fragmentos_Fragmento_strategy)
def test_fragmentos_fragmento_texto_setter(instance):
    original = instance.texto
    instance.texto = original
    assert instance.texto == original



@given(instance=Fragmentos_Fragmento_strategy)
def test_fragmentos_fragmento_numLinea_setter(instance):
    original = instance.numLinea
    instance.numLinea = original
    assert instance.numLinea == original

@given(instance=Fragmentos_Fichero_strategy)
@settings(max_examples=50)
def test_fragmentos_fichero_instantiation(instance):
    assert isinstance(instance, Fragmentos_Fichero)



@given(instance=Fragmentos_Fichero_strategy)
def test_fragmentos_fichero_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Fragmentos_Aplicacion_strategy)
@settings(max_examples=50)
def test_fragmentos_aplicacion_instantiation(instance):
    assert isinstance(instance, Fragmentos_Aplicacion)
