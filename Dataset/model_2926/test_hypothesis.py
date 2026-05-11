import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractElement,
    wh::PackageDeclaration,
    wh::AbstractElement,
    wh::Wh,
    wh::Feature,
    Type,
    wh::Entity,
    wh::DataType,
    wh::Type,
    wh::Import,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_wh::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(wh::PackageDeclaration)


def test_wh::packagedeclaration_constructor_exists():
    assert callable(wh::PackageDeclaration.__init__)


def test_wh::packagedeclaration_constructor_args():
    sig = inspect.signature(wh::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh::packagedeclaration_has_name():
    assert hasattr(wh::PackageDeclaration, "name")
    descriptor = None
    for klass in wh::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh::abstractelement_is_not_abstract():
    assert not inspect.isabstract(wh::AbstractElement)


def test_wh::abstractelement_constructor_exists():
    assert callable(wh::AbstractElement.__init__)


def test_wh::abstractelement_constructor_args():
    sig = inspect.signature(wh::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_wh::wh_is_not_abstract():
    assert not inspect.isabstract(wh::Wh)


def test_wh::wh_constructor_exists():
    assert callable(wh::Wh.__init__)


def test_wh::wh_constructor_args():
    sig = inspect.signature(wh::Wh.__init__)
    params = list(sig.parameters.keys())



def test_wh::feature_is_not_abstract():
    assert not inspect.isabstract(wh::Feature)


def test_wh::feature_constructor_exists():
    assert callable(wh::Feature.__init__)


def test_wh::feature_constructor_args():
    sig = inspect.signature(wh::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_wh::feature_has_many():
    assert hasattr(wh::Feature, "many")
    descriptor = None
    for klass in wh::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_wh::feature_has_name():
    assert hasattr(wh::Feature, "name")
    descriptor = None
    for klass in wh::Feature.__mro__:
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



def test_wh::entity_is_not_abstract():
    assert not inspect.isabstract(wh::Entity)


def test_wh::entity_constructor_exists():
    assert callable(wh::Entity.__init__)


def test_wh::entity_constructor_args():
    sig = inspect.signature(wh::Entity.__init__)
    params = list(sig.parameters.keys())



def test_wh::datatype_is_not_abstract():
    assert not inspect.isabstract(wh::DataType)


def test_wh::datatype_constructor_exists():
    assert callable(wh::DataType.__init__)


def test_wh::datatype_constructor_args():
    sig = inspect.signature(wh::DataType.__init__)
    params = list(sig.parameters.keys())



def test_wh::type_is_not_abstract():
    assert not inspect.isabstract(wh::Type)


def test_wh::type_constructor_exists():
    assert callable(wh::Type.__init__)


def test_wh::type_constructor_args():
    sig = inspect.signature(wh::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh::type_has_name():
    assert hasattr(wh::Type, "name")
    descriptor = None
    for klass in wh::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh::import_is_not_abstract():
    assert not inspect.isabstract(wh::Import)


def test_wh::import_constructor_exists():
    assert callable(wh::Import.__init__)


def test_wh::import_constructor_args():
    sig = inspect.signature(wh::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_wh::import_has_importedNamespace():
    assert hasattr(wh::Import, "importedNamespace")
    descriptor = None
    for klass in wh::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
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
AbstractElement_strategy = st.builds(
    AbstractElement,
)
wh::PackageDeclaration_strategy = st.builds(
    wh::PackageDeclaration,
    name=
        safe_text
)
wh::AbstractElement_strategy = st.builds(
    wh::AbstractElement,
)
wh::Wh_strategy = st.builds(
    wh::Wh,
)
wh::Feature_strategy = st.builds(
    wh::Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
wh::Entity_strategy = st.builds(
    wh::Entity,
)
wh::DataType_strategy = st.builds(
    wh::DataType,
)
wh::Type_strategy = st.builds(
    wh::Type,
    name=
        safe_text
)
wh::Import_strategy = st.builds(
    wh::Import,
    importedNamespace=
        safe_text
)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=wh::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_wh::packagedeclaration_instantiation(instance):
    assert isinstance(instance, wh::PackageDeclaration)

@given(instance=wh::PackageDeclaration_strategy)
def test_wh::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wh::PackageDeclaration_strategy)
def test_wh::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh::AbstractElement_strategy)
@settings(max_examples=50)
def test_wh::abstractelement_instantiation(instance):
    assert isinstance(instance, wh::AbstractElement)

@given(instance=wh::Wh_strategy)
@settings(max_examples=50)
def test_wh::wh_instantiation(instance):
    assert isinstance(instance, wh::Wh)

@given(instance=wh::Feature_strategy)
@settings(max_examples=50)
def test_wh::feature_instantiation(instance):
    assert isinstance(instance, wh::Feature)

@given(instance=wh::Feature_strategy)
def test_wh::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=wh::Feature_strategy)
def test_wh::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=wh::Feature_strategy)
def test_wh::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wh::Feature_strategy)
def test_wh::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=wh::Entity_strategy)
@settings(max_examples=50)
def test_wh::entity_instantiation(instance):
    assert isinstance(instance, wh::Entity)

@given(instance=wh::DataType_strategy)
@settings(max_examples=50)
def test_wh::datatype_instantiation(instance):
    assert isinstance(instance, wh::DataType)

@given(instance=wh::Type_strategy)
@settings(max_examples=50)
def test_wh::type_instantiation(instance):
    assert isinstance(instance, wh::Type)

@given(instance=wh::Type_strategy)
def test_wh::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wh::Type_strategy)
def test_wh::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh::Import_strategy)
@settings(max_examples=50)
def test_wh::import_instantiation(instance):
    assert isinstance(instance, wh::Import)

@given(instance=wh::Import_strategy)
def test_wh::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=wh::Import_strategy)
def test_wh::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original
