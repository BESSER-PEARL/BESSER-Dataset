import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Reponse,
    myDsl_ReponseF,
    myDsl_ReponseT,
    myDsl_Greeting,
    myDsl_Model,
    myDsl_Reponse,
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



def test_mydsl_reponsef_is_not_abstract():
    assert not inspect.isabstract(myDsl_ReponseF)


def test_mydsl_reponsef_constructor_exists():
    assert callable(myDsl_ReponseF.__init__)


def test_mydsl_reponsef_constructor_args():
    sig = inspect.signature(myDsl_ReponseF.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_reponset_is_not_abstract():
    assert not inspect.isabstract(myDsl_ReponseT)


def test_mydsl_reponset_constructor_exists():
    assert callable(myDsl_ReponseT.__init__)


def test_mydsl_reponset_constructor_args():
    sig = inspect.signature(myDsl_ReponseT.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl_Greeting)


def test_mydsl_greeting_constructor_exists():
    assert callable(myDsl_Greeting.__init__)


def test_mydsl_greeting_constructor_args():
    sig = inspect.signature(myDsl_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "question" in params, "Missing parameter 'question'"

def test_mydsl_greeting_has_question():
    assert hasattr(myDsl_Greeting, "question")
    descriptor = None
    for klass in myDsl_Greeting.__mro__:
        if "question" in klass.__dict__:
            descriptor = klass.__dict__["question"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_reponse_is_not_abstract():
    assert not inspect.isabstract(myDsl_Reponse)


def test_mydsl_reponse_constructor_exists():
    assert callable(myDsl_Reponse.__init__)


def test_mydsl_reponse_constructor_args():
    sig = inspect.signature(myDsl_Reponse.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_reponse_has_name():
    assert hasattr(myDsl_Reponse, "name")
    descriptor = None
    for klass in myDsl_Reponse.__mro__:
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
myDsl_ReponseF_strategy = st.builds(
    myDsl_ReponseF,
)
myDsl_ReponseT_strategy = st.builds(
    myDsl_ReponseT,
)
myDsl_Greeting_strategy = st.builds(
    myDsl_Greeting,
    question=
        safe_text
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)
myDsl_Reponse_strategy = st.builds(
    myDsl_Reponse,
    name=
        safe_text
)

@given(instance=Reponse_strategy)
@settings(max_examples=50)
def test_reponse_instantiation(instance):
    assert isinstance(instance, Reponse)

@given(instance=myDsl_ReponseF_strategy)
@settings(max_examples=50)
def test_mydsl_reponsef_instantiation(instance):
    assert isinstance(instance, myDsl_ReponseF)

@given(instance=myDsl_ReponseT_strategy)
@settings(max_examples=50)
def test_mydsl_reponset_instantiation(instance):
    assert isinstance(instance, myDsl_ReponseT)

@given(instance=myDsl_Greeting_strategy)
@settings(max_examples=50)
def test_mydsl_greeting_instantiation(instance):
    assert isinstance(instance, myDsl_Greeting)



@given(instance=myDsl_Greeting_strategy)
def test_mydsl_greeting_question_setter(instance):
    original = instance.question
    instance.question = original
    assert instance.question == original

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)

@given(instance=myDsl_Reponse_strategy)
@settings(max_examples=50)
def test_mydsl_reponse_instantiation(instance):
    assert isinstance(instance, myDsl_Reponse)



@given(instance=myDsl_Reponse_strategy)
def test_mydsl_reponse_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
