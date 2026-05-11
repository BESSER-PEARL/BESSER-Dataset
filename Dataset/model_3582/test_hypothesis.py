import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    typeA::RootA,
    typeA::ElementA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typea::roota_is_not_abstract():
    assert not inspect.isabstract(typeA::RootA)


def test_typea::roota_constructor_exists():
    assert callable(typeA::RootA.__init__)


def test_typea::roota_constructor_args():
    sig = inspect.signature(typeA::RootA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typea::roota_has_name():
    assert hasattr(typeA::RootA, "name")
    descriptor = None
    for klass in typeA::RootA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typea::elementa_is_not_abstract():
    assert not inspect.isabstract(typeA::ElementA)


def test_typea::elementa_constructor_exists():
    assert callable(typeA::ElementA.__init__)


def test_typea::elementa_constructor_args():
    sig = inspect.signature(typeA::ElementA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typea::elementa_has_name():
    assert hasattr(typeA::ElementA, "name")
    descriptor = None
    for klass in typeA::ElementA.__mro__:
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
typeA::RootA_strategy = st.builds(
    typeA::RootA,
    name=
        safe_text
)
typeA::ElementA_strategy = st.builds(
    typeA::ElementA,
    name=
        safe_text
)

@given(instance=typeA::RootA_strategy)
@settings(max_examples=50)
def test_typea::roota_instantiation(instance):
    assert isinstance(instance, typeA::RootA)

@given(instance=typeA::RootA_strategy)
def test_typea::roota_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typeA::RootA_strategy)
def test_typea::roota_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typeA::ElementA_strategy)
@settings(max_examples=50)
def test_typea::elementa_instantiation(instance):
    assert isinstance(instance, typeA::ElementA)

@given(instance=typeA::ElementA_strategy)
def test_typea::elementa_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typeA::ElementA_strategy)
def test_typea::elementa_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
