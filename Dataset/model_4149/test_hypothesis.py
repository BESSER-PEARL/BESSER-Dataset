import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractGreeting,
    myDsl::GreetingReference,
    myDsl::Greeting,
    myDsl::AbstractGreeting,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractgreeting_is_not_abstract():
    assert not inspect.isabstract(AbstractGreeting)


def test_abstractgreeting_constructor_exists():
    assert callable(AbstractGreeting.__init__)


def test_abstractgreeting_constructor_args():
    sig = inspect.signature(AbstractGreeting.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::greetingreference_is_not_abstract():
    assert not inspect.isabstract(myDsl::GreetingReference)


def test_mydsl::greetingreference_constructor_exists():
    assert callable(myDsl::GreetingReference.__init__)


def test_mydsl::greetingreference_constructor_args():
    sig = inspect.signature(myDsl::GreetingReference.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl::Greeting)


def test_mydsl::greeting_constructor_exists():
    assert callable(myDsl::Greeting.__init__)


def test_mydsl::greeting_constructor_args():
    sig = inspect.signature(myDsl::Greeting.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::abstractgreeting_is_not_abstract():
    assert not inspect.isabstract(myDsl::AbstractGreeting)


def test_mydsl::abstractgreeting_constructor_exists():
    assert callable(myDsl::AbstractGreeting.__init__)


def test_mydsl::abstractgreeting_constructor_args():
    sig = inspect.signature(myDsl::AbstractGreeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::abstractgreeting_has_name():
    assert hasattr(myDsl::AbstractGreeting, "name")
    descriptor = None
    for klass in myDsl::AbstractGreeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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
AbstractGreeting_strategy = st.builds(
    AbstractGreeting,
)
myDsl::GreetingReference_strategy = st.builds(
    myDsl::GreetingReference,
)
myDsl::Greeting_strategy = st.builds(
    myDsl::Greeting,
)
myDsl::AbstractGreeting_strategy = st.builds(
    myDsl::AbstractGreeting,
    name=
        safe_text
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=AbstractGreeting_strategy)
@settings(max_examples=50)
def test_abstractgreeting_instantiation(instance):
    assert isinstance(instance, AbstractGreeting)

@given(instance=myDsl::GreetingReference_strategy)
@settings(max_examples=50)
def test_mydsl::greetingreference_instantiation(instance):
    assert isinstance(instance, myDsl::GreetingReference)

@given(instance=myDsl::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl::greeting_instantiation(instance):
    assert isinstance(instance, myDsl::Greeting)

@given(instance=myDsl::AbstractGreeting_strategy)
@settings(max_examples=50)
def test_mydsl::abstractgreeting_instantiation(instance):
    assert isinstance(instance, myDsl::AbstractGreeting)

@given(instance=myDsl::AbstractGreeting_strategy)
def test_mydsl::abstractgreeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::AbstractGreeting_strategy)
def test_mydsl::abstractgreeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)
