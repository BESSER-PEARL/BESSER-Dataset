import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MMA_Element,
    Element,
    MMA_Root,
    MMA_B,
    MMA_A,
    Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mma_element_is_not_abstract():
    assert not inspect.isabstract(MMA_Element)


def test_mma_element_constructor_exists():
    assert callable(MMA_Element.__init__)


def test_mma_element_constructor_args():
    sig = inspect.signature(MMA_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mma_element_has_name():
    assert hasattr(MMA_Element, "name")
    descriptor = None
    for klass in MMA_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_mma_root_is_not_abstract():
    assert not inspect.isabstract(MMA_Root)


def test_mma_root_constructor_exists():
    assert callable(MMA_Root.__init__)


def test_mma_root_constructor_args():
    sig = inspect.signature(MMA_Root.__init__)
    params = list(sig.parameters.keys())



def test_mma_b_is_not_abstract():
    assert not inspect.isabstract(MMA_B)


def test_mma_b_constructor_exists():
    assert callable(MMA_B.__init__)


def test_mma_b_constructor_args():
    sig = inspect.signature(MMA_B.__init__)
    params = list(sig.parameters.keys())



def test_mma_a_is_not_abstract():
    assert not inspect.isabstract(MMA_A)


def test_mma_a_constructor_exists():
    assert callable(MMA_A.__init__)


def test_mma_a_constructor_args():
    sig = inspect.signature(MMA_A.__init__)
    params = list(sig.parameters.keys())



def test_root_is_not_abstract():
    assert not inspect.isabstract(Root)


def test_root_constructor_exists():
    assert callable(Root.__init__)


def test_root_constructor_args():
    sig = inspect.signature(Root.__init__)
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
MMA_Element_strategy = st.builds(
    MMA_Element,
    name=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
MMA_Root_strategy = st.builds(
    MMA_Root,
)
MMA_B_strategy = st.builds(
    MMA_B,
)
MMA_A_strategy = st.builds(
    MMA_A,
)
Root_strategy = st.builds(
    Root,
)

@given(instance=MMA_Element_strategy)
@settings(max_examples=50)
def test_mma_element_instantiation(instance):
    assert isinstance(instance, MMA_Element)



@given(instance=MMA_Element_strategy)
def test_mma_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=MMA_Root_strategy)
@settings(max_examples=50)
def test_mma_root_instantiation(instance):
    assert isinstance(instance, MMA_Root)

@given(instance=MMA_B_strategy)
@settings(max_examples=50)
def test_mma_b_instantiation(instance):
    assert isinstance(instance, MMA_B)

@given(instance=MMA_A_strategy)
@settings(max_examples=50)
def test_mma_a_instantiation(instance):
    assert isinstance(instance, MMA_A)

@given(instance=Root_strategy)
@settings(max_examples=50)
def test_root_instantiation(instance):
    assert isinstance(instance, Root)
