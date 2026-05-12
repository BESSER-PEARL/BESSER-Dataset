import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Gato,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gato_is_not_abstract():
    assert not inspect.isabstract(Gato)


def test_gato_constructor_exists():
    assert callable(Gato.__init__)


def test_gato_constructor_args():
    sig = inspect.signature(Gato.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "raza" in params, "Missing parameter 'raza'"
    assert "color" in params, "Missing parameter 'color'"

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

def test_gato_has_color():
    assert hasattr(Gato, "color")
    descriptor = None
    for klass in Gato.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
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
Gato_strategy = st.builds(
    Gato,
    nombre=
        safe_text,
    raza=
        safe_text,
    color=
        safe_text
)

@given(instance=Gato_strategy)
@settings(max_examples=50)
def test_gato_instantiation(instance):
    assert isinstance(instance, Gato)



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



@given(instance=Gato_strategy)
def test_gato_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original
