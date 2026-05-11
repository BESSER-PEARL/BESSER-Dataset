import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TypeA,
    myDsl::TypeB,
    myDsl::TypeA,
    myDsl::Greeting,
    myDsl::Model,
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



def test_mydsl::typeb_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeB)


def test_mydsl::typeb_constructor_exists():
    assert callable(myDsl::TypeB.__init__)


def test_mydsl::typeb_constructor_args():
    sig = inspect.signature(myDsl::TypeB.__init__)
    params = list(sig.parameters.keys())
    assert "fullname" in params, "Missing parameter 'fullname'"

def test_mydsl::typeb_has_fullname():
    assert hasattr(myDsl::TypeB, "fullname")
    descriptor = None
    for klass in myDsl::TypeB.__mro__:
        if "fullname" in klass.__dict__:
            descriptor = klass.__dict__["fullname"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::typea_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeA)


def test_mydsl::typea_constructor_exists():
    assert callable(myDsl::TypeA.__init__)


def test_mydsl::typea_constructor_args():
    sig = inspect.signature(myDsl::TypeA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::typea_has_name():
    assert hasattr(myDsl::TypeA, "name")
    descriptor = None
    for klass in myDsl::TypeA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl::Greeting)


def test_mydsl::greeting_constructor_exists():
    assert callable(myDsl::Greeting.__init__)


def test_mydsl::greeting_constructor_args():
    sig = inspect.signature(myDsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::greeting_has_name():
    assert hasattr(myDsl::Greeting, "name")
    descriptor = None
    for klass in myDsl::Greeting.__mro__:
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
TypeA_strategy = st.builds(
    TypeA,
)
myDsl::TypeB_strategy = st.builds(
    myDsl::TypeB,
    fullname=
        safe_text
)
myDsl::TypeA_strategy = st.builds(
    myDsl::TypeA,
    name=
        safe_text
)
myDsl::Greeting_strategy = st.builds(
    myDsl::Greeting,
    name=
        safe_text
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=TypeA_strategy)
@settings(max_examples=50)
def test_typea_instantiation(instance):
    assert isinstance(instance, TypeA)

@given(instance=myDsl::TypeB_strategy)
@settings(max_examples=50)
def test_mydsl::typeb_instantiation(instance):
    assert isinstance(instance, myDsl::TypeB)

@given(instance=myDsl::TypeB_strategy)
def test_mydsl::typeb_fullname_type(instance):
    assert isinstance(instance.fullname, str)


@given(instance=myDsl::TypeB_strategy)
def test_mydsl::typeb_fullname_setter(instance):
    original = instance.fullname
    instance.fullname = original
    assert instance.fullname == original

@given(instance=myDsl::TypeA_strategy)
@settings(max_examples=50)
def test_mydsl::typea_instantiation(instance):
    assert isinstance(instance, myDsl::TypeA)

@given(instance=myDsl::TypeA_strategy)
def test_mydsl::typea_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::TypeA_strategy)
def test_mydsl::typea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl::greeting_instantiation(instance):
    assert isinstance(instance, myDsl::Greeting)

@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)
