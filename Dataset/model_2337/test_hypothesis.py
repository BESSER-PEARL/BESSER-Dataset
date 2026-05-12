import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    persons_PersonGroup,
    persons_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons_persongroup_is_not_abstract():
    assert not inspect.isabstract(persons_PersonGroup)


def test_persons_persongroup_constructor_exists():
    assert callable(persons_PersonGroup.__init__)


def test_persons_persongroup_constructor_args():
    sig = inspect.signature(persons_PersonGroup.__init__)
    params = list(sig.parameters.keys())



def test_persons_person_is_not_abstract():
    assert not inspect.isabstract(persons_Person)


def test_persons_person_constructor_exists():
    assert callable(persons_Person.__init__)


def test_persons_person_constructor_args():
    sig = inspect.signature(persons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_persons_person_has_name():
    assert hasattr(persons_Person, "name")
    descriptor = None
    for klass in persons_Person.__mro__:
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
persons_PersonGroup_strategy = st.builds(
    persons_PersonGroup,
)
persons_Person_strategy = st.builds(
    persons_Person,
    name=
        safe_text
)

@given(instance=persons_PersonGroup_strategy)
@settings(max_examples=50)
def test_persons_persongroup_instantiation(instance):
    assert isinstance(instance, persons_PersonGroup)

@given(instance=persons_Person_strategy)
@settings(max_examples=50)
def test_persons_person_instantiation(instance):
    assert isinstance(instance, persons_Person)



@given(instance=persons_Person_strategy)
def test_persons_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
