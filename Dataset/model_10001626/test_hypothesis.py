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
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "Raza" in params, "Missing parameter 'Raza'"
    assert "Color" in params, "Missing parameter 'Color'"

def test_gato_has_Nombre():
    assert hasattr(Gato, "Nombre")
    descriptor = None
    for klass in Gato.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)

def test_gato_has_Raza():
    assert hasattr(Gato, "Raza")
    descriptor = None
    for klass in Gato.__mro__:
        if "Raza" in klass.__dict__:
            descriptor = klass.__dict__["Raza"]
            break
    assert isinstance(descriptor, property)

def test_gato_has_Color():
    assert hasattr(Gato, "Color")
    descriptor = None
    for klass in Gato.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
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
    Nombre=
        safe_text,
    Raza=
        safe_text,
    Color=
        safe_text
)

@given(instance=Gato_strategy)
@settings(max_examples=50)
def test_gato_instantiation(instance):
    assert isinstance(instance, Gato)



@given(instance=Gato_strategy)
def test_gato_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=Gato_strategy)
def test_gato_Raza_setter(instance):
    original = instance.Raza
    instance.Raza = original
    assert instance.Raza == original



@given(instance=Gato_strategy)
def test_gato_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original
