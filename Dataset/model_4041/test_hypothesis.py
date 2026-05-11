import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    classdiagram::TypedElement,
    classdiagram::Typeable,
    classdiagram::NamedElement,
    TypedElement,
    classdiagram::Operation,
    classdiagram::Attribute,
    Typeable,
    classdiagram::Composition,
    classdiagram::DataType,
    classdiagram::Association,
    classdiagram::Dependency,
    classdiagram::Class,
    classdiagram::ClassDiagram,
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



def test_classdiagram::typeable_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Typeable)


def test_classdiagram::typeable_constructor_exists():
    assert callable(classdiagram::Typeable.__init__)


def test_classdiagram::typeable_constructor_args():
    sig = inspect.signature(classdiagram::Typeable.__init__)
    params = list(sig.parameters.keys())



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



def test_typeable_is_not_abstract():
    assert not inspect.isabstract(Typeable)


def test_typeable_constructor_exists():
    assert callable(Typeable.__init__)


def test_typeable_constructor_args():
    sig = inspect.signature(Typeable.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::composition_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Composition)


def test_classdiagram::composition_constructor_exists():
    assert callable(classdiagram::Composition.__init__)


def test_classdiagram::composition_constructor_args():
    sig = inspect.signature(classdiagram::Composition.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"

def test_classdiagram::composition_has_multiplicity():
    assert hasattr(classdiagram::Composition, "multiplicity")
    descriptor = None
    for klass in classdiagram::Composition.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::datatype_is_not_abstract():
    assert not inspect.isabstract(classdiagram::DataType)


def test_classdiagram::datatype_constructor_exists():
    assert callable(classdiagram::DataType.__init__)


def test_classdiagram::datatype_constructor_args():
    sig = inspect.signature(classdiagram::DataType.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::association_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Association)


def test_classdiagram::association_constructor_exists():
    assert callable(classdiagram::Association.__init__)


def test_classdiagram::association_constructor_args():
    sig = inspect.signature(classdiagram::Association.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"

def test_classdiagram::association_has_multiplicity():
    assert hasattr(classdiagram::Association, "multiplicity")
    descriptor = None
    for klass in classdiagram::Association.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)



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



def test_classdiagram::class_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Class)


def test_classdiagram::class_constructor_exists():
    assert callable(classdiagram::Class.__init__)


def test_classdiagram::class_constructor_args():
    sig = inspect.signature(classdiagram::Class.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::classdiagram_is_not_abstract():
    assert not inspect.isabstract(classdiagram::ClassDiagram)


def test_classdiagram::classdiagram_constructor_exists():
    assert callable(classdiagram::ClassDiagram.__init__)


def test_classdiagram::classdiagram_constructor_args():
    sig = inspect.signature(classdiagram::ClassDiagram.__init__)
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
classdiagram::TypedElement_strategy = st.builds(
    classdiagram::TypedElement,
    public=
        st.booleans()
)
classdiagram::Typeable_strategy = st.builds(
    classdiagram::Typeable,
)
classdiagram::NamedElement_strategy = st.builds(
    classdiagram::NamedElement,
    name=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
classdiagram::Operation_strategy = st.builds(
    classdiagram::Operation,
)
classdiagram::Attribute_strategy = st.builds(
    classdiagram::Attribute,
)
Typeable_strategy = st.builds(
    Typeable,
)
classdiagram::Composition_strategy = st.builds(
    classdiagram::Composition,
    multiplicity=
        safe_text
)
classdiagram::DataType_strategy = st.builds(
    classdiagram::DataType,
)
classdiagram::Association_strategy = st.builds(
    classdiagram::Association,
    multiplicity=
        safe_text
)
classdiagram::Dependency_strategy = st.builds(
    classdiagram::Dependency,
    name=
        safe_text
)
classdiagram::Class_strategy = st.builds(
    classdiagram::Class,
)
classdiagram::ClassDiagram_strategy = st.builds(
    classdiagram::ClassDiagram,
)

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

@given(instance=classdiagram::Typeable_strategy)
@settings(max_examples=50)
def test_classdiagram::typeable_instantiation(instance):
    assert isinstance(instance, classdiagram::Typeable)

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

@given(instance=classdiagram::Operation_strategy)
@settings(max_examples=50)
def test_classdiagram::operation_instantiation(instance):
    assert isinstance(instance, classdiagram::Operation)

@given(instance=classdiagram::Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram::attribute_instantiation(instance):
    assert isinstance(instance, classdiagram::Attribute)

@given(instance=Typeable_strategy)
@settings(max_examples=50)
def test_typeable_instantiation(instance):
    assert isinstance(instance, Typeable)

@given(instance=classdiagram::Composition_strategy)
@settings(max_examples=50)
def test_classdiagram::composition_instantiation(instance):
    assert isinstance(instance, classdiagram::Composition)

@given(instance=classdiagram::Composition_strategy)
def test_classdiagram::composition_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, str)


@given(instance=classdiagram::Composition_strategy)
def test_classdiagram::composition_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=classdiagram::DataType_strategy)
@settings(max_examples=50)
def test_classdiagram::datatype_instantiation(instance):
    assert isinstance(instance, classdiagram::DataType)

@given(instance=classdiagram::Association_strategy)
@settings(max_examples=50)
def test_classdiagram::association_instantiation(instance):
    assert isinstance(instance, classdiagram::Association)

@given(instance=classdiagram::Association_strategy)
def test_classdiagram::association_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, str)


@given(instance=classdiagram::Association_strategy)
def test_classdiagram::association_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

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

@given(instance=classdiagram::Class_strategy)
@settings(max_examples=50)
def test_classdiagram::class_instantiation(instance):
    assert isinstance(instance, classdiagram::Class)

@given(instance=classdiagram::ClassDiagram_strategy)
@settings(max_examples=50)
def test_classdiagram::classdiagram_instantiation(instance):
    assert isinstance(instance, classdiagram::ClassDiagram)
