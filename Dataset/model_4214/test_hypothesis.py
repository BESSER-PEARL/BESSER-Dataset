import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mydsl::MyModel,
    MyAbstractElement,
    mydsl::MyReference,
    mydsl::MyElement,
    mydsl::MyAbstractElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::mymodel_is_not_abstract():
    assert not inspect.isabstract(mydsl::MyModel)


def test_mydsl::mymodel_constructor_exists():
    assert callable(mydsl::MyModel.__init__)


def test_mydsl::mymodel_constructor_args():
    sig = inspect.signature(mydsl::MyModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::mymodel_has_name():
    assert hasattr(mydsl::MyModel, "name")
    descriptor = None
    for klass in mydsl::MyModel.__mro__:
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



def test_mydsl::myreference_is_not_abstract():
    assert not inspect.isabstract(mydsl::MyReference)


def test_mydsl::myreference_constructor_exists():
    assert callable(mydsl::MyReference.__init__)


def test_mydsl::myreference_constructor_args():
    sig = inspect.signature(mydsl::MyReference.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::myelement_is_not_abstract():
    assert not inspect.isabstract(mydsl::MyElement)


def test_mydsl::myelement_constructor_exists():
    assert callable(mydsl::MyElement.__init__)


def test_mydsl::myelement_constructor_args():
    sig = inspect.signature(mydsl::MyElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::myelement_has_name():
    assert hasattr(mydsl::MyElement, "name")
    descriptor = None
    for klass in mydsl::MyElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::myabstractelement_is_not_abstract():
    assert not inspect.isabstract(mydsl::MyAbstractElement)


def test_mydsl::myabstractelement_constructor_exists():
    assert callable(mydsl::MyAbstractElement.__init__)


def test_mydsl::myabstractelement_constructor_args():
    sig = inspect.signature(mydsl::MyAbstractElement.__init__)
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
mydsl::MyModel_strategy = st.builds(
    mydsl::MyModel,
    name=
        safe_text
)
MyAbstractElement_strategy = st.builds(
    MyAbstractElement,
)
mydsl::MyReference_strategy = st.builds(
    mydsl::MyReference,
)
mydsl::MyElement_strategy = st.builds(
    mydsl::MyElement,
    name=
        safe_text
)
mydsl::MyAbstractElement_strategy = st.builds(
    mydsl::MyAbstractElement,
)

@given(instance=mydsl::MyModel_strategy)
@settings(max_examples=50)
def test_mydsl::mymodel_instantiation(instance):
    assert isinstance(instance, mydsl::MyModel)

@given(instance=mydsl::MyModel_strategy)
def test_mydsl::mymodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mydsl::MyModel_strategy)
def test_mydsl::mymodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MyAbstractElement_strategy)
@settings(max_examples=50)
def test_myabstractelement_instantiation(instance):
    assert isinstance(instance, MyAbstractElement)

@given(instance=mydsl::MyReference_strategy)
@settings(max_examples=50)
def test_mydsl::myreference_instantiation(instance):
    assert isinstance(instance, mydsl::MyReference)

@given(instance=mydsl::MyElement_strategy)
@settings(max_examples=50)
def test_mydsl::myelement_instantiation(instance):
    assert isinstance(instance, mydsl::MyElement)

@given(instance=mydsl::MyElement_strategy)
def test_mydsl::myelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mydsl::MyElement_strategy)
def test_mydsl::myelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mydsl::MyAbstractElement_strategy)
@settings(max_examples=50)
def test_mydsl::myabstractelement_instantiation(instance):
    assert isinstance(instance, mydsl::MyAbstractElement)
