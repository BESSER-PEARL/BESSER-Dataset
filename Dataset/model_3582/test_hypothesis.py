import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    typeA_RootA,
    typeA_ElementA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typea_roota_is_not_abstract():
    assert not inspect.isabstract(typeA_RootA)


def test_typea_roota_constructor_exists():
    assert callable(typeA_RootA.__init__)


def test_typea_roota_constructor_args():
    sig = inspect.signature(typeA_RootA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typea_roota_has_name():
    assert hasattr(typeA_RootA, "name")
    descriptor = None
    for klass in typeA_RootA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typea_elementa_is_not_abstract():
    assert not inspect.isabstract(typeA_ElementA)


def test_typea_elementa_constructor_exists():
    assert callable(typeA_ElementA.__init__)


def test_typea_elementa_constructor_args():
    sig = inspect.signature(typeA_ElementA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typea_elementa_has_name():
    assert hasattr(typeA_ElementA, "name")
    descriptor = None
    for klass in typeA_ElementA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
typeA_RootA_strategy = st.builds(
    typeA_RootA,
    name=
        safe_text
)
typeA_ElementA_strategy = st.builds(
    typeA_ElementA,
    name=
        safe_text
)

@given(instance=typeA_RootA_strategy)
@settings(max_examples=50)
def test_typea_roota_instantiation(instance):
    assert isinstance(instance, typeA_RootA)



@given(instance=typeA_RootA_strategy)
def test_typea_roota_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typeA_ElementA_strategy)
@settings(max_examples=50)
def test_typea_elementa_instantiation(instance):
    assert isinstance(instance, typeA_ElementA)



@given(instance=typeA_ElementA_strategy)
def test_typea_elementa_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
