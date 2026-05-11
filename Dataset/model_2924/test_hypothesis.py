import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    aGES::Feature,
    Type,
    aGES::Entity,
    aGES::DataType,
    AbstractElement,
    aGES::Import,
    aGES::Type,
    aGES::PackageDeclaration,
    aGES::AbstractElement,
    aGES::Domainmodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ages::feature_is_not_abstract():
    assert not inspect.isabstract(aGES::Feature)


def test_ages::feature_constructor_exists():
    assert callable(aGES::Feature.__init__)


def test_ages::feature_constructor_args():
    sig = inspect.signature(aGES::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_ages::feature_has_many():
    assert hasattr(aGES::Feature, "many")
    descriptor = None
    for klass in aGES::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_ages::feature_has_name():
    assert hasattr(aGES::Feature, "name")
    descriptor = None
    for klass in aGES::Feature.__mro__:
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



def test_ages::entity_is_not_abstract():
    assert not inspect.isabstract(aGES::Entity)


def test_ages::entity_constructor_exists():
    assert callable(aGES::Entity.__init__)


def test_ages::entity_constructor_args():
    sig = inspect.signature(aGES::Entity.__init__)
    params = list(sig.parameters.keys())



def test_ages::datatype_is_not_abstract():
    assert not inspect.isabstract(aGES::DataType)


def test_ages::datatype_constructor_exists():
    assert callable(aGES::DataType.__init__)


def test_ages::datatype_constructor_args():
    sig = inspect.signature(aGES::DataType.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_ages::import_is_not_abstract():
    assert not inspect.isabstract(aGES::Import)


def test_ages::import_constructor_exists():
    assert callable(aGES::Import.__init__)


def test_ages::import_constructor_args():
    sig = inspect.signature(aGES::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_ages::import_has_importedNamespace():
    assert hasattr(aGES::Import, "importedNamespace")
    descriptor = None
    for klass in aGES::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_ages::type_is_not_abstract():
    assert not inspect.isabstract(aGES::Type)


def test_ages::type_constructor_exists():
    assert callable(aGES::Type.__init__)


def test_ages::type_constructor_args():
    sig = inspect.signature(aGES::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ages::type_has_name():
    assert hasattr(aGES::Type, "name")
    descriptor = None
    for klass in aGES::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ages::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(aGES::PackageDeclaration)


def test_ages::packagedeclaration_constructor_exists():
    assert callable(aGES::PackageDeclaration.__init__)


def test_ages::packagedeclaration_constructor_args():
    sig = inspect.signature(aGES::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ages::packagedeclaration_has_name():
    assert hasattr(aGES::PackageDeclaration, "name")
    descriptor = None
    for klass in aGES::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ages::abstractelement_is_not_abstract():
    assert not inspect.isabstract(aGES::AbstractElement)


def test_ages::abstractelement_constructor_exists():
    assert callable(aGES::AbstractElement.__init__)


def test_ages::abstractelement_constructor_args():
    sig = inspect.signature(aGES::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_ages::domainmodel_is_not_abstract():
    assert not inspect.isabstract(aGES::Domainmodel)


def test_ages::domainmodel_constructor_exists():
    assert callable(aGES::Domainmodel.__init__)


def test_ages::domainmodel_constructor_args():
    sig = inspect.signature(aGES::Domainmodel.__init__)
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
aGES::Feature_strategy = st.builds(
    aGES::Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
aGES::Entity_strategy = st.builds(
    aGES::Entity,
)
aGES::DataType_strategy = st.builds(
    aGES::DataType,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
aGES::Import_strategy = st.builds(
    aGES::Import,
    importedNamespace=
        safe_text
)
aGES::Type_strategy = st.builds(
    aGES::Type,
    name=
        safe_text
)
aGES::PackageDeclaration_strategy = st.builds(
    aGES::PackageDeclaration,
    name=
        safe_text
)
aGES::AbstractElement_strategy = st.builds(
    aGES::AbstractElement,
)
aGES::Domainmodel_strategy = st.builds(
    aGES::Domainmodel,
)

@given(instance=aGES::Feature_strategy)
@settings(max_examples=50)
def test_ages::feature_instantiation(instance):
    assert isinstance(instance, aGES::Feature)

@given(instance=aGES::Feature_strategy)
def test_ages::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=aGES::Feature_strategy)
def test_ages::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=aGES::Feature_strategy)
def test_ages::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aGES::Feature_strategy)
def test_ages::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=aGES::Entity_strategy)
@settings(max_examples=50)
def test_ages::entity_instantiation(instance):
    assert isinstance(instance, aGES::Entity)

@given(instance=aGES::DataType_strategy)
@settings(max_examples=50)
def test_ages::datatype_instantiation(instance):
    assert isinstance(instance, aGES::DataType)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=aGES::Import_strategy)
@settings(max_examples=50)
def test_ages::import_instantiation(instance):
    assert isinstance(instance, aGES::Import)

@given(instance=aGES::Import_strategy)
def test_ages::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=aGES::Import_strategy)
def test_ages::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=aGES::Type_strategy)
@settings(max_examples=50)
def test_ages::type_instantiation(instance):
    assert isinstance(instance, aGES::Type)

@given(instance=aGES::Type_strategy)
def test_ages::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aGES::Type_strategy)
def test_ages::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aGES::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_ages::packagedeclaration_instantiation(instance):
    assert isinstance(instance, aGES::PackageDeclaration)

@given(instance=aGES::PackageDeclaration_strategy)
def test_ages::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aGES::PackageDeclaration_strategy)
def test_ages::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aGES::AbstractElement_strategy)
@settings(max_examples=50)
def test_ages::abstractelement_instantiation(instance):
    assert isinstance(instance, aGES::AbstractElement)

@given(instance=aGES::Domainmodel_strategy)
@settings(max_examples=50)
def test_ages::domainmodel_instantiation(instance):
    assert isinstance(instance, aGES::Domainmodel)
