import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BaseType,
    base_nested_SubA,
    base_BaseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basetype_is_not_abstract():
    assert not inspect.isabstract(BaseType)


def test_basetype_constructor_exists():
    assert callable(BaseType.__init__)


def test_basetype_constructor_args():
    sig = inspect.signature(BaseType.__init__)
    params = list(sig.parameters.keys())



def test_base_nested_suba_is_not_abstract():
    assert not inspect.isabstract(base_nested_SubA)


def test_base_nested_suba_constructor_exists():
    assert callable(base_nested_SubA.__init__)


def test_base_nested_suba_constructor_args():
    sig = inspect.signature(base_nested_SubA.__init__)
    params = list(sig.parameters.keys())



def test_base_basetype_is_not_abstract():
    assert not inspect.isabstract(base_BaseType)


def test_base_basetype_constructor_exists():
    assert callable(base_BaseType.__init__)


def test_base_basetype_constructor_args():
    sig = inspect.signature(base_BaseType.__init__)
    params = list(sig.parameters.keys())
    assert "stuff" in params, "Missing parameter 'stuff'"

def test_base_basetype_has_stuff():
    assert hasattr(base_BaseType, "stuff")
    descriptor = None
    for klass in base_BaseType.__mro__:
        if "stuff" in klass.__dict__:
            descriptor = klass.__dict__["stuff"]
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
BaseType_strategy = st.builds(
    BaseType,
)
base_nested_SubA_strategy = st.builds(
    base_nested_SubA,
)
base_BaseType_strategy = st.builds(
    base_BaseType,
    stuff=
        safe_text
)

@given(instance=BaseType_strategy)
@settings(max_examples=50)
def test_basetype_instantiation(instance):
    assert isinstance(instance, BaseType)

@given(instance=base_nested_SubA_strategy)
@settings(max_examples=50)
def test_base_nested_suba_instantiation(instance):
    assert isinstance(instance, base_nested_SubA)

@given(instance=base_BaseType_strategy)
@settings(max_examples=50)
def test_base_basetype_instantiation(instance):
    assert isinstance(instance, base_BaseType)



@given(instance=base_BaseType_strategy)
def test_base_basetype_stuff_setter(instance):
    original = instance.stuff
    instance.stuff = original
    assert instance.stuff == original
