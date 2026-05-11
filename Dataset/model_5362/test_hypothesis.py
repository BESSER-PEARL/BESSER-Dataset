import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BaseType,
    base::nested::SubA,
    base::BaseType,
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



def test_base::nested::suba_is_not_abstract():
    assert not inspect.isabstract(base::nested::SubA)


def test_base::nested::suba_constructor_exists():
    assert callable(base::nested::SubA.__init__)


def test_base::nested::suba_constructor_args():
    sig = inspect.signature(base::nested::SubA.__init__)
    params = list(sig.parameters.keys())



def test_base::basetype_is_not_abstract():
    assert not inspect.isabstract(base::BaseType)


def test_base::basetype_constructor_exists():
    assert callable(base::BaseType.__init__)


def test_base::basetype_constructor_args():
    sig = inspect.signature(base::BaseType.__init__)
    params = list(sig.parameters.keys())
    assert "stuff" in params, "Missing parameter 'stuff'"

def test_base::basetype_has_stuff():
    assert hasattr(base::BaseType, "stuff")
    descriptor = None
    for klass in base::BaseType.__mro__:
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
base::nested::SubA_strategy = st.builds(
    base::nested::SubA,
)
base::BaseType_strategy = st.builds(
    base::BaseType,
    stuff=
        safe_text
)

@given(instance=BaseType_strategy)
@settings(max_examples=50)
def test_basetype_instantiation(instance):
    assert isinstance(instance, BaseType)

@given(instance=base::nested::SubA_strategy)
@settings(max_examples=50)
def test_base::nested::suba_instantiation(instance):
    assert isinstance(instance, base::nested::SubA)

@given(instance=base::BaseType_strategy)
@settings(max_examples=50)
def test_base::basetype_instantiation(instance):
    assert isinstance(instance, base::BaseType)

@given(instance=base::BaseType_strategy)
def test_base::basetype_stuff_type(instance):
    assert isinstance(instance.stuff, str)


@given(instance=base::BaseType_strategy)
def test_base::basetype_stuff_setter(instance):
    original = instance.stuff
    instance.stuff = original
    assert instance.stuff == original
