import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypeA,
    myDsl_TypeB,
    myDsl_TypeA,
    myDsl_Greeting,
    myDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typea_is_not_abstract():
    assert not inspect.isabstract(TypeA)


def test_typea_constructor_exists():
    assert callable(TypeA.__init__)


def test_typea_constructor_args():
    sig = inspect.signature(TypeA.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_typeb_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeB)


def test_mydsl_typeb_constructor_exists():
    assert callable(myDsl_TypeB.__init__)


def test_mydsl_typeb_constructor_args():
    sig = inspect.signature(myDsl_TypeB.__init__)
    params = list(sig.parameters.keys())
    assert "fullname" in params, "Missing parameter 'fullname'"

def test_mydsl_typeb_has_fullname():
    assert hasattr(myDsl_TypeB, "fullname")
    descriptor = None
    for klass in myDsl_TypeB.__mro__:
        if "fullname" in klass.__dict__:
            descriptor = klass.__dict__["fullname"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_typea_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeA)


def test_mydsl_typea_constructor_exists():
    assert callable(myDsl_TypeA.__init__)


def test_mydsl_typea_constructor_args():
    sig = inspect.signature(myDsl_TypeA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_typea_has_name():
    assert hasattr(myDsl_TypeA, "name")
    descriptor = None
    for klass in myDsl_TypeA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl_Greeting)


def test_mydsl_greeting_constructor_exists():
    assert callable(myDsl_Greeting.__init__)


def test_mydsl_greeting_constructor_args():
    sig = inspect.signature(myDsl_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_greeting_has_name():
    assert hasattr(myDsl_Greeting, "name")
    descriptor = None
    for klass in myDsl_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
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
TypeA_strategy = st.builds(
    TypeA,
)
myDsl_TypeB_strategy = st.builds(
    myDsl_TypeB,
    fullname=
        safe_text
)
myDsl_TypeA_strategy = st.builds(
    myDsl_TypeA,
    name=
        safe_text
)
myDsl_Greeting_strategy = st.builds(
    myDsl_Greeting,
    name=
        safe_text
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)

@given(instance=TypeA_strategy)
@settings(max_examples=50)
def test_typea_instantiation(instance):
    assert isinstance(instance, TypeA)

@given(instance=myDsl_TypeB_strategy)
@settings(max_examples=50)
def test_mydsl_typeb_instantiation(instance):
    assert isinstance(instance, myDsl_TypeB)



@given(instance=myDsl_TypeB_strategy)
def test_mydsl_typeb_fullname_setter(instance):
    original = instance.fullname
    instance.fullname = original
    assert instance.fullname == original

@given(instance=myDsl_TypeA_strategy)
@settings(max_examples=50)
def test_mydsl_typea_instantiation(instance):
    assert isinstance(instance, myDsl_TypeA)



@given(instance=myDsl_TypeA_strategy)
def test_mydsl_typea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Greeting_strategy)
@settings(max_examples=50)
def test_mydsl_greeting_instantiation(instance):
    assert isinstance(instance, myDsl_Greeting)



@given(instance=myDsl_Greeting_strategy)
def test_mydsl_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)
