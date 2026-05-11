import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractElement,
    domainmodel::Import,
    domainmodel::Type,
    domainmodel::PackageDeclaration,
    domainmodel::AbstractElement,
    domainmodel::Domainmodel,
    domainmodel::Method,
    domainmodel::Feature,
    Type,
    domainmodel::Entity,
    domainmodel::DataType,
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



def test_domainmodel::import_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Import)


def test_domainmodel::import_constructor_exists():
    assert callable(domainmodel::Import.__init__)


def test_domainmodel::import_constructor_args():
    sig = inspect.signature(domainmodel::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_domainmodel::import_has_importedNamespace():
    assert hasattr(domainmodel::Import, "importedNamespace")
    descriptor = None
    for klass in domainmodel::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::type_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Type)


def test_domainmodel::type_constructor_exists():
    assert callable(domainmodel::Type.__init__)


def test_domainmodel::type_constructor_args():
    sig = inspect.signature(domainmodel::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel::type_has_name():
    assert hasattr(domainmodel::Type, "name")
    descriptor = None
    for klass in domainmodel::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(domainmodel::PackageDeclaration)


def test_domainmodel::packagedeclaration_constructor_exists():
    assert callable(domainmodel::PackageDeclaration.__init__)


def test_domainmodel::packagedeclaration_constructor_args():
    sig = inspect.signature(domainmodel::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel::packagedeclaration_has_name():
    assert hasattr(domainmodel::PackageDeclaration, "name")
    descriptor = None
    for klass in domainmodel::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::abstractelement_is_not_abstract():
    assert not inspect.isabstract(domainmodel::AbstractElement)


def test_domainmodel::abstractelement_constructor_exists():
    assert callable(domainmodel::AbstractElement.__init__)


def test_domainmodel::abstractelement_constructor_args():
    sig = inspect.signature(domainmodel::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::domainmodel_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Domainmodel)


def test_domainmodel::domainmodel_constructor_exists():
    assert callable(domainmodel::Domainmodel.__init__)


def test_domainmodel::domainmodel_constructor_args():
    sig = inspect.signature(domainmodel::Domainmodel.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::method_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Method)


def test_domainmodel::method_constructor_exists():
    assert callable(domainmodel::Method.__init__)


def test_domainmodel::method_constructor_args():
    sig = inspect.signature(domainmodel::Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_domainmodel::method_has_name():
    assert hasattr(domainmodel::Method, "name")
    descriptor = None
    for klass in domainmodel::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel::method_has_body():
    assert hasattr(domainmodel::Method, "body")
    descriptor = None
    for klass in domainmodel::Method.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::feature_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Feature)


def test_domainmodel::feature_constructor_exists():
    assert callable(domainmodel::Feature.__init__)


def test_domainmodel::feature_constructor_args():
    sig = inspect.signature(domainmodel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel::feature_has_many():
    assert hasattr(domainmodel::Feature, "many")
    descriptor = None
    for klass in domainmodel::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel::feature_has_value():
    assert hasattr(domainmodel::Feature, "value")
    descriptor = None
    for klass in domainmodel::Feature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel::feature_has_name():
    assert hasattr(domainmodel::Feature, "name")
    descriptor = None
    for klass in domainmodel::Feature.__mro__:
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
    assert not inspect.isabstract(domainmodel::Entity)


def test_domainmodel::entity_constructor_exists():
    assert callable(domainmodel::Entity.__init__)


def test_domainmodel::entity_constructor_args():
    sig = inspect.signature(domainmodel::Entity.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::datatype_is_not_abstract():
    assert not inspect.isabstract(domainmodel::DataType)


def test_domainmodel::datatype_constructor_exists():
    assert callable(domainmodel::DataType.__init__)


def test_domainmodel::datatype_constructor_args():
    sig = inspect.signature(domainmodel::DataType.__init__)
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
AbstractElement_strategy = st.builds(
    AbstractElement,
)
domainmodel::Import_strategy = st.builds(
    domainmodel::Import,
    importedNamespace=
        safe_text
)
domainmodel::Type_strategy = st.builds(
    domainmodel::Type,
    name=
        safe_text
)
domainmodel::PackageDeclaration_strategy = st.builds(
    domainmodel::PackageDeclaration,
    name=
        safe_text
)
domainmodel::AbstractElement_strategy = st.builds(
    domainmodel::AbstractElement,
)
domainmodel::Domainmodel_strategy = st.builds(
    domainmodel::Domainmodel,
)
domainmodel::Method_strategy = st.builds(
    domainmodel::Method,
    name=
        safe_text,
    body=
        safe_text
)
domainmodel::Feature_strategy = st.builds(
    domainmodel::Feature,
    many=
        st.booleans(),
    value=
        safe_text,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
domainmodel::Entity_strategy = st.builds(
    domainmodel::Entity,
)
domainmodel::DataType_strategy = st.builds(
    domainmodel::DataType,
)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=domainmodel::Import_strategy)
@settings(max_examples=50)
def test_domainmodel::import_instantiation(instance):
    assert isinstance(instance, domainmodel::Import)

@given(instance=domainmodel::Import_strategy)
def test_domainmodel::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=domainmodel::Import_strategy)
def test_domainmodel::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=domainmodel::Type_strategy)
@settings(max_examples=50)
def test_domainmodel::type_instantiation(instance):
    assert isinstance(instance, domainmodel::Type)

@given(instance=domainmodel::Type_strategy)
def test_domainmodel::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainmodel::Type_strategy)
def test_domainmodel::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_domainmodel::packagedeclaration_instantiation(instance):
    assert isinstance(instance, domainmodel::PackageDeclaration)

@given(instance=domainmodel::PackageDeclaration_strategy)
def test_domainmodel::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainmodel::PackageDeclaration_strategy)
def test_domainmodel::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel::AbstractElement_strategy)
@settings(max_examples=50)
def test_domainmodel::abstractelement_instantiation(instance):
    assert isinstance(instance, domainmodel::AbstractElement)

@given(instance=domainmodel::Domainmodel_strategy)
@settings(max_examples=50)
def test_domainmodel::domainmodel_instantiation(instance):
    assert isinstance(instance, domainmodel::Domainmodel)

@given(instance=domainmodel::Method_strategy)
@settings(max_examples=50)
def test_domainmodel::method_instantiation(instance):
    assert isinstance(instance, domainmodel::Method)

@given(instance=domainmodel::Method_strategy)
def test_domainmodel::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainmodel::Method_strategy)
def test_domainmodel::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel::Method_strategy)
def test_domainmodel::method_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=domainmodel::Method_strategy)
def test_domainmodel::method_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=domainmodel::Feature_strategy)
@settings(max_examples=50)
def test_domainmodel::feature_instantiation(instance):
    assert isinstance(instance, domainmodel::Feature)

@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=domainmodel::Entity_strategy)
@settings(max_examples=50)
def test_domainmodel::entity_instantiation(instance):
    assert isinstance(instance, domainmodel::Entity)

@given(instance=domainmodel::DataType_strategy)
@settings(max_examples=50)
def test_domainmodel::datatype_instantiation(instance):
    assert isinstance(instance, domainmodel::DataType)
