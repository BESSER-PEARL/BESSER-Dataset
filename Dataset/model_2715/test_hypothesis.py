import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Kasu3::ClassC,
    Kasu3::ClassB,
    Kasu3::ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kasu3::classc_is_not_abstract():
    assert not inspect.isabstract(Kasu3::ClassC)


def test_kasu3::classc_constructor_exists():
    assert callable(Kasu3::ClassC.__init__)


def test_kasu3::classc_constructor_args():
    sig = inspect.signature(Kasu3::ClassC.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu3::classc_has_Name():
    assert hasattr(Kasu3::ClassC, "Name")
    descriptor = None
    for klass in Kasu3::ClassC.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu3::classb_is_not_abstract():
    assert not inspect.isabstract(Kasu3::ClassB)


def test_kasu3::classb_constructor_exists():
    assert callable(Kasu3::ClassB.__init__)


def test_kasu3::classb_constructor_args():
    sig = inspect.signature(Kasu3::ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu3::classb_has_Name():
    assert hasattr(Kasu3::ClassB, "Name")
    descriptor = None
    for klass in Kasu3::ClassB.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu3::classa_is_not_abstract():
    assert not inspect.isabstract(Kasu3::ClassA)


def test_kasu3::classa_constructor_exists():
    assert callable(Kasu3::ClassA.__init__)


def test_kasu3::classa_constructor_args():
    sig = inspect.signature(Kasu3::ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu3::classa_has_Name():
    assert hasattr(Kasu3::ClassA, "Name")
    descriptor = None
    for klass in Kasu3::ClassA.__mro__:
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
Kasu3::ClassC_strategy = st.builds(
    Kasu3::ClassC,
    Name=
        safe_text
)
Kasu3::ClassB_strategy = st.builds(
    Kasu3::ClassB,
    Name=
        safe_text
)
Kasu3::ClassA_strategy = st.builds(
    Kasu3::ClassA,
    Name=
        safe_text
)

@given(instance=Kasu3::ClassC_strategy)
@settings(max_examples=50)
def test_kasu3::classc_instantiation(instance):
    assert isinstance(instance, Kasu3::ClassC)

@given(instance=Kasu3::ClassC_strategy)
def test_kasu3::classc_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Kasu3::ClassC_strategy)
def test_kasu3::classc_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu3::ClassB_strategy)
@settings(max_examples=50)
def test_kasu3::classb_instantiation(instance):
    assert isinstance(instance, Kasu3::ClassB)

@given(instance=Kasu3::ClassB_strategy)
def test_kasu3::classb_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Kasu3::ClassB_strategy)
def test_kasu3::classb_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu3::ClassA_strategy)
@settings(max_examples=50)
def test_kasu3::classa_instantiation(instance):
    assert isinstance(instance, Kasu3::ClassA)

@given(instance=Kasu3::ClassA_strategy)
def test_kasu3::classa_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Kasu3::ClassA_strategy)
def test_kasu3::classa_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
