import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    multicontainment::b::Identified,
    Identified,
    multicontainment::b::ChildB2,
    multicontainment::b::ChildB1,
    multicontainment::b::RootB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_multicontainment::b::identified_is_not_abstract():
    assert not inspect.isabstract(multicontainment::b::Identified)


def test_multicontainment::b::identified_constructor_exists():
    assert callable(multicontainment::b::Identified.__init__)


def test_multicontainment::b::identified_constructor_args():
    sig = inspect.signature(multicontainment::b::Identified.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_multicontainment::b::identified_has_id():
    assert hasattr(multicontainment::b::Identified, "id")
    descriptor = None
    for klass in multicontainment::b::Identified.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_identified_is_not_abstract():
    assert not inspect.isabstract(Identified)


def test_identified_constructor_exists():
    assert callable(Identified.__init__)


def test_identified_constructor_args():
    sig = inspect.signature(Identified.__init__)
    params = list(sig.parameters.keys())



def test_multicontainment::b::childb2_is_not_abstract():
    assert not inspect.isabstract(multicontainment::b::ChildB2)


def test_multicontainment::b::childb2_constructor_exists():
    assert callable(multicontainment::b::ChildB2.__init__)


def test_multicontainment::b::childb2_constructor_args():
    sig = inspect.signature(multicontainment::b::ChildB2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_multicontainment::b::childb2_has_name():
    assert hasattr(multicontainment::b::ChildB2, "name")
    descriptor = None
    for klass in multicontainment::b::ChildB2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_multicontainment::b::childb1_is_not_abstract():
    assert not inspect.isabstract(multicontainment::b::ChildB1)


def test_multicontainment::b::childb1_constructor_exists():
    assert callable(multicontainment::b::ChildB1.__init__)


def test_multicontainment::b::childb1_constructor_args():
    sig = inspect.signature(multicontainment::b::ChildB1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_multicontainment::b::childb1_has_name():
    assert hasattr(multicontainment::b::ChildB1, "name")
    descriptor = None
    for klass in multicontainment::b::ChildB1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_multicontainment::b::rootb_is_not_abstract():
    assert not inspect.isabstract(multicontainment::b::RootB)


def test_multicontainment::b::rootb_constructor_exists():
    assert callable(multicontainment::b::RootB.__init__)


def test_multicontainment::b::rootb_constructor_args():
    sig = inspect.signature(multicontainment::b::RootB.__init__)
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
multicontainment::b::Identified_strategy = st.builds(
    multicontainment::b::Identified,
    id=
        safe_text
)
Identified_strategy = st.builds(
    Identified,
)
multicontainment::b::ChildB2_strategy = st.builds(
    multicontainment::b::ChildB2,
    name=
        safe_text
)
multicontainment::b::ChildB1_strategy = st.builds(
    multicontainment::b::ChildB1,
    name=
        safe_text
)
multicontainment::b::RootB_strategy = st.builds(
    multicontainment::b::RootB,
)

@given(instance=multicontainment::b::Identified_strategy)
@settings(max_examples=50)
def test_multicontainment::b::identified_instantiation(instance):
    assert isinstance(instance, multicontainment::b::Identified)

@given(instance=multicontainment::b::Identified_strategy)
def test_multicontainment::b::identified_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=multicontainment::b::Identified_strategy)
def test_multicontainment::b::identified_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Identified_strategy)
@settings(max_examples=50)
def test_identified_instantiation(instance):
    assert isinstance(instance, Identified)

@given(instance=multicontainment::b::ChildB2_strategy)
@settings(max_examples=50)
def test_multicontainment::b::childb2_instantiation(instance):
    assert isinstance(instance, multicontainment::b::ChildB2)

@given(instance=multicontainment::b::ChildB2_strategy)
def test_multicontainment::b::childb2_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=multicontainment::b::ChildB2_strategy)
def test_multicontainment::b::childb2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=multicontainment::b::ChildB1_strategy)
@settings(max_examples=50)
def test_multicontainment::b::childb1_instantiation(instance):
    assert isinstance(instance, multicontainment::b::ChildB1)

@given(instance=multicontainment::b::ChildB1_strategy)
def test_multicontainment::b::childb1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=multicontainment::b::ChildB1_strategy)
def test_multicontainment::b::childb1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=multicontainment::b::RootB_strategy)
@settings(max_examples=50)
def test_multicontainment::b::rootb_instantiation(instance):
    assert isinstance(instance, multicontainment::b::RootB)
