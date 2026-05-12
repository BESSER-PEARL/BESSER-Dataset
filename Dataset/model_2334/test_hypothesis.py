import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    personDsl_Person,
    personDsl_PersonContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persondsl_person_is_not_abstract():
    assert not inspect.isabstract(personDsl_Person)


def test_persondsl_person_constructor_exists():
    assert callable(personDsl_Person.__init__)


def test_persondsl_person_constructor_args():
    sig = inspect.signature(personDsl_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_persondsl_person_has_name():
    assert hasattr(personDsl_Person, "name")
    descriptor = None
    for klass in personDsl_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_persondsl_person_has_ID():
    assert hasattr(personDsl_Person, "ID")
    descriptor = None
    for klass in personDsl_Person.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_persondsl_personcontainer_is_not_abstract():
    assert not inspect.isabstract(personDsl_PersonContainer)


def test_persondsl_personcontainer_constructor_exists():
    assert callable(personDsl_PersonContainer.__init__)


def test_persondsl_personcontainer_constructor_args():
    sig = inspect.signature(personDsl_PersonContainer.__init__)
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
personDsl_Person_strategy = st.builds(
    personDsl_Person,
    name=
        safe_text,
    ID=
        st.integers()
)
personDsl_PersonContainer_strategy = st.builds(
    personDsl_PersonContainer,
)

@given(instance=personDsl_Person_strategy)
@settings(max_examples=50)
def test_persondsl_person_instantiation(instance):
    assert isinstance(instance, personDsl_Person)



@given(instance=personDsl_Person_strategy)
def test_persondsl_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=personDsl_Person_strategy)
def test_persondsl_person_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=personDsl_PersonContainer_strategy)
@settings(max_examples=50)
def test_persondsl_personcontainer_instantiation(instance):
    assert isinstance(instance, personDsl_PersonContainer)
