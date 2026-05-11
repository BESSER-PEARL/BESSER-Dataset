import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myTuto::Feature,
    Type,
    myTuto::Entity,
    myTuto::DataType,
    AbstractElement,
    myTuto::Import,
    myTuto::Type,
    myTuto::PackageDeclaration,
    myTuto::AbstractElement,
    myTuto::MyTuto,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mytuto::feature_is_not_abstract():
    assert not inspect.isabstract(myTuto::Feature)


def test_mytuto::feature_constructor_exists():
    assert callable(myTuto::Feature.__init__)


def test_mytuto::feature_constructor_args():
    sig = inspect.signature(myTuto::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_mytuto::feature_has_many():
    assert hasattr(myTuto::Feature, "many")
    descriptor = None
    for klass in myTuto::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_mytuto::feature_has_name():
    assert hasattr(myTuto::Feature, "name")
    descriptor = None
    for klass in myTuto::Feature.__mro__:
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



def test_mytuto::entity_is_not_abstract():
    assert not inspect.isabstract(myTuto::Entity)


def test_mytuto::entity_constructor_exists():
    assert callable(myTuto::Entity.__init__)


def test_mytuto::entity_constructor_args():
    sig = inspect.signature(myTuto::Entity.__init__)
    params = list(sig.parameters.keys())



def test_mytuto::datatype_is_not_abstract():
    assert not inspect.isabstract(myTuto::DataType)


def test_mytuto::datatype_constructor_exists():
    assert callable(myTuto::DataType.__init__)


def test_mytuto::datatype_constructor_args():
    sig = inspect.signature(myTuto::DataType.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_mytuto::import_is_not_abstract():
    assert not inspect.isabstract(myTuto::Import)


def test_mytuto::import_constructor_exists():
    assert callable(myTuto::Import.__init__)


def test_mytuto::import_constructor_args():
    sig = inspect.signature(myTuto::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNameSpace" in params, "Missing parameter 'importedNameSpace'"

def test_mytuto::import_has_importedNameSpace():
    assert hasattr(myTuto::Import, "importedNameSpace")
    descriptor = None
    for klass in myTuto::Import.__mro__:
        if "importedNameSpace" in klass.__dict__:
            descriptor = klass.__dict__["importedNameSpace"]
            break
    assert isinstance(descriptor, property)



def test_mytuto::type_is_not_abstract():
    assert not inspect.isabstract(myTuto::Type)


def test_mytuto::type_constructor_exists():
    assert callable(myTuto::Type.__init__)


def test_mytuto::type_constructor_args():
    sig = inspect.signature(myTuto::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mytuto::type_has_name():
    assert hasattr(myTuto::Type, "name")
    descriptor = None
    for klass in myTuto::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mytuto::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(myTuto::PackageDeclaration)


def test_mytuto::packagedeclaration_constructor_exists():
    assert callable(myTuto::PackageDeclaration.__init__)


def test_mytuto::packagedeclaration_constructor_args():
    sig = inspect.signature(myTuto::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mytuto::packagedeclaration_has_name():
    assert hasattr(myTuto::PackageDeclaration, "name")
    descriptor = None
    for klass in myTuto::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mytuto::abstractelement_is_not_abstract():
    assert not inspect.isabstract(myTuto::AbstractElement)


def test_mytuto::abstractelement_constructor_exists():
    assert callable(myTuto::AbstractElement.__init__)


def test_mytuto::abstractelement_constructor_args():
    sig = inspect.signature(myTuto::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_mytuto::mytuto_is_not_abstract():
    assert not inspect.isabstract(myTuto::MyTuto)


def test_mytuto::mytuto_constructor_exists():
    assert callable(myTuto::MyTuto.__init__)


def test_mytuto::mytuto_constructor_args():
    sig = inspect.signature(myTuto::MyTuto.__init__)
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
myTuto::Feature_strategy = st.builds(
    myTuto::Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myTuto::Entity_strategy = st.builds(
    myTuto::Entity,
)
myTuto::DataType_strategy = st.builds(
    myTuto::DataType,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
myTuto::Import_strategy = st.builds(
    myTuto::Import,
    importedNameSpace=
        safe_text
)
myTuto::Type_strategy = st.builds(
    myTuto::Type,
    name=
        safe_text
)
myTuto::PackageDeclaration_strategy = st.builds(
    myTuto::PackageDeclaration,
    name=
        safe_text
)
myTuto::AbstractElement_strategy = st.builds(
    myTuto::AbstractElement,
)
myTuto::MyTuto_strategy = st.builds(
    myTuto::MyTuto,
)

@given(instance=myTuto::Feature_strategy)
@settings(max_examples=50)
def test_mytuto::feature_instantiation(instance):
    assert isinstance(instance, myTuto::Feature)

@given(instance=myTuto::Feature_strategy)
def test_mytuto::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=myTuto::Feature_strategy)
def test_mytuto::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=myTuto::Feature_strategy)
def test_mytuto::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myTuto::Feature_strategy)
def test_mytuto::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myTuto::Entity_strategy)
@settings(max_examples=50)
def test_mytuto::entity_instantiation(instance):
    assert isinstance(instance, myTuto::Entity)

@given(instance=myTuto::DataType_strategy)
@settings(max_examples=50)
def test_mytuto::datatype_instantiation(instance):
    assert isinstance(instance, myTuto::DataType)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=myTuto::Import_strategy)
@settings(max_examples=50)
def test_mytuto::import_instantiation(instance):
    assert isinstance(instance, myTuto::Import)

@given(instance=myTuto::Import_strategy)
def test_mytuto::import_importedNameSpace_type(instance):
    assert isinstance(instance.importedNameSpace, str)


@given(instance=myTuto::Import_strategy)
def test_mytuto::import_importedNameSpace_setter(instance):
    original = instance.importedNameSpace
    instance.importedNameSpace = original
    assert instance.importedNameSpace == original

@given(instance=myTuto::Type_strategy)
@settings(max_examples=50)
def test_mytuto::type_instantiation(instance):
    assert isinstance(instance, myTuto::Type)

@given(instance=myTuto::Type_strategy)
def test_mytuto::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myTuto::Type_strategy)
def test_mytuto::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myTuto::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_mytuto::packagedeclaration_instantiation(instance):
    assert isinstance(instance, myTuto::PackageDeclaration)

@given(instance=myTuto::PackageDeclaration_strategy)
def test_mytuto::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myTuto::PackageDeclaration_strategy)
def test_mytuto::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myTuto::AbstractElement_strategy)
@settings(max_examples=50)
def test_mytuto::abstractelement_instantiation(instance):
    assert isinstance(instance, myTuto::AbstractElement)

@given(instance=myTuto::MyTuto_strategy)
@settings(max_examples=50)
def test_mytuto::mytuto_instantiation(instance):
    assert isinstance(instance, myTuto::MyTuto)
