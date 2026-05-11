import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Element,
    ABC::B,
    ABC::C,
    ABC::A,
    ABC::Element,
    ABC::Root,
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



def test_abc::b_is_not_abstract():
    assert not inspect.isabstract(ABC::B)


def test_abc::b_constructor_exists():
    assert callable(ABC::B.__init__)


def test_abc::b_constructor_args():
    sig = inspect.signature(ABC::B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_abc::b_has_b():
    assert hasattr(ABC::B, "b")
    descriptor = None
    for klass in ABC::B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_abc::c_is_not_abstract():
    assert not inspect.isabstract(ABC::C)


def test_abc::c_constructor_exists():
    assert callable(ABC::C.__init__)


def test_abc::c_constructor_args():
    sig = inspect.signature(ABC::C.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"

def test_abc::c_has_c():
    assert hasattr(ABC::C, "c")
    descriptor = None
    for klass in ABC::C.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)



def test_abc::a_is_not_abstract():
    assert not inspect.isabstract(ABC::A)


def test_abc::a_constructor_exists():
    assert callable(ABC::A.__init__)


def test_abc::a_constructor_args():
    sig = inspect.signature(ABC::A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_abc::a_has_a():
    assert hasattr(ABC::A, "a")
    descriptor = None
    for klass in ABC::A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_abc::element_is_not_abstract():
    assert not inspect.isabstract(ABC::Element)


def test_abc::element_constructor_exists():
    assert callable(ABC::Element.__init__)


def test_abc::element_constructor_args():
    sig = inspect.signature(ABC::Element.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_abc::element_has_id():
    assert hasattr(ABC::Element, "id")
    descriptor = None
    for klass in ABC::Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_abc::root_is_not_abstract():
    assert not inspect.isabstract(ABC::Root)


def test_abc::root_constructor_exists():
    assert callable(ABC::Root.__init__)


def test_abc::root_constructor_args():
    sig = inspect.signature(ABC::Root.__init__)
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
ABC::B_strategy = st.builds(
    ABC::B,
    b=
        safe_text
)
ABC::C_strategy = st.builds(
    ABC::C,
    c=
        safe_text
)
ABC::A_strategy = st.builds(
    ABC::A,
    a=
        safe_text
)
ABC::Element_strategy = st.builds(
    ABC::Element,
    id=
        st.integers()
)
ABC::Root_strategy = st.builds(
    ABC::Root,
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=ABC::B_strategy)
@settings(max_examples=50)
def test_abc::b_instantiation(instance):
    assert isinstance(instance, ABC::B)

@given(instance=ABC::B_strategy)
def test_abc::b_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=ABC::B_strategy)
def test_abc::b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=ABC::C_strategy)
@settings(max_examples=50)
def test_abc::c_instantiation(instance):
    assert isinstance(instance, ABC::C)

@given(instance=ABC::C_strategy)
def test_abc::c_c_type(instance):
    assert isinstance(instance.c, str)


@given(instance=ABC::C_strategy)
def test_abc::c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=ABC::A_strategy)
@settings(max_examples=50)
def test_abc::a_instantiation(instance):
    assert isinstance(instance, ABC::A)

@given(instance=ABC::A_strategy)
def test_abc::a_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=ABC::A_strategy)
def test_abc::a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=ABC::Element_strategy)
@settings(max_examples=50)
def test_abc::element_instantiation(instance):
    assert isinstance(instance, ABC::Element)

@given(instance=ABC::Element_strategy)
def test_abc::element_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=ABC::Element_strategy)
def test_abc::element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ABC::Root_strategy)
@settings(max_examples=50)
def test_abc::root_instantiation(instance):
    assert isinstance(instance, ABC::Root)
