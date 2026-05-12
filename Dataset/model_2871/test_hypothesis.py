import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PortB,
    TypeB_PortB,
    TypeB_OutPortB,
    TypeB_InPortB,
    TypeB_BlockB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_portb_is_not_abstract():
    assert not inspect.isabstract(PortB)


def test_portb_constructor_exists():
    assert callable(PortB.__init__)


def test_portb_constructor_args():
    sig = inspect.signature(PortB.__init__)
    params = list(sig.parameters.keys())



def test_typeb_portb_is_not_abstract():
    assert not inspect.isabstract(TypeB_PortB)


def test_typeb_portb_constructor_exists():
    assert callable(TypeB_PortB.__init__)


def test_typeb_portb_constructor_args():
    sig = inspect.signature(TypeB_PortB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb_portb_has_name():
    assert hasattr(TypeB_PortB, "name")
    descriptor = None
    for klass in TypeB_PortB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeb_outportb_is_not_abstract():
    assert not inspect.isabstract(TypeB_OutPortB)


def test_typeb_outportb_constructor_exists():
    assert callable(TypeB_OutPortB.__init__)


def test_typeb_outportb_constructor_args():
    sig = inspect.signature(TypeB_OutPortB.__init__)
    params = list(sig.parameters.keys())



def test_typeb_inportb_is_not_abstract():
    assert not inspect.isabstract(TypeB_InPortB)


def test_typeb_inportb_constructor_exists():
    assert callable(TypeB_InPortB.__init__)


def test_typeb_inportb_constructor_args():
    sig = inspect.signature(TypeB_InPortB.__init__)
    params = list(sig.parameters.keys())



def test_typeb_blockb_is_not_abstract():
    assert not inspect.isabstract(TypeB_BlockB)


def test_typeb_blockb_constructor_exists():
    assert callable(TypeB_BlockB.__init__)


def test_typeb_blockb_constructor_args():
    sig = inspect.signature(TypeB_BlockB.__init__)
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
PortB_strategy = st.builds(
    PortB,
)
TypeB_PortB_strategy = st.builds(
    TypeB_PortB,
    name=
        safe_text
)
TypeB_OutPortB_strategy = st.builds(
    TypeB_OutPortB,
)
TypeB_InPortB_strategy = st.builds(
    TypeB_InPortB,
)
TypeB_BlockB_strategy = st.builds(
    TypeB_BlockB,
)

@given(instance=PortB_strategy)
@settings(max_examples=50)
def test_portb_instantiation(instance):
    assert isinstance(instance, PortB)

@given(instance=TypeB_PortB_strategy)
@settings(max_examples=50)
def test_typeb_portb_instantiation(instance):
    assert isinstance(instance, TypeB_PortB)



@given(instance=TypeB_PortB_strategy)
def test_typeb_portb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeB_OutPortB_strategy)
@settings(max_examples=50)
def test_typeb_outportb_instantiation(instance):
    assert isinstance(instance, TypeB_OutPortB)

@given(instance=TypeB_InPortB_strategy)
@settings(max_examples=50)
def test_typeb_inportb_instantiation(instance):
    assert isinstance(instance, TypeB_InPortB)

@given(instance=TypeB_BlockB_strategy)
@settings(max_examples=50)
def test_typeb_blockb_instantiation(instance):
    assert isinstance(instance, TypeB_BlockB)
