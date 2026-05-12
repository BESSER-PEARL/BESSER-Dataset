import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mydsl_MyAbstractElement,
    mydsl_MyModel,
    MyAbstractElement,
    mydsl_MyReference,
    mydsl_MyElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_myabstractelement_is_not_abstract():
    assert not inspect.isabstract(mydsl_MyAbstractElement)


def test_mydsl_myabstractelement_constructor_exists():
    assert callable(mydsl_MyAbstractElement.__init__)


def test_mydsl_myabstractelement_constructor_args():
    sig = inspect.signature(mydsl_MyAbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_mymodel_is_not_abstract():
    assert not inspect.isabstract(mydsl_MyModel)


def test_mydsl_mymodel_constructor_exists():
    assert callable(mydsl_MyModel.__init__)


def test_mydsl_mymodel_constructor_args():
    sig = inspect.signature(mydsl_MyModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_mymodel_has_name():
    assert hasattr(mydsl_MyModel, "name")
    descriptor = None
    for klass in mydsl_MyModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myabstractelement_is_not_abstract():
    assert not inspect.isabstract(MyAbstractElement)


def test_myabstractelement_constructor_exists():
    assert callable(MyAbstractElement.__init__)


def test_myabstractelement_constructor_args():
    sig = inspect.signature(MyAbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_myreference_is_not_abstract():
    assert not inspect.isabstract(mydsl_MyReference)


def test_mydsl_myreference_constructor_exists():
    assert callable(mydsl_MyReference.__init__)


def test_mydsl_myreference_constructor_args():
    sig = inspect.signature(mydsl_MyReference.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_myelement_is_not_abstract():
    assert not inspect.isabstract(mydsl_MyElement)


def test_mydsl_myelement_constructor_exists():
    assert callable(mydsl_MyElement.__init__)


def test_mydsl_myelement_constructor_args():
    sig = inspect.signature(mydsl_MyElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_myelement_has_name():
    assert hasattr(mydsl_MyElement, "name")
    descriptor = None
    for klass in mydsl_MyElement.__mro__:
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
mydsl_MyAbstractElement_strategy = st.builds(
    mydsl_MyAbstractElement,
)
mydsl_MyModel_strategy = st.builds(
    mydsl_MyModel,
    name=
        safe_text
)
MyAbstractElement_strategy = st.builds(
    MyAbstractElement,
)
mydsl_MyReference_strategy = st.builds(
    mydsl_MyReference,
)
mydsl_MyElement_strategy = st.builds(
    mydsl_MyElement,
    name=
        safe_text
)

@given(instance=mydsl_MyAbstractElement_strategy)
@settings(max_examples=50)
def test_mydsl_myabstractelement_instantiation(instance):
    assert isinstance(instance, mydsl_MyAbstractElement)

@given(instance=mydsl_MyModel_strategy)
@settings(max_examples=50)
def test_mydsl_mymodel_instantiation(instance):
    assert isinstance(instance, mydsl_MyModel)



@given(instance=mydsl_MyModel_strategy)
def test_mydsl_mymodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MyAbstractElement_strategy)
@settings(max_examples=50)
def test_myabstractelement_instantiation(instance):
    assert isinstance(instance, MyAbstractElement)

@given(instance=mydsl_MyReference_strategy)
@settings(max_examples=50)
def test_mydsl_myreference_instantiation(instance):
    assert isinstance(instance, mydsl_MyReference)

@given(instance=mydsl_MyElement_strategy)
@settings(max_examples=50)
def test_mydsl_myelement_instantiation(instance):
    assert isinstance(instance, mydsl_MyElement)



@given(instance=mydsl_MyElement_strategy)
def test_mydsl_myelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
