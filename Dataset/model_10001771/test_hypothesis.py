import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ClassC,
    ClassB,
    ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classc_is_not_abstract():
    assert not inspect.isabstract(ClassC)


def test_classc_constructor_exists():
    assert callable(ClassC.__init__)


def test_classc_constructor_args():
    sig = inspect.signature(ClassC.__init__)
    params = list(sig.parameters.keys())
    assert "attC1" in params, "Missing parameter 'attC1'"
    assert "attC2" in params, "Missing parameter 'attC2'"

def test_classc_has_attC1():
    assert hasattr(ClassC, "attC1")
    descriptor = None
    for klass in ClassC.__mro__:
        if "attC1" in klass.__dict__:
            descriptor = klass.__dict__["attC1"]
            break
    assert isinstance(descriptor, property)

def test_classc_has_attC2():
    assert hasattr(ClassC, "attC2")
    descriptor = None
    for klass in ClassC.__mro__:
        if "attC2" in klass.__dict__:
            descriptor = klass.__dict__["attC2"]
            break
    assert isinstance(descriptor, property)



def test_classb_is_not_abstract():
    assert not inspect.isabstract(ClassB)


def test_classb_constructor_exists():
    assert callable(ClassB.__init__)


def test_classb_constructor_args():
    sig = inspect.signature(ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_classb_has_attribute():
    assert hasattr(ClassB, "attribute")
    descriptor = None
    for klass in ClassB.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_classa_is_not_abstract():
    assert not inspect.isabstract(ClassA)


def test_classa_constructor_exists():
    assert callable(ClassA.__init__)


def test_classa_constructor_args():
    sig = inspect.signature(ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "attA" in params, "Missing parameter 'attA'"

def test_classa_has_attA():
    assert hasattr(ClassA, "attA")
    descriptor = None
    for klass in ClassA.__mro__:
        if "attA" in klass.__dict__:
            descriptor = klass.__dict__["attA"]
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
ClassC_strategy = st.builds(
    ClassC,
    attC1=
        st.integers(),
    attC2=
        st.booleans()
)
ClassB_strategy = st.builds(
    ClassB,
    attribute=
        st.integers()
)
ClassA_strategy = st.builds(
    ClassA,
    attA=
        safe_text
)

@given(instance=ClassC_strategy)
@settings(max_examples=50)
def test_classc_instantiation(instance):
    assert isinstance(instance, ClassC)



@given(instance=ClassC_strategy)
def test_classc_attC1_setter(instance):
    original = instance.attC1
    instance.attC1 = original
    assert instance.attC1 == original



@given(instance=ClassC_strategy)
def test_classc_attC2_setter(instance):
    original = instance.attC2
    instance.attC2 = original
    assert instance.attC2 == original

@given(instance=ClassB_strategy)
@settings(max_examples=50)
def test_classb_instantiation(instance):
    assert isinstance(instance, ClassB)



@given(instance=ClassB_strategy)
def test_classb_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=ClassA_strategy)
@settings(max_examples=50)
def test_classa_instantiation(instance):
    assert isinstance(instance, ClassA)



@given(instance=ClassA_strategy)
def test_classa_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original
