import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ling::Feature,
    Type,
    ling::Entity,
    ling::DataType,
    AbstractElement,
    ling::Type,
    ling::Import,
    ling::PackageDeclaration,
    ling::AbstractElement,
    ling::Domainmodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ling::feature_is_not_abstract():
    assert not inspect.isabstract(ling::Feature)


def test_ling::feature_constructor_exists():
    assert callable(ling::Feature.__init__)


def test_ling::feature_constructor_args():
    sig = inspect.signature(ling::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_ling::feature_has_many():
    assert hasattr(ling::Feature, "many")
    descriptor = None
    for klass in ling::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_ling::feature_has_name():
    assert hasattr(ling::Feature, "name")
    descriptor = None
    for klass in ling::Feature.__mro__:
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



def test_ling::entity_is_not_abstract():
    assert not inspect.isabstract(ling::Entity)


def test_ling::entity_constructor_exists():
    assert callable(ling::Entity.__init__)


def test_ling::entity_constructor_args():
    sig = inspect.signature(ling::Entity.__init__)
    params = list(sig.parameters.keys())



def test_ling::datatype_is_not_abstract():
    assert not inspect.isabstract(ling::DataType)


def test_ling::datatype_constructor_exists():
    assert callable(ling::DataType.__init__)


def test_ling::datatype_constructor_args():
    sig = inspect.signature(ling::DataType.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_ling::type_is_not_abstract():
    assert not inspect.isabstract(ling::Type)


def test_ling::type_constructor_exists():
    assert callable(ling::Type.__init__)


def test_ling::type_constructor_args():
    sig = inspect.signature(ling::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ling::type_has_name():
    assert hasattr(ling::Type, "name")
    descriptor = None
    for klass in ling::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ling::import_is_not_abstract():
    assert not inspect.isabstract(ling::Import)


def test_ling::import_constructor_exists():
    assert callable(ling::Import.__init__)


def test_ling::import_constructor_args():
    sig = inspect.signature(ling::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_ling::import_has_importedNamespace():
    assert hasattr(ling::Import, "importedNamespace")
    descriptor = None
    for klass in ling::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_ling::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(ling::PackageDeclaration)


def test_ling::packagedeclaration_constructor_exists():
    assert callable(ling::PackageDeclaration.__init__)


def test_ling::packagedeclaration_constructor_args():
    sig = inspect.signature(ling::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ling::packagedeclaration_has_name():
    assert hasattr(ling::PackageDeclaration, "name")
    descriptor = None
    for klass in ling::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ling::abstractelement_is_not_abstract():
    assert not inspect.isabstract(ling::AbstractElement)


def test_ling::abstractelement_constructor_exists():
    assert callable(ling::AbstractElement.__init__)


def test_ling::abstractelement_constructor_args():
    sig = inspect.signature(ling::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_ling::domainmodel_is_not_abstract():
    assert not inspect.isabstract(ling::Domainmodel)


def test_ling::domainmodel_constructor_exists():
    assert callable(ling::Domainmodel.__init__)


def test_ling::domainmodel_constructor_args():
    sig = inspect.signature(ling::Domainmodel.__init__)
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
ling::Feature_strategy = st.builds(
    ling::Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
ling::Entity_strategy = st.builds(
    ling::Entity,
)
ling::DataType_strategy = st.builds(
    ling::DataType,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
ling::Type_strategy = st.builds(
    ling::Type,
    name=
        safe_text
)
ling::Import_strategy = st.builds(
    ling::Import,
    importedNamespace=
        safe_text
)
ling::PackageDeclaration_strategy = st.builds(
    ling::PackageDeclaration,
    name=
        safe_text
)
ling::AbstractElement_strategy = st.builds(
    ling::AbstractElement,
)
ling::Domainmodel_strategy = st.builds(
    ling::Domainmodel,
)

@given(instance=ling::Feature_strategy)
@settings(max_examples=50)
def test_ling::feature_instantiation(instance):
    assert isinstance(instance, ling::Feature)

@given(instance=ling::Feature_strategy)
def test_ling::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=ling::Feature_strategy)
def test_ling::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=ling::Feature_strategy)
def test_ling::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ling::Feature_strategy)
def test_ling::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ling::Entity_strategy)
@settings(max_examples=50)
def test_ling::entity_instantiation(instance):
    assert isinstance(instance, ling::Entity)

@given(instance=ling::DataType_strategy)
@settings(max_examples=50)
def test_ling::datatype_instantiation(instance):
    assert isinstance(instance, ling::DataType)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=ling::Type_strategy)
@settings(max_examples=50)
def test_ling::type_instantiation(instance):
    assert isinstance(instance, ling::Type)

@given(instance=ling::Type_strategy)
def test_ling::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ling::Type_strategy)
def test_ling::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ling::Import_strategy)
@settings(max_examples=50)
def test_ling::import_instantiation(instance):
    assert isinstance(instance, ling::Import)

@given(instance=ling::Import_strategy)
def test_ling::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=ling::Import_strategy)
def test_ling::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=ling::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_ling::packagedeclaration_instantiation(instance):
    assert isinstance(instance, ling::PackageDeclaration)

@given(instance=ling::PackageDeclaration_strategy)
def test_ling::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ling::PackageDeclaration_strategy)
def test_ling::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ling::AbstractElement_strategy)
@settings(max_examples=50)
def test_ling::abstractelement_instantiation(instance):
    assert isinstance(instance, ling::AbstractElement)

@given(instance=ling::Domainmodel_strategy)
@settings(max_examples=50)
def test_ling::domainmodel_instantiation(instance):
    assert isinstance(instance, ling::Domainmodel)
