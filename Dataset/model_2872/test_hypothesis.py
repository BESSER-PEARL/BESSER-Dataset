import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PortB,
    typeB_PortB,
    typeB_OutPortB,
    typeB_InPortB,
    typeB_BlockB,
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
    assert not inspect.isabstract(typeB_PortB)


def test_typeb_portb_constructor_exists():
    assert callable(typeB_PortB.__init__)


def test_typeb_portb_constructor_args():
    sig = inspect.signature(typeB_PortB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb_portb_has_name():
    assert hasattr(typeB_PortB, "name")
    descriptor = None
    for klass in typeB_PortB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeb_outportb_is_not_abstract():
    assert not inspect.isabstract(typeB_OutPortB)


def test_typeb_outportb_constructor_exists():
    assert callable(typeB_OutPortB.__init__)


def test_typeb_outportb_constructor_args():
    sig = inspect.signature(typeB_OutPortB.__init__)
    params = list(sig.parameters.keys())



def test_typeb_inportb_is_not_abstract():
    assert not inspect.isabstract(typeB_InPortB)


def test_typeb_inportb_constructor_exists():
    assert callable(typeB_InPortB.__init__)


def test_typeb_inportb_constructor_args():
    sig = inspect.signature(typeB_InPortB.__init__)
    params = list(sig.parameters.keys())



def test_typeb_blockb_is_not_abstract():
    assert not inspect.isabstract(typeB_BlockB)


def test_typeb_blockb_constructor_exists():
    assert callable(typeB_BlockB.__init__)


def test_typeb_blockb_constructor_args():
    sig = inspect.signature(typeB_BlockB.__init__)
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
typeB_PortB_strategy = st.builds(
    typeB_PortB,
    name=
        safe_text
)
typeB_OutPortB_strategy = st.builds(
    typeB_OutPortB,
)
typeB_InPortB_strategy = st.builds(
    typeB_InPortB,
)
typeB_BlockB_strategy = st.builds(
    typeB_BlockB,
)

@given(instance=PortB_strategy)
@settings(max_examples=50)
def test_portb_instantiation(instance):
    assert isinstance(instance, PortB)

@given(instance=typeB_PortB_strategy)
@settings(max_examples=50)
def test_typeb_portb_instantiation(instance):
    assert isinstance(instance, typeB_PortB)



@given(instance=typeB_PortB_strategy)
def test_typeb_portb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typeB_OutPortB_strategy)
@settings(max_examples=50)
def test_typeb_outportb_instantiation(instance):
    assert isinstance(instance, typeB_OutPortB)

@given(instance=typeB_InPortB_strategy)
@settings(max_examples=50)
def test_typeb_inportb_instantiation(instance):
    assert isinstance(instance, typeB_InPortB)

@given(instance=typeB_BlockB_strategy)
@settings(max_examples=50)
def test_typeb_blockb_instantiation(instance):
    assert isinstance(instance, typeB_BlockB)
