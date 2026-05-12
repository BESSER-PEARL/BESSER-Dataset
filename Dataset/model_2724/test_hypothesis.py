import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Kasu2_Root,
    Kasu2_ClassB,
    Kasu2_ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kasu2_root_is_not_abstract():
    assert not inspect.isabstract(Kasu2_Root)


def test_kasu2_root_constructor_exists():
    assert callable(Kasu2_Root.__init__)


def test_kasu2_root_constructor_args():
    sig = inspect.signature(Kasu2_Root.__init__)
    params = list(sig.parameters.keys())



def test_kasu2_classb_is_not_abstract():
    assert not inspect.isabstract(Kasu2_ClassB)


def test_kasu2_classb_constructor_exists():
    assert callable(Kasu2_ClassB.__init__)


def test_kasu2_classb_constructor_args():
    sig = inspect.signature(Kasu2_ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu2_classb_has_Name():
    assert hasattr(Kasu2_ClassB, "Name")
    descriptor = None
    for klass in Kasu2_ClassB.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu2_classa_is_not_abstract():
    assert not inspect.isabstract(Kasu2_ClassA)


def test_kasu2_classa_constructor_exists():
    assert callable(Kasu2_ClassA.__init__)


def test_kasu2_classa_constructor_args():
    sig = inspect.signature(Kasu2_ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu2_classa_has_Name():
    assert hasattr(Kasu2_ClassA, "Name")
    descriptor = None
    for klass in Kasu2_ClassA.__mro__:
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
Kasu2_Root_strategy = st.builds(
    Kasu2_Root,
)
Kasu2_ClassB_strategy = st.builds(
    Kasu2_ClassB,
    Name=
        safe_text
)
Kasu2_ClassA_strategy = st.builds(
    Kasu2_ClassA,
    Name=
        safe_text
)

@given(instance=Kasu2_Root_strategy)
@settings(max_examples=50)
def test_kasu2_root_instantiation(instance):
    assert isinstance(instance, Kasu2_Root)

@given(instance=Kasu2_ClassB_strategy)
@settings(max_examples=50)
def test_kasu2_classb_instantiation(instance):
    assert isinstance(instance, Kasu2_ClassB)



@given(instance=Kasu2_ClassB_strategy)
def test_kasu2_classb_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu2_ClassA_strategy)
@settings(max_examples=50)
def test_kasu2_classa_instantiation(instance):
    assert isinstance(instance, Kasu2_ClassA)



@given(instance=Kasu2_ClassA_strategy)
def test_kasu2_classa_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
