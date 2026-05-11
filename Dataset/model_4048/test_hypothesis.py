import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    necsis14::classdiagram::Attribute,
    necsis14::classdiagram::NamedElement,
    necsis14::classdiagram::Association,
    necsis14::classdiagram::Class,
    necsis14::classdiagram::ClassDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_necsis14::classdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(necsis14::classdiagram::Attribute)


def test_necsis14::classdiagram::attribute_constructor_exists():
    assert callable(necsis14::classdiagram::Attribute.__init__)


def test_necsis14::classdiagram::attribute_constructor_args():
    sig = inspect.signature(necsis14::classdiagram::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_necsis14::classdiagram::namedelement_is_not_abstract():
    assert not inspect.isabstract(necsis14::classdiagram::NamedElement)


def test_necsis14::classdiagram::namedelement_constructor_exists():
    assert callable(necsis14::classdiagram::NamedElement.__init__)


def test_necsis14::classdiagram::namedelement_constructor_args():
    sig = inspect.signature(necsis14::classdiagram::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_necsis14::classdiagram::namedelement_has_name():
    assert hasattr(necsis14::classdiagram::NamedElement, "name")
    descriptor = None
    for klass in necsis14::classdiagram::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_necsis14::classdiagram::association_is_not_abstract():
    assert not inspect.isabstract(necsis14::classdiagram::Association)


def test_necsis14::classdiagram::association_constructor_exists():
    assert callable(necsis14::classdiagram::Association.__init__)


def test_necsis14::classdiagram::association_constructor_args():
    sig = inspect.signature(necsis14::classdiagram::Association.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_necsis14::classdiagram::association_has_lowerBound():
    assert hasattr(necsis14::classdiagram::Association, "lowerBound")
    descriptor = None
    for klass in necsis14::classdiagram::Association.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_necsis14::classdiagram::association_has_upperBound():
    assert hasattr(necsis14::classdiagram::Association, "upperBound")
    descriptor = None
    for klass in necsis14::classdiagram::Association.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_necsis14::classdiagram::class_is_not_abstract():
    assert not inspect.isabstract(necsis14::classdiagram::Class)


def test_necsis14::classdiagram::class_constructor_exists():
    assert callable(necsis14::classdiagram::Class.__init__)


def test_necsis14::classdiagram::class_constructor_args():
    sig = inspect.signature(necsis14::classdiagram::Class.__init__)
    params = list(sig.parameters.keys())



def test_necsis14::classdiagram::classdiagram_is_not_abstract():
    assert not inspect.isabstract(necsis14::classdiagram::ClassDiagram)


def test_necsis14::classdiagram::classdiagram_constructor_exists():
    assert callable(necsis14::classdiagram::ClassDiagram.__init__)


def test_necsis14::classdiagram::classdiagram_constructor_args():
    sig = inspect.signature(necsis14::classdiagram::ClassDiagram.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
necsis14::classdiagram::Attribute_strategy = st.builds(
    necsis14::classdiagram::Attribute,
)
necsis14::classdiagram::NamedElement_strategy = st.builds(
    necsis14::classdiagram::NamedElement,
    name=
        safe_text
)
necsis14::classdiagram::Association_strategy = st.builds(
    necsis14::classdiagram::Association,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers()
)
necsis14::classdiagram::Class_strategy = st.builds(
    necsis14::classdiagram::Class,
)
necsis14::classdiagram::ClassDiagram_strategy = st.builds(
    necsis14::classdiagram::ClassDiagram,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=necsis14::classdiagram::Attribute_strategy)
@settings(max_examples=50)
def test_necsis14::classdiagram::attribute_instantiation(instance):
    assert isinstance(instance, necsis14::classdiagram::Attribute)

@given(instance=necsis14::classdiagram::NamedElement_strategy)
@settings(max_examples=50)
def test_necsis14::classdiagram::namedelement_instantiation(instance):
    assert isinstance(instance, necsis14::classdiagram::NamedElement)

@given(instance=necsis14::classdiagram::NamedElement_strategy)
def test_necsis14::classdiagram::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=necsis14::classdiagram::NamedElement_strategy)
def test_necsis14::classdiagram::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=necsis14::classdiagram::Association_strategy)
@settings(max_examples=50)
def test_necsis14::classdiagram::association_instantiation(instance):
    assert isinstance(instance, necsis14::classdiagram::Association)

@given(instance=necsis14::classdiagram::Association_strategy)
def test_necsis14::classdiagram::association_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=necsis14::classdiagram::Association_strategy)
def test_necsis14::classdiagram::association_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=necsis14::classdiagram::Association_strategy)
def test_necsis14::classdiagram::association_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=necsis14::classdiagram::Association_strategy)
def test_necsis14::classdiagram::association_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=necsis14::classdiagram::Class_strategy)
@settings(max_examples=50)
def test_necsis14::classdiagram::class_instantiation(instance):
    assert isinstance(instance, necsis14::classdiagram::Class)

@given(instance=necsis14::classdiagram::ClassDiagram_strategy)
@settings(max_examples=50)
def test_necsis14::classdiagram::classdiagram_instantiation(instance):
    assert isinstance(instance, necsis14::classdiagram::ClassDiagram)
