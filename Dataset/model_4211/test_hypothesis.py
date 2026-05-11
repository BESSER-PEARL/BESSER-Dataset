import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Element,
    myDsl::Greeting,
    myDsl::Person,
    myDsl::Element,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl::Greeting)


def test_mydsl::greeting_constructor_exists():
    assert callable(myDsl::Greeting.__init__)


def test_mydsl::greeting_constructor_args():
    sig = inspect.signature(myDsl::Greeting.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::person_is_not_abstract():
    assert not inspect.isabstract(myDsl::Person)


def test_mydsl::person_constructor_exists():
    assert callable(myDsl::Person.__init__)


def test_mydsl::person_constructor_args():
    sig = inspect.signature(myDsl::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::person_has_name():
    assert hasattr(myDsl::Person, "name")
    descriptor = None
    for klass in myDsl::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::element_is_not_abstract():
    assert not inspect.isabstract(myDsl::Element)


def test_mydsl::element_constructor_exists():
    assert callable(myDsl::Element.__init__)


def test_mydsl::element_constructor_args():
    sig = inspect.signature(myDsl::Element.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
Element_strategy = st.builds(
    Element,
)
myDsl::Greeting_strategy = st.builds(
    myDsl::Greeting,
)
myDsl::Person_strategy = st.builds(
    myDsl::Person,
    name=
        safe_text
)
myDsl::Element_strategy = st.builds(
    myDsl::Element,
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=myDsl::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl::greeting_instantiation(instance):
    assert isinstance(instance, myDsl::Greeting)

@given(instance=myDsl::Person_strategy)
@settings(max_examples=50)
def test_mydsl::person_instantiation(instance):
    assert isinstance(instance, myDsl::Person)

@given(instance=myDsl::Person_strategy)
def test_mydsl::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Person_strategy)
def test_mydsl::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Element_strategy)
@settings(max_examples=50)
def test_mydsl::element_instantiation(instance):
    assert isinstance(instance, myDsl::Element)

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)
