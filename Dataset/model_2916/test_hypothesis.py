import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    domainModel::Feature,
    Type,
    domainModel::Entity,
    domainModel::DataType,
    AbstractElement,
    domainModel::Import,
    domainModel::Type,
    domainModel::PackageDeclaration,
    domainModel::AbstractElement,
    domainModel::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_domainmodel::feature_is_not_abstract():
    assert not inspect.isabstract(domainModel::Feature)


def test_domainmodel::feature_constructor_exists():
    assert callable(domainModel::Feature.__init__)


def test_domainmodel::feature_constructor_args():
    sig = inspect.signature(domainModel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel::feature_has_many():
    assert hasattr(domainModel::Feature, "many")
    descriptor = None
    for klass in domainModel::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel::feature_has_name():
    assert hasattr(domainModel::Feature, "name")
    descriptor = None
    for klass in domainModel::Feature.__mro__:
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



def test_domainmodel::entity_is_not_abstract():
    assert not inspect.isabstract(domainModel::Entity)


def test_domainmodel::entity_constructor_exists():
    assert callable(domainModel::Entity.__init__)


def test_domainmodel::entity_constructor_args():
    sig = inspect.signature(domainModel::Entity.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::datatype_is_not_abstract():
    assert not inspect.isabstract(domainModel::DataType)


def test_domainmodel::datatype_constructor_exists():
    assert callable(domainModel::DataType.__init__)


def test_domainmodel::datatype_constructor_args():
    sig = inspect.signature(domainModel::DataType.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::import_is_not_abstract():
    assert not inspect.isabstract(domainModel::Import)


def test_domainmodel::import_constructor_exists():
    assert callable(domainModel::Import.__init__)


def test_domainmodel::import_constructor_args():
    sig = inspect.signature(domainModel::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_domainmodel::import_has_importedNamespace():
    assert hasattr(domainModel::Import, "importedNamespace")
    descriptor = None
    for klass in domainModel::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::type_is_not_abstract():
    assert not inspect.isabstract(domainModel::Type)


def test_domainmodel::type_constructor_exists():
    assert callable(domainModel::Type.__init__)


def test_domainmodel::type_constructor_args():
    sig = inspect.signature(domainModel::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel::type_has_name():
    assert hasattr(domainModel::Type, "name")
    descriptor = None
    for klass in domainModel::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(domainModel::PackageDeclaration)


def test_domainmodel::packagedeclaration_constructor_exists():
    assert callable(domainModel::PackageDeclaration.__init__)


def test_domainmodel::packagedeclaration_constructor_args():
    sig = inspect.signature(domainModel::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel::packagedeclaration_has_name():
    assert hasattr(domainModel::PackageDeclaration, "name")
    descriptor = None
    for klass in domainModel::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::abstractelement_is_not_abstract():
    assert not inspect.isabstract(domainModel::AbstractElement)


def test_domainmodel::abstractelement_constructor_exists():
    assert callable(domainModel::AbstractElement.__init__)


def test_domainmodel::abstractelement_constructor_args():
    sig = inspect.signature(domainModel::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::model_is_not_abstract():
    assert not inspect.isabstract(domainModel::Model)


def test_domainmodel::model_constructor_exists():
    assert callable(domainModel::Model.__init__)


def test_domainmodel::model_constructor_args():
    sig = inspect.signature(domainModel::Model.__init__)
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
domainModel::Feature_strategy = st.builds(
    domainModel::Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
domainModel::Entity_strategy = st.builds(
    domainModel::Entity,
)
domainModel::DataType_strategy = st.builds(
    domainModel::DataType,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
domainModel::Import_strategy = st.builds(
    domainModel::Import,
    importedNamespace=
        safe_text
)
domainModel::Type_strategy = st.builds(
    domainModel::Type,
    name=
        safe_text
)
domainModel::PackageDeclaration_strategy = st.builds(
    domainModel::PackageDeclaration,
    name=
        safe_text
)
domainModel::AbstractElement_strategy = st.builds(
    domainModel::AbstractElement,
)
domainModel::Model_strategy = st.builds(
    domainModel::Model,
)

@given(instance=domainModel::Feature_strategy)
@settings(max_examples=50)
def test_domainmodel::feature_instantiation(instance):
    assert isinstance(instance, domainModel::Feature)

@given(instance=domainModel::Feature_strategy)
def test_domainmodel::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=domainModel::Feature_strategy)
def test_domainmodel::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=domainModel::Feature_strategy)
def test_domainmodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainModel::Feature_strategy)
def test_domainmodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=domainModel::Entity_strategy)
@settings(max_examples=50)
def test_domainmodel::entity_instantiation(instance):
    assert isinstance(instance, domainModel::Entity)

@given(instance=domainModel::DataType_strategy)
@settings(max_examples=50)
def test_domainmodel::datatype_instantiation(instance):
    assert isinstance(instance, domainModel::DataType)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=domainModel::Import_strategy)
@settings(max_examples=50)
def test_domainmodel::import_instantiation(instance):
    assert isinstance(instance, domainModel::Import)

@given(instance=domainModel::Import_strategy)
def test_domainmodel::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=domainModel::Import_strategy)
def test_domainmodel::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=domainModel::Type_strategy)
@settings(max_examples=50)
def test_domainmodel::type_instantiation(instance):
    assert isinstance(instance, domainModel::Type)

@given(instance=domainModel::Type_strategy)
def test_domainmodel::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainModel::Type_strategy)
def test_domainmodel::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainModel::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_domainmodel::packagedeclaration_instantiation(instance):
    assert isinstance(instance, domainModel::PackageDeclaration)

@given(instance=domainModel::PackageDeclaration_strategy)
def test_domainmodel::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainModel::PackageDeclaration_strategy)
def test_domainmodel::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainModel::AbstractElement_strategy)
@settings(max_examples=50)
def test_domainmodel::abstractelement_instantiation(instance):
    assert isinstance(instance, domainModel::AbstractElement)

@given(instance=domainModel::Model_strategy)
@settings(max_examples=50)
def test_domainmodel::model_instantiation(instance):
    assert isinstance(instance, domainModel::Model)
