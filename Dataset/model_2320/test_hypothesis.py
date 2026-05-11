import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Persons,
    Persons::Female,
    Persons::Male,
    Persons::Persons,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons_is_not_abstract():
    assert not inspect.isabstract(Persons)


def test_persons_constructor_exists():
    assert callable(Persons.__init__)


def test_persons_constructor_args():
    sig = inspect.signature(Persons.__init__)
    params = list(sig.parameters.keys())



def test_persons::female_is_not_abstract():
    assert not inspect.isabstract(Persons::Female)


def test_persons::female_constructor_exists():
    assert callable(Persons::Female.__init__)


def test_persons::female_constructor_args():
    sig = inspect.signature(Persons::Female.__init__)
    params = list(sig.parameters.keys())



def test_persons::male_is_not_abstract():
    assert not inspect.isabstract(Persons::Male)


def test_persons::male_constructor_exists():
    assert callable(Persons::Male.__init__)


def test_persons::male_constructor_args():
    sig = inspect.signature(Persons::Male.__init__)
    params = list(sig.parameters.keys())



def test_persons::persons_is_not_abstract():
    assert not inspect.isabstract(Persons::Persons)


def test_persons::persons_constructor_exists():
    assert callable(Persons::Persons.__init__)


def test_persons::persons_constructor_args():
    sig = inspect.signature(Persons::Persons.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_persons::persons_has_fullName():
    assert hasattr(Persons::Persons, "fullName")
    descriptor = None
    for klass in Persons::Persons.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
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
Persons_strategy = st.builds(
    Persons,
)
Persons::Female_strategy = st.builds(
    Persons::Female,
)
Persons::Male_strategy = st.builds(
    Persons::Male,
)
Persons::Persons_strategy = st.builds(
    Persons::Persons,
    fullName=
        safe_text
)

@given(instance=Persons_strategy)
@settings(max_examples=50)
def test_persons_instantiation(instance):
    assert isinstance(instance, Persons)

@given(instance=Persons::Female_strategy)
@settings(max_examples=50)
def test_persons::female_instantiation(instance):
    assert isinstance(instance, Persons::Female)

@given(instance=Persons::Male_strategy)
@settings(max_examples=50)
def test_persons::male_instantiation(instance):
    assert isinstance(instance, Persons::Male)

@given(instance=Persons::Persons_strategy)
@settings(max_examples=50)
def test_persons::persons_instantiation(instance):
    assert isinstance(instance, Persons::Persons)

@given(instance=Persons::Persons_strategy)
def test_persons::persons_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=Persons::Persons_strategy)
def test_persons::persons_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original
