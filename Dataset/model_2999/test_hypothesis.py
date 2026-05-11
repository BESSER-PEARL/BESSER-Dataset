import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    typeB::BlockB,
    PortB,
    typeB::InPortB,
    typeB::PortB,
    typeB::OutPortB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typeb::blockb_is_not_abstract():
    assert not inspect.isabstract(typeB::BlockB)


def test_typeb::blockb_constructor_exists():
    assert callable(typeB::BlockB.__init__)


def test_typeb::blockb_constructor_args():
    sig = inspect.signature(typeB::BlockB.__init__)
    params = list(sig.parameters.keys())



def test_portb_is_not_abstract():
    assert not inspect.isabstract(PortB)


def test_portb_constructor_exists():
    assert callable(PortB.__init__)


def test_portb_constructor_args():
    sig = inspect.signature(PortB.__init__)
    params = list(sig.parameters.keys())



def test_typeb::inportb_is_not_abstract():
    assert not inspect.isabstract(typeB::InPortB)


def test_typeb::inportb_constructor_exists():
    assert callable(typeB::InPortB.__init__)


def test_typeb::inportb_constructor_args():
    sig = inspect.signature(typeB::InPortB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb::inportb_has_name():
    assert hasattr(typeB::InPortB, "name")
    descriptor = None
    for klass in typeB::InPortB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeb::portb_is_not_abstract():
    assert not inspect.isabstract(typeB::PortB)


def test_typeb::portb_constructor_exists():
    assert callable(typeB::PortB.__init__)


def test_typeb::portb_constructor_args():
    sig = inspect.signature(typeB::PortB.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_typeb::portb_has_id():
    assert hasattr(typeB::PortB, "id")
    descriptor = None
    for klass in typeB::PortB.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_typeb::outportb_is_not_abstract():
    assert not inspect.isabstract(typeB::OutPortB)


def test_typeb::outportb_constructor_exists():
    assert callable(typeB::OutPortB.__init__)


def test_typeb::outportb_constructor_args():
    sig = inspect.signature(typeB::OutPortB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb::outportb_has_name():
    assert hasattr(typeB::OutPortB, "name")
    descriptor = None
    for klass in typeB::OutPortB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
typeB::BlockB_strategy = st.builds(
    typeB::BlockB,
)
PortB_strategy = st.builds(
    PortB,
)
typeB::InPortB_strategy = st.builds(
    typeB::InPortB,
    name=
        safe_text
)
typeB::PortB_strategy = st.builds(
    typeB::PortB,
    id=
        st.integers()
)
typeB::OutPortB_strategy = st.builds(
    typeB::OutPortB,
    name=
        safe_text
)

@given(instance=typeB::BlockB_strategy)
@settings(max_examples=50)
def test_typeb::blockb_instantiation(instance):
    assert isinstance(instance, typeB::BlockB)

@given(instance=PortB_strategy)
@settings(max_examples=50)
def test_portb_instantiation(instance):
    assert isinstance(instance, PortB)

@given(instance=typeB::InPortB_strategy)
@settings(max_examples=50)
def test_typeb::inportb_instantiation(instance):
    assert isinstance(instance, typeB::InPortB)

@given(instance=typeB::InPortB_strategy)
def test_typeb::inportb_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typeB::InPortB_strategy)
def test_typeb::inportb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typeB::PortB_strategy)
@settings(max_examples=50)
def test_typeb::portb_instantiation(instance):
    assert isinstance(instance, typeB::PortB)

@given(instance=typeB::PortB_strategy)
def test_typeb::portb_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=typeB::PortB_strategy)
def test_typeb::portb_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=typeB::OutPortB_strategy)
@settings(max_examples=50)
def test_typeb::outportb_instantiation(instance):
    assert isinstance(instance, typeB::OutPortB)

@given(instance=typeB::OutPortB_strategy)
def test_typeb::outportb_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typeB::OutPortB_strategy)
def test_typeb::outportb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
