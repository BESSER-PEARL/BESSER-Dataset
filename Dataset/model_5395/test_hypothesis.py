import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    multicontainment_b_Identified,
    Identified,
    multicontainment_b_ChildB2,
    multicontainment_b_ChildB1,
    multicontainment_b_RootB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_multicontainment_b_identified_is_not_abstract():
    assert not inspect.isabstract(multicontainment_b_Identified)


def test_multicontainment_b_identified_constructor_exists():
    assert callable(multicontainment_b_Identified.__init__)


def test_multicontainment_b_identified_constructor_args():
    sig = inspect.signature(multicontainment_b_Identified.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_multicontainment_b_identified_has_id():
    assert hasattr(multicontainment_b_Identified, "id")
    descriptor = None
    for klass in multicontainment_b_Identified.__mro__:
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



def test_multicontainment_b_childb2_is_not_abstract():
    assert not inspect.isabstract(multicontainment_b_ChildB2)


def test_multicontainment_b_childb2_constructor_exists():
    assert callable(multicontainment_b_ChildB2.__init__)


def test_multicontainment_b_childb2_constructor_args():
    sig = inspect.signature(multicontainment_b_ChildB2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_multicontainment_b_childb2_has_name():
    assert hasattr(multicontainment_b_ChildB2, "name")
    descriptor = None
    for klass in multicontainment_b_ChildB2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_multicontainment_b_childb1_is_not_abstract():
    assert not inspect.isabstract(multicontainment_b_ChildB1)


def test_multicontainment_b_childb1_constructor_exists():
    assert callable(multicontainment_b_ChildB1.__init__)


def test_multicontainment_b_childb1_constructor_args():
    sig = inspect.signature(multicontainment_b_ChildB1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_multicontainment_b_childb1_has_name():
    assert hasattr(multicontainment_b_ChildB1, "name")
    descriptor = None
    for klass in multicontainment_b_ChildB1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_multicontainment_b_rootb_is_not_abstract():
    assert not inspect.isabstract(multicontainment_b_RootB)


def test_multicontainment_b_rootb_constructor_exists():
    assert callable(multicontainment_b_RootB.__init__)


def test_multicontainment_b_rootb_constructor_args():
    sig = inspect.signature(multicontainment_b_RootB.__init__)
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
multicontainment_b_Identified_strategy = st.builds(
    multicontainment_b_Identified,
    id=
        safe_text
)
Identified_strategy = st.builds(
    Identified,
)
multicontainment_b_ChildB2_strategy = st.builds(
    multicontainment_b_ChildB2,
    name=
        safe_text
)
multicontainment_b_ChildB1_strategy = st.builds(
    multicontainment_b_ChildB1,
    name=
        safe_text
)
multicontainment_b_RootB_strategy = st.builds(
    multicontainment_b_RootB,
)

@given(instance=multicontainment_b_Identified_strategy)
@settings(max_examples=50)
def test_multicontainment_b_identified_instantiation(instance):
    assert isinstance(instance, multicontainment_b_Identified)



@given(instance=multicontainment_b_Identified_strategy)
def test_multicontainment_b_identified_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Identified_strategy)
@settings(max_examples=50)
def test_identified_instantiation(instance):
    assert isinstance(instance, Identified)

@given(instance=multicontainment_b_ChildB2_strategy)
@settings(max_examples=50)
def test_multicontainment_b_childb2_instantiation(instance):
    assert isinstance(instance, multicontainment_b_ChildB2)



@given(instance=multicontainment_b_ChildB2_strategy)
def test_multicontainment_b_childb2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=multicontainment_b_ChildB1_strategy)
@settings(max_examples=50)
def test_multicontainment_b_childb1_instantiation(instance):
    assert isinstance(instance, multicontainment_b_ChildB1)



@given(instance=multicontainment_b_ChildB1_strategy)
def test_multicontainment_b_childb1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=multicontainment_b_RootB_strategy)
@settings(max_examples=50)
def test_multicontainment_b_rootb_instantiation(instance):
    assert isinstance(instance, multicontainment_b_RootB)
