import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Kasu1_ClassB,
    Kasu1_ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kasu1_classb_is_not_abstract():
    assert not inspect.isabstract(Kasu1_ClassB)


def test_kasu1_classb_constructor_exists():
    assert callable(Kasu1_ClassB.__init__)


def test_kasu1_classb_constructor_args():
    sig = inspect.signature(Kasu1_ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu1_classb_has_Name():
    assert hasattr(Kasu1_ClassB, "Name")
    descriptor = None
    for klass in Kasu1_ClassB.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu1_classa_is_not_abstract():
    assert not inspect.isabstract(Kasu1_ClassA)


def test_kasu1_classa_constructor_exists():
    assert callable(Kasu1_ClassA.__init__)


def test_kasu1_classa_constructor_args():
    sig = inspect.signature(Kasu1_ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu1_classa_has_Name():
    assert hasattr(Kasu1_ClassA, "Name")
    descriptor = None
    for klass in Kasu1_ClassA.__mro__:
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
Kasu1_ClassB_strategy = st.builds(
    Kasu1_ClassB,
    Name=
        safe_text
)
Kasu1_ClassA_strategy = st.builds(
    Kasu1_ClassA,
    Name=
        safe_text
)

@given(instance=Kasu1_ClassB_strategy)
@settings(max_examples=50)
def test_kasu1_classb_instantiation(instance):
    assert isinstance(instance, Kasu1_ClassB)



@given(instance=Kasu1_ClassB_strategy)
def test_kasu1_classb_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu1_ClassA_strategy)
@settings(max_examples=50)
def test_kasu1_classa_instantiation(instance):
    assert isinstance(instance, Kasu1_ClassA)



@given(instance=Kasu1_ClassA_strategy)
def test_kasu1_classa_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
