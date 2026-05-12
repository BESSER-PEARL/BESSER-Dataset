import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Persons_Person,
    Persons_PersonContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons_person_is_not_abstract():
    assert not inspect.isabstract(Persons_Person)


def test_persons_person_constructor_exists():
    assert callable(Persons_Person.__init__)


def test_persons_person_constructor_args():
    sig = inspect.signature(Persons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_persons_person_has_name():
    assert hasattr(Persons_Person, "name")
    descriptor = None
    for klass in Persons_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_persons_person_has_ID():
    assert hasattr(Persons_Person, "ID")
    descriptor = None
    for klass in Persons_Person.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_persons_personcontainer_is_not_abstract():
    assert not inspect.isabstract(Persons_PersonContainer)


def test_persons_personcontainer_constructor_exists():
    assert callable(Persons_PersonContainer.__init__)


def test_persons_personcontainer_constructor_args():
    sig = inspect.signature(Persons_PersonContainer.__init__)
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
Persons_Person_strategy = st.builds(
    Persons_Person,
    name=
        safe_text,
    ID=
        st.integers()
)
Persons_PersonContainer_strategy = st.builds(
    Persons_PersonContainer,
)

@given(instance=Persons_Person_strategy)
@settings(max_examples=50)
def test_persons_person_instantiation(instance):
    assert isinstance(instance, Persons_Person)



@given(instance=Persons_Person_strategy)
def test_persons_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Persons_Person_strategy)
def test_persons_person_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Persons_PersonContainer_strategy)
@settings(max_examples=50)
def test_persons_personcontainer_instantiation(instance):
    assert isinstance(instance, Persons_PersonContainer)
