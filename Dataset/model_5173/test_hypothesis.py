import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Element,
    ABC_B,
    ABC_C,
    ABC_A,
    ABC_Element,
    ABC_Root,
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



def test_abc_b_is_not_abstract():
    assert not inspect.isabstract(ABC_B)


def test_abc_b_constructor_exists():
    assert callable(ABC_B.__init__)


def test_abc_b_constructor_args():
    sig = inspect.signature(ABC_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_abc_b_has_b():
    assert hasattr(ABC_B, "b")
    descriptor = None
    for klass in ABC_B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_abc_c_is_not_abstract():
    assert not inspect.isabstract(ABC_C)


def test_abc_c_constructor_exists():
    assert callable(ABC_C.__init__)


def test_abc_c_constructor_args():
    sig = inspect.signature(ABC_C.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"

def test_abc_c_has_c():
    assert hasattr(ABC_C, "c")
    descriptor = None
    for klass in ABC_C.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)



def test_abc_a_is_not_abstract():
    assert not inspect.isabstract(ABC_A)


def test_abc_a_constructor_exists():
    assert callable(ABC_A.__init__)


def test_abc_a_constructor_args():
    sig = inspect.signature(ABC_A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_abc_a_has_a():
    assert hasattr(ABC_A, "a")
    descriptor = None
    for klass in ABC_A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_abc_element_is_not_abstract():
    assert not inspect.isabstract(ABC_Element)


def test_abc_element_constructor_exists():
    assert callable(ABC_Element.__init__)


def test_abc_element_constructor_args():
    sig = inspect.signature(ABC_Element.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_abc_element_has_id():
    assert hasattr(ABC_Element, "id")
    descriptor = None
    for klass in ABC_Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_abc_root_is_not_abstract():
    assert not inspect.isabstract(ABC_Root)


def test_abc_root_constructor_exists():
    assert callable(ABC_Root.__init__)


def test_abc_root_constructor_args():
    sig = inspect.signature(ABC_Root.__init__)
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
ABC_B_strategy = st.builds(
    ABC_B,
    b=
        safe_text
)
ABC_C_strategy = st.builds(
    ABC_C,
    c=
        safe_text
)
ABC_A_strategy = st.builds(
    ABC_A,
    a=
        safe_text
)
ABC_Element_strategy = st.builds(
    ABC_Element,
    id=
        st.integers()
)
ABC_Root_strategy = st.builds(
    ABC_Root,
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=ABC_B_strategy)
@settings(max_examples=50)
def test_abc_b_instantiation(instance):
    assert isinstance(instance, ABC_B)



@given(instance=ABC_B_strategy)
def test_abc_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=ABC_C_strategy)
@settings(max_examples=50)
def test_abc_c_instantiation(instance):
    assert isinstance(instance, ABC_C)



@given(instance=ABC_C_strategy)
def test_abc_c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=ABC_A_strategy)
@settings(max_examples=50)
def test_abc_a_instantiation(instance):
    assert isinstance(instance, ABC_A)



@given(instance=ABC_A_strategy)
def test_abc_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=ABC_Element_strategy)
@settings(max_examples=50)
def test_abc_element_instantiation(instance):
    assert isinstance(instance, ABC_Element)



@given(instance=ABC_Element_strategy)
def test_abc_element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ABC_Root_strategy)
@settings(max_examples=50)
def test_abc_root_instantiation(instance):
    assert isinstance(instance, ABC_Root)
