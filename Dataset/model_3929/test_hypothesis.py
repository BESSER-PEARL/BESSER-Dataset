import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Property,
    Type,
    myDsl::Datatype,
    myDsl::Entity,
    Element,
    myDsl::Namespace,
    myDsl::Type,
    myDsl::Import,
    myDsl::Element,
    myDsl::File,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::property_is_not_abstract():
    assert not inspect.isabstract(myDsl::Property)


def test_mydsl::property_constructor_exists():
    assert callable(myDsl::Property.__init__)


def test_mydsl::property_constructor_args():
    sig = inspect.signature(myDsl::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::property_has_name():
    assert hasattr(myDsl::Property, "name")
    descriptor = None
    for klass in myDsl::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::datatype_is_not_abstract():
    assert not inspect.isabstract(myDsl::Datatype)


def test_mydsl::datatype_constructor_exists():
    assert callable(myDsl::Datatype.__init__)


def test_mydsl::datatype_constructor_args():
    sig = inspect.signature(myDsl::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::entity_is_not_abstract():
    assert not inspect.isabstract(myDsl::Entity)


def test_mydsl::entity_constructor_exists():
    assert callable(myDsl::Entity.__init__)


def test_mydsl::entity_constructor_args():
    sig = inspect.signature(myDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::namespace_is_not_abstract():
    assert not inspect.isabstract(myDsl::Namespace)


def test_mydsl::namespace_constructor_exists():
    assert callable(myDsl::Namespace.__init__)


def test_mydsl::namespace_constructor_args():
    sig = inspect.signature(myDsl::Namespace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::namespace_has_name():
    assert hasattr(myDsl::Namespace, "name")
    descriptor = None
    for klass in myDsl::Namespace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type)


def test_mydsl::type_constructor_exists():
    assert callable(myDsl::Type.__init__)


def test_mydsl::type_constructor_args():
    sig = inspect.signature(myDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::type_has_name():
    assert hasattr(myDsl::Type, "name")
    descriptor = None
    for klass in myDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::import_is_not_abstract():
    assert not inspect.isabstract(myDsl::Import)


def test_mydsl::import_constructor_exists():
    assert callable(myDsl::Import.__init__)


def test_mydsl::import_constructor_args():
    sig = inspect.signature(myDsl::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_mydsl::import_has_importedNamespace():
    assert hasattr(myDsl::Import, "importedNamespace")
    descriptor = None
    for klass in myDsl::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::element_is_not_abstract():
    assert not inspect.isabstract(myDsl::Element)


def test_mydsl::element_constructor_exists():
    assert callable(myDsl::Element.__init__)


def test_mydsl::element_constructor_args():
    sig = inspect.signature(myDsl::Element.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::file_is_not_abstract():
    assert not inspect.isabstract(myDsl::File)


def test_mydsl::file_constructor_exists():
    assert callable(myDsl::File.__init__)


def test_mydsl::file_constructor_args():
    sig = inspect.signature(myDsl::File.__init__)
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
myDsl::Property_strategy = st.builds(
    myDsl::Property,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDsl::Datatype_strategy = st.builds(
    myDsl::Datatype,
)
myDsl::Entity_strategy = st.builds(
    myDsl::Entity,
)
Element_strategy = st.builds(
    Element,
)
myDsl::Namespace_strategy = st.builds(
    myDsl::Namespace,
    name=
        safe_text
)
myDsl::Type_strategy = st.builds(
    myDsl::Type,
    name=
        safe_text
)
myDsl::Import_strategy = st.builds(
    myDsl::Import,
    importedNamespace=
        safe_text
)
myDsl::Element_strategy = st.builds(
    myDsl::Element,
)
myDsl::File_strategy = st.builds(
    myDsl::File,
)

@given(instance=myDsl::Property_strategy)
@settings(max_examples=50)
def test_mydsl::property_instantiation(instance):
    assert isinstance(instance, myDsl::Property)

@given(instance=myDsl::Property_strategy)
def test_mydsl::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Property_strategy)
def test_mydsl::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl::Datatype_strategy)
@settings(max_examples=50)
def test_mydsl::datatype_instantiation(instance):
    assert isinstance(instance, myDsl::Datatype)

@given(instance=myDsl::Entity_strategy)
@settings(max_examples=50)
def test_mydsl::entity_instantiation(instance):
    assert isinstance(instance, myDsl::Entity)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=myDsl::Namespace_strategy)
@settings(max_examples=50)
def test_mydsl::namespace_instantiation(instance):
    assert isinstance(instance, myDsl::Namespace)

@given(instance=myDsl::Namespace_strategy)
def test_mydsl::namespace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Namespace_strategy)
def test_mydsl::namespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Type_strategy)
@settings(max_examples=50)
def test_mydsl::type_instantiation(instance):
    assert isinstance(instance, myDsl::Type)

@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Import_strategy)
@settings(max_examples=50)
def test_mydsl::import_instantiation(instance):
    assert isinstance(instance, myDsl::Import)

@given(instance=myDsl::Import_strategy)
def test_mydsl::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=myDsl::Import_strategy)
def test_mydsl::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=myDsl::Element_strategy)
@settings(max_examples=50)
def test_mydsl::element_instantiation(instance):
    assert isinstance(instance, myDsl::Element)

@given(instance=myDsl::File_strategy)
@settings(max_examples=50)
def test_mydsl::file_instantiation(instance):
    assert isinstance(instance, myDsl::File)
