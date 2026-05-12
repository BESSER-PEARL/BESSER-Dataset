import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    people_Model,
    people_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_people_model_is_not_abstract():
    assert not inspect.isabstract(people_Model)


def test_people_model_constructor_exists():
    assert callable(people_Model.__init__)


def test_people_model_constructor_args():
    sig = inspect.signature(people_Model.__init__)
    params = list(sig.parameters.keys())



def test_people_person_is_not_abstract():
    assert not inspect.isabstract(people_Person)


def test_people_person_constructor_exists():
    assert callable(people_Person.__init__)


def test_people_person_constructor_args():
    sig = inspect.signature(people_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_people_person_has_name():
    assert hasattr(people_Person, "name")
    descriptor = None
    for klass in people_Person.__mro__:
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
people_Model_strategy = st.builds(
    people_Model,
)
people_Person_strategy = st.builds(
    people_Person,
    name=
        safe_text
)

@given(instance=people_Model_strategy)
@settings(max_examples=50)
def test_people_model_instantiation(instance):
    assert isinstance(instance, people_Model)

@given(instance=people_Person_strategy)
@settings(max_examples=50)
def test_people_person_instantiation(instance):
    assert isinstance(instance, people_Person)



@given(instance=people_Person_strategy)
def test_people_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
