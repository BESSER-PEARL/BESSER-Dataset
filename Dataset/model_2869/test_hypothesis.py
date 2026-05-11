import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PortB,
    typeB::PortB,
    typeB::InPortB,
    typeB::BlockB,
    typeB::OutPortB,
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



def test_typeb::portb_is_not_abstract():
    assert not inspect.isabstract(typeB::PortB)


def test_typeb::portb_constructor_exists():
    assert callable(typeB::PortB.__init__)


def test_typeb::portb_constructor_args():
    sig = inspect.signature(typeB::PortB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb::portb_has_name():
    assert hasattr(typeB::PortB, "name")
    descriptor = None
    for klass in typeB::PortB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeb::inportb_is_not_abstract():
    assert not inspect.isabstract(typeB::InPortB)


def test_typeb::inportb_constructor_exists():
    assert callable(typeB::InPortB.__init__)


def test_typeb::inportb_constructor_args():
    sig = inspect.signature(typeB::InPortB.__init__)
    params = list(sig.parameters.keys())



def test_typeb::blockb_is_not_abstract():
    assert not inspect.isabstract(typeB::BlockB)


def test_typeb::blockb_constructor_exists():
    assert callable(typeB::BlockB.__init__)


def test_typeb::blockb_constructor_args():
    sig = inspect.signature(typeB::BlockB.__init__)
    params = list(sig.parameters.keys())



def test_typeb::outportb_is_not_abstract():
    assert not inspect.isabstract(typeB::OutPortB)


def test_typeb::outportb_constructor_exists():
    assert callable(typeB::OutPortB.__init__)


def test_typeb::outportb_constructor_args():
    sig = inspect.signature(typeB::OutPortB.__init__)
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
typeB::PortB_strategy = st.builds(
    typeB::PortB,
    name=
        safe_text
)
typeB::InPortB_strategy = st.builds(
    typeB::InPortB,
)
typeB::BlockB_strategy = st.builds(
    typeB::BlockB,
)
typeB::OutPortB_strategy = st.builds(
    typeB::OutPortB,
)

@given(instance=PortB_strategy)
@settings(max_examples=50)
def test_portb_instantiation(instance):
    assert isinstance(instance, PortB)

@given(instance=typeB::PortB_strategy)
@settings(max_examples=50)
def test_typeb::portb_instantiation(instance):
    assert isinstance(instance, typeB::PortB)

@given(instance=typeB::PortB_strategy)
def test_typeb::portb_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typeB::PortB_strategy)
def test_typeb::portb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typeB::InPortB_strategy)
@settings(max_examples=50)
def test_typeb::inportb_instantiation(instance):
    assert isinstance(instance, typeB::InPortB)

@given(instance=typeB::BlockB_strategy)
@settings(max_examples=50)
def test_typeb::blockb_instantiation(instance):
    assert isinstance(instance, typeB::BlockB)

@given(instance=typeB::OutPortB_strategy)
@settings(max_examples=50)
def test_typeb::outportb_instantiation(instance):
    assert isinstance(instance, typeB::OutPortB)
