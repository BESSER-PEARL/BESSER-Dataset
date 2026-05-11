import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Kasu1::ClassB,
    Kasu1::ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kasu1::classb_is_not_abstract():
    assert not inspect.isabstract(Kasu1::ClassB)


def test_kasu1::classb_constructor_exists():
    assert callable(Kasu1::ClassB.__init__)


def test_kasu1::classb_constructor_args():
    sig = inspect.signature(Kasu1::ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu1::classb_has_Name():
    assert hasattr(Kasu1::ClassB, "Name")
    descriptor = None
    for klass in Kasu1::ClassB.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu1::classa_is_not_abstract():
    assert not inspect.isabstract(Kasu1::ClassA)


def test_kasu1::classa_constructor_exists():
    assert callable(Kasu1::ClassA.__init__)


def test_kasu1::classa_constructor_args():
    sig = inspect.signature(Kasu1::ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu1::classa_has_Name():
    assert hasattr(Kasu1::ClassA, "Name")
    descriptor = None
    for klass in Kasu1::ClassA.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
Kasu1::ClassB_strategy = st.builds(
    Kasu1::ClassB,
    Name=
        safe_text
)
Kasu1::ClassA_strategy = st.builds(
    Kasu1::ClassA,
    Name=
        safe_text
)

@given(instance=Kasu1::ClassB_strategy)
@settings(max_examples=50)
def test_kasu1::classb_instantiation(instance):
    assert isinstance(instance, Kasu1::ClassB)

@given(instance=Kasu1::ClassB_strategy)
def test_kasu1::classb_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Kasu1::ClassB_strategy)
def test_kasu1::classb_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu1::ClassA_strategy)
@settings(max_examples=50)
def test_kasu1::classa_instantiation(instance):
    assert isinstance(instance, Kasu1::ClassA)

@given(instance=Kasu1::ClassA_strategy)
def test_kasu1::classa_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Kasu1::ClassA_strategy)
def test_kasu1::classa_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
