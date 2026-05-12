import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    typeB_ElementB,
    typeB_RootB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typeb_elementb_is_not_abstract():
    assert not inspect.isabstract(typeB_ElementB)


def test_typeb_elementb_constructor_exists():
    assert callable(typeB_ElementB.__init__)


def test_typeb_elementb_constructor_args():
    sig = inspect.signature(typeB_ElementB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb_elementb_has_name():
    assert hasattr(typeB_ElementB, "name")
    descriptor = None
    for klass in typeB_ElementB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeb_rootb_is_not_abstract():
    assert not inspect.isabstract(typeB_RootB)


def test_typeb_rootb_constructor_exists():
    assert callable(typeB_RootB.__init__)


def test_typeb_rootb_constructor_args():
    sig = inspect.signature(typeB_RootB.__init__)
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
typeB_ElementB_strategy = st.builds(
    typeB_ElementB,
    name=
        safe_text
)
typeB_RootB_strategy = st.builds(
    typeB_RootB,
)

@given(instance=typeB_ElementB_strategy)
@settings(max_examples=50)
def test_typeb_elementb_instantiation(instance):
    assert isinstance(instance, typeB_ElementB)



@given(instance=typeB_ElementB_strategy)
def test_typeb_elementb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typeB_RootB_strategy)
@settings(max_examples=50)
def test_typeb_rootb_instantiation(instance):
    assert isinstance(instance, typeB_RootB)
