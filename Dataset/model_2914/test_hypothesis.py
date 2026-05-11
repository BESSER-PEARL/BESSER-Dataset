import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Feature,
    AbstractElement,
    myDsl::PackageDeclaration,
    myDsl::AbstractElement,
    myDsl::Model,
    myDsl::Import,
    Type,
    myDsl::Entity,
    myDsl::DataType,
    myDsl::Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::feature_is_not_abstract():
    assert not inspect.isabstract(myDsl::Feature)


def test_mydsl::feature_constructor_exists():
    assert callable(myDsl::Feature.__init__)


def test_mydsl::feature_constructor_args():
    sig = inspect.signature(myDsl::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::feature_has_many():
    assert hasattr(myDsl::Feature, "many")
    descriptor = None
    for klass in myDsl::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::feature_has_name():
    assert hasattr(myDsl::Feature, "name")
    descriptor = None
    for klass in myDsl::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::PackageDeclaration)


def test_mydsl::packagedeclaration_constructor_exists():
    assert callable(myDsl::PackageDeclaration.__init__)


def test_mydsl::packagedeclaration_constructor_args():
    sig = inspect.signature(myDsl::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::packagedeclaration_has_name():
    assert hasattr(myDsl::PackageDeclaration, "name")
    descriptor = None
    for klass in myDsl::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::abstractelement_is_not_abstract():
    assert not inspect.isabstract(myDsl::AbstractElement)


def test_mydsl::abstractelement_constructor_exists():
    assert callable(myDsl::AbstractElement.__init__)


def test_mydsl::abstractelement_constructor_args():
    sig = inspect.signature(myDsl::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
    params = list(sig.parameters.keys())



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



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::entity_is_not_abstract():
    assert not inspect.isabstract(myDsl::Entity)


def test_mydsl::entity_constructor_exists():
    assert callable(myDsl::Entity.__init__)


def test_mydsl::entity_constructor_args():
    sig = inspect.signature(myDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::datatype_is_not_abstract():
    assert not inspect.isabstract(myDsl::DataType)


def test_mydsl::datatype_constructor_exists():
    assert callable(myDsl::DataType.__init__)


def test_mydsl::datatype_constructor_args():
    sig = inspect.signature(myDsl::DataType.__init__)
    params = list(sig.parameters.keys())



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
myDsl::Feature_strategy = st.builds(
    myDsl::Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
myDsl::PackageDeclaration_strategy = st.builds(
    myDsl::PackageDeclaration,
    name=
        safe_text
)
myDsl::AbstractElement_strategy = st.builds(
    myDsl::AbstractElement,
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)
myDsl::Import_strategy = st.builds(
    myDsl::Import,
    importedNamespace=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDsl::Entity_strategy = st.builds(
    myDsl::Entity,
)
myDsl::DataType_strategy = st.builds(
    myDsl::DataType,
)
myDsl::Type_strategy = st.builds(
    myDsl::Type,
    name=
        safe_text
)

@given(instance=myDsl::Feature_strategy)
@settings(max_examples=50)
def test_mydsl::feature_instantiation(instance):
    assert isinstance(instance, myDsl::Feature)

@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=myDsl::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_mydsl::packagedeclaration_instantiation(instance):
    assert isinstance(instance, myDsl::PackageDeclaration)

@given(instance=myDsl::PackageDeclaration_strategy)
def test_mydsl::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::PackageDeclaration_strategy)
def test_mydsl::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::AbstractElement_strategy)
@settings(max_examples=50)
def test_mydsl::abstractelement_instantiation(instance):
    assert isinstance(instance, myDsl::AbstractElement)

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)

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

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl::Entity_strategy)
@settings(max_examples=50)
def test_mydsl::entity_instantiation(instance):
    assert isinstance(instance, myDsl::Entity)

@given(instance=myDsl::DataType_strategy)
@settings(max_examples=50)
def test_mydsl::datatype_instantiation(instance):
    assert isinstance(instance, myDsl::DataType)

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
