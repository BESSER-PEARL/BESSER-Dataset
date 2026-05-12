import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Kasu3_ClassC,
    Kasu3_ClassB,
    Kasu3_ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kasu3_classc_is_not_abstract():
    assert not inspect.isabstract(Kasu3_ClassC)


def test_kasu3_classc_constructor_exists():
    assert callable(Kasu3_ClassC.__init__)


def test_kasu3_classc_constructor_args():
    sig = inspect.signature(Kasu3_ClassC.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu3_classc_has_Name():
    assert hasattr(Kasu3_ClassC, "Name")
    descriptor = None
    for klass in Kasu3_ClassC.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu3_classb_is_not_abstract():
    assert not inspect.isabstract(Kasu3_ClassB)


def test_kasu3_classb_constructor_exists():
    assert callable(Kasu3_ClassB.__init__)


def test_kasu3_classb_constructor_args():
    sig = inspect.signature(Kasu3_ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu3_classb_has_Name():
    assert hasattr(Kasu3_ClassB, "Name")
    descriptor = None
    for klass in Kasu3_ClassB.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu3_classa_is_not_abstract():
    assert not inspect.isabstract(Kasu3_ClassA)


def test_kasu3_classa_constructor_exists():
    assert callable(Kasu3_ClassA.__init__)


def test_kasu3_classa_constructor_args():
    sig = inspect.signature(Kasu3_ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu3_classa_has_Name():
    assert hasattr(Kasu3_ClassA, "Name")
    descriptor = None
    for klass in Kasu3_ClassA.__mro__:
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
Kasu3_ClassC_strategy = st.builds(
    Kasu3_ClassC,
    Name=
        safe_text
)
Kasu3_ClassB_strategy = st.builds(
    Kasu3_ClassB,
    Name=
        safe_text
)
Kasu3_ClassA_strategy = st.builds(
    Kasu3_ClassA,
    Name=
        safe_text
)

@given(instance=Kasu3_ClassC_strategy)
@settings(max_examples=50)
def test_kasu3_classc_instantiation(instance):
    assert isinstance(instance, Kasu3_ClassC)



@given(instance=Kasu3_ClassC_strategy)
def test_kasu3_classc_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu3_ClassB_strategy)
@settings(max_examples=50)
def test_kasu3_classb_instantiation(instance):
    assert isinstance(instance, Kasu3_ClassB)



@given(instance=Kasu3_ClassB_strategy)
def test_kasu3_classb_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu3_ClassA_strategy)
@settings(max_examples=50)
def test_kasu3_classa_instantiation(instance):
    assert isinstance(instance, Kasu3_ClassA)



@given(instance=Kasu3_ClassA_strategy)
def test_kasu3_classa_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
