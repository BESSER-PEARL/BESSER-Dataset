import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MMA::Element,
    Element,
    MMA::Root,
    MMA::B,
    MMA::A,
    Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mma::element_is_not_abstract():
    assert not inspect.isabstract(MMA::Element)


def test_mma::element_constructor_exists():
    assert callable(MMA::Element.__init__)


def test_mma::element_constructor_args():
    sig = inspect.signature(MMA::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mma::element_has_name():
    assert hasattr(MMA::Element, "name")
    descriptor = None
    for klass in MMA::Element.__mro__:
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



def test_mma::root_is_not_abstract():
    assert not inspect.isabstract(MMA::Root)


def test_mma::root_constructor_exists():
    assert callable(MMA::Root.__init__)


def test_mma::root_constructor_args():
    sig = inspect.signature(MMA::Root.__init__)
    params = list(sig.parameters.keys())



def test_mma::b_is_not_abstract():
    assert not inspect.isabstract(MMA::B)


def test_mma::b_constructor_exists():
    assert callable(MMA::B.__init__)


def test_mma::b_constructor_args():
    sig = inspect.signature(MMA::B.__init__)
    params = list(sig.parameters.keys())



def test_mma::a_is_not_abstract():
    assert not inspect.isabstract(MMA::A)


def test_mma::a_constructor_exists():
    assert callable(MMA::A.__init__)


def test_mma::a_constructor_args():
    sig = inspect.signature(MMA::A.__init__)
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
MMA::Element_strategy = st.builds(
    MMA::Element,
    name=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
MMA::Root_strategy = st.builds(
    MMA::Root,
)
MMA::B_strategy = st.builds(
    MMA::B,
)
MMA::A_strategy = st.builds(
    MMA::A,
)
Root_strategy = st.builds(
    Root,
)

@given(instance=MMA::Element_strategy)
@settings(max_examples=50)
def test_mma::element_instantiation(instance):
    assert isinstance(instance, MMA::Element)

@given(instance=MMA::Element_strategy)
def test_mma::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MMA::Element_strategy)
def test_mma::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=MMA::Root_strategy)
@settings(max_examples=50)
def test_mma::root_instantiation(instance):
    assert isinstance(instance, MMA::Root)

@given(instance=MMA::B_strategy)
@settings(max_examples=50)
def test_mma::b_instantiation(instance):
    assert isinstance(instance, MMA::B)

@given(instance=MMA::A_strategy)
@settings(max_examples=50)
def test_mma::a_instantiation(instance):
    assert isinstance(instance, MMA::A)

@given(instance=Root_strategy)
@settings(max_examples=50)
def test_root_instantiation(instance):
    assert isinstance(instance, Root)
