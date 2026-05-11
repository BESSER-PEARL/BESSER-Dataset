import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    typeB::ElementB,
    typeB::RootB,
    typeB::DefinitionB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typeb::elementb_is_not_abstract():
    assert not inspect.isabstract(typeB::ElementB)


def test_typeb::elementb_constructor_exists():
    assert callable(typeB::ElementB.__init__)


def test_typeb::elementb_constructor_args():
    sig = inspect.signature(typeB::ElementB.__init__)
    params = list(sig.parameters.keys())



def test_typeb::rootb_is_not_abstract():
    assert not inspect.isabstract(typeB::RootB)


def test_typeb::rootb_constructor_exists():
    assert callable(typeB::RootB.__init__)


def test_typeb::rootb_constructor_args():
    sig = inspect.signature(typeB::RootB.__init__)
    params = list(sig.parameters.keys())



def test_typeb::definitionb_is_not_abstract():
    assert not inspect.isabstract(typeB::DefinitionB)


def test_typeb::definitionb_constructor_exists():
    assert callable(typeB::DefinitionB.__init__)


def test_typeb::definitionb_constructor_args():
    sig = inspect.signature(typeB::DefinitionB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb::definitionb_has_name():
    assert hasattr(typeB::DefinitionB, "name")
    descriptor = None
    for klass in typeB::DefinitionB.__mro__:
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
typeB::ElementB_strategy = st.builds(
    typeB::ElementB,
)
typeB::RootB_strategy = st.builds(
    typeB::RootB,
)
typeB::DefinitionB_strategy = st.builds(
    typeB::DefinitionB,
    name=
        safe_text
)

@given(instance=typeB::ElementB_strategy)
@settings(max_examples=50)
def test_typeb::elementb_instantiation(instance):
    assert isinstance(instance, typeB::ElementB)

@given(instance=typeB::RootB_strategy)
@settings(max_examples=50)
def test_typeb::rootb_instantiation(instance):
    assert isinstance(instance, typeB::RootB)

@given(instance=typeB::DefinitionB_strategy)
@settings(max_examples=50)
def test_typeb::definitionb_instantiation(instance):
    assert isinstance(instance, typeB::DefinitionB)

@given(instance=typeB::DefinitionB_strategy)
def test_typeb::definitionb_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typeB::DefinitionB_strategy)
def test_typeb::definitionb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
