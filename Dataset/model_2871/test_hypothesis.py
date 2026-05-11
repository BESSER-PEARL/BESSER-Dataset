import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PortB,
    TypeB::PortB,
    TypeB::OutPortB,
    TypeB::InPortB,
    TypeB::BlockB,
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
    assert not inspect.isabstract(TypeB::PortB)


def test_typeb::portb_constructor_exists():
    assert callable(TypeB::PortB.__init__)


def test_typeb::portb_constructor_args():
    sig = inspect.signature(TypeB::PortB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb::portb_has_name():
    assert hasattr(TypeB::PortB, "name")
    descriptor = None
    for klass in TypeB::PortB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeb::outportb_is_not_abstract():
    assert not inspect.isabstract(TypeB::OutPortB)


def test_typeb::outportb_constructor_exists():
    assert callable(TypeB::OutPortB.__init__)


def test_typeb::outportb_constructor_args():
    sig = inspect.signature(TypeB::OutPortB.__init__)
    params = list(sig.parameters.keys())



def test_typeb::inportb_is_not_abstract():
    assert not inspect.isabstract(TypeB::InPortB)


def test_typeb::inportb_constructor_exists():
    assert callable(TypeB::InPortB.__init__)


def test_typeb::inportb_constructor_args():
    sig = inspect.signature(TypeB::InPortB.__init__)
    params = list(sig.parameters.keys())



def test_typeb::blockb_is_not_abstract():
    assert not inspect.isabstract(TypeB::BlockB)


def test_typeb::blockb_constructor_exists():
    assert callable(TypeB::BlockB.__init__)


def test_typeb::blockb_constructor_args():
    sig = inspect.signature(TypeB::BlockB.__init__)
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
TypeB::PortB_strategy = st.builds(
    TypeB::PortB,
    name=
        safe_text
)
TypeB::OutPortB_strategy = st.builds(
    TypeB::OutPortB,
)
TypeB::InPortB_strategy = st.builds(
    TypeB::InPortB,
)
TypeB::BlockB_strategy = st.builds(
    TypeB::BlockB,
)

@given(instance=PortB_strategy)
@settings(max_examples=50)
def test_portb_instantiation(instance):
    assert isinstance(instance, PortB)

@given(instance=TypeB::PortB_strategy)
@settings(max_examples=50)
def test_typeb::portb_instantiation(instance):
    assert isinstance(instance, TypeB::PortB)

@given(instance=TypeB::PortB_strategy)
def test_typeb::portb_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeB::PortB_strategy)
def test_typeb::portb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeB::OutPortB_strategy)
@settings(max_examples=50)
def test_typeb::outportb_instantiation(instance):
    assert isinstance(instance, TypeB::OutPortB)

@given(instance=TypeB::InPortB_strategy)
@settings(max_examples=50)
def test_typeb::inportb_instantiation(instance):
    assert isinstance(instance, TypeB::InPortB)

@given(instance=TypeB::BlockB_strategy)
@settings(max_examples=50)
def test_typeb::blockb_instantiation(instance):
    assert isinstance(instance, TypeB::BlockB)
