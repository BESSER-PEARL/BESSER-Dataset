import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    classdiagram::NamedElement,
    TypedElement,
    classdiagram::ClassDiagram,
    classdiagram::Operation,
    classdiagram::Attribute,
    NamedElement,
    classdiagram::TypedElement,
    classdiagram::Class,
    classdiagram::Association,
    classdiagram::Dependency,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classdiagram::namedelement_is_not_abstract():
    assert not inspect.isabstract(classdiagram::NamedElement)


def test_classdiagram::namedelement_constructor_exists():
    assert callable(classdiagram::NamedElement.__init__)


def test_classdiagram::namedelement_constructor_args():
    sig = inspect.signature(classdiagram::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::namedelement_has_name():
    assert hasattr(classdiagram::NamedElement, "name")
    descriptor = None
    for klass in classdiagram::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::classdiagram_is_not_abstract():
    assert not inspect.isabstract(classdiagram::ClassDiagram)


def test_classdiagram::classdiagram_constructor_exists():
    assert callable(classdiagram::ClassDiagram.__init__)


def test_classdiagram::classdiagram_constructor_args():
    sig = inspect.signature(classdiagram::ClassDiagram.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::operation_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Operation)


def test_classdiagram::operation_constructor_exists():
    assert callable(classdiagram::Operation.__init__)


def test_classdiagram::operation_constructor_args():
    sig = inspect.signature(classdiagram::Operation.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Attribute)


def test_classdiagram::attribute_constructor_exists():
    assert callable(classdiagram::Attribute.__init__)


def test_classdiagram::attribute_constructor_args():
    sig = inspect.signature(classdiagram::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::typedelement_is_not_abstract():
    assert not inspect.isabstract(classdiagram::TypedElement)


def test_classdiagram::typedelement_constructor_exists():
    assert callable(classdiagram::TypedElement.__init__)


def test_classdiagram::typedelement_constructor_args():
    sig = inspect.signature(classdiagram::TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "public" in params, "Missing parameter 'public'"

def test_classdiagram::typedelement_has_public():
    assert hasattr(classdiagram::TypedElement, "public")
    descriptor = None
    for klass in classdiagram::TypedElement.__mro__:
        if "public" in klass.__dict__:
            descriptor = klass.__dict__["public"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::class_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Class)


def test_classdiagram::class_constructor_exists():
    assert callable(classdiagram::Class.__init__)


def test_classdiagram::class_constructor_args():
    sig = inspect.signature(classdiagram::Class.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::association_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Association)


def test_classdiagram::association_constructor_exists():
    assert callable(classdiagram::Association.__init__)


def test_classdiagram::association_constructor_args():
    sig = inspect.signature(classdiagram::Association.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::dependency_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Dependency)


def test_classdiagram::dependency_constructor_exists():
    assert callable(classdiagram::Dependency.__init__)


def test_classdiagram::dependency_constructor_args():
    sig = inspect.signature(classdiagram::Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::dependency_has_name():
    assert hasattr(classdiagram::Dependency, "name")
    descriptor = None
    for klass in classdiagram::Dependency.__mro__:
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
classdiagram::NamedElement_strategy = st.builds(
    classdiagram::NamedElement,
    name=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
classdiagram::ClassDiagram_strategy = st.builds(
    classdiagram::ClassDiagram,
)
classdiagram::Operation_strategy = st.builds(
    classdiagram::Operation,
)
classdiagram::Attribute_strategy = st.builds(
    classdiagram::Attribute,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
classdiagram::TypedElement_strategy = st.builds(
    classdiagram::TypedElement,
    public=
        st.booleans()
)
classdiagram::Class_strategy = st.builds(
    classdiagram::Class,
)
classdiagram::Association_strategy = st.builds(
    classdiagram::Association,
)
classdiagram::Dependency_strategy = st.builds(
    classdiagram::Dependency,
    name=
        safe_text
)

@given(instance=classdiagram::NamedElement_strategy)
@settings(max_examples=50)
def test_classdiagram::namedelement_instantiation(instance):
    assert isinstance(instance, classdiagram::NamedElement)

@given(instance=classdiagram::NamedElement_strategy)
def test_classdiagram::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classdiagram::NamedElement_strategy)
def test_classdiagram::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=classdiagram::ClassDiagram_strategy)
@settings(max_examples=50)
def test_classdiagram::classdiagram_instantiation(instance):
    assert isinstance(instance, classdiagram::ClassDiagram)

@given(instance=classdiagram::Operation_strategy)
@settings(max_examples=50)
def test_classdiagram::operation_instantiation(instance):
    assert isinstance(instance, classdiagram::Operation)

@given(instance=classdiagram::Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram::attribute_instantiation(instance):
    assert isinstance(instance, classdiagram::Attribute)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=classdiagram::TypedElement_strategy)
@settings(max_examples=50)
def test_classdiagram::typedelement_instantiation(instance):
    assert isinstance(instance, classdiagram::TypedElement)

@given(instance=classdiagram::TypedElement_strategy)
def test_classdiagram::typedelement_public_type(instance):
    assert isinstance(instance.public, bool)


@given(instance=classdiagram::TypedElement_strategy)
def test_classdiagram::typedelement_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original

@given(instance=classdiagram::Class_strategy)
@settings(max_examples=50)
def test_classdiagram::class_instantiation(instance):
    assert isinstance(instance, classdiagram::Class)

@given(instance=classdiagram::Association_strategy)
@settings(max_examples=50)
def test_classdiagram::association_instantiation(instance):
    assert isinstance(instance, classdiagram::Association)

@given(instance=classdiagram::Dependency_strategy)
@settings(max_examples=50)
def test_classdiagram::dependency_instantiation(instance):
    assert isinstance(instance, classdiagram::Dependency)

@given(instance=classdiagram::Dependency_strategy)
def test_classdiagram::dependency_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classdiagram::Dependency_strategy)
def test_classdiagram::dependency_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
