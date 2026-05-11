import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Reponse,
    myDsl::ReponseF,
    myDsl::ReponseT,
    myDsl::Greeting,
    myDsl::Model,
    myDsl::Reponse,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_reponse_is_not_abstract():
    assert not inspect.isabstract(Reponse)


def test_reponse_constructor_exists():
    assert callable(Reponse.__init__)


def test_reponse_constructor_args():
    sig = inspect.signature(Reponse.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reponsef_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReponseF)


def test_mydsl::reponsef_constructor_exists():
    assert callable(myDsl::ReponseF.__init__)


def test_mydsl::reponsef_constructor_args():
    sig = inspect.signature(myDsl::ReponseF.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reponset_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReponseT)


def test_mydsl::reponset_constructor_exists():
    assert callable(myDsl::ReponseT.__init__)


def test_mydsl::reponset_constructor_args():
    sig = inspect.signature(myDsl::ReponseT.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl::Greeting)


def test_mydsl::greeting_constructor_exists():
    assert callable(myDsl::Greeting.__init__)


def test_mydsl::greeting_constructor_args():
    sig = inspect.signature(myDsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "question" in params, "Missing parameter 'question'"

def test_mydsl::greeting_has_question():
    assert hasattr(myDsl::Greeting, "question")
    descriptor = None
    for klass in myDsl::Greeting.__mro__:
        if "question" in klass.__dict__:
            descriptor = klass.__dict__["question"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reponse_is_not_abstract():
    assert not inspect.isabstract(myDsl::Reponse)


def test_mydsl::reponse_constructor_exists():
    assert callable(myDsl::Reponse.__init__)


def test_mydsl::reponse_constructor_args():
    sig = inspect.signature(myDsl::Reponse.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::reponse_has_name():
    assert hasattr(myDsl::Reponse, "name")
    descriptor = None
    for klass in myDsl::Reponse.__mro__:
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
Reponse_strategy = st.builds(
    Reponse,
)
myDsl::ReponseF_strategy = st.builds(
    myDsl::ReponseF,
)
myDsl::ReponseT_strategy = st.builds(
    myDsl::ReponseT,
)
myDsl::Greeting_strategy = st.builds(
    myDsl::Greeting,
    question=
        safe_text
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)
myDsl::Reponse_strategy = st.builds(
    myDsl::Reponse,
    name=
        safe_text
)

@given(instance=Reponse_strategy)
@settings(max_examples=50)
def test_reponse_instantiation(instance):
    assert isinstance(instance, Reponse)

@given(instance=myDsl::ReponseF_strategy)
@settings(max_examples=50)
def test_mydsl::reponsef_instantiation(instance):
    assert isinstance(instance, myDsl::ReponseF)

@given(instance=myDsl::ReponseT_strategy)
@settings(max_examples=50)
def test_mydsl::reponset_instantiation(instance):
    assert isinstance(instance, myDsl::ReponseT)

@given(instance=myDsl::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl::greeting_instantiation(instance):
    assert isinstance(instance, myDsl::Greeting)

@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_question_type(instance):
    assert isinstance(instance.question, str)


@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_question_setter(instance):
    original = instance.question
    instance.question = original
    assert instance.question == original

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)

@given(instance=myDsl::Reponse_strategy)
@settings(max_examples=50)
def test_mydsl::reponse_instantiation(instance):
    assert isinstance(instance, myDsl::Reponse)

@given(instance=myDsl::Reponse_strategy)
def test_mydsl::reponse_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Reponse_strategy)
def test_mydsl::reponse_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
