import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Element,
    TransitionQVT::C,
    TransitionQVT::B,
    TransitionQVT::A,
    TransitionQVT::Element,
    TransitionQVT::Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_transitionqvt::c_is_not_abstract():
    assert not inspect.isabstract(TransitionQVT::C)


def test_transitionqvt::c_constructor_exists():
    assert callable(TransitionQVT::C.__init__)


def test_transitionqvt::c_constructor_args():
    sig = inspect.signature(TransitionQVT::C.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"

def test_transitionqvt::c_has_c():
    assert hasattr(TransitionQVT::C, "c")
    descriptor = None
    for klass in TransitionQVT::C.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)



def test_transitionqvt::b_is_not_abstract():
    assert not inspect.isabstract(TransitionQVT::B)


def test_transitionqvt::b_constructor_exists():
    assert callable(TransitionQVT::B.__init__)


def test_transitionqvt::b_constructor_args():
    sig = inspect.signature(TransitionQVT::B.__init__)
    params = list(sig.parameters.keys())
    assert "boss" in params, "Missing parameter 'boss'"

def test_transitionqvt::b_has_boss():
    assert hasattr(TransitionQVT::B, "boss")
    descriptor = None
    for klass in TransitionQVT::B.__mro__:
        if "boss" in klass.__dict__:
            descriptor = klass.__dict__["boss"]
            break
    assert isinstance(descriptor, property)



def test_transitionqvt::a_is_not_abstract():
    assert not inspect.isabstract(TransitionQVT::A)


def test_transitionqvt::a_constructor_exists():
    assert callable(TransitionQVT::A.__init__)


def test_transitionqvt::a_constructor_args():
    sig = inspect.signature(TransitionQVT::A.__init__)
    params = list(sig.parameters.keys())
    assert "reduction" in params, "Missing parameter 'reduction'"
    assert "height" in params, "Missing parameter 'height'"

def test_transitionqvt::a_has_reduction():
    assert hasattr(TransitionQVT::A, "reduction")
    descriptor = None
    for klass in TransitionQVT::A.__mro__:
        if "reduction" in klass.__dict__:
            descriptor = klass.__dict__["reduction"]
            break
    assert isinstance(descriptor, property)

def test_transitionqvt::a_has_height():
    assert hasattr(TransitionQVT::A, "height")
    descriptor = None
    for klass in TransitionQVT::A.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_transitionqvt::element_is_not_abstract():
    assert not inspect.isabstract(TransitionQVT::Element)


def test_transitionqvt::element_constructor_exists():
    assert callable(TransitionQVT::Element.__init__)


def test_transitionqvt::element_constructor_args():
    sig = inspect.signature(TransitionQVT::Element.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_transitionqvt::element_has_id():
    assert hasattr(TransitionQVT::Element, "id")
    descriptor = None
    for klass in TransitionQVT::Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_transitionqvt::root_is_not_abstract():
    assert not inspect.isabstract(TransitionQVT::Root)


def test_transitionqvt::root_constructor_exists():
    assert callable(TransitionQVT::Root.__init__)


def test_transitionqvt::root_constructor_args():
    sig = inspect.signature(TransitionQVT::Root.__init__)
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
Element_strategy = st.builds(
    Element,
)
TransitionQVT::C_strategy = st.builds(
    TransitionQVT::C,
    c=
        safe_text
)
TransitionQVT::B_strategy = st.builds(
    TransitionQVT::B,
    boss=
        safe_text
)
TransitionQVT::A_strategy = st.builds(
    TransitionQVT::A,
    reduction=
        safe_text,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
TransitionQVT::Element_strategy = st.builds(
    TransitionQVT::Element,
    id=
        st.integers()
)
TransitionQVT::Root_strategy = st.builds(
    TransitionQVT::Root,
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=TransitionQVT::C_strategy)
@settings(max_examples=50)
def test_transitionqvt::c_instantiation(instance):
    assert isinstance(instance, TransitionQVT::C)

@given(instance=TransitionQVT::C_strategy)
def test_transitionqvt::c_c_type(instance):
    assert isinstance(instance.c, str)


@given(instance=TransitionQVT::C_strategy)
def test_transitionqvt::c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=TransitionQVT::B_strategy)
@settings(max_examples=50)
def test_transitionqvt::b_instantiation(instance):
    assert isinstance(instance, TransitionQVT::B)

@given(instance=TransitionQVT::B_strategy)
def test_transitionqvt::b_boss_type(instance):
    assert isinstance(instance.boss, str)


@given(instance=TransitionQVT::B_strategy)
def test_transitionqvt::b_boss_setter(instance):
    original = instance.boss
    instance.boss = original
    assert instance.boss == original

@given(instance=TransitionQVT::A_strategy)
@settings(max_examples=50)
def test_transitionqvt::a_instantiation(instance):
    assert isinstance(instance, TransitionQVT::A)

@given(instance=TransitionQVT::A_strategy)
def test_transitionqvt::a_reduction_type(instance):
    assert isinstance(instance.reduction, str)


@given(instance=TransitionQVT::A_strategy)
def test_transitionqvt::a_reduction_setter(instance):
    original = instance.reduction
    instance.reduction = original
    assert instance.reduction == original

@given(instance=TransitionQVT::A_strategy)
def test_transitionqvt::a_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=TransitionQVT::A_strategy)
def test_transitionqvt::a_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=TransitionQVT::Element_strategy)
@settings(max_examples=50)
def test_transitionqvt::element_instantiation(instance):
    assert isinstance(instance, TransitionQVT::Element)

@given(instance=TransitionQVT::Element_strategy)
def test_transitionqvt::element_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=TransitionQVT::Element_strategy)
def test_transitionqvt::element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=TransitionQVT::Root_strategy)
@settings(max_examples=50)
def test_transitionqvt::root_instantiation(instance):
    assert isinstance(instance, TransitionQVT::Root)
