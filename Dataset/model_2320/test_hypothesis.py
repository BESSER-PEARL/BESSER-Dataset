import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Persons,
    Persons_Female,
    Persons_Male,
    Persons_Persons,
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



def test_persons_female_is_not_abstract():
    assert not inspect.isabstract(Persons_Female)


def test_persons_female_constructor_exists():
    assert callable(Persons_Female.__init__)


def test_persons_female_constructor_args():
    sig = inspect.signature(Persons_Female.__init__)
    params = list(sig.parameters.keys())



def test_persons_male_is_not_abstract():
    assert not inspect.isabstract(Persons_Male)


def test_persons_male_constructor_exists():
    assert callable(Persons_Male.__init__)


def test_persons_male_constructor_args():
    sig = inspect.signature(Persons_Male.__init__)
    params = list(sig.parameters.keys())



def test_persons_persons_is_not_abstract():
    assert not inspect.isabstract(Persons_Persons)


def test_persons_persons_constructor_exists():
    assert callable(Persons_Persons.__init__)


def test_persons_persons_constructor_args():
    sig = inspect.signature(Persons_Persons.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_persons_persons_has_fullName():
    assert hasattr(Persons_Persons, "fullName")
    descriptor = None
    for klass in Persons_Persons.__mro__:
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
Persons_Female_strategy = st.builds(
    Persons_Female,
)
Persons_Male_strategy = st.builds(
    Persons_Male,
)
Persons_Persons_strategy = st.builds(
    Persons_Persons,
    fullName=
        safe_text
)

@given(instance=Persons_strategy)
@settings(max_examples=50)
def test_persons_instantiation(instance):
    assert isinstance(instance, Persons)

@given(instance=Persons_Female_strategy)
@settings(max_examples=50)
def test_persons_female_instantiation(instance):
    assert isinstance(instance, Persons_Female)

@given(instance=Persons_Male_strategy)
@settings(max_examples=50)
def test_persons_male_instantiation(instance):
    assert isinstance(instance, Persons_Male)

@given(instance=Persons_Persons_strategy)
@settings(max_examples=50)
def test_persons_persons_instantiation(instance):
    assert isinstance(instance, Persons_Persons)



@given(instance=Persons_Persons_strategy)
def test_persons_persons_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original
